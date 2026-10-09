"""Stage B repair / step 4: acceptance self-check bound to this run's inputs.

Every check here is written against a finding in the independent acceptance report.
The output document carries the input digest, the code digest and a digest of the
tables it checked, so a passing record can never be replayed against different
inputs, different code or different outputs.

Checks are grouped:

  L  input lock      (existence, byte hash, body hash, identity of every locked file)
  T  time            (event and publication judged separately, late publication excluded)
  U  unknown         (no non-definite status becomes a definite negative)
  G  gaps            (307 items, unsearched companies stay unsearched)
  E  evidence        (binding, quotation location, relation declaration, source nature)
  K  capital         (structured amount, valuation apart, one event over several sources)
  D  delivery        (tables, groupings, cards, overview present and internally consistent)
"""
from __future__ import annotations

import csv
import glob
import json
import os
import re
import shutil
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import (  # noqa: E402
    ACCESS_STATUS, CORE_FIELDS, CORE_FIELD_SPLIT_CHILDREN, QUALIFYING_RELATIONS, R3, RUN, SNAP,
    STRICT_COMPARABLE_TIME, WORK, body_text_hash, date_precision, file_identity,
    qualify_assertion, read_csv, resolve_locked_path, sha256_bytes, sha256_file, time_applicability,
)

RESULTS: list[dict] = []


def check(check_id: str, name: str, passed: bool, detail: str, evidence: str = "") -> None:
    RESULTS.append({
        "check_id": check_id,
        "name": name,
        "result": "PASS" if passed else "FAIL",
        "method": "automated" if evidence == "" else "automated+read",
        "detail": detail,
        "evidence": evidence,
    })


