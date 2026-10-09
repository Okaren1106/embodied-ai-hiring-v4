"""Stage B repair / extension step: create the authored-layer skeleton for the
remaining companies.

The repair package covers three companies; the remaining twenty-one still carry every
inherited gap in the not-yet-searched state. Extending to them is a research task, and
this step gives each of those companies a ready-made authored file seeded from the
inherited profile and evidence ledger, with empty evidence / facts / relations /
capital arrays that research fills in one company at a time.

Nothing is invented here: the skeleton records only identity fields already present in
the sealed r3 package (name, research subject, hiring channel, observation date) and
copies the inherited evidence identifiers for traceability.
"""
from __future__ import annotations

import csv
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s00_common import R3, RUN, WORK, load_companies, read_csv, write_json  # noqa: E402

AUTHORED_DIR = os.path.join(WORK, "research")
PILOTS = ["CN_XSQUARE", "US_AMAZON_FTR", "CN_FOURIER"]


def main() -> int:
    companies = {c["company_id"]: c for c in load_companies()}
    profile = {r["company_id"]: r for r in read_csv(os.path.join(R3, "company_profile.csv"))}
    inherited_evidence = read_csv(os.path.join(R3, "company_evidence.csv"))
    t1 = {r["company_id"]: r for r in read_csv(os.path.join(R3, "T1_sample_company.csv"))}
    os.makedirs(AUTHORED_DIR, exist_ok=True)

    created, skipped, existing = [], [], []
    for cid in sorted(companies):
        if cid in PILOTS:
            continue
        target = os.path.join(AUTHORED_DIR, f"authored_{cid}.json")
        if os.path.exists(target):
            existing.append(cid)
            continue
        c = companies[cid]
        p = profile.get(cid, {})
        t = t1.get(cid, {})
        waves = sorted(k for k in c.get("waves_from_jobs", {}) if k)
        inherited_ids = sorted({e["evidence_id"] for e in inherited_evidence if e["company_id"] == cid})
        doc = {
            "company_id": cid,
            "observation_date": waves[-1] if waves else "",
            "observation_waves": waves,
            "research_subject": (p.get("company_name_cn") or p.get("company_name_en") or cid) +
                                f"（{p.get('entity_scope_inherited', 'WHOLE_COMPANY')}）",
            "entity_note": ("本文件由扩展步骤生成骨架，事实、证据、关系与资本事件由研究填入；"
                            "未填写的字段一律保持未查状态，不代填结论。"),
            "company_name_en": p.get("company_name_en", ""),
            "company_name_cn": p.get("company_name_cn", ""),
            "country": c.get("country", ""),
            "website": p.get("website", ""),
            "founded_year_inherited": p.get("founded_year", ""),
            "headquarters_inherited": p.get("headquarters", ""),
            "hiring_source_url": t.get("hiring_source_url", ""),
            "ats_provider": t.get("ats_provider", ""),
            "n_ads_inherited": c.get("n_ads"),
            "inherited_evidence_ids": inherited_ids,
            "evidence": [],
            "facts": [],
            "relations": [],
            "capital_events": [],
            "extra_notes": [
                "骨架文件：继承身份字段来自 r3 只读包，未做新的联网查证。",
                "研究时按主体/范围/事件拆分事实，并为每条引用的证据声明关系（SUPPORTS / CONTEXT_ONLY / "
                "ACCESS_NOTE / REPLACES / REFUTES）。",
            ],
        }
        write_json(target, doc)
        created.append(cid)

    print(json.dumps({
        "authored_dir": AUTHORED_DIR,
        "created": created,
        "already_present": existing,
        "skipped_pilots": PILOTS,
        "n_remaining_to_research": len(created),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
