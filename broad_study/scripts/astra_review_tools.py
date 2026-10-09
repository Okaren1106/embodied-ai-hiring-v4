"""Read-only dossiers and explicit Astra review transactions for M5 repair."""
from common import *
from datetime import datetime,timezone
import sys

E=read(ROOT/'tables/Q3_semantic_evidence_partial.csv')
EB=defaultdict(list)
for e in E: EB[e['identity_key']].append(e)
AD={a['identity_key']:a for a in read(ROOT/'tables/Q3_adjudicated_ads_partial.csv')}
RID={a['reading_id']:k for k,a in AD.items()}
SAMPLE={r['identity_key'] for r in read(ROOT/'tables/Q_quality_review_sample.csv')}
MAND={r['identity_key']:r for r in read(ROOT/'tables/Q_all_second_pass_queue.csv')}
DOC={}
for p in (ROOT/'configs/Q_adjudications').glob('*.json'):
 for k,a in json.loads(p.read_text(encoding='utf-8'))['ads'].items():DOC[a['identity_key']]=a
Q=json.loads((ROOT/'notes/Q_semantic_review_queue.json').read_text(encoding='utf-8'))
QB=defaultdict(list)
for q in Q: QB[q['identity_key']].append(q)

def transactions():
 p=ROOT/'review/astra_reviews.jsonl'
 return [json.loads(s) for s in p.read_text(encoding='utf-8').splitlines()] if p.exists() else []

def register(records, batch):
 existing=transactions(); ids={(a['identity_key'],a['review_mode'],a['batch'] if a['review_mode']=='FOLLOWUP' else '') for a in existing}
 cat={x['code']:x for x in json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))['labels']}
 for a in records:
  rid=a['reading_id'];k=a.get('identity_key') or RID[rid]
  assert AD[k]['reading_id']==rid,(rid,k,'identity mismatch')
  assert a.get('identity_key') or sum(x['reading_id']==rid for x in AD.values())==1,(rid,'ambiguous reading id; specify identity_key')
  review_key=(k,a['review_mode'],batch if a['review_mode']=='FOLLOWUP' else '')
  assert review_key not in ids, (rid,'already registered; use explicit follow-up mode')
  assert a['judgment'] and a['review_mode'] in ['FULL_SOURCE_AND_CODING','BOUNDARY_CONTEXTS','FOLLOWUP']
  for change in a.get('evidence_overrides',[]):
   found=[e for e in EB[k] if e['evidence_id']==change['evidence_id']]
   assert len(found)==1,(rid,change)
   change['before']={z:found[0][z] for z in ['code','metric','branch','quote','field','start','end']}
   assert change.get('reason')
   assert any(z in change for z in ['code','metric','branch'])
   if change.get('quote'):
    assert locate(k,change)['method']!='UNRESOLVED_LOCATION',(rid,change)
  for add in a.get('additions',[]):
   assert AD[k]['role'] in cat[add['code']]['applicable_roles'],(rid,add['code'],'outside frozen role catalogue')
   loc=locate(k,add);assert loc['method']!='UNRESOLVED_LOCATION',(rid,add)
   add.update(loc);assert add.get('reason')
  if a.get('task_override'):
   t=a['task_override'];loc=locate(k,t);assert loc['method']!='UNRESOLVED_LOCATION'
   t.update(loc);t['before']=AD[k]['task']
  a.update(identity_key=k,reviewer='Astra',batch=batch,created_utc=datetime.now(timezone.utc).isoformat(),
      source_version=AD[k]['source_version'],source_fields_sha256={f:hashlib.sha256((RAW[k].get(f) or '').encode()).hexdigest() for f in ['full_description','duties','requirements']})
  ids.add(review_key)
 with (ROOT/'review/astra_reviews.jsonl').open('a',encoding='utf-8') as f:
  for a in records:f.write(js(a)+'\n')
 print('Registered',len(records),'explicit reviews',batch)

