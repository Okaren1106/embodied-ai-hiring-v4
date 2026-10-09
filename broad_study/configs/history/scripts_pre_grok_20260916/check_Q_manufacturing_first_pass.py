"""First-pass structural checkpoint, never semantic acceptance or final comparison."""
from common import *
import math
rolecode='RF_MANUFACTURING_QUALITY_SUPPLY'
ads=read(ROOT/'tables/Q3_adjudicated_ads_partial.csv')
roleads=[a for a in ads if a['role']==rolecode]
assert len(roleads)==215 and len({a['reading_id'] for a in roleads})==215
assert {a['identity_key'] for a in roleads}=={k for k,j in J.items() if role(j)==rolecode}
evidence=[r for r in read(ROOT/'tables/Q3_semantic_evidence_partial.csv') if r['role']==rolecode]
states=[r for r in read(ROOT/'tables/Q3_applicable_states_partial.csv') if r['role']==rolecode]
sx={(r['reading_id'],r['label_code'],r['metric'],r['branch']):r['state'] for r in states}
assert len(sx)==len(states)==215*192*14
# Researcher-defined unknown scopes: neither strength nor branch may leak.
goldens=[
('N0784','V2_QUALITY_CREDENTIAL',{('PREFERRED','CHOICE')}),
('N0382','V2_TRITON_COMPILER',{('PREFERRED','EXAMPLE')}),
('N0429','V2_DFM',{('DUTY_OWN_USE','UNCONDITIONAL'),('DUTY_OWN_DEVELOP','UNCONDITIONAL')}),
]
for rid,c,expected in goldens:
 actual={(m,b) for (r,cc,m,b),v in sx.items() if r==rid and cc==c and v=='U'}
 assert actual==expected,(rid,c,expected,actual)
frame=read(ROOT/'tables/Q3_coding_frame.csv')
coded={a['reading_id'] for a in ads}
assert {r['reading_id'] for r in frame if r['status']=='CODED_FIRST_PASS'}==coded
pending_total=len([r for r in frame if r['status']=='PENDING'])
assert len(frame)==1576 and pending_total==1576-len(coded)
# Every emitted positive needs same-ad, same-item, exact-slice evidence.
positive={(r['reading_id'],r['code'],r['metric'],r['branch']) for r in evidence}
assert all(k in positive for k,v in sx.items() if v=='P')
unknownids={r['reading_id'] for r in states if r['state']=='U'}
naids={r['reading_id'] for r in states if r['state']=='NA'}
sample={r['reading_id'] for r in read(ROOT/'tables/Q_quality_review_sample.csv') if r['role']==rolecode}
assert len(sample)==max(10,math.ceil(215*.2))==43
data=json.loads((ROOT/'configs/Q_adjudications'/f'{rolecode}.json').read_text(encoding='utf-8'))['ads']
qcreqs=[]
for a in roleads:
 rid=a['reading_id'];d=data[rid];reasons=[]
 if rid in sample:reasons.append('SEEDED_SAMPLE')
 if rid in unknownids:reasons.append('UNKNOWN')
 if rid in naids:reasons.append('NA')
 if d.get('old_overrides'):reasons.append('DERIVED_CONTEXT_OR_OBJECT_CORRECTION')
 if any(isinstance(x,str) and x.startswith('OUTSIDE:') for x in d['new'].values()) or d.get('outside_extra'):reasons.append('CATALOG_BOUNDARY')
 if d.get('uncertainty_scope'):reasons.append('EXPLICIT_UNCERTAINTY')
 if reasons:qcreqs.append(dict(reading_id=rid,identity_key=a['identity_key'],company_id=a['company_id'],role=rolecode,reasons=js(reasons),status='PENDING_SECOND_PASS',reviewer='Astra',independent_external_review='NO'))
dump('tables/Q_manufacturing_second_pass_queue.csv',qcreqs)
tasks=[]
for task in sorted({a['task'] for a in roleads}):
 rr=[a for a in roleads if a['task']==task]
 tasks.append(dict(role=rolecode,task=task,ads=len(rr),companies=len({r['company_id'] for r in rr}),status='FIRST_PASS_DESCRIPTIVE_NOT_FINAL'))
dump('tables/Q_manufacturing_first_pass_task_inventory.csv',tasks)
perco=[]
for co in sorted({a['company_id'] for a in roleads}):
 rr=[a for a in roleads if a['company_id']==co]
 perco.append(dict(company_id=co,ads=len(rr),tasks=js(Counter(r['task'] for r in rr)),status='FIRST_PASS_DESCRIPTIVE_NOT_FINAL'))
dump('tables/Q_manufacturing_first_pass_company_inventory.csv',perco)
protected=lock_check(originals=True)
receipt=dict(status='FIRST_PASS_STRUCTURAL_CHECKPOINT_NOT_SEMANTIC_ACCEPTANCE',role=rolecode,coded_ads=215,companies=len(perco),role_labels=192,explicit_states=len(states),evidence=len(evidence),state_counts=dict(Counter(r['state'] for r in states)),derived_old_changes=sum(r['reading_id'] in data for r in read(ROOT/'tables/Q2_v2_semantic_changes_partial.csv')),seeded_qc_ads=43,mandatory_qc_queue_ads=len(qcreqs),unknown_ads=len(unknownids),full_second_pass_complete=sum(a['qc_status']!='PENDING_SECOND_PASS' for a in roleads),remaining_role_ads=0,remaining_project_ads=pending_total,original_lock_check=protected)
save_json('verification/Q_manufacturing_first_pass_checkpoint.json',receipt)
print(js(receipt))
print(js(tasks))
