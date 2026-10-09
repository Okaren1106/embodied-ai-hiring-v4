"""Stage B repair r2 / search log: per-question real trail, not company-level SEARCH."""
from __future__ import annotations

import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import RUN, WORK, read_csv, write_json  # noqa: E402

LOG = os.path.join(RUN, "search_log.jsonl")


def derived(e: dict) -> bool:
    note = e.get("note") or ""
    return (e.get("record_kind") == "DERIVED_STATUS_SUMMARY"
            or "扩展批次：本轮为该命题实际查证" in note)


def main() -> int:
    entries = [json.loads(line) for line in open(LOG, encoding="utf-8") if line.strip()] if os.path.exists(LOG) else []
    real_search = [e for e in entries if e.get("action") == "SEARCH" and not derived(e)]
    derived_search = [e for e in entries if e.get("action") == "SEARCH" and derived(e)]
    fetches = [e for e in entries if e.get("action") == "FETCH"]
    reviews = [e for e in entries if e.get("action") == "PAGE_REVIEW"]
    by_action = Counter(e.get("action", "") for e in entries)
    fetch_failures = [e for e in fetches if e.get("access_status") not in ("OK", "OK_ARCHIVED", None, "")]
    real_trail = real_search + reviews + fetches

    facts = read_csv(os.path.join(RUN, "company_facts.csv"))
    not_found = [f for f in facts if f["value_status"] == "SEARCHED_NOT_FOUND"]
    blocked = [f for f in facts if f["value_status"] == "ACCESS_BLOCKED"]

    missing_search = []
    for f in not_found:
        field = f["field"]
        hits = [e for e in real_trail
                if e.get("company_id") == f["company_id"]
                and field in ((e.get("question") or "") + " " + (e.get("query") or "")
                              + " " + (e.get("field") or ""))]
        if not hits:
            missing_search.append({"fact_id": f["fact_id"], "field": field,
                                   "company_id": f["company_id"]})

    missing_fetch = []
    for f in blocked:
        hits = [e for e in fetches if e.get("company_id") == f["company_id"]
                and e.get("access_status") not in ("OK", "OK_ARCHIVED")]
        if not hits:
            missing_fetch.append(f["fact_id"])

    summary = {
        "n_log_entries": len(entries),
        "by_action": dict(by_action),
        "n_real_search": len(real_search),
        "n_derived_search": len(derived_search),
        "n_fetches": len(fetches),
        "n_page_reviews": len(reviews),
        "n_fetch_failures": len(fetch_failures),
        "missing_per_question_trail": missing_search,
        "blocked_without_fetch_failure": missing_fetch,
        "queries": [{"ts_utc": e.get("ts_utc", ""), "company_id": e.get("company_id", ""),
                     "tool": e.get("tool", ""), "query": e.get("query", ""),
                     "result": e.get("result", ""), "record_kind": e.get("record_kind", "")}
                    for e in real_search],
        "derived_not_counted_as_search": len(derived_search),
    }
    write_json(os.path.join(WORK, "search_log_summary.json"), summary)
    ok = not missing_search and not missing_fetch
    print(json.dumps({
        "n_real_search": summary["n_real_search"],
        "n_derived_search": summary["n_derived_search"],
        "n_fetches": summary["n_fetches"],
        "n_page_reviews": summary["n_page_reviews"],
        "missing_per_question": len(missing_search),
        "blocked_without_fetch": len(missing_fetch),
    }, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
