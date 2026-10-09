"""Meaningful invariants and adversarial semantics; never reads the live research store."""
from pathlib import Path
import csv,json,hashlib,sys,tempfile
from collections import Counter,defaultdict
import build_rules as b
R=Path(__file__).resolve().parents[1]
def main():
 checks=[]
 def check(name,ok,detail=None):checks.append({'name':name,'passed':bool(ok),'detail':detail})
 def read(n):return json.loads((R/n).read_text(encoding='utf-8'))
 def rows(n):return list(csv.DictReader((R/n).open(encoding='utf-8-sig',newline='')))
 check('design_lock_present',(R/'design_lock.json').exists())
 try:b.verify_design();check('design_hashes_match',True)
 except Exception as e:check('design_hashes_match',False,str(e))
 try:n=b.verify_inputs();check('input_hashes_match',True,n)
 except Exception as e:check('input_hashes_match',False,str(e))
 cc=rows('company_classification.csv');sc=rows('company_scene_assertions.csv');sm=rows('company_scene_matrix.csv');jobs=rows('inputs/stage_a/jobs.csv');q=read('decisions/q2_rules.json')
 jb={j['identity_key']:j for j in jobs};cb={c['company_id']:c for c in cc};facts={f['fact_id']:f for f in rows('inputs/stage_b/company_facts.csv')}
 check('1654_unique_ad_versions',len(jobs)==len(jb)==1654)
 check('24_unique_company_decisions',len(cc)==len(cb)==24 and set(cb)=={j['company_id'] for j in jobs})
 check('company_ad_totals_match_frozen_jobs',all(int(c['n_ads'])==sum(j['company_id']==c['company_id'] for j in jobs) for c in cc))
 check('all_stratum_decisions_have_same_subject_fact_basis',all(c['basis_fact_ids'] and all(facts[f]['company_id']==c['company_id'] for f in c['basis_fact_ids'].split('|')) for c in cc))
 check('source_scope_team_separated',cb['US_AMAZON_FTR']['stratum']=='TEAM_SEPARATE' and cb['US_AMAZON_FTR']['scope_main_company']=='NO')
 check('component_portfolio_not_forced_into_system_group',cb['CN_PAXINI']['stratum']=='COMPONENT_SYSTEM_PORTFOLIO')
 check('operator_service_not_robot_sale',cb['US_NIMBLE']['stratum']=='ROBOT_OPERATED_SERVICE')
 check('PI_research_company_not_internal_team',cb['US_PHYSICAL_INTELLIGENCE']['stratum']=='CROSS_BODY_MODELS' and cb['US_PHYSICAL_INTELLIGENCE']['scope_main_company']=='YES')
 check('18_3_1_1_1_strata_counts',Counter(c['stratum'] for c in cc)==Counter({'SYSTEM_PRODUCTS':18,'CROSS_BODY_MODELS':3,'COMPONENT_SYSTEM_PORTFOLIO':1,'ROBOT_OPERATED_SERVICE':1,'TEAM_SEPARATE':1}))
 check('7_scene_matrix_cells_per_company',len(sm)==168 and len({(r['company_id'],r['scene']) for r in sm})==168)
 current={(r['company_id'],r['scene']) for r in sc if r['current_connection']=='YES'}
 check('future_demo_unknown_not_current',all(r['current_connection']=='NO' for r in sc if r['state'] in ['FUTURE_PLAN','LONG_TERM_GOAL','DEMONSTRATED_TASK','BACKGROUND_DATE_UNKNOWN','TEAM_BACKGROUND','END_USE_UNSPECIFIED']))
 check('current_scene_basis_passes_time',all(facts[f]['time_applicability'] in ['USABLE_AT_OBSERVATION','NOT_TIME_SENSITIVE'] for r in sc if r['current_connection']=='YES' for f in r['basis_fact_ids'].split('|')))
 check('galaxea_undated_research_not_current',('CN_GALAXEA','RESEARCH_EDUCATION') not in current)
 check('unitree_undated_inspection_not_current',('CN_UNITREE','FIELD_INSPECTION') not in current)
 check('spirit_home_long_term_not_current',('CN_SPIRITAI','HOME') not in current)
 check('pi_household_demo_not_market',('US_PHYSICAL_INTELLIGENCE','HOME') not in current)
 check('apptronik_future_markets_excluded',all(('US_APPTRONIK',s) not in current for s in ['HOME','HEALTHCARE_CARE','RETAIL_SERVICE']))
 check('donation_research_offer_distinguished',any(r['company_id']=='CN_NOETIX' and r['state']=='OBSERVED_DONATION' for r in sc) and any(r['company_id']=='CN_UNITREE' and r['state']=='OBSERVED_RESEARCH_USE' for r in sc) and any(r['company_id']=='CN_LIMX' and r['state']=='CURRENT_OFFER' for r in sc))
 check('unknown_not_negative_group',all(r['connection_status'] in ['CURRENT_CONNECTION','BACKGROUND_OR_FUTURE_ONLY','NOT_ESTABLISHED'] for r in sm))
 admission=rows('diagnostics/admission.csv');rd=rows('diagnostics/role_coverage.csv')
 check('all17_roles_diagnosed',len(rd)==17)
 check('1576_concrete_ads_two_dimensions',len(admission)==3152 and len({(r['identity_key'],r['dimension']) for r in admission})==3152)
 check('selected_role_counts_original',all(int(r['n_ads_all'])=={'RF_ML_AI_ENGINEERING':159,'RF_ROBOTICS_SOFTWARE':181}[r['role_code']] for r in rd if r['selected']=='YES'))
 check('selected_roles_pass_gates',sum(r['selected']=='YES' for r in rd)==2 and all(r['feasibility_gate']=='PASS' for r in rd if r['selected']=='YES'))
 check('unmapped_kept_source_unassessable_excluded',all(r['source_assessable']==('NO' if r['dimension_status']=='SOURCE_UNASSESSABLE' else 'YES') for r in admission))
 check('structural_roles_not_expanded_into_q2',all(jb[r['identity_key']]['primary_code']==r['role_code'] and jb[r['identity_key']]['primary_status']=='CODED' for r in admission))
 selected_ids={r['identity_key'] for r in admission if r['selected_q2_role']=='YES'}
 check('selected340_ads_with336_main_company_ads',len(selected_ids)==340 and len({r['identity_key'] for r in admission if r['selected_q2_role']=='YES' and r['main_company_scope']=='YES'})==336)
 # Synthetic cases cover branch nesting, absent nodes and semantics—not implementation mirrors.
 rootkey=('test-ad','root');leafkey=('test-ad','leaf');exkey=('test-ad','example')
 row={'identity_key':'test-ad','context':'REQUIREMENT','requirement_node_id':'leaf'}
 idx={rootkey:{'relation':'OR','parent_id':''},leafkey:{'relation':'ITEM','parent_id':'root'}};roots={rootkey:'ALL',leafkey:'ALL'}
 check('ancestor_OR_is_choice',b.branch(row,idx,roots,q)[0]=='CHOICE')
 idx[rootkey]={'relation':'EXAMPLE','parent_id':''}
 check('ancestor_example_not_unconditional',b.branch(row,idx,roots,q)[0]=='EXAMPLE')
 idx[rootkey]={'relation':'OR','parent_id':'example'};idx[exkey]={'relation':'EXAMPLE','parent_id':''};roots[exkey]='ALL'
 check('nested_choice_example_preserved',b.branch(row,idx,roots,q)[0]=='CHOICE_AND_EXAMPLE')
 idx[exkey]['relation']='UNRESOLVED'
 check('unresolved_ancestor_dominates',b.branch(row,idx,roots,q)[0]=='UNRESOLVED')
 check('missing_requirement_node_not_unconditional',b.branch(row,{}, {},q)[0]=='UNRESOLVED')
 unknown={'metric_bucket':'SEPARATE_NOT_POSITIVE','candidate_metric':'GENERAL','branch_bucket':'UNRESOLVED','use':'GENERAL_REQUIREMENT','mention_relation':'EXPERIENCE_REQUIREMENT','context':'REQUIREMENT'}
 certain={**unknown,'metric_bucket':'GENERAL','branch_bucket':'UNCONDITIONAL'}
 choice={**certain,'branch_bucket':'CHOICE'}
 check('unknown_relation_is_not_zero',b.label_state([unknown],'GENERAL','UNCONDITIONAL')=='UNKNOWN')
 check('known_positive_survives_other_unknown',b.label_state([unknown,certain],'GENERAL','UNCONDITIONAL')=='PRESENT')
 check('choice_not_both_required',b.label_state([choice],'GENERAL','UNCONDITIONAL')=='NO_RECORDED_POSITIVE' and b.label_state([choice],'GENERAL','CHOICE')=='PRESENT')
 check('empty_label_is_only_no_recorded_positive',b.label_state([],'GENERAL','UNCONDITIONAL')=='NO_RECORDED_POSITIVE')
 items=rows('diagnostics/q2_item_interpretation.csv');byitems=defaultdict(list)
 for r in items:byitems[(r['identity_key'],r['dimension'],r['label_code'])].append(r)
 check('unresolved_items_never_positive',all(r['positive_recorded_mention']=='NO' for r in items if r['branch_bucket']=='UNRESOLVED'))
 check('background_negated_not_positive',all(r['positive_recorded_mention']=='NO' for r in items if r['use'] in ['BACKGROUND','NEGATED','UNRESOLVED']))
 check('collaboration_not_personal_use',all(r['metric_bucket']=='SEPARATE_NOT_POSITIVE' for r in items if r['mention_relation'] in ['COLLABORATION_OBJECT','PRODUCT_DEFINITION_OBJECT','PROCUREMENT_OBJECT','RECRUITMENT_OBJECT','TEACHING_OBJECT']))
 raw_count=0
 for filename in ['skills.csv','technical_concepts.csv']:
  raw_count+=sum(r['identity_key'] in selected_ids for r in rows('inputs/stage_a/'+filename))
 check('all_selected_source_items_retained',len(items)==raw_count)
 avail=rows('diagnostics/q2_label_interpretability.csv');bad=[]
 for r in avail:
  ids=json.loads(r['unknown_ad_ids_json'])
  if len(ids)!=int(r['n_relation_unknown']) or int(r['n_interpretable_ads'])+len(ids)!=int(r['base_ads']):bad.append('count '+r['label_code'])
  if any(b.label_state(byitems[(ad,r['dimension'],r['label_code'])],r['metric_bucket'],r['branch_bucket'])!='UNKNOWN' for ad in ids):bad.append('not unknown '+r['label_code'])
 check('label_specific_unknown_denominators_consistent',not bad,bad[:10])
 check('unknown_identity_list_lossless_with_embedded_pipes',all(ad in jb for r in avail for ad in json.loads(r['unknown_ad_ids_json'])))
 dis=rows('q2_display_selection.csv');selected=[r for r in dis if r['main_display']=='YES']
 check('generic_labels_separate',all(r['label_code'] not in q['display_selection']['generic_skill_codes_separate'] for r in selected if r['dimension']=='skills'))
 check('selected_display_meets_coverage',all(int(r['n_companies'])>=5 and int(r['n_ads'])>=10 for r in selected))
 check('display_counts_10_9_tools_8_8_concepts',Counter((r['role_code'],r['dimension']) for r in selected)==Counter({('RF_ML_AI_ENGINEERING','skills'):10,('RF_ROBOTICS_SOFTWARE','skills'):9,('RF_ML_AI_ENGINEERING','technical_concepts'):8,('RF_ROBOTICS_SOFTWARE','technical_concepts'):8}))
 # Recount distinct ads from interpreted source items independently of displayed counters.
 bad=[]
 for r in dis:
  pairs={(i['identity_key'],i['company_id']) for i in items if i['role_code']==r['role_code'] and i['dimension']==r['dimension'] and i['label_code']==r['label_code'] and i['positive_recorded_mention']=='YES' and cb[i['company_id']]['scope_main_company']=='YES'}
  if len(pairs)!=int(r['n_ads']) or len({c for a,c in pairs})!=int(r['n_companies']):bad.append(r['label_code'])
 check('display_counts_are_unique_ads_and_companies',not bad,bad)
 grid=rows('diagnostics/group_role_coverage.csv');model=[r for r in grid if r['group']=='CROSS_BODY_MODELS' and r['dimension']=='skills']
 check('ml_model_group_below20_points_only',any(r['role_code']=='RF_ML_AI_ENGINEERING' and r['n_assessable_ads']=='17' and r['display_status']=='COMPANY_POINTS_ONLY' for r in model))
 check('software_model_group_concentration_flagged',any(r['role_code']=='RF_ROBOTICS_SOFTWARE' and r['n_assessable_ads']=='38' and r['dominance_warning']=='YES' for r in model))
 country=rows('diagnostics/country_coverage.csv')
 check('no_country_contrast_for_us_only_models',all(r['auxiliary_country_coverage_gate']=='NO_COUNTRY_CONTRAST' for r in country if r['group']=='CROSS_BODY_MODELS'))
 check('heterogeneous_scenes_case_only',all(r['display_status']=='HETEROGENEOUS_SCENE_CASES' for r in grid if r['group'] in ['SCENE_HOME','SCENE_HEALTHCARE_CARE','SCENE_FIELD_INSPECTION','SCENE_RESEARCH_EDUCATION']))
 ov=rows('diagnostics/scene_overlap.csv')
 check('overlapping_scenes_not_independent',all(r['independent_samples']=='NO' for r in ov if int(r['n_overlap'])>0))
 es=rows('evidence_index.csv')
 check('all56_basis_evidence_texts_preserved',len(es)==56 and all((R/e['local_text_path']).is_file() and b.sha(R/e['local_text_path'])==e['snapshot_sha256'] for e in es))
 # Adversarial lock probes use tiny isolated fixtures, never mutate original inputs or design.
 oldroot=b.ROOT
 with tempfile.TemporaryDirectory(prefix='q2-rule-lock-test-') as temp:
  tr=Path(temp).resolve();(tr/'inputs').mkdir();target=tr/'inputs/data.txt';target.write_text('original',encoding='utf-8')
  b.ROOT=tr;b.dump(tr/'inputs/source_lock.json',{'files':{'inputs/data.txt':{'bytes':8,'sha256':b.sha(target)}}})
  b.dump(tr/'design_lock.json',{'files':{'inputs/source_lock.json':{'sha256':b.sha(tr/'inputs/source_lock.json')}}})
  target.write_text('mutation',encoding='utf-8');rejected=False
  try:b.verify_inputs()
  except ValueError:rejected=True
  check('tampered_input_rejected',rejected)
  (tr/'inputs/source_lock.json').write_text('{}',encoding='utf-8');rejected=False
  try:b.verify_design()
  except ValueError:rejected=True
  check('relocked_input_requires_design_version_change',rejected)
  b.ROOT=oldroot
 check('no_group_skill_rate_results_claimed',read('diagnostics/summary.json')['role_rates_by_group_computed'] is False and read('comparison_registry.json')['no_outcome_contrasts_computed'] is True)
 # Local HTML hrefs must exist; anchors are checked against the 24 known company ids.
 import re
 html=(R/'index.html').read_text(encoding='utf-8');hrefs=re.findall(r'href="([^"]+)"',html)
 check('overview24_company_sections',len(re.findall(r'<section id=',html))==24)
 check('overview_local_links_resolve',all(h[1:] in cb if h.startswith('#') else (R/h).exists() for h in hrefs if not h.startswith('http') and h!='verification/result.json'))
 out={'n_checks':len(checks),'n_pass':sum(c['passed'] for c in checks),'n_fail':sum(not c['passed'] for c in checks),'validation_kind':'AUTHOR_SELF_VALIDATION_WITH_ADVERSARIAL_FIXTURES','checks':checks}
 b.dump(R/'verification/result.json',out)
 print(json.dumps({k:v for k,v in out.items() if k!='checks'}|{'failed':[c for c in checks if not c['passed']]},ensure_ascii=False))
 return bool(out['n_fail'])
if __name__=='__main__':raise SystemExit(main())
