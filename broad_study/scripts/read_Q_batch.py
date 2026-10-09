from common import *
import sys
# Readable raw text, without exact repeated paragraphs already printed in an earlier
# calibration batch. This is a display transformation, never an extraction or coding rule.
# Receipt says GENERATED only. Researcher completion is recorded separately.
fi,lo,hi=map(int,sys.argv[1:4])
pilot=read(ROOT/'tables/Q_calibration_sample.csv')
prev=[r for r in pilot if (int(r['role_order']),int(r['pilot_order']))<(fi,lo)]
seen={}
def lines(t):return [s.strip() for s in (t or '').splitlines() if s.strip()]
def content(r):
 k=r['identity_key'];z=RAW[k];d=z.get('duties','') or '';q=z.get('requirements','') or '';out=[('duties',d)]
 if q and q not in d:out.append(('requirements',q))
 return out
for r in prev:
 for field,t in content(r):
  for s in lines(t):
   if len(s)>80:seen.setdefault(s,r['reading_id'])
selected=[r for r in pilot if int(r['role_order'])==fi and lo<=int(r['pilot_order'])<=hi]
out=[];receipt=[]
for r in selected:
 out.append('\n### '+r['pilot_order']+' '+r['reading_id']+' '+r['company_id']+' '+r['title'])
 ndup=0;refs=set()
 for field,t in content(r):
  out.append('['+field+']')
  pending=[]
  def flush():
   if pending:out.append('[与已读广告完全相同的连续原文 '+str(len(pending))+' 行；参见 '+', '.join(sorted(set(pending)))+']');pending.clear()
  for s in lines(t):
   if len(s)>80 and s in seen:
    pending.append(seen[s]);refs.add(seen[s]);ndup+=1
   else:
    flush();out.append(s)
    if len(s)>80:seen[s]=r['reading_id']
  flush()
 receipt.append(dict(identity_key=r['identity_key'],reading_id=r['reading_id'],role_order=fi,pilot_order=r['pilot_order'],exact_repeated_lines=ndup,references=sorted(refs),status='GENERATED_NOT_REVIEW_CERTIFICATE'))
name=f'Q_read_{fi:02d}_{lo:02d}_{hi:02d}'
(ROOT/f'notes/{name}.md').write_text('\n'.join(out),encoding='utf-8')
save_json(f'notes/{name}.json',receipt)
print('\n'.join(out))
