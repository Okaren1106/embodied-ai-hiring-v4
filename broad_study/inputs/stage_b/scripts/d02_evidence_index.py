"""Repair pass / diagnostic 2: dump the evidence index and every fact->evidence
reference from the submitted package, so each relation can be reviewed and then
declared explicitly in work/relation_policy.json.

Read-only. Output: work/diag_evidence.json
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import RUN, SUBMITTED, WORK, read_csv, write_json  # noqa: E402


def main() -> int:
    evid = read_csv(os.path.join(SUBMITTED, "company_evidence.csv"))
    facts = read_csv(os.path.join(SUBMITTED, "company_facts.csv"))
    links = read_csv(os.path.join(SUBMITTED, "evidence_links.csv"))

    refs = defaultdict(list)
    for f in facts:
        for e in (f["evidence_ids"] or "").split("|"):
            if e:
                refs[e].append({"fact_id": f["fact_id"], "field": f["field"],
                                "value_status": f["value_status"],
                                "time_applicability": f["time_applicability"],
                                "value_head": (f["value"] or "")[:60]})

    evidence = []
    for e in evid:
        evidence.append({
            "evidence_id": e["evidence_id"],
            "company_id": e["company_id"],
            "field": e["field"],
            "claim_nature": e["claim_nature"],
            "source_nature": e["source_nature"],
            "access_status": e["access_status"],
            "relation_to_inherited": e.get("relation_to_inherited", ""),
            "publication_date": e["publication_date"],
            "event_date": e["event_date"],
            "url": e["url"],
            "snapshot_id": e["snapshot_id"],
            "snapshot_text_path": e["snapshot_text_path"],
            "linked_inherited_evidence": e.get("linked_inherited_evidence", ""),
            "note_head": (e.get("note", "") or "")[:120],
            "referenced_by": refs.get(e["evidence_id"], []),
        })

    link_pairs = [{"link_id": l["link_id"], "fact_id": l["fact_id"], "evidence_id": l["evidence_id"],
                   "relation": l["relation"]} for l in links]

    write_json(os.path.join(WORK, "diag_evidence.json"), {
        "n_evidence": len(evidence), "evidence": evidence, "n_links": len(link_pairs),
        "links": link_pairs,
    })

    print(json.dumps({
        "n_evidence": len(evidence),
        "context_like": [e["evidence_id"] for e in evidence
                         if e["relation_to_inherited"] in ("PARENT_CONTEXT_ONLY", "ACCESS_NOTE")
                         or e["access_status"] != "OK"
                         or e["claim_nature"] in ("ACCESS_NOTE", "SEARCH_RECORD")],
        "by_claim_nature": {k: sum(1 for e in evidence if e["claim_nature"] == k)
                            for k in sorted({e["claim_nature"] for e in evidence})},
        "unreferenced": [e["evidence_id"] for e in evidence if not e["referenced_by"]],
        "multi_fact_evidence": {e["evidence_id"]: [r["fact_id"] for r in e["referenced_by"]]
                                for e in evidence if len(e["referenced_by"]) > 1},
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
