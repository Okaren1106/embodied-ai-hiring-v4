"""Independently reconstruct sparse states and exercise the real resolver's exclusion path."""
from astra_review_tools import *
from copy import deepcopy
import ast
tx=transactions();ee={(e['identity_key'],e['evidence_id']):deepcopy(e) for e in E};lims=defaultdict(list)
for t in tx:
 k=t['identity_key'];lims[k]+=t.get('source_limits',[])
 for ch in t.get('evidence_overrides',[]):
  for f in ['code','metric','branch','affected_metrics']:
   if f in ch:ee[k,ch['evidence_id']][f]=ch[f]
 for i,a in enumerate(t.get('additions',[]),1):ee[k,t['reading_id']+':ASTRA:'+t['batch']+':'+str(i)]=dict(a,identity_key=k)
 for ch in t.get('transaction_overrides',[]):
  key=(k,t['reading_id']+':ASTRA:'+ch['target_batch']+':'+str(ch['target_addition_index']))
  for f in ['code','metric','branch','affected_metrics','excluded_from_catalog']:
   if f in ch:ee[key][f]=ch[f]
rules=json.loads((ROOT/'configs/Q_coding_rules_v2.json').read_text(encoding='utf-8'))
slices=[(x['metric'],x['branch']) for x in rules['legacy_14_slices']]+[(m,b) for m in ['DUTY_OWN_USE','DUTY_OWN_DEVELOP'] for b in ['CHOICE','EXAMPLE','CHOICE_AND_EXAMPLE','CONDITIONAL']]
catalog=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))['labels']
codes={r:{c['code'] for c in catalog if r in c['applicable_roles']} for r in CONCRETE}
expected={}
# Apply each priority in reverse order: U, NA, excluded, P.
for (k,eid),e in ee.items():
 if e.get('excluded_from_catalog'):continue
 affected=e.get('affected_metrics') or []
 if isinstance(affected,str):affected=json.loads(affected)
 for m,b in slices:
  hit=e['metric']==m and e['branch']=='UNRESOLVED'
  hit |= e['metric']=='UNKNOWN' and (m in affected or m+'_'+b in affected) and e['branch'] in ['UNRESOLVED',b]
  if hit:expected[k,e['code'],m,b]='U'
for k,a in AD.items():
 for c in codes[a['role']]:
  for m,b in slices:
   if DOC[k].get('not_applicable',{}).get(c):expected[k,c,m,b]='NA'
   for limit in lims[k]:
    targets=limit['codes']
    if (targets=='ALL_APPLICABLE' or 'ALL_APPLICABLE' in targets or c in targets) and m in limit['metrics']:expected[k,c,m,b]='SOURCE_EXCLUDED'
for (k,eid),e in ee.items():
 if not e.get('excluded_from_catalog') and (e['metric'],e['branch']) in slices:expected[k,e['code'],e['metric'],e['branch']]='P'
seen=set();counts=Counter();n=0
with (ROOT/'tables/Q3_states_final.csv').open(encoding='utf-8-sig',newline='') as f:
 for s in csv.DictReader(f):
  key=(s['identity_key'],s['label_code'],s['metric'],s['branch'])
  assert s['state']==expected.get(key,'Z'),(key,s['state'],expected.get(key,'Z'))
  if s['state']!='Z':seen.add(key)
  n+=1;counts[s['state']]+=1
assert seen==set(expected)
assert n==sum(len(codes[a['role']])*len(slices) for a in AD.values())
# Extract exactly the production resolve function without executing its file.
tree=ast.parse((ROOT/'scripts/materialize_astra_final.py').read_text(encoding='utf-8'))
func=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='resolve')
g={'grouped':defaultdict(list),'limits':defaultdict(list),'DOC':{'a':{'not_applicable':{}}}}
exec(compile(ast.Module(body=[func],type_ignores=[]),'production_resolver','exec'),g)
res=g['resolve'];tests=[]
def check(name,want,m='GENERAL',b='UNCONDITIONAL'):
 assert res('a','x',m,b)[0]==want,name;tests.append(name)
check('readable_absence','Z')
g['limits']['a']=[{'codes':'ALL_APPLICABLE','metrics':['GENERAL'],'reason':'cut'}];check('string_all_scope','SOURCE_EXCLUDED');check('unaffected_context','Z','DUTY_OWN_USE')
g['limits']['a'][0]['codes']=['ALL_APPLICABLE'];check('list_all_scope','SOURCE_EXCLUDED')
g['limits']['a'][0]['codes']=['other'];check('unaffected_label','Z')
g['limits']['a'][0]['codes']=['x'];check('specific_label_scope','SOURCE_EXCLUDED')
g['grouped']['a','x']=[dict(metric='GENERAL',branch='UNCONDITIONAL')];check('positive_survives_local_truncation','P')
g['grouped']['a','x']=[];g['limits']['a']=[];g['DOC']['a']['not_applicable']['x']='outside';check('explicit_na','NA')
g['DOC']['a']['not_applicable']={};g['grouped']['a','x']=[dict(metric='GENERAL',branch='UNRESOLVED')];check('unresolved_branch','U');check('unresolved_other_metric','Z','PREFERRED');check('unresolved_example','U',b='EXAMPLE')
g['grouped']['a','x']=[dict(metric='UNKNOWN',branch='UNRESOLVED',affected_metrics=['GENERAL_EXAMPLE'])];check('scoped_unknown_does_not_spread','Z');check('scoped_unknown_target','U',b='EXAMPLE')
save_json('verification/V3_independent_state_resolution.json',dict(status='PASS',rows=n,state_counts=dict(counts),nonzero_states=len(expected),resolver_fixtures=tests,method='Independent sparse evidence replay, reverse-priority state construction; production resolver extracted for scoped source-exclusion fixtures. Not a semantic accuracy test.'))
print('PASS',n,'states',len(tests),'resolver fixtures')
