"""Dump E0419 inherited safety quote and N0216 cand 1."""
import json
from pathlib import Path
notes = Path(__file__).resolve().parents[1] / 'notes'
out = []
for p in sorted(notes.glob('Q_packet_10*.json')):
    for ad in json.loads(p.read_text(encoding='utf-8')):
        if ad['reading_id'] not in {'E0419','N0216'}:
            continue
        out.append('==== %s %s' % (ad['coding_order'], ad['reading_id']))
        fields = ad.get('fields') or {}
        duty = fields.get('duties') or ''
        full = fields.get('full_description') or ''
        out.append('DUTY_LEN %s FULL_LEN %s' % (len(duty), len(full)))
        for inh in ad.get('inherited') or []:
            out.append('INH %s %s | %s | %s | %r' % (inh.get('id'), inh.get('code'), inh.get('method'), inh.get('suggested_metric'), inh.get('quote')))
        for c in ad.get('candidates') or []:
            out.append('C%s %s | %r' % (c['id'], ','.join(c.get('codes') or []) or '-', (c.get('quote') or '')[:400]))
        # safety snippet
        blob = duty + '\n' + full
        i = blob.lower().find('safety')
        out.append('SAFETY_CTX ' + repr(blob[max(0,i-80):i+120]))
        out.append('')
(notes/'in_probe.txt').write_text('\n'.join(out), encoding='utf-8')
print('wrote', len(out))
