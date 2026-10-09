"""Bounded source audit of cue-free framework lists; no primary-state edits.

This records a model review of all 23 positive PyTorch target statements and
all 43 model-task example increments, with a broader parenthesis retrieval
check over every recorded PyTorch GENERAL/REQUIRED parent. The regex retrieves
parentheses only; the listed structural decisions are explicit model judgments.
"""
from pathlib import Path
from collections import defaultdict,Counter
import csv,json,hashlib,re,unicodedata
from _phase4_review_frame import states as phase4_states, example_increments

ROOT=Path(__file__).resolve().parents[2]
SNAP=ROOT/'source_snapshot'
OUT=ROOT/'analysis/empirical'

DECISIONS={
 'N0798':('BARE_MULTI_FRAMEWORK_LIST','INCLUDE_COUPLED_LIST_READING',
           'A framework category is followed by a comma-separated three-name parenthesis. No such as, e.g., or, one-of, 等 or 如 operator governs the list. No other PyTorch occurrence appears in the complete captured body. Current P is one defensible reading, but differs from N1044 and the inherited TensorFlow EXAMPLE reading of this same list.'),
 'N1044':('BARE_MULTI_FRAMEWORK_LIST','INCLUDE_COUPLED_LIST_READING',
           'A framework category is followed by a comma-separated two-name parenthesis. No explicit example or alternative operator governs the list. The parent is inside We’re Looking For and before Nice to Have. No other PyTorch occurrence appears in the complete captured body. Current EXAMPLE is a defensible reading but not supported by an explicit example cue.'),
 'E0206':('SINGLE_TARGET_WITH_EXPLICIT_EMPHASIS','EXCLUDE_FROM_MULTI_FRAMEWORK_LIST_READING',
           'PyTorch 为主 explicitly emphasizes PyTorch as the main framework. The parenthesis contains one named target plus an emphasis modifier, not a cue-free list of peer frameworks. The full source places this under 硬性要求.'),
 'E0195':('SINGLE_STACK_APPOSITION','EXCLUDE_FROM_MULTI_FRAMEWORK_LIST_READING',
           'Python(PyTorch) is a single framework annotation to the named programming language in a 熟练使用 predicate. It does not list alternative or illustrative members of a framework category. Any separate ambiguity in this stack apposition requires its own stated rule, not inclusion in the multi-framework-list switch.'),
}

