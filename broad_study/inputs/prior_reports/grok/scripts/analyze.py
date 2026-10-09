"""Stage D. Frozen C/B/rules inputs, no recoding. Python stdlib only."""
from pathlib import Path
import csv,json,hashlib,math,re
from collections import Counter,defaultdict
from statistics import median
ROOT=Path(__file__).resolve().parents[1]
IN=ROOT/'inputs';T=ROOT/'tables'
def read(p):
 with Path(p).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def js(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def table(name,rows):
 rows=list(rows);assert rows,name
 keys=[]
 for r in rows:
  for k in r:
   if k not in keys:keys.append(k)
 p=T/name;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=keys,restval='');w.writeheader();w.writerows(rows)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def check_inputs():
 for rel,e in js(ROOT/'input_lock.json')['files'].items():
  p=ROOT/rel
  if not p.is_file() or sha(p)!=e['sha256'] or p.stat().st_size!=e['bytes']:raise ValueError('INPUT_DRIFT: '+rel)
def ratio(n,d):return round(n/d,10) if d else ''
def top_company(counter):
 if not counter:return ('',0)
 m=max(counter.values())
 return min(c for c,v in counter.items() if v==m),m
def pctile(vals,p):
 s=sorted(vals);n=len(s)
 if n==0:return ''
 if n==1:return round(s[0],10)
 k=(n-1)*p;f=int(k);w=k-f
 if f+1>=n:return round(s[-1],10)
 return round(s[f]*(1-w)+s[f+1]*w,10)
def classof(j):return j['primary_code'] if j['primary_status']=='CODED' else j['primary_status']
def iint(x):return int(x) if x not in ('',None) else 0
def ffloat(x):return float(x) if x not in ('',None) else 0.0

NAMESAKE={'ACT_RESEARCH':'RF_RESEARCH_SCIENCE','ACT_DEPLOYMENT':'RF_DEPLOYMENT_FIELD_SERVICE','ACT_QUALITY':'RF_MANUFACTURING_QUALITY_SUPPLY'}
PAIRS=[('RESEARCH_ENGINEERING','ACT_RESEARCH','ACT_ENGINEERING','研究探索','工程实现'),('ENGINEERING_QUALITY','ACT_ENGINEERING','ACT_QUALITY','工程实现','质量验证'),('ENGINEERING_DEPLOYMENT','ACT_ENGINEERING','ACT_DEPLOYMENT','工程实现','部署与维护')]
ML_TECH=[('TC_ML_SYSTEMS','训练推理系统'),('TC_FOUNDATION_MODEL','基础模型/VLA'),('TC_DATA_PIPELINE','数据管线与资产')]
KIND_UNSP={'AMBIGUOUS','UNMAPPED','SOURCE_UNASSESSABLE'}
KIND_STRUCT={'RF_COMPOSITE_FUNCTION','RF_ALTERNATIVE_DIRECTIONS'}

def spans_overlap(a,b):
 if not a or not b:return False
 fa,sa,ea=a;fb,sb,eb=b
 if fa!=fb or sa is None or ea is None or sb is None or eb is None:return False
 return sa<eb and sb<ea

def node_span(ev):
 try:return ev.get('field',''),int(ev.get('start') or 0),int(ev.get('end') or 0)
 except Exception:return None

def top_children(tree):
 expr=tree.get('expression',tree)
 rel=expr.get('relation','')
 kids=expr.get('children') or []
 out=[]
 for ch in kids:
  sp=[]
  def collect(n):
   for ev in n.get('evidence') or []:
    s=node_span(ev); 
    if s:sp.append(s)
   for d in n.get('duties') or []:
    for ev in d.get('evidence') or []:
     s=node_span(ev)
     if s:sp.append(s)
   for c in n.get('children') or []:collect(c)
  collect(ch)
  out.append(dict(id=ch.get('id',''),relation=ch.get('relation',''),spans=sp,function=ch.get('value','')))
 return rel,out

def judge_dual(ident,quotes_a,quotes_b,structures):
 st=structures.get(ident)
 if not st:return 'UNCONDITIONAL_JOINT','no_role_structure','same posting presents both as owned duties; no exclusive-direction tree'
 tree=json.loads(st['tree_json']) if isinstance(st['tree_json'],str) else st['tree_json']
 root,children=top_children(tree)
 qa=[(q.get('field',''),iint(q.get('start')),iint(q.get('end')) or None) for q in quotes_a]
 qb=[(q.get('field',''),iint(q.get('start')),iint(q.get('end')) or None) for q in quotes_b]
 def bind(qs):
  hits=set();ok=False
  for q in qs:
   qsp=(q[0],q[1] if q[1] else None,q[2])
   if qsp[1] is None or qsp[2] in (None,0):
    continue
   ok=True
   for i,ch in enumerate(children):
    if any(spans_overlap(qsp,sp) for sp in ch['spans']):hits.add(i)
  return hits,ok
 ha,oka=bind(qa);hb,okb=bind(qb)
 if root=='ALL':
  return 'UNCONDITIONAL_JOINT','compound_all','composite tree (ALL): advertised hire jointly carries both duties'
 if root=='OR':
  if not oka or not okb or not ha or not hb:return 'UNRESOLVED','or_bind_failed','activity quotes could not be bound to exclusive branches'
  if ha==hb and len(ha)==1:return 'CONDITIONAL_JOINT','same_or_branch','both owned duties only bind to one optional direction'
  if ha.isdisjoint(hb):return 'ALTERNATIVE_ONLY','disjoint_or_branches','owned duties bind to mutually exclusive directions'
  return 'UNRESOLVED','or_overlap_ambiguous','OR tree binding overlaps more than one branch'
 return 'UNCONDITIONAL_JOINT','other_structure','structure present but not exclusive OR; treated as joint advertised duties'

def subject_guess(fact):
 text=' '.join(str(fact.get(k) or '') for k in ['value','note','decision_reason','product_or_business_scope'])
 if any(x in text for x in ['自营','自有履单','自有品牌','机器人履单','3PL','Robots-as-a-Service','RaaS']):
  if any(x in text for x in ['自营','自有履单','自有品牌','履单中心']):return 'COMPANY'
  if 'RaaS' in text or 'Robots-as-a-Service' in text:return 'UNKNOWN'
 return 'UNKNOWN'

def stage_for(fact):
 field=fact['field'];val=str(fact.get('value') or '')
 if field.startswith('product_lines'):return 'PRODUCT_OR_MODEL_DEVELOPMENT'
 if field=='delivery_form':
  if any(x in val for x in ['集成','system integration']):return 'SYSTEM_INTEGRATION'
  if any(x in val for x in ['履单','3PL','自营','RaaS','运营']):return 'ONGOING_OPERATIONS'
  return 'PRODUCT_OR_MODEL_DEVELOPMENT'
 if field in ['deployment_status_actual','evidence_customer_delivery']:return 'CUSTOMER_SITE_DEPLOYMENT'
 if field=='evidence_sustained_use':return 'ONGOING_OPERATIONS'
 if field=='evidence_demo':return 'DEMONSTRATION_NOT_OPERATIONS'
 if field=='evidence_external_pilot':return 'PILOT_NOT_FULL_OPERATIONS'
 if field in ['evidence_paid','evidence_repeat_order']:return 'COMMERCIAL_EVIDENCE'
 if field=='evidence_production_shipment':return 'PRODUCTION_OR_SHIPMENT'
 if field=='target_markets':return 'TARGET_NOT_RESPONSIBILITY'
 if '维护' in val or '售后' in val:return 'MAINTENANCE_SUPPORT'
 return ''

