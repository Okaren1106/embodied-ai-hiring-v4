from common import *
from datetime import datetime,timezone
PREV=ROOT.parent/'run_20260916_astra_m5_m6_final'
GROK=ROOT.parent/'run_20260916_astra_v2'
fields=['role','label_code','metric','branch']
def loadagg(path):
 with path.open(encoding='utf-8-sig',newline='') as f:return {tuple(r[x] for x in fields):r for r in csv.DictReader(f) if r['scope']=='WHOLE23'}
old=loadagg(PREV/'tables/Q4_aggregates_final.csv');new=loadagg(ROOT/'tables/Q4_aggregates_final.csv');grok=loadagg(GROK/'tables/Q4_aggregates.csv')
out=[]
for key,n in new.items():
 o=old[key]
 if any(n[x]!=o[x] for x in ['P','U','Z','N','B','SOURCE_EXCLUDED','gate']):
  out.append(dict(zip(fields,key),label_name=n['label_name'],**{'v2_'+x:o[x] for x in ['P','U','Z','N','B','SOURCE_EXCLUDED','gate']},**{'v3_'+x:n[x] for x in ['P','U','Z','N','B','SOURCE_EXCLUDED','gate']},delta_P=int(n['P'])-int(o['P']),delta_U=int(n['U'])-int(o['U']),change_pp=(float(n['share_ad_weighted'])-float(o['share_ad_weighted']))*100 if n['share_ad_weighted'] and o['share_ad_weighted'] else ''))
dump('tables/V3_revision_impact_v2_to_v3.csv',out)
ch=read(ROOT/'tables/Q3_astra_changes.csv');baseline_n=len(read(ROOT/'baseline_v2/Q3_astra_changes.csv'));inc=ch[baseline_n:];axes=defaultdict(list)
for x in inc:
 try:b=json.loads(x['before']);a=json.loads(x['after'])
 except json.JSONDecodeError:axes['TASK'].append(x);continue
 if not b:axes['ADDITION'].append(x)
 else:
  for z in ['code','metric','branch','affected_metrics','excluded_from_catalog']:
   if b.get(z)!=a.get(z):axes[z].append(x)
  if any(b.get(z)!=a.get(z) for z in ['quote','field','start','end']):axes['LOCATION'].append(x)
dump('tables/V3_incremental_change_axes.csv',[dict(axis=a,operations=len(xs),ads=len({x['identity_key'] for x in xs}),note='各轴重叠，事务可重复修改同一证据，不能当错误率') for a,xs in axes.items()])
def evmap(p):return {(e['identity_key'],e['evidence_id']):e for e in read(p)}
be=evmap(ROOT/'baseline_v2/Q3_evidence_final.csv');ne=evmap(ROOT/'tables/Q3_evidence_final.csv');effective=[]
for key,e in ne.items():
 b=be.get(key,{})
 ff=[f for f in ['code','metric','branch','quote','field','start','end','affected_metrics','excluded_from_catalog'] if e.get(f,'')!=b.get(f,'')]
 if ff:effective.append(dict(identity_key=key[0],evidence_id=key[1],reading_id=e['reading_id'],change_type='ADDED' if not b else 'CHANGED',fields=js(ff)))
dump('tables/V3_effective_evidence_changes.csv',effective)
selected=[('RF_ML_AI_ENGINEERING','TC_ML_SYSTEMS','DUTY_OWN_DEVELOP','UNCONDITIONAL'),('RF_ML_AI_ENGINEERING','TC_FOUNDATION_MODEL','DUTY_OWN_DEVELOP','UNCONDITIONAL'),('RF_ML_AI_ENGINEERING','SK_PYTHON','GENERAL','UNCONDITIONAL'),('RF_ML_AI_ENGINEERING','SK_CPP','GENERAL','UNCONDITIONAL'),('RF_ROBOTICS_SOFTWARE','SK_LINUX','GENERAL','UNCONDITIONAL'),('RF_ROBOTICS_SOFTWARE','SK_CPP','GENERAL','UNCONDITIONAL'),('RF_CONTROL_PLANNING','TC_CONTROL','GENERAL','UNCONDITIONAL'),('RF_DEPLOYMENT_FIELD_SERVICE','SK_PYTHON','GENERAL','UNCONDITIONAL')]
cmap={}
for p in (ROOT/'inputs/stage_c/tables').glob('*q2*plot_data.csv'):
 for x in read(p):
  if x.get('group')=='WHOLE23' and all(z in x for z in ['role_code','label_code','metric_bucket','branch_bucket']):cmap[x['role_code'],x['label_code'],x['metric_bucket'],x['branch_bucket']]=x
sel=[]
for key in selected:
 a=dict(zip(fields,key));a['label_name']=new[key]['label_name']
 for version,d in [('C',cmap),('grok',grok),('Astra_v2',old),('Astra_v3',new)]:
  row=d.get(key)
  for name,cn in [('P','n_positive'),('N','n_interpretable'),('U','n_relation_unknown')]:a[version+'_'+name]=row.get(cn if version=='C' else name,'') if row else ''
 sel.append(a)
dump('tables/V3_key_results_version_chain.csv',sel)
qc=read(ROOT/'tables/Q3_review_receipts.csv');ad=read(ROOT/'tables/Q3_ads_final.csv')
quality=[]
for role in CONCRETE:
 rr=[x for x in qc if x['role']==role]
 quality.append(dict(role=role,role_name=RN[role],total=len(rr),full=sum(x['second_pass_status']=='ASTRA_FULL_SOURCE_REVIEWED' for x in rr),boundary_only=sum(x['second_pass_status']=='ASTRA_BOUNDARY_REVIEWED' for x in rr),not_selected=sum(x['second_pass_status']=='REVIEW_PENDING' for x in rr),seed=sum(x['seeded']=='YES' for x in rr),mandatory=sum(x['mandatory']=='YES' for x in rr)))
dump('tables/V3_review_coverage_final.csv',quality)
summary=dict(status='COMPLETE',same_scope_cells=len(new),changed_cells=len(out),gate_changes=sum(x['v2_gate']!=x['v3_gate'] for x in out),total_revision_operations=len(ch),v3_incremental_operations=len(inc),v3_incremental_ads=len({x['identity_key'] for x in inc}),effective_evidence_changed=len(effective),effective_evidence_ads=len({x['identity_key'] for x in effective}),reviewed_union=sum(x['second_pass_status']!='REVIEW_PENDING' for x in qc),full=sum(x['second_pass_status']=='ASTRA_FULL_SOURCE_REVIEWED' for x in qc),boundary_only=sum(x['second_pass_status']=='ASTRA_BOUNDARY_REVIEWED' for x in qc),unselected=sum(x['second_pass_status']=='REVIEW_PENDING' for x in qc),source_limits_ads=len({t['identity_key'] for t in [json.loads(s) for s in (ROOT/'review/astra_reviews.jsonl').read_text(encoding='utf-8').splitlines()] if t.get('source_limits')}))
save_json('verification/V3_revision_impact_final.json',summary)
print(js(summary));print(js(sel))
