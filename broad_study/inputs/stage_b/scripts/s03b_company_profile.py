"""Stage B repair / step 4b: the 24-row company master table.

One row per inherited company_id, carrying the inherited identity plus this run's
conclusions read back from the generated tables: how many qualified comparison facts
the company has, how its gaps ended, whether it was researched at all, and the
capital events found. A company that was not researched keeps empty conclusion cells
and an explicit not-researched status rather than inheriting anyone else's numbers.
"""
from __future__ import annotations

import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import RUN, STRICT_COMPARABLE_TIME, WORK, load_companies, read_csv, stable, write_csv  # noqa: E402

PROFILE_FIELDS = [
    "company_id", "company_name", "country", "n_ads_inherited", "observation_date",
    "observation_dates_t1", "entity_scope_inherited", "hiring_scope_inherited",
    "researched_this_run", "research_subject", "subject_entity", "fact_rows",
    "qualified_comparison_facts", "background_only_facts", "unknown_or_not_applicable_facts",
    "gap_rows", "gaps_open_at_end", "gaps_found", "gaps_not_found_not_definite",
    "gaps_not_yet_searched", "capital_events", "latest_financing_disclosed",
    "latest_financing_at_observation", "own_listing_status", "ma_events",
    "strongest_value_status", "note",
]

ESTABLISHED = {"SUPPORTED_EXTERNAL", "COMPANY_SELF_REPORT", "MEDIA_STATEMENT",
               "COUNTERPARTY_CONFIRMATION", "CONFLICT_RESOLVED_BY_SEPARATION", "MIXED_SEE_EVIDENCE"}
STRENGTH_ORDER = ["COUNTERPARTY_CONFIRMATION", "SUPPORTED_EXTERNAL", "MEDIA_STATEMENT",
                  "MIXED_SEE_EVIDENCE", "CONFLICT_RESOLVED_BY_SEPARATION", "COMPANY_SELF_REPORT",
                  "PARENT_CONTEXT_ONLY", "INHERITED_UNVERIFIED", "NOT_YET_SEARCHED",
                  "SEARCHED_NOT_FOUND", "ACCESS_BLOCKED", "NOT_APPLICABLE"]


def main() -> int:
    companies = load_companies()
    facts = read_csv(os.path.join(RUN, "company_facts.csv"))
    gaps = read_csv(os.path.join(RUN, "company_gaps.csv"))
    caps = read_csv(os.path.join(RUN, "capital_events.csv"))

    by_fact = defaultdict(list)
    for f in facts:
        by_fact[f["company_id"]].append(f)
    by_gap = defaultdict(list)
    for g in gaps:
        by_gap[g["company_id"]].append(g)
    by_cap = defaultdict(list)
    for c in caps:
        by_cap[c["company_id"]].append(c)

    rows = []
    for c in companies:
        cid = c["company_id"]
        fs = by_fact.get(cid, [])
        gs = by_gap.get(cid, [])
        cs = by_cap.get(cid, [])
        qualified = [f for f in fs if f["value_status"] in ESTABLISHED
                     and f["time_applicability"] in STRICT_COMPARABLE_TIME]
        background = [f for f in fs if f["value_status"] in ESTABLISHED
                      and f["time_applicability"] not in STRICT_COMPARABLE_TIME]
        unknown = [f for f in fs if f["value_status"] not in ESTABLISHED]
        strengths = [s for s in STRENGTH_ORDER if any(f["value_status"] == s for f in fs)]
        def field(name: str) -> str:
            hits = [f for f in fs if f["field"] == name or f["merge_parent_field"] == name]
            return " | ".join(f["value"] for f in hits if f["value"])
        research_subject = next((f["subject_scope"] for f in fs if f["field"] == "research_subject"), "")
        subject_entity = next((f["subject_entity"] for f in fs if f["field"] == "research_subject"), "")
        rows.append({
            "company_id": cid,
            "company_name": c["company_name"],
            "country": c["country"],
            "n_ads_inherited": c["n_ads"],
            "observation_date": max([f["observation_date"] for f in fs], default=""),
            "observation_dates_t1": c["observation_dates_t1"],
            "entity_scope_inherited": c["entity_scope_inherited"],
            "hiring_scope_inherited": c["hiring_scope_inherited"],
            "researched_this_run": "YES" if fs else "NO",
            "research_subject": research_subject,
            "subject_entity": subject_entity,
            "fact_rows": len(fs),
            "qualified_comparison_facts": len(qualified),
            "background_only_facts": len(background),
            "unknown_or_not_applicable_facts": len(unknown),
            "gap_rows": len(gs),
            "gaps_open_at_end": sum(1 for g in gs if g["open_at_stage_b_end"] == "YES"),
            "gaps_found": sum(1 for g in gs if g["stage_b_status"] == "RESOLVED_FOUND"),
            "gaps_not_found_not_definite": sum(1 for g in gs if g["stage_b_status"] == "NOT_FOUND_NOT_DEFINITE"),
            "gaps_not_yet_searched": sum(1 for g in gs
                                         if g["stage_b_status"] in ("NOT_YET_MAPPED_THIS_RUN", "NOT_YET_SEARCHED")),
            "capital_events": len(cs),
            "latest_financing_disclosed": field("latest_financing_disclosed"),
            "latest_financing_at_observation": field("latest_financing_at_observation"),
            "own_listing_status": field("own_listing_status"),
            "ma_events": field("ma_events"),
            "strongest_value_status": strengths[0] if strengths else "",
            "note": ("本轮已有公司记录" if fs else "本轮无事实行：缺口保留待查，不参与比较，也不代填结论"),
        })

    write_csv(os.path.join(RUN, "company_profile.csv"), PROFILE_FIELDS,
              stable(rows, ["company_id"]))
    print({
        "rows": len(rows),
        "researched": sum(1 for r in rows if r["researched_this_run"] == "YES"),
        "unsearched": sum(1 for r in rows if r["researched_this_run"] == "NO"),
        "qualified_total": sum(r["qualified_comparison_facts"] for r in rows),
    })
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
