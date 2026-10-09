"""Complete Q2 comparison with explicit exclusions and reproducible sensitivities.
No statistical row licenses population or causal interpretation.
"""
from common import *
from astra_stats import point,aggregate,tests
from contextlib import ExitStack
from datetime import datetime,timezone

assert tests()==8
ads=read(ROOT/'tables/Q3_ads_final.csv');AD={a['identity_key']:a for a in ads}
assert len(AD)==1576
cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
CD={x['code']:x for x in cat['labels']};CBR=defaultdict(set)
for c,l in CD.items():
 for r in l['applicable_roles']:CBR[r].add(c)
rules=json.loads((ROOT/'configs/Q_coding_rules_v2.json').read_text(encoding='utf-8'))
slices=[(s['metric'],s['branch']) for s in rules['legacy_14_slices']]
slices += [(m,b) for m in ['DUTY_OWN_USE','DUTY_OWN_DEVELOP'] for b in ['CHOICE','EXAMPLE','CHOICE_AND_EXAMPLE','CONDITIONAL']]
whole={k for k,a in AD.items() if a['company_id'] in WHOLE}
mem={'WHOLE23':whole,'ALL24':set(AD),'FAR':set(AD)-whole};scope_notes={}
source=defaultdict(set)
for r in read(ROOT/'tables/R_source_membership.csv'):source[r['scope']].add(r['identity_key'])
for s in ['S1_ACTIVITY_COMPLETE','S2_SOURCE_QUALITY','S3_SOURCE_QUALITY_LENGTH200']:
 mem[s]=source[s]&whole;scope_notes[s]='固定来源方案与Q2整公司主范围求交；不是国家子样本。'
for s,field in [('EXCLUDE_MULTI_PRODUCT','known_multi_product'),('EXCLUDE_MEDIA_ONLY','media_only_basis')]:
 mem[s]={k for k in whole if CO[AD[k]['company_id']].get(field)!='YES'}
ex={r['identity_key'] for r in read(ROOT/'tables/D_explicit_audience_exclusions.csv')}
mem['EXCLUDE_EXPLICIT_CAMPUS_INTERN']=whole-ex
scope_notes['EXCLUDE_EXPLICIT_CAMPUS_INTERN']='排除明确实习/校招/应届资格广告；部分也接受有经验者，不称纯校园岗位。'
clusters=defaultdict(list)
for k in whole:
 a=AD[k];t=re.sub(r'\s+',' ',RAW[k].get('duties') or '').strip()
 if len(t)>=80:clusters[a['company_id'],a['role'],t].append(k)
removed=set();dr=[]
for (co,ro,t),ks in sorted(clusters.items()):
 if len(ks)<2:continue
 ks=sorted(ks);removed.update(ks[1:]);h=hashlib.sha256(t.encode()).hexdigest()
 for i,k in enumerate(ks):dr.append(dict(cluster_sha256=h,company_id=co,role=ro,identity_key=k,reading_id=AD[k]['reading_id'],keep='YES' if i==0 else 'NO',reason='同公司同主职能职责文本仅归一空白后完全相同；保留identity_key字典序首条',requirements_equal_to_kept=RAW[k].get('requirements')==RAW[ks[0]].get('requirements')))
mem['DEDUPE_EXACT_DUTIES']=whole-removed
scope_notes['DEDUPE_EXACT_DUTIES']='职责>=80字符的完全相同模板敏感性；要求可能不同，不能认定为重复职位或替代主分析。'
if dr:dump('tables/Q4_dedup_membership.csv',dr)
for st in sorted({CO[AD[k]['company_id']]['stratum'] for k in whole}):
 mem['SUPPLY_'+st]={k for k in whole if CO[AD[k]['company_id']]['stratum']==st}
scene_rows=read(C/'inputs/rules_v1/company_scene_matrix.csv')
for sc in sorted({s['scene'] for s in scene_rows}):
 current={s['company_id'] for s in scene_rows if s['scene']==sc and s['connection_status']=='CURRENT_CONNECTION'}
 actual={s['company_id'] for s in scene_rows if s['scene']==sc and any(v in s['states'] for v in ['OBSERVED_USE','OBSERVED_DONATION','OBSERVED_RESEARCH_USE'])}
 for mode,cos in [('CURRENT',current),('ACTUAL_USE',actual)]:
  name='SCENE_'+sc+'_'+mode;mem[name]={k for k in whole if AD[k]['company_id'] in cos}
  scope_notes[name]='公司可多场景重叠；未知不是无场景；ACTUAL_USE包含研究使用/捐赠，不等于商业交付。'
