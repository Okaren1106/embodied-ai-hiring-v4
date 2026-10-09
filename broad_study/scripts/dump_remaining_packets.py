"""Dump remaining-role first-pass packets in 16-ad chunks. Display aid only."""
from common import *
from collections import defaultdict
frame=read(ROOT/'tables/Q3_coding_frame.csv')
qq=json.loads((ROOT/'notes/Q_semantic_review_queue.json').read_text(encoding='utf-8'))
old=json.loads((ROOT/'notes/Q_inherited_semantics_all17.json').read_text(encoding='utf-8'))
cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
CD={r['code']:r for r in cat['labels']}
byq=defaultdict(list);byo=defaultdict(list)
for r in qq:byq[r['identity_key']].append(r)
for r in old:byo[r['identity_key']].append(r)
done=set()
for p in (ROOT/'configs/Q_adjudications').glob('*.json'):
 d=json.loads(p.read_text(encoding='utf-8'))
 done.update(a.get('identity_key',k) for k,a in d.get('ads',{}).items())
roles=defaultdict(list)
for r in frame:
 roles[int(r['role_order'])].append(r)
written=0
for fidx in range(5,18):
 recs=sorted(roles[fidx], key=lambda r:int(r['coding_order']))
 n=len(recs)
 for lo in range(1,n+1,16):
  hi=min(lo+15,n)
  sel=[r for r in recs if lo<=int(r['coding_order'])<=hi]
  out=[]
  for r in sel:
   k=r['identity_key'];j=J[k];rid=j['reading_id']
   item=dict(coding_order=int(r['coding_order']),reading_id=rid,company_id=j['company_id'],title=j['title'],identity_key=k,already_coded=k in done,fields={f:(RAW[k].get(f) or '') for f in ['duties','requirements','full_description']},inherited=[],candidates=[])
   for n_i,v in enumerate(byo[k],1):
    item['inherited'].append(dict(id=f'O{n_i}',code=v['code'],name=CD.get(v['code'],{}).get('name',''),suggested_metric=v['suggested_metric'],suggested_branch=v['suggested_branch'],prior_relation=v['prior_relation'],field=v['field'],start=v['start'],end=v['end'],quote=v['quote'],method=v.get('method','')))
   for v in byq[k]:
    ni=v['review_id'].split(':')[-1]
    item['candidates'].append(dict(id=ni,review_id=v['review_id'],codes=v['candidate_codes'],names=[CD.get(c,{}).get('name','') for c in v['candidate_codes']],surface=v['surface'],quote=v['quote'],field=v['field'],start=v['start'],end=v['end']))
   out.append(item)
  name=f'notes/Q_packet_{fidx:02d}_{lo:03d}_{hi:03d}.json'
  save_json(name,out)
  written+=1
  print(name, 'ads', len(out), 'already', sum(x['already_coded'] for x in out), 'cands', sum(len(x['candidates']) for x in out))
print('packets', written)
