"""Materialize completed researcher decisions. Unread ads remain PENDING."""
from common import *
import datetime
design=json.loads((ROOT/'configs/Q_design_lock_v2.json').read_text(encoding='utf-8'))
for r in design['files']:assert hashlib.sha256((ROOT/r['path']).read_bytes()).hexdigest()==r['sha256']
cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
CD={r['code']:r for r in cat['labels']};rule=json.loads((ROOT/'configs/Q_coding_rules_v2.json').read_text(encoding='utf-8'))
catalog_by_role=defaultdict(set)
for c,d in CD.items():
 for f in d['applicable_roles']:catalog_by_role[f].add(c)
queue=json.loads((ROOT/'notes/Q_semantic_review_queue.json').read_text(encoding='utf-8'));qh=hashlib.sha256((ROOT/'notes/Q_semantic_review_queue.json').read_bytes()).hexdigest()
qr={r['review_id']:r for r in queue}
old=json.loads((ROOT/'notes/Q_inherited_semantics_all17.json').read_text(encoding='utf-8'));ob=defaultdict(list);obk=defaultdict(list)
for r in old:
 ob[r['reading_id']].append(r);obk[r['identity_key']].append(r)
qb=defaultdict(list)
for r in queue:qb[r['identity_key']].append(r)
adjud={};newaudit=[];oldchanges=[];evidence=[];itemby=defaultdict(list);adrows=[];outside=[]
for p in sorted((ROOT/'configs/Q_adjudications').glob('*.json')):
 d=json.loads(p.read_text(encoding='utf-8'));assert d['queue_sha256']==qh and d['catalog_version']=='Q2-v2.1'
 for store,a in d['ads'].items():
  k=a['identity_key'];rid=a.get('reading_id') or J[k]['reading_id']
  assert k not in adjud;adjud[k]=a
  assert a['full_text_read'] and a['status']=='CODED_FIRST_PASS' and a['source_version']==J[k]['text_version_hash']
  inh=obk[k] or ob[rid]
  for i,r in enumerate(inh,1):
   rr=dict(r,metric=r['suggested_metric'],branch=r['suggested_branch'],evidence_id=rid+f':O{i}',judgement='INHERITED_REVIEWED',reviewer=a.get('reader','Astra'))
   override=a.get('old_overrides',{}).get(f'O{i}')
   if override:
    oldchanges.append(dict(reading_id=rid,identity_key=k,code=r['code'],old_metric=r['suggested_metric'],old_branch=r['suggested_branch'],old_relation=r['prior_relation'],new_metric=override['metric'],new_branch=override['branch'],new_relation=override['relation'],reason=override['reason'],quote=r['quote'],original_unchanged='YES'))
    rr.update(metric=override['metric'],branch=override['branch'],prior_relation=override['relation'],judgement='DERIVED_OVERRIDE',override_reason=override['reason'])
    if override.get('quote'):
     newloc=locate(k,override);assert newloc['method']!='UNRESOLVED_LOCATION'
     rr.update(newloc)
    oldchanges[-1].update(old_field=r['field'],old_start=r['start'],old_end=r['end'],new_field=rr['field'],new_start=rr['start'],new_end=rr['end'],new_quote=rr['quote'],evidence_id=rr['evidence_id'])
   # A verified quote, not a claimed independent semantic validation.
   assert rr['method']!='UNRESOLVED_LOCATION',(rid,rr['code'],rr['quote'])
   assert (RAW[k].get(rr['field']) or '')[int(rr['start']):int(rr['end'])]==rr['quote']
   evidence.append(rr);itemby[k,rr['code']].append(rr)
  for ni,actions in a['new'].items():
   matches=[r for r in qb[k] if r['review_id'].split(':')[-1]==str(ni)]
   q=matches[0] if len(matches)==1 else qr[rid+':'+ni]
   assert q['identity_key']==k,(k,ni,q.get('identity_key'))
   audit=dict(reading_id=rid,identity_key=k,review_id=q['review_id'],origin=q['origin'],surface=q['surface'],candidate_codes=js(q['candidate_codes']),decision=js(actions),quote=q['quote'])
   newaudit.append(audit)
   if isinstance(actions,str):
    if actions.startswith('OUTSIDE:'):outside.append(dict(audit,reason=actions))
    if actions.startswith('DUPLICATE:'):
     target=actions.split('DUPLICATE:',1)[1];tni=target.split(':')[-1]
     tmatch=[r for r in qb[k] if r['review_id'].split(':')[-1]==tni]
     assert tmatch and tmatch[0]['identity_key']==k
     assert isinstance(a['new'][tni],list),(rid,ni,'duplicate must resolve directly to retained evidence')
    continue
   for ci,(c,m,b) in enumerate(actions):
    assert c in catalog_by_role[a['role']],(rid,c,'Outside frozen role scope')
    rr=dict(identity_key=k,reading_id=rid,role=a['role'],code=c,origin=q['origin'],prior_context='DUTY' if m.startswith('DUTY') else 'REQUIREMENT' if m in ['GENERAL','REQUIRED','PREFERRED'] else 'REVIEWED_SEPARATE',prior_use='REVIEWED',prior_relation='REVIEWED',metric=m,branch=b,evidence_id=q['review_id']+':'+str(ci),judgement='RESEARCHER_CONTEXT_ADJUDICATED',reviewer=a.get('reader','Astra'),**{f:q[f] for f in ['field','start','end','quote','method']})
    if m=='UNKNOWN':
     rr['affected_metrics']=a.get('uncertainty_scope',{}).get(c)
     assert rr['affected_metrics'],(rid,c,'Unknown requires explicit metric scope')
    assert rr['method']!='UNRESOLVED_LOCATION'
    assert (RAW[k].get(rr['field']) or '')[int(rr['start']):int(rr['end'])]==rr['quote']
    evidence.append(rr);itemby[k,c].append(rr)
  for i,r in enumerate(a.get('additions',[]),1):
   loc=locate(k,r);assert loc['method']!='UNRESOLVED_LOCATION',(rid,r)
   assert r['code'] in catalog_by_role[a['role']],(rid,r['code'],'Additional item outside role scope requires amendment')
   rr=dict(identity_key=k,reading_id=rid,role=a['role'],code=r['code'],origin='FULL_READ_ADDITION',metric=r['metric'],branch=r['branch'],prior_context='DUTY' if r['metric'].startswith('DUTY') else 'REQUIREMENT' if r['metric'] in ['GENERAL','REQUIRED','PREFERRED'] else 'REVIEWED_SEPARATE',prior_use='REVIEWED',prior_relation='REVIEWED',evidence_id=rid+':ADD'+str(i),judgement='RESEARCHER_CONTEXT_ADJUDICATED',reviewer=a.get('reader','Astra'),reason=r['reason'],**loc)
   if r['metric']=='UNKNOWN':
    rr['affected_metrics']=a.get('uncertainty_scope',{}).get(r['code'])
    assert rr['affected_metrics'],(rid,r['code'],'Unknown addition requires explicit metric scope')
   evidence.append(rr);itemby[k,r['code']].append(rr)
  for r in a.get('outside_extra',[]):
   loc=locate(k,r);assert loc['method']!='UNRESOLVED_LOCATION'
   outside.append(dict(reading_id=rid,identity_key=k,review_id=rid+':OUTSIDE_EXTRA',origin='FULL_READ_ADDITION',surface=r['quote'],reason=r['description'],**loc))
  adrows.append(dict(identity_key=k,reading_id=rid,company_id=a['company_id'],role=a['role'],task=a['task'],fine_task=a['fine_task'],secondary_task=a.get('secondary_task',''),task_quote=a['task_evidence'],task_field=a['task_evidence_location']['field'],task_start=a['task_evidence_location']['start'],task_end=a['task_evidence_location']['end'],source_version=a['source_version'],catalog_version='Q2-v2.1',coding_version=a.get('coding_version','Astra-Q2-v2.1-first-pass' if a.get('reader','Astra')=='Astra' else 'grok4.6-Q2-v2.1-first-pass'),full_text_read='YES',status=a['status'],reviewer=a.get('reader','Astra'),qc_status=a['qc_status'],notes=a['notes']))