# DIRECT is label-dimension specific. New v2 labels have no old direct-coverage status.
for dim in ['technical','skills']:
 mem['DIRECT_'+dim]={k for k in whole if J[k][dim+'_status'] in ['CODED','NOT_MENTIONED']}
 scope_notes['DIRECT_'+dim]='仅旧目录对应维度的CODED/NOT_MENTIONED；新增条目没有旧目录状态，不伪造对应。'
dump('tables/Q4_scope_membership.csv',[dict(scope=s,identity_key=k,reading_id=AD[k]['reading_id'],company_id=AD[k]['company_id']) for s,ks in mem.items() for k in sorted(ks)])
dump('tables/Q4_scope_definitions.csv',[dict(scope=s,ads=len(ks),companies=len({AD[k]['company_id'] for k in ks}),note=scope_notes.get(s,'冻结范围；FAR团队独列，整公司组不含FAR。')) for s,ks in mem.items()])
isc=defaultdict(list)
for s,ks in mem.items():
 for k in ks:isc[k].append(s)
# Only nonzero/nonassessable cells require storage. Z is derived with an assertion.
cnt=defaultdict(Counter);tcnt=defaultdict(Counter);union=defaultdict(set);observed=Counter()
with (ROOT/'tables/Q3_states_final.csv').open(encoding='utf-8-sig',newline='') as f:
 for a in csv.DictReader(f):
  observed[a['state']]+=1
  if a['state']=='Z':continue
  k=a['identity_key'];r,c,m,b,co=a['role'],a['label_code'],a['metric'],a['branch'],a['company_id'];st=a['state']
  assert st in ['P','U','NA','SOURCE_EXCLUDED']
  for s in isc[k]:cnt[s,r,c,m,b,co][st]+=1
  if k in whole:
   tcnt[r,a['task'],c,m,b,co][st]+=1
   if st=='P':union[r,c].add(k)
print('Counted',dict(observed),flush=True)
nbase=defaultdict(Counter);ntask=defaultdict(Counter)
for k,a in AD.items():
 for s in isc[k]:nbase[s,a['role']][a['company_id']]+=1
 if k in whole:ntask[a['role'],a['task']][a['company_id']]+=1
disp=[];selected=set()
generic={'SK_GENERIC_LANGUAGE','SK_GENERIC_ML_FRAMEWORK','SK_CAD','SK_GENERIC_CAD','SK_GENERIC_CAE'}
for r in sorted(CBR):
 for mt in sorted({CD[c]['measurement_type'] for c in CBR[r]}):
  scored=[]
  for c in CBR[r]:
   if CD[c]['measurement_type']!=mt or c in generic:continue
   ks=union[r,c];nc=len({AD[k]['company_id'] for k in ks})
   if nc>=int(rules['display']['min_positive_companies']) and len(ks)>=int(rules['display']['min_positive_ads']):scored.append((nc,len(ks),c))
  for i,(nc,nn,c) in enumerate(sorted(scored,key=lambda x:(-x[0],-x[1],x[2]))[:int(rules['display']['max_per_type'])],1):
   selected.add((r,c));disp.append(dict(role=r,label_code=c,label_name=CD[c]['name'],measurement_type=mt,display_rank=i,positive_companies_union=nc,positive_ads_union=nn,selection='任何明确本人职责或要求语境正例按广告去重；各语境结果仍分别报告'))
dump('tables/Q4_display_selection.csv',disp)
def pts(s,r,c,m,b):
 return [point(co,n,cnt.get((s,r,c,m,b,co),{})) for co,n in sorted(nbase[s,r].items())]
def flat(a):return {k:js(v) if isinstance(v,list) else v for k,v in a.items()}
class Writer:
 def __init__(self,name,stack):self.f=stack.enter_context((ROOT/name).open('w',encoding='utf-8-sig',newline=''));self.w=None;self.n=0
 def put(self,r):
  if self.w is None:self.w=csv.DictWriter(self.f,fieldnames=list(r));self.w.writeheader()
  self.w.writerow(flat(r));self.n+=1
