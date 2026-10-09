"""Verify minimum-edit counts and hypothetical witnesses without production imports."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import csv,json

ROOT=Path(__file__).resolve().parents[2]
V3=ROOT/'source_snapshot'
V4=ROOT

def read(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def run():
    base=read(V4/'analysis/paired/paired_advertisements.csv')
    diag=read(V3/'source_v2/analysis/diagnostic_comparison.csv')
    policy=json.loads((V3/'data/sensitivity_policy.json').read_text(encoding='utf-8'))['groups']
    diag={r['audit_id']:r for r in diag}
    checks=0
    main=[]
    for result in read(V4/'analysis/paired/paired_breakdown_readings.csv'):
        bits=list(map(int,result['reading'].split('_')[1]))
        revised={(diag[a]['identity_key'],diag[a]['label_code']):diag[a]
                 for g,bit in zip(policy,bits) if bit for a in g['audit_ids']}
        rows=[]
        for original in base:
            if original['task']!=result['task']:continue
            if result['subset']=='both_mentioned' and not int(original['both_mentioned']):continue
            r=dict(original)
            for side in ['a','b']:
                k=r['identity_key'],r['target_'+side]
                if k in revised:
                    d=revised[k]
                    r['Q_'+side]='P' if 'P' in [d['G_fresh'],d['R_fresh']] else 'Z' if d['G_fresh']==d['R_fresh']=='Z' else 'U'
            rows.append(r)
        f=Counter(r['company_id'] for r in rows)
        t=Counter((r['company_id'],r['template_field'],r['template_hash']) for r in rows)
        firm_t=Counter(k[0] for k in t)
        weights={}
        for r in rows:
            if result['weighting']=='ad_equal':w=F(1,len(rows))
            elif result['weighting']=='firm_equal':w=F(1,len(f)*f[r['company_id']])
            else:w=F(1,len(f)*firm_t[r['company_id']]*t[r['company_id'],r['template_field'],r['template_hash']])
            weights[r['identity_key']]=w
        assert sum(weights.values(),F(0))==1;checks+=1
        lower=sum((weights[r['identity_key']]*(int(r['Q_a']=='P')-int(r['Q_b']!='Z')) for r in rows),F(0))
        upper=sum((weights[r['identity_key']]*(int(r['Q_a']!='Z')-int(r['Q_b']=='P')) for r in rows),F(0))
        sign=1 if lower>0 else -1 if upper<0 else 0
        assert sign==int(result['direction']);checks+=1
        margin=lower if sign==1 else -upper if sign==-1 else F(0)
        assert abs(float(100*margin)-float(result['margin_pp']))<1e-10;checks+=1
        if not sign:
            assert int(result['minimum_pair_state_edits'])==int(result['minimum_advertisements_edited'])==0
            assert json.loads(result['pair_edit_witness_json'])==json.loads(result['advertisement_edit_witness_json'])==[]
            checks+=2
            continue
        high,low=('a','b') if sign==1 else ('b','a')
        legal={}
        byad={}
        for r in rows:
            k=r['identity_key'];w=weights[k];candidate=[]
            if r['Q_'+high]=='P':candidate.append(k+'|'+high+'|P_to_Z')
            if r['Q_'+low]=='Z' and int(r['M_'+low]):candidate.append(k+'|'+low+'|Z_to_P')
            for item in candidate:legal[item]=w
            if candidate:byad[k]=w*len(candidate)
        for cost_col,witness_col,cap in [('minimum_pair_state_edits','pair_edit_witness_json',legal),
                                         ('minimum_advertisements_edited','advertisement_edit_witness_json',byad)]:
            witness=json.loads(result[witness_col]);cost=int(result[cost_col])
            assert len(witness)==len(set(witness))==cost;checks+=1
            assert set(witness)<=set(cap);checks+=1
            assert sum((cap[k] for k in witness),F(0))>=margin;checks+=1
            # For any smaller selection, the sum of the largest cost-1 possible
            # effects is an upper bound; if this is insufficient, optimality is
            # proven without relying on which production witness was chosen.
            maximum_smaller=sum(sorted(cap.values(),reverse=True)[:cost-1],F(0))
            assert maximum_smaller<margin;checks+=1
        if result['reading']=='READING_0000000' and result['task']=='ROBOT_MODEL':
            main.append({k:result[k] for k in ['task','subset','weighting','margin_pp','minimum_pair_state_edits','minimum_advertisements_edited']})
    report={'status':'PASS','arithmetic_feasibility_and_optimality_checks':checks,
            'scenario_rows':2304,'primary_robot_model':main,
            'interpretation':'Minimum corrections to lose the original strict direction; a discrete correction may cross past zero rather than make the interval include zero.',
            'independent_human_source_validation':False,
            'advertisement_cost_assumption':'An edited advertisement may change both resolved target Q states without additional ad cost.',
            'scope':'M, U membership, sample and weights fixed within each reading. No estimated error probability.'}
    (V4/'analysis/empirical/paired_breakdown_independent_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':run()
