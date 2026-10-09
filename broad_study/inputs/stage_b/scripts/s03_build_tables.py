"""Stage B repair / step 3: build every outward-facing table from the corrected
fact layer.

Contracts enforced here (each one closes a finding in the acceptance report):

  * A fact's time qualification comes only from the evidence rows whose declared
    relation is SUPPORTS or REFUTES. CONTEXT_ONLY / ACCESS_NOTE material can never
    supply the event date or the publication date of a fact it does not support.
  * An assertion is usable at the observation date only when both its event date
    and its publication date fall at or before that date. Late publication becomes
    RETROSPECTIVE_LATE_PUBLISH, a post-observation event becomes
    POST_OBSERVATION_EVENT, an imprecise date that straddles the observation date
    becomes DATE_IMPRECISE_SPANS_OBS, and anything else becomes DATE_UNKNOWN.
    No minimum over several dates is taken.
  * Relations are taken verbatim from the authored layer: nothing is inferred from
    an evidence id's prefix.
  * A company that was not researched keeps an explicit not-yet-mapped status for
    every inherited gap, and a company-specific inherited question is never closed
    on behalf of a company this run did not research.
  * A capital row is one real event over one or more sources, with the amount,
    currency, unit and amount scope recorded as structured fields; valuation stays
    apart from the amount.
"""
from __future__ import annotations

import glob
import json
import os
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import (  # noqa: E402
    CORE_FIELDS, QUALIFYING_RELATIONS, R3, RUN, WORK, date_precision, load_companies,
    qualify_assertion, read_csv, stable, time_applicability, write_csv, write_json,
)

FACT_FIELDS = [
    "fact_id", "company_id", "field", "fact_seq", "assertion_kind", "merge_parent_field",
    "subject_entity", "subject_scope", "product_or_business_scope", "event_or_period",
    "aggregation", "value", "unit", "value_status", "research_status", "observation_date",
    "time_applicability", "time_reason", "time_basis_evidence_ids",
    "event_date", "publication_date", "date_precision", "evidence_ids",
    "inherited_gap_ids", "decision_reason", "note", "checked_in_stage_b",
]

EVIDENCE_FIELDS = [
    "evidence_id", "record_kind", "company_id", "subject_entity", "field", "claim",
    "quote", "quote_locator", "source_title", "publisher", "source_nature", "url",
    "url_note", "publication_date", "event_date", "event_date_precision", "retrieved_at",
    "date_precision", "claim_nature", "access_status", "snapshot_id", "snapshot_text_path",
    "snapshot_raw_path", "snapshot_sha256", "linked_inherited_evidence",
    "relation_to_inherited", "note", "capture_medium", "snapshot_raw_sha256", "capture_record_path", "capture_record_sha256",
]

LINK_FIELDS = ["link_id", "company_id", "fact_id", "field", "evidence_id", "relation",
               "qualifies_date", "scope_match", "review_note"]

CAPITAL_FIELDS = [
    "capital_event_id", "company_id", "subject_entity", "event_type", "round_or_deal",
    "amount_original", "currency", "amount_unit", "amount_scope",
    "post_money_valuation_original", "post_money_valuation_currency",
    "wording_original", "declared_event_or_period",
    "event_date", "event_date_precision", "publication_date",
    "publication_date_precision", "retrieved_at", "evidence_ids", "source_count",
    "claim_nature", "at_observation_availability", "time_applicability", "conflict_note", "note",
]

GAP_FIELDS = [
    "orig_gap_id", "company_id", "fact_field", "gap_type_inherited", "inherited_value",
    "inherited_evidence_ids", "stage_b_status", "stage_b_result", "new_fact_ids",
    "new_evidence_ids", "closure_reason", "affects_entity_or_scope", "affects_grouping",
    "affects_time_applicability", "open_at_stage_b_end", "company_researched_this_run",
]

GROUP_FIELDS = [
    "company_id", "dimension", "group_value", "basis_fact_ids", "evidence_strength",
    "value_status", "time_applicability", "comparison_bucket",
    "included_in_comparison", "exclusion_reason", "multiple_allowed", "rule_version",
]

