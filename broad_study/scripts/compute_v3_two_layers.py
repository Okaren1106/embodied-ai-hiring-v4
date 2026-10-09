"""Task-matched mentions, requirement forms, and bounded sensitivities.
No context counts are added as if mutually exclusive; every count is ad-deduped.
"""
from astra_review_tools import *
AD={a['identity_key']:a for a in read(ROOT/'tables/Q3_ads_final.csv')}
CD={x['code']:x for x in json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))['labels']}
EV=defaultdict(list)
for e in read(ROOT/'tables/Q3_evidence_final.csv'):
 if e.get('excluded_from_catalog')!='True':EV[e['identity_key'],e['code']].append(e)
metrics=['DUTY_OWN_USE','DUTY_OWN_DEVELOP','REQUIRED','GENERAL','PREFERRED']
limits=defaultdict(list)
for t in transactions():limits[t['identity_key']].extend(t.get('source_limits',[]))
def flags(k,c):
 ee=EV[k,c];affirm=[e for e in ee if e['metric'] in metrics]
 # Known term / context, even if its list/slash branch remains unresolved.
 mention=bool(affirm)
 incomplete=any((c in t['codes'] or t['codes']=='ALL_APPLICABLE' or 'ALL_APPLICABLE' in t['codes']) and set(t['metrics'])&set(metrics) for t in limits[k])
 na=bool(DOC[k].get('not_applicable',{}).get(c))
 unknown=any(e['metric']=='UNKNOWN' for e in ee)
 st='P' if mention else 'SOURCE_EXCLUDED' if incomplete else 'NA' if na else 'U' if unknown else 'Z'
 out={s:int(st==s) for s in ['P','U','Z','SOURCE_EXCLUDED','NA']}
 out['clear_relation_mention']=int(any(e['branch']!='UNRESOLVED' for e in affirm))
 out['has_unresolved_branch']=int(any(e['branch']=='UNRESOLVED' for e in affirm))
 for m in metrics:
  out[m]=int(any(e['metric']==m for e in affirm))
  out[m+'_UNCONDITIONAL']=int(any(e['metric']==m and e['branch']=='UNCONDITIONAL' for e in affirm))
 for b in ['CHOICE','EXAMPLE','CHOICE_AND_EXAMPLE','CONDITIONAL']:
  out[b]=int(any(e['branch']==b for e in affirm))
 out['DUTY_ANY']=int(any(e['metric'].startswith('DUTY_') for e in affirm))
 out['DUTY_RESOLVED']=int(any(e['metric'].startswith('DUTY_') and e['branch']!='UNRESOLVED' for e in affirm))
 # This is an intentionally broad contact upper scenario, NOT owned competence.
 contact=[e for e in ee if e['metric']=='SEPARATE' and any(w in e['branch'] for w in ['PARTICIPAT','COLLABORAT','SUPPORT'])]
 out['DUTY_PLUS_COLLAB_CONTACT']=int(bool(contact) or bool(out['DUTY_ANY']))
 out['CONTACT_ONLY']=int(bool(contact) and not bool(out['DUTY_ANY']))
 out['BACKGROUND_OR_OTHER_ONLY']=int(bool(ee) and not mention and not unknown)
 return out
