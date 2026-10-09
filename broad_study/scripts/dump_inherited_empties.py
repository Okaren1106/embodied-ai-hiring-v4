"""Dump inherited items with empty/unresolved location."""
import json, sys
from pathlib import Path
notes = Path(__file__).resolve().parents[1] / 'notes'
prefix = sys.argv[1]
dest = notes / sys.argv[2]
out = []
n = 0
for p in sorted(notes.glob(prefix + '*.json')):
    data = json.loads(p.read_text(encoding='utf-8'))
    for ad in data:
        bad = []
        for i, inh in enumerate(ad.get('inherited') or [], 1):
            q = inh.get('quote') or ''
            method = inh.get('method') or ''
            start = inh.get('start')
            if not q or method == 'UNRESOLVED_LOCATION' or start in ('', None, 'None'):
                bad.append('O%s %s | %s | %s | %s' % (
                    i, inh.get('code'), method, (q or '')[:80], inh.get('suggested_metric')))
        if bad:
            n += 1
            out.append('==== %s %s nI=%s' % (ad.get('coding_order'), ad['reading_id'], len(ad.get('inherited') or [])))
            out.append('TITLE ' + (ad.get('title') or ''))
            for b in bad:
                out.append(b)
            out.append('')
dest.write_text('\n'.join(out), encoding='utf-8')
print('wrote', dest.name, 'ads_with_empty', n, 'lines', len(out))