# inherited gap "fact" values -> Stage B fact fields (uniform vocabulary)
GAP_FACT_TO_FIELDS = {
    "entity_and_hiring_scope": ["research_subject", "hiring_board_channel", "observation_coverage"],
    "headquarters": ["hq_or_team_location"],
    "founded_or_team_start": ["founded_or_team_start_date"],
    "founded_or_team_start_date": ["founded_or_team_start_date"],
    "parent_relationship": ["parent_relationship"],
    "parent_listing_status": ["parent_listing_status"],
    "own_listing_status": ["own_listing_status"],
    "latest_disclosed_financing": ["latest_financing_disclosed", "latest_financing_at_observation"],
    "ma_events": ["ma_events"],
    "commercialization_research": ["evidence_demo", "evidence_internal_test"],
    "commercialization_research_date": ["evidence_demo", "evidence_internal_test"],
    "commercialization_prototype": ["evidence_demo", "evidence_internal_test"],
    "commercialization_prototype_date": ["evidence_demo", "evidence_internal_test"],
    "commercialization_external_pilot": ["evidence_external_pilot"],
    "commercialization_external_pilot_date": ["evidence_external_pilot"],
    "commercialization_delivery": ["evidence_customer_delivery"],
    "commercialization_delivery_date": ["evidence_customer_delivery"],
    "commercialization_deployment": ["deployment_status_actual"],
    "commercialization_deployment_date": ["deployment_status_actual"],
    "commercialization_manufacturing_scale_up": ["evidence_production_shipment"],
    "commercialization_scaled_operation": ["evidence_sustained_use", "deployment_status_actual"],
    "commercialization_paid": ["evidence_paid"],
    "commercialization_paid_date": ["evidence_paid"],
    "commercialization_repeat_order": ["evidence_repeat_order"],
    "product_or_service_scope": ["product_lines", "delivery_form"],
    "product_delivery_form": ["delivery_form"],
    "target_markets": ["target_markets", "named_customers_or_partners"],
    "evidence_publication_dates": ["__publication_dates__"],
    "inherited_open_question": ["__open_question__"],
    "hiring_source_change": ["hiring_source_history"],
    "parent_operational_scale_boundary": ["__boundary__"],
    "sample_company_scope": ["research_subject"],
    "acquisition_boundary": ["__acquisition_boundary__"],
}

BUCKET_BY_STATUS = {
    "FOUND": "ESTABLISHED",
    "SEARCHED_NOT_FOUND": "SEARCHED_NOT_FOUND",
    "NOT_YET_SEARCHED": "NOT_YET_SEARCHED",
    "NOT_APPLICABLE": "NOT_APPLICABLE",
    "ACCESS_BLOCKED": "ACCESS_BLOCKED",
    "INHERITED_ONLY": "INHERITED_ONLY",
}


def bucket(status: str) -> str:
    if status in ("SUPPORTED_EXTERNAL", "COMPANY_SELF_REPORT", "MEDIA_STATEMENT",
                  "COUNTERPARTY_CONFIRMATION", "MEDIA_AND_THIRD_PARTY_RECORD",
                  "PUBLISHED_BY_THIRD_PARTY_FROM_PROVIDER", "MIXED_SEE_EVIDENCE",
                  "CONFLICT_RESOLVED_BY_SEPARATION"):
        return "FOUND"
    if status == "SEARCHED_NOT_FOUND":
        return "SEARCHED_NOT_FOUND"
    if status == "NOT_YET_SEARCHED":
        return "NOT_YET_SEARCHED"
    if status == "NOT_APPLICABLE":
        return "NOT_APPLICABLE"
    if status == "ACCESS_BLOCKED":
        return "ACCESS_BLOCKED"
    if status in ("INHERITED_UNVERIFIED", "PARENT_CONTEXT_ONLY"):
        return "INHERITED_ONLY"
    return "OTHER"


