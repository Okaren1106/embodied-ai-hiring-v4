from common import *
import re
lock_check()
SPECIAL={'ACT_RESEARCH':'RF_RESEARCH_SCIENCE','ACT_DEPLOYMENT':'RF_DEPLOYMENT_FIELD_SERVICE','ACT_QUALITY':'RF_MANUFACTURING_QUALITY_SUPPLY'}
scopes={'ALL24':ALL,'WHOLE23':WHOLE,'ACTIVITY_COMPLETE_COMPANIES':FULL,'EXCLUDE_KNOWN_MULTIPRODUCT':[c for c in WHOLE if CO[c]['known_multi_product']!='YES']}
for c in WHOLE:scopes['LOO_'+c]=[x for x in WHOLE if x!=c]
res=[]
for scope,cs in scopes.items():
 for a,r in SPECIAL.items():
  ai=ids(cs,True)&OWN[a];ded={k for k in ai if role(J[k])==r};other={k for k in ai if role(J[k]) in CONCRETE and role(J[k])!=r};struc={k for k in ai if role(J[k]) in {x['primary_code'] for x in structures}};unknown=ai-ded-other-struc
  for denominator in ['ALL_ACTIVITY_POSITIVE','CONCRETE_PRIMARY_ONLY']:
   d=ai if denominator=='ALL_ACTIVITY_POSITIVE' else other|ded;pos=d-ded;pts=[(c,len([k for k in pos if J[k]['company_id']==c]),len([k for k in d if J[k]['company_id']==c])) for c in cs if any(J[k]['company_id']==c for k in d)]
   res.append({'scope':scope,'activity':a,'dedicated_role':r,'denominator':denominator,'dedicated':len(ded),'other_concrete':len(other),'structural':len(struc),'unclear_primary':len(unknown),'outside_lower_if_unclear_dedicated':ratio(len(other|struc),len(ai)),'outside_upper_if_unclear_elsewhere':ratio(len(ai-ded),len(ai)),**distribution(pts)})
dump('H1_cross_function_sensitivity.csv',res)
# Source-missing scenarios are activity-specific, not estimates of missing recruitment advertisements.
q3bound=[]
for scope,cs in scopes.items():
 for a in ACTS:
  points=[]
  for c in cs:
   base=ids([c]);valid=base&admitted;p=len(valid&OWN[a]);u=len(base-valid)
   points.append({'company_id':c,'P':p,'B':len(base),'U':u,'N':len(valid),'low':ratio(p,len(base)),'high':ratio(p+u,len(base))})
  p=sum(x['P'] for x in points);u=sum(x['U'] for x in points);b=sum(x['B'] for x in points)
  q3bound.append({'scope':scope,'activity':a,'P':p,'U':u,'B':b,'N':b-u,'ad_main':ratio(p,b-u),'ad_low':ratio(p,b),'ad_high':ratio(p+u,b),'equal_main':statistics.mean(x['P']/x['N'] for x in points if x['N']),'equal_low':statistics.mean(x['low'] for x in points),'equal_high':statistics.mean(x['high'] for x in points),'unknown_by_company_json':js([x for x in points if x['U']])})
