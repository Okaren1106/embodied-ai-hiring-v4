from common import *
import sys
ids=sys.argv[1:] or ['N0401','N0384','E0248','N0312','N0867','N0577','N0611','N0614']
out=[]
for rid in ids:
 matches=[(k,j) for k,j in J.items() if j['reading_id']==rid]
 for k,j in matches:
  out += ['\n## '+rid+' '+j['company_id']+' '+j['title']]
  seen=set()
  for f in ['duties','requirements','full_description']:
   lines=[]
   for line in (RAW[k].get(f) or '').splitlines():
    if line and line not in seen:lines.append(line);seen.add(line)
   if lines:out+=['['+f+']','\n'.join(lines)]
  out+=['ACT '+js([dict(label=a,relation=rel,quote=e['quote']) for a in ACTS for rel in ['OWNED','PARTICIPATES'] for e in AE[k,a,rel]])]
text='\n'.join(out)
(ROOT/'review/activity_boundary_packet.md').write_text(text,encoding='utf-8')
print(text)
