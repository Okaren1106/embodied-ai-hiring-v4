from common import *
import re
lock_check()
caseinfo=json.loads((ROOT/'evidence/case_selection.json').read_text(encoding='utf-8'));cases=caseinfo['cases'];CASE={c:case['case_id'] for case in cases for c in case['companies']};cs=list(CASE)
facts=read(B/'company_facts.csv');ev=read(B/'company_evidence.csv');assertions=json.loads((ROOT/'evidence/responsibility_assertions.json').read_text(encoding='utf-8'))
summary=[];metrics=[];gaps=[]
for c in ALL:
 co=CO[c];ff=[f for f in facts if f['company_id']==c];pids=ids([c]);ai=pids&admitted
 summary.append({**co,'case_id':CASE.get(c,''),'astra_status':'TARGETED_EVIDENCE_READ' if c in CASE else 'INHERITED_B_AND_RULES_NO_NEW_SEARCH','inherited_fact_n':len(ff),'inherited_evidence_n':len([e for e in ev if e['company_id']==c]),'responsibility_status':'PRODUCT_SCENE_ROWS_SEE_T5' if c in CASE else 'NOT_NEWLY_MAPPED','comparison_qualification':next(case['reason'] for case in cases if c in case['companies']) if c in CASE else '未入选有限案例；保留全样本分布和候选记录','remaining_gap':'招聘板全渠道覆盖未确认；各产品/合同收入与维保分工未知；公司招聘不可全归给案例产品','source_quality_note':'正文可判读与招聘板覆盖分开；资历见332广告附表' if c in CASE else '沿用B/C来源状态','metrics_path':'tables/T5_company_metric_long.csv'})
 for a in ACTS:
  metrics.append({'company_id':c,'case_id':CASE.get(c,''),'family':'ACTIVITY_OWNED','indicator':a,'P':len(ai&OWN[a]),'N':len(ai),'B':len(pids),'U':len(pids-ai),'rate':ratio(len(ai&OWN[a]),len(ai)),'lineage':'inputs/stage_c/tables/T4_activity_lineage.csv'})
 for r in ROLES:metrics.append({'company_id':c,'case_id':CASE.get(c,''),'family':'PRIMARY_ROLE','indicator':r,'P':sum(role(J[k])==r for k in pids),'N':len(pids),'B':len(pids),'U':0,'rate':ratio(sum(role(J[k])==r for k in pids),len(pids)),'lineage':'inputs/stage_c/tables/T2_ad_lineage.csv'})
 for question in ['各产品客户现场部署责任','持续运营责任','维护支持合同分工','招聘板全部渠道覆盖']:
  gaps.append({'company_id':c,'question':question,'status':'TARGETED_SEARCH_REMAINING_UNCERTAINTY' if c in CASE else 'INHERITED_NOT_TARGETED_THIS_ROUND','checked_channels':'B原事实与证据；所选官方公司/客户/合作方原文，见责任长表与web检索快照' if c in CASE else 'B/C封存资料及固定场景表','opposing_evidence':'智元客户承担工艺与现场管理；银河维保是计划；Dexterity仅现场验证；Nimble自营不等于所有员工执行维护' if c in CASE else '未开展新增定向核验','decision':'不推定合同分工；已知范围外保留未知','search_log':'evidence/web_*.json' if c in CASE else ''})
dump('T5_company_background_job_link.csv',summary);dump('T5_company_metric_long.csv',metrics);dump('T5_inherited_fact_long.csv',[f|{'case_id':CASE.get(f['company_id'],''),'inheritance':'B_SEALED_UNCHANGED'} for f in facts]);dump('T5_key_gaps.csv',gaps)
ares=[]
for i,r in enumerate(assertions,1):
 ares.append({'assertion_id':f'ASTRA_R{i:02}',**r,'case_id':CASE[r['company_id']],'read_date':'2026-09-16','hiring_observation':'2026-09-11','time_applicability':'PUBLIC_BEFORE_HIRING_OBSERVATION','time_note':'历史事实的公开日期早于招聘观察日；不推定观察日仍按相同规模运行','fact_vs_interpretation':'来源可支持的有限责任判断','linked_activity_metric':'ACT_DEPLOYMENT;ACT_ENGINEERING;ACT_QUALITY','ad_n':CO[r['company_id']]['n_ads'],'activity_N':len(ids([r['company_id']],True)),'comparison_unit':'COMPANY_CASE_CONTEXT_NOT_AD_INDEPENDENT_OBSERVATIONS'})
dump('T5_responsibility_long.csv',ares)
src={}
for r in ares:src[r['evidence_id']]={k:r[k] for k in ['evidence_id','source_url','publication_date','source_nature','read_date']}|{'source_capture':'evidence/web_*.json; inputs/stage_b/evidence_snapshots for inherited IDs'}
dump('T5_evidence_register.csv',list(src.values()))
obj=[]
for rid,objtype,quote,note in json.loads((ROOT/'evidence/ad_object_decisions.json').read_text(encoding='utf-8')):
 k=next(k for k,j in J.items() if j['reading_id']==rid);s=RAW[k];found=False
 for f in ['duties','full_description','requirements']:
  t=s.get(f) or '';start=t.find(quote)
  if start>=0:found=True;break
 assert found,(rid,quote)
 obj.append({'identity_key':k,'reading_id':rid,'company_id':J[k]['company_id'],'case_id':CASE[J[k]['company_id']],'role':role(J[k]),'title':J[k]['title'],'work_object':objtype,'quote':quote,'field':f,'start':start,'end':start+len(quote),'interpretation':note,'source_url':J[k]['source_url'],'text_version_hash':J[k]['text_version_hash'],'activity_codes_json':js([a for a in ACTS if k in OWN[a]]),'reviewer':'Astra','status':'BOUNDED_CASE_TEXT_READING_NO_RECLASSIFICATION'})
