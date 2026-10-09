import json,csv
from pathlib import Path
from collections import Counter
root=Path(__file__).resolve().parents[1]
ads=json.loads((root/'configs/Q_adjudications/RF_PERCEPTION.json').read_text(encoding='utf-8'))['ads']
frame=list(csv.DictReader((root/'tables/Q3_coding_frame.csv').open(encoding='utf-8-sig')))
pe=[r for r in frame if r['primary_code']=='RF_PERCEPTION']
# coding frame columns?
Path('../notes/probe_pe_done.txt').write_text('frame_cols='+','.join(frame[0].keys())+'\n'+ 'pe_n='+str(len(pe))+'\n adj_n='+str(len(ads))+'\n keys=\n'+'\n'.join(sorted(ads))+'\n',encoding='utf-8')
print('pe',len(pe),'adj',len(ads))
print('cols',list(frame[0].keys())[:20])
missing=[r.get('reading_id') for r in pe if r.get('reading_id') not in ads and r.get('identity_key') not in ads]
print('missing',missing)
