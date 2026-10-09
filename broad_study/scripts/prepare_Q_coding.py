"""Produce reviewable semantic candidates. No automatic final P/Z/U/NA assignment."""
from common import *
import unicodedata,math,random
for f in json.loads((ROOT/'configs/Q_design_lock_v2.json').read_text(encoding='utf-8'))['files']:
 assert hashlib.sha256((ROOT/f['path']).read_bytes()).hexdigest()==f['sha256']
cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
CD={d['code']:d for d in cat['labels']}
idx={};roots={}
for line in (A/'relations.jsonl').read_text(encoding='utf-8').splitlines():
 r=json.loads(line)
 if r['kind']=='requirement_group':
  for n in r['nodes']:idx[r['identity_key'],n['node_id']]=n;roots[r['identity_key'],n['node_id']]=r['root_relation']
def branch(r):
 if r.get('context')!='REQUIREMENT':return 'UNCONDITIONAL' if r.get('context')=='DUTY' else 'UNRESOLVED'
 node=r.get('requirement_node_id');rels=set();seen=set()
 if not node:return 'UNRESOLVED'
 while node:
  key=(r['identity_key'],node)
  if key not in idx or node in seen:return 'UNRESOLVED'
  seen.add(node);rels.update([idx[key]['relation'],roots[key]]);node=idx[key]['parent_id']
 if 'UNRESOLVED' in rels:return 'UNRESOLVED'
 ch=bool(rels&{'OR','OR_EQUIVALENT','SOME_OF'});ex='EXAMPLE' in rels
 return 'CHOICE_AND_EXAMPLE' if ch and ex else 'CHOICE' if ch else 'EXAMPLE' if ex else 'UNCONDITIONAL'
rule=json.loads((ROOT/'configs/Q_coding_rules_v2.json').read_text(encoding='utf-8'))
def metric(r):
 for m,pair in rule['inherited_positive_buckets'].items():
  if [r.get('use'),r.get('mention_relation')]==pair and r.get('context')==('DUTY' if m.startswith('DUTY_') else 'REQUIREMENT'):return m
 return 'SEPARATE'
unmapped=read(A/'unmapped_mentions.csv')
pool=read(ROOT/'tables/Q_candidate_mention_pool.csv')
lex={r['candidate_id']:json.loads(r['candidate_codes']) for r in read(ROOT/'tables/Q_lexical_catalog_candidates.csv')}
ad_items=defaultdict(list);rows=[];accepted_by=defaultdict(list)
for r in read(A/'skills.csv')+read(A/'technical_concepts.csv'):
 if role(J[r['identity_key']]) not in CONCRETE:continue
 loc=locate(r['identity_key'],r)
 rr=dict(identity_key=r['identity_key'],reading_id=J[r['identity_key']]['reading_id'],role=role(J[r['identity_key']]),code=r['label_code'],origin='INHERITED_ACCEPTED',prior_context=r['context'],prior_use=r['use'],prior_relation=r['mention_relation'],suggested_metric=metric(r),suggested_branch=branch(r),requirement_node_id=r['requirement_node_id'],**loc)
 accepted_by[r['identity_key']].append(rr)
# Non-semantic candidate mapping from prior unmapped records.
for r in pool:
 if r['origin']=='ACCEPTED_TAG':continue
 source=unmapped[int(r['candidate_id'].split('_')[-1])]
 loc=locate(r['identity_key'],source)
 codes=lex[r['candidate_id']]
 rows.append(dict(identity_key=r['identity_key'],reading_id=J[r['identity_key']]['reading_id'],role=r['role'],candidate_origin=r['candidate_id'],origin='UNMAPPED_LEXICAL',surface=r['surface'],candidate_codes=codes,prior_context=r['context'],prior_use=r['use'],prior_relation=r['mention_relation'],suggested_metric=metric(r),suggested_branch=branch(r),requirement_node_id=r['requirement_node_id'],**loc))
# Search all raw text for new-catalog expressions not represented in the unmapped inventory.
# This finds omissions only. Every occurrence still requires semantic review.
patterns={}
for code,d in CD.items():
 if not code.startswith('V2_'):continue
 pats=[]
 for a in d['aliases']:
  if not a:continue
  p=re.escape(a)
  if re.match(r'^[A-Za-z0-9]',a):p=r'(?<![A-Za-z0-9_])'+p
  if re.search(r'[A-Za-z0-9]$',a):p+=r'(?![A-Za-z0-9_])'
  pats.append(p)
 patterns[code]=re.compile('|'.join('(?:'+p+')' for p in pats),re.I)
