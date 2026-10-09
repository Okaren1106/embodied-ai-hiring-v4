"""Final verification on current RUN tables. Isolated rematerialize compared separately."""
from common import *
from collections import Counter
import json
checks=[]
def ok(name,cond,detail=''):
    checks.append(dict(check=name,status='PASS' if cond else 'FAIL',detail=str(detail)[:500]))
    if not cond: print('FAIL',name,detail)
lock=lock_check(); ok('input_lock',lock==909,lock)
ads=read(ROOT/'tables/Q3_adjudicated_ads_partial.csv')
ok('ads_1576',len(ads)==1576,len(ads))
ok('pending_zero',all(r['status']=='CODED_FIRST_PASS' for r in ads),'')
keys=[r['identity_key'] for r in ads]
ok('identity_unique',len(keys)==len(set(keys)),len(keys)-len(set(keys)))
ok('e0107_two_identities',sum(r['reading_id']=='E0107' for r in ads)==2,sum(r['reading_id']=='E0107' for r in ads))
# jobs identities
ok('ads_subset_jobs',set(keys)<=set(J),len(set(keys)-set(J)))
# B=P+Z+U on aggregates sample
agg=read(ROOT/'tables/Q4_aggregates.csv')
bad=0
for r in agg:
    P,U,Z,N,B=int(r['P']),int(r['U']),int(r['Z']),int(r['N']),int(r['B'])
    if P+Z+U!=B or P+Z!=N: bad+=1
ok('aggregate_identities',bad==0,bad)
disp=read(ROOT/'tables/Q4_display_items.csv')
ok('display_115',len(disp)==115,len(disp))
# display rows exist in aggregates
idx={(r['scope'],r['role'],r['label_code'],r['metric'],r['branch']) for r in agg}
miss=sum(1 for r in disp if (r['scope'],r['role'],r['label_code'],r['metric'],r['branch']) not in idx)
ok('display_in_aggregates',miss==0,miss)
# D identity
d=read(ROOT/'tables/D2_decomposition_summary.csv')
d_bad=0
for r in d:
    if r.get('qualification')!='ELIGIBLE': continue
    if r.get('delta_pp') in ('',None): continue
    delta=float(r['delta_pp']); c=float(r['composition_pp']); w=float(r['within_role_pp'])
    if abs(delta-(c+w))>1e-8: d_bad+=1
ok('D_C_plus_W',d_bad==0,d_bad)
# catalog codes in frozen
cat=json.loads((ROOT/'configs/Q_catalog_v2_frozen.json').read_text(encoding='utf-8'))
codes={x['code'] for x in cat['labels']}
badc=sum(1 for r in disp if r['label_code'] not in codes)
ok('display_codes_in_catalog',badc==0,badc)
# quote locate sample from evidence
ev=read(ROOT/'tables/Q3_semantic_evidence_partial.csv')
ok('evidence_nonzero',len(ev)>=25500,len(ev))
sample=ev[0],ev[len(ev)//2],ev[-1]
qloc=0
for r in sample:
    k=r['identity_key']; f=r['field']; q=r['quote']
    txt=RAW[k].get(f,'') or ''
    if q and txt[int(r['start']):int(r['end'])]==q: qloc+=1
ok('quote_sample_3',qloc==3,qloc)
# second pass marked
qc=Counter(r['qc_status'] for r in ads)
ok('second_pass_all_marked',sum(qc.values())==1576 and 'PENDING_SECOND_PASS' not in qc,dict(qc))
# research/ops L3
cov=read(ROOT/'tables/Q1_role_coverage.csv')
rs=[r for r in cov if r['role'] in ('RF_RESEARCH_SCIENCE','RF_ROBOT_OPERATIONS')]
ok('sparse_no_L3',all(r['L3_status']=='NO_CELL_PASSED_GROUP_GATE' for r in rs),[r['L3_status'] for r in rs])
ok('L0_all_complete',all(r['L0_status']=='COMPLETE' for r in cov),'')
# catalog decision
dec=json.loads((ROOT/'notes/Q2_catalog_v2.2_decision.json').read_text(encoding='utf-8'))
ok('catalog_kept_v21',dec['decision'].startswith('KEEP_Q2_v2.1'),dec['decision'])
fails=[c for c in checks if c['status']=='FAIL']
save_json('verification/Q2_final_verification.json', dict(status='PASS' if not fails else 'FAIL',n=len(checks),fails=fails,checks=checks,evidence_n=len(ev),aggregates=len(agg)))
print('verification', 'PASS' if not fails else 'FAIL', len(checks), 'fails', len(fails))
