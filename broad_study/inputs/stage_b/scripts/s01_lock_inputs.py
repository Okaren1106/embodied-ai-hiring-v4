"""Stage B repair / step 1: lock every input this run actually reads.

Produces work/input_lock.json:

  * one entry per locked file with existence, byte hash, logical body hash, identity
    and the role it plays (sealed r3 table / research source / evidence snapshot /
    rule document / sealed r3 release member);
  * for every saved evidence snapshot, the body hash recomputed from disk compared
    against the hash the snapshot index declared when the page was captured, so a
    rewritten snapshot cannot hide behind a stale declaration;
  * input_root_digest: one digest over the whole locked input set. Every later
    step binds its success to this digest, so a success record can never be
    replayed against different inputs.

The document is itself part of the release; s03/s11 re-derive the digest and refuse
to publish when the bytes on disk no longer match it.
"""
from __future__ import annotations

import glob
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import (  # noqa: E402
    CODE_FILES, CODE_VERSION, R3, R3_LOCKED_DIR, R3_REQUIRED_TABLES, R3_RELEASE_MANIFEST,
    RESEARCH_SOURCES, RULE_DOCS, RUN, SNAP, WORK, file_identity, read_csv, read_json,
    resolve_locked_path, sha256_bytes, write_json,
)

SCRIPTS = os.path.join(RUN, "scripts")


def rel(path: str) -> str:
    return os.path.relpath(path, RUN).replace("\\", "/")


