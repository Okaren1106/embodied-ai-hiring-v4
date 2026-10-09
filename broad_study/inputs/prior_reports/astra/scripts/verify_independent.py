"""Independent SQL reconstruction from the accepted JSON snapshot; does not import analysis code."""
from pathlib import Path
import json,csv,sqlite3,collections,math,hashlib
R=Path(__file__).resolve().parents[1]
def csvrows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
checks=[]
def ck(name,ok,detail=''):
 checks.append({'check':name,'pass':bool(ok),'detail':detail})
 if not ok:raise AssertionError(name+' '+str(detail))
raw=[json.loads(s) for s in (R/'inputs/accepted_jobs.jsonl').read_text(encoding='utf-8').splitlines()];source={r['identity_key']:r for r in raw}
ck('accepted_snapshot_hash',hashlib.sha256((R/'inputs/accepted_jobs.jsonl').read_bytes()).hexdigest()=='492080a56d62bd5e7aace9e0a7543d767774f4c0bf63681b4f2b299e03d263bd')
db=sqlite3.connect(':memory:');db.execute('create table ads(k text primary key,c text,r text,eligible int,primary_coded int)');db.execute('create table acts(k text,a text,rel text,primary key(k,a,rel))')
for s in raw:
 ref=s['record']['reference'];r=s['primary_codes'] if s['primary_status']=='CODED' else 'STATUS_'+s['primary_status']
 db.execute('insert into ads values(?,?,?,?,?)',(s['identity_key'],s['company_id'],r,int(ref['activities']['status'] in ['CODED','NOT_MENTIONED']),int(s['primary_status']=='CODED')))
 for a in ref['activities'].get('items',[]):db.execute('insert or ignore into acts values(?,?,?)',(s['identity_key'],a['value'],a['relation']))
db.commit();ck('unique_ads_1654',db.execute('select count(*) from ads').fetchone()[0]==1654)
ck('activity_admission_1623',db.execute('select sum(eligible) from ads').fetchone()[0]==1623)
co=sorted({s['company_id'] for s in raw});whole=[c for c in co if c!='US_AMAZON_FTR'];full=[c for c in whole if db.execute('select min(eligible) from ads where c=?',(c,)).fetchone()[0]==1]
ck('whole_23_and_source_subset_17',len(whole)==23 and len(full)==17)
scopes={'ALL24':co,'WHOLE23':whole,'ACTIVITY_COMPLETE_COMPANIES':full}
def in_sql(cs):return ','.join('?' for _ in cs)
counts=dict(db.execute("select a,count(*) from acts where rel='OWNED' group by a"))
ck('owned_activity_anchors',all(counts[a]==n for a,n in [('ACT_RESEARCH',75),('ACT_ENGINEERING',957),('ACT_DEPLOYMENT',351),('ACT_QUALITY',466)]),counts)
for r in csvrows(R/'tables/role_activity_bidirectional.csv'):
 cs=scopes[r['scope']];sql=in_sql(cs)
 n=db.execute(f'select count(*) from ads where eligible=1 and r=? and c in ({sql})',[r['role']]+cs).fetchone()[0]
 p=db.execute(f"select count(*) from ads join acts using(k) where eligible=1 and r=? and a=? and rel='OWNED' and c in ({sql})",[r['role'],r['activity']]+cs).fetchone()[0]
 allp=db.execute(f"select count(*) from ads join acts using(k) where eligible=1 and a=? and rel='OWNED' and c in ({sql})",[r['activity']]+cs).fetchone()[0]
 assert (p,n,allp)==tuple(int(r[k]) for k in ['P','role_activity_interpretable_N','activity_positive_N'])
ck('528_bidirectional_cells_sql',True)
for r in csvrows(R/'tables/company_role_activity.csv'):
 n=db.execute('select count(*) from ads where c=? and r=? and eligible=1',(r['company_id'],r['role'])).fetchone()[0]
 p=db.execute("select count(*) from ads join acts using(k) where c=? and r=? and eligible=1 and a=? and rel='OWNED'",(r['company_id'],r['role'],r['activity'])).fetchone()[0]
 assert (p,n)==(int(r['P']),int(r['role_N']))
ck('4224_company_role_activity_cells_sql',True)
for row in csvrows(R/'tables/Q1_company_coverage.csv'):
 cs=scopes[row['scope']];p=db.execute(f'select count(*) from ads where c in ({in_sql(cs)}) and r=?',cs+[row['role']]).fetchone()[0]
 n=db.execute(f'select count(*) from ads where c in ({in_sql(cs)})',cs).fetchone()[0];assert (p,n)==(int(row['P']),int(row['N']))
ck('66_Q1_coverage_counts_sql',True)
# Joint counts recomputed directly from original reference arrays, with exact or whitespace-only text match.
joint=csvrows(R/'tables/activity_joint_ad_status.csv')
for r in joint:
 s=source[r['identity_key']];aa={x['value'] for x in s['record']['reference']['activities']['items'] if x['relation']=='OWNED'};double=r['activity1'] in aa and r['activity2'] in aa
 assert double==(r['raw_double_positive']=='True')
 if r['joint_state']=='UNCONDITIONAL':
  assert double
  for col in ['evidence1_json','evidence2_json']:
   es=json.loads(r[col]);assert any(e['status']!='NOT_LOCATED' and s[e['field']][int(e['start']):int(e['end'])]==e.get('frozen_exact_quote',e['quote']) for e in es)