focus={'RF_ML_AI_ENGINEERING':'ROBOT_MODEL','RF_ROBOTICS_SOFTWARE':'ROBOT_RUNTIME','RF_HARDWARE_ELECTRICAL':'BOARD_CIRCUIT'}
scope=defaultdict(set)
for r in read(ROOT/'tables/Q4_scope_membership.csv'):scope[r['scope']].add(r['identity_key'])
rows=[];pts=[];membership=[];loo=[]
def summarize(ks,c):
 pp=[]
 for co in sorted({AD[k]['company_id'] for k in ks}):
  kk=[k for k in ks if AD[k]['company_id']==co];vv=[flags(k,c) for k in kk]
  x={z:sum(v[z] for v in vv) for z in vv[0]};x['company_id']=co;x['total_ads']=len(kk)
  x['N']=x['P']+x['Z'];x['B']=x['N']+x['U']
  x['share']=ratio(x['P'],x['N']);x['unknown_low']=ratio(x['P'],x['B']);x['unknown_high']=ratio(x['P']+x['U'],x['B']);x['small_n']='YES' if 0<x['N']<10 else 'NO'
  pp.append(x)
 names=[z for z in pp[0] if z not in ['company_id','share','unknown_low','unknown_high','small_n']] if pp else []
 a={z:sum(p[z] for p in pp) for z in names};valid=[p for p in pp if p['N']>0]
 a.update(n_companies=len(valid),n_positive_companies=sum(p['P']>0 for p in pp))
 gate=len(valid)>=3 and a.get('N',0)>=20;a['gate']='EXPLORATORY_SUMMARY' if gate else 'POINTS_ONLY'
 a['share_ad_weighted']=ratio(a.get('P',0),a.get('N',0)) if gate else None
 a['share_company_equal']=statistics.mean(p['share'] for p in valid) if gate else None
 a['unknown_low']=ratio(a.get('P',0),a.get('B',0)) if gate else None;a['unknown_high']=ratio(a.get('P',0)+a.get('U',0),a.get('B',0)) if gate else None
 a['max_positive_contribution']=ratio(max((p['P'] for p in pp),default=0),a.get('P',0))
 return a,pp
for role,task in focus.items():
 primary={k for k,a in AD.items() if a['role']==role and a['task']==task and a['company_id'] in WHOLE}
 extended={k for k,a in AD.items() if a['role']==role and task in [a['task'],a['secondary_task']] and a['company_id'] in WHOLE}
 scenarios={'PRIMARY':primary,'PLUS_SECONDARY':extended,'DEDUP_PRIMARY':primary&scope['DEDUPE_EXACT_DUTIES'],'NO_CAMPUS_PRIMARY':primary&scope['EXCLUDE_EXPLICIT_CAMPUS_INTERN']}
 codes=sorted(c for c,d in CD.items() if role in d['applicable_roles'])
 for scen,ks in scenarios.items():
  membership.extend(dict(scenario=scen,role=role,task=task,identity_key=k,reading_id=AD[k]['reading_id'],company_id=AD[k]['company_id']) for k in sorted(ks))
  for c in codes:
   base=dict(scenario=scen,role=role,task=task,label_code=c,label_name=CD[c]['name'],measurement_type=CD[c]['measurement_type'])
   a,pp=summarize(ks,c);rows.append(dict(base,**a));pts.extend(dict(base,**p) for p in pp)
   if scen=='PRIMARY' and a.get('P',0):
    for co in sorted({AD[k]['company_id'] for k in ks}):
     a2,_=summarize({k for k in ks if AD[k]['company_id']!=co},c)
     loo.append(dict(base,removed_company=co,**a2))
dump('tables/V3_two_layer_aggregates.csv',rows);dump('tables/V3_two_layer_company_points.csv',pts);dump('tables/V3_two_layer_membership.csv',membership);dump('tables/V3_two_layer_leave_one_company_out.csv',loo)
# Explicit evidence for every positive/ambiguous/contact record in the three tasks.
allkeys={r['identity_key'] for r in membership}
dump('tables/V3_two_layer_evidence.csv',[e for (k,c),ee in EV.items() if k in allkeys for e in ee])
save_json('verification/V3_two_layers.json',dict(status='COMPUTED',primary_ads={t:sum(a['task']==t and a['role']==r and a['company_id'] in WHOLE for a in AD.values()) for r,t in focus.items()},secondary_ads=sum(bool(a['secondary_task']) for a in AD.values()),aggregates=len(rows),points=len(pts),loo=len(loo),definition='L1可辨识本人职责或资格提及，含分支关系未解；UNKNOWN对象不算明确提及。L2按提及广告去重的各语境，可重叠；无条件子列另保留。协作联系是宽敏感性上界而非本人能力。'))
print('two layers',len(rows),len(pts),flush=True)