def cellstate(k,code,m,b):
 rr=itemby[k,code]
 if any(r['metric']==m and r['branch']==b for r in rr):return 'P'
 for r in rr:
  if r['metric']=='UNKNOWN' and m in r.get('affected_metrics',[]) and (r['branch']=='UNRESOLVED' or b==r['branch']):return 'U'
  ctx=r['prior_context']
  relevant=ctx in (['DUTY','UNCERTAIN'] if m.startswith('DUTY') else ['REQUIREMENT','UNCERTAIN'])
  # Known background/collaboration/exclusion is not uncertainty.
  ambiguous=r['prior_use']=='UNRESOLVED' or r['prior_relation']=='UNRESOLVED' or ctx=='UNCERTAIN'
  if relevant and (ambiguous or (r['metric']==m and r['branch']=='UNRESOLVED') or r['metric']=='UNKNOWN'):return 'U'
 return 'Z'
states=[]
for a in adrows:
 k=a['identity_key'];r=adjud[k]
 for c in sorted(catalog_by_role[a['role']]):
  for s in rule['legacy_14_slices']:
   m,b=s['metric'],s['branch'];state=cellstate(k,c,m,b)
   na=r.get('not_applicable',{}).get(c)
   if na:
    assert state!='P';state='NA'
   states.append(dict(identity_key=k,reading_id=a['reading_id'],company_id=a['company_id'],role=a['role'],task=a['task'],label_code=c,measurement_type=CD[c]['measurement_type'],metric=m,branch=b,state=state,not_applicable_reason=na or '',catalog_version='Q2-v2.1',coding_status='FIRST_PASS_NOT_FINAL',qc_status=a['qc_status']))
