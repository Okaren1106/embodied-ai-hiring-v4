#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Stage D step 3.

Company point values (Q1/Q2/Q3), the restricted common-function (K) weighted
comparison for the selected case pair, within-function activity rates, and the
case-level work-object / seniority appendix derived by keyword rule.

All denominators follow the fixed Stage C / Q2 v1 rules. Restricted comparison
only answers differences inside the common-function coverage; it never
replaces the whole-company result, and no zero is padded for missing functions.
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
import os
from pathlib import Path

RUN = Path(__file__).resolve().parent.parent


def _resolve_base(run: Path) -> Path:
    """Input root: explicit env wins, then the run's own input_lock.json."""
    env = os.environ.get("STAGE_D_BASE")
    if env:
        return Path(env)
    lock = run / "input_lock.json"
    if lock.is_file():
        try:
            recorded = json.loads(lock.read_text(encoding="utf-8")).get("base_dir")
        except (OSError, json.JSONDecodeError):
            recorded = None
        if recorded:
            return Path(recorded)
    return run.parents[1]


BASE = _resolve_base(RUN)
C = BASE / "stage_c/run_20260915T105656Z"
R = BASE / "analysis_rules_v1/run_20260915T085828Z"

TAB = RUN / "tables"
VER = RUN / "verification"


