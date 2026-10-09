"""Build 17-role second-pass queues from the frozen seeded sample plus U/NA/boundary/no-keyword."""
from common import *
import math
ads=read(ROOT/'tables/Q3_adjudicated_ads_partial.csv')
# Stream states only for U/NA identity sets to avoid holding 2.8M rows.
unknown=set(); naids=set()
with (ROOT/'tables/Q3_applicable_states_partial.csv').open(encoding='utf-8-sig',newline='') as f:
    r=csv.DictReader(f)
    for row in r:
        if row['state']=='U': unknown.add(row['identity_key'])
        elif row['state']=='NA': naids.add(row['identity_key'])
sample=defaultdict(set)
for row in read(ROOT/'tables/Q_quality_review_sample.csv'):
    sample[row['role']].add(row['identity_key'])
# zero-candidate ads
candn=Counter()
for rec in json.loads((ROOT/'notes/Q_semantic_review_queue.json').read_text(encoding='utf-8')):
    candn[rec['identity_key']]+=1
docs={}
for p in sorted((ROOT/'configs/Q_adjudications').glob('*.json')):
    docs[p.stem]=json.loads(p.read_text(encoding='utf-8'))['ads']
def get_ad(role, identity, rid):
    d=docs[role]
    if identity in d: return d[identity]
    if rid in d: return d[rid]
    for a in d.values():
        if a.get('identity_key')==identity: return a
    raise KeyError((role,rid))
allq=[]
inv_task=[]; inv_co=[]
receipts=[]
for cov in read(ROOT/'tables/Q1_role_coverage.csv'):
    role=cov['role']; roleads=[a for a in ads if a['role']==role]
    n=len(roleads)
    seeded=sample[role]
    assert len(seeded)==min(n, max(10, math.ceil(n*.2))), (role,len(seeded),n)
    qcreqs=[]
    for a in roleads:
        k=a['identity_key']; rid=a['reading_id']; d=get_ad(role,k,rid)
        reasons=[]
        if k in seeded: reasons.append('SEEDED_SAMPLE')
        if k in unknown: reasons.append('UNKNOWN')
        if k in naids: reasons.append('NA')
        if d.get('old_overrides'): reasons.append('DERIVED_CONTEXT_OR_OBJECT_CORRECTION')
        if any(isinstance(x,str) and x.startswith('OUTSIDE:') for x in d['new'].values()) or d.get('outside_extra'): reasons.append('CATALOG_BOUNDARY')
        if d.get('uncertainty_scope'): reasons.append('EXPLICIT_UNCERTAINTY')
        if candn[k]==0: reasons.append('NO_KEYWORD')
        if reasons:
            first=a.get('reviewer') or d.get('reader') or 'grok4.6'
            qcreqs.append(dict(reading_id=rid,identity_key=k,company_id=a['company_id'],role=role,reasons=js(reasons),status=d.get('qc_status') or 'PENDING_SECOND_PASS',first_pass_reader=first,second_pass_reviewer='grok4.6',independent_external_review='NO',same_model_reread='YES' if first=='grok4.6' else 'GROK_REVIEW_OF_ASTRA'))
    dump(f'tables/Q_{role}_second_pass_queue.csv', qcreqs)
    allq.extend(qcreqs)
    for task in sorted({a['task'] for a in roleads}):
        rr=[a for a in roleads if a['task']==task]
        inv_task.append(dict(role=role,task=task,ads=len(rr),companies=len({r['company_id'] for r in rr})))
    for co in sorted({a['company_id'] for a in roleads}):
        rr=[a for a in roleads if a['company_id']==co]
        inv_co.append(dict(role=role,company_id=co,ads=len(rr),tasks=js(Counter(r['task'] for r in rr))))
    receipts.append(dict(role=role,ads=n,seeded=len(seeded),queue=len(qcreqs),unknown=sum(a['identity_key'] in unknown for a in roleads),no_keyword=sum(candn[a['identity_key']]==0 for a in roleads)))
dump('tables/Q_all_second_pass_queue.csv', allq)
dump('tables/Q_task_inventory.csv', inv_task)
dump('tables/Q_company_inventory.csv', inv_co)
save_json('verification/Q_second_pass_queue_receipt.json', dict(status='QUEUE_BUILT_NOT_ALL_ADS_REREAD',seed=20260916,total_queue=len(allq),roles=receipts,note='Seeded sample is company round-robin from prepare_Q_coding.py and must not be regenerated. grok4.6 reviews Astra first-pass ads; grok rereads of grok first-pass are disclosed as same-model, not independent dual coding.'))
print('queue', len(allq), 'roles', len(receipts))
