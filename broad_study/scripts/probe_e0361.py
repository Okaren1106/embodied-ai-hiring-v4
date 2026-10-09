"""All Creo/Windchill contexts in E0361."""
import json,re
from pathlib import Path
notes=Path(__file__).resolve().parents[1]/'notes'
for p in sorted(notes.glob('Q_packet_11*.json')):
    for ad in json.loads(p.read_text(encoding='utf-8')):
        if ad['reading_id']!='E0361': continue
        fields=ad.get('fields') or {}
        for name in ['duties','requirements','full_description']:
            t=fields.get(name) or ''
            print('FIELD',name,'len',len(t))
            for m in re.finditer(r'.{0,80}Creo.{0,80}', t):
                print(' C',repr(m.group()))
            for m in re.finditer(r'.{0,80}Windchill.{0,80}', t):
                print(' W',repr(m.group()))
