"""Compact candidate dump. Usage: dump_role_cands.py Q_packet_05 cm_05_cands.txt"""
import json, sys
from pathlib import Path
notes = Path(__file__).resolve().parents[1] / 'notes'
prefix = sys.argv[1]
dest = notes / sys.argv[2]
paths = sorted(notes.glob(prefix + '*.json'))
out = []
for p in paths:
    data = json.loads(p.read_text(encoding='utf-8'))
    for ad in data:
        empt = [x['id'] + ':' + x['code'] + ':' + (x.get('quote') or '')[:40]
                for x in ad.get('inherited') or [] if not x.get('field')]
        out.append('==== %s %s nC=%s nI=%s empty=%s' % (
            ad['coding_order'], ad['reading_id'], len(ad['candidates']),
            len(ad.get('inherited') or []), empt))
        out.append('TITLE ' + ad['title'])
        duty = (ad.get('fields') or {}).get('duties') or ''
        out.append('DUTY ' + (duty.replace('\n', ' ')[:220]))
        for c in ad['candidates']:
            codes = ','.join(c.get('codes') or []) or '-'
            q = (c.get('quote') or '').replace('\n', ' ')[:150]
            out.append('%s %s | %s' % (c['id'], codes, q))
        out.append('')
dest.write_text('\n'.join(out), encoding='utf-8')
print('wrote', dest.name, 'packets', len(paths), 'ads',
      sum(1 for x in out if x.startswith('====')), 'lines', len(out))
