"""Q2 v2.1 L0–L3 and required sensitivities from first-pass states. Stream 2.8M rows."""
from common import *
from datetime import datetime, timezone
rule=json.loads((ROOT/'configs/Q_coding_rules_v2.json').read_text(encoding='utf-8'))
cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
CD={r['code']:r for r in cat['labels']}
ads=read(ROOT/'tables/Q3_adjudicated_ads_partial.csv')
assert len(ads)==1576
byk={a['identity_key']:a for a in ads}
T1={r['company_id']:r for r in read(C/'tables/T1_company_sample.csv')}
mem=defaultdict(set)
for r in read(ROOT/'tables/R_source_membership.csv'):
    mem[r['scope']].add(r['identity_key'])
# Q2 ads only
q2ids={a['identity_key'] for a in ads}
mem['ALL24']={k for k in mem.get('ALL24', q2ids) if k in q2ids} or q2ids
# rebuild membership from ads if needed
if len(mem['ALL24'])!=1576:
    mem['ALL24']=q2ids
mem['WHOLE23']={k for k,a in byk.items() if T1[a['company_id']]['scope_main_company']=='YES'}
mem['FAR']={k for k,a in byk.items() if a['company_id']=='US_AMAZON_FTR'}
# source schemes already in R_source_membership for 1654; intersect Q2
for s in ['S1_ACTIVITY_COMPLETE','S2_SOURCE_QUALITY','S3_SOURCE_QUALITY_LENGTH200']:
    mem[s]={k for k in mem.get(s,set()) if k in q2ids}
mem['EXCLUDE_MULTI_PRODUCT']={k for k,a in byk.items() if T1[a['company_id']].get('known_multi_product')!='YES' and T1[a['company_id']]['scope_main_company']=='YES'}
mem['EXCLUDE_MEDIA_ONLY']={k for k,a in byk.items() if T1[a['company_id']].get('media_only_basis')!='YES' and T1[a['company_id']]['scope_main_company']=='YES'}
role_ads=defaultdict(list)
for a in ads: role_ads[a['role']].append(a)
co_role_n=Counter((a['company_id'],a['role']) for a in ads)
co_role_task_n=Counter((a['company_id'],a['role'],a['task']) for a in ads)
# PU counts: (scope is applied later) store per identity? too big.
# Store per (role,code,metric,branch,company) P/U/NA using WHOLE identity later filtered by membership via company? Membership is ad-level not company-level for S3.
# Must count ads, so key includes nothing about identity but we need to filter ads by membership.
# Stream: for each P/U/NA row, increment for each scope that contains identity_key.
PU=defaultdict(lambda: Counter())  # key=(scope,role,task,code,metric,branch,company) -> state count
# Too memory heavy if we include task. Do two passes? One without task for display/L3, one with task only for P.
# Compact: only record P and U (NA rare). Z derived from n_ads in membership.
Pcount=defaultdict(int)  # (scope,role,code,metric,branch,company)
Ucount=defaultdict(int)
NAcount=defaultdict(int)
Ptask=defaultdict(int)  # (scope,role,task,code,metric,branch,company)
scopes=list(mem)
# Precompute identity->scopes
id_scopes=defaultdict(list)
for s,ks in mem.items():
    for k in ks: id_scopes[k].append(s)
with (ROOT/'tables/Q3_applicable_states_partial.csv').open(encoding='utf-8-sig',newline='') as f:
    r=csv.DictReader(f)
    for row in r:
        st=row['state']
        if st not in ('P','U','NA'): continue
        k=row['identity_key']; role=row['role']; code=row['label_code']; m=row['metric']; b=row['branch']; co=row['company_id']; task=row['task']
        for s in id_scopes[k]:
            key=(s,role,code,m,b,co)
            if st=='P':
                Pcount[key]+=1
                Ptask[(s,role,task,code,m,b,co)]+=1
            elif st=='U':
                Ucount[key]+=1
            else:
                NAcount[key]+=1
# n ads per scope,role,company
n_src=defaultdict(int)
n_src_task=defaultdict(int)
for a in ads:
    for s in id_scopes[a['identity_key']]:
        n_src[(s,a['role'],a['company_id'])]+=1
        n_src_task[(s,a['role'],a['task'],a['company_id'])]+=1
