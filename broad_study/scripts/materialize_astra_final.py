"""Rebuild Q2 from submitted first-pass evidence plus explicit Astra transactions.

No pending review is promoted to confirmed. Original source and author are retained.
"""
from astra_review_tools import *
from copy import deepcopy

for x in json.loads((ROOT/'configs/Q_design_lock_v2.json').read_text(encoding='utf-8'))['files']:
 assert hashlib.sha256((ROOT/x['path']).read_bytes()).hexdigest()==x['sha256']
cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
CD={x['code']:x for x in cat['labels']}
CBR=defaultdict(set)
for code,lab in CD.items():
 for role in lab['applicable_roles']:CBR[role].add(code)
rules=json.loads((ROOT/'configs/Q_coding_rules_v2.json').read_text(encoding='utf-8'))
slices=[(x['metric'],x['branch'],'LEGACY_14') for x in rules['legacy_14_slices']]
slices += [(m,b,'DUTY_BRANCH_SUPPLEMENT') for m in ['DUTY_OWN_USE','DUTY_OWN_DEVELOP'] for b in ['CHOICE','EXAMPLE','CHOICE_AND_EXAMPLE','CONDITIONAL']]
unknown_targets={m for m,b,_ in slices}|{m+'_'+b for m,b,_ in slices}
evidence=deepcopy(E); index={(e['identity_key'],e['evidence_id']):e for e in evidence}
ads=deepcopy(AD); limits=defaultdict(list); reviews=defaultdict(list); changes=[]
for tx in transactions():
 k=tx['identity_key'];reviews[k].append(tx)
 assert tx['source_version']==J[k]['text_version_hash']
 for f,h in tx['source_fields_sha256'].items():assert hashlib.sha256((RAW[k].get(f) or '').encode()).hexdigest()==h
 for n,ch in enumerate(tx.get('evidence_overrides',[]),1):
  e=index[k,ch['evidence_id']];before={z:e.get(z,'') for z in ['code','metric','branch','quote','field','start','end','affected_metrics']}
  for z in ['code','metric','branch','affected_metrics']:
   if z in ch:e[z]=ch[z]
  if ch.get('quote'):
   loc=locate(k,ch);assert loc['method']!='UNRESOLVED_LOCATION';e.update(loc)
  e['first_pass_reviewer']=e.get('first_pass_reviewer',e['reviewer']);e['reviewer']='Astra';e['judgement']='ASTRA_REVIEW_OVERRIDE';e['review_reason']=ch['reason']
  changes.append(dict(reading_id=tx['reading_id'],identity_key=k,evidence_id=e['evidence_id'],batch=tx['batch'],before=js(before),after=js({z:e.get(z,'') for z in before}),reason=ch['reason']))
 for n,add in enumerate(tx.get('additions',[]),1):
  eid=tx['reading_id']+':ASTRA:'+tx['batch']+':'+str(n)
  e=dict(identity_key=k,reading_id=tx['reading_id'],role=ads[k]['role'],code=add['code'],metric=add['metric'],branch=add['branch'],
      evidence_id=eid,origin='ASTRA_'+tx['review_mode']+'_ADDITION',prior_context='REVIEWED',prior_use='REVIEWED',prior_relation='REVIEWED',
      judgement='ASTRA_REVIEW_ADDITION',first_pass_reviewer='',reviewer='Astra',review_reason=add['reason'],**{z:add[z] for z in ['field','start','end','quote','method']})
  if 'affected_metrics' in add:e['affected_metrics']=add['affected_metrics']
  evidence.append(e);index[k,eid]=e
  changes.append(dict(reading_id=tx['reading_id'],identity_key=k,evidence_id=eid,batch=tx['batch'],before='{}',after=js(e),reason=add['reason']))
 for ch in tx.get('transaction_overrides',[]):
  eid=tx['reading_id']+':ASTRA:'+ch['target_batch']+':'+str(ch['target_addition_index'])
  e=index[k,eid];before={z:e.get(z,'') for z in ['code','metric','branch','affected_metrics','excluded_from_catalog']}
  for z in before:
   if z in ch:e[z]=ch[z]
  e['review_reason']=ch['reason'];e['judgement']='ASTRA_REVIEW_FOLLOWUP'
  changes.append(dict(reading_id=tx['reading_id'],identity_key=k,evidence_id=eid,batch=tx['batch'],before=js(before),after=js({z:e.get(z,'') for z in before}),reason=ch['reason']))
 if tx.get('task_override'):
  a=ads[k];ch=tx['task_override'];before=a['task'];a['task']=ch['task'];a['task_quote']=ch['quote'];a['task_field']=ch['field'];a['task_start']=ch['start'];a['task_end']=ch['end']
  if a.get('secondary_task')==a['task']:a['secondary_task']=''
  changes.append(dict(reading_id=tx['reading_id'],identity_key=k,evidence_id='TASK',batch=tx['batch'],before=before,after=a['task'],reason=ch['reason']))
 limits[k].extend(tx.get('source_limits',[]))

