from common import *
from itertools import combinations
import sqlite3
lock_check()
PAIR={'RESEARCH_ENGINEERING':('ACT_RESEARCH','ACT_ENGINEERING'),'ENGINEERING_QUALITY':('ACT_ENGINEERING','ACT_QUALITY'),'ENGINEERING_DEPLOYMENT':('ACT_ENGINEERING','ACT_DEPLOYMENT')}
S1=[c for c in WHOLE if int(CO[c]['activities_SOURCE_UNASSESSABLE'])==0]
S2=[c for c in WHOLE if CO[c]['source_type']=='official' and CO[c]['hiring_data_quality_score'] in ['GOOD','EXCELLENT'] and int(CO[c]['activities_SOURCE_UNASSESSABLE'])==0 and int(CO[c]['primary_SOURCE_UNASSESSABLE'])==0]
SC={'ALL24':ids(ALL),'WHOLE23':ids(WHOLE),'S1_ACTIVITY_COMPLETE':ids(S1),'S2_SOURCE_QUALITY':ids(S2),'S3_SOURCE_QUALITY_LENGTH200':{k for k in ids(S2) if int(J[k]['full_description_chars'])>=200}}
assert [len(SC[s]) for s in SC]==[1654,1630,968,576,557]
dump('tables/R_source_membership.csv',[{'scope':s,'identity_key':k,'company_id':J[k]['company_id'],'reading_id':J[k]['reading_id'],'role':role(J[k]),'activity_eligible':k in admitted,'full_description_chars':J[k]['full_description_chars']} for s,kk in SC.items() for k in sorted(kk)])
dump('tables/R_source_scope_summary.csv',[{'scope':s,'companies':len({J[k]['company_id'] for k in kk}),'ads':len(kk),'activity_N':len(kk&admitted),'company_ids':js(sorted({J[k]['company_id'] for k in kk}))} for s,kk in SC.items()])
dump('tables/R_S3_removed_ads.csv',[{'identity_key':k,**{f:J[k][f] for f in ['reading_id','company_id','title','full_description_chars','primary_code']}} for k in sorted(SC['S2_SOURCE_QUALITY']-SC['S3_SOURCE_QUALITY_LENGTH200'])])
manual=json.loads((ROOT/'configs/R2_manual_adjudication.json').read_text(encoding='utf-8'))['decisions']
oldjoint=read(ROOT/'inputs/prior_reports/astra/tables/activity_joint_ad_status.csv');OJ={(r['identity_key'],r['pair']):r for r in oldjoint}
dsv=read(ROOT/'inputs/prior_reports/dsv/tables/D4_activity_pair_lineage.csv');DJ={(r['identity_key'],r['pair_id'][3:]):r for r in dsv}
disputes=[];trace=[];recover=[];joint={};JUNK={}
for pid,(a,b) in PAIR.items():
    joint[pid]=set();JUNK[pid]=set()
    for k in sorted(admitted):
        raw=k in OWN[a]&OWN[b];old=OJ[k,pid];d=DJ.get((k,pid),{});state='NO_RECORDED_JOINT';why='原认可编码无双本人承担，不把参与或职位知识要求升级为承担';ev=[]
        if raw:
            for act in [a,b]:
                for e in AE[k,act,'OWNED']:
                    loc=locate(k,e);ev.append({'activity':act,**loc});recover.append({'identity_key':k,'pair':pid,'activity':act,**loc})
            unresolved=any(e['method']=='UNRESOLVED_LOCATION' for e in ev)
            if d.get('status')=='UNRESOLVED':
                dec=manual[J[k]['reading_id']];state=dec['state'];why=dec['reason']
                assert not unresolved
                disputes.append({'identity_key':k,'reading_id':J[k]['reading_id'],'company_id':J[k]['company_id'],'pair':pid,'old_astra':old['joint_state'],'old_dsv':d['status'],'old_grok':'UNCONDITIONAL','decision':state,'reason':why,'evidence_json':js(ev),'role_tree':ST.get(k,{}).get('tree_json',''),'reviewer':'Astra full-text adjudication; not independent double coding'})
            elif unresolved:state='UNRESOLVED';why='本轮严格定位仍不唯一，退出主分母'
            else:state=old['joint_state'];why='继承既有共同承担语义判读；本轮逐证据严格定位通过。未声称另一次全部全文人工复核。'
            assert state in ['UNCONDITIONAL','CONDITIONAL_ONLY','CHOICE_ONLY','UNRESOLVED']
        if state=='UNCONDITIONAL':joint[pid].add(k)
        if state=='UNRESOLVED':JUNK[pid].add(k)
        trace.append({'identity_key':k,'reading_id':J[k]['reading_id'],'company_id':J[k]['company_id'],'role':role(J[k]),'pair':pid,'raw_double_positive':raw,'joint_state':state,'reason':why,'evidence_json':js(ev)})
