"""Compact briefing: duties + candidates for a software packet summary."""
from common import locate
from pathlib import Path
import json, re, sys
ROOT = Path(__file__).resolve().parent.parent
sum_path = ROOT / "notes" / sys.argv[1]
pkt_name = "Q_packet_04_" + sys.argv[1].replace("Q_sum_04_", "")
pkt = {ad["reading_id"]: ad for ad in json.loads((ROOT / "notes" / pkt_name).read_text(encoding="utf-8"))}
data = json.loads(sum_path.read_text(encoding="utf-8"))
lines = []
for rec in data:
    ad = pkt[rec["rid"]]
    k = ad["identity_key"]
    d = ad["fields"].get("duties") or ad["fields"].get("full_description") or ""
    parts = [p.strip() for p in re.split(r"[\n]+", d) if len(p.strip()) >= 12]
    duty = ""
    for p in parts[:8]:
        loc = locate(k, {"quote": p[:200]})
        if loc["method"] != "UNRESOLVED_LOCATION":
            duty = p[:200]
            break
    empt = ",".join(f"{x['id']}:{x['code']}:{x['quote']}" for x in rec["empty"])
    lines.append(f"#{rec['order']} {rec['rid']} | {rec['title']} | nI={rec['n_inherited']} empty={empt or '-'}")
    lines.append("DUTY " + duty)
    for c in rec["cands"]:
        codes = ",".join(c["codes"]) or "-"
        lines.append(f"  {c['id']}|{codes}|{(c.get('surface') or '')[:50]}|{c['quote'][:90]}")
    lines.append("")
out = ROOT / "notes" / (sum_path.stem.replace("Q_sum", "Q_brief") + ".txt")
out.write_text("\n".join(lines), encoding="utf-8")
print("wrote", out.name, "ads", len(data), "chars", out.stat().st_size)
