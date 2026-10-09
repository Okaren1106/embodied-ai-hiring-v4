from pathlib import Path
import json
p=json.loads(Path(r"D:/Embod AI analysis/embodied-ai-hiring-research/reports/2026-09-14_company_data_analysis/stage_d_integrated_v2/run_20260916_astra_v2/notes/Q_packet_04_097_112.json").read_text(encoding="utf-8"))
lines=[]
for ad in p:
    ids=[c["id"] for c in ad["candidates"]]
    empt=[x["id"] for x in ad["inherited"] if not x.get("field")]
    lines.append(f"{ad['coding_order']} {ad['reading_id']} nC={len(ad['candidates'])} ids={ids} empty={empt} already={ad['already_coded']} k={ad['identity_key'][-20:]}")
Path(r"D:/Embod AI analysis/embodied-ai-hiring-research/reports/2026-09-14_company_data_analysis/stage_d_integrated_v2/run_20260916_astra_v2/notes/sw_97_112_ids.txt").write_text("\n".join(lines),encoding="utf-8")
print("\n".join(lines))
