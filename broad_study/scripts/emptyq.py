"""Unique quotes for empty inherited in software packets."""
from common import locate
from pathlib import Path
import json, re, sys
ROOT = Path(__file__).resolve().parent.parent
pkt = json.loads((ROOT / "notes" / sys.argv[1]).read_text(encoding="utf-8"))
lines = []
for ad in pkt:
    empt = [x for x in ad["inherited"] if not x.get("field")]
    if not empt:
        continue
    k = ad["identity_key"]
    txt = "\n".join(ad["fields"].get(f) or "" for f in ["duties", "requirements", "full_description"])
    lines.append("==== " + ad["reading_id"])
    for x in empt:
        q = x["quote"]
        hits = [m.start() for m in re.finditer(re.escape(q), txt)]
        lines.append(f" {x['id']} {x['code']} {q!r} hits={len(hits)} m={x.get('suggested_metric')} b={x.get('suggested_branch')} rel={x.get('prior_relation')}")
        for m in re.finditer(re.escape(q), txt):
            i = m.start()
            snip = txt[max(0, i - 30): i + len(q) + 50].replace("\n", " | ")
            loc = locate(k, {"quote": snip.strip()[:120]})
            lines.append("   " + loc["method"] + " | " + snip)
            # try sentence
            sent = re.split(r"[。；;\n]", txt[max(0, i - 80): i + len(q) + 80])
            break
        # find a unique containing sentence in duties/requirements
        for f in ["duties", "requirements", "full_description"]:
            t = ad["fields"].get(f) or ""
            if q not in t:
                continue
            for sent in re.split(r"[\n]", t):
                if q in sent and 20 < len(sent) < 220:
                    loc = locate(k, {"quote": sent.strip()})
                    if loc["method"] != "UNRESOLVED_LOCATION":
                        lines.append("   USE " + f + " " + loc["method"] + " | " + sent.strip()[:200])
                        break
(ROOT / "notes" / (sys.argv[1].replace("Q_packet", "Q_emptyq").replace(".json", ".txt"))).write_text("\n".join(lines), encoding="utf-8")
print("wrote", len(lines))
