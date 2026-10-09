"""Mark second-pass QC status. Seeded sample + systematic alias back-check; remaining queue is pattern-audited, not independent dual coding."""
from common import *
from datetime import datetime, timezone
sample={r['identity_key'] for r in read(ROOT/'tables/Q_quality_review_sample.csv')}
queue={r['identity_key'] for r in read(ROOT/'tables/Q_all_second_pass_queue.csv')}
n=0; counts=Counter()
for p in sorted((ROOT/'configs/Q_adjudications').glob('*.json')):
    data=json.loads(p.read_text(encoding='utf-8'))
    for store,a in data['ads'].items():
        k=a['identity_key']
        prev=a.get('qc_status')
        if prev=='SECOND_PASS_REVISED':
            st='SECOND_PASS_REVISED'
        elif k in sample:
            st='SECOND_PASS_SEEDED_CONFIRMED'
        elif k in queue:
            st='SECOND_PASS_QUEUE_PATTERN_AUDIT'
        else:
            st='SECOND_PASS_OUTSIDE_MANDATORY_QUEUE'
        a['qc_status']=st
        a['second_pass_reviewer']='grok4.6'
        a['independent_external_review']=False
        counts[st]+=1; n+=1
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
# refresh ad table qc_status
ads=read(ROOT/'tables/Q3_adjudicated_ads_partial.csv')
lookup={}
for p in sorted((ROOT/'configs/Q_adjudications').glob('*.json')):
    d=json.loads(p.read_text(encoding='utf-8'))
    for a in d['ads'].values():
        lookup[a['identity_key']]=a['qc_status']
for r in ads:
    r['qc_status']=lookup[r['identity_key']]
dump('tables/Q3_adjudicated_ads_partial.csv', ads)
save_json('verification/Q_second_pass_status.json', dict(reviewer='grok4.6',independent_external_review=False,seeded_sample=len(sample),mandatory_queue=len(queue),ads=n,status_counts=dict(counts),method='Company-stratified seed 20260916 sample plus all U/NA/catalog-boundary/no-keyword ads. Systematic frozen-alias back-check for V2_RS485. Same-model reread of grok first-pass is disclosed. Not external dual coding.',created_utc=datetime.now(timezone.utc).isoformat()))
print(dict(counts), 'n', n)
