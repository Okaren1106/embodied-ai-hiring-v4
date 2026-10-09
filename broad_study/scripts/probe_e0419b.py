"""Find unique E0419 safety contexts."""
import json
from pathlib import Path
notes = Path(__file__).resolve().parents[1] / 'notes'
needle = 'tackling the complex challenges like safety, commercialization, and mass production'
for p in sorted(notes.glob('Q_packet_10*.json')):
    for ad in json.loads(p.read_text(encoding='utf-8')):
        if ad['reading_id']!='E0419':
            continue
        t = (ad.get('fields') or {}).get('full_description') or ''
        start=0; n=0
        while True:
            i=t.find(needle, start)
            if i<0: break
            n+=1
            print('OCC', n, repr(t[max(0,i-120):i+len(needle)+80]))
            start=i+1
        # candidates
        for q in [
            'You will join a team dedicated to bringing Apollo to market at scale, tackling the complex challenges like safety',
            'dedicated to bringing Apollo to market at scale, tackling the complex challenges like safety, commercialization',
            'society\'s most important problems. You will join a team dedicated to bringing Apollo to market at scale',
        ]:
            print('TRY', t.count(q), q[:80])
