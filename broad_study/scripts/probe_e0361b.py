"""Unique neighbors around E0361 Creo lines."""
import json
from pathlib import Path
notes=Path(__file__).resolve().parents[1]/'notes'
for p in sorted(notes.glob('Q_packet_11*.json')):
    for ad in json.loads(p.read_text(encoding='utf-8')):
        if ad['reading_id']!='E0361': continue
        t=(ad.get('fields') or {}).get('requirements') or ''
        start=0;n=0
        while True:
            i=t.find('Creo and Windchill experience', start)
            if i<0: break
            n+=1
            print('OCC',n, repr(t[max(0,i-120):i+80]))
            start=i+1