def classify_gap(gap: dict, facts_by_field: dict[str, list[dict]], new_ev: dict,
                 is_researched: bool) -> dict:
    """Map one inherited gap item to its Stage B result.

    A company this run did not research keeps an explicit not-yet-mapped status for
    every one of its inherited items, including inherited open questions: a
    build-wide rule calibrated on the pilots can never close a company-specific
    question on behalf of a company nobody looked at.
    """
    fact_field = gap["fact"]
    mapped = GAP_FACT_TO_FIELDS.get(fact_field)
    row = {
        "orig_gap_id": gap["gap_id"],
        "company_id": gap["company_id"],
        "fact_field": fact_field,
        "gap_type_inherited": gap["gap_type"],
        "inherited_value": gap["inherited_value"],
        "inherited_evidence_ids": gap["existing_evidence_ids"],
        "affects_entity_or_scope": gap["affects_entity_or_scope"],
        "affects_grouping": gap["affects_grouping"],
        "affects_time_applicability": gap["affects_time_applicability"],
        "company_researched_this_run": "YES" if is_researched else "NO",
    }

    def not_mapped(reason: str) -> dict:
        row.update({
            "stage_b_status": "NOT_YET_MAPPED_THIS_RUN",
            "stage_b_result": reason,
            "new_fact_ids": "", "new_evidence_ids": "",
            "closure_reason": "",
            "open_at_stage_b_end": "YES",
        })
        return row

    if mapped is None:
        row.update({
            "stage_b_status": "UNRESOLVED_MAPPING",
            "stage_b_result": "NO_EXPLICIT_FIELD_MAPPING",
            "new_fact_ids": "", "new_evidence_ids": "", "closure_reason": "",
            "open_at_stage_b_end": "YES",
        })
        return row

    if not is_researched:
        return not_mapped(
            "公司本轮未查证；该缺口按未查状态保留，留待后续批次，不因通用规则关闭")

    if mapped == ["__publication_dates__"]:
        comp_evs = [e for e in new_ev.values() if e["company_id"] == gap["company_id"]]
        dated = [e for e in comp_evs if e.get("publication_date")]
        row.update({
            "stage_b_status": "RESOLVED_PARTIAL",
            "stage_b_result": f"{len(dated)} of {len(comp_evs)} Stage B evidence rows carry a publication date; undated rows remain undated",
            "new_fact_ids": "",
            "new_evidence_ids": "|".join(sorted(e["evidence_id"] for e in comp_evs)),
            "closure_reason": "Publication dates were recovered for the openable pages; rows that carry no published date on the page remain DATE_UNKNOWN by design.",
            "open_at_stage_b_end": "PARTIAL",
        })
        return row

    if mapped == ["__open_question__"]:
        row.update({
            "stage_b_status": "RESOLVED_PARTIAL",
            "stage_b_result": "本轮查证给出部分答复；原问题本身不因通用规则关闭",
            "new_fact_ids": "", "new_evidence_ids": "",
            "closure_reason": ("公司本轮已查证，答复见公司卡开放项一节；未取得决定性证据前不改写为已解决。"
                               "原问题：" + gap["inherited_value"][:160]),
            "open_at_stage_b_end": "PARTIAL",
        })
        return row

    if mapped == ["__boundary__"]:
        row.update({
            "stage_b_status": "RESOLVED_BY_SEPARATION_RULE",
            "stage_b_result": "Boundary rule applied: parent scale kept as context only, never assigned to the FAR team",
            "new_fact_ids": "", "new_evidence_ids": "B_US_AMAZON_FTR_007",
            "closure_reason": "Inherited conflict is resolved by an explicit separation rule rather than by averaging the two sides.",
            "open_at_stage_b_end": "NO",
        })
        return row

    if mapped == ["__acquisition_boundary__"]:
        row.update({
            "stage_b_status": "DEFERRED_TO_STAGE_B_BATCH_2",
            "stage_b_result": "Acquisition-boundary company not in the three-company repair batch; scheduled for the remaining batch",
            "new_fact_ids": "", "new_evidence_ids": "",
            "closure_reason": "", "open_at_stage_b_end": "YES",
        })
        return row

    rows = [f for f in facts_by_field.get(fact_field, [])]
    present = [f for field_name in mapped for f in facts_by_field.get(field_name, [])]
    if not present:
        return not_mapped("Field not assessed for this company in this run")
    fact_ids = [f["fact_id"] for f in present]
    ev_ids: list[str] = []
    for f in present:
        ev_ids.extend(f["evidence_ids"])
        if f["time_basis_evidence_ids"]:
            ev_ids.extend(f["time_basis_evidence_ids"])
    statuses = [f["value_status"] for f in present]
    buckets = [bucket(s) for s in statuses]
    if all(b == "NOT_APPLICABLE" for b in buckets):
        stage_status = "RESOLVED_NOT_APPLICABLE"
    elif any(b == "FOUND" for b in buckets):
        stage_status = "RESOLVED_FOUND"
    elif any(b == "SEARCHED_NOT_FOUND" for b in buckets):
        stage_status = "NOT_FOUND_NOT_DEFINITE"
    elif any(b == "ACCESS_BLOCKED" for b in buckets):
        stage_status = "ACCESS_BLOCKED"
    elif any(b == "NOT_YET_SEARCHED" for b in buckets):
        stage_status = "NOT_YET_SEARCHED"
    else:
        stage_status = "INHERITED_ONLY"

    row.update({
        "stage_b_status": stage_status,
        "stage_b_result": "; ".join(f"{f['field']}={f['value_status']}" for f in present),
        "new_fact_ids": "|".join(dict.fromkeys(fact_ids)),
        "new_evidence_ids": "|".join(dict.fromkeys(e for e in ev_ids if e)),
        "closure_reason": "" if stage_status in ("NOT_YET_SEARCHED", "INHERITED_ONLY",
                                                 "NOT_FOUND_NOT_DEFINITE") else
                          "Mapped to Stage B fields: " + ", ".join(sorted({f["field"] for f in present})),
        "open_at_stage_b_end": "NO" if stage_status in ("RESOLVED_FOUND", "RESOLVED_NOT_APPLICABLE") else "YES",
    })
    return row


