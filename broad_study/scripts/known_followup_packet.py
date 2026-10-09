from astra_review_tools import *
import sys
tx=transactions()
for rid in sys.argv[1:]:
 k=RID[rid];print('\n##',rid,J[k]['title'])
 for e in EB[k]:
  eff=dict(e)
  for t in tx:
   if t['identity_key']==k:
    for ch in t.get('evidence_overrides',[]):
     if ch['evidence_id']==e['evidence_id']:eff.update(ch)
  if eff['code'].startswith('TC_') or eff['code'] in ['V2_GIT','V2_TCPIP','SK_LINUX','SK_PYTHON']:
   print(eff['evidence_id'],eff['code'],eff['metric'],eff['branch'],eff['quote'])
 for t in tx:
  if t['identity_key']==k:
   for i,a in enumerate(t.get('additions',[]),1):print('ADD',t['batch'],i,js(a))
 for n,line in enumerate(RAW[k]['full_description'].splitlines(),1):
  if re.search('UDP|Git|git|mocap|MoCap|动捕|动作捕|安全|SOP|manufactur|real.time',line):print('F'+str(n),line)
