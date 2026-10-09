"""Summarize remaining software packets 33-181."""
from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
# reuse summarize_Q_packet logic inline
ROOT = Path(__file__).resolve().parent.parent
notes = ROOT / "notes"
for p in sorted(notes.glob("Q_packet_04_*.json")):
    lohi = p.stem.replace("Q_packet_04_", "")
    out = notes / f"Q_sum_04_{lohi}.json"
    if out.exists():
        continue
    data = json.loads(p.read_text(encoding="utf-8"))
    recs = []
    for ad in data:
        empty = [x for x in ad["inherited"] if not x.get("field")]
        cands = [{"id": c["id"], "codes": c["codes"], "quote": c["quote"][:180], "surface": (c.get("surface") or "")[:80]} for c in ad["candidates"]]
        recs.append({"order": ad["coding_order"], "rid": ad["reading_id"], "title": ad["title"], "n_inherited": len(ad["inherited"]), "empty": [{"id": x["id"], "code": x["code"], "quote": x["quote"]} for x in empty], "cands": cands})
    out.write_text(json.dumps(recs, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", out.name, "ads", len(recs))
print("done")
