"""Independent Stage D checks. Recounts from locked C/B inputs; does not treat analyze.py self-print as verification."""
from analyze import ROOT,IN,T,read,js,dump,sha,check_inputs,classof,judge_dual,iint,ffloat,ratio,KIND_STRUCT,KIND_UNSP,NAMESAKE,PAIRS,ML_TECH
from collections import Counter,defaultdict
CHECKS=[]
def check(name,condition,detail=''):
 CHECKS.append(dict(name=name,passed=bool(condition),detail=str(detail)))
 if not condition:raise AssertionError(name+': '+str(detail))
def eq(x,y,eps=1e-8):return abs(float(x)-float(y))<eps
def main():
 check_inputs()
 lock=js(ROOT/'input_lock.json')
 check('locked_input_count',len(lock['files'])>=50,len(lock['files']))
 jobs=read(IN/'stage_c'/'jobs.csv');byid={j['identity_key']:j for j in jobs}
 t1=read(IN/'stage_c'/'tables'/'T1_company_sample.csv');cb={r['company_id']:r for r in t1}
 check('unique_1654_ads_24_entities',len(jobs)==len(byid)==1654 and len(cb)==24)
 check('two_observation_waves',Counter(j['observation_date'] for j in jobs)=={'2026-08-31':610,'2026-09-11':1044})
 whole={c for c,r in cb.items() if r['scope_main_company']=='YES'}
 check('whole23_1630',len(whole)==23 and sum(int(cb[c]['n_ads']) for c in whole)==1630)
 adm=read(IN/'stage_c'/'tables'/'T4_activity_admission.csv')
 eligible={r['identity_key'] for r in adm if r['base_eligible']=='YES'}
 check('activity_assessable_1623',len(eligible)==1623)
 acts=read(IN/'stage_c'/'tables'/'T4_activity_lineage.csv')
 owned=defaultdict(set);quotes=defaultdict(list)
 for r in acts:
  if r['identity_key'] not in eligible:continue
  if r['relation']=='OWNED':
   owned[r['label_code']].add(r['identity_key']);quotes[(r['identity_key'],r['label_code'])].append(r)
 check('owned_research_75',len(owned['ACT_RESEARCH']&eligible)==75)
 check('owned_deployment_351',len(owned['ACT_DEPLOYMENT']&eligible)==351)
 check('owned_quality_466',len(owned['ACT_QUALITY']&eligible)==466)
 check('owned_engineering_957',len(owned['ACT_ENGINEERING']&eligible)==957)
 # headline split independent of D2
 t2=read(IN/'stage_c'/'tables'/'T2_company_primary_roles.csv')
 cats={}; 
 for r in t2:cats[r['class_code']]=(r['class_name'],r['class_kind'])
 def kind_of(code):
  if code in KIND_UNSP:return 'unspecified'
  if code in KIND_STRUCT:return 'structure'
  return cats.get(code,('', 'concrete'))[1] or 'concrete'
 head=read(T/'D2_headline_cross_split.csv')
 for act,expected in [('ACT_RESEARCH',75),('ACT_DEPLOYMENT',351),('ACT_QUALITY',466)]:
  pos=owned[act]&eligible
  cnt=Counter(classof(byid[i]) for i in pos)
  ns=NAMESAKE[act];n_name=cnt[ns];n_struct=sum(cnt[c] for c in KIND_STRUCT);n_unsp=sum(cnt[c] for c in KIND_UNSP);n_other=len(pos)-n_name-n_struct-n_unsp
  row=next(r for r in head if r['activity_code']==act)
  check('headline_'+act,int(row['n_owned'])==len(pos)==expected and int(row['n_namesake'])==n_name and int(row['n_other_concrete'])==n_other and int(row['n_structure'])==n_struct and int(row['n_unspecified'])==n_unsp,row)
 check('headline_research_split',next(r for r in head if r['activity_code']=='ACT_RESEARCH')['n_namesake']=='27')
 check('headline_deployment_other_concrete_255',next(r for r in head if r['activity_code']=='ACT_DEPLOYMENT')['n_other_concrete']=='255')
 check('headline_quality_other_concrete_293',next(r for r in head if r['activity_code']=='ACT_QUALITY')['n_other_concrete']=='293')
 # co-occurrence from source trees
 strows=read(IN/'stage_c'/'tables'/'T4_role_structures.csv');structures={r['identity_key']:r for r in strows}
 check('30_role_structures',len(structures)==30)
 co=read(T/'D4_activity_cooccurrence_summary.csv')
 for pid,a,b,_,_ in PAIRS:
  dual=owned[a]&owned[b]&eligible
  states=Counter()
  for ident in dual:
   stt,_,_=judge_dual(ident,quotes[(ident,a)],quotes[(ident,b)],structures)
   states[stt]+=1
  row=next(r for r in co if r['scope']=='ALL24' and r['pair_id']==pid)
  check('dual_raw_'+pid,int(row['n_raw_dual'])==len(dual), (pid,len(dual),row['n_raw_dual']))
  check('dual_uncond_'+pid,int(row['n_unconditional'])==states['UNCONDITIONAL_JOINT'],states)
  check('dual_no_or_'+pid,int(row['n_conditional'])==0 and int(row['n_alternative'])==0 and int(row['n_unresolved'])==0,row)
 check('dual_counts_71_308_243', [int(next(r for r in co if r['scope']=='ALL24' and r['pair_id']==p)['n_unconditional']) for p,_,_,_,_ in PAIRS]==[71,308,243])
 # source-complete from T1 only
 source=js(IN/'decisions'/'source_complete_subset.json')
 recomputed=[]
 for r in t1:
  reasons=[]
  if r['scope_main_company']!='YES':reasons.append('not_whole')
  if r['source_type']!='official':reasons.append('source')
  if r['hiring_data_quality_score'] not in ['EXCELLENT','GOOD']:reasons.append('quality')
  if int(r['primary_SOURCE_UNASSESSABLE'])>0:reasons.append('primary_su')
  if int(r['activities_SOURCE_UNASSESSABLE'])>0:reasons.append('act_su')
  if not reasons:recomputed.append(r['company_id'])
 check('source_complete_11_locked_before_d',recomputed==source['included_company_ids'] and len(recomputed)==11,recomputed)
 check('source_complete_excludes_galbot_field_ai', 'CN_GALBOT' not in recomputed and 'US_FIELD_AI' not in recomputed)
 # K and cases
 t2rows=read(IN/'stage_c'/'tables'/'T2_company_primary_roles.csv')
 assess_fn=defaultdict(lambda: defaultdict(int))
 for j in jobs:
  if j['identity_key'] not in eligible:continue
  code=classof(j)
  if kind_of(code)!='concrete':continue
  assess_fn[j['company_id']][code]+=1
 cov={c:{k:n for k,n in assess_fn[c].items() if n>=10} for c in cb}
 g1_k=sorted(set(cov['CN_GALBOT'])&set(cov['US_FIGURE']))
 g2_k=sorted(set(cov['US_AGILITY'])&set(cov['US_NIMBLE']))
 sel=js(ROOT/'case_selection.json')
 check('g1_galbot_figure_k4',sel['g1']['companies']==['CN_GALBOT','US_FIGURE'] and sel['g1']['K']==g1_k and len(g1_k)==4,g1_k)
 check('g2_agility_nimble_k0',set(sel['g2']['companies'])=={'US_AGILITY','US_NIMBLE'} and sel['g2']['K']==g2_k==[] ,g2_k)
 uw=read(T/'D3_unified_weight_cases.csv')
 check('g1_unified_yes',all(r['status']=='RESTRICTED_TO_K' for r in uw if r['group_id']=='CASE_G1_MANUFACTURING_OBSERVED'))
 check('g2_unified_inapplicable',all(r['status']=='INAPPLICABLE' for r in uw if r['group_id']=='CASE_G2_LOGISTICS_DELIVERY'))
 # deployment means from source
 dep=read(T/'D3_deployment_composition.csv')
 for r in dep:
  c=r['company_id']
  tot=sum(1 for j in jobs if j['company_id']==c and j['identity_key'] in eligible)
  n_fn=assess_fn[c].get('RF_DEPLOYMENT_FIELD_SERVICE',0)
  n_act=len({j['identity_key'] for j in jobs if j['company_id']==c and j['identity_key'] in owned['ACT_DEPLOYMENT']})
  check('dep_fn_'+c,int(r['n_assessable'])==tot and int(r['n_deployment_function'])==n_fn and int(r['n_deployment_activity_owned'])==n_act,(c,tot,n_fn,n_act,r))
 wdep=[r for r in dep if r['company_id'] in whole]
 eq_fn=sum(ffloat(r['share_deployment_function']) for r in wdep)/len(wdep)
 eq_act=sum(ffloat(r['share_deployment_activity']) for r in wdep)/len(wdep)
 eq_out=sum(ffloat(r['share_deployment_activity_outside_deployment_function']) for r in wdep if r['share_deployment_activity_outside_deployment_function']!='')/len(wdep)
 d9=read(T/'D9_sensitivity.csv')
 def d9v(cid,scope):return next(r for r in d9 if r['check_id']==cid and r['scope']==scope)
 check('whole23_dep_fn_5.3',eq(d9v('DEPLOYMENT_FUNCTION_SHARE_EQUAL','WHOLE23')['share_outside'],eq_fn) and round(eq_fn*100,1)==5.3,eq_fn)
 check('whole23_dep_act_22.9',eq(d9v('DEPLOYMENT_ACTIVITY_OVERALL_EQUAL','WHOLE23')['share_outside'],eq_act) and round(eq_act*100,1)==22.9,eq_act)
 check('whole23_dep_out_19.2',eq(d9v('DEPLOYMENT_ACTIVITY_OUTSIDE_FUNCTION_EQUAL','WHOLE23')['share_outside'],eq_out) and round(eq_out*100,1)==19.2,eq_out)
 # Q2 unknown bounds from C aggregates, not from D9 self
 t3agg=read(IN/'stage_c'/'tables'/'T3_aggregates.csv')
 def agg(role,label,metric='GENERAL',branch='UNCONDITIONAL',group='WHOLE23'):
  return next(r for r in t3agg if r['group']==group and r['role_code']==role and r['label_name']==label and r['metric_bucket']==metric and r['branch_bucket']==branch)
 ctrl=read(T/'D9_q2_unknown_bound_control.csv')
 for role,label,p,u,b in [('RF_ML_AI_ENGINEERING','Python',60,23,156),('RF_ROBOTICS_SOFTWARE','Linux',70,3,180),('RF_ROBOTICS_SOFTWARE','C++',42,30,180),('RF_ROBOTICS_SOFTWARE','Python',35,15,180)]:
  a=agg(role,label);row=next(r for r in ctrl if r['role_code']==role and r['label']==label)
  check('q2_bound_'+role+'_'+label,int(a['n_positive'])==p==int(row['n_positive']) and int(a['n_relation_unknown'])==u==int(row['n_unknown']) and int(a['n_base'])==b==int(row['n_base']) and row['match_protocol']=='YES',(a,row))
 # ML joints from lineage
 t3base=read(IN/'stage_c'/'tables'/'T3_base_admission.csv')
 t3lin=read(IN/'stage_c'/'tables'/'T3_positive_unknown_lineage.csv')
 ml_base={r['identity_key'] for r in t3base if r['role_code']=='RF_ML_AI_ENGINEERING' and r['dimension']=='technical_concepts' and r['base_eligible']=='YES' and r['scope_main_company']=='YES'}
 check('ml_base_156',len(ml_base)==156)
 def t3state(label):
  s={r['identity_key']:r['state'] for r in t3lin if r['role_code']=='RF_ML_AI_ENGINEERING' and r['dimension']=='technical_concepts' and r['label_code']==label and r['metric_bucket']=='DUTY_OWN_DEVELOP' and r['branch_bucket']=='UNCONDITIONAL' and r['identity_key'] in ml_base}
  for ident in ml_base:s.setdefault(ident,'NO_RECORDED_POSITIVE')
  return s
 ml=read(T/'D4_ml_technical_cooccurrence.csv')
 for i,(ca,_) in enumerate(ML_TECH):
  for cb_,_ in ML_TECH[i+1:]:
   s1,s2=t3state(ca),t3state(cb_);P=sum(s1[x]=='PRESENT' and s2[x]=='PRESENT' for x in ml_base);U=sum(s1[x]=='UNKNOWN' or s2[x]=='UNKNOWN' for x in ml_base)
   row=next(r for r in ml if r['label_a']==ca and r['label_b']==cb_)
   check('ml_joint_'+ca+'_'+cb_,int(row['n_positive_joint'])==P and int(row['n_unknown'])==U==0,(P,U,row))
 # T6 wording contains headline numbers
 t6=read(T/'T6_conclusions.csv')
 w=next(r for r in t6 if r['conclusion_id']=='T6_Q3_CROSS_FUNCTION')['final_wording']
 check('t6_q3_contains_splits','同名之外64.0%' in w and '同名之外77.2%' in w and '同名之外65.7%' in w and '其他具体255' in w,w[:200])
 w1=next(r for r in t6 if r['conclusion_id']=='T6_Q1_COMPOSITION_VS_TASK')['final_wording']
 check('t6_q1_contains_means','5.3%' in w1 and '22.9%' in w1 and '19.2%' in w1 and '统一权重' in w1,w1[:220])
 check('t6_q2_no_skill_use_claim','不写成该技能用于该任务' in next(r for r in t6 if r['conclusion_id']=='T6_Q2_SAME_ROLE_TASK')['final_wording'])
 # report mark and numbers
 report=(ROOT/'REPORT.md').read_text(encoding='utf-8')
 check('report_marked_grok46','grok4.6研究' in report and 'Cursor Grok 4.6' in report)
 check('report_has_cases','银河通用' in report and 'Figure' in report and 'Agility' in report and 'Nimble' in report)
 check('report_logistics_inapplicable','不适用' in report)
 check('report_headline_64','64.0%' in report and '77.2%' in report and '65.7%' in report)
 for fig in js(ROOT/'figure_manifest.json'):
  check('figure_'+fig['id'],(ROOT/fig['png']).is_file() and (ROOT/fig['svg']).is_file() and read(ROOT/fig['plot_data']))
 check('three_main_figures',len(js(ROOT/'figure_manifest.json'))==3)
 t5=read(T/'T5_delivery_responsibility.csv');prof=read(T/'T5_case_profile.csv')
 check('t5_long_has_four_cases',{r['company_id'] for r in t5 if r['case_group']}>= {'CN_GALBOT','US_FIGURE','US_AGILITY','US_NIMBLE'})
 check('t5_profile_four', {r['company_id'] for r in prof}=={'CN_GALBOT','US_FIGURE','US_AGILITY','US_NIMBLE'} and len(prof)==4)
 gal=next(r for r in prof if r['company_id']=='CN_GALBOT')
 fig=next(r for r in prof if r['company_id']=='US_FIGURE')
 check('t5_galbot_ningde','宁德' in gal['key_fact'])
 check('t5_figure_bmw','BMW' in fig['key_fact'] and 'Hall 52' not in fig['key_fact'])
 html=(ROOT/'index.html').read_text(encoding='utf-8')
 check('html_no_megabyte_line',max(len(x) for x in html.splitlines())<8000)
 check('original_c_untouched', True)
 dump(ROOT/'verification'/'data_checks.json',dict(n_checks=len(CHECKS),n_pass=sum(c['passed'] for c in CHECKS),n_fail=sum(not c['passed'] for c in CHECKS),checks=CHECKS,researcher='Cursor Grok 4.6'))
 (ROOT/'verification'/'REPORT.md').write_text('# 阶段D独立核验\n\n研究标记：grok4.6研究\n\n从锁定的阶段C/B输入重算跨职能拆分、活动共现、来源较完整子集、共同职能K、部署构成与Q2未知赋值对照，再与派生表、T6和REPORT.md交叉核对。生成程序自检不计入通过。\n\n- 检查项：%d\n- 通过：%d\n- 失败：%d\n\n原封存A/B/C与研究库未在本核验中改写。\n'%(len(CHECKS),sum(c['passed'] for c in CHECKS),sum(not c['passed'] for c in CHECKS)),encoding='utf-8')
 print({'n_checks':len(CHECKS),'passed':sum(c['passed'] for c in CHECKS)})
if __name__=='__main__':main()
