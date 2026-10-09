import json
from pathlib import Path
notes = Path(__file__).resolve().parents[1] / 'notes'
out = []
for name in ['Q_packet_04_145_160.json', 'Q_packet_04_161_176.json', 'Q_packet_04_177_181.json']:
    data = json.loads((notes / name).read_text(encoding='utf-8'))
    for ad in data:
        rid = ad['reading_id']
        duties = (ad.get('fields') or {}).get('duties') or ''
        first = duties.replace('\n', ' ')[:280]
        out.append('RID %s TITLE %s' % (rid, ad.get('title')))
        out.append('DUTY ' + first)
        for i, inh in enumerate(ad.get('inherited') or [], 1):
            q = inh.get('quote') or ''
            method = inh.get('method') or ''
            start = inh.get('start')
            if not q or method == 'UNRESOLVED_LOCATION' or start in ('', None, 'None'):
                out.append('EMPTY O%s %s | %s | %s' % (i, inh.get('code'), q[:100], inh.get('suggested_metric')))
            elif 'application security' in q.lower() or q in ('embedded', 'hardware test', 'real-time', 'SaaS Security', 'Enterprise'):
                out.append('SHORT O%s %s | %s | %s' % (i, inh.get('code'), q, inh.get('suggested_metric')))
        out.append('')
p = notes / 'sw_145_181_inherited_notes.txt'
p.write_text('\n'.join(out), encoding='utf-8')
print('wrote', p)
