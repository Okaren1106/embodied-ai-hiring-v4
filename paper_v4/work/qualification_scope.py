"""Construct scope ladder from existing v3 source-context classifications.

M = explicit mention anywhere in the retained coding scope.
H = a mention recorded in GENERAL or REQUIRED qualification context, regardless
    of local choice/example/uncertain operator. H is candidate-context inclusion,
    not an unconditional or mandatory requirement and not a new human label.
Q = existing union of unqualified GENERAL and REQUIRED target expressions.
Q <= H <= M is checked for every row; metric coding is held fixed.
Scope alternatives add existing EXAMPLE or all choice/example qualification
branches to Q. These are changes of construct, NOT alternative truths or
unknown completions. They deliberately show whether the new paired finding
survives defining qualification inclusion more broadly.
"""
from pathlib import Path
from collections import defaultdict,Counter
import csv,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT/'source_snapshot'
OUT=ROOT/'analysis/paired'
def read(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(name,rows):
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def main():
    state_path=ROOT/'analysis/v4_ad_technology_current.csv'
    context_path=OLD/'source_v2/data/inputs/context_index.csv'
    evidence_path=OLD/'source_v2/data/inputs/context_evidence.csv'
    revision_path=OLD/'data/analysis_revision_ledger.json'
    revision_ledger=json.loads(revision_path.read_text(encoding='utf-8'))
    clarifications={ (r['identity_key'],r['label_code']):r for r in revision_ledger['changes'] }
    assert {r['audit_id'] for r in clarifications.values()}=={'A032','A065','A099'}
    v4_revision_path=ROOT/'data/v4_source_corrections.json'
    v4_ledger=json.loads(v4_revision_path.read_text(encoding='utf-8'))
    v4_clarifications={(r['identity_key'],r['label_code']):r for r in v4_ledger['changes']}
    assert not set(clarifications)&set(v4_clarifications)
    rows=read(state_path);context=read(context_path);evidence=read(evidence_path)
    records=json.loads((OLD/'source_v2/data/inputs/records.json').read_text(encoding='utf-8'))
    sources={r['identity_key']:r for r in records}; key=lambda r:(r['identity_key'],r['label_code'])
    bycontext={key(r):r for r in context};assert len(bycontext)==len(context)==len(rows)==496
    assert set(bycontext)=={key(r) for r in rows}
    byev=defaultdict(list);checks=[]
    for e in evidence:
        byev[e['identity_key'],e['code']].append(e)
        text=sources[e['identity_key']]['fields'][e['field']]
        start,end=int(e['verified_start']),int(e['verified_end'])
        exact=text[start:end]==e['quote']
        hash_ok=hashlib.sha256(text.encode()).hexdigest()==e['source_field_sha256']
        checks.append({'identity_key':e['identity_key'],'evidence_id':e['evidence_id'],'field':e['field'],
                       'exact_span':int(exact),'source_hash_match':int(hash_ok)})
        assert exact and hash_ok,(e['reading_id'],e['evidence_id'])
    out=[]
    for r in rows:
        c=bycontext[key(r)];ev=byev[key(r)]
        gm=[e for e in ev if e['metric'] in ['GENERAL','REQUIRED']]
        h=int(any(m in ['GENERAL','REQUIRED'] for m in json.loads(c['metrics_json'])))
        assert h==int(bool(gm)),(r['reading_id'],r['label_code'],'context/evidence mismatch')
        q=int(r['Q']=='P');m=int(r['M']);assert q<=h<=m
        example=int(any(e['branch']=='EXAMPLE' for e in gm))
        relation=int(any(e['branch'] in ['EXAMPLE','CHOICE','CHOICE_AND_EXAMPLE'] for e in gm))
        clarified_example=key(r) in clarifications
        if clarified_example:
            # v3 resolves three original UNRESOLVED operators as explicit examples.
            # Carry that existing adjudication forward into the expanded construct.
            assert r['revised']=='1' and r['Q']=='Z' and h==1
            assert r['revision_audit_id']==clarifications[key(r)]['audit_id']
            assert any(e['branch']=='UNRESOLVED' for e in gm)
            example=relation=1
        v4_clarification=v4_clarifications.get(key(r))
        parenthetical_ambiguity=False
        if v4_clarification:
            assert r['revised']=='1' and h==1
            assert r['revision_audit_id']==v4_clarification['audit_id']
            governing=v4_clarification['governing_relation']
            if governing=='UNCONDITIONAL_OR_EXAMPLE':
                assert r['Q']=='U'
                # Both declared readings enter the union construct. Neither is
                # independently known to be the correct local interpretation.
                parenthetical_ambiguity=True;example=relation=0
            else:
                assert r['Q']=='Z' and any(e['branch']=='UNRESOLVED' for e in gm)
                example=int(bool(example) or governing=='EXAMPLE')
                relation=int(bool(relation) or governing in ['EXAMPLE','CHOICE','CHOICE_AND_EXAMPLE'])
        extended_example='P' if q or example or parenthetical_ambiguity else r['Q']
        extended_relations='P' if q or relation or parenthetical_ambiguity else r['Q']
        out.append({k:r[k] for k in ['identity_key','reading_id','company_id','task','label_code','M','Q']}|
                   {'H_qualification_context':h,'H_extra_over_Q':h-q,
                    'example_qualification':example,'choice_or_example_qualification':relation,
                    'v3_example_clarification_applied':int(clarified_example),
                    'v4_scope_clarification_applied':int(bool(v4_clarification)),
                    'v4_governing_relation':v4_clarification['governing_relation'] if v4_clarification else '',
                    'unconditional_or_example_ambiguous':int(parenthetical_ambiguity),
                    'Q_plus_example':extended_example,'Q_plus_choice_example':extended_relations,
                    'qualification_evidence_ids':json.dumps([e['evidence_id'] for e in gm]),
                    'qualification_branches':json.dumps(sorted({e['branch'] for e in gm}))})
    write('qualification_scope_states.csv',out);write('source_span_verification.csv',checks)
    tasksummary=[]
    for label in sorted({r['label_code'] for r in out}):
        rr=[r for r in out if r['label_code']==label];n=len(rr)
        tasksummary.append({'task':rr[0]['task'],'label_code':label,'ads':n,
                            'M':sum(int(r['M']) for r in rr),'H':sum(r['H_qualification_context'] for r in rr),
                            'Q_P':sum(r['Q']=='P' for r in rr),'Q_U':sum(r['Q']=='U' for r in rr),
                            'Q_plus_example_P':sum(r['Q_plus_example']=='P' for r in rr),
                            'Q_plus_example_U':sum(r['Q_plus_example']=='U' for r in rr),
                            'Q_plus_choice_example_P':sum(r['Q_plus_choice_example']=='P' for r in rr),
                            'Q_plus_choice_example_U':sum(r['Q_plus_choice_example']=='U' for r in rr)})
    write('qualification_scope_summary.csv',tasksummary)
    pairs=read(OUT/'paired_advertisements.csv');states={key(r):r for r in out};contrasts=[]
    for task in sorted({p['task'] for p in pairs}):
        for subset in ['all_ads','both_mentioned']:
            rr=[r for r in pairs if r['task']==task and (subset=='all_ads' or int(r['both_mentioned']))]
            n=len(rr)
            for measure in ['M','H_qualification_context','Q','Q_plus_example','Q_plus_choice_example']:
                counts=Counter()
                for p in rr:
                    for ab in ['a','b']:
                        v=states[p['identity_key'],p['target_'+ab]][measure]
                        if measure in ['M','H_qualification_context']:v='P' if int(v) else 'Z'
                        counts[ab,v]+=1
                contrasts.append({'task':task,'subset':subset,'measure':measure,'ads':n,
                    'a_P':counts['a','P'],'a_U':counts['a','U'],'b_P':counts['b','P'],'b_U':counts['b','U'],
                    'confirmed_gap_pp':100*(counts['a','P']-counts['b','P'])/n,
                    'difference_lo_pp':100*(counts['a','P']-counts['b','P']-counts['b','U'])/n,
                    'difference_hi_pp':100*(counts['a','P']+counts['a','U']-counts['b','P'])/n})
    write('qualification_scope_contrasts.csv',contrasts)
    audit={'state_rows':len(out),'source_spans':len(checks),'all_spans_and_hashes_verified':True,
           'Q_subset_H_subset_M':True,'H_metric_evidence_reconciled':True,'classification_changed_by_construct_step':False,
           'v4_state_overlay_used':True,
           'scope_alternatives_are_different_constructs':True,'independent_human_validation':False,
           'existing_example_clarifications_applied':sum(r['v3_example_clarification_applied'] for r in out),
           'v4_scope_clarifications_applied':sum(r['v4_scope_clarification_applied'] for r in out),
           'inputs':[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [state_path,context_path,evidence_path,revision_path,v4_revision_path]],'failures':0}
    (OUT/'qualification_scope_checks.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps([r for r in contrasts if r['task']=='ROBOT_MODEL'],indent=2))
if __name__=='__main__':main()
