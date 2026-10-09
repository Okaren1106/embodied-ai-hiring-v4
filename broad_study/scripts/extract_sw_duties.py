"""Extract first-duty locate checks for software packets."""
from common import locate
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parent.parent
packets = []
for name in ["Q_packet_04_017_024.json", "Q_packet_04_025_032.json"]:
    packets += json.loads((ROOT / "notes" / name).read_text(encoding="utf-8"))
lines = []
for ad in packets:
    k = ad["identity_key"]
    d = ad["fields"].get("duties") or ad["fields"].get("full_description") or ""
    first = d.strip().split("\n")[0][:220]
    loc = locate(k, {"quote": first})
    lines.append(f"{ad['coding_order']} {ad['reading_id']} {ad['title']} nI={len(ad['inherited'])} nC={len(ad['candidates'])} loc={loc['method']}")
    lines.append("  " + first)
    lines.append("")
(ROOT / "notes" / "sw_17_32_duties.txt").write_text("\n".join(lines), encoding="utf-8")
print("ads", len(packets))
