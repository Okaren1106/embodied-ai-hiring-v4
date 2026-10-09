"""Show E0190 Linux sentences."""
from common import RAW, J
ks=[k for k,j in J.items() if j['reading_id']=='E0190']
k=ks[0]
raw=RAW[k]
out=[]
for f in ['duties','requirements','full_description']:
    t=raw.get(f) or ''
    out.append('==== '+f+' len='+str(len(t)))
    for needle in ['Linux','linux','LINUX']:
        i=0
        while True:
            j=t.find(needle,i)
            if j<0: break
            out.append(repr(t[max(0,j-40):j+80]))
            i=j+1
from pathlib import Path
Path(__file__).resolve().parents[1].joinpath('notes/e0190_linux.txt').write_text('\n'.join(out), encoding='utf-8')
print('ok', len(out))
