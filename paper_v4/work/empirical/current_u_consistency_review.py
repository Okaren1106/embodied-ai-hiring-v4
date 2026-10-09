"""Document a complete model source review of the 46 v3 current unresolved Q pairs.

All 44 distinct full captured descriptions were read. All target-bearing lines
in the remaining source fields are checked against normalized full-description
content. This module proposes five modifier-scope corrections but never changes
the analytical input. The root task owns any v4 adjudication and overlay.
"""
from pathlib import Path
from collections import defaultdict,Counter
import csv,json,re,unicodedata,hashlib

ROOT=Path(__file__).resolve().parents[2]
V3=ROOT/'source_snapshot'
V4=ROOT
OUT=V4/'analysis/empirical'

def read(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def norm(t):return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',t)).strip().casefold()

PROPOSE={
    ('N0508','SK_PYTORCH'):('EXAMPLE','The complete captured body is identical to N0486/A099, including the same qualification clause. The already-adjudicated 等 framework example must govern the unresolved slash inside that example. No other unconditional PyTorch qualification occurs.'),
    ('N0634','SK_CPP'):('CHOICE','The full local requirement is C/C++或Python. The explicit outer 或 admits Python instead of the C/C++ expression, so uncertainty within the slash cannot establish an unconditional C++ item. No separate unconditional C++ occurrence appears.'),
    ('E0071','SK_CPP'):('EXAMPLE','The qualification clause is C/C++、MATLAB、Python等编程语言. Under the frozen 等-as-example rule, the outer language-example list governs C++ regardless of the inner C/C++ slash. No separate unconditional C++ qualification appears.'),
    ('E0549','SK_CPP'):('CHOICE','The complete language list ends C/C++, Rust, Golang, Python or similar. The explicit list-level alternative permits another language; treating the embedded C/C++ slash as unresolved does not erase the governing alternative. No other C++ qualification appears.'),
    ('E0560','SK_CPP'):('CHOICE','The complete language list ends C/C++, Rust, Golang, Python or similar, identically to E0549. The outer alternative governs the embedded slash. No other C++ qualification appears.'),
}
PATTERNS={'SK_CPP':r'C\+\+','SK_PYTHON':r'Python','SK_PYTORCH':r'PyTorch','SK_LINUX':r'Linux'}

def keep_reason(r):
    rid=r['reading_id'];label=r['label_code']
    if rid in {'N0573','E0043'}:
        return 'Bare Python / PyTorch wording can denote a joint implementation stack or an alternative/list relation. It contains no explicit governing example/choice operator. Retain U rather than resolve it from general technical knowledge; both target states should be considered jointly in any later reading scenario.'
    if rid=='N0633':return 'Qt/C++ can denote a technical stack, but the slash is unexpanded and no explicit inclusive operator or separate C++ qualification resolves it. Retain the existing primary U and its recorded alternative reading.'
    if rid=='N0095':return 'Linux/Unix is an unexpanded slash expression. The separate unconditional C++ and C clause does not resolve the operating-system relation. Retain U.'
    if rid in {'N0509','N0158','N0035','N0315','N0337','E0284','E0275','E0217','E0175','E0169','E0157'}:
        return 'The target appears in an unexpanded programming-language slash. Example or choice markers in a neighboring framework clause or later proficiency phrase have their own predicate/scope and must not be transferred onto this target. No separate unconditional target qualification was found. Retain U.'
    if rid=='E0017':return 'Several C/C++ occurrences exist in duties and qualifications, including C/C++/系统软件/高性能计算 and 精通C/C++. None resolves the internal language slash; duty scope does not supply an unconditional qualification. Retain U.'
    if rid=='E0008':return 'The target C++ remains inside C/C++; the additional requirement explicitly names C语言, not C++. Do not substitute the distinct C language for the selected C++ target. Retain U.'
    if label=='SK_PYTORCH':return 'The framework slash has no explicit governing example or alternative operator in its own clause. Retain U; an optional alternative interpretation is not a compelled correction.'
    return 'The target remains in an unexpanded slash expression within qualification scope. No governing explicit choice/example or separate unconditional target occurrence resolves the relation in the captured fields. Retain U.'

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    (V4/'audit').mkdir(parents=True,exist_ok=True)
    input_state=V3/'analysis/ad_technology_current.csv';input_source=V3/'source_v2/data/inputs/records.json'
    allrows=read(input_state);unknown=[r for r in allrows if r['Q']=='U']
    assert len(unknown)==46 and len({r['identity_key'] for r in unknown})==44
    sources=json.loads(input_source.read_text(encoding='utf-8'));sources={r['identity_key']:r for r in sources}
    evidence=read(V3/'source_v2/data/inputs/context_evidence.csv');by=defaultdict(list)
    for e in evidence:by[e['identity_key'],e['code']].append(e)
    rows=[];occurrences=[];sections=[];proposed=[]
    for number,r in enumerate(unknown,1):
        rid=r['reading_id'];label=r['label_code'];source=sources[r['identity_key']]
        ev=by[r['identity_key'],label]
        assert r['G']=='U' and r['R']=='Z'
        full=source['fields']['full_description'];fullnorm=norm(full)
        hits=[]
        for field,body in source['fields'].items():
            for m in re.finditer(r'[^\n]*(?:'+PATTERNS[label]+r')[^\n]*',body,re.I):
                assert norm(m.group()) in fullnorm,(rid,field,m.group())
                hit={'review_id':f'UREV_{number:03d}','identity_key':r['identity_key'],'reading_id':rid,
                     'label_code':label,'field':field,'start':m.start(),'end':m.end(),
                     'full_target_line':m.group(),'field_sha256':hashlib.sha256(body.encode()).hexdigest(),
                     'represented_in_reviewed_full_description':1}
                occurrences.append(hit);hits.append(hit)
        assert hits
        proposed_rule,reason=PROPOSE.get((rid,label),('',keep_reason(r)))
        action='PROPOSE_U_TO_Z' if proposed_rule else 'RETAIN_U'
        row={'review_id':f'UREV_{number:03d}',**{k:r[k] for k in ['identity_key','reading_id','company_id','task','label_code','M','G','R','Q']},
             'review_action':action,'proposed_Q':'Z' if proposed_rule else 'U',
             'governing_modifier_if_corrected':proposed_rule,'reason':reason,
             'full_description_sha256':hashlib.sha256(full.encode()).hexdigest(),
             'full_description_characters':len(full),'all_source_fields_target_occurrences':len(hits),
             'separate_unconditional_target_qualification_found':0,
             'evidence_ids':json.dumps([e['evidence_id'] for e in ev]),
             'parent_texts':json.dumps([e['parent_text'] for e in ev],ensure_ascii=False),
             'model_full_captured_source_review':True,'independent_human_validation':False,
             'accepted_data_changed':False,'source_url':source['source_url']}
        rows.append(row)
        if proposed_rule:
            proposed.append({**row,'G_after_if_adopted':'Z','R_after_if_adopted':'Z','H_after_if_adopted':1,
                             'add_to_example_construct':int(proposed_rule=='EXAMPLE'),
                             'add_to_choice_example_construct':1})
        excerpts=[]
        for e in ev:
            body=source['fields'][e['field']]
            start,end=int(e['parent_start']),int(e['parent_end'])
            assert body[start:end]==e['parent_text']
            excerpts.append(f"`{e['field']}` [{start}, {end}), recorded {e['metric']}/{e['branch']}:\n\n> {e['parent_text']}")
        sections.append(f"## {row['review_id']} — {rid} — {label}\n\n"
                        f"Identity: `{r['identity_key']}`\n\n"
                        f"Title: {source['title']}. Existing G/R/Q: U/Z/U. Action: **{action}**.\n\n"
                        +'\n\n'.join(excerpts)+f"\n\nReview: {reason}\n\n"
                        f"Full captured body: {len(full)} characters; SHA-256 `{row['full_description_sha256']}`. All target-bearing lines in duties/requirements/full_description are represented in that body after NFKC/case/whitespace normalization. See the occurrence CSV for every raw-field span.\n")
    assert {(r['reading_id'],r['label_code']) for r in proposed}==set(PROPOSE)
    # Strongest propagation example: all captured body fields, not merely a
    # selected sentence, match the previously adjudicated advertisement.
    n0508=next(s for s in sources.values() if s['reading_id']=='N0508')
    n0486=next(s for s in sources.values() if s['reading_id']=='N0486')
    equal_fields={field:n0508['fields'][field]==n0486['fields'][field] for field in n0508['fields']}
    assert all(equal_fields.values())
    for filename,values in [('current_u_consistency_review_ledger.csv',rows),('current_u_all_field_occurrences.csv',occurrences),('current_u_proposed_corrections.csv',proposed)]:
        with (OUT/filename).open('w',encoding='utf-8',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(values[0]));w.writeheader();w.writerows(values)
    analogy_targets={('N0486','SK_PYTORCH'),('N0489','SK_PYTHON'),('N0473','SK_CPP'),
                     ('N0199','SK_PYTHON'),('N0876','SK_PYTORCH'),('N0927','SK_CPP'),
                     ('E0599','SK_CPP'),('N0011','SK_CPP')}
    indexed={(r['identity_key'],r['label_code']):r for r in allrows}
    analogies=[]
    for e in evidence:
        if (e['reading_id'],e['code']) not in analogy_targets or e['metric'] not in {'GENERAL','REQUIRED'}:continue
        source=sources[e['identity_key']];body=source['fields'][e['field']]
        assert body[int(e['parent_start']):int(e['parent_end'])]==e['parent_text']
        prior=indexed[e['identity_key'],e['code']]
        analogies.append({'reading_id':e['reading_id'],'identity_key':e['identity_key'],'target':e['code'],
                          'metric':e['metric'],'legacy_branch':e['branch'],'current_Q':prior['Q'],
                          'field':e['field'],'parent_start':e['parent_start'],'parent_end':e['parent_end'],
                          'parent_text':e['parent_text'],'source_field_sha256':e['source_field_sha256'],
                          'use':'Existing resolved analogue or counterexample; not a newly recoded item.'})
    with (OUT/'current_u_rule_analogues.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(analogies[0]));w.writeheader();w.writerows(analogies)
    corrected_keys={(r['identity_key'],r['label_code']) for r in proposed}
    hypothetical=Counter('Z' if (r['identity_key'],r['label_code']) in corrected_keys else r['Q'] for r in allrows)
    report={'status':'FROZEN_V3_U_REVIEW_COMPLETE','current_U_pairs_reviewed':46,'distinct_ads_full_captured_body_read':44,
            'subsequent_adoption':'All five proposals are adopted separately in data/v4_source_corrections.json; verify_v4_overlay_independent.py checks their propagation. This module preserves the original review frame.',
            'target_occurrences_in_all_fields_verified':len(occurrences),'retain_U_pairs':41,
            'proposed_U_to_Z_pairs':5,'proposed_by_target':dict(Counter(r['label_code'] for r in proposed)),
            'proposed_by_modifier':dict(Counter(r['governing_modifier_if_corrected'] for r in proposed)),
            'N0508_N0486_all_captured_body_fields_identical':equal_fields,
            'original_input_sha256':{'current_states':hashlib.sha256(input_state.read_bytes()).hexdigest(),'source_records':hashlib.sha256(input_source.read_bytes()).hexdigest()},
            'proposed_identity_keys':[{k:r[k] for k in ['review_id','identity_key','reading_id','label_code','governing_modifier_if_corrected']} for r in proposed],
            'hypothetical_if_all_adopted':{'Q_'+k:hypothetical[k] for k in ['P','Z','U']},
            'existing_resolved_analogue_occurrences':len(analogies),
            'scope_limit':'Complete review of current unresolved pairs for explicit modifier and duplicate-adjudication consistency; not revalidation of all resolved states.',
            'review_type':'Model source review after an inconsistency was discovered; not independent human coding.'}
    (OUT/'current_u_consistency_review_checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    intro="""# Complete current-U modifier-scope consistency review

All 46 v3-current Q=U pairs from 44 advertisements were reviewed using the complete captured descriptions. Every target-bearing line in every other captured field was checked against the reviewed description after normalization. This is a post hoc model review, not independent human validation. This module preserves the frozen review frame and does not edit accepted states. All five proposals below were subsequently adopted in `data/v4_source_corrections.json`; their exact propagation is checked separately by `verify_v4_overlay_independent.py`.

The review proposes five U→Z corrections: N0508/PyTorch and E0071/C++ under the existing EXAMPLE rule; N0634/C++, E0549/C++ and E0560/C++ under explicit CHOICE scope. The remaining 41 original pairs retain U. Adopting these five yielded the phase-four total of 170 P, 285 Z and 41 U in the fixed 496-pair frame. A subsequent bounded parenthetical review moved two formerly resolved pairs to U, producing the current seven-correction total of 169 P, 284 Z and 43 U. All mention states, tasks and advertisements remain fixed. This review ledger deliberately retains each original U and the proposal that motivated its correction; the later review is documented separately in `bare_parenthetical_source_review.md`.

The decisive duplicate is N0508 against N0486/A099: every captured body field is byte-for-byte identical, while titles differ. Their shared text says ‘熟练掌握Python/C++中的至少一种编程语言，熟悉PyTorch/TensorFlow等深度学习框架’. N0486 received the v3 explicit-example clarification, but N0508 retained U. No additional unconditional PyTorch statement appears in either source. Applying the same modifier rule requires propagation in the new analysis layer, with the original v3 archive preserved.

Explicit outer choices or examples govern nested unresolved slash expressions. For N0634, Python can satisfy the ‘C/C++或Python’ alternative. For E0071, the entire ‘C/C++、MATLAB、Python等编程语言’ expression is an illustrative language list under the current rule. The two Figure advertisements use an identical list ending ‘Python or similar’; the alternative governs the list, not merely the spelling of the C/C++ item. These proposals do not infer employer behavior; they apply the existing narrow-Q construct consistently.

Scope is local. The review deliberately does not move an example marker from a neighboring PyTorch clause onto an earlier Python/C++ predicate. Nor does it turn C into C++, infer a mandatory framework from a qualification heading alone, or expand bare slash constructions using technical knowledge. Bare Python/PyTorch and Qt/C++ stacks remain unresolved under the primary rule and may enter separately identified readings.

The prior resolved analogues are preserved with exact parent spans in `current_u_rule_analogues.csv`: N0489 treats a language slash inside an explicit at-least-one operator as CHOICE/Z; N0473 treats C++ 或 Python as CHOICE/Z; N0199 treats a language list ending C/C++等 as EXAMPLE/Z for its Python target; E0599 and N0927 treat comma-separated language lists with final or as CHOICE/Z; N0876 treats PyTorch (or similar frameworks) as CHOICE/Z. N0011 is a counterexample: C/C++ appears together with a separate ‘了解现代C++常用特性’ qualification, so Q=P is supported despite the slash. These analogues establish scope priority under existing practice, not a universal rule that every slash is negative. N0486's old evidence branch is still UNRESOLVED; its current Z comes from the explicit v3 A099 adjudication.

The five proposed changes should be propagated into any Q thresholds, company eligibility, paired bounds, expanded-example/choice measures and semantic scenarios. The three choice cases enter the choice-inclusive construct; the two example cases enter the example-inclusive construct. H remains one for all five. Do not selectively implement only the duplicate or only changes that leave a preferred result intact.

"""
    (V4/'audit/current_u_consistency_review.md').write_text(intro+'\n'.join(sections),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
