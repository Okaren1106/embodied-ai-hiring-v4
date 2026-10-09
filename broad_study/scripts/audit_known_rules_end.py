from astra_review_tools import *
from copy import deepcopy
eff={(e['identity_key'],e['evidence_id']):deepcopy(e) for e in E}
for t in transactions():
 for ch in t.get('evidence_overrides',[]):eff[t['identity_key'],ch['evidence_id']].update(ch)
for x in json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))['labels']:
 if x['code'] in ['V2_GIT','V2_MOCAP','V2_TCPIP','TC_MODEL_COMPRESSION','TC_POWER_ELECTRONICS']:print('DEF',x['code'],x['definition'],x['aliases'])
for rid in ['N0977','E0325','E0502']:
 print('\nFULL',rid);print(compact_packet([RID[rid]]))
print('\nMOCAP',[(e['evidence_id'],e['metric'],e['branch'],e['quote']) for e in EB[RID['N0063']] if e['code'].startswith('V2')])
for e in eff.values():
 if e['branch'] in ['TEST_OBJECT','SIMULATION_OR_TEST_OBJECT'] or (e['code'] in ['V2_EMC','V2_SI_PI'] and e['metric']=='DUTY_OWN_DEVELOP') or (e['code']=='TC_POWER_ELECTRONICS' and re.search('suppl|供应|电源',e['quote'],re.I) and e['metric'].startswith('DUTY')):
  print('CHECK',e['evidence_id'],e['code'],e['metric'],e['branch'],e['quote'])
for k,qs in QB.items():
 for q in qs:
  v=DOC[k]['new'][q['review_id'].split(':')[-1]]
  if isinstance(v,str) and v.startswith('REJECT') and (re.search('LoRA|QLoRA',q['quote'],re.I) or ('UDP' in q['quote'] and 'TCP' in v)):
   print('REJECT_CHECK',AD[k]['reading_id'],q['review_id'],v,q['quote'])