SELF_ONLY_NATURE = {"COMPANY_SELF_REPORT", "PARENT_CONTEXT"}


def coarse_type(claim_nature: str) -> str:
    if claim_nature in ("COMPANY_SELF_REPORT", "PARENT_CONTEXT"):
        return claim_nature
    if claim_nature in ("INDEPENDENT_CHANNEL_STATEMENT", "COUNTERPARTY_STATEMENT"):
        return "COUNTERPARTY_CONFIRMATION"
    if claim_nature in ("MEDIA_STATEMENT", "MEDIA_REPORT"):
        return "MEDIA_STATEMENT"
    return claim_nature


def degrade_value_status(status: str, supporting_natures: set[str]) -> tuple[str, str]:
    """Never let a claim rest on a weaker source than the status it declares.

    A fact whose only supporting evidence is the company's own material, or the
    parent company's material, cannot be advertised as an outside confirmation.
    """
    if status != "SUPPORTED_EXTERNAL" or not supporting_natures:
        return status, ""
    if supporting_natures <= {"COMPANY_SELF_REPORT"}:
        return "COMPANY_SELF_REPORT", ("仅有公司自述材料支持，按自述记录，不升级为外部确认"
                                       "（返修：原送审版本此类字段标为 SUPPORTED_EXTERNAL）")
    if supporting_natures <= SELF_ONLY_NATURE:
        return "PARENT_CONTEXT_ONLY", "仅有公司自述与母公司背景材料支持，按背景记录"
    if supporting_natures <= {"MEDIA_STATEMENT"}:
        return "MEDIA_STATEMENT", "仅有媒体报道支持，按媒体陈述记录"
    return status, ""


