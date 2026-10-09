"""Compact first-pass packet for a coding-order range. Display aid, not an adjudication."""
from common import *
import sys
fidx,lo,hi=map(int,sys.argv[1:4])
frame=read(ROOT/'tables/Q3_coding_frame.csv')
sel=[r for r in frame if int(r['role_order'])==fidx and lo<=int(r['coding_order'])<=hi]
qq=json.loads((ROOT/'notes/Q_semantic_review_queue.json').read_text(encoding='utf-8'))
old=json.loads((ROOT/'notes/Q_inherited_semantics_all17.json').read_text(encoding='utf-8'))
cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
CD={r['code']:r for r in cat['labels']}
byq=defaultdict(list);byo=defaultdict(list)
for r in qq:byq[r['reading_id']].append(r)
for r in old:byo[r['reading_id']].append(r)
done=set()
for p in (ROOT/'configs/Q_adjudications').glob('*.json'):
 d=json.loads(p.read_text(encoding='utf-8'))
 done.update(d.get('ads',{}))
out=[]
for r in sel:
 k=r['identity_key'];j=J[k];rid=j['reading_id']
 item=dict(coding_order=int(r['coding_order']),reading_id=rid,company_id=j['company_id'],title=j['title'],identity_key=k,already_coded=rid in done,fields={f:(RAW[k].get(f) or '') for f in ['duties','requirements','full_description']},inherited=[],candidates=[])
 for n,v in enumerate(byo[rid],1):
  item['inherited'].append(dict(id=f'O{n}',code=v['code'],name=CD.get(v['code'],{}).get('name',''),suggested_metric=v['suggested_metric'],suggested_branch=v['suggested_branch'],prior_relation=v['prior_relation'],field=v['field'],start=v['start'],end=v['end'],quote=v['quote']))
 for v in byq[rid]:
  ni=v['review_id'].split(':')[1]
  item['candidates'].append(dict(id=ni,review_id=v['review_id'],codes=v['candidate_codes'],names=[CD.get(c,{}).get('name','') for c in v['candidate_codes']],surface=v['surface'],quote=v['quote'],field=v['field'],start=v['start'],end=v['end']))
 out.append(item)
name=f'Q_packet_{fidx:02d}_{lo:03d}_{hi:03d}.json'
save_json('notes/'+name,out)
print('wrote',name,'ads',len(out),'already_coded',sum(x['already_coded'] for x in out))