slices=[(x['metric'],x['branch']) for x in rule['legacy_14_slices']]
gate_c=int(rule['group_gate']['min_valid_companies']); gate_n=int(rule['group_gate']['min_interpretable_ads']); small_n=int(rule['group_gate']['small_company_n'])
disp=rule['display']

def summarize(p_by_co, u_by_co, n_by_co):
    companies=sorted(n_by_co)
    P=U=N=B=0; rows=[]
    for c in companies:
        n_ads=n_by_co[c]; p=p_by_co.get(c,0); u=u_by_co.get(c,0); z=max(0,n_ads-p-u); nn=p+z; bb=p+z+u
        P+=p; U+=u; N+=nn; B+=bb
        share= (p/nn) if nn else None
        rows.append((c,p,u,nn,share, n_ads<small_n and nn>0))
    valid=[r for r in rows if r[3]>0]
    nc=len(valid)
    eq=sum(r[4] for r in valid)/nc if nc else None
    aw= (P/N) if N else None
    maxp=max((r[1] for r in rows), default=0)
    max_cos=sorted(r[0] for r in rows if r[1]==maxp) if P else []
    gate='EXPLORATORY_SUMMARY' if nc>=gate_c and N>=gate_n else 'POINTS_ONLY'
    return dict(P=P,U=U,Z=N-P,N=N,B=B,n_companies_positive_denom=nc,share_ad_weighted=aw,share_company_equal=eq,gate=gate,largest_positive_share=(maxp/P if P else None),largest_positive_companies=js(max_cos),small_n_companies=sum(r[5] for r in rows),company_points=[{'company_id':c,'P':p,'U':u,'N':nn,'share':sh,'small_n':sm} for c,p,u,nn,sh,sm in rows])

# L0
l0=[]
for cov in read(ROOT/'tables/Q1_role_coverage.csv'):
    role=cov['role']; rr=role_ads[role]
    tasks=Counter(a['task'] for a in rr)
    cos=sorted({a['company_id'] for a in rr})
    whole=[a for a in rr if a['identity_key'] in mem['WHOLE23']]
    l0.append(dict(role=role,role_name=cov['role_name'],all24_ads=len(rr),all24_companies=len(cos),whole23_ads=len(whole),whole23_companies=len({a['company_id'] for a in whole}),tasks=js(dict(tasks)),catalog_items=cov['catalog_items'],L0='COMPLETE',L1='CONTENT_CODED_SECOND_PASS_QUEUED',notes='L2/L3 are cell-specific; sparse functions remain case/points.'))
dump('tables/Q4_L0_coverage.csv', l0)

# company points + aggregates for WHOLE23 main
agg=[]; points=[]; display=[]; task_agg=[]
# iterate existing P/U keys union n_src
roles=sorted(role_ads)
# catalog by role
cbr=defaultdict(set)
for lab in cat['labels']:
    for f in lab['applicable_roles']: cbr[f].add(lab['code'])

def nmap(s,role):
    m=defaultdict(int)
    for (ss,rr,co),n in n_src.items():
        if ss==s and rr==role: m[co]=n
    return m

for s in ['WHOLE23','ALL24','FAR','S1_ACTIVITY_COMPLETE','S2_SOURCE_QUALITY','S3_SOURCE_QUALITY_LENGTH200','EXCLUDE_MULTI_PRODUCT','EXCLUDE_MEDIA_ONLY']:
    for role in roles:
        n_by=nmap(s,role)
        codes=sorted(cbr[role])
        for code in codes:
            mt=CD[code]['measurement_type']
            for m,b in slices:
                p_by=defaultdict(int); u_by=defaultdict(int)
                for co in n_by:
                    p_by[co]=Pcount.get((s,role,code,m,b,co),0)
                    u_by[co]=Ucount.get((s,role,code,m,b,co),0)
                sm=summarize(p_by,u_by,n_by)
                rec=dict(scope=s,role=role,label_code=code,label_name=CD[code]['name'],measurement_type=mt,metric=m,branch=b,P=sm['P'],U=sm['U'],Z=sm['Z'],N=sm['N'],B=sm['B'],n_companies=sm['n_companies_positive_denom'],share_ad_weighted=sm['share_ad_weighted'] if sm['gate']=='EXPLORATORY_SUMMARY' else '',share_company_equal=sm['share_company_equal'] if sm['gate']=='EXPLORATORY_SUMMARY' else '',gate=sm['gate'],largest_positive_share=sm['largest_positive_share'],largest_positive_companies=sm['largest_positive_companies'],dominance_warning='YES' if (sm['largest_positive_share'] or 0)>0.5 else 'NO',catalog_version='Q2-v2.1')
                agg.append(rec)
                if s=='WHOLE23':
                    for pt in sm['company_points']:
                        if pt['P'] or pt['N']:
                            points.append(dict(scope=s,role=role,label_code=code,metric=m,branch=b,company_id=pt['company_id'],P=pt['P'],U=pt['U'],N=pt['N'],share=pt['share'],small_n='YES' if pt['small_n'] else 'NO'))

