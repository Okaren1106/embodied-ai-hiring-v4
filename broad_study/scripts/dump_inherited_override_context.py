"""Dump suggested override quotes for unresolved inherited items."""
import json, sys
from pathlib import Path
notes = Path(__file__).resolve().parents[1] / 'notes'
prefix = sys.argv[1]
dest = notes / sys.argv[2]
out = []
for p in sorted(notes.glob(prefix + '*.json')):
    data = json.loads(p.read_text(encoding='utf-8'))
    for ad in data:
        bad = [inh for inh in (ad.get('inherited') or []) if (inh.get('method')=='UNRESOLVED_LOCATION' or not (inh.get('quote') or '') or inh.get('start') in ('', None, 'None'))]
        if not bad:
            continue
        req = ((ad.get('fields') or {}).get('requirements') or '').replace('\n', ' ')
        duty = ((ad.get('fields') or {}).get('duties') or '').replace('\n', ' ')
        out.append('==== %s %s TITLE %s' % (ad.get('coding_order'), ad['reading_id'], ad.get('title')))
        for inh in bad:
            q = inh.get('quote') or ''
            out.append('O%s %s | %s | %s | %s' % (inh.get('id','?').lstrip('O') if str(inh.get('id','')).startswith('O') else inh.get('id'), inh.get('code'), inh.get('suggested_metric'), inh.get('suggested_branch'), q))
        out.append('DUTY ' + duty[:400])
        out.append('REQ ' + req[:500])
        out.append('')
dest.write_text('\n'.join(out), encoding='utf-8')
print('wrote', dest.name, 'chars', dest.stat().st_size)