main={};counts={};loo_max=defaultdict(lambda:[None,None,0]);positive_eligible=Counter();task_positive_eligible=Counter()
with ExitStack() as stack:
 wa=Writer('tables/Q4_aggregates_final.csv',stack);wp=Writer('tables/Q4_company_points_final.csv',stack);wd=Writer('tables/Q4_display_cells_final.csv',stack);wl=Writer('tables/Q4_leave_one_company_out_final.csv',stack)
 for s in mem:
  print('Aggregate',s,flush=True)
  for r in sorted(CBR):
   for c in sorted(CBR[r]):
    if s.startswith('DIRECT_') and CD[c]['legacy_dimension']!=s[len('DIRECT_'):]:continue
    for m,b in slices:
     pp=pts(s,r,c,m,b);a=aggregate(pp);base=dict(scope=s,role=r,label_code=c,label_name=CD[c]['name'],measurement_type=CD[c]['measurement_type'],metric=m,branch=b)
     rec=dict(base,**a);wa.put(rec)
     if s=='WHOLE23':
      main[r,c,m,b]=rec
      if a['P'] and a['gate']=='EXPLORATORY_SUMMARY':positive_eligible[r]+=1
      for p in pp:wp.put(dict(base,**p))
      if (r,c) in selected:
       wd.put(rec)
       # Exact leave-one-company-out for every separate context of selected labels.
       for p in pp:
        la=aggregate([v for v in pp if v['company_id']!=p['company_id']]);wl.put(dict(base,removed_company=p['company_id'],**la))
 wt=Writer('tables/Q4_task_strata_final.csv',stack);wtp=Writer('tables/Q4_task_company_points_final.csv',stack)
 focus={r['role']:r['focus_task'] for r in read(ROOT/'tables/Q1_prefixed_comparison_plan.csv')}
 for (r,t),nb in sorted(ntask.items()):
  for c in sorted(CBR[r]):
   for m,b in slices:
    pp=[point(co,n,tcnt.get((r,t,c,m,b,co),{})) for co,n in sorted(nb.items())];a=aggregate(pp)
    base=dict(scope='WHOLE23',role=r,task=t,prefixed_focus='YES' if t==focus[r] else 'NO',label_code=c,label_name=CD[c]['name'],measurement_type=CD[c]['measurement_type'],metric=m,branch=b)
    wt.put(dict(base,**a))
    if a['P'] and a['gate']=='EXPLORATORY_SUMMARY':task_positive_eligible[r]+=1
    # Full company points of the pre-specified task, plus all positive/unknown task cells.
    if t==focus[r] or a['P'] or a['U']:
     for p in pp:wtp.put(dict(base,**p))
 counts={name:w.n for name,w in [('aggregates',wa),('company_points',wp),('display_cells',wd),('loo',wl),('task_aggregates',wt),('task_company_points',wtp)]}
dump('tables/Q4_role_coverage_final.csv',[dict(role=r,role_name=RN[r],all24_ads=sum(a['role']==r for a in ads),whole23_ads=sum(nbase['WHOLE23',r].values()),whole23_companies=len(nbase['WHOLE23',r]),applicable_labels=len(CBR[r]),full_review_ads=sum(a['role']==r and a['qc_status']=='ASTRA_FULL_SOURCE_REVIEWED' for a in ads),positive_cells_with_group_gate=positive_eligible[r],positive_task_cells_with_group_gate=task_positive_eligible[r],display_labels=sum(rr==r for rr,c in selected),interpretation='L3逐格许可与主图筛选独立；许可不等于行业代表性或差异显著。') for r in sorted(CBR)])
save_json('verification/astra_comparison.json',dict(status='COMPUTED_NOT_AUTOMATIC_CONTENT_ACCEPTANCE',state_rows=sum(observed.values()),state_counts=dict(observed),ads=len(ads),scopes=len(mem),display_labels=len(selected),**counts,arithmetic_checks=8,catalog='Q2-v2.1',coding='Astra-Q2-v2.1-review3',created_utc=datetime.now(timezone.utc).isoformat()))
print(js(counts),flush=True)