assert len(disputes)==20
dump('tables/R2_adjudication.csv',disputes);dump('tables/R_joint_ad_status.csv',trace);dump('tables/R_joint_evidence_locations.csv',recover)
dump('tables/R_mixed_tree_audit.csv',[{'identity_key':k,'reading_id':J[k]['reading_id'],'root':v['root_relation'],'owned_activities':js([a for a in ACTS if k in OWN[a]]),'impact_on_three_pairs':any(k in OWN[a]&OWN[b] for a,b in PAIR.values()),'finding':'树必须递归处理；N0396没有原编码本人承担活动，根节点捷径不影响本批三组数值'} for k,v in ST.items() if v['has_mixed_branch']=='YES'])
q1=[];q3=[];jc=[];bid=[];cross=[];cp=[]
DED={'ACT_RESEARCH':'RF_RESEARCH_SCIENCE','ACT_DEPLOYMENT':'RF_DEPLOYMENT_FIELD_SERVICE','ACT_QUALITY':'RF_MANUFACTURING_QUALITY_SUPPLY'}
for sn,kk in SC.items():
    cc=sorted({J[k]['company_id'] for k in kk});byc={c:{k for k in kk if J[k]['company_id']==c} for c in cc};valid=kk&admitted
    for f in sorted(RN):
        qq={k for k in kk if role(J[k])==f};points=[(c,len(qq&v),0,len(v)) for c,v in byc.items()];q1.append({'scope':sn,'role':f,'role_name':RN[f],**summary(points)})
    for a in ACTS:
        points=[(c,len(OWN[a]&v&admitted),0,len(v&admitted)) for c,v in byc.items()];q3.append({'scope':sn,'activity':a,'activity_name':AN[a],**summary(points)})
        for c,p,u,b in points:cp.append({'scope':sn,'metric':a,'company_id':c,'P':p,'U':u,'B':b,'N':b-u,'share':ratio(p,b-u)})
        for f in sorted(RN):
            ff={k for k in valid if role(J[k])==f};p=len(ff&OWN[a]);bid.append({'scope':sn,'role':f,'activity':a,'P':p,'within_role_N':len(ff),'within_role_rate':ratio(p,len(ff)),'activity_positive_N':len(valid&OWN[a]),'role_composition_of_activity':ratio(p,len(valid&OWN[a]))})
        if a in DED:
            ak=valid&OWN[a];same={k for k in ak if role(J[k])==DED[a]};other={k for k in ak if role(J[k]) in CONCRETE and k not in same};struct={k for k in ak if k in ST};unclear=ak-same-other-struct
            pp=[(c,len((ak-same)&v),0,len(ak&v)) for c,v in byc.items()];ss=summary(pp)
            loo=[ratio(len((ak-same)-v),len(ak-v)) for v in byc.values() if ak-v]
            cross.append({'scope':sn,'activity':a,'dedicated_role':DED[a],'same_role':len(same),'other_concrete':len(other),'structural':len(struct),'unclear_primary':len(unclear),**ss,'outside_lower_unclear_as_dedicated':ratio(len(other|struct),len(ak)),'outside_upper_unclear_outside':ratio(len(other|struct|unclear),len(ak)),'loo_min':min(loo) if loo else None,'loo_max':max(loo) if loo else None})
    for pid in PAIR:
        points=[(c,len(joint[pid]&v),len(JUNK[pid]&v),len(v&admitted)) for c,v in byc.items()];jc.append({'scope':sn,'pair':pid,**summary(points)})
        for c,p,u,b in points:cp.append({'scope':sn,'metric':pid,'company_id':c,'P':p,'U':u,'B':b,'N':b-u,'share':ratio(p,b-u)})