dump('tables/Q3_adjudicated_ads_partial.csv',adrows)
dump('tables/Q3_semantic_evidence_partial.csv',[dict(r,affected_metrics=js(r['affected_metrics'])) if isinstance(r.get('affected_metrics'),list) else r for r in evidence])
dump('tables/Q3_candidate_decisions_partial.csv',newaudit)
dump('tables/Q3_applicable_states_partial.csv',states)
if oldchanges:dump('tables/Q2_v2_semantic_changes_partial.csv',oldchanges)
if outside:dump('tables/Q2_remaining_directory_gaps_partial.csv',outside)
frame=read(ROOT/'tables/Q3_coding_frame.csv')
for r in frame:
 if r['identity_key'] in adjud:r['status']='CODED_FIRST_PASS'
dump('tables/Q3_coding_frame.csv',frame)
coverage=read(ROOT/'tables/Q1_role_coverage.csv')
for r in coverage:
 n=sum(a['role']==r['role'] for a in adrows)
 r.update(first_pass_coded_ads=n,L1_status='FIRST_PASS_COMPLETE_QC_PENDING' if n==int(r['all24_ads']) else f'IN_PROGRESS_{n}_OF_{r["all24_ads"]}' if n else 'PENDING',catalog_items=len(catalog_by_role[r['role']]))
dump('tables/Q1_role_coverage.csv',coverage)
save_json('verification/Q_partial_materialization.json',dict(status='PASS_PARTIAL_ONLY',coded_ads=len(adrows),pending_ads=1576-len(adrows),candidate_decisions=len(newaudit),semantic_evidence=len(evidence),explicit_ad_label_slice_states=len(states),states=dict(Counter(r['state'] for r in states)),derived_old_semantic_changes=len(oldchanges),directory_gap_records=len(outside),all_sources_exact=True,design_lock_checked=True,scope='First-pass coding integrity, not completed Q2 study or second-pass acceptance',input_files_checked=lock_check()))
print('Partial materialization PASS',len(adrows),'ads;',len(states),'explicit states;',len(evidence),'exact evidence;',len(oldchanges),'derived old-context changes;',1576-len(adrows),'pending')
