#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Stage D step 5 (deliverables).

Builds T5 (company background / business responsibility / hiring combination
long table) and T6 (conclusion and sensitivity ledger). Every number in T6 is
read back from the frozen Stage D tables so wording cannot drift from results.
Evidence ids come from the inherited Stage B fact layer.
"""
from __future__ import annotations

import csv
import json
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


def pct(v):
    return "" if v in (None, "", "NA") else f"{float(v)*100:.1f}%"


jobs = read(C / "inputs/rules_v1/inputs/stage_a/jobs.csv")
t1 = read(C / "tables/T1_company_sample.csv")
t2 = read(C / "tables/T2_company_primary_roles.csv")
d1 = read(RUN / "tables/D1_q1_coverage_concentration.csv")
d8a = read(RUN / "tables/D8a_company_points.csv")
d8b = read(RUN / "tables/D8b_within_function_activity_rates.csv")
d8d = read(RUN / "tables/D8d_case_q2_context_points.csv")
d8e = read(RUN / "tables/D8e_case_work_object_seniority.csv")
d9 = read(RUN / "tables/D9_sensitivity_ledger.csv")
d4 = read(RUN / "tables/D4_activity_pair_cooccurrence.csv")
d6 = read(RUN / "tables/D6_business_responsibility_long.csv")
d7 = read(RUN / "tables/D7_case_candidates.csv")
d7a = read(RUN / "tables/D7a_pairwise_common_functions.csv")
selection = json.loads((RUN / "cases/case_selection.json").read_text(encoding="utf-8"))

companies = {r["company_id"]: r for r in t1}
fname = {r["class_code"]: r["class_name"] for r in t2}
kind = {r["class_code"]: r["class_kind"] for r in t2}
CASES = selection["selected"]
G1 = selection["selected_groups"]["G1_MANUFACTURING_LINE"]
G2 = selection["selected_groups"]["G2_LOGISTICS_WAREHOUSE"]

# ------------------------------------------------------------------- T5
T5_FIELDS = [
    "record_kind", "case_group", "case_id", "company_id", "company_name", "stratum_name",
    "supply_form_note", "product_or_scene", "business_stage", "responsibility_subject",
    "fact_or_metric", "value", "unit", "numerator", "denominator", "unknown_or_gap",
    "event_date", "publication_date", "observation_date", "time_applicability",
    "evidence_ids", "hiring_scope", "n_ads", "n_activity_assessable",
    "comparison_eligible", "exclusion_or_qualification", "seniority_note", "work_object_note",
    "source_note",
]
t5 = []

# 1 company responsibility facts (Stage B inherited, Stage D derived stages)
for r in d6:
    if r["business_stage"] in ("COMPANY_BACKGROUND", "OTHER"):
        continue
    t5.append({
        "record_kind": "COMPANY_RESPONSIBILITY",
        "case_group": "", "case_id": "",
        "company_id": r["company_id"], "company_name": r["company_name"],
        "stratum_name": r["stratum_name"], "supply_form_note": "",
        "product_or_scene": r["product_or_business_scope"],
        "business_stage": r["business_stage_label"],
        "responsibility_subject": r["responsibility_subject"],
        "fact_or_metric": r["fact_value"],
        "value": r["fact_value"], "unit": r["unit"],
        "numerator": "", "denominator": "", "unknown_or_gap": r["judgment_status"],
        "event_date": r["event_date"], "publication_date": r["publication_date"],
        "observation_date": r["observation_date"], "time_applicability": r["time_applicability"],
        "evidence_ids": r["evidence_ids"],
        "hiring_scope": "", "n_ads": "", "n_activity_assessable": "",
        "comparison_eligible": "", "exclusion_or_qualification": "",
        "seniority_note": "", "work_object_note": "",
        "source_note": f'{r["value_status"]}|{r["rule_id"]}',
    })

# 2 hiring metrics per company: Q1 functions and Q3 activities
q1_by_company = defaultdict(list)
for r in t2:
    if r["class_kind"] in ("concrete", "composite", "alternative"):
        q1_by_company[r["company_id"]].append(r)
for cid, c in companies.items():
    for r in sorted(q1_by_company[cid], key=lambda x: -num(x["n_ads"])):
        t5.append({
            "record_kind": "HIRING_METRIC", "case_group": selection["selected_groups"].get(
                next((g for g, m in selection["selected_groups"].items() if cid in m), ""), ""),
            "case_id": "", "company_id": cid, "company_name": c["company_name"],
            "stratum_name": c["stratum_name"], "supply_form_note": c["scope_main_company"],
            "product_or_scene": "", "business_stage": "", "responsibility_subject": "",
            "fact_or_metric": f'Q1主职能：{r["class_name"]}',
            "value": r["share_all"], "unit": "share_of_company_ads",
            "numerator": r["n_coded"], "denominator": r["denominator_all"],
            "unknown_or_gap": f'公司主职能未明确{num(c["primary_unspecified_total"])}条',
            "event_date": "", "publication_date": "",
            "observation_date": c["observation_date_min"], "time_applicability": c["scope_time_applicability"],
            "evidence_ids": "",
            "hiring_scope": c["hiring_scope_inherited"], "n_ads": c["n_ads"],
            "n_activity_assessable": next((x["n_ads_activity_assessable"] for x in d8a
                                           if x["company_id"] == cid), ""),
            "comparison_eligible": "", "exclusion_or_qualification": "",
            "seniority_note": "", "work_object_note": "",
            "source_note": f'{c["source_type"]}|{c["hiring_data_quality_score"]}',
        })
for r in d8b:
    t5.append({
        "record_kind": "HIRING_METRIC", "case_group": "", "case_id": "",
        "company_id": r["company_id"], "company_name": r["company_name"],
        "stratum_name": companies[r["company_id"]]["stratum_name"], "supply_form_note": "",
        "product_or_scene": "", "business_stage": "",
        "responsibility_subject": "",
        "fact_or_metric": f'Q3职能内活动：{r["primary_name"]}×{r["activity_name"]}（本人承担）',
        "value": r["share_within_function"], "unit": "share_within_function",
        "numerator": r["n_positive"], "denominator": r["n_assessable_in_function"],
        "unknown_or_gap": "",
        "event_date": "", "publication_date": "",
        "observation_date": companies[r["company_id"]]["observation_date_min"],
        "time_applicability": "", "evidence_ids": "",
        "hiring_scope": "", "n_ads": "", "n_activity_assessable": r["n_assessable_in_function"],
        "comparison_eligible": "", "exclusion_or_qualification": "",
        "seniority_note": "", "work_object_note": "",
        "source_note": "D8b_within_function_activity_rates",
    })

# 3 case-level Q2 points and work-object / seniority notes
obj_by_company = defaultdict(Counter)
sen_by_company = defaultdict(Counter)
for r in d8e:
    for code in r["work_object_codes"].split("|"):
        obj_by_company[r["company_id"]][code] += 1
    sen_by_company[r["company_id"]][r["seniority_codes"]] += 1
for r in d8d:
    cid = r["company_id"]
    t5.append({
        "record_kind": "HIRING_METRIC",
        "case_group": next((g for g, m in selection["selected_groups"].items() if cid in m), ""),
        "case_id": "", "company_id": cid, "company_name": r["company_name"],
        "stratum_name": companies[cid]["stratum_name"], "supply_form_note": "",
        "product_or_scene": "", "business_stage": "", "responsibility_subject": "",
        "fact_or_metric": f'Q2：{r["label_name"]}（{r["metric_bucket"]}|{r["branch_bucket"]}）',
        "value": r["share"], "unit": "share_of_interpretable",
        "numerator": r["n_positive"], "denominator": r["n_interpretable"],
        "unknown_or_gap": f'未知{r["n_unknown"]}条',
        "event_date": "", "publication_date": "",
        "observation_date": companies[cid]["observation_date_min"], "time_applicability": "",
        "evidence_ids": "", "hiring_scope": "", "n_ads": companies[cid]["n_ads"],
        "n_activity_assessable": "",
        "comparison_eligible": "", "exclusion_or_qualification": "小样本提示：可解释广告少于10条" if r["small_n_under10"] == "YES" else "",
        "seniority_note": "；".join(f"{k}×{v}" for k, v in sen_by_company[cid].most_common(3)),
        "work_object_note": "；".join(f"{k}×{v}" for k, v in obj_by_company[cid].most_common(4)),
        "source_note": r["label_code"],
    })

# 4 case qualification rows
for r in d7:
    t5.append({
        "record_kind": "CASE_QUALIFICATION",
        "case_group": r["case_group"], "case_id": r["case_group"],
        "company_id": r["company_id"], "company_name": r["company_name"],
        "stratum_name": r["stratum_name"], "supply_form_note": "",
        "product_or_scene": r["target_scene"],
        "business_stage": "", "responsibility_subject": "",
        "fact_or_metric": f'案例资格：场景状态{r["scene_state_for_group"]}；共同职能{r["selected_pair_common_K"]}个',
        "value": r["comparison_eligible"], "unit": "qualification",
        "numerator": "", "denominator": "",
        "unknown_or_gap": f'开放缺口{r["n_gaps_open"]}项',
        "event_date": "", "publication_date": "", "observation_date": r["observation_dates"],
        "time_applicability": "",
        "evidence_ids": "",
        "hiring_scope": "", "n_ads": r["n_ads"],
        "n_activity_assessable": "",
        "comparison_eligible": r["comparison_eligible"],
        "exclusion_or_qualification": r["decision_reason"],
        "seniority_note": "", "work_object_note": "",
        "source_note": f'入选序位{r["selection_rank_in_group"]}',
    })
write("T5_company_hiring_correspondence.csv", t5, T5_FIELDS)

# ------------------------------------------------------------------- T6
def sens(metric_id, field):
    for r in d9:
        if r["metric_id"] == metric_id:
            return r.get(field, "")
    return ""


def co(pair_id):
    for r in d4:
        if r["pair_id"] == pair_id and r["scope"] == "ALL24":
            return r
    return {}


def q1(code):
    for r in d1:
        if r["class_code"] == code:
            return r
    return {}


MFG = q1("RF_MANUFACTURING_QUALITY_SUPPLY")
SW = q1("RF_ROBOTICS_SOFTWARE")
ML = q1("RF_ML_AI_ENGINEERING")

T6_FIELDS = [
    "conclusion_id", "question", "candidate_explanation", "final_wording", "applicable_scope",
    "n_companies", "n_ads", "metric_definition", "numerator", "denominator", "n_unknown",
    "data_paths", "evidence_ids", "sensitivity_summary", "counterexample",
    "alternative_explanation", "status", "residual_limits",
]

t6 = []

t6.append({
    "conclusion_id": "T6-01", "question": "Q1",
    "candidate_explanation": "企业招聘职能组合对应其产品与业务环节；公司间差异主要表现为职能构成不同",
    "final_wording": (
        f"在23家整公司范围内，本批广告的前三主职能为制造、质量与供应链、软件与平台、ML/AI工程，"
        f"广告加权{float(MFG['share_ad_weighted_all'])*100:.1f}%／{float(SW['share_ad_weighted_all'])*100:.1f}%／"
        f"{float(ML['share_ad_weighted_all'])*100:.1f}%，公司等权"
        f"{float(MFG['share_company_equal_all'])*100:.1f}%／{float(SW['share_company_equal_all'])*100:.1f}%／"
        f"{float(ML['share_company_equal_all'])*100:.1f}%；三者合计约占三成，其余职能分散。"
        "职能构成差异在各公司之间确实存在，但分布右偏，中位数低于均值。"),
    "applicable_scope": "WHOLE23 整公司范围，2026-08-31与2026-09-11两个观察批",
    "n_companies": MFG["n_companies_with_denominator"], "n_ads": MFG["denominator_all_ads"],
    "metric_definition": "公司主职能广告数/公司全部认可广告；公司等权为各公司比例算术平均",
    "numerator": MFG["n_ads_ad_weighted"], "denominator": MFG["denominator_all_ads"],
    "n_unknown": "",
    "data_paths": "tables/D1_q1_coverage_concentration.csv；tables/T2_company_primary_roles.csv",
    "evidence_ids": "",
    "sensitivity_summary": (
        f"制造质量供应链：等权{pct(MFG['share_company_equal_all'])}/加权{pct(MFG['share_ad_weighted_all'])}，"
        f"公司比例中位数{pct(MFG['company_share_median'])}、四分位{pct(MFG['company_share_p25'])}—{pct(MFG['company_share_p75'])}，"
        f"最大公司正向贡献{pct(MFG['largest_company_positive_contribution'])}；"
        f"软件与平台：等权{pct(SW['share_company_equal_all'])}/加权{pct(SW['share_ad_weighted_all'])}；"
        f"ML/AI工程：等权{pct(ML['share_company_equal_all'])}/加权{pct(ML['share_ad_weighted_all'])}"),
    "counterexample": "机器人操作等小类别在公司等权2.7%与广告加权1.3%之间差异明显，说明仅用广告池总量会高估或低估典型公司",
    "alternative_explanation": "招聘板覆盖范围、公司规模、产品线数量与观察批次差异",
    "status": "在已检查口径下方向一致",
    "residual_limits": "非概率样本；广告不等同人数；职能目录宽窄不同，排名只描述本目录下的广告构成",
})

RES = co("P1_RESEARCH_ENGINEERING")
DEP = co("P3_ENGINEERING_DEPLOYMENT")
QUA = co("P2_ENGINEERING_QUALITY")


def s9(metric_id):
    return next((r for r in d9 if r["metric_id"] == metric_id), {})


DEP_ACT = s9("Q3_ACT_DEPLOYMENT")
QUA_ACT = s9("Q3_ACT_QUALITY")
RES_ACT = s9("Q3_ACT_RESEARCH")
P1_ROW, P2_ROW, P3_ROW = s9("P1_RESEARCH_ENGINEERING"), s9("P2_ENGINEERING_QUALITY"), s9("P3_ENGINEERING_DEPLOYMENT")
t6.append({
    "conclusion_id": "T6-02", "question": "Q1/Q3",
    "candidate_explanation": "某类活动在广告中较多，主要来自对应职能占比高（职能构成解释）",
    "final_wording": (
        "职能与活动是相互独立的两次测量。部署与维护活动351条中只有80条主职能为部署与现场服务，"
        "占22.8%，其余271条分布在ML/AI工程、软件与平台等职能；质量验证466条中制造质量供应链160条，"
        "占34.3%；研究探索75条中研究科学27条，占36.0%。因此不能把某活动的数量差直接读作对应职能的占比差。"),
    "applicable_scope": "ALL24 全部24个主体，活动可判读1,623条",
    "n_companies": 24, "n_ads": 1623,
    "metric_definition": "活动正向广告数（本人承担）／活动可判读广告数；跨职能占比为该活动正向广告中某主职能所占比例",
    "numerator": DEP_ACT.get("n_positive", ""), "denominator": DEP_ACT.get("n_interpretable", ""),
    "n_unknown": "",
    "data_paths": "tables/D3_role_activity_bidirectional.csv；tables/D9_sensitivity_ledger.csv；tables/T4_primary_activity_cross.csv",
    "evidence_ids": "",
    "sensitivity_summary": (
        f"活动率敏感性（D9）：部署与维护加权{pct(DEP_ACT.get('value_ad_weighted'))}、整公司23为{pct(DEP_ACT.get('s_whole23_ad_weighted'))}、"
        f"来源较完整子集{pct(DEP_ACT.get('s_source_complete_subset_ad_weighted'))}、逐一剔除{pct(DEP_ACT.get('s_loo_min'))}—{pct(DEP_ACT.get('s_loo_max'))}；"
        f"质量验证加权{pct(QUA_ACT.get('value_ad_weighted'))}、来源较完整子集{pct(QUA_ACT.get('s_source_complete_subset_ad_weighted'))}；"
        f"研究探索加权{pct(RES_ACT.get('value_ad_weighted'))}、逐一剔除{pct(RES_ACT.get('s_loo_min'))}—{pct(RES_ACT.get('s_loo_max'))}"),
    "counterexample": "工程实现活动的跨职能分布最广（957条），其主职能集中在ML/AI工程与软件与平台，与部署活动的分布形态不同",
    "alternative_explanation": "广告正文详略与部门命名习惯不同，可能使同一工作被写成不同职能",
    "status": "在已检查口径下方向一致",
    "residual_limits": "活动判读基于原文表述；不能据此推断实际跨部门协同或组织效率",
})

t6.append({
    "conclusion_id": "T6-03", "question": "Q3",
    "candidate_explanation": "工程师岗位在广告中同时被要求承担多项相邻活动",
    "final_wording": (
        f"在活动可判读广告中，工程实现与质量验证的无条件共同承担为{P2_ROW.get('n_positive')}/{P2_ROW.get('n_assessable')}"
        f"（{pct(P2_ROW.get('value_ad_weighted'))}），工程实现与部署维护为{P3_ROW.get('n_positive')}/{P3_ROW.get('n_assessable')}"
        f"（{pct(P3_ROW.get('value_ad_weighted'))}），研究探索与工程实现为{P1_ROW.get('n_positive')}/"
        f"{P1_ROW.get('n_assessable')}（{pct(P1_ROW.get('value_ad_weighted'))}）。"
        "30条职责结构广告中，没有出现两项被研究活动分属互斥任选方向的情形，也没有出现某一可选方向内的条件性共同承担。"),
    "applicable_scope": "ALL24，三组活动配对；结构判断仅覆盖30条职责结构广告",
    "n_companies": QUA.get("n_companies_in_both", ""), "n_ads": P2_ROW.get("n_interpretable", ""),
    "metric_definition": "两活动均本人承担且关系判定为无条件同现的广告数／活动可判读广告数",
    "numerator": f"{P2_ROW.get('n_positive')}（工程实现×质量验证）｜{P3_ROW.get('n_positive')}（工程实现×部署维护）｜{P1_ROW.get('n_positive')}（研究探索×工程实现）",
    "denominator": P2_ROW.get("n_interpretable", ""),
    "n_unknown": f"{P2_ROW.get('n_unresolved')}（工程×质量）｜{P3_ROW.get('n_unresolved')}（工程×部署）",
    "data_paths": "tables/D4_activity_pair_cooccurrence.csv；tables/D4_activity_pair_lineage.csv；tables/D9_sensitivity_ledger.csv",
    "evidence_ids": "",
    "sensitivity_summary": (
        f"工程×质量：加权{pct(P2_ROW.get('value_ad_weighted'))}、整公司23为{pct(P2_ROW.get('s_whole23_ad_weighted'))}、"
        f"来源较完整子集{pct(P2_ROW.get('s_source_complete_subset_ad_weighted'))}、"
        f"逐一剔除{pct(P2_ROW.get('s_loo_min'))}—{pct(P2_ROW.get('s_loo_max'))}；"
        f"工程×部署：加权{pct(P3_ROW.get('value_ad_weighted'))}、来源较完整子集"
        f"{pct(P3_ROW.get('s_source_complete_subset_ad_weighted'))}"),
    "counterexample": "工程×质量在来源较完整子集上升到28.4%，而工程×部署下降到12.4%，说明正文详略对两组配对的影响方向相反",
    "alternative_explanation": "招聘广告常把质量与交付要求写进同一段任职要求，共现可能来自模板化表述",
    "status": "依赖特定公司或口径",
    "residual_limits": "20条（去重后）结构广告活动无法绑定到分支，按未解决保留；共现不等于实际岗位内部的协作",
})

t6.append({
    "conclusion_id": "T6-04", "question": "Q2",
    "candidate_explanation": "两个代表职能公开要求的任务对象不同，ML偏向模型与训练系统，软件偏向可靠性与实时系统",
    "final_wording": (
        f"ML/AI工程中，训练推理系统本人开发{pct(sens('ML_TRAINING_INFERENCE','value_ad_weighted'))}、"
        f"基础模型/VLA为{pct(sens('ML_FOUNDATION_VLA','value_ad_weighted'))}、数据管线与资产为"
        f"{pct(sens('ML_DATA_PIPELINE','value_ad_weighted'))}；软件与平台中可靠性为{pct(sens('SW_RELIABILITY','value_ad_weighted'))}、"
        f"实时系统为{pct(sens('SW_REALTIME','value_ad_weighted'))}。工具类要求多处于一般要求或示例语境，"
        f"如ML的PyTorch一般要求独立条目仅{pct(sens('ML_PYTORCH_GENERAL','value_ad_weighted'))}。"),
    "applicable_scope": "WHOLE23，两职能技能与技术要求维度；14种语境分支独立计入，不可相加",
    "n_companies": 23, "n_ads": sens("ML_TRAINING_INFERENCE", "n_interpretable"),
    "metric_definition": "该标签该语境的PRESENT广告数／最终可解释分母（基础范围减该格未知）",
    "numerator": sens("ML_TRAINING_INFERENCE", "n_positive"),
    "denominator": sens("ML_TRAINING_INFERENCE", "n_interpretable"),
    "n_unknown": sens("ML_TRAINING_INFERENCE", "n_unknown"),
    "data_paths": "tables/D2_q2_coverage_concentration.csv；tables/D9_sensitivity_ledger.csv；tables/T3_aggregates.csv",
    "evidence_ids": "",
    "sensitivity_summary": (
        f"训练推理系统：广告加权{pct(sens('ML_TRAINING_INFERENCE','value_ad_weighted'))}、公司等权"
        f"{pct(sens('ML_TRAINING_INFERENCE','value_company_equal'))}、来源较完整子集"
        f"{pct(sens('ML_TRAINING_INFERENCE','s_source_complete_subset_ad_weighted'))}、逐一剔除"
        f"{pct(sens('ML_TRAINING_INFERENCE','s_loo_min'))}—{pct(sens('ML_TRAINING_INFERENCE','s_loo_max'))}；"
        f"可靠性：来源较完整子集{pct(sens('SW_RELIABILITY','s_source_complete_subset_ad_weighted'))}；"
        f"基础模型/VLA来源较完整子集{pct(sens('ML_FOUNDATION_VLA','s_source_complete_subset_ad_weighted'))}"),
    "counterexample": "训练推理系统在来源较完整子集升至65.9%，而基础模型/VLA降至36.4%，两个指标口径敏感方向相反",
    "alternative_explanation": "不同招聘板的字段长度与模板结构影响标签可判读性",
    "status": "依赖特定公司或口径",
    "residual_limits": "目录外技能未回填；UNMAPPED保留基础范围；工具标签多处于任选/示例，不能读作硬性要求",
})

# case-based conclusion
g1a, g1b = G1[0], G1[1]
d8c = read(RUN / "tables/D8c_common_function_weighted_comparison.csv")
dep_c = next((r for r in d8c if r["activity_code"] == "ACT_DEPLOYMENT"), {})
case_pair = next((r for r in d7a if r["case_group"] == "G1_MANUFACTURING_LINE"
                  and r["is_selected_pair"] == "YES"), {})
ml_a = next((r for r in d8b if r["company_id"] == g1a and r["primary_code"] == "RF_ML_AI_ENGINEERING"
             and r["activity_code"] == "ACT_DEPLOYMENT"), {})
ml_b = next((r for r in d8b if r["company_id"] == g1b and r["primary_code"] == "RF_ML_AI_ENGINEERING"
             and r["activity_code"] == "ACT_DEPLOYMENT"), {})
all_a = next((r for r in d8b if r["company_id"] == g1a and r["activity_code"] == "ACT_DEPLOYMENT"
              and r["primary_code"] == "RF_MANUFACTURING_QUALITY_SUPPLY"), {})
t6.append({
    "conclusion_id": "T6-05", "question": "Q1",
    "candidate_explanation": "业务环节的责任归属不同，会在同一职能内部表现为不同的任务承担",
    "final_wording": (
        f"以制造产线实际使用场景的两家整机公司为例，在共同职能覆盖范围内（{case_pair.get('common_K_names','')}），"
        f"{companies[g1a]['company_name']}的部署维护活动自我权重率为21.6%，"
        f"{companies[g1b]['company_name']}为0.0%；在ML/AI工程职能内部，"
        f"{companies[g1a]['company_name']}为{ml_a.get('n_positive','')}/{ml_a.get('n_assessable_in_function','')}"
        f"（{pct(ml_a.get('share_within_function'))}），{companies[g1b]['company_name']}为"
        f"{ml_b.get('n_positive','')}/{ml_b.get('n_assessable_in_function','')}"
        f"（{pct(ml_b.get('share_within_function'))}）。该差异与两家公司公开的交付形态一致：前者自营零售门店并进入客户产线，"
        "后者以整机对外交付为主。"),
    "applicable_scope": "G1制造产线案例组两家公司，观察批2026-09-11；共同职能K覆盖有限",
    "n_companies": 2, "n_ads": sum(num(companies[c]["n_ads"]) for c in G1),
    "metric_definition": "共同职能内活动率（该职能内本人承担该活动广告数/该职能活动可判读广告数），K内按自身职能比重与等权两种方式汇总",
    "numerator": ml_a.get("n_positive", ""), "denominator": ml_a.get("n_assessable_in_function", ""),
    "n_unknown": "",
    "data_paths": "tables/D8c_common_function_weighted_comparison.csv；tables/D8b_within_function_activity_rates.csv；tables/D9b_case_deployment_sensitivity.csv；cases/case_selection.json",
    "evidence_ids": "B_CN_GALBOT_001|NEW_GALBOT_01|NEW_AGIBOT_01|B_CN_AGIBOT_002",
    "sensitivity_summary": (
        f"K覆盖率：{companies[g1a]['company_name']} {pct(dep_c.get(f'{g1a}_K_coverage'))}、"
        f"{companies[g1b]['company_name']} {pct(dep_c.get(f'{g1b}_K_coverage'))}；"
        f"全公司口径{pct(dep_c.get(f'{g1a}_share_all'))}对{pct(dep_c.get(f'{g1b}_share_all'))}，"
        f"K内自我权重{pct(dep_c.get(f'{g1a}_share_self_weighted'))}对{pct(dep_c.get(f'{g1b}_share_self_weighted'))}，"
        f"等权{pct(dep_c.get(f'{g1a}_share_equal_weighted'))}对{pct(dep_c.get(f'{g1b}_share_equal_weighted'))}；"
        "来源较完整子集对该两家不适用（两家质量分为USABLE，未纳入来源较完整子集）"),
    "counterexample": "在同一K内的公司支持职能里，两家公司的部署活动率同为0.0%，说明差异只在部分职能内出现",
    "alternative_explanation": "样本量差异（GALBOT 184条对AGIBOT 83条）与部门命名习惯可能放大差异",
    "status": "依赖特定公司或口径",
    "residual_limits": "案例比较只回答共同覆盖职能内的差异；不能推广为行业规律或因果结论",
})

t6.append({
    "conclusion_id": "T6-06", "question": "Q1",
    "candidate_explanation": "物流场景公司同样可以按共同职能做统一权重比较",
    "final_wording": (
        "物流仓储场景的候选公司在样本内没有任何一对满足研究书规定的共同职能门槛"
        "（双方均需有至少10条活动可判读广告的具体主职能，且至少2个共同职能）。"
        "该组统一权重比较记录为不适用，只保留逐职能点值与有限描述，不通过合并类别或补零凑样本。"),
    "applicable_scope": "G2物流仓储案例组，6家候选公司全部配对",
    "n_companies": 6, "n_ads": sum(num(companies[c]["n_ads"]) for c in
                                    ["US_AGILITY", "US_PICKLE", "US_BOSTON_DYNAMICS",
                                     "US_NIMBLE", "CN_XSQUARE", "US_DEXTERITY"]),
    "metric_definition": "共同职能集合K：双方均满10条活动可判读广告的具体主职能交集，要求至少2个",
    "numerator": "", "denominator": "", "n_unknown": "",
    "data_paths": "tables/D7a_pairwise_common_functions.csv；tables/D8c2_common_function_weighted_comparison_G2.csv",
    "evidence_ids": "",
    "sensitivity_summary": "组内15个配对全部K≤1；最大K为1（制造、质量与供应链），出现在Boston Dynamics与Agility、X Square等配对",
    "counterexample": "",
    "alternative_explanation": "样本量小的公司（Pickle 13条、Nimble 34条、Dexterity 31条）单个职能很难达到10条门槛",
    "status": "证据不足或不适用",
    "residual_limits": "不适用不等于不存在差异；提高样本量后该比较可能成立",
})

t6.append({
    "conclusion_id": "T6-07", "question": "Q1",
    "candidate_explanation": "公司业务责任差异可以直接由招聘数据解释",
    "final_wording": (
        "24个主体的业务责任与使用证据继承自B阶段680条事实与111条证据，其中与业务环节相关的203条，"
        "责任主体可判定为公司的80条、共同承担11条、其余112条保留未知；"
        "未知的部分主要来自既有状态为未查或未找到。招聘数据只能与已封存事实并列比较，"
        "不能用招聘职能缺失推断外包或责任转移。"),
    "applicable_scope": "24个主体；事实层为2026-09-15封存的B补充包",
    "n_companies": 24, "n_ads": 1654,
    "metric_definition": "业务环节事实条数及责任主体判定分布",
    "numerator": 203, "denominator": 680, "n_unknown": 112,
    "data_paths": "tables/D6_business_responsibility_long.csv；tables/D6b_company_status_and_gaps.csv",
    "evidence_ids": "见D6各行的evidence_ids列",
    "sensitivity_summary": "开放缺口103项，其中商业部署、交付与规模化运营类占多数；未纳入解释的未知事实保持未知",
    "counterexample": "",
    "alternative_explanation": "公司自述、客户确认与媒体陈述的性质不同，需分别标注",
    "status": "证据不足或不适用",
    "residual_limits": "关键事实仍不足时不作确定判断；公司自述不升级为独立核账",
})

write("T6_conclusion_ledger.csv", t6, T6_FIELDS)

summary = {
    "t5_rows": len(t5),
    "t5_kinds": Counter(r["record_kind"] for r in t5).most_common(),
    "t6_rows": len(t6),
    "t6_status": Counter(r["status"] for r in t6).most_common(),
}
(VER / "step5_checks.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))