def collect() -> tuple[list[dict], list[dict], dict]:
    entries: list[dict] = []
    problems: list[dict] = []

    # 1. sealed r3 release members (every file the r3 manifest declares)
    manifest_path = os.path.join(R3, R3_RELEASE_MANIFEST)
    manifest = read_json(manifest_path)
    declared = manifest.get("files", {})
    for name, meta in sorted(declared.items()):
        path = os.path.join(R3, name)
        ident = file_identity(path)
        entry = {**ident, "path": path, "role": "r3_release_member", "identity": f"stage_a_r3/{name}",
                 "declared_sha256": meta.get("sha256"), "declared_bytes": meta.get("bytes")}
        entries.append(entry)
        if not ident["exists"]:
            problems.append({"path": path, "problem": "MISSING", "role": "r3_release_member"})
        elif ident["sha256"] != meta.get("sha256") or ident["bytes"] != meta.get("bytes"):
            problems.append({"path": path, "problem": "HASH_OR_SIZE_MISMATCH", "role": "r3_release_member",
                             "expected_sha256": meta.get("sha256"), "actual_sha256": ident["sha256"]})

    # 2. the r3 tables this run parses by name (must be in the manifest too)
    for name in R3_REQUIRED_TABLES:
        path = os.path.join(R3, name)
        ident = file_identity(path)
        entries.append({**ident, "path": path, "role": "r3_required_table",
                        "identity": f"stage_a_r3/{name}"})
        if not ident["exists"]:
            problems.append({"path": path, "problem": "MISSING", "role": "r3_required_table"})
        elif name not in declared:
            problems.append({"path": path, "problem": "NOT_IN_RELEASE_MANIFEST", "role": "r3_required_table"})

    # 3. locked_inputs subtree
    locked_dir = os.path.join(R3, R3_LOCKED_DIR)
    for path in sorted(glob.glob(os.path.join(locked_dir, "**", "*"), recursive=True)):
        if os.path.isdir(path):
            continue
        name = os.path.relpath(path, R3).replace("\\", "/")
        ident = file_identity(path)
        entries.append({**ident, "path": path, "role": "r3_locked_input",
                        "identity": f"stage_a_r3/{name}"})
        if not ident["exists"]:
            problems.append({"path": path, "problem": "MISSING", "role": "r3_locked_input"})

    # 4. research sources authored for this run: the raw per-company inputs, both the
    # pilot sources and the extension skeletons / filled extension files
    authored_paths = sorted(glob.glob(os.path.join(WORK, "pilot_facts_*.json")))
    authored_paths += sorted(glob.glob(os.path.join(WORK, "research", "authored_*.json")))
    if not authored_paths:
        problems.append({"path": os.path.join(WORK, "research"), "problem": "NO_AUTHORED_SOURCES",
                         "role": "research_source"})
    for path in authored_paths:
        name = os.path.relpath(path, WORK).replace("\\", "/")
        ident = file_identity(path)
        entries.append({**ident, "path": path, "role": "research_source", "identity": f"work/{name}"})
        if not ident["exists"]:
            problems.append({"path": path, "problem": "MISSING", "role": "research_source"})
    for name in RESEARCH_SOURCES:
        path = os.path.join(WORK, name)
        if any(e["identity"] == f"work/{name}" for e in entries):
            continue
        ident = file_identity(path)
        entries.append({**ident, "path": path, "role": "research_source", "identity": f"work/{name}"})
        if not ident["exists"]:
            problems.append({"path": path, "problem": "MISSING", "role": "research_source"})

    # 5. rule / policy documents
    for name in RULE_DOCS:
        path = os.path.join(WORK, name)
        ident = file_identity(path)
        entries.append({**ident, "path": path, "role": "rule_document", "identity": f"work/{name}"})
        if not ident["exists"]:
            problems.append({"path": path, "problem": "MISSING", "role": "rule_document"})

    # 6. evidence snapshots + their declarations
    snap_index_path = os.path.join(WORK, "snapshot_index.json")
    snap_index = read_json(snap_index_path) if os.path.exists(snap_index_path) else {"snapshots": {}}
    entries.append({**file_identity(snap_index_path), "path": snap_index_path,
                    "role": "snapshot_index", "identity": "work/snapshot_index.json"})
    declared_snaps = snap_index.get("snapshots", {})
    snap_disk = {}
    for path in sorted(glob.glob(os.path.join(SNAP, "*"))):
        if os.path.isdir(path):
            continue
        ident = file_identity(path)
        snap_disk[rel(path)] = ident
        entries.append({**ident, "path": path, "role": "evidence_snapshot", "identity": rel(path)})

    snap_checks = []
    for snap_id, meta in sorted(declared_snaps.items()):
        text_rel = (meta.get("snapshot_text_path") or "").replace("\\", "/")
        raw_rel = (meta.get("snapshot_raw_path") or "").replace("\\", "/")
        text_ident = snap_disk.get(text_rel)
        raw_ident = snap_disk.get(raw_rel) if raw_rel else None
        declared_body = meta.get("body_text_sha256") or ""
        declared_raw = meta.get("raw_sha256") or ""
        actual_body = (text_ident or {}).get("body_text_sha256")
        actual_body_norm = (text_ident or {}).get("normalized_newline_sha256")
        # A body is intact when the declared hash matches the saved bytes, or when it
        # matches after newline normalization (a platform that rewrote line endings
        # without changing content must not be reported as tampering).
        ok_body = bool(text_ident and text_ident["exists"] and declared_body
                       and (actual_body == declared_body or actual_body_norm == declared_body))
        if not declared_body and text_ident and text_ident["exists"] and text_ident["bytes"] == 0:
            ok_body = True   # a page whose body was never retrievable declares an empty body
        ok_raw = raw_rel == "" or bool(raw_ident and raw_ident["exists"] and declared_raw
                                       and raw_ident["sha256"] == declared_raw)
        rec = {
            "snapshot_id": snap_id,
            "company_id": meta.get("company_id", ""),
            "access_status": meta.get("access_status", ""),
            "snapshot_text_path": text_rel,
            "declared_body_text_sha256": declared_body,
            "actual_body_text_sha256": actual_body,
            "actual_normalized_newline_sha256": actual_body_norm,
            "declared_raw_sha256": declared_raw,
            "actual_raw_sha256": (raw_ident or {}).get("sha256"),
            "body_matches": ok_body,
            "raw_matches": ok_raw,
            "normalizer": meta.get("normalizer", ""),
        }
        snap_checks.append(rec)
        if not ok_body and meta.get("access_status") == "OK":
            problems.append({"path": text_rel, "problem": "SNAPSHOT_BODY_HASH_MISMATCH",
                             "role": "evidence_snapshot", "snapshot_id": snap_id,
                             "declared": declared_body, "actual": actual_body})
        if not ok_raw and meta.get("access_status") == "OK" and raw_rel:
            problems.append({"path": raw_rel, "problem": "SNAPSHOT_RAW_HASH_MISMATCH",
                             "role": "evidence_snapshot", "snapshot_id": snap_id,
                             "declared": declared_raw, "actual": (raw_ident or {}).get("sha256")})

    # 7. search log (part of the evidence trail)
    log_path = os.path.join(RUN, "search_log.jsonl")
    entries.append({**file_identity(log_path), "path": log_path,
                    "role": "search_log", "identity": "search_log.jsonl"})

    # 7b. derived company roster and the fixed sample-identity map
    extra_work = ["work/companies.json", "work/identity_map.json"]
    for identity in extra_work:
        path = os.path.join(RUN, identity.replace("/", os.sep))
        ident = file_identity(path)
        entries.append({**ident, "path": path, "role": "run_identity_input", "identity": identity})
        if not ident["exists"]:
            problems.append({"path": path, "problem": "MISSING", "role": "run_identity_input"})

    # 8. the code that produces the release
    code = []
    for name in CODE_FILES:
        path = os.path.join(SCRIPTS, name)
        ident = file_identity(path)
        code.append({**ident, "script": name})
        if not ident["exists"]:
            problems.append({"path": path, "problem": "MISSING", "role": "code_file"})

    return entries, problems, {"snap_checks": snap_checks, "code": code,
                               "snapshot_index": snap_index, "manifest": manifest}