def packet(keys, reuse_read_lines=False):
 out=[]
 known={}
 if reuse_read_lines:
  for tx in transactions():
   if tx['review_mode']!='FULL_SOURCE_AND_CODING':continue
   for f in ['full_description','duties','requirements']:
    for n,line in enumerate((RAW[tx['identity_key']].get(f) or '').splitlines(),1):
     if len(line)>100:known.setdefault(line,tx['reading_id']+':'+f+':'+str(n))
 for k in keys:
  a=AD[k];rid=a['reading_id'];d=DOC[k]
  out += [f'\n## {rid} {a["company_id"]} {a["role"]} {J[k]["title"]}',
      'TASK '+a['task']+' '+a['fine_task']+' secondary='+a['secondary_task'],
      'REVIEW '+MAND.get(k,{}).get('reasons','EXTRA')]
  seen=set()
  for f in ['full_description','duties','requirements']:
   lines=[]
   for line in (RAW[k].get(f) or '').splitlines():
    if line.strip() and line not in seen:
     lines.append(('[原字节同已全文复读 '+known[line]+'] '+line[:36]+' … '+line[-24:]) if line in known else line)
     seen.add(line)
   if lines:out += ['['+f+']','\n'.join(lines)]
  # Group same original quote so requirement/branch labels can be read together.
  grouped=defaultdict(list)
  for e in EB[k]:grouped[e['quote']].append(e)
  for quote,ee in grouped.items():
   out += ['EV '+ '; '.join(e['evidence_id']+' '+e['code']+' '+e['metric']+'/'+e['branch'] for e in ee)+' | '+quote]
  for q in QB[k]:
   ni=q['review_id'].split(':')[-1];decision=d['new'][ni]
   if isinstance(decision,str) and not decision.startswith('DUPLICATE:'):
    out += ['CAND '+q['review_id']+' '+js(decision)+' | '+q['quote']]
  out += ['NOTES '+d['notes']]
 return '\n'.join(out)

def compact_packet(keys):
 """Every source line remains visible or points to a byte-identical full read.
 Evidence references source line numbers instead of repeating the same paragraph.
 """
 known={}
 for tx in transactions():
  if tx['review_mode']=='FULL_SOURCE_AND_CODING':
   for f in ['full_description','duties','requirements']:
    for n,line in enumerate((RAW[tx['identity_key']].get(f) or '').splitlines(),1):
     if len(line)>70:known.setdefault(line,tx['reading_id']+':'+f+':'+str(n))
 out=[]
 for k in keys:
  a=AD[k];rid=a['reading_id'];d=DOC[k];seen={};refs={}
  out.extend([f'\n## {rid} {a["company_id"]} {a["role"]} {J[k]["title"]}', 'TASK '+a['task']+' '+a['fine_task'], 'REVIEW '+MAND.get(k,{}).get('reasons','EXTRA')])
  for f,short in [('full_description','F'),('duties','D'),('requirements','R')]:
   field_seen=set()
   for n,line in enumerate((RAW[k].get(f) or '').splitlines(),1):
    if not line.strip():continue
    ref=short+str(n)
    if line in seen and line not in field_seen:
     refs[f,n]=seen[line];field_seen.add(line);continue
    field_seen.add(line)
    refs[f,n]=ref;seen.setdefault(line,ref)
    out.append(ref+' '+('[原字节同已全文复读 '+known[line]+'] '+line[:30]+' … '+line[-20:] if line in known else line))
  def ref_for(field,start,end):
   t=RAW[k].get(field) or '';n=t[:int(start)].count('\n')+1;last=t[:int(end)].count('\n')+1
   return ','.join(refs.get((field,i),field+str(i)) for i in range(n,last+1))
  for e in EB[k]:out.append('EV '+e['evidence_id']+' '+e['code']+' '+e['metric']+'/'+e['branch']+' @'+ref_for(e['field'],e['start'],e['end']))
  for q in QB[k]:
   decision=d['new'][q['review_id'].split(':')[-1]]
   if isinstance(decision,str) and not decision.startswith('DUPLICATE:'):
    loc=locate(k,q);ref=ref_for(loc['field'],loc['start'],loc['end']) if loc['method']!='UNRESOLVED_LOCATION' else q['quote']
    out.append('CAND '+q['review_id']+' '+decision+' @'+ref)
  out.append('NOTES '+d['notes'])
 return '\n'.join(out)

if __name__=='__main__':
 mode=sys.argv[1]
 if mode=='register':
  p=Path(sys.argv[2]);register(json.loads(p.read_text(encoding='utf-8')),p.stem)
 elif mode in ['packet','delta','compact']:
  keys=[RID[x] for x in sys.argv[2:]]
  text=compact_packet(keys) if mode=='compact' else packet(keys,reuse_read_lines=mode=='delta');dest=ROOT/'review'/('packet_'+'_'.join(sys.argv[2:])+'.md')
  dest.write_text(text,encoding='utf-8');print(text)
 elif mode=='next':
  reviewed={r['identity_key'] for r in transactions() if r['review_mode']=='FULL_SOURCE_AND_CODING'}
  role_filter=sys.argv[2] if len(sys.argv)>2 else ''
  wanted=SAMPLE | {k for k,r in MAND.items() if 'NO_KEYWORD' in r['reasons']}
  pending=[a for k,a in AD.items() if k in wanted-reviewed and (not role_filter or a['role']==role_filter)]
  print(js([dict(reading_id=a['reading_id'],role=a['role'],title=J[a['identity_key']]['title'],chars=max(len(RAW[a['identity_key']].get(f) or '') for f in ['full_description','duties','requirements'])) for a in pending]))
