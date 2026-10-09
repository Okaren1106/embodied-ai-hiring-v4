"""Count E0419 safety quote occurrences."""
import json
from pathlib import Path
notes = Path(__file__).resolve().parents[1] / 'notes'
needle = 'tackling the complex challenges like safety, commercialization, and mass production'
for p in sorted(notes.glob('Q_packet_10*.json')):
    for ad in json.loads(p.read_text(encoding='utf-8')):
        if ad['reading_id']!='E0419':
            continue
        fields = ad.get('fields') or {}
        for name in ['duties','requirements','full_description']:
            t = fields.get(name) or ''
            print(name, 'len', len(t), 'n', t.count(needle))
            i = t.find('safety')
            print(' first safety', repr(t[max(0,i-60):i+90]))
