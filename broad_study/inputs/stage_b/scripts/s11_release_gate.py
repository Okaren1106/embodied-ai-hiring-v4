"""Stage B repair r2 / step 11: release gate.

The previous publisher trusted stored success documents and hashed files before the
gate status was written. This gate re-derives what it needs from the current run
directory (via lock identities, not stale absolute paths), refuses when a required
fault probe is missing or failed, binds the current page / company master table /
cards / Node script, then writes the status and only afterwards checksums.
"""
from __future__ import annotations

import glob
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import R3, RUN, WORK, file_identity, read_csv, read_json, resolve_locked_path, sha256_file, write_json  # noqa: E402

FAILURE_DOC = "release_gate_status.json"
REQUIRED_PROBES = [
    "完整未修改的正对照",
    "删除一份研究源文件",
    "删除必需表",
    "删除一条原缺口",
    "篡改快照实际内容",
    "改证据发布日期到 2027",
    "改日期后强行保留观察日可用",
    "把查无写成确定否定",
    "关闭未研究公司的问题",
    "改写快照哈希声明",
    "把母公司规模写进团队字段",
    "按前缀把背景证据改成支持",
    "篡改输入锁一条 sha256",
    "篡改代码摘要 code_digest",
    "改事实值",
    "修改当前副本的研究源文件",
    "核验后替换 index.html",
    "公司主表广告数改为 999",
    "必需负例失败但计数写成全绿",
    "替换 Node 检查脚本并保留原成功报告",
    "融资证据换成产品页且重建合法哈希",
    "媒体报道升级成外部确认",
]


