from common import *
lock_check()
scopes={'ALL24':ALL,'WHOLE23':WHOLE,'ACTIVITY_COMPLETE_COMPANIES':FULL}
dump('source_subset.csv',[{'company_id':c,'n_ads':CO[c]['n_ads'],'source_unassessable_activities':CO[c]['activities_SOURCE_UNASSESSABLE'],'activity_complete_subset':c in FULL,'whole_company':c in WHOLE,'board_coverage_status':'NOT_CONFIRMED_ALL_CHANNELS','reason':'既有全部广告活动可判读且整公司' if c in FULL else '团队或活动来源不足','source': 'inputs/stage_c/tables/T1_company_sample.csv'} for c in ALL])
q1=[];q3=[];cross=[];company_role=[]
for scope,cs in scopes.items():
 for r in ROLES:
  q1.append({'scope':scope,'role':r,'role_name':RN[r],**distribution([(c,sum(role(J[k])==r for k in ids([c])),len(ids([c]))) for c in cs])})
 for a in ACTS:
  q3.append({'scope':scope,'activity':a,'activity_name':AN[a],**distribution([(c,len(ids([c],True)&OWN[a]),len(ids([c],True))) for c in cs])})
 for r,a in itertools.product(ROLES,ACTS):
  elig=ids(cs,True);ri={k for k in elig if role(J[k])==r};pi=elig&OWN[a]
  cross.append({'scope':scope,'role':r,'role_name':RN[r],'activity':a,'activity_name':AN[a],'P':len(ri&pi),'role_activity_interpretable_N':len(ri),'activity_positive_N':len(pi),'activity_within_role':ratio(len(ri&pi),len(ri)),'role_within_activity':ratio(len(ri&pi),len(pi)),'positive_ids_json':js(sorted(ri&pi))})
for c,r,a in itertools.product(ALL,ROLES,ACTS):
 ci=ids([c],True);ri={k for k in ci if role(J[k])==r}
 company_role.append({'company_id':c,'role':r,'role_name':RN[r],'activity':a,'P':len(ri&OWN[a]),'role_N':len(ri),'company_activity_N':len(ci),'role_share_in_company':ratio(len(ri),len(ci)),'activity_within_role':ratio(len(ri&OWN[a]),len(ri)),'small_n_under10':0<len(ri)<10})
dump('Q1_company_coverage.csv',q1);dump('Q3_company_coverage.csv',q3);dump('role_activity_bidirectional.csv',cross);dump('company_role_activity.csv',company_role)
dump('cross_company_points.csv',[{'company_id':c,'activity':a,'role':r,'P':len(ids([c],True)&OWN[a]&{k for k in J if role(J[k])==r}),'activity_P':len(ids([c],True)&OWN[a])} for c,r,a in itertools.product(ALL,ROLES,ACTS)])
# Every pair is retained even if there are no common roles. Qualification depends only on counts and background.
candidates=[];standard=[]
for c1,c2 in itertools.combinations(WHOLE,2):
 i1,i2=ids([c1],True),ids([c2],True)
 nr1={r:len([k for k in i1 if role(J[k])==r]) for r in CONCRETE};nr2={r:len([k for k in i2 if role(J[k])==r]) for r in CONCRETE}
 K=[r for r in CONCRETE if min(nr1[r],nr2[r])>=10];n1=sum(nr1[r] for r in K);n2=sum(nr2[r] for r in K)
 common_scenes=sorted(set(json.loads(CO[c1]['current_scenes_json']))&set(json.loads(CO[c2]['current_scenes_json'])))
 rec={'company1':c1,'company2':c2,'same_wave':CO[c1]['observation_dates']==CO[c2]['observation_dates'],'common_scenes_json':js(common_scenes),'same_supply':CO[c1]['stratum']==CO[c2]['stratum'],'known_multiproduct':any(CO[c]['known_multi_product']=='YES' for c in [c1,c2]),'K_json':js(K),'n_common_roles':len(K),'coverage1_N':n1,'company1_N':len(i1),'coverage1_share':ratio(n1,len(i1)),'coverage2_N':n2,'company2_N':len(i2),'coverage2_share':ratio(n2,len(i2)),'standardization_eligible':len(K)>=2,'eligibility_reason':'PASS' if len(K)>=2 else 'FEWER_THAN_TWO_COMMON_ROLES_EACH_N10'}
 candidates.append(rec)
 if len(K)<2:continue
 for a in ACTS:
  ar1={r:ratio(len({k for k in i1 if role(J[k])==r}&OWN[a]),nr1[r]) for r in K};ar2={r:ratio(len({k for k in i2 if role(J[k])==r}&OWN[a]),nr2[r]) for r in K}
  for weight in ['OWN_K','EQUAL_K','POOLED_K']:
   w1={r:nr1[r]/n1 if weight=='OWN_K' else 1/len(K) if weight=='EQUAL_K' else (nr1[r]+nr2[r])/(n1+n2) for r in K}
   w2={r:nr2[r]/n2 if weight=='OWN_K' else w1[r] for r in K}
   p1=sum(ar1[r]*w1[r] for r in K);p2=sum(ar2[r]*w2[r] for r in K)
   standard.append({**rec,'activity':a,'weight':weight,'rate1':p1,'rate2':p2,'difference1_minus2':p1-p2,'overall1':ratio(len(i1&OWN[a]),len(i1)),'overall2':ratio(len(i2&OWN[a]),len(i2))})
