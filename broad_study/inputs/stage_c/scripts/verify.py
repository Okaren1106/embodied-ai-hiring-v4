"""Checks against sealed upstream sources, independent aggregations, semantic boundaries."""
from analyze import *
import math
CHECKS=[]
def check(name,condition,detail=''):
 CHECKS.append(dict(name=name,passed=bool(condition),detail=detail))
 if not condition:raise AssertionError(name+': '+str(detail))
def eq(x,y):return abs(float(x)-float(y))<1e-8
def main():
 check_inputs();check('184_locked_inputs',len(js(ROOT/'input_lock.json')['files'])==184)
 j=read(A/'jobs.csv');ji={r['identity_key']:r for r in j};cs=read(R/'company_classification.csv');cb={r['company_id']:r for r in cs};whole={c for c in cb if cb[c]['scope_main_company']=='YES'}
 check('unique_1654_ads_24_entities',len(j)==len(ji)==1654 and len(cb)==24)
 check('country_counts',Counter(r['country'] for r in j)=={'China':963,'US':691})
 check('two_observation_waves',Counter(r['observation_date'] for r in j)=={'2026-08-31':610,'2026-09-11':1044})
 q=read(T/'T2_company_primary_roles.csv');old=read(A/'T2_company_primary_roles.csv');oldidx={(r['company_id'],r['class_code']):r for r in old}
 for r in q:
  prior=oldidx[r['company_id'],r['class_code']]
  for newkey,oldkey in [('n_ads','n_ads'),('denominator_all','denominator_all'),('denominator_coded','denominator_coded'),('n_coded','n_in_coded_subset')]:assert int(r[newkey])==int(prior[oldkey])
  assert abs(float(r['share_all'])-float(prior['share_all']))<1e-6
 check('528_q1_cells_match_accepted_A',len(q)==528)
 for c in cb:
  rows=[r for r in q if r['company_id']==c];assert sum(int(r['n_ads']) for r in rows)==int(cb[c]['n_ads']);assert abs(sum(float(r['share_all']) for r in rows)-1)<1e-8
 check('q1_company_totals_and_shares',True)
 qa=read(T/'T2_aggregates.csv')
 for r in qa:
  members=set(cb) if r['scope']=='ALL24' else whole if r['scope']=='WHOLE23' else {c for c in cb if cb[c]['stratum']==r['scope']}
  ads=[a for a in j if a['company_id'] in members and (r['denominator_basis']=='ALL' or a['primary_status']=='CODED')];n=sum((a['primary_code'] if a['primary_status']=='CODED' else a['primary_status'])==r['class_code'] for a in ads)
  assert int(r['denominator'])==len(ads) and int(r['n_ads'])==n
  if r['share_ad_weighted']!='':assert eq(r['share_ad_weighted'],n/len(ads))
  else:assert r['denominator_basis']=='CODED' and r['class_kind']=='unspecified'
 check('q1_aggregates_recounted',len(qa)==308)
 spec=importlib.util.spec_from_file_location('frozen',R/'scripts/build_rules.py');fr=importlib.util.module_from_spec(spec);spec.loader.exec_module(fr)
 idx,roots,_=fr.requirement_index();rule=js(R/'decisions/q2_rules.json');ann=read(T/'T3_all_item_semantics.csv');lk={(r['identity_key'],r['dimension'],r['item_index']):r for r in ann}
 rawselected=[]
 for dim,file in [('skills','skills.csv'),('technical_concepts','technical_concepts.csv')]:
  for r in read(A/file):
   job=ji[r['identity_key']]
   if job['primary_status']!='CODED' or job['primary_code'] not in rule['primary_roles']:continue
   rawselected.append(r);out=lk[r['identity_key'],dim,r['item_index']];b,path=fr.branch(r,idx,roots,rule)
   m='SEPARATE_NOT_POSITIVE'
   for k,pair in rule['positive_buckets'].items():
    if [r['use'],r['mention_relation']]==pair and ((k.startswith('DUTY_') and r['context']=='DUTY') or (not k.startswith('DUTY_') and r['context']=='REQUIREMENT')):m=k
   assert out['candidate_metric']==m
   if b=='UNRESOLVED' or r['use'] in ['NEGATED','UNRESOLVED','BACKGROUND']:m='SEPARATE_NOT_POSITIVE'
   assert out['branch_bucket']==b and out['metric_bucket']==m and out['quote']==r['quote']
 check('5547_semantics_replayed_from_original_items',len(rawselected)==len(ann)==5547)
 check('frozen_item_interpretation_exact',sha(T/'T3_all_item_semantics.csv')==sha(R/'diagnostics/q2_item_interpretation.csv'))
 # Boundary fixtures use the fixed label function, test positive precedence and unknown isolation.
 unknown=dict(metric_bucket='SEPARATE_NOT_POSITIVE',candidate_metric='GENERAL',branch_bucket='UNRESOLVED',use='GENERAL_REQUIREMENT',mention_relation='EXPERIENCE_REQUIREMENT',context='REQUIREMENT')
 positive=unknown|dict(metric_bucket='GENERAL',branch_bucket='CHOICE')
 check('unknown_not_zero',fr.label_state([unknown],'GENERAL','UNCONDITIONAL')=='UNKNOWN')
 check('certain_positive_takes_precedence',fr.label_state([unknown,positive],'GENERAL','CHOICE')=='PRESENT')
 check('choice_not_unconditional',fr.label_state([positive],'GENERAL','UNCONDITIONAL')=='NO_RECORDED_POSITIVE')
 check('requirement_unknown_does_not_delete_duty',fr.label_state([unknown],'DUTY_OWN_USE','UNCONDITIONAL')=='NO_RECORDED_POSITIVE')
 check('empty_item_list_means_no_recorded_positive',fr.label_state([],'GENERAL','EXAMPLE')=='NO_RECORDED_POSITIVE')
 trace=read(T/'T3_positive_unknown_lineage.csv');tk=lambda r:(r['role_code'],r['dimension'],r['label_code'],r['metric_bucket'],r['branch_bucket'])
 ts=defaultdict(dict)
 for r in trace:
  key=tk(r);assert r['identity_key'] not in ts[key];ts[key][r['identity_key']]=r['state'];assert r['state'] in ['PRESENT','UNKNOWN']
 check('q2_trace_unique_valid_states',len(trace)==5466)
 adm=read(T/'T3_base_admission.csv');check('q2_admission_680_rows',len(adm)==680 and len({(r['identity_key'],r['dimension']) for r in adm})==680)
 check('UNMAPPED_retained',sum(r['dimension_status']=='UNMAPPED' and r['base_eligible']=='YES' for r in adm)==4)
 qc=read(T/'T3_company_context.csv');base=defaultdict(set)
 for r in adm:
  if r['base_eligible']=='YES':base[(r['role_code'],r['dimension'],r['company_id'])].add(r['identity_key'])
 for r in qc:
  ids=base[(r['role_code'],r['dimension'],r['company_id'])];state=ts[tk(r)];n=sum(state.get(a)=='PRESENT' for a in ids);u=sum(state.get(a)=='UNKNOWN' for a in ids);d=len(ids)-u
  assert (n,u,d,len(ids))==tuple(int(r[k]) for k in ['n_positive','n_relation_unknown','n_interpretable','n_base'])
  assert (r['share']=='' and not d) or (d and eq(r['share'],n/d))
  assert (r['small_n_under10']=='YES')==(0<d<10)
 check('38640_company_cells_reconciled_to_trace',len(qc)==38640)
 for r in read(R/'diagnostics/q2_label_interpretability.csv'):
  expected=set(json.loads(r['unknown_ad_ids_json']));actual={a for a,state in ts[tk(r)].items() if state=='UNKNOWN' and ji[a]['company_id'] in whole};assert expected==actual
 check('490_fixed_unknown_ad_sets_unchanged',True)
 agg=read(T/'T3_aggregates.csv');qi=defaultdict(list)
 for r in qc:qi[tk(r)].append(r)
 for r in agg:
  g=r['group'];members=whole if g=='WHOLE23' else set(cb) if g=='ALL24_TEAM_SENSITIVITY' else {c for c in cb if cb[c]['stratum']==g} if not g.startswith('SYSTEM_PRODUCTS_') else {c for c in cb if cb[c]['stratum']=='SYSTEM_PRODUCTS' and cb[c]['country']==g.removeprefix('SYSTEM_PRODUCTS_')}
  rows=[x for x in qi[tk(r)] if x['company_id'] in members];den=sum(int(x['n_interpretable']) for x in rows);num=sum(int(x['n_positive']) for x in rows);nc=sum(int(x['n_interpretable'])>0 for x in rows)
  assert (den,num,nc)==(int(r['n_interpretable']),int(r['n_positive']),int(r['n_companies']))
  passed=nc>=3 and den>=20;assert (r['gate']=='PASS')==passed
  if r['display_status']=='EXPLORATORY_SUMMARY':assert passed and eq(r['share_ad_weighted'],num/den) and eq(r['share_company_equal'],sum(float(x['share']) for x in rows if x['share']!='')/nc)
  else:assert r['share_ad_weighted']==r['share_company_equal']==''
 check('14490_group_cells_and_gates_recomputed',len(agg)==14490)
 modelml=[r for r in agg if r['group']=='CROSS_BODY_MODELS' and r['role_code']=='RF_ML_AI_ENGINEERING'];check('model_ML_points_only',all(r['display_status']=='CASE_POINTS_ONLY' for r in modelml))
 lo=read(T/'T3_leave_one_company_out.csv');field=[r for r in lo if r['group']=='CROSS_BODY_MODELS' and r['role_code']=='RF_ROBOTICS_SOFTWARE' and r['removed_company']=='US_FIELD_AI'];check('removing_Field_AI_invalidates_model_summary',len(field)>0 and all(r['gate']=='POINTS_ONLY' and r['share_company_equal']=='' for r in field))
 # All Q2 sensitivity rows independently recomputed from trace + source eligibility.
 for r in read(T/'T3_scope_sensitivity.csv'):
  ids=set().union(*(base[(r['role_code'],r['dimension'],c)] for c in whole));variant=r['variant']
  if variant=='CATALOG_DIRECT':ids={a for a in ids if ji[a]['skills_status' if r['dimension']=='skills' else 'technical_status']!='UNMAPPED'}
  if variant=='EXCLUDE_MULTI_PRODUCT':ids={a for a in ids if cb[ji[a]['company_id']]['known_multi_product']!='YES'}
  if variant=='EXCLUDE_MEDIA_ONLY':ids={a for a in ids if cb[ji[a]['company_id']]['media_only_basis']!='YES'}
  n=sum(ts[tk(r)].get(a)=='PRESENT' for a in ids);u=sum(ts[tk(r)].get(a)=='UNKNOWN' for a in ids)
  assert int(r['n_base'])==len(ids) and int(r['n_positive'])==n and int(r['n_interpretable'])==len(ids)-u
 check('1960_scope_sensitivity_cells_recomputed',True)
 acts=read(ROOT/'inputs/stage_a_extra/activities.csv');ps=defaultdict(set)
 for r in acts:ps[(r['label_code'],r['relation'])].add(r['identity_key']);ps[(r['label_code'],'ANY_RECORDED')].add(r['identity_key'])
 eligible={a for a,jj in ji.items() if jj['activities_status'] in ['CODED','NOT_MENTIONED','UNMAPPED']}
 check('activity_1623_assessable',len(eligible)==1623)
 check('activity_3236_source_rows_preserved',len(read(T/'T4_activity_lineage.csv'))==len(acts)==3236)
 for r in read(T/'T4_activity_company.csv'):
  ids={a for a in eligible if ji[a]['company_id']==r['company_id']};n=len(ids&ps[(r['label_code'],r['relation'])]);assert int(r['n_positive'])==n and int(r['n_assessable'])==len(ids) and eq(r['share'],n/len(ids))
 check('576_activity_company_cells_recounted',True)
 for r in read(T/'T4_activity_aggregates.csv'):
  ids={a for a in eligible if r['scope']=='ALL24' or ji[a]['company_id'] in whole};assert int(r['n_positive'])==len(ids&ps[(r['label_code'],r['relation'])]) and int(r['n_assessable'])==len(ids)
 check('48_activity_aggregates_recounted',True)
 check('engineering_overlap_not_added',len(ps['ACT_ENGINEERING','OWNED'])==957 and len(ps['ACT_ENGINEERING','PARTICIPATES'])==205 and len(ps['ACT_ENGINEERING','ANY_RECORDED'])==1034 and len(ps['ACT_ENGINEERING','OWNED']&ps['ACT_ENGINEERING','PARTICIPATES'])==128)
 check('research_activity_distinct_from_role',len(ps['ACT_RESEARCH','OWNED'])==75 and sum(ji[a]['primary_code']=='RF_ML_AI_ENGINEERING' for a in ps['ACT_RESEARCH','OWNED'])==36 and sum(ji[a]['primary_code']=='RF_RESEARCH_SCIENCE' for a in ps['ACT_RESEARCH','OWNED'])==27)
 trees=read(T/'T4_role_structures.csv');nodes=read(T/'T4_role_structure_nodes.csv');original={r['identity_key']:r for r in (json.loads(x) for x in (A/'relations.jsonl').read_text(encoding='utf-8').splitlines()) if r['kind']=='role_structure'}
 for r in trees:
  raw=original[r['identity_key']]['tree_json'];raw=json.loads(raw) if isinstance(raw,str) else raw;assert json.loads(r['tree_json'])==raw
 check('30_trees_verbatim_preserved',len(trees)==30 and Counter(r['root_relation'] for r in trees)=={'ALL':19,'OR':11})
 check('118_nodes_87_role_nodes',len(nodes)==118 and sum(r['relation']=='ROLE' for r in nodes)==87)
 statuses=Counter(r['duties_status'] or r['duty_status'] for r in nodes if r['relation']=='ROLE');check('role_duty_status_preserved',statuses=={'DESCRIBED':75,'NOT_EXPANDED':12},dict(statuses))
 mixed=[r for r in trees if r['has_mixed_branch']=='YES'];check('N0396_nested_choice_retained',len(mixed)==1 and mixed[0]['reading_id']=='N0396' and mixed[0]['root_relation']=='OR')
 check('structures_excluded_from_Q2',not ({r['identity_key'] for r in trees}&{r['identity_key'] for r in adm}))
 for f in js(ROOT/'figure_manifest.json'):
  assert (ROOT/f['png']).is_file() and (ROOT/f['svg']).is_file() and read(ROOT/f['plot_data'])
 check('10_figures_have_png_svg_and_exact_data',len(js(ROOT/'figure_manifest.json'))==10)
 dump(ROOT/'verification/data_checks.json',dict(n_checks=len(CHECKS),n_pass=sum(c['passed'] for c in CHECKS),n_fail=sum(not c['passed'] for c in CHECKS),checks=CHECKS));print(json.dumps({'n_checks':len(CHECKS),'passed':sum(c['passed'] for c in CHECKS)},ensure_ascii=False))
if __name__=='__main__':main()
