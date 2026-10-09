"""Persist explicit researcher decisions and verify evidence; not a classifier."""
from common import *
import sys,datetime
def register(role, decisions):
 q=json.loads((ROOT/'notes/Q_semantic_review_queue.json').read_text(encoding='utf-8'))
 old=json.loads((ROOT/'notes/Q_inherited_semantics_all17.json').read_text(encoding='utf-8'))
 by=defaultdict(list);oi=defaultdict(list)
 for r in q:by[r['reading_id']].append(r)
 for r in old:oi[r['reading_id']].append(r)
 cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'));codes={r['code'] for r in cat['labels']}
 jsby={j['reading_id']:j for j in jobs}
 path=ROOT/'configs/Q_adjudications'/f'{role}.json';path.parent.mkdir(exist_ok=True)
 queue_hash=hashlib.sha256((ROOT/'notes/Q_semantic_review_queue.json').read_bytes()).hexdigest()
 data=json.loads(path.read_text(encoding='utf-8')) if path.exists() else dict(catalog_version='Q2-v2.1',coding_version='Astra-Q2-v2.1-first-pass',reader='Astra',queue_sha256=queue_hash,ads={})
 assert data['queue_sha256']==queue_hash
 for rid,d in decisions.items():
  assert rid not in data['ads'],'Use an explicit revision instead of overwriting: '+rid
  j=jsby[rid];assert role==j['primary_code']
  choices=d['new'];assert set(map(int,choices))=={int(r['review_id'].split(':')[1]) for r in by[rid]},(rid,choices,len(by[rid]))
  for r in by[rid]:
   action=choices[str(r['review_id'].split(':')[1])]
   if isinstance(action,list):
    for c,m,b in action:
     assert c in codes and m in ['DUTY_OWN_USE','DUTY_OWN_DEVELOP','REQUIRED','GENERAL','PREFERRED','SEPARATE','UNKNOWN']
     assert b in ['UNCONDITIONAL','CHOICE','EXAMPLE','CHOICE_AND_EXAMPLE','CONDITIONAL','UNRESOLVED','BACKGROUND','COLLABORATION_OBJECT','RECRUITMENT_OBJECT','PROCUREMENT_OBJECT','NEGATED']
     assert r['method']!='UNRESOLVED_LOCATION',(rid,r)
     t=RAW[j['identity_key']].get(r['field'],'') or ''
     assert t[int(r['start']):int(r['end'])]==r['quote'],(rid,r)
   else:assert action.startswith(('REJECT:','OUTSIDE:','DUPLICATE:')),action
  evidence=d['task_evidence']
  for key,override in d.get('old_overrides',{}).items():
   assert key.startswith('O') and 1<=int(key[1:])<=len(oi[rid]),(rid,key)
   assert all(x in override for x in ['metric','branch','relation','reason']),(rid,key,'Incomplete override')
  taskbook=json.loads((ROOT/'configs/Q_task_strata_v2.json').read_text(encoding='utf-8'))
  assert d['task'] in {x['task_code'] for x in taskbook['roles'][role]}|{'OTHER','UNRESOLVED'},(rid,d['task'])
  for extra in d.get('additions',[]):
   assert extra['code'] in codes,(rid,extra['code'])
   assert extra['metric'] in ['DUTY_OWN_USE','DUTY_OWN_DEVELOP','REQUIRED','GENERAL','PREFERRED','SEPARATE','UNKNOWN']
   assert locate(j['identity_key'],extra)['method']!='UNRESOLVED_LOCATION',(rid,extra)
  loc=locate(j['identity_key'],dict(quote=evidence))
  assert loc['method']!='UNRESOLVED_LOCATION',(rid,evidence)
  d.update(identity_key=j['identity_key'],company_id=j['company_id'],role=role,status='CODED_FIRST_PASS',reviewed_inherited_count=len(oi[rid]),reviewed_candidate_count=len(by[rid]),task_evidence_location=loc,reader='Astra',qc_status='PENDING_SECOND_PASS',source_version=j['text_version_hash'],full_text_read=True,updated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
  data['ads'][rid]=d
 path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
 print(role,'completed first pass',len(data['ads']))