# Only raw fields from the fixed source, with full_description preferred. Other fields may add unique substantive text.
norm=lambda t:''.join(c for c in unicodedata.normalize('NFKC',t) if not c.isspace() and unicodedata.category(c)[0] not in ('P','Z'))
knownocc=defaultdict(list)
for r in rows:
 for code in r['candidate_codes']:knownocc[r['identity_key'],code].append(r)
for k,j in J.items():
 f=role(j)
 if f not in CONCRETE:continue
 seen=set()
 for field in ['full_description','duties','requirements']:
  text=RAW[k].get(field,'') or ''
  for matchline in re.finditer(r'[^\r\n]+',text):
   line=matchline.group();n=norm(line)
   if not n or n in seen:continue
   seen.add(n)
   cc=[]
   for code,pat in patterns.items():
    if f not in CD[code]['applicable_roles'] or not pat.search(line):continue
    # Retain occurrences in every distinct raw line. A short prior quote such as
    # "Postman" in duties must not suppress a separate requirement occurrence.
    cc.append(code)
   if cc:
    rows.append(dict(identity_key=k,reading_id=j['reading_id'],role=f,candidate_origin='FULL_RAW_SEARCH',origin='RAW_LEXICAL',surface=line,candidate_codes=cc,prior_context='',prior_use='',prior_relation='',suggested_metric='REVIEW_REQUIRED',suggested_branch='REVIEW_REQUIRED',requirement_node_id='',field=field,start=matchline.start(),end=matchline.end(),method='EXACT_RAW_LINE',quote=line))
by=defaultdict(list)
for r in rows:by[r['identity_key']].append(r)
final=[]
for k in sorted(by):
 for n,r in enumerate(sorted(by[k],key=lambda r:(['full_description','duties','requirements'].index(r['field']) if r['field'] in ['full_description','duties','requirements'] else 9,int(r['start']) if str(r['start']).isdigit() else -1,r['candidate_origin'])),1):
  r['review_id']=J[k]['reading_id']+':'+str(n);r['status']='PENDING_RESEARCHER_JUDGEMENT';final.append(r)
save_json('notes/Q_semantic_review_queue.json',final)
save_json('notes/Q_inherited_semantics_all17.json',[r for v in accepted_by.values() for r in v])
tasks=json.loads((ROOT/'configs/Q_task_strata_v2.json').read_text(encoding='utf-8'))['roles']
pil=read(ROOT/'tables/Q_calibration_sample.csv');pids={r['identity_key'] for r in pil}
frame=[]
for cov in read(ROOT/'tables/Q1_role_coverage.csv'):
 f=cov['role'];p=[r['identity_key'] for r in pil if r['role']==f]
 remainder=sorted(k for k,j in J.items() if role(j)==f and k not in pids)
 for i,k in enumerate(p+remainder,1):frame.append(dict(identity_key=k,reading_id=J[k]['reading_id'],role=f,company_id=J[k]['company_id'],role_order=list(tasks).index(f)+1,coding_order=i,pilot_previously_read=k in pids,status='PENDING',candidate_rows=len(by[k]),inherited_rows=len(accepted_by[k])))
dump('tables/Q3_coding_frame.csv',frame)
qc=[]
rng=random.Random(20260916)
for f in CONCRETE:
 kk=[k for k,j in J.items() if role(j)==f];bc=defaultdict(list)
 for k in sorted(kk):bc[J[k]['company_id']].append(k)
 for v in bc.values():rng.shuffle(v)
 cs=sorted(bc);rng.shuffle(cs);chosen=[];roundn=0
 while len(chosen)<min(len(kk),max(10,math.ceil(len(kk)*.2))):
  for c in cs:
   if roundn<len(bc[c]):chosen.append(bc[c][roundn])
   if len(chosen)>=min(len(kk),max(10,math.ceil(len(kk)*.2))):break
  roundn+=1
 for k in chosen:qc.append(dict(role=f,identity_key=k,reading_id=J[k]['reading_id'],company_id=J[k]['company_id'],reason='SEEDED_COMPANY_ROUND_ROBIN'))
dump('tables/Q_quality_review_sample.csv',qc)
print('Queue',len(final),Counter(r['origin'] for r in final),'inherited',sum(map(len,accepted_by.values())),'QC sample',len(qc))