def read(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write(name,rows):
    with (OUT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def norm(s):return ' '.join(unicodedata.normalize('NFKC',s).casefold().split())

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    (ROOT/'audit').mkdir(parents=True,exist_ok=True)
    (OUT/'bare_parenthetical_correction_payload.json').write_bytes((ROOT/'work/empirical/bare_parenthetical_correction_payload.json').read_bytes())
    paths={'frozen_states':SNAP/'analysis/ad_technology_current.csv',
           'phase4_ledger':ROOT/'data/v4_source_corrections_phase4.json',
           'v3_ledger':SNAP/'data/analysis_revision_ledger.json',
           'evidence':SNAP/'source_v2/data/inputs/context_evidence.csv',
           'sources':SNAP/'source_v2/data/inputs/records.json'}
    hashes={k:sha(v) for k,v in paths.items()}
    states=phase4_states();evidence=read(paths['evidence'])
    sources={r['identity_key']:r for r in json.loads(paths['sources'].read_text(encoding='utf-8'))}
    state={(r['identity_key'],r['label_code']):r for r in states}
    positives=[r for r in states if r['label_code']=='SK_PYTORCH' and r['Q']=='P']
    increments=example_increments(states,evidence)
    assert len(positives)==23 and len(increments)==43
    selected={(r['identity_key'],r['label_code']):'PYTORCH_Q_P' for r in positives}
    assert not set(selected)&{(r['identity_key'],r['label_code']) for r in increments}
    selected.update({(r['identity_key'],r['label_code']):'EXAMPLE_INCREMENT' for r in increments})
    assert len(selected)==66
    parent_by=defaultdict(list)
    for e in evidence:parent_by[e['identity_key'],e['code']].append(e)
    scope=[];occ=[];parentheses=[];details=[];checks=0
    for k,origin in selected.items():
        r=state[k];source=sources[k[0]]
        ev=[e for e in parent_by[k] if e['metric'] in ['GENERAL','REQUIRED']]
        for e in ev:
            raw=source['fields'][e['field']]
            assert raw[int(e['parent_start']):int(e['parent_end'])]==e['parent_text'];checks+=1
            assert hashlib.sha256(raw.encode()).hexdigest()==e['source_field_sha256'];checks+=1
        scope.append({'identity_key':k[0],'reading_id':r['reading_id'],'label_code':k[1],'review_frame':origin,
                      'company_id':r['company_id'],'Q':r['Q'],
                      'qualification_parent_texts':json.dumps([e['parent_text'] for e in ev],ensure_ascii=False),
                      'qualification_branches':json.dumps([e['branch'] for e in ev]),
                      'reviewed_structure':DECISIONS[r['reading_id']][0] if r['reading_id'] in DECISIONS else 'NO_CUE_FREE_MULTI_FRAMEWORK_PARENTHETICAL_LIST_FOUND',
                      'model_source_review':True,'independent_human_validation':False})
    for e in evidence:
        if e['code']!='SK_PYTORCH' or e['metric'] not in ['GENERAL','REQUIRED']:continue
        # Retrieve parentheses that contain the selected target. This does not
        # decide whether their contents are illustrative or unconditional.
        match=re.search(r'[（(][^）)]*pytorch[^）)]*[）)]',e['parent_text'],re.I)
        if not match:continue
        source=sources[e['identity_key']];raw=source['fields'][e['field']]
        assert raw[int(e['parent_start']):int(e['parent_end'])]==e['parent_text'];checks+=1
        assert hashlib.sha256(raw.encode()).hexdigest()==e['source_field_sha256'];checks+=1
        rid=e['reading_id'];decision=DECISIONS.get(rid,('EXPLICIT_LOCAL_CUE','EXCLUDE_EXPLICIT_OPERATOR','Explicit e.g., 如 or 等 occurs in the local target parenthesis; it is not a cue-free list.'))
        parentheses.append({k:e[k] for k in ['identity_key','reading_id','code','evidence_id','field','metric','branch','parent_start','parent_end','parent_text','source_field_sha256','nearest_heading_text']} |
                            {'current_Q':state[e['identity_key'],e['code']]['Q'],'target_parenthesis':match.group(),
                             'reviewed_structure':decision[0],'coupled_reading_decision':decision[1],
                             'model_review_reason':decision[2],'independent_human_validation':False})
        if rid in DECISIONS:
            for field,body in source['fields'].items():
                for m in re.finditer(r'[^\n]*pytorch[^\n]*',body,re.I):
                    assert norm(m.group()) in norm(source['fields']['full_description']);checks+=1
                    occ.append({'reading_id':rid,'identity_key':e['identity_key'],'target':'SK_PYTORCH','field':field,
                                'start':m.start(),'end':m.end(),'source_text':m.group(),
                                'field_sha256':hashlib.sha256(body.encode()).hexdigest(),
                                'included_in_reviewed_full_body':True})
            details.append(f"## {rid}: {decision[0]}\n\nIdentity: `{e['identity_key']}`\n\n"
                           f"Title: {source['title']}. Current PyTorch Q={state[e['identity_key'],e['code']]['Q']}; "
                           f"historical {e['metric']}/{e['branch']}.\n\n"
                           f"Exact `{e['field']}` [{e['parent_start']}, {e['parent_end']}):\n\n> {e['parent_text']}\n\n"
                           f"SHA-256 of field: `{e['source_field_sha256']}`.\n\n{decision[2]}\n")
    assert {r['reading_id'] for r in parentheses if r['reviewed_structure']=='BARE_MULTI_FRAMEWORK_LIST'}=={'N0798','N1044'}
    assert len(parentheses)==12
    write('bare_parenthetical_review_frame.csv',scope)
    write('bare_parenthetical_target_parentheses.csv',parentheses)
    write('bare_parenthetical_all_field_occurrences.csv',occ)
    assert hashes=={k:sha(v) for k,v in paths.items()}
    checks_report={'status':'BOUNDED_SOURCE_REVIEW_COMPLETE','positive_PyTorch_pairs_reviewed':len(positives),
      'example_increment_pairs_reviewed':len(increments),'combined_distinct_target_pairs':len(scope),
      'all_qualification_PyTorch_parentheses_retrieved':len(parentheses),'exact_source_checks':checks,
      'structure_counts':dict(Counter(r['reviewed_structure'] for r in parentheses)),
      'coupled_multi_framework_list_reading_ids':['N0798','N1044'],
      'excluded_QP_parenthetical_cases':['E0206','E0195'],
      'all_input_hashes_unchanged':True,'inputs':[{ 'name':k,'path':str(v.relative_to(ROOT)).replace('\\','/'),'sha256':hashes[k]} for k,v in paths.items()],
      'primary_state_changes':0,'independent_human_validation':False,
      'limits':'Full captured sources were read for the four cue-free parenthetical cases; all target parent statements were read for the bounded 23 positive plus 43 increment frame. Not complete semantic revalidation of every target or source omission.'}
    (OUT/'bare_parenthetical_checks.json').write_text(json.dumps(checks_report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    intro='''# Cue-free parenthetical framework lists: bounded source review

This review preserves the phase-four discovery frame (23 PyTorch positives and 43 example increments), reconstructed from frozen source states, the three v3 clarifications and `data/v4_source_corrections_phase4.json`. It does not depend on previously generated analysis files. The coordinator subsequently adopted both disputed lists as U in the current v4 layer. “Current” in the row-level discovery ledger means current at that review phase, not the later harmonized state.

The review confirms a source-level inconsistency in the inherited narrow-Q states. N0798 names “machine learning frameworks (PyTorch, JAX, TensorFlow)” and records PyTorch as unconditional/P. N1044 names “modern ML frameworks (PyTorch, JAX)” and records PyTorch as EXAMPLE/Z. Neither local list has an explicit example or alternative operator. The first advertisement also has a historical TensorFlow EXAMPLE branch, making a framework contrast based solely on these inherited codes particularly vulnerable to a coding artifact.

All 23 positive PyTorch target statements and all 43 model-task example increments were read. The 43 increments include 42 PyTorch pairs and one Python pair. An additional retrieval check over every recorded GENERAL/REQUIRED PyTorch parent found 12 target-containing parentheses: the two cue-free peer-framework lists, two structurally different positive parentheses, and eight with explicit e.g., 如 or 等 cues. The four cue-free cases' complete captured descriptions were read, and every PyTorch-bearing line in every captured field was matched to that body after normalization. CSV files preserve source spans, field hashes, complete parents and original branches. This is model source review, not independent human coding.

For a narrowly defined coupled sensitivity, treat N0798 and N1044 alike: a uniformly example reading makes both PyTorch Q=Z; a uniformly unconditional reading makes both Q=P. The inherited mixed P/Z result remains a historical baseline, not a third harmonized semantic rule. A primary harmonized uncertainty representation can make both U, then display the coupled endpoints separately. Independent U assignments produce a conservative outer range containing mixed interpretations; they should not be described as the exact set from the two linked list readings.

E0206 and E0195 should not silently enter that switch. The former says PyTorch 为主 and explicitly emphasizes the target under hard requirements. The latter is Python(PyTorch), a single stack annotation to a named language, not a category followed by peer framework members. A broader uncertainty rule might question that apposition, but it would be a different rule needing its own rationale and coverage. Similarly, explicit e.g./如/等 cases remain governed by their local cues.

No primary data are edited by this module. The same rule should apply to each named framework inside a given list; it should not declare PyTorch unconditional and TensorFlow illustrative within N0798 solely because their inherited branches differ. This bounded audit identifies wording structure and consistent alternatives, not the employer's intended acceptance set or real screening requirement.

'''
    (ROOT/'audit/bare_parenthetical_source_review.md').write_text(intro+'\n'.join(details),encoding='utf-8')
    print(json.dumps(checks_report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
