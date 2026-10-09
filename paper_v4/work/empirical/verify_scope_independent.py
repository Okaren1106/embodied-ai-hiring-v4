"""Rebuild qualification-scope measures from frozen evidence and v4 states.

No production module is imported. GENERAL/REQUIRED scope is inherited as an
observed coding decision; this checks its aggregation, not independent truth.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
import csv,json,hashlib

ROOT=Path(__file__).resolve().parents[2]
V3=ROOT/'source_snapshot'
V4=ROOT
OUT=V4/'analysis/empirical'

def read(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def run():
    states=read(V4/'analysis/v4_ad_technology_current.csv')
    evidence=read(V3/'source_v2/data/inputs/context_evidence.csv')
    source=json.loads((V3/'source_v2/data/inputs/records.json').read_text(encoding='utf-8'))
    source={r['identity_key']:r for r in source}
    revisions=json.loads((V3/'data/analysis_revision_ledger.json').read_text(encoding='utf-8'))['changes']
    clarification={(r['identity_key'],r['label_code']) for r in revisions}
    v4_changes=json.loads((V4/'data/v4_source_corrections.json').read_text(encoding='utf-8'))['changes']
    v4_relations={(r['identity_key'],r['label_code']):r['governing_relation'] for r in v4_changes}
    assert {r['audit_id'] for r in revisions}=={'A032','A065','A099'}
    qualifying=defaultdict(list)
    checks=0
    for r in evidence:
        raw=source[r['identity_key']]['fields'][r['field']]
        assert raw[int(r['verified_start']):int(r['verified_end'])]==r['quote'];checks+=1
        assert hashlib.sha256(raw.encode()).hexdigest()==r['source_field_sha256'];checks+=1
        if r['metric'] in {'GENERAL','REQUIRED'}:qualifying[r['identity_key'],r['code']].append(r)
    reconstructed={}
    transitions=Counter()
    output=read(V4/'analysis/paired/qualification_scope_states.csv')
    output={(r['identity_key'],r['label_code']):r for r in output}
    diagnostic=[]
    for r in states:
        k=r['identity_key'],r['label_code'];e=qualifying[k]
        branches={x['branch'] for x in e}
        # Apply existing v3 source adjudications to the newly expanded metric;
        # the old evidence file is intentionally not rewritten.
        if k in clarification:
            assert r['Q']=='Z' and r['revised']=='1' and 'UNRESOLVED' in branches
            branches.add('EXAMPLE')
        if k in v4_relations:
            if v4_relations[k]=='UNCONDITIONAL_OR_EXAMPLE':
                assert r['Q']=='U' and branches&{'UNCONDITIONAL','EXAMPLE'}
                assert output[k]['unconditional_or_example_ambiguous']=='1'
                assert output[k]['example_qualification']==output[k]['choice_or_example_qualification']=='0'
                checks+=3
                # Under either allowed reading, Q plus examples includes the
                # target. Uncertainty in narrow Q need not propagate to this
                # broader construct when both possible states imply positive.
                branches.add('EXAMPLE')
            else:
                assert r['Q']=='Z' and 'UNRESOLVED' in branches
                branches.add(v4_relations[k])
        h=int(bool(e))
        example=bool(branches&{'EXAMPLE'})
        options=bool(branches&{'EXAMPLE','CHOICE','CHOICE_AND_EXAMPLE'})
        ex='P' if r['Q']=='P' or example else r['Q']
        opt='P' if r['Q']=='P' or options else r['Q']
        made={'M':int(r['M']),'H_qualification_context':h,'Q':r['Q'],
              'Q_plus_example':ex,'Q_plus_choice_example':opt}
        assert int(r['Q']=='P')<=h<=int(r['M'])
        if r['Q']=='U':assert h==1,('U outside inherited qualification scope',k)
        for field,value in made.items():assert str(value)==output[k][field],(k,field);checks+=1
        for measure in ['Q_plus_example','Q_plus_choice_example']:
            transitions[r['task'],r['label_code'],measure,r['Q'],made[measure]]+=1
        reconstructed[k]=made
        if k in clarification:
            diagnostic.append({'reading_id':r['reading_id'],'audit_id':r['revision_audit_id'],
                               'Q_current':r['Q'],'H':h,'example_originally_recorded':int(any(x['branch']=='EXAMPLE' for x in e)),
                               'Q_plus_example_with_existing_clarification':ex})
    paired=read(V4/'analysis/paired/paired_advertisements.csv')
    verified_contrasts=[]
    for result in read(V4/'analysis/paired/qualification_scope_contrasts.csv'):
        rs=[p for p in paired if p['task']==result['task'] and (result['subset']=='all_ads' or int(p['both_mentioned']))]
        counts=Counter()
        for r in rs:
            for side in ['a','b']:
                q=reconstructed[r['identity_key'],r['target_'+side]][result['measure']]
                q=('P' if q else 'Z') if isinstance(q,int) else q
                counts[side,q]+=1
        assert len(rs)==int(result['ads'])
        for side,state in [('a','P'),('a','U'),('b','P'),('b','U')]:
            assert counts[side,state]==int(result[side+'_'+state]);checks+=1
        p=counts['a','P']-counts['b','P'];n=len(rs)
        expected={'confirmed_gap_pp':F(100*p,n),
                  'difference_lo_pp':F(100*(p-counts['b','U']),n),
                  'difference_hi_pp':F(100*(p+counts['a','U']),n)}
        for col,value in expected.items():assert abs(float(value)-float(result[col]))<1e-10;checks+=1
        if result['task']=='ROBOT_MODEL':verified_contrasts.append(result)
    tx=[{'task':k[0],'label_code':k[1],'measure':k[2],'Q_before':k[3],'state_after':k[4],'pairs':n}
        for k,n in sorted(transitions.items())]
    with (OUT/'qualification_scope_transitions_independent.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(tx[0]));w.writeheader();w.writerows(tx)
    report={'status':'PASS','independent_arithmetic_and_span_checks':checks,
            'raw_evidence_rows':len(evidence),'independent_source_human_validation':False,
            'all_current_U_have_inherited_qualification_scope':True,
            'existing_three_clarifications':diagnostic,
            'additional_v4_governing_relations':{r['audit_id']:r['governing_relation'] for r in v4_changes},
            'U_to_P_transitions':[r for r in tx if r['Q_before']=='U' and r['state_after']=='P'],
            'verified_robot_model_contrasts':verified_contrasts,
            'construct_caveat':'H includes names in GENERAL/REQUIRED scope under any local branch. It is not evidence that each named skill is individually required.'}
    (OUT/'qualification_scope_independent_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':run()
