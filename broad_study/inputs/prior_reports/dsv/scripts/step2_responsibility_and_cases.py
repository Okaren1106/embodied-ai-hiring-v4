#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Stage D step 2.

Inherit the Stage B company fact layer, derive the business-stage /
responsibility-subject long table, list inherited status plus key gaps for all
24 subjects, and build the case candidate table with the Stage D selection.

Derivation only: every row keeps its Stage B fact_id and evidence_ids; no new
company facts are invented here. Case selection follows the research book
order: entity scope, product scene, observation vintage, evidence
completeness, then common-function coverage. Statistical gaps are never used.
"""
from __future__ import annotations

import csv
import itertools
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
B = BASE / "stage_b_supplemented/run_20260915T073556Z"
R = BASE / "analysis_rules_v1/run_20260915T085828Z"

TAB = RUN / "tables"
CASES = RUN / "cases"
VER = RUN / "verification"
for p in (TAB, CASES, VER):
    p.mkdir(parents=True, exist_ok=True)


def read(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def write(name, rows, fields):
    path = TAB / name
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        wr = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        wr.writeheader()
        for row in rows:
            wr.writerow(row)
    return path


def num(v, default=0):
    return int(v) if v not in (None, "", "NA") else default


def ratio(a, b):
    return None if not b else round(a / b, 10)


# ------------------------------------------------------------------ inputs
facts = read(B / "company_facts.csv")
gaps = read(B / "company_gaps.csv")
profile = {r["company_id"]: r for r in read(B / "company_profile.csv")}
t1 = read(C / "tables/T1_company_sample.csv")
t2 = read(C / "tables/T2_company_primary_roles.csv")
t4adm = read(C / "tables/T4_activity_admission.csv")
scene_rows = read(R / "company_scene_assertions.csv")
companies = {r["company_id"]: r for r in t1}
jobs = read(C / "inputs/rules_v1/inputs/stage_a/jobs.csv")

# ------------------------------------------- business stage / subject rules
FIELD_TO_STAGE = {
    "product_lines": ("PRODUCT_MODEL_DEV", "产品与模型范围"),
    "product_lines_humanoid": ("PRODUCT_MODEL_DEV", "产品与模型范围"),
    "product_lines_rehab": ("PRODUCT_MODEL_DEV", "产品与模型范围"),
    "product_lines_companion": ("PRODUCT_MODEL_DEV", "产品与模型范围"),
    "delivery_form": ("PRODUCT_DELIVERY", "产品交付形态"),
    "target_markets": ("TARGET_MARKET_ONLY", "仅公开目标场景"),
    "target_markets_domestic_rehab": ("TARGET_MARKET_ONLY", "仅公开目标场景"),
    "target_markets_malaysia": ("TARGET_MARKET_ONLY", "仅公开目标场景"),
    "target_markets_singapore": ("TARGET_MARKET_ONLY", "仅公开目标场景"),
    "named_customers_or_partners": ("PARTNER_OR_CUSTOMER", "客户与合作方"),
    "evidence_demo": ("DEMONSTRATION", "演示"),
    "evidence_internal_test": ("INTERNAL_TEST", "内部测试"),
    "evidence_loi_intent": ("LOI_INTENT", "意向或备忘录"),
    "evidence_external_pilot": ("PILOT", "外部试点"),
    "evidence_customer_delivery": ("CUSTOMER_SITE_DEPLOYMENT", "客户现场部署"),
    "evidence_production_shipment": ("PRODUCT_DELIVERY", "量产出货"),
    "evidence_paid": ("PAYMENT_OR_REVENUE_CLAIM", "付款或收入断言"),
    "evidence_repeat_order": ("REPEAT_ORDER", "重复订单"),
    "evidence_sustained_use": ("SUSTAINED_OPERATION", "持续运行"),
    "deployment_status_actual": ("FIELD_VERIFIED_DEPLOYMENT", "实际部署状态"),
    "hiring_board_channel": ("HIRING_SCOPE", "招聘渠道范围"),
    "hiring_source_history": ("HIRING_SCOPE", "招聘渠道范围"),
    "hiring_role_scope": ("HIRING_SCOPE", "招聘范围"),
    "observation_coverage": ("HIRING_SCOPE", "观察覆盖"),
}
BACKGROUND_FIELDS = {
    "own_listing_status", "parent_listing_status", "latest_financing_disclosed",
    "latest_financing_at_observation", "ma_events", "founded_or_team_start_date",
    "parent_relationship", "legal_entity_name", "research_subject",
    "hq_or_team_location", "boundary_far_vs_ftr", "parent_robotics_scale_context",
}

OPERATION_KEYWORDS = ("RaaS", "机器人即服务", "自营", "自有", "robots-as-a-service", "3PL", "履单中心")
SUSTAINED_KEYWORDS = ("持续", "运行", "日常", "全轮班", "已投用", "投产", "并线")
UNKNOWN_VALUES = ("NOT_YET_SEARCHED", "SEARCHED_NOT_FOUND", "NOT_APPLICABLE")
VALUE_STATUS_TO_CLASS = {
    "COMPANY_SELF_REPORT": "COMPANY_SELF_REPORT",
    "MEDIA_STATEMENT": "MEDIA_STATEMENT",
    "SUPPORTED_EXTERNAL": "SUPPORTED_EXTERNAL",
    "COUNTERPARTY_CONFIRMATION": "COUNTERPARTY_CONFIRMATION",
    "INHERITED_UNVERIFIED": "INHERITED_UNVERIFIED",
    "NOT_YET_SEARCHED": "UNKNOWN_NOT_SEARCHED",
    "SEARCHED_NOT_FOUND": "UNKNOWN_NOT_FOUND",
    "NOT_APPLICABLE": "NOT_APPLICABLE",
}
BUSINESS_STAGES = ("PRODUCT_MODEL_DEV", "SYSTEM_INTEGRATION", "CUSTOMER_SITE_DEPLOYMENT",
                   "CONTINUOUS_OPERATION", "PRODUCT_DELIVERY")


def derive_stage(fact):
    field = fact["field"]
    if field in BACKGROUND_FIELDS or field.startswith("capital_event") or field == "DATE_CONFLICT":
        return "COMPANY_BACKGROUND", "公司背景"
    if field in FIELD_TO_STAGE:
        return FIELD_TO_STAGE[field]
    return "OTHER", "其他"


def derive_subject(fact):
    val = (fact["value"] or "") + " " + (fact["note"] or "")
    status = fact["value_status"]
    if status in UNKNOWN_VALUES:
        return "UNKNOWN", "R-UNKNOWN-STATUS", "既有状态为未查或未找到，保留未知"
    if any(k in val for k in OPERATION_KEYWORDS):
        return "COMPANY", "R-SUBJ-OPERATE", "交付形态显示由供应方自营或提供持续服务"
    if fact["field"] in ("evidence_customer_delivery", "evidence_external_pilot",
                         "evidence_production_shipment", "delivery_form"):
        if "客户" in val or "交付" in val or "销售" in val or "订单" in val:
            return "COMPANY", "R-SUBJ-DELIVER", "公司将产品或方案交付至客户侧"
        return "COMPANY", "R-SUBJ-DELIVER-GEN", "交付类事实默认由供应方承担交付责任"
    if fact["field"] == "evidence_sustained_use":
        return "SHARED", "R-SUBJ-SHARED", "持续使用发生在客户侧且由供应方支持，不单方归因"
    if status == "COUNTERPARTY_CONFIRMATION":
        return "COMPANY", "R-SUBJ-COUNTERPARTY", "对方确认公司侧交付或部署行为"
    if fact["field"] in ("target_markets", "evidence_demo"):
        return "UNKNOWN", "R-SUBJ-TARGET", "公开目标或演示不等于已确定的责任承担"
    return "UNKNOWN", "R-SUBJ-DEFAULT", "未记录明确责任承担方"


def derive_stage_detail(fact):
    field = fact["field"]
    val = fact["value"] or ""
    stage, label = derive_stage(fact)
    if field == "deployment_status_actual":
        if fact["value_status"] in UNKNOWN_VALUES or not val.strip():
            return "UNKNOWN_STAGE", "未知：既有检索未取得部署状态"
        if "试点" in val or "试用" in val or "评估" in val:
            return "CUSTOMER_SITE_DEPLOYMENT", "客户现场部署（试点）"
        if any(k in val for k in SUSTAINED_KEYWORDS):
            return "CONTINUOUS_OPERATION", "持续运行"
        return "CUSTOMER_SITE_DEPLOYMENT", "客户现场部署"
    if field == "evidence_external_pilot":
        return "CUSTOMER_SITE_DEPLOYMENT", "客户现场部署（试点）"
    if field == "evidence_customer_delivery":
        return "CUSTOMER_SITE_DEPLOYMENT", "客户现场部署"
    if field in ("evidence_sustained_use", "evidence_repeat_order"):
        return "CONTINUOUS_OPERATION", "持续运行"
    if field == "delivery_form":
        if "系统集成" in val:
            return "SYSTEM_INTEGRATION", "系统集成"
        return "PRODUCT_MODEL_DEV", "产品或模型开发与交付"
    if field.startswith("product_lines"):
        return "PRODUCT_MODEL_DEV", "产品或模型开发"
    return stage, label


long_rows = []
for f in facts:
    stage, stage_label = derive_stage_detail(f)
    subject, rule_id, rule_reason = derive_subject(f)
    cls = VALUE_STATUS_TO_CLASS.get(f["value_status"], f["value_status"])
    long_rows.append({
        "company_id": f["company_id"],
        "company_name": companies.get(f["company_id"], {}).get("company_name", ""),
        "stratum": companies.get(f["company_id"], {}).get("stratum", ""),
        "stratum_name": companies.get(f["company_id"], {}).get("stratum_name", ""),
        "scope_main_company": companies.get(f["company_id"], {}).get("scope_main_company", ""),
        "fact_id": f["fact_id"],
        "field": f["field"],
        "fact_seq": f["fact_seq"],
        "assertion_kind": f["assertion_kind"],
        "subject_scope": f["subject_scope"],
        "product_or_business_scope": f["product_or_business_scope"],
        "business_stage": stage,
        "business_stage_label": stage_label,
        "responsibility_subject": subject,
        "evidence_class": cls,
        "fact_value": f["value"],
        "unit": f["unit"],
        "value_status": f["value_status"],
        "research_status": f["research_status"],
        "event_date": f["event_date"],
        "publication_date": f["publication_date"],
        "date_precision": f["date_precision"],
        "time_applicability": f["time_applicability"],
        "time_reason": f["time_reason"],
        "observation_date": f["observation_date"],
        "evidence_ids": f["evidence_ids"],
        "rule_id": rule_id,
        "rule_reason": rule_reason,
        "judgment_status": ("UNKNOWN_NOT_SEARCHED" if f["value_status"] == "NOT_YET_SEARCHED"
                            else "UNKNOWN_NOT_FOUND" if f["value_status"] == "SEARCHED_NOT_FOUND"
                            else "NOT_APPLICABLE" if f["value_status"] == "NOT_APPLICABLE"
                            else "RECORDED"),
    })
write("D6_business_responsibility_long.csv", long_rows, list(long_rows[0].keys()))

# ------------------------------------------------ company status and gaps
gap_by_company = defaultdict(list)
for g in gaps:
    gap_by_company[g["company_id"]].append(g)

status_rows = []
for cid, c in companies.items():
    st = profile.get(cid, {})
    gr = gap_by_company.get(cid, [])
    og = [g for g in gr if g["open_at_stage_b_end"] == "YES"]
    facts_c = [f for f in long_rows if f["company_id"] == cid]
    observed = [r for r in scene_rows if r["company_id"] == cid and r["state"].startswith("OBSERVED")]
    status_rows.append({
        "company_id": cid,
        "company_name": c["company_name"],
        "country": c["country"],
        "stratum": c["stratum"],
        "stratum_name": c["stratum_name"],
        "n_ads": c["n_ads"],
        "observation_dates": c["observation_dates"],
        "entity_scope_inherited": c["entity_scope_inherited"],
        "hiring_scope_inherited": c["hiring_scope_inherited"],
        "source_type": c["source_type"],
        "hiring_data_quality_score": c["hiring_data_quality_score"],
        "inheritance_status": c["inheritance_status"],
        "scope_time_applicability": c["scope_time_applicability"],
        "n_facts_inherited": len(facts_c),
        "n_facts_recorded": sum(1 for f in facts_c if f["judgment_status"] == "RECORDED"),
        "n_facts_unknown_not_searched": sum(1 for f in facts_c if f["judgment_status"] == "UNKNOWN_NOT_SEARCHED"),
        "n_gap_rows": len(gr),
        "n_gaps_open": len(og),
        "n_gaps_resolved_found": sum(1 for g in gr if g["stage_b_status"] == "RESOLVED_FOUND"),
        "n_gaps_not_searched": sum(1 for g in gr if g["stage_b_status"] == "NOT_YET_SEARCHED"),
        "key_open_gap_fields": "|".join(sorted({g["fact_field"] for g in og})),
        "n_scene_assertions": len([r for r in scene_rows if r["company_id"] == cid]),
        "n_scenes_observed": len(observed),
        "observed_scenes": "|".join(sorted({f"{r['scene']}:{r['state']}" for r in observed})),
        "n_responsibility_rows": len([f for f in facts_c if f["business_stage"] in BUSINESS_STAGES]),
        "n_business_rows_known_subject": len([f for f in facts_c if f["business_stage"] in BUSINESS_STAGES
                                              and f["responsibility_subject"] != "UNKNOWN"]),
        "n_delivery_rows": len([f for f in facts_c if f["business_stage"] in
                                ("PRODUCT_DELIVERY", "CUSTOMER_SITE_DEPLOYMENT",
                                 "CONTINUOUS_OPERATION", "SYSTEM_INTEGRATION")]),
        "n_unknown_stage_rows": len([f for f in facts_c if f["business_stage"] == "UNKNOWN_STAGE"]),
    })
write("D6b_company_status_and_gaps.csv", status_rows, list(status_rows[0].keys()))

# --------------------------------------------------- common-function sets
eligible = {r["identity_key"] for r in t4adm if r["base_eligible"] == "YES"}
primary_of = {j["identity_key"]: (j["primary_code"] if j["primary_status"] == "CODED" else j["primary_status"])
              for j in jobs}
jobs_by_id = {j["identity_key"]: j for j in jobs}
concrete = {r["class_code"] for r in t2 if r["class_kind"] == "concrete"}
fname = {r["class_code"]: r["class_name"] for r in t2}
asg = defaultdict(lambda: defaultdict(int))
for ik in sorted(eligible):
    code = primary_of[ik]
    if code in concrete:
        asg[jobs_by_id[ik]["company_id"]][code] += 1
ge10 = {c: {k: n for k, n in d.items() if n >= 10} for c, d in asg.items()}
OBSERVED = defaultdict(set)
for r in scene_rows:
    if r["state"].startswith("OBSERVED"):
        OBSERVED[r["company_id"]].add(r["scene"])

SCENE_GROUPS = {
    "G1_MANUFACTURING_LINE": ("MANUFACTURING",
                              ["CN_AGIBOT", "CN_GALBOT", "US_FIGURE", "CN_SPIRITAI"]),
    "G2_LOGISTICS_WAREHOUSE": ("LOGISTICS",
                               ["US_AGILITY", "US_PICKLE", "US_BOSTON_DYNAMICS", "US_NIMBLE",
                                "CN_XSQUARE", "US_DEXTERITY"]),
}

# pairwise common-function coverage inside each group
pair_rows = []
for group, (scene, members) in SCENE_GROUPS.items():
    for a, b in itertools.combinations(members, 2):
        Ka = {k for k, v in ge10.get(a, {}).items()}
        Kb = {k for k, v in ge10.get(b, {}).items()}
        K = sorted(Ka & Kb)
        pair_rows.append({
            "case_group": group, "target_scene": scene,
            "company_a": a, "company_b": b,
            "wave_a": companies[a]["observation_date_min"], "wave_b": companies[b]["observation_date_min"],
            "same_wave": "YES" if companies[a]["observation_date_min"] == companies[b]["observation_date_min"] else "NO",
            "n_common_K": len(K),
            "common_K_list": "|".join(K),
            "common_K_names": "|".join(fname.get(k, k) for k in K),
            "meets_both_ge10": "YES" if (len(K) >= 2) else "NO",
            "per_company_K_a": "|".join(f"{k}={v}" for k, v in sorted(ge10.get(a, {}).items(), key=lambda x: (-x[1], x[0]))),
            "per_company_K_b": "|".join(f"{k}={v}" for k, v in sorted(ge10.get(b, {}).items(), key=lambda x: (-x[1], x[0]))),
            "eligible_for_weighted_comparison": "YES" if (len(K) >= 2) else "NO",
            "reason": ("双方均有至少10条活动可判读广告的具体职能满2个，可按研究书执行统一权重比较"
                       if len(K) >= 2 else
                       "共同职能不足2个各满10条，统一权重比较不适用，保留逐职能点值与有限描述"),
        })
BASE_STRATUM = "SYSTEM_PRODUCTS"
ORDER_TERMS = ("场景是否有实际使用证据", "观察批次是否与基准批一致", "主体范围是否与整机系统产品一致",
               "招聘数据质量分", "是否存在来源不足广告", "≥10条具体职能数", "company_id")
GROUP_ORDER = {}
for group, (scene, members) in SCENE_GROUPS.items():
    GROUP_ORDER[group] = sorted(members, key=lambda cid: (
        0 if scene in OBSERVED.get(cid, set()) else 1,
        0 if companies[cid]["observation_date_min"] == "2026-09-11" else 1,
        0 if companies[cid]["stratum"] == BASE_STRATUM else 1,
        0 if companies[cid]["hiring_data_quality_score"] in ("EXCELLENT", "GOOD") else 1,
        0 if (num(companies[cid]["primary_SOURCE_UNASSESSABLE"]) == 0
              and num(companies[cid]["activities_SOURCE_UNASSESSABLE"]) == 0) else 1,
        -len(ge10.get(cid, {})),
        cid))
SELECTED = [cid for g, order in GROUP_ORDER.items() for cid in order[:2]]
SELECT_GROUP = {cid: g for g, order in GROUP_ORDER.items() for cid in order[:2]}

SELECTED_PAIR_K = {}
for g, order in GROUP_ORDER.items():
    a, b = order[0], order[1]
    K = sorted({k for k in ge10.get(a, {})} & {k for k in ge10.get(b, {})})
    SELECTED_PAIR_K[g] = (a, b, K)
    for r in pair_rows:
        if r["case_group"] == g and {r["company_a"], r["company_b"]} == {a, b}:
            r["is_selected_pair"] = "YES"
            r["eligible_for_weighted_comparison"] = "YES" if len(K) >= 2 else "NO"
            r["reason"] = (f"入选对：共同职能{len(K)}个（{'|'.join(fname.get(k, k) for k in K)}）；"
                           + ("满足门槛，执行统一权重比较" if len(K) >= 2
                              else "不足2个共同职能，统一权重比较不适用，仅保留逐职能点值"))
        else:
            r.setdefault("is_selected_pair", "NO")
write("D7a_pairwise_common_functions.csv", pair_rows, list(pair_rows[0].keys()))

cand_rows = []
for group, (scene, members) in SCENE_GROUPS.items():
    order_key = GROUP_ORDER[group]
    for cid in members:
        c = companies[cid]
        st = next(r for r in status_rows if r["company_id"] == cid)
        obs = OBSERVED.get(cid, set())
        partners = [r for r in pair_rows if r["case_group"] == group and cid in (r["company_a"], r["company_b"])]
        best = max(partners, key=lambda r: r["n_common_K"]) if partners else None
        rank = order_key.index(cid) + 1
        row = {
            "case_group": group,
            "target_scene": scene,
            "selection_rank_in_group": rank,
            "company_id": cid,
            "company_name": c["company_name"],
            "country": c["country"],
            "stratum_name": c["stratum_name"],
            "n_ads": c["n_ads"],
            "observation_dates": c["observation_dates"],
            "hiring_wave": c["observation_date_min"],
            "scene_state_for_group": "OBSERVED_USE" if scene in obs else ("OTHER_STATE" if any(
                r["company_id"] == cid and r["scene"] == scene for r in scene_rows) else "NOT_RECORDED"),
            "any_observed_scene": "|".join(sorted(obs)),
            "n_scenes_observed": len(obs),
            "source_type": c["source_type"],
            "hiring_data_quality_score": c["hiring_data_quality_score"],
            "primary_SOURCE_UNASSESSABLE": c["primary_SOURCE_UNASSESSABLE"],
            "activities_SOURCE_UNASSESSABLE": c["activities_SOURCE_UNASSESSABLE"],
            "n_gaps_open": st["n_gaps_open"],
            "n_business_rows": st["n_responsibility_rows"],
            "n_delivery_rows": st["n_delivery_rows"],
            "n_unknown_stage_rows": st["n_unknown_stage_rows"],
            "n_concrete_functions_ge10": len(ge10.get(cid, {})),
            "concrete_functions_ge10": "|".join(sorted(ge10.get(cid, {}))),
            "best_partner": best["company_b"] if best and best["company_a"] == cid else (best["company_a"] if best else ""),
            "best_pair_common_K": best["n_common_K"] if best else 0,
            "best_pair_K_names": best["common_K_names"] if best else "",
            "meets_common_K_rule": "YES" if best and best["n_common_K"] >= 2 else "NO",
            "meets_source_complete_rule": "YES" if (c["hiring_data_quality_score"] in ("EXCELLENT", "GOOD")
                                                    and num(c["primary_SOURCE_UNASSESSABLE"]) == 0
                                                    and num(c["activities_SOURCE_UNASSESSABLE"]) == 0) else "NO",
            "selected": "YES" if cid in SELECTED else "NO",
        }
        if cid in SELECTED:
            pa, pb, K = SELECTED_PAIR_K[group]
            partner = pb if cid == pa else pa
            row["selected_pair_common_K"] = len(K)
            row["selected_pair_K_names"] = "|".join(fname.get(k, k) for k in K)
            row["comparison_eligible"] = ("YES" if len(K) >= 2 else "NO_COMPARISON_ONLY_DESCRIPTION")
            row["decision_reason"] = "；".join([
                f"主体范围：{c['stratum_name']}",
                f"产品场景：{scene}为{row['scene_state_for_group']}",
                f"观察批次：{row['hiring_wave']}",
                f"证据完整性：质量分{c['hiring_data_quality_score']}，来源不足广告"
                f"{c['primary_SOURCE_UNASSESSABLE']}/{c['activities_SOURCE_UNASSESSABLE']}",
                f"入选对共同职能覆盖：与{partner}共同{len(K)}个"
                f"（{'|'.join(fname.get(k, k) for k in K)}）",
                ("满足共同职能门槛，可执行统一权重比较" if len(K) >= 2
                 else "共同职能不足2个，统一权重比较不适用，仅保留逐职能点值与有限描述"),
                f"组内入选序位{rank}/{len(members)}",
            ])
        else:
            row["selected_pair_common_K"] = ""
            row["selected_pair_K_names"] = ""
            reasons = []
            if row["scene_state_for_group"] != "OBSERVED_USE":
                reasons.append(f"该组场景无实际使用证据（{scene}未取得OBSERVED_USE）")
            if row["hiring_wave"] != "2026-09-11":
                reasons.append("观察批次为2026-08-31，与入选公司不同批，时点可比性低")
            if row["meets_source_complete_rule"] == "NO":
                reasons.append("来源完整性规则未满足")
            if row["meets_common_K_rule"] == "NO":
                reasons.append("共同职能覆盖不足2个各满10条的具体职能")
            if companies[cid]["stratum"] != BASE_STRATUM:
                reasons.append(f"主体范围为{c['stratum_name']}，与该组整机系统产品口径不同")
            if cid == "CN_XSQUARE":
                reasons.append("物流真实场景客户未具名，责任主体无法定位")
            if not reasons:
                reasons.append("同组入选序位在后者，按研究书条款顺序未进入前两名")
            row["comparison_eligible"] = "NOT_SELECTED"
            row["decision_reason"] = "；".join(reasons)
        cand_rows.append(row)
write("D7_case_candidates.csv", cand_rows, list(cand_rows[0].keys()))

with (CASES / "case_selection.json").open("w", encoding="utf-8") as fh:
    json.dump({
        "rule": "按主体范围、产品场景、观察时点、证据完整性、共同职能覆盖依次比较；统计差距不作入选依据",
        "selection_order_key": list(ORDER_TERMS),
        "selected": SELECTED,
        "selected_groups": {g: order[:2] for g, order in GROUP_ORDER.items()},
        "group_rank_order": GROUP_ORDER,
        "weighted_comparison_eligible": {
            g: ("YES" if any(r["eligible_for_weighted_comparison"] == "YES"
                             for r in pair_rows if r["case_group"] == g
                             and r["company_a"] in order[:2] and r["company_b"] in order[:2]) else "NO")
            for g, order in GROUP_ORDER.items()},
        "common_K_rule": "双方均需有至少10条活动可判读广告的具体主职能，且至少2个共同职能",
        "reasons": {r["company_id"]: r["decision_reason"] for r in cand_rows if r["selected"] == "YES"},
        "excluded": [{"company_id": r["company_id"], "case_group": r["case_group"],
                      "reason": r["decision_reason"]} for r in cand_rows if r["selected"] == "NO"],
        "counterexample_scan": "已对同一场景组全部候选逐一记录排名与排除理由，未只保留支持预期的公司",
    }, fh, ensure_ascii=False, indent=2)

summary = {
    "n_facts_inherited": len(facts),
    "n_long_rows": len(long_rows),
    "n_business_rows": sum(1 for r in long_rows if r["business_stage"] in BUSINESS_STAGES),
    "n_business_rows_known_subject": sum(1 for r in long_rows if r["business_stage"] in BUSINESS_STAGES
                                         and r["responsibility_subject"] != "UNKNOWN"),
    "n_gap_rows": len(gaps),
    "n_gaps_open": sum(1 for g in gaps if g["open_at_stage_b_end"] == "YES"),
    "stage_distribution": Counter(r["business_stage"] for r in long_rows).most_common(),
    "subject_distribution_business_only": Counter(r["responsibility_subject"] for r in long_rows
                                                  if r["business_stage"] in BUSINESS_STAGES).most_common(),
    "evidence_class_business_only": Counter(r["evidence_class"] for r in long_rows
                                            if r["business_stage"] in BUSINESS_STAGES).most_common(),
    "eligible_weighted_pairs": [f'{r["company_a"]}x{r["company_b"]}' for r in pair_rows
                                if r["eligible_for_weighted_comparison"] == "YES"],
    "selected_cases": SELECTED,
}
(VER / "step2_checks.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))