def main() -> int:
    lock = json.load(open(os.path.join(WORK, "input_lock.json"), encoding="utf-8"))
    companies = load_companies()
    inherited_gaps = read_csv(os.path.join(R3, "company_gaps.csv"))
    snap_index = json.load(open(os.path.join(WORK, "snapshot_index.json"), encoding="utf-8"))["snapshots"]

    authored = []
    for path in sorted(glob.glob(os.path.join(WORK, "pilot_facts_v2_*.json"))):
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not data.get("facts"):
            # a company whose authored file is still an empty skeleton keeps every
            # inherited gap in the not-yet-searched state and contributes no rows
            continue
        authored.append(data)
    researched = sorted(c["company_id"] for c in authored)

    fact_rows, evidence_rows, link_rows, capital_rows = [], [], [], []
    degraded: list[dict] = []
    facts_by_company_field: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
    new_ev_by_id: dict[str, dict] = {}

    for comp in authored:
        cid = comp["company_id"]
        obs = comp["observation_date"]
        subject_default = comp.get("research_subject", "")

        for ev in comp["evidence"]:
            snap = snap_index.get(ev.get("snapshot_id", ""), {})
            row = dict(ev)
            row.update({
                "company_id": cid,
                "subject_entity": subject_default,
                "record_kind": "STAGE_B_NEW",
                "snapshot_text_path": snap.get("snapshot_text_path", ""),
                "snapshot_raw_path": snap.get("snapshot_raw_path", ""),
                "snapshot_sha256": snap.get("body_text_sha256", ""),
                "capture_medium": snap.get("capture_medium", "ORIGINAL_HTTP_BYTES" if snap.get("snapshot_raw_path") else "LEGACY_TEXT_RECORD"),
                "snapshot_raw_sha256": snap.get("raw_sha256", "") if snap.get("snapshot_raw_path") else "",
                "capture_record_path": snap.get("capture_record_path", ""),
                "capture_record_sha256": snap.get("capture_record_sha256", ""),
                "linked_inherited_evidence": "|".join(ev.get("linked_inherited_evidence", []) or []),
            })
            evidence_rows.append(row)
            new_ev_by_id[row["evidence_id"]] = row

        rel_by_pair = {(r["fact_id"], r["evidence_id"]): r for r in comp["relations"]}

        for fact in comp["facts"]:
            ev_ids = fact["evidence_ids"]
            qualifying = [e for e in ev_ids
                          if rel_by_pair.get((fact["fact_id"], e), {}).get("relation") in QUALIFYING_RELATIONS]
            # a claim may never rest on a weaker source than the status it declares:
            # self-report-only support becomes a self-report fact, never an outside one
            supporting_natures = {coarse_type(new_ev_by_id[e].get("claim_nature", ""))
                                  for e in qualifying if e in new_ev_by_id}
            value_status, degrade_note = degrade_value_status(fact["value_status"], supporting_natures)
            if value_status == "SUPPORTED_EXTERNAL" and not qualifying:
                value_status, extra = "COMPANY_SELF_REPORT", (
                    "无直接支持证据（仅有背景或访问记录关系），按自述/背景记录，不标为外部确认")
                degrade_note = (degrade_note + "；" if degrade_note else "") + extra
            if degrade_note:
                degraded.append({"fact_id": fact["fact_id"], "from": fact["value_status"],
                                 "to": value_status, "supporting_natures": sorted(supporting_natures),
                                 "reason": degrade_note})
            ev_pairs = [(new_ev_by_id[e].get("event_date", ""),
                         new_ev_by_id[e].get("publication_date", ""))
                        for e in qualifying if e in new_ev_by_id]
            time_sensitive = value_status not in ("NOT_APPLICABLE",)
            ta, reason, ev_date, pub_date = qualify_assertion(
                ev_pairs, obs, time_sensitive=time_sensitive)
            row = {
                "fact_id": fact["fact_id"],
                "company_id": cid,
                "field": fact["field"],
                "fact_seq": fact["fact_seq"],
                "assertion_kind": fact["assertion_kind"],
                "merge_parent_field": fact["merge_parent_field"],
                "subject_entity": fact["subject_entity"],
                "subject_scope": fact["subject_scope"],
                "product_or_business_scope": fact["product_or_business_scope"],
                "event_or_period": fact["event_or_period"],
                "aggregation": fact["aggregation"],
                "value": fact["value"],
                "unit": fact["unit"],
                "value_status": value_status,
                "research_status": fact["research_status"],
                "observation_date": obs,
                "time_applicability": ta,
                "time_reason": reason,
                "time_basis_evidence_ids": "|".join(qualifying),
                "event_date": ev_date,
                "publication_date": pub_date,
                "date_precision": date_precision(ev_date or pub_date),
                "evidence_ids": "|".join(ev_ids),
                "inherited_gap_ids": "|".join(fact["inherited_gap_ids"]),
                "decision_reason": (fact["decision_reason"] + ("；" + degrade_note if degrade_note else "")),
                "note": fact["note"],
                "checked_in_stage_b": fact["checked_in_stage_b"],
            }
            fact_rows.append(row)
            facts_by_company_field[cid][fact["field"]].append(row)

            for e in ev_ids:
                rel = rel_by_pair.get((fact["fact_id"], e))
                if rel is None:
                    raise SystemExit(f"missing declared relation for {fact['fact_id']} -> {e}")
                link_rows.append({
                    "link_id": f"L_{fact['fact_id']}__{e}",
                    "company_id": cid,
                    "fact_id": fact["fact_id"],
                    "field": fact["field"],
                    "evidence_id": e,
                    "relation": rel["relation"],
                    "qualifies_date": "YES" if rel["relation"] in QUALIFYING_RELATIONS else "NO",
                    "scope_match": ("SUBJECT_AND_PRODUCT_SCOPE_RECORDED" if rel["relation"] in QUALIFYING_RELATIONS
                                    else "BACKGROUND_NOT_QUALIFYING"),
                    "review_note": rel["review_note"],
                })

        capital_list = comp.get("capital_events") or []
        for cap in capital_list:
            evs = [new_ev_by_id[e] for e in cap["evidence_ids"]]
            pairs = [(e.get("event_date", ""), e.get("publication_date", "")) for e in evs]
            declared_ev = cap.get("event_date", "") or ""
            declared_pub = cap.get("publication_date", "") or ""
            if declared_ev or declared_pub:
                declared_pair = (declared_ev, declared_pub)
                if declared_pair not in pairs:
                    # a declared pair must belong to one source; otherwise keep it but
                    # qualify it on its own instead of mixing dates across sources
                    pairs = [declared_pair] + [p for p in pairs if p != ("", "")]
                else:
                    pairs = [declared_pair] + [p for p in pairs if p != declared_pair]
            ta, reason, evd, pub = qualify_assertion(pairs, obs)
            if declared_ev or declared_pub:
                evd, pub = declared_ev, declared_pub
                ta, reason = time_applicability(evd, pub, obs)
            # several sources describing one event may disagree (a company timeline and
            # a news report often differ by a month): keep every distinct date on the
            # event instead of collapsing them with a minimum
            conflict = cap.get("conflict_note", "")
            dated_pairs = [(e.get("event_date", ""), e.get("publication_date", "")) for e in evs
                           if e.get("event_date") or e.get("publication_date")]
            if len({p[1] for p in dated_pairs if p[1]}) > 1 and not conflict:
                conflict = "来源发布日期不一致，按原成对日期分别保存，不取最早日期拼合"
            capital_rows.append({
                "capital_event_id": f"C_{cid}__{cap['event_key']}",
                "company_id": cid,
                "subject_entity": facts_by_company_field[cid].get("latest_financing_disclosed", [{}])[0].get(
                    "subject_entity", subject_default),
                "event_type": cap["event_type"],
                "round_or_deal": cap["round_or_deal"],
                "amount_original": cap.get("amount_original", ""),
                "currency": cap.get("currency", ""),
                "amount_unit": cap.get("amount_unit", ""),
                "amount_scope": cap.get("amount_scope", ""),
                "post_money_valuation_original": cap.get("post_money_valuation_original", ""),
                "post_money_valuation_currency": cap.get("post_money_valuation_currency", ""),
                "wording_original": cap.get("wording_original", ""),
                "declared_event_or_period": cap.get("declared_event_or_period", ""),
                "event_date": evd,
                "event_date_precision": date_precision(evd),
                "publication_date": pub,
                "publication_date_precision": date_precision(pub),
                "retrieved_at": max([e.get("retrieved_at", "") for e in evs], default=""),
                "evidence_ids": "|".join(cap["evidence_ids"]),
                "source_count": len(cap["evidence_ids"]),
                "claim_nature": cap.get("claim_nature", "MEDIA_OR_COMPANY_DISCLOSURE"),
                "at_observation_availability": ta,
                "time_applicability": ta,
                "conflict_note": conflict,
                "note": cap.get("note", "") + ("" if ta == "USABLE_AT_OBSERVATION" else f"（时点判定：{reason}）"),
            })

    write_csv(os.path.join(RUN, "company_facts.csv"), FACT_FIELDS,
              stable(fact_rows, ["company_id", "field", "fact_seq"]))
    write_csv(os.path.join(RUN, "company_evidence.csv"), EVIDENCE_FIELDS,
              stable(evidence_rows, ["company_id", "evidence_id"]))
    write_csv(os.path.join(RUN, "evidence_links.csv"), LINK_FIELDS,
              stable(link_rows, ["company_id", "link_id"]))
    write_csv(os.path.join(RUN, "capital_events.csv"), CAPITAL_FIELDS,
              stable(capital_rows, ["company_id", "capital_event_id"]))

    gap_rows = []
    for g in inherited_gaps:
        cid = g["company_id"]
        gap_rows.append(classify_gap(g, facts_by_company_field.get(cid, {}), new_ev_by_id,
                                     cid in researched))
    write_csv(os.path.join(RUN, "company_gaps.csv"), GAP_FIELDS,
              stable(gap_rows, ["company_id", "orig_gap_id"]))

    dist = {
        "n_facts": len(fact_rows),
        "n_evidence": len(evidence_rows),
        "n_links": len(link_rows),
        "n_capital_rows": len(capital_rows),
        "n_gap_rows": len(gap_rows),
        "fact_by_time_applicability": dict(Counter(f["time_applicability"] for f in fact_rows).most_common()),
        "fact_by_value_status": dict(Counter(f["value_status"] for f in fact_rows).most_common()),
        "link_by_relation": dict(Counter(l["relation"] for l in link_rows).most_common()),
        "gap_by_status": dict(Counter(r["stage_b_status"] for r in gap_rows).most_common()),
        "source_upgrade_corrections": degraded,
        "gap_by_company_status": {},
        "self_check": {
            "relations_declared": len(link_rows),
            "links_qualifying_date": sum(1 for l in link_rows if l["qualifies_date"] == "YES"),
            "links_background": sum(1 for l in link_rows if l["qualifies_date"] == "NO"),
            "facts_usable_at_observation": sum(1 for f in fact_rows if f["time_applicability"] == "USABLE_AT_OBSERVATION"),
            "facts_without_qualifying_evidence": [f["fact_id"] for f in fact_rows
                                                  if f["value_status"] not in
                                                  ("NOT_APPLICABLE", "NOT_YET_SEARCHED", "SEARCHED_NOT_FOUND",
                                                   "ACCESS_BLOCKED", "INHERITED_UNVERIFIED", "PARENT_CONTEXT_ONLY")
                                                  and not f["time_basis_evidence_ids"]],
        },
    }
    per = defaultdict(Counter)
    for r in gap_rows:
        per[r["company_id"]][r["stage_b_status"]] += 1
    dist["gap_by_company_status"] = {k: dict(v.most_common()) for k, v in sorted(per.items())}
    write_json(os.path.join(WORK, "build_summary.json"), dist)

    print(json.dumps(dist, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
