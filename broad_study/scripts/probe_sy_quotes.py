"""Dump unique duty snippets and inherited codes for systems ads."""
import json
from pathlib import Path
from common import RAW, jobs, locate
root = Path(__file__).resolve().parents[1]
frame = []
import csv
with (root/'tables/Q3_coding_frame.csv').open(encoding='utf-8-sig') as f:
    r = csv.DictReader(f)
    frame = [x for x in r if x['role']=='RF_SYSTEMS_ENGINEERING_INTEGRATION']
old = json.loads((root/'notes/Q_inherited_semantics_all17.json').read_text(encoding='utf-8'))
obk = {}
for rec in old:
    obk.setdefault(rec['identity_key'], []).append(rec)
out = []
for i, j in enumerate(sorted(frame, key=lambda x: int(x['coding_order'])), 1):
    k = j['identity_key']; rid = j['reading_id']
    raw = RAW[k]
    duty = raw.get('duties') or ''
    req = raw.get('requirements') or ''
    inh = obk.get(k) or []
    codes = [f"{r.get('code')}|{r.get('quote','')[:40]}" for r in inh]
    # pick a unique 20-40 char ascii/cjk snippet from duties
    snippet = ''
    for n in range(24, 80):
        cand = duty[:n].strip()
        if not cand:
            break
        loc = locate(k, dict(quote=cand))
        if loc['method'] != 'UNRESOLVED_LOCATION' and loc.get('field')=='duties':
            snippet = cand
            break
    out.append(f"==== {i} {rid} TITLE {j.get('title')}")
    out.append('EVID_TRY ' + snippet.replace('\n',' / '))
    out.append('DUTY0 ' + duty[:180].replace('\n',' / '))
    out.append('INH ' + ' ; '.join(codes[:25]))
    out.append('')
(root/'notes/sy_17_quote_probe.txt').write_text('\n'.join(out), encoding='utf-8')
print('wrote', len(out))