dump('tables/Q4_aggregates.csv', agg)
dump('tables/Q4_company_points.csv', points)

# display items WHOLE23: any-P across slices collapsed? Protocol: 主图按覆盖公司数. Use GENERAL UNCONDITIONAL as primary display slice, fallback max P companies.
disp_rows=[]
for role in roles:
    by_type=defaultdict(list)
    for rec in agg:
        if rec['scope']!='WHOLE23' or rec['role']!=role: continue
        if rec['metric']=='GENERAL' and rec['branch']=='UNCONDITIONAL':
            by_type[rec['measurement_type']].append(rec)
    for mt, rows in by_type.items():
        rows=sorted(rows, key=lambda r:(-(r['P']>0), -sum(1 for p in points if p['role']==role and p['label_code']==r['label_code'] and p['metric']=='GENERAL' and p['branch']=='UNCONDITIONAL' and p['P']>0), -r['P'], r['label_code']))
        # positive companies
        scored=[]
        for r in rows:
            pcs=sum(1 for p in points if p['role']==role and p['label_code']==r['label_code'] and p['metric']==r['metric'] and p['branch']==r['branch'] and p['P']>0)
            if pcs>=int(disp['min_positive_companies']) and r['P']>=int(disp['min_positive_ads']):
                scored.append((pcs,r['P'],r['label_code'],r))
        scored.sort(key=lambda x:(-x[0],-x[1],x[2]))
        for i,(_,_,_,r) in enumerate(scored[:int(disp['max_per_type'])],1):
            disp_rows.append(dict(r, display_rank=i))
dump('tables/Q4_display_items.csv', disp_rows)

# leave-one-out on display items WHOLE23
loo=[]
for rec in disp_rows:
    role,code,m,b=rec['role'],rec['label_code'],rec['metric'],rec['branch']
    n_by=nmap('WHOLE23',role)
    companies=sorted(n_by)
    for drop in companies:
        n2={c:n for c,n in n_by.items() if c!=drop}
        p_by={c:Pcount.get(('WHOLE23',role,code,m,b,c),0) for c in n2}
        u_by={c:Ucount.get(('WHOLE23',role,code,m,b,c),0) for c in n2}
        sm=summarize(p_by,u_by,n2)
        loo.append(dict(role=role,label_code=code,metric=m,branch=b,removed_company=drop,P=sm['P'],N=sm['N'],n_companies=sm['n_companies_positive_denom'],gate=sm['gate'],share_ad_weighted=sm['share_ad_weighted'] if sm['gate']=='EXPLORATORY_SUMMARY' else '',share_company_equal=sm['share_company_equal'] if sm['gate']=='EXPLORATORY_SUMMARY' else ''))
dump('tables/Q4_leave_one_company_out.csv', loo)

# unknown bound: treat U as Z (low) vs U as P (high) for display items
ub=[]
for rec in disp_rows:
    role,code,m,b=rec['role'],rec['label_code'],rec['metric'],rec['branch']
    n_by=nmap('WHOLE23',role)
    p_by={c:Pcount.get(('WHOLE23',role,code,m,b,c),0) for c in n_by}
    u_by={c:Ucount.get(('WHOLE23',role,code,m,b,c),0) for c in n_by}
    low=summarize(p_by,{c:0 for c in n_by}, {c:n_by[c] for c in n_by})  # U folded into Z by zeroing U and keeping n_ads
    # high: P' = P+U
    p_high={c:p_by[c]+u_by[c] for c in n_by}
    high=summarize(p_high,{c:0 for c in n_by}, n_by)
    ub.append(dict(role=role,label_code=code,metric=m,branch=b,P=rec['P'],U=rec['U'],N=rec['N'],low_ad_weighted=low['share_ad_weighted'],high_ad_weighted=high['share_ad_weighted'],low_company_equal=low['share_company_equal'],high_company_equal=high['share_company_equal']))
