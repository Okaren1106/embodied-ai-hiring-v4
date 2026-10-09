"""Independent NumPy reconstruction from every state, not the aggregate code.
Does not import astra_stats or reuse sparse counters from the production path.
"""
from common import *
import numpy as np
from datetime import datetime,timezone

ads=read(ROOT/'tables/Q3_ads_final.csv');AD={a['identity_key']:a for a in ads}
cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
CD={x['code']:x for x in cat['labels']};CBR=defaultdict(list)
for c,l in CD.items():
 for r in l['applicable_roles']:CBR[r].append(c)
rules=json.loads((ROOT/'configs/Q_coding_rules_v2.json').read_text(encoding='utf-8'))
slices=[(s['metric'],s['branch']) for s in rules['legacy_14_slices']]+[(m,b) for m in ['DUTY_OWN_USE','DUTY_OWN_DEVELOP'] for b in ['CHOICE','EXAMPLE','CHOICE_AND_EXAMPLE','CONDITIONAL']]
K={r:sorted(k for k,a in AD.items() if a['role']==r) for r in CBR};KI={r:{k:i for i,k in enumerate(ks)} for r,ks in K.items()}
COL={r:{(c,m,b):i for i,(c,m,b) in enumerate((c,m,b) for c in sorted(cs) for m,b in slices)} for r,cs in CBR.items()}
M={r:np.full((len(K[r]),len(COL[r])),255,dtype=np.uint8) for r in CBR};state_codes={'Z':0,'P':1,'U':2,'NA':3,'SOURCE_EXCLUDED':4}
ns=0
with (ROOT/'tables/Q3_states_final.csv').open(encoding='utf-8-sig',newline='') as f:
 for a in csv.DictReader(f):
  r=a['role'];i=KI[r][a['identity_key']];j=COL[r][a['label_code'],a['metric'],a['branch']]
  assert M[r][i,j]==255,'Duplicate state'
  assert a['company_id']==AD[a['identity_key']]['company_id'] and a['task']==AD[a['identity_key']]['task']
  M[r][i,j]=state_codes[a['state']];ns+=1
for r in M:assert not np.any(M[r]==255),'Missing states '+r
mem=defaultdict(set)
for a in read(ROOT/'tables/Q4_scope_membership.csv'):
 assert a['identity_key'] not in mem[a['scope']]
 mem[a['scope']].add(a['identity_key'])
for a in read(ROOT/'tables/Q4_scope_definitions.csv'):mem[a['scope']]
COIDS={r:sorted({AD[k]['company_id'] for k in K[r]}) for r in K}
CIX={r:{c:i for i,c in enumerate(cs)} for r,cs in COIDS.items()}
CM={r:np.array([[AD[k]['company_id']==c for k in K[r]] for c in cs],dtype=np.int16) for r,cs in COIDS.items()}
boolstates={r:{s:(mat==n).astype(np.int16) for s,n in state_codes.items()} for r,mat in M.items()}
def divide(x,y):
 return np.divide(x,y,out=np.full(np.broadcast_shapes(x.shape,y.shape),np.nan),where=y!=0)
def expected(r,ks):
 include=np.array([k in ks for k in K[r]],dtype=np.int16);mask=CM[r]*include
 pts={s:mask@v for s,v in boolstates[r].items()}
 pts['total_ads']=np.broadcast_to(mask.sum(axis=1,keepdims=True),pts['P'].shape)
 pts['N']=pts['P']+pts['Z'];pts['B']=pts['N']+pts['U']
 pts['share']=divide(pts['P'],pts['N']);pts['unknown_low']=divide(pts['P'],pts['B']);pts['unknown_high']=divide(pts['P']+pts['U'],pts['B'])
 pts['small_n']=np.where((pts['N']>0)&(pts['N']<10),'YES','NO')
 a={s:pts[s].sum(axis=0) for s in ['total_ads','P','Z','U','NA','SOURCE_EXCLUDED','N','B']}
 a['n_companies']=(pts['N']>0).sum(axis=0);a['n_positive_companies']=(pts['P']>0).sum(axis=0)
 gate=(a['n_companies']>=3)&(a['N']>=20);a['gate']=np.where(gate,'EXPLORATORY_SUMMARY','POINTS_ONLY')
 a['small_n_companies']=(pts['small_n']=='YES').sum(axis=0)
 a['share_ad_weighted']=np.where(gate,divide(a['P'],a['N']),np.nan)
 a['share_company_equal']=np.where(gate,divide(np.nansum(pts['share'],axis=0),a['n_companies']),np.nan)
 a['unknown_low_ad']=np.where(gate,divide(a['P'],a['B']),np.nan)
 a['unknown_high_ad']=np.where(gate,divide(a['P']+a['U'],a['B']),np.nan)
 a['unknown_low_company']=np.where(gate,divide(np.nansum(pts['unknown_low'],axis=0),(pts['B']>0).sum(axis=0)),np.nan)
 a['unknown_high_company']=np.where(gate,divide(np.nansum(pts['unknown_high'],axis=0),(pts['B']>0).sum(axis=0)),np.nan)
 for s,n in [('P','positive'),('N','denominator')]:
  a['max_'+n+'_count']=pts[s].max(axis=0)
  a['max_'+n+'_contribution']=divide(a['max_'+n+'_count'],a[s])
 a['dominance_warning']=np.where(a['max_positive_contribution']>.5,'YES','NO')
 return a,pts