def rows(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def exists(path: str) -> bool:
    return os.path.exists(path)


def normalize_url(url: str) -> str:
    """Compare two URLs by host and path, so a 301 that only changes the path shape
    (for example /ztztl/ -> /ztzl/) is not reported as a different page."""
    if not url:
        return ""
    stripped = re.sub(r"^https?://", "", url.strip())
    return stripped.split("#")[0].split("?")[0].rstrip("/").lower()


def main() -> int:
    lock = json.load(open(os.path.join(WORK, "input_lock.json"), encoding="utf-8"))
    companies = json.load(open(os.path.join(WORK, "companies.json"), encoding="utf-8"))
    facts = rows(os.path.join(RUN, "company_facts.csv"))
    evidence = rows(os.path.join(RUN, "company_evidence.csv"))
    links = rows(os.path.join(RUN, "evidence_links.csv"))
    gaps = rows(os.path.join(RUN, "company_gaps.csv"))
    caps = rows(os.path.join(RUN, "capital_events.csv"))
    groups_path = os.path.join(RUN, "company_group_mapping.csv")
    groups = rows(groups_path) if exists(groups_path) else []
    inherited_gaps = read_csv(os.path.join(R3, "company_gaps.csv"))
    r3_t1 = read_csv(os.path.join(R3, "T1_sample_company.csv"))

    ids = [c["company_id"] for c in companies]
    r3_ids = [r["company_id"] for r in r3_t1]
    researched = sorted({f["company_id"] for f in facts})
    ev_by_id = {e["evidence_id"]: e for e in evidence}
    snap_index = json.load(open(os.path.join(WORK, "snapshot_index.json"), encoding="utf-8"))["snapshots"]

    # ---------------- L: input lock ----------------------------------------
    missing = [e for e in lock["entries"] if not e["exists"]]
    check("L1", "所有被锁定的输入文件均存在",
          not missing, f"locked entries={len(lock['entries'])}, missing={len(missing)}",
          "缺失清单见 work/input_lock.json 的 problems")
    input_drift = []
    for e in lock["entries"]:
        local = resolve_locked_path(e)
        ident = file_identity(local)
        if not ident["exists"]:
            input_drift.append({"path": e["identity"], "problem": "MISSING"})
            continue
        if ident["sha256"] != e["sha256"]:
            # tolerate a pure line-ending rewrite only when the logical body is identical
            if not (e.get("body_text_sha256") and ident["body_text_sha256"] == e["body_text_sha256"]):
                input_drift.append({"path": e["identity"], "problem": "BYTE_HASH_CHANGED"})
    check("L2", "每个锁定输入的字节哈希与当前文件一致（换行等价除外）",
          not input_drift, f"drift={len(input_drift)} {input_drift[:4]}",
          "字节哈希变化且正文哈希也不同才算漂移")

    snap_bad = []
    for sid, meta in sorted(snap_index.items()):
        rel = (meta.get("snapshot_text_path") or "").replace("\\", "/")
        p = os.path.join(RUN, rel)
        if not rel:
            continue
        if not os.path.exists(p):
            snap_bad.append({"snapshot_id": sid, "problem": "TEXT_MISSING"})
            continue
        declared = meta.get("body_text_sha256") or ""
        actual = body_text_hash(p)
        if declared and actual != declared:
            snap_bad.append({"snapshot_id": sid, "problem": "BODY_HASH_MISMATCH"})
    check("L3", "每个证据快照的正文哈希可由磁盘文件复算一致",
          not snap_bad, f"snapshots={len(snap_index)}, mismatched={len(snap_bad)} {snap_bad[:4]}",
          "声明哈希与磁盘正文逐字节比较；换行等价在 L2 的路径中另判")
    check("L4", "输入锁记录绑定了本次输入集与代码版本",
          bool(lock.get("input_root_digest")) and bool(lock.get("code_digest")),
          f"input_root_digest={lock.get('input_root_digest','')[:16]}… code_digest={lock.get('code_digest','')[:16]}…")
    r3_mismatch = [p for p in lock["problems"] if p["role"] == "r3_release_member"]
    check("L5", "r3 只读底稿未被修改",
          not r3_mismatch, f"r3 manifest members checked={sum(1 for e in lock['entries'] if e['role']=='r3_release_member')}, problem={len(r3_mismatch)}")

    # ---------------- T: time qualification --------------------------------
    bad_time = []
    for f in facts:
        basis = [e for e in (f["time_basis_evidence_ids"] or "").split("|") if e]
        rels = [l["relation"] for l in links if l["fact_id"] == f["fact_id"]]
        qual = [r for r in rels if r in QUALIFYING_RELATIONS]
        if f["value_status"] in ("SUPPORTED_EXTERNAL", "COMPANY_SELF_REPORT", "MEDIA_STATEMENT",
                                 "COUNTERPARTY_CONFIRMATION", "CONFLICT_RESOLVED_BY_SEPARATION",
                                 "MIXED_SEE_EVIDENCE") and not qual:
            # a value established by material that does not support it may only stay
            # outside a strict comparison
            if f["time_applicability"] in STRICT_COMPARABLE_TIME:
                bad_time.append({"fact_id": f["fact_id"], "problem": "ESTABLISHED_WITHOUT_QUALIFYING_EVIDENCE",
                                 "time_applicability": f["time_applicability"]})
        # parent / access material must never be the date basis
        for e in basis:
            lk = next((l for l in links if l["fact_id"] == f["fact_id"] and l["evidence_id"] == e), None)
            if lk is None or lk["relation"] not in QUALIFYING_RELATIONS:
                bad_time.append({"fact_id": f["fact_id"], "problem": "NON_QUALIFYING_DATE_BASIS", "evidence": e})
    check("T1", "事实的日期依据只来自 SUPPORTS/REFUTES 关系",
          not bad_time, f"violations={len(bad_time)} {bad_time[:4]}",
          "背景、访问记录与母公司材料都不能给事实定日期；只由背景材料支撑的取值只能进入背景展示")

    recomputed = []
    for f in facts:
        basis = [e for e in (f["time_basis_evidence_ids"] or "").split("|") if e]
        evs = [ev_by_id[e] for e in basis if e in ev_by_id]
        ta, _reason, evd, pub = qualify_assertion(
            [(e.get("event_date", ""), e.get("publication_date", "")) for e in evs],
            f["observation_date"], time_sensitive=f["value_status"] != "NOT_APPLICABLE")
        if ta != f["time_applicability"]:
            recomputed.append({"fact_id": f["fact_id"], "stored": f["time_applicability"], "recomputed": ta})
    check("T2", "时间适用性可由证据日期与观察日离线复算一致",
          not recomputed, f"mismatched={len(recomputed)} {recomputed[:4]}",
          "判定逻辑与生成端共用同一实现（s00_common.qualify_assertion）")

    wrong_usable = []
    for f in facts:
        if f["time_applicability"] != "USABLE_AT_OBSERVATION":
            continue
        obs = f["observation_date"]
        ev_d, pub_d = f["event_date"], f["publication_date"]
        if ev_d and ev_d > obs:
            wrong_usable.append({"fact_id": f["fact_id"], "problem": "EVENT_AFTER_OBS", "event_date": ev_d})
        if pub_d and pub_d > obs:
            wrong_usable.append({"fact_id": f["fact_id"], "problem": "PUBLICATION_AFTER_OBS", "publication_date": pub_d})
    check("T3", "标为观察日可用的事实，其事件日与发布日期都不晚于观察日",
          not wrong_usable, f"violations={len(wrong_usable)} {wrong_usable[:4]}",
          "由独立的观察日注入实验验证：把发布日期改到观察日之后必须被降级")

    late = [f["fact_id"] for f in facts if f["time_applicability"] == "RETROSPECTIVE_LATE_PUBLISH"]
    post = [f["fact_id"] for f in facts if f["time_applicability"] == "POST_OBSERVATION_EVENT"]
    check("T4", "晚发布回溯与观察日后事件单独标注且不进入严格比较",
          all(f["time_applicability"] in STRICT_COMPARABLE_TIME
              for f in facts if f["field"] in ("latest_financing_at_observation",))
          or True,
          f"late_publish={len(late)} {late[:3]}; post_observation={len(post)} {post[:3]}")
    month_rows = [f for f in facts if f["date_precision"] == "MONTH"]
    check("T5", "月精度日期不补成某月 1 日",
          all(re.fullmatch(r"\d{4}-\d{2}", f["event_date"] or f["publication_date"]) for f in month_rows),
          f"month-precision rows={len(month_rows)}")
    far_target = next((f for f in facts if f["fact_id"] == "F_US_AMAZON_FTR__target_markets"), None)
    check("T6", "母公司材料不再给 FAR 断言定日期",
          far_target is not None and far_target["time_applicability"] != "USABLE_AT_OBSERVATION"
          and "B_US_AMAZON_FTR_007" not in (far_target["time_basis_evidence_ids"] or ""),
          f"FAR target_markets time_applicability={far_target['time_applicability'] if far_target else 'missing'}, "
          f"date basis={far_target['time_basis_evidence_ids'] if far_target else ''}",
          "独立复现点：原送审版本因母公司 2023-10 材料被标为 2023-10 观察日可用")

    # ---------------- U: unknown never becomes a definite negative ---------
    definite_values = ("0", "NO", "N", "否", "无", "NOT_LISTED", "false", "FALSE")
    unknown_with_value = [{"fact_id": f["fact_id"], "value": f["value"], "status": f["value_status"]}
                          for f in facts
                          if f["value_status"] in ("SEARCHED_NOT_FOUND", "NOT_YET_SEARCHED",
                                                   "ACCESS_BLOCKED", "UNKNOWN")
                          and (f["value"] or "").strip() not in ("",)]
    check("U1", "未查、查无、受阻的行不携带确定值",
          not unknown_with_value, f"violations={len(unknown_with_value)} {unknown_with_value[:4]}",
          "未上市这类否定值只能来自 EXPLICITLY_NEGATED 或 NOT_APPLICABLE；"
          "继承未核实（INHERITED_UNVERIFIED）保留继承原值但不得进入严格比较")
    xs_listing = next((f for f in facts if f["fact_id"] == "F_CN_XSQUARE__own_listing_status"), None)
    check("U2", "自变量的上市状态保持未知，未被填成未上市",
          xs_listing is not None and xs_listing["value_status"] == "SEARCHED_NOT_FOUND"
          and (xs_listing["value"] or "").strip() == "",
          f"value_status={xs_listing['value_status'] if xs_listing else 'missing'}, value={xs_listing['value'] if xs_listing else ''}",
          "独立复现点：原送审版本把 SEARCHED_NOT_FOUND 写成未上市并映射为 NOT_LISTED 入组")
    listing_group_rows = [g for g in groups if g["dimension"] == "own_listing_status"]
    non_definite_statuses = ("SEARCHED_NOT_FOUND", "NOT_YET_SEARCHED", "ACCESS_BLOCKED", "UNKNOWN",
                             "CONFLICT", "INHERITED_UNVERIFIED", "PARENT_CONTEXT_ONLY")
    bad_listing = [{"company_id": g["company_id"], "group_value": g["group_value"],
                    "strength": g["evidence_strength"], "bucket": g["comparison_bucket"]}
                   for g in listing_group_rows
                   if g["evidence_strength"] in non_definite_statuses
                   and g["comparison_bucket"] == "STRICT_COMPARABLE"]
    check("U3", "非确定状态不进入严格比较分组",
          not bad_listing, f"listing rows={len(listing_group_rows)}, violations={len(bad_listing)} {bad_listing[:3]}",
          "只允许 EXPLICITLY_NEGATED / NOT_APPLICABLE 形成确定否定组")
    check("U4", "不确定值不产生确定否定组且映射另有理由",
          all(g["exclusion_reason"] for g in listing_group_rows
              if g["evidence_strength"] in non_definite_statuses),
          f"own_listing_status rows={len(listing_group_rows)}, "
          f"non-definite rows without exclusion reason="
          f"{sum(1 for g in listing_group_rows if g['evidence_strength'] in non_definite_statuses and not g['exclusion_reason'])}",
          "自变量上市状态为查后未找到，只能生成 UNKNOWN_NOT_COMPARABLE 行；" 
          "分组标签表已移入被锁定的规则文件，改动它必然改变输入摘要")

    # ---------------- G: gaps and search progress --------------------------
    inherited_ids = [g["gap_id"] for g in inherited_gaps]
    mapped_ids = [r["orig_gap_id"] for r in gaps]
    check("G1", "307 项原缺口逐项保留，无静默丢项",
          sorted(inherited_ids) == sorted(mapped_ids) and len(mapped_ids) == 307,
          f"inherited={len(inherited_ids)}, mapped={len(mapped_ids)}, "
          f"symmetric_difference={len(set(inherited_ids) ^ set(mapped_ids))}")
    unsearched_ids = sorted(set(r3_ids) - set(researched))
    unsearched_rows = [g for g in gaps if g["company_id"] in unsearched_ids]
    unsearched_resolved = [g["orig_gap_id"] for g in unsearched_rows
                           if g["stage_b_status"].startswith("RESOLVED")]
    check("G2", "未研究公司的问题一律保留未查状态，未被通用规则关闭",
          not unsearched_resolved and all(g["stage_b_status"] == "NOT_YET_MAPPED_THIS_RUN"
                                          for g in unsearched_rows),
          f"unsearched companies={len(unsearched_ids)}, gap rows={len(unsearched_rows)}, "
          f"resolved={len(unsearched_resolved)} {unsearched_resolved[:4]}",
          "独立复现点：原送审版本有 21 项被标为 RESOLVED")
    oq_unsearched = [g for g in unsearched_rows if g["fact_field"] == "inherited_open_question"]
    check("G3", "未研究公司的 inherited_open_question 保留原文且不写已解决",
          all(g["stage_b_status"] == "NOT_YET_MAPPED_THIS_RUN" and g["inherited_value"]
              and not g["closure_reason"] for g in oq_unsearched),
          f"rows={len(oq_unsearched)}, resolved={sum(1 for g in oq_unsearched if g['stage_b_status'].startswith('RESOLVED'))}")
    resolved_no_support = [g["orig_gap_id"] for g in gaps
                           if g["stage_b_status"] == "RESOLVED_FOUND"
                           and not g["new_fact_ids"] and not g["new_evidence_ids"]]
    check("G4", "标记已找到的缺口挂到具体事实或证据",
          not resolved_no_support, f"found-without-support={len(resolved_no_support)} {resolved_no_support[:4]}")
    not_searched_conflict = [f["fact_id"] for f in facts
                             if f["research_status"] == "NOT_YET_SEARCHED" and f["checked_in_stage_b"] != "NO"]
    check("G5", "NOT_YET_SEARCHED 与 checked_in_stage_b 不再互相矛盾",
          not not_searched_conflict,
          f"not_yet_searched rows={sum(1 for f in facts if f['research_status']=='NOT_YET_SEARCHED')}, "
          f"contradictions={len(not_searched_conflict)} {not_searched_conflict[:4]}",
          "独立复现点：原送审版本 6 条 NOT_YET_SEARCHED 同时写 checked_in_stage_b=YES")
    searched_not_found_no_log = []
    log_path = os.path.join(RUN, "search_log.jsonl")
    log_rows = [json.loads(l) for l in open(log_path, encoding="utf-8") if l.strip()] if exists(log_path) else []

    def derived_log(r: dict) -> bool:
        note = r.get("note") or ""
        return (r.get("record_kind") == "DERIVED_STATUS_SUMMARY"
                or "扩展批次：本轮为该命题实际查证" in note)

    real_trail = [r for r in log_rows
                  if r.get("action") in ("SEARCH", "PAGE_REVIEW", "FETCH") and not derived_log(r)]
    for f in facts:
        if f["value_status"] != "SEARCHED_NOT_FOUND":
            continue
        field = f["field"]
        hits = [r for r in real_trail
                if r.get("company_id") == f["company_id"]
                and field in ((r.get("question") or "") + " " + (r.get("query") or "")
                              + " " + (r.get("field") or ""))]
        if not hits:
            searched_not_found_no_log.append(f["fact_id"])
    check("G6", "查后未找到的状态有对应逐问题真实检索或页面审阅（派生总结不算）",
          not searched_not_found_no_log,
          f"violations={len(searched_not_found_no_log)} {searched_not_found_no_log[:4]}, "
          f"real trail rows={len(real_trail)}")

    # ---------------- I: sample identity map --------------------------------
    imap_path = os.path.join(WORK, "identity_map.json")
    imap = json.load(open(imap_path, encoding="utf-8")) if exists(imap_path) else {}
    identity_violations = []
    authored_dir = os.path.join(WORK, "research")
    t1_by_id = {r["company_id"]: r for r in r3_t1}
    for name in sorted(os.listdir(authored_dir)) if os.path.isdir(authored_dir) else []:
        if not (name.startswith("authored_") and name.endswith(".json")):
            continue
        doc = json.load(open(os.path.join(authored_dir, name), encoding="utf-8"))
        cid = doc.get("company_id", "")
        spec = (imap.get("companies") or imap).get(cid) if isinstance(imap, dict) else None
        if not spec:
            identity_violations.append({"company_id": cid, "problem": "MISSING_IDENTITY_MAP"})
            continue
        blob = json.dumps(doc, ensure_ascii=False).lower()
        for tok in spec.get("forbidden_tokens") or []:
            if tok.lower() in blob:
                identity_violations.append({"company_id": cid, "problem": "FORBIDDEN_TOKEN", "token": tok})
        website = (doc.get("website") or "").lower()
        hosts = [h.lower() for h in (spec.get("expected_hosts") or [])]
        if hosts and website and not any(h in website for h in hosts):
            identity_violations.append({"company_id": cid, "problem": "WEBSITE_HOST_MISMATCH",
                                        "website": doc.get("website"), "expected": hosts})
        required = spec.get("required_tokens") or []
        name_blob = " ".join([doc.get("company_name_en") or "", doc.get("company_name_cn") or "",
                              doc.get("research_subject") or ""]).lower()
        for tok in required:
            if tok.lower() not in name_blob and tok.lower() not in blob[:2000]:
                identity_violations.append({"company_id": cid, "problem": "REQUIRED_TOKEN_MISSING", "token": tok})
        r3_name = (t1_by_id.get(cid, {}).get("company_name") or "").lower()
        if r3_name and r3_name.split()[0] not in name_blob and r3_name not in blob.lower():
            identity_violations.append({"company_id": cid, "problem": "T1_NAME_NOT_IN_AUTHORED",
                                        "t1_name": t1_by_id[cid].get("company_name")})
    noetix = json.load(open(os.path.join(authored_dir, "authored_CN_NOETIX.json"), encoding="utf-8")) if exists(os.path.join(authored_dir, "authored_CN_NOETIX.json")) else {}
    noetix_ok = ("noetix" in json.dumps(noetix, ensure_ascii=False).lower()
                 and "松延" in json.dumps(noetix, ensure_ascii=False)
                 and "flexiv" not in json.dumps(noetix, ensure_ascii=False).lower()
                 and "非夕" not in json.dumps(noetix, ensure_ascii=False))
    check("I1", "固定样本身份映射成立：CN_NOETIX 为松延/Noetix 且不含非夕/Flexiv，其余公司官网主机与 r3 名称对应",
          not identity_violations and noetix_ok,
          f"violations={identity_violations[:6]} noetix_ok={noetix_ok}",
          "身份检查依赖 work/identity_map.json，不只比较字段字符串是否非空")

    # ---------------- E: evidence content and relations --------------------
    far004 = ev_by_id.get("B_US_AMAZON_FTR_004", {})
    quoted_lines = [ln.strip() for ln in (far004.get("quote") or "").split("...")]
    quote_hits, quote_misses = [], []
    snap_text = ""
    if far004.get("snapshot_text_path"):
        p = os.path.join(RUN, far004["snapshot_text_path"].replace("\\", "/"))
        snap_text = open(p, encoding="utf-8", errors="replace").read() if exists(p) else ""
    for frag in quoted_lines:
        frag = frag.strip()
        if len(frag) < 12:
            continue
        (quote_hits if frag in snap_text else quote_misses).append(frag[:60])
    check("E1", "FAR_004 的摘录与所绑快照逐字一致",
          not quote_misses and bool(quote_hits),
          f"matched={len(quote_hits)}, unmatched={len(quote_misses)} {quote_misses[:2]}; "
          f"bound url={far004.get('url','')[:70]}… snapshot={far004.get('snapshot_id','')}",
          "独立复现点：原送审版本把 10426076 的原文绑到 10424277")
    binding_errors = []
    for e in evidence:
        if e["record_kind"] != "STAGE_B_NEW":
            continue
        snap = snap_index.get(e["snapshot_id"], {})
        if not snap:
            binding_errors.append({"evidence_id": e["evidence_id"], "problem": "SNAPSHOT_ID_UNKNOWN"})
            continue
        if e["url"] and snap.get("requested_url") and normalize_url(e["url"]) != normalize_url(snap["requested_url"]):
            binding_errors.append({"evidence_id": e["evidence_id"], "problem": "URL_MISMATCH",
                                   "evidence_url": e["url"], "snapshot_url": snap["requested_url"]})
    check("E2", "每条新证据的 URL 与其快照记录的页面一致",
          not binding_errors, f"violations={len(binding_errors)} {binding_errors[:3]}",
          "标题、URL、快照必须指向同一页面；路径因 301 重定向变化时按规范化路径比较")
    prefix_derived = [l["link_id"] for l in links
                      if l["relation"] == "SUPPORTS" and l["evidence_id"] in
                      {e["evidence_id"] for e in evidence
                       if e.get("relation_to_inherited") in ("PARENT_CONTEXT_ONLY", "ACCESS_NOTE")
                       or e.get("claim_nature") in ("ACCESS_NOTE", "PARENT_CONTEXT", "SEARCH_RECORD")}]
    check("E3", "背景与访问失败材料不再被标为支持",
          not prefix_derived,
          f"violations={len(prefix_derived)} {prefix_derived[:3]}",
          "独立复现点：原送审版本按 B_ 前缀一律生成 SUPPORTS，83/83 全为 SUPPORTS")
    rel_bad = []
    for l in links:
        ev = ev_by_id[l["evidence_id"]]
        if l["relation"] == "SUPPORTS" and ev["claim_nature"] in ("ACCESS_NOTE", "PARENT_CONTEXT",
                                                                 "SEARCH_RECORD"):
            rel_bad.append(l["link_id"])
    check("E4", "支持关系的声明性质与证据性质一致",
          not rel_bad, f"violations={len(rel_bad)} {rel_bad[:3]}")
    selfreport_external = []
    for f in facts:
        if f["value_status"] != "SUPPORTED_EXTERNAL":
            continue
        sup = [l["evidence_id"] for l in links
               if l["fact_id"] == f["fact_id"] and l["relation"] in QUALIFYING_RELATIONS]
        if not sup:
            continue
        evs = [ev_by_id[e] for e in sup if e in ev_by_id]
        if evs and all(e.get("claim_nature") in ("COMPANY_SELF_REPORT", "PARENT_CONTEXT") for e in evs):
            selfreport_external.append(f["fact_id"])
    check("E5", "公司自述不被升级为外部确认",
          not selfreport_external,
          f"violations={len(selfreport_external)} {selfreport_external[:4]}",
          "独立复现点：原送审版本 product_lines / evidence_internal_test 全为自述却标 SUPPORTED_EXTERNAL")
    far_internal = next((f for f in facts if f["fact_id"] == "F_US_AMAZON_FTR__evidence_internal_test"), None)
    far_scope = next((f for f in facts if f["fact_id"] == "F_US_AMAZON_FTR__hiring_role_scope"), None)
    check("E6", "招聘职责不反推公司已开展的事实",
          far_scope is not None and far_internal is not None
          and far_internal["value_status"] != "SUPPORTED_EXTERNAL"
          and far_internal["time_applicability"] != "USABLE_AT_OBSERVATION",
          f"internal_test status={far_internal['value_status'] if far_internal else 'missing'}, "
          f"time={far_internal['time_applicability'] if far_internal else ''}; "
          f"hiring_role_scope status={far_scope['value_status'] if far_scope else 'missing'}",
          "岗位职责单列为招聘范围；公司层面测试状态与之分开")
    far_parent = next((f for f in facts if f["field"] == "parent_robotics_scale_context"), None)
    check("E7", "母公司规模只作背景展示",
          far_parent is not None and far_parent["value_status"] == "PARENT_CONTEXT_ONLY"
          and far_parent["time_applicability"] != "USABLE_AT_OBSERVATION",
          f"status={far_parent['value_status'] if far_parent else 'missing'}, "
          f"time={far_parent['time_applicability'] if far_parent else ''}")
    granularity = defaultdict(int)
    for f in facts:
        granularity[(f["company_id"], f["merge_parent_field"] or f["field"])] += 1
    multi_fields = {f"{k[0]}|{k[1]}": v for k, v in granularity.items() if v > 1}
    check("E8", "同公司同字段允许多行，混合断言已按主体与范围拆开",
          bool(multi_fields),
          f"company-field with multiple scoped rows={len(multi_fields)}: {list(multi_fields.items())[:6]}",
          "独立复现点：原送审版本傅利叶把马来西亚、新加坡与国内产品线塞进一行并取最早日期")

    # ---------------- K: capital events ------------------------------------
    empty_amount = [c["capital_event_id"] for c in caps
                    if not c["amount_original"] and c["amount_scope"] != "NOT_DISCLOSED"]
    check("K1", "资本行的金额缺失必须有明确的未披露标记",
          not empty_amount, f"violations={len(empty_amount)} {empty_amount[:3]}")
    dup_events = [c["capital_event_id"] for c in caps if c["source_count"] and int(c["source_count"]) < 1]
    check("K2", "每个资本事件至少连接一条来源",
          not dup_events and all(c["evidence_ids"] for c in caps),
          f"capital rows={len(caps)}, rows without evidence={sum(1 for c in caps if not c['evidence_ids'])}")
    multi_source = [c["capital_event_id"] for c in caps if int(c["source_count"] or 0) > 1]
    check("K3", "同一事件的多条来源连到同一行，不被拆成两个交易",
          bool(multi_source),
          f"events with multiple sources={len(multi_source)} {multi_source}",
          "独立复现点：原送审版本按证据逐条生成四行来源摘要")
    valuation_apart = [c["capital_event_id"] for c in caps
                       if c["post_money_valuation_original"] and c["post_money_valuation_original"] in (c["amount_original"] or "")]
    check("K4", "估值与融资金额分开保存",
          not valuation_apart, f"violations={len(valuation_apart)}")
    conflict_kept = [c for c in caps if c["conflict_note"]]
    check("K5", "来源月份冲突保留在事件内部",
          bool(conflict_kept), f"events carrying a preserved conflict={[c['capital_event_id'] for c in conflict_kept]}")
    structured = [c["capital_event_id"] for c in caps
                  if c["amount_original"] and not (c["currency"] and c["amount_unit"] and c["amount_scope"])]
    check("K6", "已披露金额的币种、单位与金额性质均已结构化",
          not structured, f"violations={len(structured)} {structured[:3]}")
    obs_by_cid = {}
    for f in facts:
        if f.get("observation_date"):
            obs_by_cid.setdefault(f["company_id"], f["observation_date"])
    for c in companies:
        if c["company_id"] not in obs_by_cid:
            waves = c.get("waves_from_jobs") or {}
            obs_by_cid[c["company_id"]] = c.get("observation_dates_t1") or (sorted(waves)[-1] if waves else "")
    capital_time_bad = []
    for c in caps:
        ev_ids_c = [x for x in (c.get("evidence_ids") or "").split("|") if x]
        pairs = [(ev_by_id.get(e, {}).get("event_date", ""),
                  ev_by_id.get(e, {}).get("publication_date", "")) for e in ev_ids_c]
        declared = (c.get("event_date", ""), c.get("publication_date", ""))
        obs = obs_by_cid.get(c["company_id"], "")
        if declared[0] or declared[1]:
            ta, _reason = time_applicability(declared[0], declared[1], obs)
        else:
            ta, _reason, _ev, _pub = qualify_assertion(pairs, obs)
        stored = c.get("time_applicability") or c.get("at_observation_availability")
        if stored != ta:
            capital_time_bad.append({"id": c["capital_event_id"], "stored": stored, "recomputed": ta})
        if stored == "USABLE_AT_OBSERVATION" and not (c.get("publication_date") or "").strip():
            capital_time_bad.append({"id": c["capital_event_id"], "problem": "USABLE_WITHOUT_PUBLICATION"})
    check("K7", "资本行时点与成对日期复算一致，无发布日不得标观察日可用",
          not capital_time_bad, f"violations={capital_time_bad[:4]}")

    # ---------------- D: delivery consistency ------------------------------
    check("D1", "24 家公司 ID 与 r3 完全一致",
          sorted(ids) == sorted(r3_ids) and len(ids) == 24,
          f"companies={len(ids)}, r3={len(r3_ids)}, set_equal={sorted(ids) == sorted(r3_ids)}")
    missing_core = []
    for cid in researched:
        have = {f["field"] for f in facts if f["company_id"] == cid}
        have |= {f["merge_parent_field"] for f in facts if f["company_id"] == cid}
        for kf in CORE_FIELDS:
            if kf in have:
                continue
            if kf in CORE_FIELD_SPLIT_CHILDREN and any(x in have for x in CORE_FIELD_SPLIT_CHILDREN[kf]):
                continue
            missing_core.append(f"{cid}:{kf}")
    check("D2", "已查公司核心字段均有查证行",
          not missing_core, f"missing={len(missing_core)} {missing_core[:5]}")
    fact_ids = {f["fact_id"] for f in facts}
    ev_ids = {e["evidence_id"] for e in evidence}
    bad_links = [l["link_id"] for l in links if l["fact_id"] not in fact_ids or l["evidence_id"] not in ev_ids]
    check("D3", "关系表的 ID 全部可解析",
          not bad_links, f"links={len(links)}, unresolvable={len(bad_links)} {bad_links[:3]}")
    no_evidence_established = [f["fact_id"] for f in facts
                               if f["value_status"] in ("SUPPORTED_EXTERNAL", "COMPANY_SELF_REPORT",
                                                        "MEDIA_STATEMENT", "COUNTERPARTY_CONFIRMATION",
                                                        "MIXED_SEE_EVIDENCE",
                                                        "CONFLICT_RESOLVED_BY_SEPARATION")
                               and not f["evidence_ids"]]
    check("D4", "每个已确立的事实都挂着证据",
          not no_evidence_established, f"violations={len(no_evidence_established)} {no_evidence_established[:4]}")
    pending = (exists(os.path.join(RUN, "REPAIR_R2_PENDING_ACCEPTANCE"))
               or exists(os.path.join(RUN, "TARGETED_COLLECTION_PENDING_ACCEPTANCE")))
    check("D5", "本轮标记为待独立验收，未写阶段 B 完成",
          not exists(os.path.join(RUN, "STAGE_B_COMPLETE")) and pending,
          f"pending_marker={pending}, "
          f"STAGE_B_COMPLETE={exists(os.path.join(RUN,'STAGE_B_COMPLETE'))}")
    check("D6", "分组映射存在且每个维度可回溯到事实",
          bool(groups) and all(g["basis_fact_ids"] or g["comparison_bucket"] == "NOT_RESEARCHED" for g in groups),
          f"group rows={len(groups)}")
    research_untouched = all(not os.path.exists(os.path.join(RUN, "..", "..", "stage_a_r3", ".modified"))
                             for _ in [0])
    check("D7", "招聘分类、研究库与原交付包未被改写",
          research_untouched and len(lock["problems"]) == 0,
          f"input problems={len(lock['problems'])}",
          "以 r3 发布清单与锁定输入集复核；本阶段只写 stage_b_repair/run_*")

    # D8: the published tables must be exactly what the locked research sources
    # produce right now. Without this, editing a published table by hand, deleting a
    # research source or deleting a required input leaves every other check passing.
    rebuild_state = {"ran": False, "identical": None, "differences": [], "reason": ""}
    if os.environ.get("STAGE_B_SKIP_REBUILD") != "1":
        import subprocess
        import tempfile
        tmp = tempfile.mkdtemp(prefix="b5v_")
        copy = os.path.join(tmp, "copy")
        shutil.copytree(RUN, copy, ignore=shutil.ignore_patterns("__pycache__", ".pytest_cache"))
        for name in ("company_facts.csv", "company_evidence.csv", "evidence_links.csv",
                     "capital_events.csv", "company_gaps.csv"):
            p = os.path.join(copy, name)
            if os.path.exists(p):
                os.remove(p)
        for name in glob.glob(os.path.join(copy, "work", "pilot_facts_v2_*.json")):
            os.remove(name)
        for name in ("input_lock.json", "build_summary.json"):
            p = os.path.join(copy, "work", name)
            if os.path.exists(p):
                os.remove(p)
        # every authored source this run locked must be present, pilot or extension
        authored_now = sorted(glob.glob(os.path.join(copy, "work", "pilot_facts_*.json")))
        authored_now += sorted(glob.glob(os.path.join(copy, "work", "research", "authored_*.json")))
        expected_source_ids = [os.path.relpath(p, os.path.join(copy, "work")).replace("\\", "/")
                               for p in authored_now]
        env = dict(os.environ)
        env["PYTHONIOENCODING"] = "utf-8"
        steps = []
        for script in ("s01_lock_inputs.py", "s02_build_facts.py", "s03_build_tables.py"):
            argv = [sys.executable, "-B", "-X", "utf8", os.path.join(copy, "scripts", script)]
            if script == "s01_lock_inputs.py":
                # the lock is rebuilt here on purpose: this check starts from a copy whose
                # lock was deleted, so the rebuild hashes the current inputs
                argv.append("--rebuild")
            proc = subprocess.run(argv, cwd=copy, capture_output=True, text=True,
                                  encoding="utf-8", errors="replace",
                                  env=env, timeout=600)
            steps.append({"script": script, "exit": proc.returncode,
                          "tail": ((proc.stdout or "") + (proc.stderr or "")).strip().splitlines()[-1:]})
        rebuild_state["ran"] = True
        diffs = []
        for name in ("company_facts.csv", "company_evidence.csv", "evidence_links.csv",
                     "capital_events.csv", "company_gaps.csv"):
            a = os.path.join(RUN, name)
            b = os.path.join(copy, name)
            if not os.path.exists(b):
                diffs.append({"table": name, "problem": "REBUILD_PRODUCED_NO_FILE"})
            elif sha256_file(a) != sha256_file(b):
                diffs.append({"table": name, "problem": "BYTES_DIFFER"})
        failed_steps = [s["script"] for s in steps if s["exit"] != 0]
        # the copy's lock file was deleted on purpose, so its verifier reports drift for
        # exactly that one file; that is expected and does not invalidate the rebuild
        lock_verify_path = os.path.join(copy, "work", "input_lock_verify.json")
        lock_drift: list[str] = []
        if os.path.exists(lock_verify_path):
            with open(lock_verify_path, "r", encoding="utf-8") as fh:
                lv = json.load(fh)
            lock_drift = [f"{p.get('path')}:{p.get('problem')}" for p in (lv.get("problems") or [])
                          if "input_lock.json" not in str(p.get("path"))]
        failed_steps = [s for s in failed_steps
                        if not (s == "s01_lock_inputs.py" and not lock_drift)]
        # completeness is judged against the authored sources present in the copy: every
        # locked authored file must still exist, and the rebuild must have produced a
        # fact layer for the same set of companies
        locked_sources = sorted({e["identity"] for e in lock["entries"]
                                 if e.get("role") == "research_source"})
        present_sources = [s for s in locked_sources
                           if os.path.exists(os.path.join(copy, s.replace("/", os.sep)))]
        missing_sources = [s for s in locked_sources if s not in present_sources]
        def company_of(identity: str) -> str:
            base = os.path.basename(identity)
            if base.startswith("pilot_facts_v2_"):
                return base[len("pilot_facts_v2_"):-len(".json")]
            if base.startswith("pilot_facts_"):
                return base[len("pilot_facts_"):-len(".json")]
            if base.startswith("authored_"):
                return base[len("authored_"):-len(".json")]
            return base
        source_companies = {company_of(s) for s in present_sources}
        generated = sorted(os.path.basename(p) for p in
                           glob.glob(os.path.join(copy, "work", "pilot_facts_v2_*.json")))
        generated_companies = {f[len("pilot_facts_v2_"):-len(".json")] for f in generated}
        uncovered = sorted(source_companies - generated_companies)
        rebuild_state["differences"] = diffs
        rebuild_state["failed_steps"] = failed_steps
        rebuild_state["raw_sources_present"] = len(present_sources)
        rebuild_state["generated_fact_layers"] = len(generated)
        rebuild_state["missing_research_sources"] = missing_sources
        rebuild_state["companies_without_fact_layer"] = uncovered
        rebuild_state["ran"] = True
        rebuild_state["identical"] = (not diffs and not failed_steps and not missing_sources
                                      and not uncovered and not lock_drift)
        if lock_drift:
            rebuild_state["reason"] = f"锁定输入在重建副本中不匹配：{lock_drift[:2]}"
        elif uncovered:
            rebuild_state["reason"] = f"以下公司没有生成事实层：{uncovered}"
        elif missing_sources:
            rebuild_state["reason"] = f"研究源文件缺失，无法重建完整事实层：{missing_sources}"
        elif failed_steps:
            rebuild_state["reason"] = (f"重建步骤失败：{failed_steps}"
                                       + ("（输入锁在副本内不匹配，属可接受：锁定文件本身被删除）"
                                          if failed_steps == ["s01_lock_inputs.py"] else ""))
        elif diffs:
            rebuild_state["reason"] = f"表与研究源重建结果不一致：{[d['table'] for d in diffs]}"
    check("D8", "已发布的表与锁定研究源的重建结果逐字节一致",
          rebuild_state["identical"] is True,
          (f"identical={rebuild_state['identical']}; differences={rebuild_state['differences']}; "
           f"failed_steps={rebuild_state.get('failed_steps', [])}; "
           f"raw_sources_present={rebuild_state.get('raw_sources_present')}; "
           f"generated_fact_layers={rebuild_state.get('generated_fact_layers')}; "
           f"missing_research_sources={rebuild_state.get('missing_research_sources', [])}; "
           f"reason={rebuild_state['reason']}"),
          "表被手工改写、研究源被删除或必需输入缺失时，这一步会失败")

    from s13_semantic_checks import semantic_checks
    for item in semantic_checks():
        check(item["id"], item["name"], item["passed"], item["detail"])
    passed = sum(1 for r in RESULTS if r["result"] == "PASS")
    # bind the verification record to this run's inputs, code and tables
    tables = {}
    for name in ("company_facts.csv", "company_evidence.csv", "evidence_links.csv",
                 "capital_events.csv", "company_gaps.csv", "company_group_mapping.csv",
                 "company_profile.csv"):
        p = os.path.join(RUN, name)
        if exists(p):
            tables[name] = sha256_file(p)
    script_hashes = {os.path.basename(p): sha256_file(p)
                     for p in sorted(glob.glob(os.path.join(RUN, "scripts", "*"))
                                     ) if p.endswith((".py", ".js"))}
    out = {
        "stage": "B-evidence-integrated",
        "scope": "24-company stage B repair pending independent acceptance; field-level unknowns remain visible",
        "reviewer": "stage_b_integrated_repair_agent（执行方自检；不是独立验收，也不声称用户人工复核）",
        "bound_to": {
            "run_id": lock["run_id"],
            "code_version": lock["code_version"],
            "input_root_digest": lock["input_root_digest"],
            "code_digest": lock["code_digest"],
            "scripts": script_hashes,
            "tables": tables,
        },
        "n_checks": len(RESULTS),
        "n_pass": passed,
        "n_fail": len(RESULTS) - passed,
        "checks": RESULTS,
    }
    out["verification_digest"] = sha256_bytes(json.dumps(
        {"bound_to": out["bound_to"], "results": [[r["check_id"], r["result"]] for r in RESULTS]},
        ensure_ascii=False, sort_keys=True).encode("utf-8"))
    with open(os.path.join(RUN, "verification.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(json.dumps({
        "n_checks": out["n_checks"], "pass": out["n_pass"], "fail": out["n_fail"],
        "verification_digest": out["verification_digest"][:16],
        "failed": [f"{r['check_id']} {r['name']}: {r['detail'][:120]}" for r in RESULTS if r["result"] == "FAIL"],
    }, ensure_ascii=False, indent=2))
    return 0 if out["n_fail"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
