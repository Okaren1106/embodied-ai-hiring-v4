"""Pull unique duty-body quotes for software ads whose first line is a header."""
from common import locate
from pathlib import Path
import json, re
ROOT = Path(__file__).resolve().parent.parent
packets = []
for name in ["Q_packet_04_017_024.json", "Q_packet_04_025_032.json"]:
    packets += json.loads((ROOT / "notes" / name).read_text(encoding="utf-8"))
need = {"N0434","N0431","N0418","N0405","N0393","N0390","N0504","N0452","N0483","N0461","N0473","E0008","N0311","E0098","E0485","N0511"}
lines = []
for ad in packets:
    if ad["reading_id"] not in need:
        continue
    k = ad["identity_key"]
    d = ad["fields"].get("duties") or ""
    lines.append("==== " + ad["reading_id"] + " " + ad["title"])
    # split by newlines and numbered items
    parts = re.split(r"[\n]+", d)
    shown = 0
    for p in parts:
        p = p.strip()
        if len(p) < 12:
            continue
        loc = locate(k, {"quote": p[:180]})
        lines.append(loc["method"] + " | " + p[:180])
        shown += 1
        if shown >= 6:
            break
    lines.append("")
(ROOT / "notes" / "sw_17_32_body.txt").write_text("\n".join(lines), encoding="utf-8")
print("ok")
