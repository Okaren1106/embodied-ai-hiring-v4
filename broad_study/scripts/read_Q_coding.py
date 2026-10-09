from common import *
import sys,unicodedata,hashlib
fidx,lo,hi=map(int,sys.argv[1:4])
frame=read(ROOT/'tables/Q3_coding_frame.csv')
sel=[r for r in frame if int(r['role_order'])==fidx and lo<=int(r['coding_order'])<=hi]
qq=json.loads((ROOT/'notes/Q_semantic_review_queue.json').read_text(encoding='utf-8'))
old=json.loads((ROOT/'notes/Q_inherited_semantics_all17.json').read_text(encoding='utf-8'))
byq=defaultdict(list);byo=defaultdict(list)
for r in qq:byq[r['identity_key']].append(r)
for r in old:byo[r['identity_key']].append(r)
pilot={r['identity_key'] for r in read(ROOT/'tables/Q_calibration_sample.csv')}
# Punctuation may distinguish lists, examples and alternatives. Preserve it.
norm=lambda t:''.join(c for c in unicodedata.normalize('NFKC',t) if not c.isspace())
force_full='--full' in sys.argv
seen={}
for k in pilot:
 for field in ['full_description','duties','requirements']:
  for line in (RAW[k].get(field) or '').splitlines():
   if len(line)>60:seen[norm(line)]=J[k]['reading_id']
# Only prior officially completed coding may supply additional duplicate references.
completed=ROOT/'configs/Q_adjudications'
if completed.exists():
 for p in completed.glob('*.json'):
  d=json.loads(p.read_text(encoding='utf-8'))
  for rid,a in d.get('ads',{}).items():
   if a.get('status')!='CODED_FIRST_PASS':continue
   k=a['identity_key']
   for field in ['full_description','duties','requirements']:
    for line in (RAW[k].get(field) or '').splitlines():
     if len(line)>60:seen[norm(line)]=rid
out=[]
for r in sel:
 k=r['identity_key'];j=J[k]
 qrefs={};line_number=0
 out.append('\n## '+r['coding_order']+' '+j['reading_id']+' '+j['company_id']+' '+j['title'])
 if k not in pilot or force_full:
  local=set()
  for field in ['full_description','duties','requirements']:
   lines=[]
   for line in (RAW[k].get(field) or '').splitlines():
    n=norm(line)
    if not n or n in local:continue
    local.add(n)
    if not force_full and len(line)>60 and n in seen and seen[n]!=j['reading_id']:
     preview=line[:100]
     lines.append('[仅空白/全半角归一相同，已读：'+seen[n]+'；段落SHA256前12位 '+hashlib.sha256(n.encode('utf-8')).hexdigest()[:12]+'；起句：'+preview+('…' if len(line)>100 else '')+']')
    else:
     line_number+=1;qrefs[line]=f'L{line_number}'
     lines.append(f'L{line_number} '+line);seen[n]=j['reading_id']
   if lines:out.append('['+field+']\n'+'\n'.join(lines))
 else:out.append('[校准全文此前已完整阅读；此处进行逐提及正式审读]')
 out.append('### 继承标签候选（仍需语境复核）')
 for n,v in enumerate(byo[k],1):
  out.append(f"O{n} {v['code']} {v['suggested_metric']}/{v['suggested_branch']} {v['prior_relation']} [{v['field']}@{v['start']}] | {qrefs.get(v['quote'],v['quote'])}")
 out.append('### 新增与目录外候选（不是正例；空目录仍须处理）')
 for v in byq[k]:
  surface='' if v['surface']==v['quote'] else f" [surface: {v['surface']}]"
  out.append(f"{v['review_id']} {' '.join(v['candidate_codes']) or '[目录外]'} {v['suggested_metric']}/{v['suggested_branch']} {v['prior_relation']} [{v['field']}@{v['start']}] | {qrefs.get(v['quote'],v['quote'])}{surface}")
name=f'Q_coding_{fidx:02d}_{lo:03d}_{hi:03d}.md'
(ROOT/'notes'/name).write_text('\n'.join(out),encoding='utf-8')
print('\n'.join(out))
