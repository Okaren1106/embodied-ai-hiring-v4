"""Stage B repair r2 / search-log reconcile.

The previous step invented SEARCH rows from final SEARCHED_NOT_FOUND statuses.
This version never writes a SEARCH. It only labels historical derived rows so
they cannot be mistaken for original queries.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import RUN, WORK  # noqa: E402

LOG = os.path.join(RUN, "search_log.jsonl")
DERIVED_NOTE = "扩展批次：本轮为该命题实际查证"


def main() -> int:
    entries = [json.loads(l) for l in open(LOG, encoding="utf-8") if l.strip()] if os.path.exists(LOG) else []
    relabeled = 0
    out = []
    for e in entries:
        note = e.get("note") or ""
        if e.get("action") == "SEARCH" and (
                e.get("tool") == "stage_b_repair_extension" or DERIVED_NOTE in note):
            if e.get("record_kind") != "DERIVED_STATUS_SUMMARY":
                e = dict(e)
                e["record_kind"] = "DERIVED_STATUS_SUMMARY"
                e["derived_from"] = "final_SEARCHED_NOT_FOUND_status"
                e["note"] = (note + " 【本行由程序根据最终状态补写，不是原始查询；保留原时间戳，不作更早时间伪装】").strip()
                relabeled += 1
        out.append(e)
    with open(LOG, "w", encoding="utf-8", newline="\n") as fh:
        for e in out:
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")
    summary = {
        "n_log_entries": len(out),
        "n_searches_added": 0,
        "n_derived_relabeled": relabeled,
        "note": "不再根据 SEARCHED_NOT_FOUND 补写 SEARCH；历史派生行已标明 DERIVED_STATUS_SUMMARY。",
    }
    with open(os.path.join(WORK, "search_log_reconcile.json"), "w", encoding="utf-8") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=2)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
