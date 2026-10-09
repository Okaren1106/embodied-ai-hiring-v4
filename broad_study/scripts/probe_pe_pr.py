import json,csv
from pathlib import Path
from collections import Counter,defaultdict
root=Path(__file__).resolve().parents[1]
out=[]
ads=json.loads((root/'configs/Q_adjudications/RF_PERCEPTION.json').read_text(encoding='utf-8'))['ads']
frame=list(csv.DictReader((root/'tables/Q3_coding_frame.csv').open(encoding='utf-8-sig')))
out.append('frame_cols='+','.join(frame[0].keys()))
# guess role column
role_col=[c for c in frame[0] if 'role' in c.lower() or 'primary' in c.lower() or 'class' in c.lower()]
out.append('roleish='+','.join(role_col))
pe=[r for r in frame if 'RF_PERCEPTION' in r.values()]
out.append('pe_n='+str(len(pe)))
out.append('adj_n='+str(len(ads)))
# reading_id col
rid_col='reading_id' if 'reading_id' in frame[0] else None
if rid_col:
    missing=[r[rid_col] for r in pe if r[rid_col] not in ads and r.get('identity_key') not in ads]
    out.append('missing='+','.join(missing))
# catalog for product
cat=json.loads((root/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
role='RF_PRODUCT_PROGRAM'
inc=[x['code']+'\t'+x['name'] for x in cat['labels'] if role in x.get('applicable_roles',[])]
out.append('PRODUCT_IN '+str(len(inc)))
out.extend(inc)
Path('../notes/probe_pe_pr.txt').write_text('\n'.join(out),encoding='utf-8')
print('pe',len(pe),'adj',len(ads),'prod_in',len(inc),'missing',missing if rid_col else 'na')
