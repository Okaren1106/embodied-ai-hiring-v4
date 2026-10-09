from common import RAW, J, jobs
from pathlib import Path
out=[]
# find N0282
j=next(x for x in jobs if x['reading_id']=='N0282')
k=j['identity_key']
r=RAW[k]
out.append('jobs duties len='+str(len(j.get('duties') or '')))
out.append('RAW keys sample='+','.join(list(r.keys())[:40]))
for f in ['duties','requirements','full_description','title','jd_text','description','raw_text']:
    v=r.get(f)
    out.append(f+' type='+str(type(v).__name__)+' len='+str(len(v or '') if isinstance(v,str) else 'NA')+' val='+repr((v or '')[:200] if isinstance(v,str) else v))
# how many empty RAW ads in perception
empty=[]
from csv import DictReader
from pathlib import Path as P
frame=list(DictReader((P('../tables/Q3_coding_frame.csv')).open(encoding='utf-8-sig')))
pe=[x for x in frame if x['role']=='RF_PERCEPTION']
for row in pe:
    kk=row['identity_key']
    rr=RAW[kk]
    d=(rr.get('duties') or '')+(rr.get('requirements') or '')+(rr.get('full_description') or '')
    if not d.strip():
        empty.append(row['reading_id']+' title='+(rr.get('title') or J[kk].get('title') or ''))
out.append('perception empty RAW count='+str(len(empty)))
out.extend(empty)
Path('../notes/probe_n0282_raw.txt').write_text('\n'.join(out),encoding='utf-8')
print('ok', len(empty))