grouped=defaultdict(list)
for e in evidence:
 k=e['identity_key']
 assert (RAW[k].get(e['field']) or '')[int(e['start']):int(e['end'])]==e['quote']
 if e.get('excluded_from_catalog'):
  assert e['code'] not in CBR[ads[e['identity_key']]['role']]
  continue
 k=e['identity_key'];assert e['code'] in CBR[ads[k]['role']], (e['reading_id'],e['code'],'outside role catalogue')
 if isinstance(e.get('affected_metrics'),str) and e['affected_metrics']:
  e['affected_metrics']=json.loads(e['affected_metrics'])
 if e['metric']=='UNKNOWN':
  assert e.get('affected_metrics'),(e['evidence_id'],'UNKNOWN requires explicit affected scope')
  assert set(e['affected_metrics'])<=unknown_targets,(e['evidence_id'],'invalid unknown scope',e['affected_metrics'])
 grouped[k,e['code']].append(e)

def resolve(k,code,m,b):
 ee=grouped[k,code]
 if any(e['metric']==m and e['branch']==b for e in ee):return 'P',''
 for lim in limits[k]:
  scope=lim['codes']
  if m in lim['metrics'] and (scope=='ALL_APPLICABLE' or 'ALL_APPLICABLE' in scope or code in scope):return 'SOURCE_EXCLUDED',lim['reason']
 na=DOC[k].get('not_applicable',{}).get(code)
 if na:return 'NA',na
 for e in ee:
  if e['metric']=='UNKNOWN' and (m in e.get('affected_metrics',[]) or m+'_'+b in e.get('affected_metrics',[])):
   if e['branch']=='UNRESOLVED' or e['branch']==b:return 'U','UNKNOWN_OBJECT_OR_RESPONSIBILITY'
  if e['metric']==m and e['branch']=='UNRESOLVED':return 'U','UNKNOWN_BRANCH_IN_THIS_METRIC'
 return 'Z',''

reviewrows=[]
for k,a in ads.items():
 txs=reviews[k];full=any(t['review_mode']=='FULL_SOURCE_AND_CODING' for t in txs)
 boundary=any(t['review_mode']=='BOUNDARY_CONTEXTS' for t in txs)
 q='ASTRA_FULL_SOURCE_REVIEWED' if full else 'ASTRA_BOUNDARY_REVIEWED' if boundary else 'REVIEW_PENDING'
 a['first_pass_reader']=a['reviewer'];a['second_pass_reviewer']='Astra' if txs else '';a['qc_status']=q
 a['coding_version']='Astra-Q2-v2.1-review3';a['review_batches']=js([t['batch'] for t in txs])
 reviewrows.append(dict(identity_key=k,reading_id=a['reading_id'],role=a['role'],first_pass_reader=a['reviewer'],
   seeded='YES' if k in SAMPLE else 'NO',mandatory='YES' if k in MAND else 'NO',reasons=MAND.get(k,{}).get('reasons','[]'),
   second_pass_status=q,review_batches=a['review_batches'],judgments=js([t['judgment'] for t in txs]),
   review_independence=('SAME_MODEL_REREVIEW' if a['reviewer']=='Astra' else 'ASTRA_REVIEW_OF_GROK') if (full or boundary) else 'NOT_YET_REVIEWED'))
counts=Counter();n=0
p=ROOT/'tables/Q3_states_final.csv'
fields=['identity_key','reading_id','company_id','role','task','label_code','measurement_type','metric','branch','slice_family','state','state_reason','catalog_version','coding_version','qc_status']
with p.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for k,a in ads.items():
  for c in sorted(CBR[a['role']]):
   for m,b,family in slices:
    st,reason=resolve(k,c,m,b);counts[family,st]+=1;n+=1
    w.writerow(dict(identity_key=k,reading_id=a['reading_id'],company_id=a['company_id'],role=a['role'],task=a['task'],label_code=c,measurement_type=CD[c]['measurement_type'],metric=m,branch=b,slice_family=family,state=st,state_reason=reason,catalog_version='Q2-v2.1',coding_version='Astra-Q2-v2.1-review3',qc_status=a['qc_status']))
dump('tables/Q3_ads_final.csv',list(ads.values()))
dump('tables/Q3_evidence_final.csv',[dict(e,affected_metrics=js(e['affected_metrics'])) if isinstance(e.get('affected_metrics'),list) else e for e in evidence])
dump('tables/Q3_review_receipts.csv',reviewrows)
if changes:dump('tables/Q3_astra_changes.csv',changes)
receipt=dict(status='MATERIALIZED_REVIEW_PROGRESS_NOT_AUTOMATIC_ACCEPTANCE',ads=len(ads),evidence=len(evidence),
 states=n,counts={family:{st:v for (f,st),v in counts.items() if f==family} for family in ['LEGACY_14','DUTY_BRANCH_SUPPLEMENT']},
 reviewed_full=sum(a['qc_status']=='ASTRA_FULL_SOURCE_REVIEWED' for a in ads.values()),
 seeded_total=len(SAMPLE),seeded_full_reviewed=sum(ads[k]['qc_status']=='ASTRA_FULL_SOURCE_REVIEWED' for k in SAMPLE),
 mandatory_total=len(MAND),mandatory_reviewed=sum(ads[k]['qc_status']!='REVIEW_PENDING' for k in MAND),
 changes=len(changes),frozen_inputs_checked=lock_check(),created_utc=datetime.now(timezone.utc).isoformat())
save_json('verification/astra_materialization.json',receipt)
print(js(receipt))
