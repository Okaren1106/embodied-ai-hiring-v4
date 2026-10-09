"""Independent arithmetic/provenance audit of the TensorFlow extension.

No extension production module is imported. Source-review annotations are
model judgments being audited for their stated arithmetic implications, not
an independent human semantic gold standard.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import csv,json,re,hashlib,itertools

ROOT=Path(__file__).resolve().parents[2]
EXT=ROOT/'extensions/framework_control'
OUT=ROOT/'analysis/empirical'
MEASURES=['M','H','Q','Q_plus_example','Q_plus_choice_example']
TF=re.compile(r'(?<![A-Za-z0-9_])tensorflow(?![A-Za-z0-9_])',re.I)
PY=re.compile(r'(?<![A-Za-z0-9_])pytorch(?![A-Za-z0-9_])',re.I)
SHORT=re.compile(r'(?<![A-Za-z0-9_])tf(?![A-Za-z0-9_])',re.I)

def read(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def as_state(x):return ('P' if x else 'Z') if isinstance(x,int) else x
def derive(annotation):
    qual=annotation['metric'] in ['GENERAL','REQUIRED']
    b=annotation['branch']
    if not qual:return {'M':1,'H':0,'Q':'Z','Q_plus_example':'Z','Q_plus_choice_example':'Z'}
    q='P' if b=='UNCONDITIONAL' else 'U' if b in ['UNRESOLVED','UNCONDITIONAL_OR_EXAMPLE'] else 'Z'
    ex='P' if b in ['UNCONDITIONAL','EXAMPLE','UNCONDITIONAL_OR_EXAMPLE'] else q
    ch='P' if b in ['UNCONDITIONAL','EXAMPLE','CHOICE','CHOICE_AND_EXAMPLE','UNCONDITIONAL_OR_EXAMPLE'] else q
    return {'M':1,'H':1,'Q':q,'Q_plus_example':ex,'Q_plus_choice_example':ch}

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    inputs={'sources':ROOT/'source_snapshot/source_v2/data/inputs/records.json',
            'annotations':EXT/'data/source_review_annotations.json',
            'pytorch_scope':ROOT/'analysis/paired/qualification_scope_states.csv'}
    hashes={k:sha(p) for k,p in inputs.items()}
    sources=[r for r in json.loads(inputs['sources'].read_text(encoding='utf-8')) if r['task']=='ROBOT_MODEL']
    annotations=json.loads(inputs['annotations'].read_text(encoding='utf-8'))
    scope={r['identity_key']:r for r in read(inputs['pytorch_scope']) if r['task']=='ROBOT_MODEL' and r['label_code']=='SK_PYTORCH'}
    assert len(sources)==len(scope)==105 and len(annotations)==26
    tf_output={r['identity_key']:r for r in read(EXT/'outputs/tensorflow_states_105.csv')}
    pairs={r['identity_key']:r for r in read(EXT/'outputs/paired_states_105.csv')}
    reviews={r['identity_key']:r for r in read(EXT/'outputs/source_review_26.csv')}
    assert len(tf_output)==len(pairs)==105 and len(reviews)==26
    rows=[];checks=0;occurrences=0;fields=0;preferred=[];annotation_rids=set();source_matches=[]
    for s in sources:
        k=s['identity_key'];rid=s['reading_id'];hit=False
        for field,body in s['fields'].items():
            assert not SHORT.search(body);checks+=1;fields+=1
            matches=list(TF.finditer(body));occurrences+=len(matches)
            hit=hit or bool(matches)
            for m in matches:
                assert m.group().lower()=='tensorflow';checks+=1
        inherited={'M':int(scope[k]['M']),'H':int(scope[k]['H_qualification_context']),
                   **{m:scope[k][m] for m in MEASURES[2:]}}
        if hit:
            assert rid in annotations;checks+=1;annotation_rids.add(rid)
            a=annotations[rid]
            assert a['full_captured_source_model_read'] is True;checks+=1
            assert a['independent_human_validation'] is False;checks+=1
            assert a['same_predicate_and_operator_as_pytorch'] is True;checks+=1
            assert a['independent_separate_tensorflow_qualification_found'] is False;checks+=1
            assert a['independent_separate_pytorch_qualification_found'] is False;checks+=1
            tf=derive(a);harm=dict(tf)
            if not tf['H']:preferred.append(rid)
            rev=reviews[k];raw=s['fields'][rev['source_field']]
            p0,p1=int(rev['parent_start']),int(rev['parent_end'])
            assert raw[p0:p1]==rev['parent_text'];checks+=1
            assert hashlib.sha256(raw.encode()).hexdigest()==rev['source_field_sha256'];checks+=1
            # Verify the same recorded full-source parent encloses all literal
            # occurrences of BOTH targets. This checks the structural premise,
            # not the semantic judgment about the operator's meaning.
            assert rev['source_field']=='full_description';checks+=1
            for pat in [TF,PY]:
                hits=list(pat.finditer(raw));assert hits;checks+=1
                assert all(p0<=m.start()<m.end()<=p1 for m in hits);checks+=1
            source_matches.append({'reading_id':rid,'parent_field':rev['source_field'],'parent_start':p0,'parent_end':p1,
                                   'metric':a['metric'],'branch':a['branch'],'full_source_parent_verified':True})
        else:
            assert rid not in annotations and k not in reviews;checks+=1
            tf={'M':0,'H':0,'Q':'Z','Q_plus_example':'Z','Q_plus_choice_example':'Z'};harm=dict(inherited)
        for m in MEASURES:
            assert str(tf[m])==tf_output[k][m];checks+=1
            for prefix,d in [('inherited_pytorch',inherited),('harmonized_pytorch',harm),('tensorflow',tf)]:
                assert str(d[m])==pairs[k][prefix+'_'+m];checks+=1
        assert int(pairs[k]['both_mentioned'])==int(bool(tf['M'] and inherited['M']));checks+=1
        rows.append({'id':k,'rid':rid,'both':bool(tf['M'] and inherited['M']),'tf':tf,'inherited':inherited,'harmonized':harm})
    assert annotation_rids==set(annotations);checks+=1
    assert len(preferred)==4 and all(annotations[r]['metric']=='PREFERRED' for r in preferred);checks+=1
    assert occurrences==53;checks+=1
    contrasts=[]
    for result in read(EXT/'outputs/framework_contrasts.csv'):
        side='inherited' if result['version']=='inherited_PyTorch_vs_new_TF' else 'harmonized'
        rr=[r for r in rows if result['subset']=='all_ads' or r['both']];n=len(rr);m=result['measure']
        ac=Counter(as_state(r[side][m]) for r in rr);bc=Counter(as_state(r['tf'][m]) for r in rr)
        assert n==int(result['ads']);checks+=1
        for prefix,c in [('a',ac),('b',bc)]:
            for z in ['P','U']:assert c[z]==int(result[prefix+'_'+z]);checks+=1
        p=ac['P']-bc['P'];lo=F(100*(p-bc['U']),n);hi=F(100*(p+ac['U']),n)
        for name,value in [('confirmed_gap_pp',F(100*p,n)),('difference_lo_pp',lo),('difference_hi_pp',hi)]:
            assert abs(float(value)-float(result[name]))<1e-10;checks+=1
        if side=='harmonized':contrasts.append(result)
    coupled=[]
    for result in read(EXT/'outputs/coupled_reading_diagnostic.csv'):
        rr=[r for r in rows if result['subset']=='all_ads' or r['both']];m=result['measure'];n=len(rr)
        shared=[r for r in rr if r['rid'] in ['N0149','N0798'] and r['harmonized'][m]==r['tf'][m]=='U']
        assert {r['rid'] for r in shared}==set(json.loads(result['coupled_reading_ids']));checks+=1
        endpoints=[]
        for bits in itertools.product([0,1],repeat=len(shared)):
            assignments={r['id']:x for r,x in zip(shared,bits)};lo=F(0);hi=F(0)
            for r in rr:
                a,b=r['harmonized'][m],r['tf'][m]
                if r['id'] in assignments:a=b='P' if assignments[r['id']] else 'Z'
                lo+=F(int(a=='P')-int(b!='Z'),n)
                hi+=F(int(a!='Z')-int(b=='P'),n)
            endpoints.append((100*lo,100*hi))
        lower=min(e[0] for e in endpoints);upper=max(e[1] for e in endpoints)
        assert abs(float(lower)-float(result['lower_pp_under_shared_completion']))<1e-10;checks+=1
        assert abs(float(upper)-float(result['upper_pp_under_shared_completion']))<1e-10;checks+=1
        if result['subset']=='both_mentioned':assert lower==upper==0;checks+=1
        coupled.append(result)
    assert all(r['harmonized']==r['inherited'] for r in rows);checks+=1
    assert hashes=={k:sha(p) for k,p in inputs.items()};checks+=1
    report={'status':'PASS','independent_arithmetic_and_source_checks':checks,
            'model_task_ads':len(rows),'both_framework_mentions':sum(r['both'] for r in rows),
            'source_fields_scanned':fields,'TensorFlow_literal_occurrences_across_fields':occurrences,
            'TF_abbreviation_occurrences':0,'preferred_scope_excluded_advertisements':preferred,
            'annotation_metric_counts':dict(Counter(a['metric'] for a in annotations.values())),
            'annotation_branch_counts':dict(Counter(a['branch'] for a in annotations.values())),
            'verified_harmonized_contrasts':contrasts,'verified_coupled_diagnostics':coupled,
            'inherited_and_harmonized_PyTorch_equal_after_seven_main_corrections':True,
            'all_current_inputs_unchanged':True,'inputs':[{ 'name':k,'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':hashes[k]} for k,p in inputs.items()],
            'source_review_type':'Supplied annotations are model full-source review, not independent human coding. This audit independently checks their arithmetic and recorded source spans.',
            'coupled_zero_caveat':'Zero in 26 co-mentions depends on shared binary completion of the same predicate/operator for N0149 and N0798 within each construct. Independent U assignments still yield the reported nonzero outer ranges. Neither equality is a technology-demand effect.',
            'coverage_caveat':'TensorFlow is a post hoc literal-name extension within the same 105 model advertisements; no new firm/sample representativeness or general framework equivalence is established.'}
    (OUT/'framework_independent_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    with (OUT/'framework_source_checks_independent.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(source_matches[0]));w.writeheader();w.writerows(source_matches)
    print(json.dumps({k:report[k] for k in ['status','independent_arithmetic_and_source_checks','model_task_ads','both_framework_mentions','source_fields_scanned','TensorFlow_literal_occurrences_across_fields','preferred_scope_excluded_advertisements','inherited_and_harmonized_PyTorch_equal_after_seven_main_corrections']},indent=2))

if __name__=='__main__':main()
