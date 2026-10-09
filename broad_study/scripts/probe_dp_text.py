"""Dump duties/requirements snippets for selected deployment ads."""
import json
from pathlib import Path
notes = Path(__file__).resolve().parents[1] / 'notes'
want = {'E0570','E0569','E0598','E0557','N0857','N0756','N1029','E0105','N0778','E0471'}
found = {}
for p in sorted(notes.glob('Q_packet_09*.json')):
    for ad in json.loads(p.read_text(encoding='utf-8')):
        rid = ad['reading_id']
        if rid not in want:
            continue
        fields = ad.get('fields') or {}
        found[rid] = {
            'order': ad.get('coding_order'),
            'title': ad.get('title'),
            'duties': fields.get('duties') or '',
            'requirements': fields.get('requirements') or '',
            'full': fields.get('full_description') or '',
            'nI': len(ad.get('inherited') or []),
            'inherited': [(x.get('id'), x.get('code'), x.get('quote'), x.get('method'), x.get('field')) for x in (ad.get('inherited') or [])]
        }
dest = notes / 'dp_probe.txt'
parts = []
for rid in sorted(found):
    a = found[rid]
    parts.append('==== %s order=%s TITLE %s' % (rid, a['order'], a['title']))
    parts.append('DUTY<<<')
    parts.append(a['duties'])
    parts.append('>>>REQ<<<')
    parts.append(a['requirements'])
    parts.append('>>>INH')
    for row in a['inherited']:
        parts.append(str(row))
    parts.append('')
dest.write_text('\n'.join(parts), encoding='utf-8')
print('wrote', dest, 'n', len(found))