dump('case_candidate_coverage.csv',candidates);dump('common_role_standardization_all_eligible.csv',standard)
q2=read(C/'tables/T3_company_context.csv');sel=[r for r in q2 if r['main_display']=='YES'];q2out=[];q2agg=[]
for r in sel:
 p,b,u,n=[int(r[x]) for x in ['n_positive','n_base','n_relation_unknown','n_interpretable']]
 assert b==n+u and p<=n
 q2out.append({**r,'unknown_low':ratio(p,b),'unknown_high':ratio(p+u,b),'Z':n-p})
for key,items in itertools.groupby(sorted(sel,key=lambda r:(r['role_code'],r['dimension'],r['label_code'],r['metric_bucket'],r['branch_bucket'])),lambda r:(r['role_code'],r['dimension'],r['label_code'],r['metric_bucket'],r['branch_bucket'])):
 rr=list(items)
 for scope,cs in scopes.items():
  chosen=[r for r in rr if r['company_id'] in cs];pts=[(r['company_id'],int(r['n_positive']),int(r['n_interpretable'])) for r in chosen if int(r['n_base'])>0];d=distribution(pts);bs=sum(int(r['n_base']) for r in chosen);us=sum(int(r['n_relation_unknown']) for r in chosen)
  eligible=d['n_interpretable_companies']>=3 and d['N']>=20
  q2agg.append(dict(zip(['role','dimension','label','metric','branch'],key))|{'scope':scope,'base_B':bs,'unknown_U':us,'unknown_low_ad':ratio(d['P'],bs),'unknown_high_ad':ratio(d['P']+us,bs),'unknown_low_equal':statistics.mean([int(r['n_positive'])/int(r['n_base']) for r in chosen if int(r['n_base'])]) if bs else None,'unknown_high_equal':statistics.mean([(int(r['n_positive'])+int(r['n_relation_unknown']))/int(r['n_base']) for r in chosen if int(r['n_base'])]) if bs else None,'aggregate_eligible':eligible,**d})
dump('Q2_company_fixed_points_unknown.csv',q2out);dump('Q2_fixed_coverage_unknown.csv',q2agg)
print('COUNTS',{'concrete':len(CONCRETE),'activity_complete_companies':FULL,'standardization_pairs':sum(x['standardization_eligible'] for x in candidates),'table_rows':[len(q1),len(q3),len(cross),len(company_role),len(q2out),len(q2agg)]})
print('CANDIDATES with same wave and common scenes')
for r in candidates:
 if r['same_wave'] and r['common_scenes_json']!='[]':print(r['company1'],r['company2'],r['common_scenes_json'],r['n_common_roles'],r['coverage1_N'],r['coverage2_N'],r['known_multiproduct'])