dump('tables/R_Q1_coverage_concentration.csv',q1);dump('tables/R_Q3_activity_summary.csv',q3);dump('tables/R_joint_summary.csv',jc);dump('tables/R_company_activity_joint_points.csv',cp);dump('tables/R_role_activity_bidirectional.csv',bid);dump('tables/R_cross_function.csv',cross)
# Reconstruct the old programming error: a company passed as drop, then averaged.
old9=read(ROOT/'inputs/prior_reports/dsv/tables/D9_sensitivity_ledger.csv');wrong=[]
for old in old9:
    if old['q']!='Q3':continue
    label=old['label'];metric=label if label in ACTS else old['metric_id'].removeprefix('Q3_').removeprefix('P1_').removeprefix('P2_').removeprefix('P3_')
    if metric not in ACTS and metric not in PAIR:
        if 'RESEARCH' in old['metric_id']:metric='RESEARCH_ENGINEERING'
        elif 'QUALITY' in old['metric_id']:metric='ENGINEERING_QUALITY'
        elif 'DEPLOYMENT' in old['metric_id']:metric='ENGINEERING_DEPLOYMENT'
    assert metric in ACTS or metric in PAIR,(old,metric)
    positive=OWN[metric] if metric in ACTS else {r['identity_key'] for r in dsv if r['pair_id'][3:]==metric and r['status']=='UNCONDITIONAL'}
    wrongvalue=statistics.mean(len(positive&ids([c for c in ALL if c!=drop],True))/len(ids([c for c in ALL if c!=drop],True)) for drop in WHOLE)
    for scope in ['ALL24','WHOLE23']:
        correct=next(r for r in (q3 if metric in ACTS else jc) if r['scope']==scope and r.get('activity',r.get('pair'))==metric)
        wrong.append({'metric':metric,'scope':scope,'old_reported_equal':old['value_company_equal'],'reconstructed_average_leave_one_out':wrongvalue,'bug_reproduced':abs(float(old['value_company_equal'])-wrongvalue)<1e-8,'correct_company_equal':correct['company_equal'],'correct_ad_weighted':correct['ad_weighted'],'P':correct['P'],'U':correct['U'],'B':correct['B'],'N':correct['N'],'valid_companies':correct['n_valid_companies'],'old_n_companies_was_positive_count':old['n_companies'],'reason':'DSV activity_metric/pair_metric 的公司参数被作为 drop；修复为逐公司 P/N 算术平均。共同承担还合并本轮20格裁决。'})
dump('tables/R_DSV_company_mean_correction.csv',wrong)
oldq1=read(ROOT/'inputs/prior_reports/dsv/tables/D1_q1_coverage_concentration.csv')
dump('tables/R_max_contributor_correction.csv',[{'role':r['class_code'],'old_dsv_company':r['largest_company_id'],'correct_positive_companies':z['max_positive_companies'],'positive_count':z['max_positive_count'],'total_positive':z['P'],'correct_positive_share':z['max_positive_contribution'],'denominator_companies':z['max_den_companies'],'denominator_share':z['max_den_contribution']} for r in oldq1 for z in q1 if z['scope']=='WHOLE23' and z['role']==r['class_code']])
# Reuse the original label/branch estimand, not keywords, for source-scope Q2.
bases=read(C/'tables/T3_base_admission.csv');line=read(C/'tables/T3_positive_unknown_lineage.csv');companyq2=read(C/'tables/T3_company_context.csv')
keys=sorted({(r['role_code'],r['dimension'],r['label_code'],r['metric_bucket'],r['branch_bucket']) for r in companyq2 if r['main_display']=='YES'})
baseidx=defaultdict(set);posidx=defaultdict(set);unkidx=defaultdict(set)
for r in bases:
    if r['base_eligible']=='YES':baseidx[r['role_code'],r['dimension']].add(r['identity_key'])
