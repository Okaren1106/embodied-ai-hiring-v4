"""Stage B repair / step 10: recompute output and release checksums.

Two documents, with the input lock as a third:

  output_checksums.json  - derived tables, work artefacts, cards, overview, scripts
  release_checksums.json - everything above plus the manifest and the reports;
                           never itself and never the manifest's own size or hash
  work/input_lock.json   - the locked input set (produced by s01)

The product manifest records the digest of the verification record it was built
with, so a manifest cannot be paired with a different verification run later.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import RUN, WORK, sha256_bytes, sha256_file  # noqa: E402

SKIP_DIRS = {"__pycache__"}


def walk():
    for root, dirs, files in os.walk(RUN):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in sorted(files):
            full = os.path.join(root, f)
            yield os.path.relpath(full, RUN).replace("\\", "/")


def entry(path: str) -> dict:
    return {"bytes": os.path.getsize(os.path.join(RUN, path)),
            "sha256": sha256_file(os.path.join(RUN, path))}


def main() -> int:
    ver = json.load(open(os.path.join(RUN, "verification.json"), encoding="utf-8"))
    lock = json.load(open(os.path.join(WORK, "input_lock.json"), encoding="utf-8"))
    bound = {
        "verification_digest": ver.get("verification_digest", ""),
        "input_root_digest": lock.get("input_root_digest", ""),
        "code_digest": lock.get("code_digest", ""),
        "run_id": lock.get("run_id", ""),
    }
    outputs = {}
    out_exclude = {"output_checksums.json", "release_checksums.json", "analysis_manifest.json"}
    for p in walk():
        if p in out_exclude or p.startswith("work/"):
            continue
        outputs[p] = entry(p)
    work_files = {p: entry(p) for p in walk() if p.startswith("work/")
                  and not p.endswith("input_lock.json")}
    out_doc = {
        "stage": "B-repair",
        "scope": "derived tables, company cards, overview, scripts and saved evidence text",
        "excludes": ["output_checksums.json (self)", "release_checksums.json",
                     "analysis_manifest.json", "work/ (listed separately as work_files)"],
        "bound_to": bound,
        "n_files": len(outputs),
        "files": outputs,
        "n_work_files": len(work_files),
        "work_files": work_files,
    }
    with open(os.path.join(RUN, "output_checksums.json"), "w", encoding="utf-8") as fh:
        json.dump(out_doc, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    release = {}
    for p in walk():
        if p == "release_checksums.json":
            continue
        release[p] = entry(p)
    rel_doc = {
        "stage": "B-repair",
        "scope": ("final manifest, verification record, all data tables, scripts, saved evidence, "
                  "work artefacts and reports"),
        "excludes": ["release_checksums.json (self)"],
        "bound_to": bound,
        "manifest_self_hash_omitted": True,
        "n_files": len(release),
        "files": release,
    }
    with open(os.path.join(RUN, "release_checksums.json"), "w", encoding="utf-8") as fh:
        json.dump(rel_doc, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print(json.dumps({
        "output_checksums_files": out_doc["n_files"],
        "work_files": out_doc["n_work_files"],
        "release_checksums_files": rel_doc["n_files"],
        "bound_to": bound,
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
