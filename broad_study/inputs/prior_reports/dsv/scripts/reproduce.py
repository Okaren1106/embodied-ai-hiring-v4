#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Stage D package reproduction entry.

Verifies this package (release_checksums.json) and its locked inputs
(input_lock.json), then rebuilds every derived table and figure in an isolated
output directory and compares results byte for byte. Refuses to overwrite an
existing output directory and refuses to publish when any input drifted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent
STEPS = [
    "step1_coverage_cross_cooccurrence.py",
    "step2_responsibility_and_cases.py",
    "step3_company_and_K_comparison.py",
    "step4_sensitivity_ledger.py",
    "step5_deliverables.py",
    "step6_charts.py",
]
DOCS = ["REPORT.md", "METHODS.md", "README.md"]


def sha256(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while True:
            block = fh.read(chunk)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def resolve_base(run: Path) -> Path:
    """Input root recorded by step7; falls back to the run's parent layout."""
    lock = run / "input_lock.json"
    if lock.is_file():
        try:
            recorded = json.loads(lock.read_text(encoding="utf-8")).get("base_dir")
        except (OSError, json.JSONDecodeError):
            recorded = None
        if recorded:
            return Path(recorded)
    return run.parents[1]


def verify_package() -> dict:
    manifest = json.loads((RUN / "release_checksums.json").read_text(encoding="utf-8"))
    bad, missing = [], []
    for entry in manifest["files"]:
        path = RUN / entry["path"]
        if not path.is_file():
            missing.append(entry["path"])
            continue
        if sha256(path) != entry["sha256"]:
            bad.append(entry["path"])
    return {"checked": len(manifest["files"]), "mismatch": bad, "missing": missing}


def verify_inputs() -> dict:
    lock = json.loads((RUN / "input_lock.json").read_text(encoding="utf-8"))
    bad = []
    for name, meta in lock["inputs"].items():
        if "sha256" not in meta:
            continue
        path = Path(meta["path"])
        if not path.is_file() or sha256(path) != meta["sha256"]:
            bad.append({"input": name, "path": meta["path"]})
    return {"checked": sum(1 for m in lock["inputs"].values() if "sha256" in m), "drift": bad}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--plot-deps", default="")
    ap.add_argument("--skip-verify", action="store_true")
    args = ap.parse_args()

    out = Path(args.output).resolve()
    if out.exists():
        print(json.dumps({"status": "REFUSED", "reason": "output directory already exists",
                          "output": str(out)}, ensure_ascii=False))
        return 2

    if not args.skip_verify:
        pkg = verify_package()
        if pkg["mismatch"] or pkg["missing"]:
            print(json.dumps({"status": "REFUSED", "reason": "package checksum mismatch",
                              "detail": pkg}, ensure_ascii=False))
            return 3
        inp = verify_inputs()
        if inp["drift"]:
            print(json.dumps({"status": "REFUSED", "reason": "input drift", "detail": inp},
                             ensure_ascii=False))
            return 4
    else:
        pkg = inp = {"skipped": True}

    (out / "scripts").mkdir(parents=True)
    for name in STEPS + ["step7_package.py", "reproduce.py"]:
        shutil.copy2(RUN / "scripts" / name, out / "scripts" / name)

    env = dict(**__import__("os").environ)
    env["STAGE_D_BASE"] = str(resolve_base(RUN))
    if args.plot_deps:
        env["PYTHONPATH"] = args.plot_deps + (";" + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")

    for name in STEPS:
        proc = subprocess.run([sys.executable, "-X", "utf8", str(out / "scripts" / name)],
                              cwd=str(out), env=env)
        if proc.returncode != 0:
            print(json.dumps({"status": "FAILED", "step": name, "exit": proc.returncode},
                             ensure_ascii=False))
            return 5

    for doc in DOCS:
        src = RUN / doc
        if src.is_file():
            shutil.copy2(src, out / doc)

    proc = subprocess.run([sys.executable, "-X", "utf8", str(out / "scripts" / "step7_package.py")],
                          cwd=str(out), env=env)
    if proc.returncode != 0:
        print(json.dumps({"status": "FAILED", "step": "step7_package.py", "exit": proc.returncode},
                         ensure_ascii=False))
        return 5

    diffs, compared = [], 0
    for folder, pattern in (("tables", "*.csv"), ("charts", "*")):
        for src in sorted((RUN / folder).glob(pattern)):
            if not src.is_file():
                continue
            dst = out / folder / src.name
            compared += 1
            if not dst.is_file():
                diffs.append(f"{folder}/{src.name}: missing")
            elif sha256(src) != sha256(dst):
                diffs.append(f"{folder}/{src.name}: bytes differ")
    for name in ("cases/case_selection.json", "figure_manifest.json"):
        src, dst = RUN / name, out / name
        compared += 1
        if not dst.is_file():
            diffs.append(f"{name}: missing")
        elif sha256(src) != sha256(dst):
            diffs.append(f"{name}: bytes differ")

    result = {
        "status": "PASS" if not diffs else "FAILED",
        "output": str(out),
        "package_verify": pkg,
        "input_verify": inp,
        "compared_files": compared,
        "differences": diffs,
        "packaging": "STAGE_D_V1_REPRODUCE",
    }
    print(json.dumps(result, ensure_ascii=False))
    return 0 if not diffs else 6


if __name__ == "__main__":
    raise SystemExit(main())
