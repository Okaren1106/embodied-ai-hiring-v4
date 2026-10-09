"""Repair pass / diagnostic: enumerate the concrete defects the audit found.

Read-only with respect to both the submitted package and the r3 baseline.
Writes work/diag_current.json so every later fix can be checked against the
same list of defect instances.
"""
from __future__ import annotations

import csv
import json
import os
from collections import Counter, defaultdict

SRC = r"D:\Embod AI analysis\embodied-ai-hiring-research\reports\2026-09-14_company_data_analysis\stage_b\run_20260914T142852Z"
R3 = r"D:\Embod AI analysis\embodied-ai-hiring-research\reports\2026-09-14_company_data_analysis\stage_a_r3"
RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(RUN, "work")


def rows(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    facts = rows(os.path.join(SRC, "company_facts.csv"))
    evid = rows(os.path.join(SRC, "company_evidence.csv"))
    links = rows(os.path.join(SRC, "evidence_links.csv"))
    caps = rows(os.path.join(SRC, "capital_events.csv"))
    gaps = rows(os.path.join(SRC, "company_gaps.csv"))
    groups = rows(os.path.join(SRC, "company_group_mapping.csv"))
    pil = {cid: rows(os.path.join(R3, "T1_sample_company.csv")) for cid in [""]}
    t1 = rows(os.path.join(R3, "T1_sample_company.csv"))
    all_ids = {r["company_id"] for r in t1}
    authored = sorted({f["company_id"] for f in facts})
    unsearched = sorted(all_ids - set(authored))

    ev_by_id = {e["evidence_id"]: e for e in evid}

    # --- 2. time: USABLE_AT_OBSERVATION rows and how their dates were derived
    usable = []
    for f in facts:
        if f["time_applicability"] != "USABLE_AT_OBSERVATION":
            continue
        evs = [e for e in f["evidence_ids"].split("|") if e]
        det = []
        for e in evs:
            x = ev_by_id.get(e, {})
            det.append({"evidence_id": e, "publication_date": x.get("publication_date", ""),
                        "event_date": x.get("event_date", ""),
                        "relation_to_inherited": x.get("relation_to_inherited", ""),
                        "note_head": (x.get("note", "") or "")[:60]})
        usable.append({"fact_id": f["fact_id"], "field": f["field"], "meta_field": f.get("meta_field", ""),
                       "value_status": f["value_status"], "fact_event_date": f["event_date"],
                       "fact_publication_date": f["publication_date"], "evidence": det,
                       "value_head": (f["value"] or "")[:70]})

    # --- 3. unknown turned into definite
    snf = [{"fact_id": f["fact_id"], "field": f["field"], "value": f["value"],
            "value_status": f["value_status"], "research_status": f["research_status"]}
           for f in facts if f["value_status"] == "SEARCHED_NOT_FOUND"]
    listing_groups = [g for g in groups if g["dimension"] == "own_listing_status"]

    # --- 4. inherited open questions wrongly resolved
    oq = [{"orig_gap_id": g["orig_gap_id"], "company_id": g["company_id"],
           "status": g["stage_b_status"], "open_at_end": g["open_at_stage_b_end"],
           "result": g["stage_b_result"][:90], "inherited_value": (g["inherited_value"] or "")[:110]}
          for g in gaps if g["fact_field"] == "inherited_open_question"]
    oq_resolved = [x for x in oq if x["status"].startswith("RESOLVED")]
    oq_from_unsearched = [x for x in oq_resolved if x["company_id"] in unsearched]

    # --- 7. research_status vs checked_in_stage_b contradiction
    contradict = [{"fact_id": f["fact_id"], "research_status": f["research_status"],
                   "checked_in_stage_b": f["checked_in_stage_b"],
                   "value_status": f["value_status"]}
                  for f in facts if f["research_status"] == "NOT_YET_SEARCHED" and f["checked_in_stage_b"] == "YES"]
    checked_dist = Counter(f["checked_in_stage_b"] for f in facts)

    # --- 5/6. evidence binding + relations
    rel = Counter(l["relation"] for l in links)
    b_prefix = [l for l in links if l["evidence_id"].startswith("B_")]
    ctx_ev = {e["evidence_id"]: e for e in evid
              if e.get("relation_to_inherited") in ("PARENT_CONTEXT_ONLY", "ACCESS_NOTE")
              or e.get("access_status") != "OK"}
    ctx_but_supports = [{"link_id": l["link_id"], "fact_id": l["fact_id"], "evidence_id": l["evidence_id"],
                         "relation": l["relation"],
                         "evidence_kind": ctx_ev[l["evidence_id"]].get("relation_to_inherited", ""),
                         "access": ctx_ev[l["evidence_id"]].get("access_status", "")}
                        for l in links if l["evidence_id"] in ctx_ev and l["relation"] == "SUPPORTS"]
    selfreport_supported_external = []
    for f in facts:
        if f["value_status"] != "SUPPORTED_EXTERNAL":
            continue
        evs = [ev_by_id[e] for e in f["evidence_ids"].split("|") if e in ev_by_id]
        if evs and all(e.get("claim_nature") == "COMPANY_SELF_REPORT" for e in evs):
            selfreport_supported_external.append(
                {"fact_id": f["fact_id"], "field": f["field"], "evidence_ids": f["evidence_ids"],
                 "decision_reason": (f["decision_reason"] or "")[:90]})

    # --- 6. capital table reality
    capital = [{k: c[k] for k in ("capital_event_id", "company_id", "event_type", "round_or_deal",
                                  "amount_original", "currency", "amount_unit", "amount_scope",
                                  "event_date", "publication_date", "evidence_ids", "wording_original")}
               for c in caps]

    # --- fact granularity: how many field rows a company currently has
    per_company_field = defaultdict(int)
    for f in facts:
        per_company_field[(f["company_id"], f["field"])] += 1
    multi = {f"{k[0]}|{k[1]}": v for k, v in per_company_field.items() if v > 1}

    out = {
        "source_package": SRC,
        "n_facts": len(facts), "n_evidence": len(evid), "n_links": len(links),
        "n_capital": len(caps), "n_gaps": len(gaps), "n_groups": len(groups),
        "authored_companies": authored, "unsearched_companies": unsearched,
        "n_unsearched": len(unsearched),
        "A_time": {"n_usable_at_observation": len(usable), "rows": usable},
        "B_unknown": {"n_searched_not_found": len(snf), "rows": snf,
                      "listing_group_rows": listing_groups},
        "C_open_questions": {"n_total": len(oq), "n_resolved": len(oq_resolved),
                             "n_resolved_from_unsearched": len(oq_from_unsearched),
                             "unsearched_resolved_ids": [x["orig_gap_id"] for x in oq_from_unsearched],
                             "rows": oq},
        "D_relations": {"relation_counts": dict(rel), "n_links": len(links),
                        "n_B_prefix": len(b_prefix),
                        "context_evidence_marked_supports": ctx_but_supports},
        "E_source_upgrade": {"n_selfreport_as_external": len(selfreport_supported_external),
                             "rows": selfreport_supported_external},
        "F_capital": capital,
        "G_progress": {"checked_in_stage_b_distribution": dict(checked_dist),
                       "contradiction": contradict},
        "H_granularity": {"n_company_field_with_multiple_rows": len(multi), "detail": multi},
    }
    os.makedirs(WORK, exist_ok=True)
    with open(os.path.join(WORK, "diag_current.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)

    print(json.dumps({
        "n_facts": out["n_facts"], "n_evidence": out["n_evidence"], "n_links": out["n_links"],
        "n_capital": out["n_capital"], "n_gaps": out["n_gaps"],
        "A_n_usable": len(usable),
        "B_n_searched_not_found": len(snf),
        "C_open_questions_total": len(oq), "C_resolved": len(oq_resolved),
        "C_resolved_from_unsearched": len(oq_from_unsearched),
        "D_relation_counts": dict(rel),
        "D_context_marked_supports": len(ctx_but_supports),
        "E_selfreport_as_external": len(selfreport_supported_external),
        "G_contradiction": len(contradict),
        "H_multi_row_company_fields": len(multi),
        "unsearched_n": len(unsearched),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