for name,a,b,n in [('RESEARCH_ENGINEERING','ACT_RESEARCH','ACT_ENGINEERING',71),('ENGINEERING_QUALITY','ACT_ENGINEERING','ACT_QUALITY',308),('ENGINEERING_DEPLOYMENT','ACT_ENGINEERING','ACT_DEPLOYMENT',243)]:
 got=db.execute("select count(*) from ads join acts a1 using(k) join acts a2 using(k) where eligible=1 and a1.rel='OWNED' and a2.rel='OWNED' and a1.a=? and a2.a=?",(a,b)).fetchone()[0];ck(name+'_joint_sql',got==n)
ck('4869_joint_states_and_positive_quote_offsets',len(joint)==1623*3)
# Independent per-ad denominator accounting for inherited Q2 semantics, preserving all label-specific unknowns.
base=collections.Counter()
for s in raw:
 if s['primary_status']=='CODED' and s['primary_codes'] in ['RF_ML_AI_ENGINEERING','RF_ROBOTICS_SOFTWARE']:
  for dim,key in [('skills','skills_status'),('technical_concepts','technical_status')]:
   if s[key]!='SOURCE_UNASSESSABLE':base[(s['company_id'],s['primary_codes'],dim)]+=1
line=csvrows(R/'inputs/stage_c/tables/T3_positive_unknown_lineage.csv');sets=collections.defaultdict(set)
for r in line:sets[tuple(r[k] for k in ['company_id','role_code','dimension','label_code','metric_bucket','branch_bucket','state'])].add(r['identity_key'])
for r in csvrows(R/'inputs/stage_c/tables/T3_company_context.csv'):
 key=tuple(r[k] for k in ['company_id','role_code','dimension','label_code','metric_bucket','branch_bucket']);p=len(sets[key+('PRESENT',)]);u=len(sets[key+('UNKNOWN',)]);b=base[key[:3]]
 assert (p,u,b,b-u)==tuple(int(r[k]) for k in ['n_positive','n_relation_unknown','n_base','n_interpretable'])
ck('38640_inherited_Q2_company_cells_ad_identity_recount',True,'原始快照核对基础分母；P/U独立去重继承语义追溯，不声称重判语义')
roles=[r[0] for r in db.execute('select distinct r from ads') if r[0].startswith('RF_') and r[0] not in ['RF_ALTERNATIVE_DIRECTIONS','RF_COMPOSITE_FUNCTION']]
ck('17_concrete_roles',len(roles)==17)
eligible_pairs=0
for r in csvrows(R/'tables/case_candidate_coverage.csv'):
 ns={c:{x:db.execute('select count(*) from ads where c=? and r=? and eligible=1',(c,x)).fetchone()[0] for x in roles} for c in [r['company1'],r['company2']]};K=sorted(x for x in roles if min(ns[r['company1']][x],ns[r['company2']][x])>=10)
 assert K==json.loads(r['K_json']);eligible_pairs+=len(K)>=2
ck('253_pair_qualification_17_eligible',eligible_pairs==17)
for row in csvrows(R/'tables/common_role_standardization_all_eligible.csv'):
 cs=[row['company1'],row['company2']];K=json.loads(row['K_json']);n={c:{r:db.execute('select count(*) from ads where c=? and r=? and eligible=1',(c,r)).fetchone()[0] for r in K} for c in cs};rates={}
 for c in cs:
  terms=[]
  for r in K:
   p=db.execute("select count(*) from ads join acts using(k) where c=? and r=? and eligible=1 and a=? and rel='OWNED'",(c,r,row['activity'])).fetchone()[0]
   w=n[c][r]/sum(n[c].values()) if row['weight']=='OWN_K' else 1/len(K) if row['weight']=='EQUAL_K' else sum(n[x][r] for x in cs)/sum(sum(n[x].values()) for x in cs)
   terms.append(w*p/n[c][r])
  rates[c]=sum(terms)
 assert math.isclose(rates[cs[0]],float(row['rate1']),abs_tol=1e-12) and math.isclose(rates[cs[1]],float(row['rate2']),abs_tol=1e-12)
ck('408_standardized_rates_sql',True)
for r in csvrows(R/'tables/T5_case_work_object_evidence.csv'):
 s=source[r['identity_key']];assert s[r['field']][int(r['start']):int(r['end'])]==r['quote']
ck('18_case_object_quote_locations',True)
respons=csvrows(R/'tables/T5_responsibility_long.csv');ck('responsibility_dates_before_observation',all(r['publication_date']<='2026-09-11' for r in respons))
ck('T5_24_companies_and_21_product_scope_assertions',len(csvrows(R/'tables/T5_company_background_job_link.csv'))==24 and len(respons)==21)
for r in csvrows(R/'tables/Q2_core_scope_leave_one_unknown.csv'):
 permit=int(r['n_interpretable_companies'])>=3 and int(r['N'])>=20;assert permit==(r['group_permitted']=='True')
 if not permit:assert r['company_equal']==r['ad_weighted']==''
ck('group_threshold_reapplied_after_each_company_deletion',True)
for filename in ['activity_joint_summary.csv','ML_technical_joint_summary.csv']:
 for r in csvrows(R/'tables'/filename):assert int(r['B'])==sum(int(r[s]) for s in ['UNCONDITIONAL','CONDITIONAL_ONLY','CHOICE_ONLY','UNRESOLVED','NO_RECORDED_JOINT']) and int(r['B'])==int(r['P'])+int(r['Z'])+int(r['U'])
ck('joint_five_states_partition_and_P_Z_U_identity',True)
out={'method':'独立SQL与原始JSON实现；同一Astra研究者的计算核对，不冒称独立同行审稿','checks':checks,'passed':len(checks),'failed':0}
(R/'verification/independent_checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'passed':len(checks),'failed':0},ensure_ascii=False))
