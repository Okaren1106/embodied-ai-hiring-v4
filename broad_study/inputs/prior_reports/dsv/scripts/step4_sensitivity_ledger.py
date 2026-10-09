#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Stage D step 4.

Sensitivity ledger for the core candidate explanations: company-equal vs
ad-weighted, all-24 vs whole-23, leave-one-company-out, catalog direct subset,
source-complete subset, and the unknown-value scenarios P/B and (P+U)/B.

Scenario ranges only restate the extreme assignments of existing pending
records; they are not confidence intervals or demand ranges.
"""
from __future__ import annotations

import csv
import json
from collections import defaultdict
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


jobs = read(C / "inputs/rules_v1/inputs/stage_a/jobs.csv")
t1 = read(C / "tables/T1_company_sample.csv")
t2 = read(C / "tables/T2_company_primary_roles.csv")
t3adm = read(C / "tables/T3_base_admission.csv")
t3lin = read(C / "tables/T3_positive_unknown_lineage.csv")
t4adm = read(C / "tables/T4_activity_admission.csv")
t4lin = read(C / "tables/T4_activity_lineage.csv")
structure = json.loads((RUN / "cases/case_selection.json").read_text(encoding="utf-8"))

companies = {r["company_id"]: r for r in t1}
WHOLE = sorted(c for c, r in companies.items() if r["scope_main_company"] == "YES")
jobs_by_id = {j["identity_key"]: j for j in jobs}
concrete = {r["class_code"] for r in t2 if r["class_kind"] == "concrete"}
fname = {r["class_code"]: r["class_name"] for r in t2}
primary_of = {i: (jobs_by_id[i]["primary_code"] if jobs_by_id[i]["primary_status"] == "CODED"
                  else jobs_by_id[i]["primary_status"]) for i in jobs_by_id}
eligible = {r["identity_key"] for r in t4adm if r["base_eligible"] == "YES"}
owned = defaultdict(set)
for r in t4lin:
    if r["relation"] == "OWNED" and r["identity_key"] in eligible:
        owned[r["label_code"]].add(r["identity_key"])
aname = {}
for r in read(C / "tables/T4_activity_aggregates.csv"):
    aname[r["label_code"]] = r["label_name"]

# Q2 cell machinery
base_by_id = defaultdict(set)
dim_status = {}
for r in t3adm:
    if r["base_eligible"] == "YES":
        base_by_id[r["identity_key"]].add((r["role_code"], r["dimension"]))
        dim_status[(r["identity_key"], r["role_code"], r["dimension"])] = r["dimension_status"]
cell_pres = defaultdict(set)
cell_unk = defaultdict(set)
for r in t3lin:
    key = (r["role_code"], r["dimension"], r["label_code"], r["metric_bucket"], r["branch_bucket"])
    (cell_pres if r["state"] == "PRESENT" else cell_unk)[key].add(r["identity_key"])


def q2_cell(role, dim, lab, mb, bb, scope="WHOLE23", subset=None):
    ids = {i for i in jobs_by_id
           if (scope == "ALL24" or jobs_by_id[i]["company_id"] in set(WHOLE))
           and (role, dim) in base_by_id.get(i, set())}
    if subset == "CATALOG_DIRECT":
        ids = {i for i in ids if dim_status.get((i, role, dim)) in ("CODED", "NOT_MENTIONED")}
    elif subset == "SOURCE_COMPLETE":
        ids = {i for i in ids if pick_source_complete(i)}
    key = (role, dim, lab, mb, bb)
    pres = cell_pres.get(key, set()) & ids
    unk = cell_unk.get(key, set()) & ids
    interp = ids - unk
    comps = sorted({jobs_by_id[i]["company_id"] for i in interp})
    eq = (round(sum(q2_cell_by_company(c, role, dim, lab, mb, bb, subset) for c in comps) / len(comps), 10)
          if comps else None)
    return {"n_base": len(ids), "n_positive": len(pres), "n_unknown": len(unk),
            "n_interpretable": len(interp),
            "ad_weighted": ratio(len(pres), len(interp)),
            "company_equal": eq,
            "scenario_low_P_over_B": ratio(len(pres), len(ids)),
            "scenario_high_P_plus_U_over_B": ratio(len(pres) + len(unk), len(ids)),
            "n_companies": len(comps)}


def q2_cell_by_company(company_id, role, dim, lab, mb, bb, subset=None):
    ids = {i for i in jobs_by_id
           if jobs_by_id[i]["company_id"] == company_id and (role, dim) in base_by_id.get(i, set())}
    if subset == "CATALOG_DIRECT":
        ids = {i for i in ids if dim_status.get((i, role, dim)) in ("CODED", "NOT_MENTIONED")}
    elif subset == "SOURCE_COMPLETE":
        ids = {i for i in ids if pick_source_complete(i)}
    if not ids:
        return 0.0
    key = (role, dim, lab, mb, bb)
    interp = ids - (cell_unk.get(key, set()) & ids)
    if not interp:
        return 0.0
    return len(cell_pres.get(key, set()) & interp) / len(interp)


# source-complete inclusion rule, fixed before reading the target results
SOURCE_RULE = {
    "rule_id": "SRCCOMPLETE_V1",
    "criteria": [
        "公司招聘数据质量分为EXCELLENT或GOOD",
        "公司primary/activities来源不足广告为0",
        "该广告full_description_chars>=200",
    ],
    "note": "按覆盖证据决定纳入，不按活动数量多或正文更长挑选；正文长度只用于解释测量机会",
}
SOURCE_OK_COMPANY = {r["company_id"] for r in t1
                     if r["hiring_data_quality_score"] in ("EXCELLENT", "GOOD")
                     and num(r["primary_SOURCE_UNASSESSABLE"]) == 0
                     and num(r["activities_SOURCE_UNASSESSABLE"]) == 0}


def pick_source_complete(ik):
    j = jobs_by_id[ik]
    return (j["company_id"] in SOURCE_OK_COMPANY and num(j["full_description_chars"]) >= 200)


# -------------------------------------------------- activity metric helper
def activity_metric(act, scope="ALL24", subset=None, drop=None):
    ids = {i for i in eligible if scope == "ALL24" or jobs_by_id[i]["company_id"] in set(WHOLE)}
    if subset == "SOURCE_COMPLETE":
        ids = {i for i in ids if pick_source_complete(i)}
    if drop:
        ids = {i for i in ids if jobs_by_id[i]["company_id"] != drop}
    pos = owned[act] & ids
    return {"n_assessable": len(ids), "n_positive": len(pos), "share": ratio(len(pos), len(ids))}


# -------------------------------------------------- duplicate co-occurrence
# The joint indicator counts only adjudicated UNCONDITIONAL co-ownership, the
# same basis as the Stage D step 1 table; raw co-occurrence is kept alongside.
joint_lineage = read(RUN / "tables/D4_activity_pair_lineage.csv")
UNCOND = defaultdict(set)
JOINT_STATUS = defaultdict(lambda: defaultdict(int))
for r in joint_lineage:
    JOINT_STATUS[r["pair_id"]][r["status"]] += 1
    if r["status"] == "UNCONDITIONAL":
        UNCOND[r["pair_id"]].add(r["identity_key"])


def pair_metric(pid, a, b, scope="ALL24", subset=None, drop=None):
    ids = {i for i in eligible if scope == "ALL24" or jobs_by_id[i]["company_id"] in set(WHOLE)}
    if subset == "SOURCE_COMPLETE":
        ids = {i for i in ids if pick_source_complete(i)}
    if drop:
        ids = {i for i in ids if jobs_by_id[i]["company_id"] != drop}
    both = (owned[a] & owned[b]) & ids
    uncond = UNCOND[pid] & ids
    return {"n_assessable": len(ids), "n_both": len(uncond), "n_both_raw": len(both),
            "share": ratio(len(uncond), len(ids)), "share_raw": ratio(len(both), len(ids))}


DISPLAY_Q2 = [
    ("ML_TRAINING_INFERENCE", "RF_ML_AI_ENGINEERING", "technical_concepts", "TC_ML_SYSTEMS",
     "DUTY_OWN_DEVELOP", "UNCONDITIONAL"),
    ("ML_FOUNDATION_VLA", "RF_ML_AI_ENGINEERING", "technical_concepts", "TC_FOUNDATION_MODEL",
     "DUTY_OWN_DEVELOP", "UNCONDITIONAL"),
    ("ML_DATA_PIPELINE", "RF_ML_AI_ENGINEERING", "technical_concepts", "TC_DATA_PIPELINE",
     "DUTY_OWN_DEVELOP", "UNCONDITIONAL"),
    ("ML_PYTHON_GENERAL", "RF_ML_AI_ENGINEERING", "skills", "SK_PYTHON", "GENERAL", "UNCONDITIONAL"),
    ("ML_PYTORCH_GENERAL", "RF_ML_AI_ENGINEERING", "skills", "SK_PYTORCH", "GENERAL", "UNCONDITIONAL"),
    ("ML_PYTORCH_EXAMPLE", "RF_ML_AI_ENGINEERING", "skills", "SK_PYTORCH", "GENERAL", "EXAMPLE"),
    ("SW_RELIABILITY", "RF_ROBOTICS_SOFTWARE", "technical_concepts", "TC_RELIABILITY",
     "DUTY_OWN_DEVELOP", "UNCONDITIONAL"),
    ("SW_REALTIME", "RF_ROBOTICS_SOFTWARE", "technical_concepts", "TC_REALTIME",
     "DUTY_OWN_DEVELOP", "UNCONDITIONAL"),
    ("SW_LINUX_GENERAL", "RF_ROBOTICS_SOFTWARE", "skills", "SK_LINUX", "GENERAL", "UNCONDITIONAL"),
    ("SW_CPP_GENERAL", "RF_ROBOTICS_SOFTWARE", "skills", "SK_CPP", "GENERAL", "UNCONDITIONAL"),
    ("SW_PYTHON_GENERAL", "RF_ROBOTICS_SOFTWARE", "skills", "SK_PYTHON", "GENERAL", "UNCONDITIONAL"),
]

ledger = []
for name, role, dim, lab, mb, bb in DISPLAY_Q2:
    base = q2_cell(role, dim, lab, mb, bb, "WHOLE23")
    all24 = q2_cell(role, dim, lab, mb, bb, "ALL24")
    cat = q2_cell(role, dim, lab, mb, bb, "WHOLE23", "CATALOG_DIRECT")
    src = q2_cell(role, dim, lab, mb, bb, "WHOLE23", "SOURCE_COMPLETE")
    loo = []
    for c in WHOLE:
        ids = {i for i in jobs_by_id if (role, dim) in base_by_id.get(i, set())
               and jobs_by_id[i]["company_id"] in set(WHOLE) and jobs_by_id[i]["company_id"] != c}
        key = (role, dim, lab, mb, bb)
        pres = cell_pres.get(key, set()) & ids
        unk = cell_unk.get(key, set()) & ids
        interp = ids - unk
        loo.append((ratio(len(pres), len(interp)), c))
    loo_ok = [(v, c) for v, c in loo if v is not None]
    ledger.append({
        "metric_id": name, "q": "Q2", "role": role, "label": lab or name,
        "definition": f"{mb}|{bb} 正向数/最终可解释分母",
        "scope": "WHOLE23",
        "n_positive": base["n_positive"], "n_unknown": base["n_unknown"],
        "n_interpretable": base["n_interpretable"], "n_base": base["n_base"],
        "value_ad_weighted": base["ad_weighted"], "value_company_equal": base["company_equal"],
        "scenario_low_P_over_B": base["scenario_low_P_over_B"],
        "scenario_high_P_plus_U_over_B": base["scenario_high_P_plus_U_over_B"],
        "s_all24_ad_weighted": all24["ad_weighted"],
        "s_catalog_direct_ad_weighted": cat["ad_weighted"],
        "s_source_complete_subset_ad_weighted": src["ad_weighted"],
        "s_source_complete_n": src["n_interpretable"],
        "s_loo_min": min(loo_ok)[0] if loo_ok else None,
        "s_loo_max": max(loo_ok)[0] if loo_ok else None,
        "s_loo_argmin_company": min(loo_ok)[1] if loo_ok else "",
        "s_loo_argmax_company": max(loo_ok)[1] if loo_ok else "",
        "n_companies": base["n_companies"],
    })

# Q3 activity metrics
Q3_METRICS = sorted(aname)
q3_ledger = []
for act in Q3_METRICS:
    base = activity_metric(act, "ALL24")
    whole = activity_metric(act, "WHOLE23")
    src = activity_metric(act, "ALL24", "SOURCE_COMPLETE")
    loo = [activity_metric(act, "ALL24", None, c)["share"] for c in WHOLE]
    loo_ok = [v for v in loo if v is not None]
    q3_ledger.append({
        "metric_id": f"Q3_{act}", "q": "Q3", "role": "", "label": aname.get(act, act),
        "definition": "OWNED正向广告数/活动可判读广告数",
        "scope": "ALL24",
        "n_positive": base["n_positive"], "n_unknown": "", "n_interpretable": base["n_assessable"],
        "n_base": base["n_assessable"],
        "value_ad_weighted": base["share"],
        "value_company_equal": round(sum(activity_metric(act, "ALL24", None, c)["share"] or 0
                                         for c in WHOLE) / len(WHOLE), 10),
        "scenario_low_P_over_B": base["share"],
        "scenario_high_P_plus_U_over_B": "",
        "s_all24_ad_weighted": base["share"],
        "s_whole23_ad_weighted": whole["share"],
        "s_catalog_direct_ad_weighted": "",
        "s_source_complete_subset_ad_weighted": src["share"],
        "s_source_complete_n": src["n_assessable"],
        "s_loo_min": min(loo_ok) if loo_ok else None,
        "s_loo_max": max(loo_ok) if loo_ok else None,
        "s_loo_argmin_company": min(((v, c) for v, c in zip(loo, WHOLE) if v is not None))[1] if loo_ok else "",
        "s_loo_argmax_company": max(((v, c) for v, c in zip(loo, WHOLE) if v is not None))[1] if loo_ok else "",
        "n_companies": len({jobs_by_id[i]["company_id"] for i in owned[act] & eligible}),
    })

# co-occurrence metrics
CO_METRICS = [("P1_RESEARCH_ENGINEERING", "ACT_RESEARCH", "ACT_ENGINEERING"),
              ("P2_ENGINEERING_QUALITY", "ACT_ENGINEERING", "ACT_QUALITY"),
              ("P3_ENGINEERING_DEPLOYMENT", "ACT_ENGINEERING", "ACT_DEPLOYMENT")]
co_ledger = []
for pid, a, b in CO_METRICS:
    base = pair_metric(pid, a, b, "ALL24")
    whole = pair_metric(pid, a, b, "WHOLE23")
    src = pair_metric(pid, a, b, "ALL24", "SOURCE_COMPLETE")
    loo = [pair_metric(pid, a, b, "ALL24", None, c)["share"] for c in WHOLE]
    loo_ok = [v for v in loo if v is not None]
    st = JOINT_STATUS[pid]
    co_ledger.append({
        "metric_id": pid, "q": "Q3-joint", "role": "",
        "label": f"{aname.get(a,a)}×{aname.get(b,b)}",
        "definition": "两活动均本人承担且关系判定为无条件同现的广告数/活动可判读广告数",
        "scope": "ALL24",
        "n_positive": base["n_both"], "n_unknown": st.get("UNRESOLVED", 0),
        "n_interpretable": base["n_assessable"], "n_base": base["n_assessable"],
        "n_raw_cooccurrence": base["n_both_raw"],
        "n_conditional": st.get("CONDITIONAL", 0),
        "n_alternative_only": st.get("ALTERNATIVE_ONLY", 0),
        "n_unresolved": st.get("UNRESOLVED", 0),
        "value_ad_weighted": base["share"],
        "value_company_equal": round(sum(pair_metric(pid, a, b, "ALL24", None, c)["share"] or 0
                                         for c in WHOLE) / len(WHOLE), 10),
        "scenario_low_P_over_B": "", "scenario_high_P_plus_U_over_B": "",
        "s_all24_ad_weighted": base["share"],
        "s_whole23_ad_weighted": whole["share"],
        "s_catalog_direct_ad_weighted": "",
        "s_source_complete_subset_ad_weighted": src["share"],
        "s_source_complete_n": src["n_assessable"],
        "s_loo_min": min(loo_ok) if loo_ok else None,
        "s_loo_max": max(loo_ok) if loo_ok else None,
        "s_loo_argmin_company": min(((v, c) for v, c in zip(loo, WHOLE) if v is not None))[1] if loo_ok else "",
        "s_loo_argmax_company": max(((v, c) for v, c in zip(loo, WHOLE) if v is not None))[1] if loo_ok else "",
        "n_companies": len({jobs_by_id[i]["company_id"] for i in UNCOND[pid] & eligible}),
    })

fields = list(ledger[0].keys())
for row in q3_ledger + co_ledger:
    for k in row:
        if k not in fields:
            fields.append(k)
for row in ledger + q3_ledger + co_ledger:
    for f in fields:
        row.setdefault(f, "")
write("D9_sensitivity_ledger.csv", ledger + q3_ledger + co_ledger, fields)

# ------------------------------------------------- case-pair sensitivities
CASE_SENS = []
G1 = structure["selected_groups"]["G1_MANUFACTURING_LINE"]
CASES_ALL = structure["selected"]
deploy_rows = []
for scope in ("ALL24", "WHOLE23"):
    for tag, subset in (("BASE", None), ("SOURCE_COMPLETE", "SOURCE_COMPLETE")):
        d = {}
        for c in CASES_ALL:
            ids = {i for i in eligible
                   if (scope == "ALL24" or jobs_by_id[i]["company_id"] in set(WHOLE))
                   and jobs_by_id[i]["company_id"] == c}
            if subset == "SOURCE_COMPLETE":
                ids = {i for i in ids if pick_source_complete(i)}
            d[(c, "ALL")] = (len(ids), len(ids & owned["ACT_DEPLOYMENT"]))
            for f in ("RF_ML_AI_ENGINEERING", "RF_CORPORATE_SUPPORT"):
                inside = {i for i in ids if primary_of[i] == f}
                d[(c, f)] = (len(inside), len(inside & owned["ACT_DEPLOYMENT"]))
        row = {"comparison": "CASE_DEPLOYMENT_ACTIVITY", "scope": scope, "subset": tag}
        for c in CASES_ALL:
            row[f"{c}_n"] = d[(c, "ALL")][0]
            row[f"{c}_pos"] = d[(c, "ALL")][1]
            row[f"{c}_ML_n"] = d[(c, "RF_ML_AI_ENGINEERING")][0]
            row[f"{c}_ML_pos"] = d[(c, "RF_ML_AI_ENGINEERING")][1]
            row[f"{c}_SUP_n"] = d[(c, "RF_CORPORATE_SUPPORT")][0]
            row[f"{c}_SUP_pos"] = d[(c, "RF_CORPORATE_SUPPORT")][1]
            row[f"{c}_share_all"] = ratio(d[(c, "ALL")][1], d[(c, "ALL")][0])
            row[f"{c}_share_ML"] = ratio(d[(c, "RF_ML_AI_ENGINEERING")][1], d[(c, "RF_ML_AI_ENGINEERING")][0])
            row[f"{c}_share_SUP"] = ratio(d[(c, "RF_CORPORATE_SUPPORT")][1], d[(c, "RF_CORPORATE_SUPPORT")][0])
        deploy_rows.append(row)
write("D9b_case_deployment_sensitivity.csv", deploy_rows, list(deploy_rows[0].keys()))

# -------------------------------------------------- unknown scenario table
BOOK_REFERENCE = {
    "ML_PYTHON_GENERAL": (60, 23, 156),
    "SW_LINUX_GENERAL": (70, 3, 180),
    "SW_CPP_GENERAL": (42, 30, 180),
    "SW_PYTHON_GENERAL": (35, 15, 180),
}
unknown_rows = []
for name, role, dim, lab, mb, bb in DISPLAY_Q2:
    if name not in BOOK_REFERENCE:
        continue
    c = q2_cell(role, dim, lab, mb, bb, "WHOLE23")
    exp = BOOK_REFERENCE[name]
    unknown_rows.append({
        "metric_id": name,
        "n_positive": c["n_positive"], "n_unknown": c["n_unknown"], "n_base": c["n_base"],
        "n_interpretable": c["n_interpretable"],
        "book_reference_P_U_B": f"{exp[0]}/{exp[1]}/{exp[2]}",
        "matches_book_reference": "YES" if (c["n_positive"], c["n_unknown"], c["n_base"]) == exp else "NO",
        "scenario_low_P_over_B": ratio(c["n_positive"], c["n_base"]),
        "scenario_high_P_plus_U_over_B": ratio(c["n_positive"] + c["n_unknown"], c["n_base"]),
        "official_share_P_over_P_plus_Z": ratio(c["n_positive"], c["n_interpretable"]),
        "note": "情景仅为现有待解释记录的极端赋值，不是置信区间、真实需求范围或缺采校正",
    })
write("D9c_unknown_scenarios.csv", unknown_rows, list(unknown_rows[0].keys()))

checks = {
    "source_complete_rule": SOURCE_RULE,
    "n_source_complete_companies": len(SOURCE_OK_COMPANY),
    "source_complete_company_list": sorted(SOURCE_OK_COMPANY),
    "n_ads_source_complete": sum(1 for j in jobs if pick_source_complete(j["identity_key"])),
    "q2_ledger": [{k: r[k] for k in ("metric_id", "n_positive", "n_unknown", "n_interpretable",
                                     "value_ad_weighted", "value_company_equal",
                                     "scenario_low_P_over_B", "scenario_high_P_plus_U_over_B",
                                     "s_source_complete_subset_ad_weighted",
                                     "s_loo_min", "s_loo_max")} for r in ledger],
    "unknown_scenarios": unknown_rows,
    "case_deployment": deploy_rows,
}
(VER / "step4_checks.json").write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(checks, ensure_ascii=False, indent=2)[:4000])
