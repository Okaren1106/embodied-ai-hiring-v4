from common import *
targets=['CN_XSQUARE','US_FIGURE','US_NIMBLE','US_PICKLE','US_DEXTERITY','US_BOSTON_DYNAMICS']
ev=read(B/'company_evidence.csv')
for c in targets:
 print('\nCOMPANY',c)
 for e in ev:
  if e['company_id']==c and not any(w in e['field'].lower() for w in ['capital','listing','valuation','funding']):
   print(e['evidence_id'],e['publication_date'],e['event_date'],e['source_nature'],e['url'],e['snapshot_text_path']);print('CLAIM',e['claim'][:1200])
print('\nRAW COOWN STRUCTURES')
for s in structures:
 k=s['identity_key']; aa=[a for a in ACTS if k in OWN[a]]
 if len(aa)>1:
  print(s['reading_id'],s['company_id'],s['root_relation'],s['title'],aa)
  if s['root_relation']!='ALL':print(RAW[k]['full_description'] or RAW[k]['duties'])
print('\nLABELS',ACTS)
print('RAW RECORD KEYS',list(raw[0]['record']))