def main():
 check_inputs();T.mkdir(exist_ok=True)
 jobs=read(IN/'stage_c'/'jobs.csv');byid={j['identity_key']:j for j in jobs};assert len(byid)==1654
 t1=read(IN/'stage_c'/'tables'/'T1_company_sample.csv');cb={r['company_id']:r for r in t1};companies=sorted(cb)
 whole={c for c in companies if cb[c]['scope_main_company']=='YES'}
 t2=read(IN/'stage_c'/'tables'/'T2_company_primary_roles.csv')
 t2agg=read(IN/'stage_c'/'tables'/'T2_aggregates.csv')
 t3ctx=read(IN/'stage_c'/'tables'/'T3_company_context.csv')
 t3base=read(IN/'stage_c'/'tables'/'T3_base_admission.csv')
 t3lin=read(IN/'stage_c'/'tables'/'T3_positive_unknown_lineage.csv')
 t3sem=read(IN/'stage_c'/'tables'/'T3_all_item_semantics.csv')
 t4cross=read(IN/'stage_c'/'tables'/'T4_primary_activity_cross.csv')
 t4co=read(IN/'stage_c'/'tables'/'T4_activity_company.csv')
 t4adm=read(IN/'stage_c'/'tables'/'T4_activity_admission.csv')
 acts=read(IN/'stage_c'/'tables'/'T4_activity_lineage.csv')
 strows=read(IN/'stage_c'/'tables'/'T4_role_structures.csv');structures={r['identity_key']:r for r in strows}
 facts=read(IN/'stage_b'/'company_facts.csv');gaps=read(IN/'stage_b'/'company_gaps.csv');prof=read(IN/'stage_b'/'company_profile.csv')
 scenes=read(IN/'rules_v1'/'company_scene_assertions.csv');q2sel=read(IN/'rules_v1'/'q2_display_selection.csv')
 source=js(IN/'decisions'/'source_complete_subset.json');scset=set(source['included_company_ids']);rules=js(IN/'decisions'/'case_selection_rules.json')
 cats={}; 
 for r in t2:cats[r['class_code']]=(r['class_name'],r['class_kind'])
 anames={r['activity_code']:r['activity_name'] for r in t4cross}
 eligible={r['identity_key'] for r in t4adm if r['base_eligible']=='YES'}
 owned=defaultdict(set);part=defaultdict(set);actq=defaultdict(list)
 for r in acts:
  if r['identity_key'] not in eligible:continue
  if r['relation']=='OWNED':owned[r['label_code']].add(r['identity_key']);actq[(r['identity_key'],r['label_code'],'OWNED')].append(r)
  elif r['relation']=='PARTICIPATES':part[r['label_code']].add(r['identity_key'])
 scopes={'ALL24':set(companies),'WHOLE23':whole,'SOURCE_COMPLETE':scset}

 # D1 Q1 coverage
 q1cov=[]
 for scope,members in scopes.items():
  rows=[r for r in t2 if r['company_id'] in members]
  for code,(name,kind) in cats.items():
   sub=[r for r in rows if r['class_code']==code]
   ns=[iint(r['n_ads']) for r in sub];shares=[ffloat(r['share_all']) for r in sub];dens=[iint(r['denominator_all']) for r in sub]
   pos_companies=sum(n>0 for n in ns);total=sum(ns)
   mx=max(ns) if ns else 0;mx_c=max(sub,key=lambda r:iint(r['n_ads']))['company_id'] if sub else ''
   eq=sum(n/d for n,d in zip(ns,dens) if d)/sum(d>0 for d in dens) if any(dens) else ''
   q1cov.append(dict(scope=scope,class_code=code,class_name=name,class_kind=kind,n_ads=total,n_companies=len(members),n_companies_positive=pos_companies,share_company_equal=round(eq,10) if eq!='' else '',share_ad_weighted=ratio(total,sum(dens)),median_company_share=pctile(shares,.5),p25_company_share=pctile(shares,.25),p75_company_share=pctile(shares,.75),max_company_id=mx_c,max_company_positive_ads=mx,max_positive_contribution=ratio(mx,total),zeros_included_in_distribution='YES',note='Q1 zeros enter the company distribution; a recorded zero is not proof the company never needs the work'))
 table('D1_q1_coverage.csv',q1cov)

 # D1 Q2 coverage main display
 mainset={(r['role_code'],r['dimension'],r['label_code']) for r in q2sel if r['main_display']=='YES'}
 q2cov=[]
 for scope,members in [('WHOLE23',whole),('ALL24',set(companies)),('SOURCE_COMPLETE',scset)]:
  sub=[r for r in t3ctx if r['company_id'] in members and (r['role_code'],r['dimension'],r['label_code']) in mainset]
  for r in sub:
   pass
  keys=sorted({(r['role_code'],r['dimension'],r['label_code'],r['metric_bucket'],r['branch_bucket']) for r in sub})
  for key in keys:
   cells=[r for r in sub if (r['role_code'],r['dimension'],r['label_code'],r['metric_bucket'],r['branch_bucket'])==key]
   base_c=sum(iint(r['n_base'])>0 for r in cells);interp_c=sum(iint(r['n_interpretable'])>0 for r in cells);pos_c=sum(iint(r['n_positive'])>0 for r in cells)
   den=sum(iint(r['n_interpretable']) for r in cells);pos=sum(iint(r['n_positive']) for r in cells);base=sum(iint(r['n_base']) for r in cells);unk=sum(iint(r['n_relation_unknown']) for r in cells)
   mxden=max(cells,key=lambda r:iint(r['n_interpretable'])) if cells else None
   mxpos=max(cells,key=lambda r:iint(r['n_positive'])) if cells else None
   sample=next(r for r in cells)
   q2cov.append(dict(scope=scope,role_code=key[0],dimension=key[1],label_code=key[2],label_name=sample['label_name'],metric_bucket=key[3],branch_bucket=key[4],n_base=base,n_positive=pos,n_relation_unknown=unk,n_interpretable=den,n_companies_base=base_c,n_companies_interpretable=interp_c,n_companies_positive=pos_c,max_denom_company='' if not mxden else mxden['company_id'],max_denom_contribution=ratio(iint(mxden['n_interpretable']),den) if mxden else '',max_positive_company='' if not mxpos else mxpos['company_id'],max_positive_contribution=ratio(iint(mxpos['n_positive']),pos) if mxpos else '',dominance_warning='YES' if mxden and den and iint(mxden['n_interpretable'])/den>0.5 else 'NO',zero_denom_excluded_from_median='YES'))
 table('D1_q2_coverage.csv',q2cov)

 q3cov=[]
 for scope,members in scopes.items():
  sub=[r for r in t4co if r['company_id'] in members]
  for lab in sorted({r['label_code'] for r in sub}):
   for rel in ['OWNED','PARTICIPATES']:
    cells=[r for r in sub if r['label_code']==lab and r['relation']==rel]
    den=sum(iint(r['n_assessable']) for r in cells);pos=sum(iint(r['n_positive']) for r in cells)
    base_c=sum(iint(r['n_assessable'])>0 for r in cells);pos_c=sum(iint(r['n_positive'])>0 for r in cells)
    mxden=max(cells,key=lambda r:iint(r['n_assessable']));mxpos=max(cells,key=lambda r:iint(r['n_positive']))
    q3cov.append(dict(scope=scope,label_code=lab,label_name=cells[0]['label_name'],relation=rel,n_positive=pos,n_assessable=den,n_companies_assessable=base_c,n_companies_positive=pos_c,share_ad_weighted=ratio(pos,den),max_denom_company=mxden['company_id'],max_denom_contribution=ratio(iint(mxden['n_assessable']),den),max_positive_company=mxpos['company_id'],max_positive_contribution=ratio(iint(mxpos['n_positive']),pos),dominance_warning='YES' if iint(mxden['n_assessable'])/den>0.5 else 'NO'))
 table('D1_q3_coverage.csv',q3cov)

 # D2 bidirectional cross
 def kind_of(code):
  if code in KIND_UNSP:return 'unspecified'
  if code in KIND_STRUCT:return 'structure'
  return cats.get(code,('', 'concrete'))[1] or 'concrete'
 cross_rows=[];headline=[]
 for scope,members in [('ALL24',set(companies)),('WHOLE23',whole)]:
  ads=[j for j in jobs if j['company_id'] in members]
  elig={j['identity_key'] for j in ads if j['identity_key'] in eligible}
  for act_code,act_name in sorted(anames.items()):
   pos=owned[act_code]&elig
   cnt=Counter(classof(byid[i]) for i in pos)
   npos=len(pos)
   for code,(name,kind) in cats.items():
    ids={j['identity_key'] for j in ads if classof(j)==code and j['identity_key'] in eligible}
    n_role_act=len(ids&owned[act_code]);n_role=len(ids)
    n_act_role=cnt[code]
    cross_rows.append(dict(scope=scope,primary_code=code,primary_name=name,class_kind=kind_of(code),activity_code=act_code,activity_name=act_name,relation='OWNED',n_role_assessable=n_role,n_role_and_activity=n_role_act,share_activity_given_role=ratio(n_role_act,n_role),n_activity_positive=npos,n_activity_in_role=n_act_role,share_role_given_activity=ratio(n_act_role,npos)))
 for act_code,expected in [('ACT_RESEARCH',75),('ACT_DEPLOYMENT',351),('ACT_QUALITY',466)]:
  pos=owned[act_code]&{j['identity_key'] for j in jobs if j['identity_key'] in eligible}
  assert len(pos)==expected, (act_code,len(pos),expected)
  ns=NAMESAKE[act_code];cnt=Counter(classof(byid[i]) for i in pos)
  n_name=cnt[ns];n_struct=sum(cnt[c] for c in KIND_STRUCT);n_unsp=sum(cnt[c] for c in KIND_UNSP);n_other=len(pos)-n_name-n_struct-n_unsp
  headline.append(dict(activity_code=act_code,activity_name=anames[act_code],n_owned=len(pos),namesake_code=ns,n_namesake=n_name,n_other_concrete=n_other,n_structure=n_struct,n_unspecified=n_unsp,share_outside_namesake=ratio(len(pos)-n_name,len(pos)),note='主职能与活动独立测量；结构与未明确状态单列，不并入其他具体职能'))
 table('D2_role_activity_bidirectional.csv',cross_rows);table('D2_headline_cross_split.csv',headline)

 # D3 composition vs within-function
 within=[];assess_fn=defaultdict(lambda: defaultdict(int));owned_fn=defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
 for j in jobs:
  if j['identity_key'] not in eligible:continue
  code=classof(j);c=j['company_id']
  if kind_of(code)!='concrete':continue
  assess_fn[c][code]+=1
  for lab in owned:
   if j['identity_key'] in owned[lab]:owned_fn[c][code][lab]+=1
 for c in companies:
  tot=sum(assess_fn[c].values())
  for code,n in assess_fn[c].items():
   for lab,an in anames.items():
    p=owned_fn[c][code][lab]
    within.append(dict(company_id=c,company_name=cb[c]['company_name'],stratum=cb[c]['stratum'],primary_code=code,primary_name=cats[code][0],activity_code=lab,activity_name=an,n_function_assessable=n,n_company_assessable=tot,function_share_of_company=ratio(n,tot),n_activity_owned=p,share_activity_in_function=ratio(p,n),small_n_under10='YES' if n<10 else 'NO'))
 table('D3_within_function_activity.csv',within)
 # overall vs residual deployment
 decomp=[]
 for c in companies:
  tot=sum(1 for j in jobs if j['company_id']==c and j['identity_key'] in eligible)
  n_dep_fn=assess_fn[c].get('RF_DEPLOYMENT_FIELD_SERVICE',0)
  n_act=len({j['identity_key'] for j in jobs if j['company_id']==c and j['identity_key'] in owned['ACT_DEPLOYMENT']})
  other_ids={j['identity_key'] for j in jobs if j['company_id']==c and j['identity_key'] in eligible and classof(j)!='RF_DEPLOYMENT_FIELD_SERVICE'}
  n_act_other=len(other_ids&owned['ACT_DEPLOYMENT'])
  decomp.append(dict(company_id=c,company_name=cb[c]['company_name'],n_assessable=tot,n_deployment_function=n_dep_fn,share_deployment_function=ratio(n_dep_fn,tot),n_deployment_activity_owned=n_act,share_deployment_activity=ratio(n_act,tot),n_non_deployment_function_assessable=len(other_ids),n_deployment_activity_outside_deployment_function=n_act_other,share_deployment_activity_outside_deployment_function=ratio(n_act_other,len(other_ids)),note='若职能外部署活动仍高，则不能把总体部署活动率写成部署职能构成'))
 table('D3_deployment_composition.csv',decomp)

 # common K pairs
 pair_k=[]
 cov={c:{k:n for k,n in assess_fn[c].items() if n>=10} for c in companies}
 for i,a in enumerate(companies):
  for b in companies[i+1:]:
   K=sorted(set(cov.get(a,{}))&set(cov.get(b,{})))
   pair_k.append(dict(company_a=a,company_b=b,n_common_functions=len(K),common_functions_json=json.dumps(K,ensure_ascii=False),unified_weight_eligible='YES' if len(K)>=2 else 'NO',both_whole='YES' if a in whole and b in whole else 'NO'))
 table('D3_common_function_pairs.csv',pair_k)

 def unified(a,b,K,lab):
  # returns own-weight, equal-weight, pooled-weight rates for activity lab inside K
  def stats(c):
   rows=[]
   for fn in K:
    n=assess_fn[c][fn];p=owned_fn[c][fn][lab];rows.append((fn,n,p,p/n if n else None))
   tot=sum(n for _,n,_,_ in rows);own=sum(p for _,_,p,_ in rows)/tot if tot else ''
   eq=sum(r for *_,r in rows if r is not None)/len(rows) if rows else ''
   return rows,own,eq,tot
  ra,own_a,eq_a,tot_a=stats(a);rb,own_b,eq_b,tot_b=stats(b)
  pooled_w={fn:(assess_fn[a][fn]+assess_fn[b][fn]) for fn in K};pw=sum(pooled_w.values())
  pooled_a=sum((owned_fn[a][fn][lab]/assess_fn[a][fn])*pooled_w[fn] for fn in K)/pw if pw else ''
  pooled_b=sum((owned_fn[b][fn][lab]/assess_fn[b][fn])*pooled_w[fn] for fn in K)/pw if pw else ''
  return dict(own_a=own_a,own_b=own_b,equal_a=eq_a,equal_b=eq_b,pooled_a=pooled_a,pooled_b=pooled_b,n_a=tot_a,n_b=tot_b)

 # D4 co-occurrence
 co_rows=[];co_ads=[];co_sum=[]
 for scope,members in [('ALL24',set(companies)),('WHOLE23',whole)]:
  elig={j['identity_key'] for j in jobs if j['company_id'] in members and j['identity_key'] in eligible}
  for pid,a,b,na,nb in PAIRS:
   dual=owned[a]&owned[b]&elig
   states=Counter();byc=Counter()
   for ident in sorted(elig):
    if ident not in dual:
     states['NO_RECORDED_JOINT']+=1
     continue
    stt,rule,why=judge_dual(ident,actq[(ident,a,'OWNED')],actq[(ident,b,'OWNED')],structures)
    states[stt]+=1;byc[byid[ident]['company_id']]+= stt=='UNCONDITIONAL_JOINT'
    if scope=='ALL24':
     j=byid[ident]
     co_ads.append(dict(pair_id=pid,identity_key=ident,reading_id=j['reading_id'],company_id=j['company_id'],title=j['title'],primary_code=classof(j),has_role_structure='YES' if ident in structures else 'NO',root_relation=structures[ident]['root_relation'] if ident in structures else '',joint_state=stt,rule=rule,reason=why,quote_a=actq[(ident,a,'OWNED')][0]['quote'] if actq[(ident,a,'OWNED')] else '',quote_b=actq[(ident,b,'OWNED')][0]['quote'] if actq[(ident,b,'OWNED')] else ''))
   P=states['UNCONDITIONAL_JOINT'];U=states['UNRESOLVED'];Z=len(elig)-P-U;B=len(elig)
   mx=top_company(byc)
   co_sum.append(dict(scope=scope,pair_id=pid,activity_a=a,activity_b=b,name_a=na,name_b=nb,n_assessable=B,n_raw_dual=len(dual),n_unconditional=P,n_conditional=states['CONDITIONAL_JOINT'],n_alternative=states['ALTERNATIVE_ONLY'],n_unresolved=U,n_no_recorded=states['NO_RECORDED_JOINT'],n_interpretable=P+Z,share_unconditional=ratio(P,P+Z),n_companies_unconditional=sum(v>0 for v in byc.values()),max_company=mx[0],max_positive_contribution=ratio(mx[1],P),participates_not_included='YES'))
   for stt,n in states.items():
    co_rows.append(dict(scope=scope,pair_id=pid,joint_state=stt,n=n))
 table('D4_activity_cooccurrence_summary.csv',co_sum)
 table('D4_activity_cooccurrence_states.csv',co_rows)
 table('D4_activity_cooccurrence_ads.csv',co_ads)

 # D4b ML technical co-occurrence, whole-company ML, own-develop, unconditional
 ml_base={r['identity_key'] for r in t3base if r['role_code']=='RF_ML_AI_ENGINEERING' and r['dimension']=='technical_concepts' and r['base_eligible']=='YES' and r['scope_main_company']=='YES'}
 def t3state(label):
  s={}
  for r in t3lin:
   if r['role_code']=='RF_ML_AI_ENGINEERING' and r['dimension']=='technical_concepts' and r['label_code']==label and r['metric_bucket']=='DUTY_OWN_DEVELOP' and r['branch_bucket']=='UNCONDITIONAL' and r['identity_key'] in ml_base:
    s[r['identity_key']]=r['state']
  for ident in sorted(ml_base):
   s.setdefault(ident,'NO_RECORDED_POSITIVE')
  return s
 ml_states={code:t3state(code) for code,_ in ML_TECH}
 ml_pairs=[]
 for i,(ca,na) in enumerate(ML_TECH):
  for cb_,nb in ML_TECH[i+1:]:
   s1=ml_states[ca];s2=ml_states[cb_];P=U=Z=0;comp=Counter()
   for ident in sorted(ml_base):
    x,y=s1[ident],s2[ident]
    if x=='PRESENT' and y=='PRESENT':P+=1;comp[byid[ident]['company_id']]+=1
    elif x=='UNKNOWN' or y=='UNKNOWN':U+=1
    else:Z+=1
   mx=top_company(comp)
   ml_pairs.append(dict(role_code='RF_ML_AI_ENGINEERING',metric_bucket='DUTY_OWN_DEVELOP',branch_bucket='UNCONDITIONAL',scope='WHOLE23',label_a=ca,name_a=na,label_b=cb_,name_b=nb,n_base=len(ml_base),n_positive_joint=P,n_unknown=U,n_no_recorded=Z,n_interpretable=P+Z,share=ratio(P,P+Z),n_companies_joint=sum(v>0 for v in comp.values()),max_company=mx[0],max_positive_contribution=ratio(mx[1],P),gate='PASS' if sum(v>0 for v in comp.values())>=3 and P+Z>=20 else 'POINTS_ONLY'))
 table('D4_ml_technical_cooccurrence.csv',ml_pairs)

 # D5 case selection
 def evidence_rank(company,scene):
  rec=[r for r in scenes if r['company_id']==company and r['scene']==scene and r['state']=='OBSERVED_USE']
  if not rec:return 9
  reason=rec[0].get('decision_reason') or '';claim=rec[0].get('selected_claim') or ''
  named_ok=any(x in claim+reason for x in ['GXO','DHL','BMW','宁德时代','宁德','SPANX'])
  customer_ok=('直接客户' in reason) or ('客户确认' in reason) or ('客户商业' in reason) or ('COUNTERPARTY' in reason)
  if '未具名' in reason or '未具名' in claim:customer_ok=False
  if customer_ok or named_ok:return 0
  fact_ids=(rec[0].get('basis_fact_ids') or '').split('|')
  kinds=[next((f['assertion_kind'] for f in facts if f['fact_id']==fid), '') for fid in fact_ids if fid]
  if any(k in ['CUSTOMER_CONFIRMED_USE','COUNTERPARTY_CONFIRMATION'] for k in kinds) and '未具名' not in reason:return 0
  if cb[company].get('media_only_basis')=='YES':return 3
  if cb[company].get('known_multi_product')=='YES':return 2
  return 1
 mfg=[r['company_id'] for r in scenes if r['scene']=='MANUFACTURING' and r['state']=='OBSERVED_USE' and r['company_id'] in whole and cb[r['company_id']]['stratum']=='SYSTEM_PRODUCTS']
 mfg=sorted(set(mfg))
 best=None
 for i,a in enumerate(mfg):
  for b in mfg[i+1:]:
   K=sorted(set(cov.get(a,{}))&set(cov.get(b,{})))
   if len(K)<2:continue
   key=(-len(K),min(evidence_rank(a,'MANUFACTURING'),evidence_rank(b,'MANUFACTURING')),a,b)
   if best is None or key<best[0]:best=(key,a,b,K)
 g1=None
 if best:g1=dict(group_id='CASE_G1_MANUFACTURING_OBSERVED',companies=[best[1],best[2]],K=best[3],unified='YES')
 logi=[r['company_id'] for r in scenes if r['scene']=='LOGISTICS' and r['state']=='OBSERVED_USE' and r['company_id'] in whole]
 logi=sorted(set(logi))
 operated=[c for c in logi if cb[c]['stratum']=='ROBOT_OPERATED_SERVICE']
 product=[c for c in logi if cb[c]['stratum']=='SYSTEM_PRODUCTS']
 g2=None
 if operated and product:
  op=operated[0]
  product_sorted=sorted(product,key=lambda c:(evidence_rank(c,'LOGISTICS'), 0 if cb[c].get('known_multi_product')!='YES' else 1, -iint(cb[c]['n_ads']), c))
  partner=product_sorted[0]
  K=sorted(set(cov.get(op,{}))&set(cov.get(partner,{})))
  g2=dict(group_id='CASE_G2_LOGISTICS_DELIVERY',companies=[partner,op],K=K,unified='YES' if len(K)>=2 else 'NO')
 case_reg=[]
 selected=set((g1['companies'] if g1 else [])+(g2['companies'] if g2 else []))
 for c in companies:
  reasons=[];status='NOT_CANDIDATE'
  if c in mfg:status='MANUFACTURING_CANDIDATE';
  if c in logi:status='LOGISTICS_CANDIDATE' if status=='NOT_CANDIDATE' else status+'|LOGISTICS_CANDIDATE'
  if c in selected:status='SELECTED'
  if c in mfg and c not in selected:
   reasons.append('manufacturing observed-use candidate not in max-|K| customer-confirmed pair')
  if c in logi and c not in selected:
   if cb[c].get('known_multi_product')=='YES':reasons.append('multi-product lowers scene-to-hiring assignment')
   elif iint(cb[c]['n_ads'])<20:reasons.append('smaller official board not preferred')
   else:reasons.append('not the contrasting operated-service vs strongest customer-confirmed product pair')
  if c not in whole:reasons.append('team slice excluded from whole-company cases')
  case_reg.append(dict(company_id=c,company_name=cb[c]['company_name'],stratum=cb[c]['stratum'],n_ads=cb[c]['n_ads'],status=status,selected_group='' if c not in selected else ('CASE_G1_MANUFACTURING_OBSERVED' if g1 and c in g1['companies'] else 'CASE_G2_LOGISTICS_DELIVERY'),exclusion_or_inclusion='; '.join(reasons) if reasons else ('selected per locked rules' if c in selected else 'outside both scene candidate sets'),n_functions_ge10=len(cov.get(c,{})),functions_ge10_json=json.dumps(sorted(cov.get(c,{})),ensure_ascii=False)))
 table('D5_case_register.csv',case_reg)
 dump(ROOT/'case_selection.json',{'g1':g1,'g2':g2,'rules_id':rules['rules_id']})

 # unified weight tables for selected pairs
 uw=[]
 for g in [g1,g2]:
  if not g:continue
  a,b=g['companies'];K=g['K']
  cover_a=sum(assess_fn[a].get(fn,0) for fn in K);cover_b=sum(assess_fn[b].get(fn,0) for fn in K)
  tot_a=sum(assess_fn[a].values());tot_b=sum(assess_fn[b].values())
  for lab,aname in anames.items():
   row=dict(group_id=g['group_id'],company_a=a,company_b=b,activity_code=lab,activity_name=aname,K_json=json.dumps(K,ensure_ascii=False),cover_share_a=ratio(cover_a,tot_a),cover_share_b=ratio(cover_b,tot_b),n_a='',n_b='',own_weight_a='',own_weight_b='',equal_weight_a='',equal_weight_b='',pooled_weight_a='',pooled_weight_b='',note='Restricted rates do not replace company-wide rates and are not a causal decomposition')
   if g['unified']!='YES':
    row.update(status='INAPPLICABLE',reason='fewer than 2 common concrete functions with >=10 assessable ads');uw.append(row);continue
   u=unified(a,b,K,lab)
   row.update(status='RESTRICTED_TO_K',reason='common functions with >=10 assessable ads each',n_a=u['n_a'],n_b=u['n_b'],own_weight_a=round(u['own_a'],10) if u['own_a']!='' else '',own_weight_b=round(u['own_b'],10) if u['own_b']!='' else '',equal_weight_a=round(u['equal_a'],10) if u['equal_a']!='' else '',equal_weight_b=round(u['equal_b'],10) if u['equal_b']!='' else '',pooled_weight_a=round(u['pooled_a'],10) if u['pooled_a']!='' else '',pooled_weight_b=round(u['pooled_b'],10) if u['pooled_b']!='' else '')
   uw.append(row)
 table('D3_unified_weight_cases.csv',uw)

 # D6 T5 responsibility long table
 t5=[]
 for f in facts:
  stg=stage_for(f)
  if not stg:continue
  t5.append(dict(fact_id=f['fact_id'],company_id=f['company_id'],company_name=cb[f['company_id']]['company_name'],stratum=cb[f['company_id']]['stratum'],case_group=next((r['selected_group'] for r in case_reg if r['company_id']==f['company_id']),''),field=f['field'],business_stage=stg,responsibility_subject=subject_guess(f),product_or_scene=f.get('product_or_business_scope') or '',fact_value=f.get('value') or '',assertion_kind=f.get('assertion_kind') or '',value_status=f.get('value_status') or '',time_applicability=f.get('time_applicability') or '',event_date=f.get('event_date') or '',publication_date=f.get('publication_date') or '',observation_date=f.get('observation_date') or '',evidence_ids=f.get('evidence_ids') or '',note=f.get('note') or '',main_comparison='YES' if f.get('time_applicability')=='USABLE_AT_OBSERVATION' and f.get('value_status') not in ['NOT_YET_SEARCHED','SEARCHED_NOT_FOUND'] and (f.get('value') or '').strip() not in ['','未确立'] else 'NO'))
 table('T5_delivery_responsibility.csv',t5)
 gap_rows=[]
 for g in gaps:
  gap_rows.append(dict(orig_gap_id=g['orig_gap_id'],company_id=g['company_id'],fact_field=g['fact_field'],open_at_stage_b_end=g['open_at_stage_b_end'],stage_b_status=g['stage_b_status'],affects_grouping=g['affects_grouping'],affects_time_applicability=g['affects_time_applicability'],closure_reason=g.get('closure_reason') or '',comparison_effect='UNKNOWN_REMAINS' if g['open_at_stage_b_end']=='YES' and g['fact_field'].startswith('commercialization') else 'INHERITED'))
 table('T5_gap_status.csv',gap_rows)

 # D7 Q2 case points
 q2case=[]
 case_cos=selected
 for r in t3ctx:
  if r['company_id'] not in case_cos:continue
  if (r['role_code'],r['dimension'],r['label_code']) not in mainset:continue
  if r['metric_bucket'] not in ['DUTY_OWN_DEVELOP','DUTY_OWN_USE','GENERAL','REQUIRED'] :continue
  if r['branch_bucket']!='UNCONDITIONAL':continue
  q2case.append(dict(r))
 table('D7_case_q2_points.csv',q2case)

 # D8 seniority / work objects for selected case ads
 sen=[]; 
 intern=re.compile(r'实习|intern',re.I);director=re.compile(r'总监|director|\bvp\b|vice president',re.I);mgr=re.compile(r'经理|\bmanager\b|head of',re.I);senior_ic=re.compile(r'专家|principal|\bstaff\b|fellow',re.I);senior=re.compile(r'资深|\bsenior\b',re.I);early=re.compile(r'应届|new grad|campus|新星',re.I)
 obj_pat=[('ROBOT_SIDE',re.compile(r'本体|关节|嵌入式|firmware|on-?robot|整机控制',re.I)),('TRAINING_INFERENCE_PLATFORM',re.compile(r'训练平台|推理|infra|集群|GPU|训练系统',re.I)),('DATA_SERVICE',re.compile(r'数据管线|数据采集|标注|data pipeline',re.I)),('CUSTOMER_SITE',re.compile(r'客户现场|产线|仓库|warehouse|factory|部署实施|现场服务',re.I))]
 for j in jobs:
  if j['company_id'] not in case_cos:continue
  title=j.get('title') or '';level='NOT_STATED'
  if intern.search(title):level='INTERNSHIP'
  elif director.search(title):level='DIRECTOR_OR_ABOVE'
  elif mgr.search(title):level='MANAGER'
  elif senior_ic.search(title):level='SENIOR_IC'
  elif senior.search(title):level='SENIOR'
  elif early.search(title):level='EARLY_CAREER'
  blob=title+' '+' '.join(x['quote'] for x in acts if x['identity_key']==j['identity_key'])
  objs=[name for name,pat in obj_pat if pat.search(blob)]
  sen.append(dict(identity_key=j['identity_key'],company_id=j['company_id'],title=title,primary_code=classof(j),seniority_from_title=level,work_objects_json=json.dumps(objs or ['UNKNOWN'],ensure_ascii=False),duties_chars=j.get('duties_chars') or '',full_description_chars=j.get('full_description_chars') or '',source_coverage=j.get('source_coverage') or '',note='Unstated seniority is not junior. Work objects are keyword flags on title and activity quotes, not a new classification.'))
 table('D8_case_seniority_work_objects.csv',sen)

 # D9 sensitivity for core metrics
 def owned_outside(act,members):
  pos=owned[act]&{j['identity_key'] for j in jobs if j['company_id'] in members and j['identity_key'] in eligible}
  ns=NAMESAKE[act];n_name=sum(1 for i in pos if classof(byid[i])==ns)
  return len(pos),n_name,len(pos)-n_name,ratio(len(pos)-n_name,len(pos))
 sens=[]
 for scope,members in [('ALL24',set(companies)),('WHOLE23',whole),('SOURCE_COMPLETE',scset)]:
  for act in ['ACT_RESEARCH','ACT_DEPLOYMENT','ACT_QUALITY']:
   n,n_name,n_out,share=owned_outside(act,members)
   sens.append(dict(check_id='CROSS_FUNCTION_OUTSIDE_NAMESAKE',scope=scope,activity=act,n_owned=n,n_namesake=n_name,n_outside=n_out,share_outside=share,removed_company=''))
  dep=[r for r in decomp if r['company_id'] in members and r['n_assessable'] and iint(cb[r['company_id']]['n_ads'])]
  # company-equal mean of outside-function deployment activity
  vals=[ffloat(r['share_deployment_activity_outside_deployment_function']) for r in dep if r['share_deployment_activity_outside_deployment_function']!='']
  fn=[ffloat(r['share_deployment_function']) for r in dep if r['share_deployment_function']!='']
  actv=[ffloat(r['share_deployment_activity']) for r in dep if r['share_deployment_activity']!='']
  sens.append(dict(check_id='DEPLOYMENT_ACTIVITY_OUTSIDE_FUNCTION_EQUAL',scope=scope,activity='ACT_DEPLOYMENT',n_owned='',n_namesake='',n_outside='',share_outside=round(sum(vals)/len(vals),10) if vals else '',removed_company='',note='company-equal mean of deployment-activity rate inside non-deployment primary functions'))
  sens.append(dict(check_id='DEPLOYMENT_FUNCTION_SHARE_EQUAL',scope=scope,activity='RF_DEPLOYMENT_FIELD_SERVICE',n_owned='',n_namesake='',n_outside='',share_outside=round(sum(fn)/len(fn),10) if fn else '',removed_company=''))
  sens.append(dict(check_id='DEPLOYMENT_ACTIVITY_OVERALL_EQUAL',scope=scope,activity='ACT_DEPLOYMENT',n_owned='',n_namesake='',n_outside='',share_outside=round(sum(actv)/len(actv),10) if actv else '',removed_company=''))
 for c in sorted(whole):
  members=whole-{c};n,n_name,n_out,share=owned_outside('ACT_DEPLOYMENT',members)
  sens.append(dict(check_id='CROSS_FUNCTION_OUTSIDE_NAMESAKE_LOO',scope='WHOLE23_LOO',activity='ACT_DEPLOYMENT',n_owned=n,n_namesake=n_name,n_outside=n_out,share_outside=share,removed_company=c))
  n,n_name,n_out,share=owned_outside('ACT_RESEARCH',members)
  sens.append(dict(check_id='CROSS_FUNCTION_OUTSIDE_NAMESAKE_LOO',scope='WHOLE23_LOO',activity='ACT_RESEARCH',n_owned=n,n_namesake=n_name,n_outside=n_out,share_outside=share,removed_company=c))
  n,n_name,n_out,share=owned_outside('ACT_QUALITY',members)
  sens.append(dict(check_id='CROSS_FUNCTION_OUTSIDE_NAMESAKE_LOO',scope='WHOLE23_LOO',activity='ACT_QUALITY',n_owned=n,n_namesake=n_name,n_outside=n_out,share_outside=share,removed_company=c))
 # unknown bounds for co-occurrence: unresolved all non-positive vs all positive
 for row in co_sum:
  if row['scope']!='WHOLE23':continue
  P=iint(row['n_unconditional']);U=iint(row['n_unresolved']);B=iint(row['n_assessable']);Z=B-P-U
  sens.append(dict(check_id='COOCCURRENCE_UNKNOWN_BOUNDS',scope='WHOLE23',activity=row['pair_id'],n_owned=P,n_namesake=U,n_outside=Z,share_outside='',removed_company='',bound_nonpositive=ratio(P,B),bound_positive=ratio(P+U,B),main_share=row['share_unconditional'],note='Unknown bounds assign unresolved ads; not a confidence interval'))
 table('D9_sensitivity.csv',sens)

 # D10 T6 structured conclusions with computed numbers
 def pick(cid,scope='ALL24'):
  return next(r for r in headline if r['activity_code']==cid)
 h_res,h_dep,h_qual=pick('ACT_RESEARCH'),pick('ACT_DEPLOYMENT'),pick('ACT_QUALITY')
 g1c=g1['companies'] if g1 else [];g2c=g2['companies'] if g2 else []
 def co(pid):return next(r for r in co_sum if r['scope']=='ALL24' and r['pair_id']==pid)
 t6=[]
 loo_dep=[r for r in sens if r['check_id']=='CROSS_FUNCTION_OUTSIDE_NAMESAKE_LOO' and r['activity']=='ACT_DEPLOYMENT']
 loo_res=[r for r in sens if r['check_id']=='CROSS_FUNCTION_OUTSIDE_NAMESAKE_LOO' and r['activity']=='ACT_RESEARCH']
 loo_q=[r for r in sens if r['check_id']=='CROSS_FUNCTION_OUTSIDE_NAMESAKE_LOO' and r['activity']=='ACT_QUALITY']
 def loo_rng(rows):
  xs=[ffloat(r['share_outside']) for r in rows];return min(xs),max(xs)
 t6.append(dict(conclusion_id='T6_Q3_CROSS_FUNCTION',q='Q3',candidate='研究/部署/质量活动主要落在同名主职能之外，说明活动与主职能测量不同内容',final_wording='',scope='ALL24 1,654 ads; activity-assessable 1,623',n_companies=24,n_ads=1654,metric='OWNED activity ads outside namesake primary / OWNED activity ads',n_positive='',n_unknown=0,n_base='',status='CONSISTENT_UNDER_CHECKED_SCOPES',sensitivity_json='',counterexample='',alternative='不是原分类错误，也不直接证明跨部门协同',remaining='无非具身对照；广告≠人数'))
 t6.append(dict(conclusion_id='T6_Q1_COMPOSITION_VS_TASK',q='Q1',candidate='公司间部署活动差异若主要来自部署职能占比，则是构成现象；若同职能内仍不同，则是任务安排差异',final_wording='',scope='whole-company 23 plus two case groups',n_companies=23,n_ads=1630,metric='deployment-function share vs owned deployment-activity rate, including rate inside non-deployment functions',n_positive='',n_unknown='',n_base='',status='',sensitivity_json='',counterexample='',alternative='招聘板覆盖、多产品范围、观察批次',remaining='统一权重只在合格共同职能内解释'))
 t6.append(dict(conclusion_id='T6_Q2_SAME_ROLE_TASK',q='Q2',candidate='同为ML/AI或软件岗位时，企业公开要求的交付对象不同；技能共现不等于用于该任务',final_wording='',scope='whole-company ML 156 / software 180; case points for selected companies',n_companies='',n_ads='',metric='fixed display DUTY_OWN_DEVELOP UNCONDITIONAL and GENERAL UNCONDITIONAL',n_positive='',n_unknown='',n_base='',status='',sensitivity_json='',counterexample='',alternative='正文模板和渠道详略',remaining='Q2仅两个代表职能'))
 # fill wording after numbers
 sc_res=next(r for r in sens if r['check_id']=='CROSS_FUNCTION_OUTSIDE_NAMESAKE' and r['scope']=='SOURCE_COMPLETE' and r['activity']=='ACT_RESEARCH')
 sc_dep=next(r for r in sens if r['check_id']=='CROSS_FUNCTION_OUTSIDE_NAMESAKE' and r['scope']=='SOURCE_COMPLETE' and r['activity']=='ACT_DEPLOYMENT')
 sc_q=next(r for r in sens if r['check_id']=='CROSS_FUNCTION_OUTSIDE_NAMESAKE' and r['scope']=='SOURCE_COMPLETE' and r['activity']=='ACT_QUALITY')
 w23_res=next(r for r in sens if r['check_id']=='CROSS_FUNCTION_OUTSIDE_NAMESAKE' and r['scope']=='WHOLE23' and r['activity']=='ACT_RESEARCH')
 w23_dep=next(r for r in sens if r['check_id']=='CROSS_FUNCTION_OUTSIDE_NAMESAKE' and r['scope']=='WHOLE23' and r['activity']=='ACT_DEPLOYMENT')
 w23_q=next(r for r in sens if r['check_id']=='CROSS_FUNCTION_OUTSIDE_NAMESAKE' and r['scope']=='WHOLE23' and r['activity']=='ACT_QUALITY')
 rmin,rmax=loo_rng(loo_res);dmin,dmax=loo_rng(loo_dep);qmin,qmax=loo_rng(loo_q)
 t6[0]['final_wording']=(f"在1,623条活动可判读广告中，本人承担研究探索{h_res['n_owned']}条，其中同名研究科学主职能{h_res['n_namesake']}条，其他具体职能{h_res['n_other_concrete']}条、结构类{h_res['n_structure']}条、未明确{h_res['n_unspecified']}条，同名之外{float(h_res['share_outside_namesake'])*100:.1f}%。"
  f"部署与维护{h_dep['n_owned']}条，同名部署职能{h_dep['n_namesake']}条，其他具体{h_dep['n_other_concrete']}、结构{h_dep['n_structure']}、未明确{h_dep['n_unspecified']}，同名之外{float(h_dep['share_outside_namesake'])*100:.1f}%。"
  f"质量验证{h_qual['n_owned']}条，同名制造质量供应{h_qual['n_namesake']}条，其他具体{h_qual['n_other_concrete']}、结构{h_qual['n_structure']}、未明确{h_qual['n_unspecified']}，同名之外{float(h_qual['share_outside_namesake'])*100:.1f}%。"
  f"整公司23与来源较完整子集方向一致（研究{float(w23_res['share_outside'])*100:.1f}%/{float(sc_res['share_outside'])*100:.1f}%，部署{float(w23_dep['share_outside'])*100:.1f}%/{float(sc_dep['share_outside'])*100:.1f}%，质量{float(w23_q['share_outside'])*100:.1f}%/{float(sc_q['share_outside'])*100:.1f}%）。"
  f"逐一剔除公司后，研究同名之外{rmin*100:.1f}–{rmax*100:.1f}%，部署{dmin*100:.1f}–{dmax*100:.1f}%，质量{qmin*100:.1f}–{qmax*100:.1f}%。"
  "这是测量范围不同，不是把原主职能判错。")
 t6[0]['n_positive']=f"{h_res['n_owned']}|{h_dep['n_owned']}|{h_qual['n_owned']}"
 t6[0]['sensitivity_json']=json.dumps({'ALL24':[h_res['share_outside_namesake'],h_dep['share_outside_namesake'],h_qual['share_outside_namesake']],'WHOLE23':[w23_res['share_outside'],w23_dep['share_outside'],w23_q['share_outside']],'SOURCE_COMPLETE':[sc_res['share_outside'],sc_dep['share_outside'],sc_q['share_outside']],'LOO_research':[rmin,rmax],'LOO_deployment':[dmin,dmax],'LOO_quality':[qmin,qmax]},ensure_ascii=False)
 t6[0]['counterexample']='研究科学主职能32条中仍有27条本人承担研究探索，同名职能不是空集；FAR团队研究科学9/24，剔除后研究活动总量下降但同名之外比例仍高。'
 eq_out=next(r for r in sens if r['check_id']=='DEPLOYMENT_ACTIVITY_OUTSIDE_FUNCTION_EQUAL' and r['scope']=='WHOLE23')
 eq_fn=next(r for r in sens if r['check_id']=='DEPLOYMENT_FUNCTION_SHARE_EQUAL' and r['scope']=='WHOLE23')
 eq_act=next(r for r in sens if r['check_id']=='DEPLOYMENT_ACTIVITY_OVERALL_EQUAL' and r['scope']=='WHOLE23')
 # case specifics
 def dep_row(c):return next(r for r in decomp if r['company_id']==c)
 txt=[]
 if g1:
  a,b=g1['companies'];ra,rb=dep_row(a),dep_row(b)
  txt.append(f"制造实际使用组{cb[a]['company_name']}与{cb[b]['company_name']}：部署职能占比分别为{float(ra['share_deployment_function'])*100:.1f}%与{float(rb['share_deployment_function'])*100:.1f}%，部署活动率{float(ra['share_deployment_activity'])*100:.1f}%与{float(rb['share_deployment_activity'])*100:.1f}%，非部署职能内部署活动率{float(ra['share_deployment_activity_outside_deployment_function'])*100:.1f}%与{float(rb['share_deployment_activity_outside_deployment_function'])*100:.1f}%。共同职能K={g1['K']}，统一权重比较资格为{g1['unified']}。")
 if g2:
  a,b=g2['companies'];ra,rb=dep_row(a),dep_row(b)
  txt.append(f"物流交付责任组{cb[a]['company_name']}与{cb[b]['company_name']}：供给形态分别为{cb[a]['stratum_name']}与{cb[b]['stratum_name']}。部署职能占比{float(ra['share_deployment_function'])*100:.1f}%与{float(rb['share_deployment_function'])*100:.1f}%，部署活动率{float(ra['share_deployment_activity'])*100:.1f}%与{float(rb['share_deployment_activity'])*100:.1f}%，非部署职能内{float(ra['share_deployment_activity_outside_deployment_function'])*100:.1f}%与{float(rb['share_deployment_activity_outside_deployment_function'])*100:.1f}%。K={g2['K']}，统一权重{g2['unified']}。")
 t6[1]['final_wording']=(f"整公司范围内，部署职能占比的公司等权均值为{float(eq_fn['share_outside'])*100:.1f}%，本人承担部署活动率均值为{float(eq_act['share_outside'])*100:.1f}%，非部署主职能内部的部署活动率均值为{float(eq_out['share_outside'])*100:.1f}%。总体部署活动明显高于部署职能构成，两类差异并存。"
  +''.join(txt)+
  "统一权重结果只解释共同覆盖职能内的差异，不能写成商业模式贡献率。物流组未达共同职能门槛时保留点值、不补零。")
 t6[1]['status']='CONSISTENT_UNDER_CHECKED_SCOPES'
 t6[1]['counterexample']='若只看部署职能招聘，会低估多数公司广告中的部署活动；Boston Dynamics与Nimble部署职能占比较高，属于构成与活动同时偏高的样本，不是反例而是并存。'
 t6[1]['alternative']='渠道覆盖、多产品招聘板、批次与临时招聘结构均可影响职能占比；本阶段不把供给组差写成国家效应。'
 t3agg=read(IN/'stage_c'/'tables'/'T3_aggregates.csv')
 def agg(role,label,metric='DUTY_OWN_DEVELOP',branch='UNCONDITIONAL',group='WHOLE23'):
  return next(r for r in t3agg if r['group']==group and r['role_code']==role and r['label_name']==label and r['metric_bucket']==metric and r['branch_bucket']==branch)
 ms,mf,md=agg('RF_ML_AI_ENGINEERING','训练推理系统'),agg('RF_ML_AI_ENGINEERING','基础模型/VLA'),agg('RF_ML_AI_ENGINEERING','数据管线与资产')
 rel,rt=agg('RF_ROBOTICS_SOFTWARE','可靠性'),agg('RF_ROBOTICS_SOFTWARE','实时系统')
 mlj='; '.join(f"{r['name_a']}×{r['name_b']} {r['n_positive_joint']}/{r['n_interpretable']} (U={r['n_unknown']})" for r in ml_pairs)
 t6[2]['final_wording']=(f"整公司ML/AI工程156条：训练推理系统本人开发独立条目{ms['n_positive']}/{ms['n_interpretable']}（未知{ms['n_relation_unknown']}），基础模型/VLA {mf['n_positive']}/{mf['n_interpretable']}（未知{mf['n_relation_unknown']}），数据管线{md['n_positive']}/{md['n_interpretable']}（未知{md['n_relation_unknown']}）。"
  f"软件与平台180条：可靠性开发{rel['n_positive']}/{rel['n_interpretable']}，实时系统{rt['n_positive']}/{rt['n_interpretable']}。可靠性开发不自动等于客户现场交付。"
  f"ML三项本人开发独立条目两两共现：{mlj}。共现只支持同广告出现；无用途连接时不写成该技能用于该任务。"
  + (f"案例组Q2点值见D7，仅解释{', '.join(cb[c]['company_name'] for c in g1c)}等入选公司，不外推。" if g1c else ''))
 t6[2]['status']='CONSISTENT_UNDER_CHECKED_SCOPES'
 t6[2]['n_ads']='156+180 whole-company representative roles'
 t6[2]['counterexample']='PyTorch一般要求独立与示例不相加；工具出现不能当作硬性要求。Field AI占跨本体软件组过大，该组软件均值失去许可。'
 t6[2]['alternative']='模板段落和渠道详略会改变技能可见度；来源较完整子集已锁定，不按正文长度校正任务数量。'
 table('T6_conclusions.csv',t6)

 # Q2 unknown bound control from protocol
 ctrl=[]
 for role,label,p,u,b in [('RF_ML_AI_ENGINEERING','Python',60,23,156),('RF_ROBOTICS_SOFTWARE','Linux',70,3,180),('RF_ROBOTICS_SOFTWARE','C++',42,30,180),('RF_ROBOTICS_SOFTWARE','Python',35,15,180)]:
  r=agg(role,label,'GENERAL','UNCONDITIONAL')
  ctrl.append(dict(role_code=role,label=label,n_positive=r['n_positive'],n_unknown=r['n_relation_unknown'],n_base=r['n_base'],n_interpretable=r['n_interpretable'],bound_low=ratio(iint(r['n_positive']),iint(r['n_base'])),bound_high=ratio(iint(r['n_positive'])+iint(r['n_relation_unknown']),iint(r['n_base'])),protocol_p=p,protocol_u=u,protocol_b=b,match_protocol='YES' if iint(r['n_positive'])==p and iint(r['n_relation_unknown'])==u and iint(r['n_base'])==b else 'NO'))
 table('D9_q2_unknown_bound_control.csv',ctrl)

 summary=dict(n_ads=1654,n_companies=24,source_complete=sorted(scset),g1=g1,g2=g2,headline=headline,cooccurrence=[dict(r) for r in co_sum if r['scope']=='ALL24'],ml_pairs=ml_pairs,t6_ids=[r['conclusion_id'] for r in t6],table_rows={p.name:len(read(p)) for p in sorted(T.glob('*.csv')) if not p.name.endswith('_plot_data.csv') and p.name!='T5_case_profile.csv'},researcher=js(IN/'decisions'/'researcher.json'))
 dump(ROOT/'summary.json',summary)
 print(json.dumps({'g1':g1,'g2':g2,'n_tables':len(summary['table_rows']),'research_outside':h_res['share_outside_namesake'],'deploy_outside':h_dep['share_outside_namesake'],'quality_outside':h_qual['share_outside_namesake']},ensure_ascii=False))
if __name__=='__main__':main()