dump('Q3_source_unknown_scenarios.csv',q3bound)
q2=read(C/'tables/T3_company_context.csv');core={'TC_ML_SYSTEMS','TC_FOUNDATION_MODEL','TC_DATA_PIPELINE','TC_RELIABILITY','TC_REALTIME','SK_PYTORCH','SK_PYTHON','SK_LINUX','SK_CPP'}
selection=[r for r in q2 if r['main_display']=='YES' and r['label_code'] in core and r['branch_bucket']=='UNCONDITIONAL' and ((r['dimension']=='skills' and r['metric_bucket']=='GENERAL') or (r['dimension']=='technical_concepts' and r['metric_bucket']=='DUTY_OWN_DEVELOP'))]
q2sens=[]
groups={'ALL24':ALL,'WHOLE23':WHOLE,'ACTIVITY_COMPLETE_COMPANIES':FULL,'SYSTEM_PRODUCTS':[c for c in WHOLE if CO[c]['stratum']=='SYSTEM_PRODUCTS'],'CROSS_BODY_MODELS':[c for c in WHOLE if CO[c]['stratum']=='CROSS_BODY_MODELS']}
for group,cs in groups.items():
 for removed in ['NONE']+cs:
  use=[c for c in cs if c!=removed]
  for key,rs in itertools.groupby(sorted(selection,key=lambda r:(r['role_code'],r['label_code'])),lambda r:(r['role_code'],r['label_code'])):
   rr=[r for r in rs if r['company_id'] in use];pts=[(r['company_id'],int(r['n_positive']),int(r['n_interpretable'])) for r in rr if int(r['n_base'])];d=distribution(pts);b=sum(int(r['n_base']) for r in rr);u=sum(int(r['n_relation_unknown']) for r in rr);permit=d['n_interpretable_companies']>=3 and d['N']>=20
   lo=[int(r['n_positive'])/int(r['n_base']) for r in rr if int(r['n_base'])];hi=[(int(r['n_positive'])+int(r['n_relation_unknown']))/int(r['n_base']) for r in rr if int(r['n_base'])]
   if not permit:
    for f in ['company_equal','ad_weighted','median','q25','q75']:d[f]=None
   q2sens.append({'scope':group,'removed_company':removed,'role':key[0],'label':key[1],'B':b,'U':u,'group_permitted':permit,'unknown_low_ad':ratio(d['P'],b) if permit else None,'unknown_high_ad':ratio(d['P']+u,b) if permit else None,'unknown_low_equal':statistics.mean(lo) if permit else None,'unknown_high_equal':statistics.mean(hi) if permit else None,**d})
dump('Q2_core_scope_leave_one_unknown.csv',q2sens)
# Exact duty template equivalence is exploratory: normalize whitespace only and choose stable ID within company AND role.
cases=json.loads((ROOT/'evidence/case_selection.json').read_text(encoding='utf-8'))['cases'];casecs=[c for case in cases for c in case['companies']]
clusters=collections.defaultdict(list)
for k in ids(casecs):
 text=RAW[k].get('duties') or RAW[k].get('full_description') or ''
 normalized=re.sub(r'\s+',' ',text).strip()
 clusters[(J[k]['company_id'],role(J[k]),normalized if normalized else '__EMPTY_UNIQUE_'+k)].append(k)
keepers={sorted(v)[0] for v in clusters.values()};dups=[]
for (c,r,t),kk in clusters.items():
 if len(kk)>1:dups.append({'company_id':c,'role':r,'n':len(kk),'ids_json':js(sorted(kk)),'retained_id':sorted(kk)[0],'normalized_duty_sha256':hashlib.sha256(t.encode()).hexdigest()})
dump('case_exact_duty_duplicates.csv',dups)
cpoints=[]
for c in casecs:
 for a in ACTS:
  for scope in ['MAIN','EXACT_DUTY_ONE_PER_COMPANY_ROLE','CLEAR_PRIMARY_ONLY']:
   base=ids([c]);valid=base&admitted
   if scope=='EXACT_DUTY_ONE_PER_COMPANY_ROLE':base &=keepers;valid &=keepers
   if scope=='CLEAR_PRIMARY_ONLY':base={k for k in base if J[k]['primary_status']=='CODED'};valid &=base
   p=len(valid&OWN[a]);u=len(base-valid)
   cpoints.append({'company_id':c,'scope':scope,'activity':a,'P':p,'N':len(valid),'B':len(base),'U':u,'rate':ratio(p,len(valid)),'unknown_low':ratio(p,len(base)),'unknown_high':ratio(p+u,len(base))})
dump('case_activity_sensitivity.csv',cpoints)
print('H1 MAIN',[(r['activity'],r['P'],r['N'],r['company_equal'],r['ad_weighted'],r['n_interpretable_companies']) for r in res if r['scope']=='WHOLE23' and r['denominator']=='ALL_ACTIVITY_POSITIVE'])
print('H1 LOO',[(a,min(r['ad_weighted'] for r in res if r['scope'].startswith('LOO') and r['activity']==a and r['denominator']=='ALL_ACTIVITY_POSITIVE'),max(r['ad_weighted'] for r in res if r['scope'].startswith('LOO') and r['activity']==a and r['denominator']=='ALL_ACTIVITY_POSITIVE')) for a in SPECIAL]);print('DUPLICATES',len(dups),sum(int(r['n'])-1 for r in dups));print('Q2 CORE LABELS',sorted({r['label_code'] for r in selection}))