dump('T5_case_work_object_evidence.csv',obj)
# All candidate pairs keep background eligibility and reasons, without using outcome differences.
scene=read(C/'inputs/rules_v1/company_scene_assertions.csv');observed=collections.defaultdict(set)
for r in scene:
 if r['state']=='OBSERVED_USE':observed[r['company_id']].add(r['scene'])
cand=[]
for r in read(ROOT/'tables/case_candidate_coverage.csv'):
 c1,c2=r['company1'],r['company2'];shared=observed[c1]&observed[c2];pair={c1,c2};chosen=next((x for x in cases if set(x['companies'])==pair),None)
 reason=chosen['reason'] if chosen else '未进入至多两组案例；保留基础覆盖'
 if not chosen:
  if r['same_wave']!='True':reason='观察批次不一致，优先同批次案例'
  elif not shared:reason='无共同已记录实际使用场景；目标、演示和未知不等同实际使用'
  elif r['known_multiproduct']=='True':reason='既定全公司多产品边界，产品场景不能分配全部广告'
  elif r['standardization_eligible']!='True':reason='共同职能不足，未优先纳入定量案例；服务责任对照另按定向主题选择'
  else:reason='供给或业务边界不同，不在本轮制造同供给或物流服务对照主题内'
 for e in caseinfo['exclusions']:
  if set(e['pair'])==pair:reason=e['reason']
 cand.append(r|{'common_observed_scenes_json':js(sorted(shared)),'case_id':chosen['case_id'] if chosen else '', 'selected':bool(chosen),'selection_reason':reason})
dump('T5_case_selection_all_pairs.csv',cand)
# Explicit audience sensitivity; wording is extracted, never imputed from age/seniority.
exclude=set();aud=[]
for k in sorted(ids(cs)):
 title=J[k]['title'];s=RAW[k];txt=(s.get('full_description') or '')+'\n'+(s.get('requirements') or '')
 mm=re.search(r'20[23]\d\s*届|应届毕业生|应届生',txt);titleflag=bool(re.search('实习|intern|校招|届',title,re.I))
 if titleflag or mm:exclude.add(k);aud.append({'identity_key':k,'reading_id':J[k]['reading_id'],'company_id':J[k]['company_id'],'title':title,'title_explicit':titleflag,'audience_match':mm.group() if mm else '', 'match_context':txt[max(0,mm.start()-40):mm.end()+70] if mm else title,'decision':'EXCLUDE_EXPLICIT_CAMPUS_OR_INTERNSHIP_SENSITIVITY_ONLY'})
dump('case_explicit_campus_internship.csv',aud)
noaud=[];std=[]
for case in cases:
 c1,c2=case['companies'];ss={c:ids([c],True)-exclude for c in [c1,c2]};K=[r for r in CONCRETE if all(sum(role(J[k])==r for k in ss[c])>=10 for c in ss)]
 for c in [c1,c2]:
  for a in ACTS:noaud.append({'case_id':case['case_id'],'company_id':c,'activity':a,'P':len(ss[c]&OWN[a]),'N':len(ss[c]),'rate':ratio(len(ss[c]&OWN[a]),len(ss[c])),'excluded_ads':len(ids([c])&exclude),'n_common_K':len(K),'standardization_eligible':len(K)>=2})
 for a in ACTS:
  vals={c:statistics.mean([ratio(len({k for k in ss[c] if role(J[k])==r}&OWN[a]),sum(role(J[k])==r for k in ss[c])) for r in K]) if len(K)>=2 else None for c in ss}
  std.append({'case_id':case['case_id'],'activity':a,'K_json':js(K),'n_common_K':len(K),'eligible':len(K)>=2,'rate1':vals[c1],'rate2':vals[c2],'company1':c1,'company2':c2,'reason':'逐格重新核对N10及K>=2；不把未经标记者称为正式社招'})
dump('case_audience_activity_sensitivity.csv',noaud);dump('case_audience_standardization.csv',std)
q2points=read(C/'tables/T3_company_context.csv');dump('T5_case_Q2_all_fixed_contexts.csv',[r|{'case_id':CASE[r['company_id']]} for r in q2points if r['company_id'] in cs and r['main_display']=='YES'])
print('T5',len(summary),'responsibilities',len(ares),'work_objects',len(obj),'audience',collections.Counter(r['company_id'] for r in aud));print('NON TITLE AUDIENCE',[(r['reading_id'],r['match_context']) for r in aud if not r['title_explicit']]);print('AUDIENCE_K',[(r['case_id'],r['K_json']) for r in std if r['activity']=='ACT_DEPLOYMENT'])