def main() -> int:
    failures: list[dict] = []

    def refuse(reason: str, detail) -> None:
        failures.append({"gate": reason, "detail": detail})

    lock_path = os.path.join(WORK, "input_lock.json")
    if not os.path.exists(lock_path):
        refuse("INPUT_LOCK_MISSING", "work/input_lock.json 不存在")
        lock = None
    else:
        lock = read_json(lock_path)
        drifted = []
        for e in lock["entries"]:
            ident = file_identity(resolve_locked_path(e))
            if not ident["exists"]:
                drifted.append({"path": e["identity"], "problem": "MISSING"})
                continue
            if ident["sha256"] != e["sha256"] and not (
                    e.get("body_text_sha256") and ident["body_text_sha256"] == e["body_text_sha256"]):
                drifted.append({"path": e["identity"], "problem": "CHANGED",
                                "expected": e["sha256"], "actual": ident["sha256"]})
        if drifted:
            refuse("INPUT_DRIFT", drifted[:8])
        if lock.get("problems"):
            refuse("INPUT_LOCK_PROBLEMS", lock["problems"][:6])
        try:
            from s00_common import CODE_FILES, sha256_bytes  # noqa: WPS433
            code_pairs = []
            for name in CODE_FILES:
                p = os.path.join(RUN, "scripts", name)
                code_pairs.append([name, sha256_file(p) if os.path.exists(p) else None])
            actual_code_digest = sha256_bytes(json.dumps(code_pairs, sort_keys=True).encode("utf-8"))
            if actual_code_digest != lock.get("code_digest"):
                refuse("CODE_DIGEST_STALE",
                       {"recorded": lock.get("code_digest"), "current": actual_code_digest})
        except Exception as exc:  # noqa: BLE001
            refuse("CODE_DIGEST_RECOMPUTE_FAILED", str(exc))
        recomputed = None
        try:
            sys.path.insert(0, os.path.join(RUN, "scripts"))
            from s01_lock_inputs import root_digest  # noqa: WPS433
            recomputed = root_digest(lock["entries"], lock["code_files"])
            if recomputed != lock.get("input_root_digest"):
                refuse("INPUT_ROOT_DIGEST_STALE",
                       {"recorded": lock.get("input_root_digest"), "recomputed": recomputed})
        except Exception as exc:  # noqa: BLE001
            refuse("INPUT_ROOT_DIGEST_RECOMPUTE_FAILED", str(exc))

    ver_path = os.path.join(RUN, "verification.json")
    if not os.path.exists(ver_path):
        refuse("VERIFICATION_MISSING", "verification.json 不存在")
        ver = None
    else:
        ver = read_json(ver_path)
        if ver.get("n_fail"):
            refuse("SELF_CHECK_FAILURES", f"{ver['n_fail']} 项自检失败")
        bound = ver.get("bound_to", {})
        if lock is not None:
            if bound.get("input_root_digest") != lock.get("input_root_digest"):
                refuse("VERIFICATION_NOT_BOUND_TO_INPUT",
                       {"record": bound.get("input_root_digest"), "current": lock.get("input_root_digest")})
            if bound.get("code_digest") != lock.get("code_digest"):
                refuse("VERIFICATION_NOT_BOUND_TO_CODE",
                       {"record": bound.get("code_digest"), "current": lock.get("code_digest")})
        for name, recorded in (bound.get("tables") or {}).items():
            p = os.path.join(RUN, name)
            if not os.path.exists(p):
                refuse("BOUND_TABLE_MISSING", name)
            elif sha256_file(p) != recorded:
                refuse("BOUND_TABLE_CHANGED", {"table": name, "recorded": recorded,
                                               "current": sha256_file(p)})
        for name, recorded in (bound.get("scripts") or {}).items():
            p = os.path.join(RUN, "scripts", name)
            if not os.path.exists(p):
                refuse("BOUND_SCRIPT_MISSING", name)
            elif sha256_file(p) != recorded:
                refuse("BOUND_SCRIPT_CHANGED", {"script": name, "recorded": recorded,
                                                "current": sha256_file(p)})

    fault_path = os.path.join(WORK, "fault_probes.json")
    fault = None
    if not os.path.exists(fault_path):
        refuse("FAULT_PROBES_MISSING", "work/fault_probes.json 不存在")
    else:
        fault = read_json(fault_path)
        probes = fault.get("probes") or []
        by_name = {p.get("probe"): p for p in probes}
        missing = [n for n in REQUIRED_PROBES if n not in by_name]
        if missing:
            refuse("REQUIRED_FAULT_PROBE_MISSING", missing)
        failed = [p.get("probe") for p in probes if p.get("result") != "PASS"]
        if failed:
            refuse("FAULT_PROBE_FAILED", failed)
        if not fault.get("positive_control_ok"):
            refuse("POSITIVE_CONTROL_FAILED",
                   "完整未修改副本未被接受：故障实验的对照不成立")
        n_pass = sum(1 for p in probes if p.get("result") == "PASS")
        n_probes = len(probes)
        if fault.get("n_pass") != n_pass or fault.get("n_probes") != n_probes:
            refuse("FAULT_REPORT_INCONSISTENT",
                   {"n_pass": fault.get("n_pass"), "actual_pass": n_pass,
                    "n_probes": fault.get("n_probes"), "actual_probes": n_probes})
        if n_pass != n_probes or n_probes < len(REQUIRED_PROBES):
            refuse("FAULT_PROBES_INCOMPLETE",
                   f"{n_pass}/{n_probes} (required {len(REQUIRED_PROBES)})")
        bound = fault.get("bound_to", {})
        if lock is not None:
            if bound.get("input_root_digest") != lock.get("input_root_digest"):
                refuse("FAULT_REPORT_NOT_BOUND_TO_INPUT",
                       {"report": bound.get("input_root_digest"),
                        "current": lock.get("input_root_digest")})
            if bound.get("code_digest") != lock.get("code_digest"):
                refuse("FAULT_REPORT_NOT_BOUND_TO_CODE",
                       {"report": bound.get("code_digest"), "current": lock.get("code_digest")})
        for p in probes:
            if p.get("expected") == "REJECT" and p.get("release", {}).get("published"):
                refuse("FAULT_PROBE_PUBLISHED", p.get("probe"))

    rb_path = os.path.join(WORK, "rebuild_check.json")
    if not os.path.exists(rb_path):
        refuse("REBUILD_CHECK_MISSING", "work/rebuild_check.json 不存在")
    else:
        rb = read_json(rb_path)
        if not rb.get("identical"):
            refuse("REBUILD_DIFFERS", list(rb.get("differences", {}))[:6])

    html_path = os.path.join(WORK, "html_runtime_checks.json")
    index_path = os.path.join(RUN, "index.html")
    js_path = os.path.join(RUN, "scripts", "s08_html_runtime_check.js")
    if not os.path.exists(html_path):
        refuse("HTML_RUNTIME_CHECK_MISSING", "work/html_runtime_checks.json 不存在")
        rt = None
    else:
        rt = read_json(html_path)
        if rt.get("summary", {}).get("n_fail"):
            refuse("HTML_RUNTIME_FAILURES", rt["summary"]["n_fail"])
        bound_rt = rt.get("bound_to") or {}
        if os.path.exists(js_path) and bound_rt.get("script_sha256") != sha256_file(js_path):
            refuse("NODE_SCRIPT_NOT_BOUND",
                   {"report": bound_rt.get("script_sha256"), "current": sha256_file(js_path)})
        if os.path.exists(index_path) and bound_rt.get("index_html_sha256") != sha256_file(index_path):
            refuse("INDEX_HTML_CHANGED_AFTER_CHECK",
                   {"report": bound_rt.get("index_html_sha256"), "current": sha256_file(index_path)})
    if not os.path.exists(index_path):
        refuse("INDEX_HTML_MISSING", "index.html 不存在")

    profile_path = os.path.join(RUN, "company_profile.csv")
    if not os.path.exists(profile_path):
        refuse("COMPANY_PROFILE_MISSING", "company_profile.csv 不存在")
    else:
        profile = read_csv(profile_path)
        t1 = read_csv(os.path.join(R3, "T1_sample_company.csv"))
        t1_ads = {r["company_id"]: r.get("n_ads") for r in t1}
        ads_drift = []
        for row in profile:
            expected = str(t1_ads.get(row["company_id"], "")).strip()
            got = str(row.get("n_ads_inherited") or "").strip()
            if expected and got != expected:
                ads_drift.append({"company_id": row["company_id"], "t1": expected, "profile": got})
        if ads_drift:
            refuse("COMPANY_PROFILE_N_ADS_DRIFT", ads_drift[:6])

    cards_dir = os.path.join(RUN, "company_cards")
    card_files = sorted(glob.glob(os.path.join(cards_dir, "*.md"))) if os.path.isdir(cards_dir) else []
    if len(card_files) != 24:
        refuse("COMPANY_CARDS_COUNT", f"n={len(card_files)}")
    manifest_path = os.path.join(WORK, "card_manifest.json")
    if os.path.exists(manifest_path):
        manifest = read_json(manifest_path)
        card_drift = []
        for rel, meta in (manifest.get("files") or {}).items():
            p = os.path.join(RUN, rel.replace("/", os.sep))
            if not os.path.exists(p):
                card_drift.append({"path": rel, "problem": "MISSING"})
            elif sha256_file(p) != meta.get("sha256"):
                card_drift.append({"path": rel, "problem": "CHANGED"})
        if card_drift:
            refuse("COMPANY_CARDS_CHANGED", card_drift[:6])
        if lock is not None and manifest.get("input_root_digest") != lock.get("input_root_digest"):
            refuse("CARD_MANIFEST_NOT_BOUND",
                   {"manifest": manifest.get("input_root_digest"),
                    "current": lock.get("input_root_digest")})
    else:
        refuse("CARD_MANIFEST_MISSING", "work/card_manifest.json 不存在")

    sl_path = os.path.join(WORK, "search_log_summary.json")
    if os.path.exists(sl_path):
        sl = read_json(sl_path)
        if sl.get("missing_per_question_trail"):
            refuse("SEARCH_TRAIL_INCOMPLETE", sl.get("missing_per_question_trail")[:8])
        if sl.get("blocked_without_fetch_failure"):
            refuse("BLOCKED_WITHOUT_FETCH", sl.get("blocked_without_fetch_failure")[:8])

    from s13_semantic_checks import semantic_checks
    for item in semantic_checks():
        if not item["passed"]:
            refuse(item["id"], item["detail"])

    if failures:
        for name in ("release_checksums.json", "output_checksums.json", "RELEASE_OK"):
            p = os.path.join(RUN, name)
            if os.path.exists(p):
                os.remove(p)
        doc = {
            "stage": "B-evidence-integrated",
            "release_gate": "FAILED",
            "generated_at_from": os.path.basename(RUN),
            "failures": failures,
            "note": ("验证失败时不发布成功结果；本文件即为失败报告，且已移除已有的成功文档与成功标记。"
                     "失败报告本身保留，便于复验。"),
        }
        write_json(os.path.join(RUN, FAILURE_DOC), doc)
        print(json.dumps(doc, ensure_ascii=False, indent=2))
        return 1

    if os.path.exists(os.path.join(RUN, FAILURE_DOC)):
        os.remove(os.path.join(RUN, FAILURE_DOC))
    published = {
        "stage": "B-evidence-integrated",
        "release_gate": "PASSED",
        "scope": "TARGETED_COLLECTION_PENDING_ACCEPTANCE：返修及证据接入完成，待独立验收；不是阶段 B 完成",
        "bound_to": {
            "verification_digest": ver.get("verification_digest"),
            "input_root_digest": (lock or {}).get("input_root_digest"),
            "code_digest": (lock or {}).get("code_digest"),
            "run_id": (lock or {}).get("run_id"),
            "index_html_sha256": sha256_file(index_path),
            "company_profile_sha256": sha256_file(profile_path),
            "node_script_sha256": sha256_file(js_path),
        },
        "self_check": f"{ver['n_pass']}/{ver['n_checks']}",
        "fault_probes": f"{fault['n_pass']}/{fault['n_probes']}",
        "positive_control": "PASS",
        "rebuild_identical": True,
        "html_runtime": (rt or {}).get("summary"),
        "n_company_cards": len(card_files),
    }
    write_json(os.path.join(RUN, "release_gate_status.json"), published)
    with open(os.path.join(RUN, "RELEASE_OK"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("release_gate: PASSED\n"
                 "scope: TARGETED_COLLECTION_PENDING_ACCEPTANCE\n"
                 "note: 返修及证据接入完成，待独立验收；不写 STAGE_B_COMPLETE；不进入阶段 C。\n")
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf8"
    chk = subprocess.run(
        [sys.executable, "-B", "-X", "utf8", os.path.join(RUN, "scripts", "s10_checksums.py")],
        cwd=RUN, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env, timeout=120)
    if chk.returncode != 0:
        refuse("CHECKSUMS_AFTER_GATE_FAILED", (chk.stdout or "")[-400:] + (chk.stderr or "")[-200:])
        for name in ("release_checksums.json", "output_checksums.json", "RELEASE_OK"):
            p = os.path.join(RUN, name)
            if os.path.exists(p):
                os.remove(p)
        doc = {
            "stage": "B-evidence-integrated",
            "release_gate": "FAILED",
            "generated_at_from": os.path.basename(RUN),
            "failures": failures,
            "note": "门禁通过后生成清单失败，已撤回成功标记。",
        }
        write_json(os.path.join(RUN, FAILURE_DOC), doc)
        print(json.dumps(doc, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps(published, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