def root_digest(entries: list[dict], code: list[dict]) -> str:
    payload = json.dumps(
        {
            "inputs": [[e["identity"], e["exists"], e["bytes"], e["sha256"], e["body_text_sha256"]]
                       for e in sorted(entries, key=lambda x: x["identity"])],
            "code": [[c["script"], c["sha256"]] for c in sorted(code, key=lambda x: x["script"])],
            "code_version": CODE_VERSION,
        },
        ensure_ascii=False, sort_keys=True,
    )
    return sha256_bytes(payload.encode("utf-8"))


def verify_existing(lock: dict) -> tuple[list[dict], list[dict]]:
    """Compare the locked input set against what is on disk right now.

    This is the mode every downstream step and every fault probe uses: the lock is
    never rewritten from a possibly tampered state, it is only checked. Rebuilding the
    lock is an explicit act (`--rebuild`) reserved for the run that authored the
    research sources.
    """
    drifted: list[dict] = []
    checked: list[dict] = []
    for e in lock.get("entries", []):
        ident = file_identity(resolve_locked_path(e))
        if not ident["exists"]:
            drifted.append({"path": e["identity"], "problem": "MISSING", "role": e["role"]})
            checked.append({**e, "verify_status": "MISSING"})
            continue
        if ident["sha256"] == e["sha256"]:
            status = "MATCH"
        elif e.get("body_text_sha256") and ident["body_text_sha256"] == e["body_text_sha256"]:
            status = "MATCH_AFTER_NEWLINE_NORMALIZATION"
        else:
            status = "CHANGED"
            drifted.append({"path": e["identity"], "problem": "CHANGED", "role": e["role"],
                            "expected_sha256": e["sha256"], "actual_sha256": ident["sha256"]})
        checked.append({**e, "verify_status": status,
                        "verify_actual_sha256": ident["sha256"],
                        "verify_actual_bytes": ident["bytes"]})
    for c in lock.get("code_files", []):
        p = os.path.join(SCRIPTS, c["script"])
        ident = file_identity(p)
        if not ident["exists"]:
            drifted.append({"path": f"scripts/{c['script']}", "problem": "MISSING", "role": "code_file"})
        elif ident["sha256"] != c["sha256"]:
            drifted.append({"path": f"scripts/{c['script']}", "problem": "CHANGED", "role": "code_file",
                            "expected_sha256": c["sha256"], "actual_sha256": ident["sha256"]})
    return drifted, checked


