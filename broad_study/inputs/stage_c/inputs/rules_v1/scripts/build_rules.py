"""Read-only derivation from locked inputs and explicit analyst decisions. No network or model calls."""
from pathlib import Path
import csv,json,hashlib
from collections import Counter,defaultdict
ROOT=Path(__file__).resolve().parents[1]
def readj(p):return json.loads(p.read_text(encoding='utf-8'))
def readcsv(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
def dump(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def table(p,rows,fields=None):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rows[0]));w.writeheader();w.writerows(rows)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def verify_inputs():
 d=readj(ROOT/'inputs/source_lock.json')
 for rel,e in d['files'].items():
  p=ROOT/rel
  if not p.is_file() or sha(p)!=e['sha256'] or p.stat().st_size!=e['bytes']:raise ValueError('INPUT_DRIFT: '+rel)
 return len(d['files'])
def verify_design():
 p=ROOT/'design_lock.json'
 if not p.exists():return
 for rel,e in readj(p)['files'].items():
  q=ROOT/rel
  if not q.is_file() or sha(q)!=e['sha256']:raise ValueError('DESIGN_DRIFT: '+rel)
def requirement_index():
 idx={};rootrels={};counts=Counter()
 for line in (ROOT/'inputs/stage_a/relations.jsonl').open(encoding='utf-8'):
  r=json.loads(line)
  if r['kind']!='requirement_group':continue
  for n in r['nodes']:
   key=(r['identity_key'],n['node_id'])
   if key in idx and idx[key]!=n:raise ValueError('Conflicting requirement node: '+str(key))
   idx[key]=n;rootrels[key]=r['root_relation'];counts[n['relation']]+=1
 return idx,rootrels,counts
def branch(row,idx,roots,rule):
 if row['context']!='REQUIREMENT':return 'UNCONDITIONAL',[]
 node=row['requirement_node_id'];ad=row['identity_key'];seen=set();rels=[]
 if not node:return 'UNRESOLVED',['MISSING_NODE_ID']
 while node:
  if node in seen:return 'UNRESOLVED',['CYCLE']
  seen.add(node);key=(ad,node)
  if key not in idx:return 'UNRESOLVED',['MISSING_NODE']
  n=idx[key];rels.append(n['relation']);rels.append(roots[key]);node=n['parent_id']
 known={'ALL','ITEM','OR','OR_EQUIVALENT','SOME_OF','EXAMPLE','UNRESOLVED'}
 if set(rels)-known:raise ValueError('Unknown requirement relation '+str(set(rels)-known))
 if 'UNRESOLVED' in rels:return 'UNRESOLVED',sorted(set(rels))
 choice=bool(set(rels)&set(rule['branch_logic']['choice_relations']));example='EXAMPLE' in rels
 return ('CHOICE_AND_EXAMPLE' if choice and example else 'CHOICE' if choice else 'EXAMPLE' if example else 'UNCONDITIONAL'),sorted(set(rels))
def label_state(items,metric,branch_bucket):
 # A certain positive is enough; uncertainty about another occurrence cannot erase it.
 if any(r['metric_bucket']==metric and r['branch_bucket']==branch_bucket for r in items):return 'PRESENT'
 for r in items:
  ambiguous_use=r['use']=='UNRESOLVED' or r['mention_relation']=='UNRESOLVED' or r['context']=='UNCERTAIN'
  relevant_context=(metric.startswith('DUTY_') and r['context'] in ['DUTY','UNCERTAIN']) or (not metric.startswith('DUTY_') and r['context'] in ['REQUIREMENT','UNCERTAIN'])
  if relevant_context and (ambiguous_use or (r['candidate_metric']==metric and r['branch_bucket']=='UNRESOLVED')):return 'UNKNOWN'
 return 'NO_RECORDED_POSITIVE'