EX={};TX={}
for s,ks in mem.items():
 for r in K:EX[s,r]=expected(r,ks)
for r in K:
 for t in sorted({AD[k]['task'] for k in K[r]}):
  ks={k for k in K[r] if AD[k]['task']==t and k in mem['WHOLE23']}
  if ks:TX[r,t]=expected(r,ks)
print('Independent matrices built',ns,flush=True)
issues=[];bad=Counter();counts={};checks=0
def fail(table,key,field,actual,want):
 bad[table]+=1
 if len(issues)<100:issues.append(dict(table=table,key=str(key),field=field,actual=str(actual),expected=str(want)))
def compare(table,key,rec,want):
 global checks
 for f,v in want.items():
  checks+=1;a=rec[f]
  if isinstance(v,(list,tuple)):ok=json.loads(a)==list(v)
  elif isinstance(v,(str,np.str_)):ok=a==v
  elif np.isnan(v):ok=a==''
  else:
   try:ok=abs(float(a)-float(v))<1e-10
   except (ValueError,TypeError):ok=False
  if not ok:fail(table,key,f,a,v)
def aggregate_wanted(r,col,arr,pts):
 want={f:v[col] for f,v in arr.items()}
 for st,name in [('P','positive'),('N','denominator')]:
  mx=want['max_'+name+'_count'];want['max_'+name+'_companies']=[co for i,co in enumerate(COIDS[r]) if pts[st][i,col]==mx] if mx else []
 return want
def rows(name):
 with (ROOT/'tables'/name).open(encoding='utf-8-sig',newline='') as f:yield from csv.DictReader(f)
for name in ['Q4_aggregates_final.csv','Q4_display_cells_final.csv','Q4_task_strata_final.csv']:
 n=0
 for rec in rows(name):
  r=rec['role'];col=COL[r][rec['label_code'],rec['metric'],rec['branch']]
  pair=TX[r,rec['task']] if 'task' in rec else EX[rec['scope'],r]
  compare(name,(rec['scope'],r,rec.get('task',''),col),rec,aggregate_wanted(r,col,*pair));n+=1
 counts[name]=n;print(name,n,'issues',bad[name],flush=True)
for name in ['Q4_company_points_final.csv','Q4_task_company_points_final.csv']:
 n=0
 for rec in rows(name):
  r=rec['role'];col=COL[r][rec['label_code'],rec['metric'],rec['branch']];i=CIX[r][rec['company_id']]
  arr,pts=TX[r,rec['task']] if 'task' in rec else EX[rec['scope'],r]
  compare(name,(r,rec.get('task',''),col,rec['company_id']),rec,{f:v[i,col] for f,v in pts.items()});n+=1
 counts[name]=n;print(name,n,'issues',bad[name],flush=True)
# LOO recomputed by removing a whole company from the independent state matrices.
LOO={};n=0
for rec in rows('Q4_leave_one_company_out_final.csv'):
 r=rec['role'];drop=rec['removed_company'];col=COL[r][rec['label_code'],rec['metric'],rec['branch']]
 if (r,drop) not in LOO:LOO[r,drop]=expected(r,{k for k in mem['WHOLE23'] if AD[k]['company_id']!=drop})
 compare('Q4_leave_one_company_out_final.csv',(r,col,drop),rec,aggregate_wanted(r,col,*LOO[r,drop]));n+=1
counts['Q4_leave_one_company_out_final.csv']=n
# Completeness of the two full Cartesian aggregate tables and full main points.
expected_agg=sum(len(COL[r]) if not s.startswith('DIRECT_') else sum(CD[c]['legacy_dimension']==s[7:] for c in CBR[r])*len(slices) for s in mem for r in K)
assert counts['Q4_aggregates_final.csv']==expected_agg
assert counts['Q4_task_strata_final.csv']==sum(len(COL[r]) for r,t in TX)
assert counts['Q4_company_points_final.csv']==sum(len({AD[k]['company_id'] for k in K[r] if k in mem['WHOLE23']})*len(COL[r]) for r in K)
out=dict(status='PASS' if not sum(bad.values()) else 'FAIL',method='Independent dense state matrices and NumPy company membership products; no production summary function imported',state_rows=ns,tables=counts,scalar_checks=checks,errors=dict(bad),first_issues=issues,created_utc=datetime.now(timezone.utc).isoformat())
save_json('verification/astra_independent_numeric.json',out)
print(js(out),flush=True)
assert not sum(bad.values()),'Independent numeric verification failed'
