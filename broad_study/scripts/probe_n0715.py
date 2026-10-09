from common import RAW, jobs
jsby={j['reading_id']:j for j in jobs}
j=jsby['N0715']; r=RAW[j['identity_key']]
open('../notes/probe_N0715.txt','w',encoding='utf-8').write((r.get('duties') or '')+'\n---REQ---\n'+(r.get('requirements') or ''))
print('duty',len(r.get('duties') or ''),'req',len(r.get('requirements') or ''))
