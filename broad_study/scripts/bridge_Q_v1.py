"""Recompute immutable v1 Q2 cells directly from locked tags and requirement trees."""
from common import *
import math
lock_check()
rule=json.loads((C/'inputs/rules_v1/decisions/q2_rules.json').read_text(encoding='utf-8'))
idx={};roots={}
for line in (A/'relations.jsonl').read_text(encoding='utf-8').splitlines():
 r=json.loads(line)
 if r['kind']=='requirement_group':
  for n in r['nodes']:idx[r['identity_key'],n['node_id']]=n;roots[r['identity_key'],n['node_id']]=r['root_relation']
def branch(r):
 if r['context']!='REQUIREMENT':return 'UNCONDITIONAL'
 node=r['requirement_node_id'];rels=set();seen=set()
 if not node:return 'UNRESOLVED'
 while node:
  key=(r['identity_key'],node)
  if key not in idx or node in seen:return 'UNRESOLVED'
  seen.add(node);rels.update([idx[key]['relation'],roots[key]]);node=idx[key]['parent_id']
 if 'UNRESOLVED' in rels:return 'UNRESOLVED'
 ch=bool(rels&{'OR','OR_EQUIVALENT','SOME_OF'});ex='EXAMPLE' in rels
 return 'CHOICE_AND_EXAMPLE' if ch and ex else 'CHOICE' if ch else 'EXAMPLE' if ex else 'UNCONDITIONAL'
items=defaultdict(list);sem=[]
for r in read(A/'skills.csv')+read(A/'technical_concepts.csv'):
 j=J[r['identity_key']]
 if role(j) not in rule['primary_roles']:continue
 bb=branch(r);metric='SEPARATE_NOT_POSITIVE'
 for m,pair in rule['positive_buckets'].items():
  if [r['use'],r['mention_relation']]==pair and r['context']==('DUTY' if m.startswith('DUTY_') else 'REQUIREMENT'):metric=m
 cand=metric
 if bb=='UNRESOLVED' or r['use'] in ['NEGATED','UNRESOLVED','BACKGROUND']:metric='SEPARATE_NOT_POSITIVE'
 rr=dict(r,branch_bucket=bb,metric_bucket=metric,candidate_metric=cand)
 items[r['identity_key'],r['dimension'],r['label_code']].append(rr);sem.append(rr)
oldsem=read(C/'tables/T3_all_item_semantics.csv')
key=lambda r:(r['identity_key'],r['dimension'],r['item_index'])
by={key(r):r for r in sem}
assert len(by)==len(sem)==len(oldsem)==5547
for r in oldsem:
 v=by[key(r)]
 for f in ['branch_bucket','metric_bucket','candidate_metric']:assert v[f]==r[f],(key(r),f,v[f],r[f])
def state(k,dim,label,m,b):
 rr=items[k,dim,label]
 if any(r['metric_bucket']==m and r['branch_bucket']==b for r in rr):return 'P'
 for r in rr:
  relevant=r['context'] in (['DUTY','UNCERTAIN'] if m.startswith('DUTY_') else ['REQUIREMENT','UNCERTAIN'])
  ambiguous=r['use']=='UNRESOLVED' or r['mention_relation']=='UNRESOLVED' or r['context']=='UNCERTAIN'
  if relevant and (ambiguous or (r['candidate_metric']==m and r['branch_bucket']=='UNRESOLVED')):return 'U'
 return 'Z'
cells=read(C/'tables/T3_company_context.csv');out=[];checks=[]
adgroups=defaultdict(list)
for k,j in J.items():
 if role(j) in rule['primary_roles']:adgroups[j['company_id'],role(j)].append(k)
for r in cells:
 dim=r['dimension'];sf='skills_status' if dim=='skills' else 'technical_status'
 base=[k for k in adgroups[r['company_id'],r['role_code']] if J[k][sf] in ['CODED','NOT_MENTIONED','UNMAPPED']]
 excluded=len(adgroups[r['company_id'],r['role_code']])-len(base)
 ss=Counter(state(k,dim,r['label_code'],r['metric_bucket'],r['branch_bucket']) for k in base)
 p,u,b=ss['P'],ss['U'],len(base);n=b-u
 for f,v in [('n_positive',p),('n_base',b),('n_relation_unknown',u),('n_interpretable',n),('n_source_unassessable',excluded)]:assert int(r[f])==v,(r,f,v)
 share=p/n if n else None
 assert (not r['share'] and share is None) or (share is not None and abs(float(r['share'])-share)<1e-6),(r,share)
 rr=dict(r,recomputed_P=p,recomputed_U=u,recomputed_B=b,recomputed_N=n,recomputed_share=share,check='MATCH')
 out.append(rr)
selected=read(C/'inputs/rules_v1/q2_display_selection.csv')
selected=[r for r in selected if r['main_display']=='YES']
expected={('RF_ML_AI_ENGINEERING','skills'):10,('RF_ML_AI_ENGINEERING','technical_concepts'):8,('RF_ROBOTICS_SOFTWARE','skills'):9,('RF_ROBOTICS_SOFTWARE','technical_concepts'):8}
assert Counter((r['role_code'],r['dimension']) for r in selected)==expected
dump('tables/Q_v1_bridge_company_cells.csv',out)
dump('tables/Q_v1_fixed_display_items.csv',selected)
save_json('verification/Q_v1_bridge.json',dict(status='PASS',item_semantics_checked=5547,company_context_cells_checked=len(out),fixed_display_items=35,fixed_display_counts=[dict(role=f,dimension=d,n=n) for (f,d),n in expected.items()],implementation='Astra separate recomputation from source tags and requirement ancestor trees; old published cells compared numerically. Not external independent reviewer.',input_files_checked=lock_check()))
print('v1 bridge PASS',len(out),'cells; 5547 item semantics; 35 fixed display items')