def read(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write(name, rows, fields):
    with (TAB / name).open("w", encoding="utf-8-sig", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        wr.writeheader()
        for row in rows:
            wr.writerow(row)


def num(v, d=0):
    return int(v) if v not in (None, "", "NA") else d


def ratio(a, b):
    return None if not b else round(a / b, 10)


# --------------------------------------------------------------- inputs
jobs = read(C / "inputs/rules_v1/inputs/stage_a/jobs.csv")
t1 = read(C / "tables/T1_company_sample.csv")
t2 = read(C / "tables/T2_company_primary_roles.csv")
t3adm = read(C / "tables/T3_base_admission.csv")
t3lin = read(C / "tables/T3_positive_unknown_lineage.csv")
t4co = read(C / "tables/T4_activity_company.csv")
t4adm = read(C / "tables/T4_activity_admission.csv")
t4lin = read(C / "tables/T4_activity_lineage.csv")
selection = json.loads((RUN / "cases/case_selection.json").read_text(encoding="utf-8"))

companies = {r["company_id"]: r for r in t1}
jobs_by_id = {j["identity_key"]: j for j in jobs}
concrete = {r["class_code"] for r in t2 if r["class_kind"] == "concrete"}
fname = {r["class_code"]: r["class_name"] for r in t2}
eligible = {r["identity_key"] for r in t4adm if r["base_eligible"] == "YES"}
primary_of = {i: (jobs_by_id[i]["primary_code"] if jobs_by_id[i]["primary_status"] == "CODED"
                  else jobs_by_id[i]["primary_status"]) for i in jobs_by_id}
owned = defaultdict(set)
for r in t4lin:
    if r["relation"] == "OWNED" and r["identity_key"] in eligible:
        owned[r["label_code"]].add(r["identity_key"])
ACTIVITIES = sorted(owned)
aname = {}
for r in t4co:
    aname[r["label_code"]] = r["label_name"]

CASES = selection["selected"]
G1 = selection["selected_groups"]["G1_MANUFACTURING_LINE"]
G2 = selection["selected_groups"]["G2_LOGISTICS_WAREHOUSE"]

# ------------------------------------------------- D8a company points
rows = []
for cid, c in sorted(companies.items()):
    ids_ads = {j["identity_key"] for j in jobs if j["company_id"] == cid}
    ids_act = ids_ads & eligible
    rows.append({
        "scope": "COMPANY", "company_id": cid, "company_name": c["company_name"],
        "stratum": c["stratum_name"], "n_ads": c["n_ads"],
        "observation_date": c["observation_date_min"],
        "n_ads_activity_assessable": len(ids_act),
        "n_primary_concrete": sum(1 for i in ids_ads if primary_of[i] in concrete),
        "n_primary_composite": num(c["primary_composite"]),
        "n_primary_alternative": num(c["primary_alternative"]),
        "n_primary_ambiguous": num(c["primary_AMBIGUOUS"]),
        "n_primary_unmapped": num(c["primary_UNMAPPED"]),
        "n_primary_source_unassessable": num(c["primary_SOURCE_UNASSESSABLE"]),
    })
write("D8a_company_points.csv", rows, list(rows[0].keys()))

# ------------------------- D8b within-function activity rates per company
rate_rows = []
for cid, c in sorted(companies.items()):
    ids_act = {j["identity_key"] for j in jobs if j["company_id"] == cid} & eligible
    for code in sorted(concrete):
        sel = {i for i in ids_act if primary_of[i] == code}
        if len(sel) < 10:
            continue
        for act in ACTIVITIES:
            pos = len(sel & owned[act])
            rate_rows.append({
                "company_id": cid, "company_name": c["company_name"],
                "primary_code": code, "primary_name": fname.get(code, code),
                "n_assessable_in_function": len(sel),
                "activity_code": act, "activity_name": aname.get(act, act),
                "n_positive": pos, "share_within_function": ratio(pos, len(sel)),
                "meets_ge10": "YES",
            })
write("D8b_within_function_activity_rates.csv", rate_rows, list(rate_rows[0].keys()))

# ------------------- D8c restricted common-function weighted comparison (K)
def k_compare(ca, cb, group):
    def funcs(cid):
        ids_act = {j["identity_key"] for j in jobs if j["company_id"] == cid} & eligible
        d = defaultdict(set)
        for i in ids_act:
            d[primary_of[i]].add(i)
        return {k: v for k, v in d.items() if k in concrete and len(v) >= 10}
    fa, fb = funcs(ca), funcs(cb)
    K = sorted(set(fa) & set(fb))
    out = []
    act_all = {c: {j["identity_key"] for j in jobs if j["company_id"] == c} & eligible for c in (ca, cb)}
    pooled = {f: len(fa[f]) + len(fb[f]) for f in K}
    pooled_total = sum(pooled.values())
    for act in ACTIVITIES:
        row = {"case_group": group, "activity_code": act, "activity_name": aname.get(act, act),
               "K_size": len(K), "K_functions": "|".join(K),
               "K_function_names": "|".join(fname.get(k, k) for k in K),
               "comparison_eligible": "YES" if len(K) >= 2 else "NO"}
        for c, f in ((ca, fa), (cb, fb)):
            n_total = len(act_all[c])
            n_in_k = sum(len(f[k]) for k in K)
            k_total = sum(len(f[k]) for k in K)
            rate_self = sum(len(f[k]) / k_total * (len(f[k] & owned[act]) / len(f[k])) for k in K) if k_total else None
            rate_equal = (sum(len(f[k] & owned[act]) / len(f[k]) for k in K) / len(K)) if K else None
            rate_pooled = (sum(pooled[k] / pooled_total * (len(f[k] & owned[act]) / len(f[k])) for k in K)
                           if pooled_total else None)
            row[f"{c}_n_assessable_all"] = n_total
            row[f"{c}_n_assessable_in_K"] = n_in_k
            row[f"{c}_K_coverage"] = ratio(n_in_k, n_total)
            row[f"{c}_n_positive_all"] = len(act_all[c] & owned[act])
            row[f"{c}_share_all"] = ratio(len(act_all[c] & owned[act]), n_total)
            row[f"{c}_share_self_weighted"] = round(rate_self, 10) if rate_self is not None else None
            row[f"{c}_share_equal_weighted"] = round(rate_equal, 10) if rate_equal is not None else None
            row[f"{c}_share_pooled_weighted"] = round(rate_pooled, 10) if rate_pooled is not None else None
            row[f"{c}_per_function_json"] = json.dumps(
                {k: {"n": len(f[k]), "positive": len(f[k] & owned[act]),
                     "rate": ratio(len(f[k] & owned[act]), len(f[k]))} for k in K}, ensure_ascii=False)
        a, b = ca, cb
        row["diff_self_weighted"] = (round(row[f"{a}_share_self_weighted"] - row[f"{b}_share_self_weighted"], 10)
                                     if row[f"{a}_share_self_weighted"] is not None
                                     and row[f"{b}_share_self_weighted"] is not None else None)
        row["diff_equal_weighted"] = (round(row[f"{a}_share_equal_weighted"] - row[f"{b}_share_equal_weighted"], 10)
                                      if row[f"{a}_share_equal_weighted"] is not None
                                      and row[f"{b}_share_equal_weighted"] is not None else None)
        row["diff_share_all"] = (round(row[f"{a}_share_all"] - row[f"{b}_share_all"], 10)
                                 if row[f"{a}_share_all"] is not None and row[f"{b}_share_all"] is not None else None)
        out.append(row)
    return out, K, fa, fb


k_rows, K1, fa1, fb1 = k_compare(G1[0], G1[1], "G1_MANUFACTURING_LINE")
write("D8c_common_function_weighted_comparison.csv", k_rows, list(k_rows[0].keys()))

k2_rows, K2, _, _ = k_compare(G2[0], G2[1], "G2_LOGISTICS_WAREHOUSE")
write("D8c2_common_function_weighted_comparison_G2.csv", k2_rows, list(k2_rows[0].keys()))

# ------------------------------- D8d company-level Q2 context points
base_by_id = defaultdict(set)
for r in t3adm:
    if r["base_eligible"] == "YES":
        base_by_id[r["identity_key"]].add((r["role_code"], r["dimension"]))
cell_pres = defaultdict(set)
cell_unk = defaultdict(set)
for r in t3lin:
    key = (r["role_code"], r["dimension"], r["label_code"], r["metric_bucket"], r["branch_bucket"])
    (cell_pres if r["state"] == "PRESENT" else cell_unk)[key].add(r["identity_key"])

DISPLAY = [
    ("RF_ML_AI_ENGINEERING", "technical_concepts", "TC_ML_SYSTEMS", "DUTY_OWN_DEVELOP", "UNCONDITIONAL"),
    ("RF_ML_AI_ENGINEERING", "technical_concepts", "TC_FOUNDATION_MODEL", "DUTY_OWN_DEVELOP", "UNCONDITIONAL"),
    ("RF_ML_AI_ENGINEERING", "technical_concepts", "TC_DATA_PIPELINE", "DUTY_OWN_DEVELOP", "UNCONDITIONAL"),
    ("RF_ML_AI_ENGINEERING", "skills", "SK_PYTHON", "GENERAL", "UNCONDITIONAL"),
    ("RF_ML_AI_ENGINEERING", "skills", "SK_PYTORCH", "GENERAL", "UNCONDITIONAL"),
    ("RF_ML_AI_ENGINEERING", "skills", "SK_PYTORCH", "GENERAL", "EXAMPLE"),
    ("RF_ROBOTICS_SOFTWARE", "technical_concepts", "TC_RELIABILITY", "DUTY_OWN_DEVELOP", "UNCONDITIONAL"),
    ("RF_ROBOTICS_SOFTWARE", "technical_concepts", "TC_REALTIME", "DUTY_OWN_DEVELOP", "UNCONDITIONAL"),
    ("RF_ROBOTICS_SOFTWARE", "skills", "SK_LINUX", "GENERAL", "UNCONDITIONAL"),
    ("RF_ROBOTICS_SOFTWARE", "skills", "SK_CPP", "GENERAL", "UNCONDITIONAL"),
    ("RF_ROBOTICS_SOFTWARE", "skills", "SK_PYTHON", "GENERAL", "UNCONDITIONAL"),
]
known = {(r["role_code"], r["dimension"], r["label_code"], r["metric_bucket"], r["branch_bucket"]): r["label_name"]
         for r in read(C / "tables/T3_aggregates.csv")}

q2_rows = []
for cid in CASES:
    c = companies[cid]
    ids = {j["identity_key"] for j in jobs if j["company_id"] == cid}
    for role, dim, lab, mb, bb in DISPLAY:
        base = {i for i in ids if (role, dim) in base_by_id.get(i, set())}
        known_key = (role, dim, lab, mb, bb)
        pres = {i for i in cell_pres.get(known_key, set()) if i in base}
        unk = {i for i in cell_unk.get(known_key, set()) if i in base}
        interp = base - unk
        q2_rows.append({
            "company_id": cid, "company_name": c["company_name"],
            "role_code": role, "dimension": dim, "label_code": lab,
            "label_name": known.get(known_key, lab),
            "metric_bucket": mb, "branch_bucket": bb,
            "n_base": len(base), "n_unknown": len(unk), "n_interpretable": len(interp),
            "n_positive": len(pres), "share": ratio(len(pres), len(interp)),
            "small_n_under10": "YES" if len(interp) < 10 else "NO",
            "zero_denominator": "YES" if len(interp) == 0 else "NO",
        })
write("D8d_case_q2_context_points.csv", q2_rows, list(q2_rows[0].keys()))

# --------------------- D8e work object and seniority appendix (rule based)
WORK_OBJECT_RULES = [
    ("WORKOBJ_ROBOT_SIDE", "机器人端", ("机器人本体", "整机", "关节", "灵巧手", "伺服", "机械臂", "本体", "驱动器",
                                   "robot", "manipulator", "actuator", "hardware bringup")),
    ("WORKOBJ_TRAIN_INFER_PLATFORM", "训练或推理平台", ("训练平台", "训练框架", "分布式训练", "推理", "集群", "GPU",
                                                 "CUDA", "算力", "inference", "training infrastructure",
                                                 "checkpoint", "并行")),
    ("WORKOBJ_DATA_SERVICE", "数据服务", ("数据采集", "数据集", "数据管线", "标注", "数据平台", "数据治理",
                                     "data pipeline", "dataset", "annotation")),
    ("WORKOBJ_CUSTOMER_SITE", "客户现场系统", ("客户现场", "现场部署", "交付", "驻场", "售后", "实施", "产线",
                                         "部署", "deployment", "on-site", "field")),
]
SENIORITY_RULES = [
    ("SENIOR_STAFF_PRINCIPAL", ("staff", "principal", "资深", "专家", "架构师", "负责人", "总监")),
    ("SENIOR_SENIOR", ("senior", "高级", "sr.")),
    ("ENTRY_INTERN", ("intern", "实习", "trainee")),
    ("ENTRY_CAMPUS", ("校招", "应届", "campus", "graduate")),
]
CASE_FUNCTIONS = {"RF_ML_AI_ENGINEERING", "RF_ROBOTICS_SOFTWARE"}

# Ad body text comes from the frozen merged baseline records file; the
# jobs.csv source_path column points at that whole file, not at a single ad.
BASELINE = (BASE.parents[1] / "outputs/reference-expansion-2026-09-11"
            / "merged-baseline-2026-09-11/records.jsonl")
body_by_record = {}
if BASELINE.is_file():
    with BASELINE.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            body_by_record[obj.get("record_id", "")] = obj.get("full_description", "") or ""

obj_rows = []
n_with_body = 0
for cid in CASES:
    c = companies[cid]
    for j in jobs:
        if j["company_id"] != cid:
            continue
        if j["primary_code"] not in CASE_FUNCTIONS or j["primary_status"] != "CODED":
            continue
        body = body_by_record.get(j["record_id"], "")
        if body:
            n_with_body += 1
        hay = (j["title"] + " " + body).lower()
        hits = [code for code, _, kws in WORK_OBJECT_RULES if any(k.lower() in hay for k in kws)]
        matched = "|".join(hits) if hits else "WORKOBJ_UNKNOWN"
        sen = [code for code, kws in SENIORITY_RULES if any(k.lower() in j["title"].lower() for k in kws)]
        obj_rows.append({
            "company_id": cid, "company_name": c["company_name"],
            "identity_key": j["identity_key"], "record_id": j["record_id"],
            "reading_id": j["reading_id"], "title": j["title"],
            "location": j["location"], "primary_code": j["primary_code"],
            "body_source": "MERGED_BASELINE_RECORDS" if body else "TITLE_ONLY",
            "body_chars": len(body),
            "work_object_codes": matched,
            "work_object_multi": "YES" if len(hits) > 1 else "NO",
            "seniority_codes": "|".join(sen) if sen else "SENIORITY_NOT_STATED",
            "derivation": "RULE_KEYWORD_V1: 标题与合并基线正文关键词派生；未匹配到正文的记录只按标题派生；"
                          "未说明不等于初级或零经验；不修改原四维分类",
        })
write("D8e_case_work_object_seniority.csv", obj_rows, list(obj_rows[0].keys()))

checks = {
    "cases": CASES,
    "G1_pair": G1, "G1_common_K": K1,
    "G1_K_sizes": {c: {fname.get(k, k): len(f.get(k, set())) for k in K1} for c, f in ((G1[0], fa1), (G1[1], fb1))},
    "G2_pair": G2, "G2_common_K": K2,
    "G2_comparison": "NOT_APPLICABLE_COMMON_K_BELOW_2",
    "n_q2_point_rows": len(q2_rows),
    "n_work_object_rows": len(obj_rows),
    "n_work_object_with_body": n_with_body,
    "baseline_records_file": str(BASELINE).replace("\\", "/"),
    "baseline_records_available": BASELINE.is_file(),
    "n_within_function_rows": len(rate_rows),
}
(VER / "step3_checks.json").write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(checks, ensure_ascii=False, indent=2)[:3000])

print("\n--- K weighted comparison (G1) key activities ---")
for r in k_rows:
    if r["activity_code"] in ("ACT_ENGINEERING", "ACT_QUALITY", "ACT_DEPLOYMENT",
                              "ACT_MANUFACTURING_SUPPLY", "ACT_RESEARCH", "ACT_BUSINESS"):
        print(r["activity_name"],
              "| all:", r[f"{G1[0]}_share_all"], r[f"{G1[1]}_share_all"],
              "| self-w:", r[f"{G1[0]}_share_self_weighted"], r[f"{G1[1]}_share_self_weighted"],
              "| eq-w:", r[f"{G1[0]}_share_equal_weighted"], r[f"{G1[1]}_share_equal_weighted"],
              "| diff-all:", r["diff_share_all"], "diff-self:", r["diff_self_weighted"])
print("\ncoverage:", [(c, r[f"{c}_n_assessable_all"], r[f"{c}_n_assessable_in_K"], r[f"{c}_K_coverage"])
                      for c in G1 for r in [k_rows[0]]])