def main() -> int:
    os.makedirs(WORK, exist_ok=True)
    lock_path = os.path.join(WORK, "input_lock.json")
    rebuild = ("--rebuild" in sys.argv) or (not os.path.exists(lock_path))

    if not rebuild:
        lock = json.load(open(lock_path, encoding="utf-8"))
        drifted, checked = verify_existing(lock)
        # the lock's own digest must still be re-derivable from its entries, so the
        # recorded input set cannot be edited without the change being noticed
        recomputed_digest = root_digest(lock["entries"], lock["code_files"])
        digest_ok = recomputed_digest == lock["input_root_digest"]
        # a locked input set that no longer lists a required research source is also a
        # drift, even when the remaining files are unchanged
        missing_required = [name for name in RESEARCH_SOURCES
                            if not any(e["identity"] == f"work/{name}" for e in lock["entries"])]
        problems = list(lock.get("problems", [])) + drifted
        if not digest_ok:
            problems.append({"path": "work/input_lock.json", "problem": "INPUT_ROOT_DIGEST_NOT_REPRODUCIBLE",
                             "role": "input_lock", "recorded": lock["input_root_digest"],
                             "recomputed": recomputed_digest})
        for name in missing_required:
            problems.append({"path": f"work/{name}", "problem": "REQUIRED_RESEARCH_SOURCE_NOT_LOCKED",
                             "role": "research_source"})
        result = {
            "mode": "VERIFY_EXISTING_LOCK",
            "run_id": lock["run_id"],
            "code_version": lock["code_version"],
            "input_root_digest": lock["input_root_digest"],
            "code_digest": lock["code_digest"],
            "digest_reproducible": digest_ok,
            "n_entries": len(checked),
            "n_snapshots": len(lock.get("snapshot_checks", [])),
            "snapshots_hash_ok": sum(1 for s in lock.get("snapshot_checks", []) if s["body_matches"]),
            "n_problems": len(problems),
            "problems": problems[:12],
            "note": ("输入锁只被核验，不被重写；任何输入或代码变化都会在这里暴露，"
                     "不会因为重跑锁定步骤而被新状态覆盖"),
            "rebuild_hint": "作者如需重新生成输入锁，显式执行 s01_lock_inputs.py --rebuild",
            "drift": drifted,
            "checked": checked,
        }
        write_json(os.path.join(WORK, "input_lock_verify.json"), result)
        print(json.dumps({k: result[k] for k in
                          ("mode", "n_entries", "snapshots_hash_ok", "digest_reproducible", "n_problems",
                           "input_root_digest", "code_digest")}, ensure_ascii=False, indent=2))
        if problems:
            print(json.dumps(problems[:6], ensure_ascii=False, indent=2))
        return 0 if not problems else 1

    entries, problems, extra = collect()
    digest = root_digest(entries, extra["code"])
    code_digest = sha256_bytes(json.dumps([[c["script"], c["sha256"]] for c in extra["code"]],
                                          sort_keys=True).encode("utf-8"))
    by_role: dict[str, int] = {}
    for e in entries:
        by_role[e["role"]] = by_role.get(e["role"], 0) + 1
    doc = {
        "run_id": os.path.basename(RUN),
        "code_version": CODE_VERSION,
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "mode": "REBUILT_LOCK",
        "inputs_root": RUN,
        "r3_root": R3,
        "n_entries": len(entries),
        "by_role": by_role,
        "input_root_digest": digest,
        "code_digest": code_digest,
        "code_files": extra["code"],
        "problems": problems,
        "n_problems": len(problems),
        "snapshot_checks": extra["snap_checks"],
        "entries": entries,
    }
    write_json(lock_path, doc)

    print(json.dumps({
        "mode": doc["mode"],
        "n_entries": doc["n_entries"],
        "by_role": by_role,
        "n_snapshots": len(extra["snap_checks"]),
        "snapshots_hash_ok": sum(1 for s in extra["snap_checks"] if s["body_matches"]),
        "input_root_digest": digest,
        "code_digest": code_digest,
        "n_problems": doc["n_problems"],
        "problems": problems[:12],
    }, ensure_ascii=False, indent=2))
    return 0 if not problems else 1


if __name__ == "__main__":
    raise SystemExit(main())
