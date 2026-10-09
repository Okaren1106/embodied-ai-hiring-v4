from common import jobs, RAW
from pathlib import Path
j = next(x for x in jobs if x['reading_id']=='N0282' or x.get('identity_key')=='N0282')
p = Path('../notes/probe_n0282.txt')
txt = []
txt.append('id='+j['identity_key'])
for f in ['title','duties','requirements','full_description']:
    t = j.get(f) or ''
    txt.append('=== '+f+' len='+str(len(t)))
    txt.append(t[:2000])
p.write_text('\n'.join(txt), encoding='utf-8')
print('wrote', p)
