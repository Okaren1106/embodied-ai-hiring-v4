from common import RAW, jobs
jsby={j['reading_id']:j for j in jobs}
j=jsby['N1020']; r=RAW[j['identity_key']]
open('../notes/probe_N1020.txt','w',encoding='utf-8').write((r.get('duties') or '')[:2000]+'\n---REQ---\n'+(r.get('requirements') or '')[:1500])
print('duty',len(r.get('duties') or ''))