def main():
 verify_design();n_inputs=verify_inputs();A=ROOT/'inputs/stage_a';B=ROOT/'inputs/stage_b'
 supply=readj(ROOT/'decisions/supply_classification.json');scenes=readj(ROOT/'decisions/scene_classification.json');rule=readj(ROOT/'decisions/q2_rules.json')
 facts={r['fact_id']:r for r in readcsv(B/'company_facts.csv')};evidence={r['evidence_id']:r for r in readcsv(B/'company_evidence.csv')}
 profiles={r['company_id']:r for r in readcsv(B/'company_profile.csv')};links=readcsv(B/'evidence_links.csv')
 jobs=readcsv(A/'jobs.csv');byjob={r['identity_key']:r for r in jobs}
 assert len(byjob)==len(jobs)==1654
 assert set(profiles)=={r['company_id'] for r in jobs}
 roles={r['class_code']:r['class_name'] for r in readcsv(A/'T2_company_primary_roles.csv') if r['class_kind']=='concrete'}
 assert len(roles)==17
 def basis(ids,c):
  fs=[facts[i] for i in ids];assert fs and all(f['company_id']==c for f in fs)
  es=sorted({e for f in fs for e in f['evidence_ids'].split('|') if e})
  assert all(e in evidence for e in es)
  return fs,es
 classification=[];prov=[];used_evidence=set()
 for r in supply['companies']:
  c=r['company_id'];p=profiles[c];fs,es=basis(r['basis_fact_ids'],c);used_evidence.update(es)
  if r['stratum']!='TEAM_SEPARATE':
   assert all(f['time_applicability'] in ['USABLE_AT_OBSERVATION','NOT_TIME_SENSITIVE'] for f in fs)
   assert all(f['value_status'] not in ['UNKNOWN','NOT_YET_SEARCHED','CONFLICT','SEARCHED_NOT_FOUND'] for f in fs)
  classification.append({'company_id':c,'company_name':p['company_name'],'country':p['country'],'n_ads':p['n_ads_inherited'],'observation_date':p['observation_date'],'scope':p['entity_scope_inherited'],'stratum':r['stratum'],'stratum_name':supply['groups'][r['stratum']]['name'],'comparison_use':supply['groups'][r['stratum']]['use'],'scope_main_company':'NO' if r['stratum']=='TEAM_SEPARATE' else 'YES','known_multi_product':'YES' if 'MULTI_PRODUCT' in p['entity_scope_inherited'] else 'NO','media_only_basis':'YES' if all(f['value_status']=='MEDIA_STATEMENT' for f in fs) else 'NO','basis_fact_ids':'|'.join(r['basis_fact_ids']),'basis_evidence_ids':'|'.join(es),'decision_reason':r['decision_reason'],'caveat':r['caveat']})
  for f in fs:prov.append({'decision_type':'SUPPLY','company_id':c,'decision_value':r['stratum'],'fact_id':f['fact_id'],'selected_claim':r['decision_reason'],'fact_value':f['value'],'value_status':f['value_status'],'time_applicability':f['time_applicability'],'evidence_ids':f['evidence_ids']})
 assert len(classification)==len({r['company_id'] for r in classification})==24
 cb={r['company_id']:r for r in classification};table(ROOT/'company_classification.csv',classification)
 scene_rows=[];members=defaultdict(set);actual=defaultdict(set)
 for i,r in enumerate(scenes['assignments'],1):
  c=r['company_id'];fs,es=basis(r['basis_fact_ids'],c);used_evidence.update(es)
  positive=r['state'] in scenes['membership_positive_states']
  if positive:
   assert all(f['time_applicability'] in ['USABLE_AT_OBSERVATION','NOT_TIME_SENSITIVE'] for f in fs),(c,r)
   assert cb[c]['stratum']!='TEAM_SEPARATE'
   members[r['scene']].add(c)
   if r['state'] in ['OBSERVED_USE','OBSERVED_DONATION','OBSERVED_RESEARCH_USE']:actual[r['scene']].add(c)
  scene_rows.append({'scene_decision_id':f'SC{i:03d}','company_id':c,'company_name':profiles[c]['company_name'],'scene':r['scene'],'scene_name':scenes['scenes'][r['scene']],'state':r['state'],'current_connection':'YES' if positive else 'NO','basis_fact_ids':'|'.join(r['basis_fact_ids']),'basis_evidence_ids':'|'.join(es),'selected_claim':r['selected_claim'],'decision_reason':r['decision_reason']})
  for f in fs:prov.append({'decision_type':'SCENE','company_id':c,'decision_value':r['scene']+'|'+r['state'],'fact_id':f['fact_id'],'selected_claim':r['selected_claim'],'fact_value':f['value'],'value_status':f['value_status'],'time_applicability':f['time_applicability'],'evidence_ids':f['evidence_ids']})
 assert {r['company_id'] for r in scene_rows}==set(profiles)
 table(ROOT/'company_scene_assertions.csv',scene_rows);table(ROOT/'decision_provenance.csv',prov)
 scene_matrix=[]
 for c in sorted(profiles):
  for s in scenes['scenes']:
   if s=='UNSPECIFIED':continue
   relevant=[r for r in scene_rows if r['company_id']==c and r['scene']==s]
   scene_matrix.append({'company_id':c,'scene':s,'connection_status':'CURRENT_CONNECTION' if c in members[s] else 'BACKGROUND_OR_FUTURE_ONLY' if relevant else 'NOT_ESTABLISHED','states':'|'.join(sorted({r['state'] for r in relevant})),'decision_ids':'|'.join(r['scene_decision_id'] for r in relevant),'absence_interpretation':'NOT_ESTABLISHED is not confirmed absence'})
 table(ROOT/'company_scene_matrix.csv',scene_matrix)
 table(ROOT/'evidence_index.csv',[{'evidence_id':eid,'company_id':evidence[eid]['company_id'],'title':evidence[eid]['source_title'],'url':evidence[eid]['url'],'claim_nature':evidence[eid]['claim_nature'],'publication_date':evidence[eid]['publication_date'],'capture_medium':evidence[eid]['capture_medium'],'source_text_path':evidence[eid]['snapshot_text_path'],'local_text_path':'inputs/evidence_snapshots/'+Path(evidence[eid]['snapshot_text_path'].replace('\\','/')).name,'snapshot_sha256':evidence[eid]['snapshot_sha256']} for eid in sorted(used_evidence)])
 # Role coverage without calculating any business-group or country outcome rate.
 admissible={'CODED','NOT_MENTIONED','UNMAPPED'};allowed=admissible|{'SOURCE_UNASSESSABLE'}
 concrete=[j for j in jobs if j['primary_status']=='CODED' and j['primary_code'] in roles]
 assert len(concrete)==1576
 admission=[]
 for j in concrete:
  for dimension,statusfield in [('skills','skills_status'),('technical_concepts','technical_status')]:
   status=j[statusfield]
   if status not in allowed:raise ValueError('Unknown dimension status '+status)
   admission.append({'identity_key':j['identity_key'],'record_id':j['record_id'],'reading_id':j['reading_id'],'company_id':j['company_id'],'role_code':j['primary_code'],'dimension':dimension,'dimension_status':status,'source_assessable':'YES' if status in admissible else 'NO','catalog_direct_subset':'YES' if status in ['CODED','NOT_MENTIONED'] else 'NO','selected_q2_role':'YES' if j['primary_code'] in rule['primary_roles'] else 'NO','main_company_scope':cb[j['company_id']]['scope_main_company'],'reason':'RECORDED_CATALOG_COVERAGE_WITH_UNMAPPED_RETAINED' if status in admissible else 'SOURCE_UNASSESSABLE'})
 table(ROOT/'diagnostics/admission.csv',admission)
 role_diag=[];company_role=[]
 for code,name in roles.items():
  rj=[j for j in concrete if j['primary_code']==code];cnt=Counter(j['company_id'] for j in rj);whole=[j for j in rj if cb[j['company_id']]['scope_main_company']=='YES'];wc=Counter(j['company_id'] for j in whole)
  row={'role_code':code,'role_name':name,'n_ads_all':len(rj),'n_companies_all':len(cnt),'n_ads_main_companies':len(whole),'n_main_companies':len(wc),'n_main_companies_ge5':sum(n>=5 for n in wc.values()),'n_main_companies_ge10':sum(n>=10 for n in wc.values())}
  for dimension,sf in [('skills','skills_status'),('technical_concepts','technical_status')]:
   states=Counter(j[sf] for j in rj)
   for status in sorted(allowed):row[dimension+'_'+status]=states[status]
   row[dimension+'_source_assessable_share']=round(sum(j[sf] in admissible for j in whole)/len(whole),6) if whole else 0
  g=rule['role_feasibility_gates'];passed=len(whole)>=g['min_ads'] and len(wc)>=g['min_companies'] and row['n_main_companies_ge5']>=g['min_companies_with_5_ads'] and all(row[d+'_source_assessable_share']>=g['min_dimension_source_assessable_share'] for d in ['skills','technical_concepts'])
  row.update({'feasibility_gate':'PASS' if passed else 'BELOW_GATE','selected':'YES' if code in rule['primary_roles'] else 'NO'})
  if row['selected']=='YES' and not passed:raise ValueError('Selected role below fixed gate '+code)
  role_diag.append(row)
  for c in sorted(profiles):
   cj=[j for j in rj if j['company_id']==c]
   rec={'company_id':c,'role_code':code,'role_name':name,'stratum':cb[c]['stratum'],'n_ads':len(cj),'small_n_under10':'YES' if len(cj)<10 else 'NO'}
   for d,sf in [('skills','skills_status'),('technical_concepts','technical_status')]:
    rec[d+'_assessable']=sum(j[sf] in admissible for j in cj);rec[d+'_unmapped']=sum(j[sf]=='UNMAPPED' for j in cj);rec[d+'_source_unassessable']=sum(j[sf]=='SOURCE_UNASSESSABLE' for j in cj)
   company_role.append(rec)
 table(ROOT/'diagnostics/role_coverage.csv',role_diag);table(ROOT/'diagnostics/company_role_coverage.csv',company_role)
 # Resolve requirement ancestors before selecting display labels. Keep all source items.
 idx,roots,relation_counts=requirement_index();item_rows=[];positive_sets=defaultdict(set);label_names={};item_summary=Counter()
 for dimension,filename in [('skills','skills.csv'),('technical_concepts','technical_concepts.csv')]:
  for r in readcsv(A/filename):
   if r['identity_key'] not in byjob:raise ValueError('Orphan tag')
   j=byjob[r['identity_key']]
   if j['primary_status']!='CODED' or j['primary_code'] not in rule['primary_roles']:continue
   bb,path=branch(r,idx,roots,rule);metric='SEPARATE_NOT_POSITIVE'
   for k,pair in rule['positive_buckets'].items():
    if [r['use'],r['mention_relation']]==pair and ((k.startswith('DUTY_') and r['context']=='DUTY') or (not k.startswith('DUTY_') and r['context']=='REQUIREMENT')):metric=k
   candidate_metric=metric
   if bb=='UNRESOLVED' or r['use'] in ['NEGATED','UNRESOLVED','BACKGROUND']:metric='SEPARATE_NOT_POSITIVE'
   positive=metric!='SEPARATE_NOT_POSITIVE'
   item_summary[(dimension,metric,bb)]+=1
   label_names[(dimension,r['label_code'])]=r['label_name']
   item_rows.append({'identity_key':r['identity_key'],'record_id':r['record_id'],'reading_id':r['reading_id'],'company_id':r['company_id'],'role_code':j['primary_code'],'dimension':dimension,'item_index':r['item_index'],'label_code':r['label_code'],'label_name':r['label_name'],'context':r['context'],'use':r['use'],'mention_relation':r['mention_relation'],'requirement_node_id':r['requirement_node_id'],'ancestor_relations':'|'.join(path),'branch_bucket':bb,'candidate_metric':candidate_metric,'metric_bucket':metric,'positive_recorded_mention':'YES' if positive else 'NO','quote':r['quote']})
   if positive and cb[j['company_id']]['scope_main_company']=='YES':positive_sets[(j['primary_code'],dimension,r['label_code'])].add((r['identity_key'],r['company_id']))
 table(ROOT/'diagnostics/q2_item_interpretation.csv',item_rows)
 display=[]
 for code in rule['primary_roles']:
  for dim in ['skills','technical_concepts']:
   items=[]
   for (role,d,label),pairs in positive_sets.items():
    if role==code and d==dim:items.append({'role_code':code,'dimension':dim,'label_code':label,'label_name':label_names[(dim,label)],'n_companies':len({c for a,c in pairs}),'n_ads':len({a for a,c in pairs})})
   items.sort(key=lambda r:(-r['n_companies'],-r['n_ads'],r['label_code']));rank=0
   for item in items:
    generic=dim=='skills' and item['label_code'] in rule['display_selection']['generic_skill_codes_separate']
    eligible=not generic and item['n_companies']>=rule['display_selection']['min_distinct_companies'] and item['n_ads']>=rule['display_selection']['min_distinct_ads']
    if eligible:rank+=1
    limit=rule['display_selection']['skill_limit' if dim=='skills' else 'technical_limit']
    item.update({'generic_separate':'YES' if generic else 'NO','coverage_eligible':'YES' if eligible else 'NO','eligible_rank':rank if eligible else '', 'main_display':'YES' if eligible and rank<=limit else 'NO'})
    display.append(item)
 table(ROOT/'q2_display_selection.csv',display)
 item_by=defaultdict(list)
 for r in item_rows:item_by[(r['identity_key'],r['dimension'],r['label_code'])].append(r)
 availability=[]
 for item in [x for x in display if x['main_display']=='YES']:
  role=item['role_code'];dim=item['dimension'];label=item['label_code'];sf='skills_status' if dim=='skills' else 'technical_status'
  base=[j for j in concrete if j['primary_code']==role and j[sf] in admissible and cb[j['company_id']]['scope_main_company']=='YES']
  for metric in rule['positive_buckets']:
   branches=['UNCONDITIONAL'] if metric.startswith('DUTY_') else ['UNCONDITIONAL','CHOICE','EXAMPLE','CHOICE_AND_EXAMPLE']
   for bb in branches:
    unknown=[j['identity_key'] for j in base if label_state(item_by[(j['identity_key'],dim,label)],metric,bb)=='UNKNOWN']
    availability.append({'role_code':role,'dimension':dim,'label_code':label,'metric_bucket':metric,'branch_bucket':bb,'base_ads':len(base),'n_relation_unknown':len(unknown),'n_interpretable_ads':len(base)-len(unknown),'unknown_ad_ids_json':json.dumps(unknown,ensure_ascii=False),'note':'No outcome numerator/rate computed; final group/company cells must filter these IDs.'})
 table(ROOT/'diagnostics/q2_label_interpretability.csv',availability)
 # Only denominators and population support, never label outcome differences.
 group_sets={g:{c for c,r in cb.items() if r['stratum']==g} for g in supply['groups']}
 group_sets.update({'SCENE_'+s:cs for s,cs in members.items() if cs})
 grid=[]
 for group,cs in sorted(group_sets.items()):
  for role in rule['primary_roles']:
   for dim,sf in [('skills','skills_status'),('technical_concepts','technical_status')]:
    js=[j for j in concrete if j['primary_code']==role and j['company_id'] in cs and j[sf] in admissible];counts=Counter(j['company_id'] for j in js)
    top=max(counts.values(),default=0);share=top/len(js) if js else 0;minc=rule['group_display']['min_positive_companies'];mina=rule['group_display']['min_assessable_role_ads_for_summary']
    gate=len(counts)>=minc and len(js)>=mina
    status='EXPLORATORY_SUMMARY_ELIGIBLE' if gate else 'COMPANY_POINTS_ONLY'
    if group in ['TEAM_SEPARATE','COMPONENT_SYSTEM_PORTFOLIO','ROBOT_OPERATED_SERVICE']:status='SEPARATE_CASE'
    if group.startswith('SCENE_') and group not in ['SCENE_MANUFACTURING','SCENE_LOGISTICS','SCENE_RETAIL_SERVICE']:status='HETEROGENEOUS_SCENE_CASES'
    grid.append({'group':group,'role_code':role,'dimension':dim,'member_companies':len(cs),'companies_with_denominator':len(counts),'n_assessable_ads':len(js),'n_companies_ge10':sum(v>=10 for v in counts.values()),'largest_company_ads':top,'largest_company_share':round(share,6),'dominance_warning':'YES' if share>rule['group_display']['dominant_company_share_warning'] else 'NO','display_status':status,'companies':'|'.join(sorted(counts)),'interpretation':'scene connection may be target or use; strata are recorded supply patterns'})
 table(ROOT/'diagnostics/group_role_coverage.csv',grid)
 overlaps=[]
 for a in sorted(members):
  for b in sorted(members):
   if a<b and members[a] and members[b]:overlaps.append({'scene_a':a,'scene_b':b,'n_a':len(members[a]),'n_b':len(members[b]),'n_overlap':len(members[a]&members[b]),'overlap_companies':'|'.join(sorted(members[a]&members[b])),'independent_samples':'NO' if members[a]&members[b] else 'NOT_ASSUMED'})
 table(ROOT/'diagnostics/scene_overlap.csv',overlaps)
 country=[]
 for group,cs in sorted(group_sets.items()):
  if group.startswith('SCENE_'):continue
  for role in rule['primary_roles']:
   row={'group':group,'role_code':role}
   for nation in ['China','USA']:
    js=[j for j in concrete if j['primary_code']==role and j['company_id'] in cs and (j['country']=='China')==(nation=='China')]
    row[nation+'_n_ads']=len(js);row[nation+'_n_companies']=len({j['company_id'] for j in js})
   row['auxiliary_country_coverage_gate']='PASS' if group!='TEAM_SEPARATE' and all(row[n+'_n_ads']>=20 and row[n+'_n_companies']>=3 for n in ['China','USA']) else 'NO_COUNTRY_CONTRAST'
   country.append(row)
 table(ROOT/'diagnostics/country_coverage.csv',country)
 summary={'n_companies':24,'n_ads':1654,'n_concrete_role_ads':1576,'strata_counts':dict(Counter(r['stratum'] for r in classification)),'strata_ads':{g:sum(int(r['n_ads']) for r in classification if r['stratum']==g) for g in supply['groups']},'scene_assertions':len(scene_rows),'scene_connections':{s:len(cs) for s,cs in members.items() if cs},'scene_observed_use_donation_research':{s:len(cs) for s,cs in actual.items() if cs},'selected_roles':[r for r in role_diag if r['selected']=='YES'],'display_counts':dict(Counter(r['role_code']+'|'+r['dimension'] for r in display if r['main_display']=='YES')),'used_evidence_ids':sorted(used_evidence),'input_files_verified':n_inputs,'item_interpretation_counts':[{'dimension':d,'metric':m,'branch':b,'n_items':n} for (d,m,b),n in sorted(item_summary.items())],'role_rates_by_group_computed':False}
 dump(ROOT/'diagnostics/summary.json',summary)
 print(json.dumps({k:summary[k] for k in ['n_companies','n_ads','strata_counts','scene_connections','display_counts','role_rates_by_group_computed']},ensure_ascii=False))
if __name__=='__main__':main()
