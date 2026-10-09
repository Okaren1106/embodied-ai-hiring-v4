from common import *
import re
lock_check()
cases=json.loads((ROOT/'evidence/case_selection.json').read_text(encoding='utf-8'))['cases'];cs=[c for x in cases for c in x['companies']]
ex={r['identity_key'] for r in read(ROOT/'tables/case_explicit_campus_internship.csv')};drop=set()
for r in read(ROOT/'tables/case_exact_duty_duplicates.csv'):drop.update(set(json.loads(r['ids_json']))-{r['retained_id']})
subsets={'MAIN':set(J),'NO_EXPLICIT_CAMPUS_ELIGIBLE_OR_INTERN':set(J)-ex,'EXACT_DUTY_TEMPLATE_ONE':set(J)-drop}
cross=[];stand=[];coverage=[]
for case in cases:
 c1,c2=case['companies']
 for scope,allowed in subsets.items():
  ss={c:ids([c],True)&allowed for c in [c1,c2]};K=[r for r in CONCRETE if all(sum(role(J[k])==r for k in ss[c])>=10 for c in ss)]
  nn={c:{r:sum(role(J[k])==r for k in ss[c]) for r in K} for c in ss}
  for c in ss:coverage.append({'case_id':case['case_id'],'scope':scope,'company_id':c,'K_json':js(K),'n_K':len(K),'eligible':len(K)>=2,'coverage_N':sum(nn[c].values()),'company_N':len(ss[c]),'coverage_share':ratio(sum(nn[c].values()),len(ss[c]))})
  for a in ACTS:
   if len(K)>=2:
    rr={c:{r:ratio(len({k for k in ss[c] if role(J[k])==r}&OWN[a]),nn[c][r]) for r in K} for c in ss}
    for weight in ['OWN_K','EQUAL_K','POOLED_K']:
     vals={}
     for c in ss:
      w={r:nn[c][r]/sum(nn[c].values()) if weight=='OWN_K' else 1/len(K) if weight=='EQUAL_K' else (nn[c1][r]+nn[c2][r])/(sum(nn[c1].values())+sum(nn[c2].values())) for r in K}
      vals[c]=sum(rr[c][r]*w[r] for r in K)
     stand.append({'case_id':case['case_id'],'scope':scope,'activity':a,'weight':weight,'company1':c1,'company2':c2,'rate1':vals[c1],'rate2':vals[c2],'difference1_minus2':vals[c1]-vals[c2],'K_json':js(K),'eligible':True})
   else:stand.append({'case_id':case['case_id'],'scope':scope,'activity':a,'weight':'NOT_APPLICABLE','company1':c1,'company2':c2,'rate1':None,'rate2':None,'difference1_minus2':None,'K_json':js(K),'eligible':False})
 for scope,group in [(case['case_id'],[c1,c2]),(c1,[c1]),(c2,[c2])]:
  ai=ids(group,True)
  for r,a in itertools.product(ROLES,ACTS):
   ri={k for k in ai if role(J[k])==r};pi=ai&OWN[a]
   cross.append({'scope':scope,'role':r,'activity':a,'P':len(ri&pi),'role_N':len(ri),'activity_P':len(pi),'activity_within_role':ratio(len(ri&pi),len(ri)),'role_within_activity':ratio(len(ri&pi),len(pi)),'positive_ids_json':js(sorted(ri&pi))})
dump('case_role_activity_bidirectional.csv',cross);dump('case_standardization_sensitivity.csv',stand);dump('case_common_role_coverage_sensitivity.csv',coverage)
ll=read(C/'tables/T3_positive_unknown_lineage.csv');ls=collections.defaultdict(dict)
for r in ll:ls[(r['company_id'],r['role_code'],r['dimension'],r['label_code'],r['metric_bucket'],r['branch_bucket'])][r['identity_key']]=r['state']
q2=[]
for r in read(ROOT/'tables/T5_case_Q2_all_fixed_contexts.csv'):
 for scope,allowed in subsets.items():
  base={k for k,j in J.items() if j['company_id']==r['company_id'] and j['primary_status']=='CODED' and j['primary_code']==r['role_code'] and j['skills_status' if r['dimension']=='skills' else 'technical_status']!='SOURCE_UNASSESSABLE'}&allowed
  states=ls[(r['company_id'],r['role_code'],r['dimension'],r['label_code'],r['metric_bucket'],r['branch_bucket'])];p=sum(states.get(k)=='PRESENT' for k in base);u=sum(states.get(k)=='UNKNOWN' for k in base);n=len(base)-u
  q2.append({k:r[k] for k in ['case_id','company_id','role_code','dimension','label_code','metric_bucket','branch_bucket']}|{'scope':scope,'P':p,'B':len(base),'U':u,'N':n,'share':ratio(p,n),'unknown_low':ratio(p,len(base)),'unknown_high':ratio(p+u,len(base)),'small_n_under10':0<n<10})
dump('case_Q2_audience_template_unknown.csv',q2)
print('case subset standardization deployment',[(r['case_id'],r['scope'],r['weight'],r['rate1'],r['rate2']) for r in stand if r['activity']=='ACT_DEPLOYMENT'])