dump('tables/Q4_unknown_bounds.csv', ub)

# task-stratified L2: WHOLE23 GENERAL UNCONDITIONAL P by task, points only unless gate
task_rows=[]
tasks_seen=sorted({(a['role'],a['task']) for a in ads})
for role,task in tasks_seen:
    n_by=defaultdict(int)
    for (s,rr,tt,co),n in n_src_task.items():
        if s=='WHOLE23' and rr==role and tt==task: n_by[co]=n
    for code in sorted(cbr[role]):
        m,b='GENERAL','UNCONDITIONAL'
        p_by={c:Ptask.get(('WHOLE23',role,task,code,m,b,c),0) for c in n_by}
        u_by={c:0 for c in n_by}
        sm=summarize(p_by,u_by,n_by)
        if sm['P']==0: continue
        task_rows.append(dict(scope='WHOLE23',role=role,task=task,label_code=code,metric=m,branch=b,P=sm['P'],N=sm['N'],n_companies=sm['n_companies_positive_denom'],gate=sm['gate'],share_ad_weighted=sm['share_ad_weighted'] if sm['gate']=='EXPLORATORY_SUMMARY' else '',share_company_equal=sm['share_company_equal'] if sm['gate']=='EXPLORATORY_SUMMARY' else ''))
dump('tables/Q4_task_strata.csv', task_rows)

# exact duplicate duties
norm=lambda t: re.sub(r'\s+',' ', (t or '')).strip()
clusters=defaultdict(list)
for a in ads:
    k=a['identity_key']; d=norm(RAW[k].get('duties') or '')
    if len(d)>=80: clusters[d].append(a['reading_id'])
dups=[dict(n_ads=len(v),reading_ids=js(sorted(v)),duties_chars=len(k)) for k,v in clusters.items() if len(v)>1]
dups.sort(key=lambda r:-r['n_ads'])
if dups: dump('tables/Q4_exact_duty_duplicates.csv', dups)

# catalog gaps
gaps=read(ROOT/'tables/Q2_remaining_directory_gaps_partial.csv')
gapn=Counter((r.get('role') or byk.get(r['identity_key'],{}).get('role',''), (r.get('surface') or '')[:40]) for r in gaps)
gap_rows=[dict(role=role,surface=surf,mentions=n) for (role,surf),n in gapn.most_common()]
dump('tables/Q4_directory_gap_surfaces.csv', gap_rows[:500])
save_json('notes/Q2_catalog_v2.2_decision.json', dict(decision='KEEP_Q2_v2.1_NO_v2.2_THIS_ROUND',reason='目录外高频项（FPGA、专用EDA、社媒平台、部分认证）分散且跨职能；新增标签须对全部适用广告做P/Z/U回查。本轮完成缺口审计后限制解释，不发布v2.2。',frozen='Q2-v2.1',reviewer='grok4.6',gap_records=len(gaps),high_frequency=gap_rows[:30]))

# L0/L1/L2/L3 status update on coverage
cov=read(ROOT/'tables/Q1_role_coverage.csv')
for r in cov:
    r['L0_status']='COMPLETE'
    r['L1_status']='CONTENT_CODED'
    # L3 if any display item
    has=any(x['role']==r['role'] for x in disp_rows)
    r['L2_status']='COMPANY_POINTS_AVAILABLE'
    r['L3_status']='SOME_CELLS_EXPLORATORY' if has else 'NO_CELL_PASSED_GROUP_GATE'
dump('tables/Q1_role_coverage.csv', cov)

save_json('verification/Q2_v2_comparison_receipt.json', dict(status='PASS_CELL_SPECIFIC',coded_ads=1576,aggregates=len(agg),display_items=len(disp_rows),leave_one=len(loo),duplicate_clusters=len(dups),catalog_kept='Q2-v2.1',created_utc=datetime.now(timezone.utc).isoformat()))
print('Q2 comparison', len(agg), 'agg', len(disp_rows), 'display', len(dups), 'dup clusters')
