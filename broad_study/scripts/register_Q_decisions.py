"""Persist explicit researcher decisions and verify evidence; not a classifier."""
from common import *
import sys,datetime
ALLOWED_READERS={'Astra','grok4.6'}
VERSION={'Astra':'Astra-Q2-v2.1-first-pass','grok4.6':'grok4.6-Q2-v2.1-first-pass'}
def _idx(review_id):
 return review_id.split(':')[-1]
def register(role, decisions, reader='grok4.6'):
 assert reader in ALLOWED_READERS, reader
 q=json.loads((ROOT/'notes/Q_semantic_review_queue.json').read_text(encoding='utf-8'))
 old=json.loads((ROOT/'notes/Q_inherited_semantics_all17.json').read_text(encoding='utf-8'))
 by=defaultdict(list);oi=defaultdict(list);byk=defaultdict(list);oik=defaultdict(list)
 for r in q:
  by[r['reading_id']].append(r);byk[r['identity_key']].append(r)
 for r in old:
  oi[r['reading_id']].append(r);oik[r['identity_key']].append(r)
 cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'));codes={r['code'] for r in cat['labels']}
 jsby={j['reading_id']:j for j in jobs};jbyk={j['identity_key']:j for j in jobs}
 rid_n=Counter(j['reading_id'] for j in jobs)
 path=ROOT/'configs/Q_adjudications'/f'{role}.json';path.parent.mkdir(exist_ok=True)
 queue_hash=hashlib.sha256((ROOT/'notes/Q_semantic_review_queue.json').read_bytes()).hexdigest()
 if path.exists():
  data=json.loads(path.read_text(encoding='utf-8'))
  orig=data.get('reader','Astra')
  contrib=list(dict.fromkeys(data.get('contributors') or [orig]))
  if reader not in contrib:contrib.append(reader)
  data['contributors']=contrib
 else:
  data=dict(catalog_version='Q2-v2.1',coding_version=VERSION[reader],reader=reader,contributors=[reader],queue_sha256=queue_hash,ads={})
 assert data['queue_sha256']==queue_hash
 existing_keys={a.get('identity_key',k) for k,a in data['ads'].items()}
 for key,d in decisions.items():
  if key in jbyk: j=jbyk[key]
  elif d.get('identity_key'): j=jbyk[d['identity_key']]
  else: j=jsby[key]
  rid=j['reading_id'];k=j['identity_key']
  assert role==j['primary_code']
  store=k if rid_n[rid]>1 else rid
  assert store not in data['ads'] and k not in existing_keys,'Use an explicit revision instead of overwriting: '+store
  qrecs=byk[k] or by[rid];orecs=oik[k] or oi[rid]
  choices=d['new'];assert set(map(int,choices))=={int(_idx(r['review_id'])) for r in qrecs},(store,choices,len(qrecs))
  for r in qrecs:
   action=choices[str(_idx(r['review_id']))]
   if isinstance(action,list):
    for c,m,b in action:
     assert c in codes and m in ['DUTY_OWN_USE','DUTY_OWN_DEVELOP','REQUIRED','GENERAL','PREFERRED','SEPARATE','UNKNOWN']
     assert b in ['UNCONDITIONAL','CHOICE','EXAMPLE','CHOICE_AND_EXAMPLE','CONDITIONAL','UNRESOLVED','BACKGROUND','COLLABORATION_OBJECT','RECRUITMENT_OBJECT','PROCUREMENT_OBJECT','NEGATED']
     assert r['method']!='UNRESOLVED_LOCATION',(store,r)
     t=RAW[k].get(r['field'],'') or ''
     assert t[int(r['start']):int(r['end'])]==r['quote'],(store,r)
   else:assert action.startswith(('REJECT:','OUTSIDE:','DUPLICATE:')),action
  evidence=d['task_evidence']
  for ok,override in d.get('old_overrides',{}).items():
   assert ok.startswith('O') and 1<=int(ok[1:])<=len(orecs),(store,ok,len(orecs))
   assert all(x in override for x in ['metric','branch','relation','reason']),(store,ok,'Incomplete override')
  taskbook=json.loads((ROOT/'configs/Q_task_strata_v2.json').read_text(encoding='utf-8'))
  assert d['task'] in {x['task_code'] for x in taskbook['roles'][role]}|{'OTHER','UNRESOLVED'},(store,d['task'])
  for extra in d.get('additions',[]):
   assert extra['code'] in codes,(store,extra['code'])
   assert extra['metric'] in ['DUTY_OWN_USE','DUTY_OWN_DEVELOP','REQUIRED','GENERAL','PREFERRED','SEPARATE','UNKNOWN']
   assert locate(k,extra)['method']!='UNRESOLVED_LOCATION',(store,extra)
  loc=locate(k,dict(quote=evidence))
  assert loc['method']!='UNRESOLVED_LOCATION',(store,evidence)
  d.update(identity_key=k,company_id=j['company_id'],role=role,status='CODED_FIRST_PASS',reviewed_inherited_count=len(orecs),reviewed_candidate_count=len(qrecs),task_evidence_location=loc,reader=reader,coding_version=VERSION[reader],qc_status='PENDING_SECOND_PASS',source_version=j['text_version_hash'],full_text_read=True,updated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
  data['ads'][store]=d;existing_keys.add(k)
 path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
 print(role,'completed first pass',len(data['ads']),'new_reader',reader)
if __name__=='__main__':
 role,src=sys.argv[1],Path(sys.argv[2])
 reader=sys.argv[3] if len(sys.argv)>3 else 'grok4.6'
 register(role,json.loads(src.read_text(encoding='utf-8')),reader=reader)
