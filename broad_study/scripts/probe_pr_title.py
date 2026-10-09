from common import RAW, jobs
from pathlib import Path
ids=['E0438','N0864','N0872','N0818','N0819','N0741']
js={j['reading_id']:j for j in jobs}
out=[]
for rid in ids:
    k=js[rid]['identity_key']
    r=RAW[k]
    out.append('==== '+rid+' title='+(r.get('title') or ''))
    out.append('DUTY '+(r.get('duties') or '')[:500])
    out.append('REQ '+(r.get('requirements') or '')[:300])
    out.append('')
Path('../notes/probe_pr_title.txt').write_text('\n'.join(out),encoding='utf-8')
print('ok')