for r in line:
    key=tuple(r[f] for f in ['role_code','dimension','label_code','metric_bucket','branch_bucket'])
    (posidx if r['state']=='PRESENT' else unkidx)[key].add(r['identity_key'])
q2=[]
for sn,kk in SC.items():
    cc=sorted({J[k]['company_id'] for k in kk})
    for key in keys:
        f,dim,lab,metric,branch=key;bb=baseidx[f,dim]&kk;uu=unkidx[key]&bb;pp=posidx[key]&bb-uu
        points=[(c,sum(J[k]['company_id']==c for k in pp),sum(J[k]['company_id']==c for k in uu),sum(J[k]['company_id']==c for k in bb)) for c in cc]
        q2.append({'scope':sn,'role':f,'dimension':dim,'label':lab,'metric':metric,'branch':branch,**summary(points)})
dump('tables/R_Q2_v1_scope_bridge.csv',q2)
# Independent arithmetic path using SQLite from the locked ad and activity rows.
db=sqlite3.connect(':memory:');db.execute('create table jobs(k text,c text,r text,valid int)');db.executemany('insert into jobs values(?,?,?,?)',[(k,j['company_id'],role(j),int(k in admitted)) for k,j in J.items()]);db.execute('create table act(k text,a text,relation text)');db.executemany('insert into act values(?,?,?)',[(r['identity_key'],r['label_code'],r['relation']) for r in activities]);checks=[]
for sn,kk in SC.items():
    db.execute('drop table if exists scope');db.execute('create table scope(k text primary key)');db.executemany('insert into scope values(?)',[(k,) for k in kk])
    for a in ACTS:
        sql=db.execute("select j.c,count(distinct j.k),count(distinct case when a.k is not null then j.k end) from jobs j join scope s on s.k=j.k left join act a on a.k=j.k and a.a=? and a.relation='OWNED' where j.valid=1 group by j.c",(a,)).fetchall();p=sum(x[2] for x in sql);n=sum(x[1] for x in sql);eq=sum(x[2]/x[1] for x in sql)/len(sql);ref=next(r for r in q3 if r['scope']==sn and r['activity']==a);checks.append({'test':sn+' '+a,'pass':p==ref['P'] and n==ref['N'] and abs(eq-ref['company_equal'])<1e-12,'P_sql':p,'N_sql':n,'equal_sql':eq})
    for pid,(a,b) in PAIR.items():
        p=db.execute("select count(distinct j.k) from jobs j join scope s on j.k=s.k join act a on a.k=j.k and a.a=? and a.relation='OWNED' join act b on b.k=j.k and b.a=? and b.relation='OWNED' where j.valid=1",(a,b)).fetchone()[0];ref=next(r for r in jc if r['scope']==sn and r['pair']==pid);checks.append({'test':sn+' raw '+pid,'pass':p==ref['P']+ref['U'],'raw_SQL':p,'P_adjudicated':ref['P'],'U':ref['U']})
assert all(x['pass'] for x in checks)
save_json('verification/R_numeric_checks.json',{'review_type':'Same researcher, independent SQL arithmetic implementation, not external peer review','checks':checks,'locked_inputs':lock_check(),'pair_states':dict(Counter(r['joint_state'] for r in trace)),'recovered_methods':dict(Counter(r['method'] for r in recover))})
print('Completed R numeric tables; source sizes',[len(v) for v in SC.values()]);print('joint',[(r['scope'],r['pair'],r['P'],r['U'],r['N']) for r in jc[:6]]);print('checks',len(checks),'DSV bug reproduced',all(r['bug_reproduced'] for r in wrong));print('unresolved',[(r['reading_id'],r['pair']) for r in trace if r['joint_state']=='UNRESOLVED'])
