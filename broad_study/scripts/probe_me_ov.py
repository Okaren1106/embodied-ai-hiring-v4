"""Dump unique override quotes for remaining mechanical empties."""
import json
from pathlib import Path
notes = Path(__file__).resolve().parents[1] / 'notes'
want = {
 'E0338':['Creo','CAD'],
 'E0361':['Creo','Windchill'],
 'E0432':['mechanical systems'],
 'E0049':['结构'],
 'E0250':['有限元'],
}
found={}
for p in sorted(notes.glob('Q_packet_11*.json')):
    for ad in json.loads(p.read_text(encoding='utf-8')):
        if ad['reading_id'] not in want: continue
        fields=ad.get('fields') or {}
        blob='\n'.join([fields.get('duties') or '', fields.get('requirements') or '', fields.get('full_description') or ''])
        found[ad['reading_id']]=blob
out=[]
for rid, needles in want.items():
    blob=found.get(rid,'')
    out.append('==== '+rid+' len='+str(len(blob)))
    for n in needles:
        c=blob.count(n)
        i=blob.find(n)
        out.append('%s count=%s ctx=%r'%(n,c, blob[max(0,i-70):i+len(n)+80] if i>=0 else ''))
    out.append('')
(notes/'me_ov_probe.txt').write_text('\n'.join(out), encoding='utf-8')
print('wrote')
