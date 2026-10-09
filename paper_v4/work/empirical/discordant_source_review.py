"""Materialize exact source excerpts for a model review of 24 discordant ads.

The qualitative notes below were written after reading the full captured
descriptions. They explain existing states and flag construct ambiguity; they
do not change accepted Q codes or claim independent human verification.
"""
from pathlib import Path
from collections import Counter
import csv, json, re, hashlib
from _phase4_review_frame import states as phase4_states

ROOT=Path(__file__).resolve().parents[2]
V4=ROOT
V3=ROOT/'source_snapshot'

def read(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

DENG={'N0440','N0492','N0490','N0460','N0469','N0071','N0001','N0102','N0097'}
EXAMPLE={'E0326','E0414','E0384','E0415','E0487','E0495','E0491','E0492','E0489'}
CHOICE={'N0646','N0876'}
BOTH={'N0412','N0814'}
REVERSE={'N0562','N0798'}
HEADINGS={'N0440':'任职要求','N0412':'任职要求 / 基本要求',
          'N0492':'【任职要求】 / 4. 编程与工程','N0490':'【任职要求】 / 4. 编程与工程',
          'N0460':'任职要求','N0469':'任职要求','N0646':'任职资格',
          'N0071':'职位要求','N0001':'职位要求','N0102':'职位要求：','N0097':'职位要求：',
          'N0562':'任职要求','E0326':'About You','E0414':'SKILLS AND REQUIREMENTS',
          'E0384':'SKILLS AND REQUIREMENTS','E0415':'SKILLS AND REQUIREMENTS',
          'N0876':'What We’re Looking For','N0798':'What You Have','N0814':'What You Have',
          'E0487':'Requirements','E0495':'Requirements','E0491':'Requirements',
          'E0492':'Requirements','E0489':'Requirements'}

def note(rid):
    if rid in DENG:
        return ('deng_only_nonexhaustive_list',
                'Both target clauses are qualification-scoped. The PyTorch clause contains 等 but no explicit one-of/or/such-as marker. Under the frozen rule 等 gives EXAMPLE; an inclusive non-exhaustive reading is linguistically plausible. This is evidence of the operational syntax distinction, not proof that PyTorch knowledge is not sought.')
    if rid in EXAMPLE:
        return ('explicit_example_such_as_or_eg',
                'Both targets occur within qualification scope. PyTorch is introduced by such as or e.g.; Python is named without that local operator. The framework-level qualification remains explicit even though the selected framework is illustrative under Q.')
    if rid in CHOICE:
        return ('explicit_choice_one_of_or_similar',
                'Python is directly named, while the full local PyTorch clause explicitly admits an alternative (至少一种 or or similar frameworks). This supports the narrower target-specific contrast, while still recording a framework qualification.')
    if rid in BOTH:
        return ('explicit_choice_and_example',
                'The PyTorch clause has an explicit alternative and an illustrative/open list. The Python clause is outside that local operator. Both are within qualification scope.')
    if rid=='N0562':
        return ('reverse_explicit_choice',
                'PyTorch is stated directly in requirement item 4; Python is in C++ 或 Python in item 6. This is a source-supported counterexample to any universal language-versus-framework pattern.')
    return ('reverse_explicit_choice',
            'Python occurs as Python and/or C++; PyTorch is in a bare parenthetical framework list with no explicit example/choice marker. The inherited code treated this as unconditional, inconsistently with N1044. The later bounded source review now represents both framework lists as U; N0798 no longer counts as a current resolved reverse discordance. See bare_parenthetical_source_review.md.')

def main():
    (V4/'analysis/empirical').mkdir(parents=True,exist_ok=True)
    (V4/'audit').mkdir(parents=True,exist_ok=True)
    path=V3/'source_v2/data/inputs/records.json'
    sources=json.loads(path.read_text(encoding='utf-8'))
    sources={r['identity_key']:r for r in sources}
    paired=read(V4/'analysis/paired/paired_advertisements.csv')
    current={r['identity_key']:r for r in paired}
    prior={(r['identity_key'],r['label_code']):r for r in phase4_states()}
    paired=[dict(r,Q_a=prior[r['identity_key'],r['target_a']]['Q'],Q_b=prior[r['identity_key'],r['target_b']]['Q']) for r in paired]
    selected=[r for r in paired if r['task']=='ROBOT_MODEL' and r['both_mentioned']=='1'
              and (r['Q_a'],r['Q_b']) in [('P','Z'),('Z','P')]]
    assert len(selected)==24
    assert {r['reading_id'] for r in selected}==DENG|EXAMPLE|CHOICE|BOTH|REVERSE
    evidence=[]
    sections=[]
    for r in selected:
        rid=r['reading_id'];src=sources[r['identity_key']]
        text=src['fields']['full_description']
        marker,judgement=note(rid)
        excerpts=[]
        # All lines containing either target are retained, with their complete
        # captured local modifiers and exact zero-based Python character spans.
        for match in re.finditer(r'[^\n]*(?:Python|PyTorch)[^\n]*',text,re.I):
            quote=match.group()
            assert text[match.start():match.end()]==quote
            excerpts.append((quote,match.start(),match.end()))
            evidence.append({'identity_key':r['identity_key'],'reading_id':rid,'company_id':r['company_id'],
                             'source_url':src['source_url'],'text_version_hash':src['text_version_hash'],
                             'Q_Python_phase4':r['Q_a'],'Q_PyTorch_phase4':r['Q_b'],
                             'Q_Python_current':current[r['identity_key']]['Q_a'],'Q_PyTorch_current':current[r['identity_key']]['Q_b'],'field':'full_description',
                             'field_sha256':hashlib.sha256(text.encode()).hexdigest(),
                             'start':match.start(),'end':match.end(),'quote':quote,
                             'qualification_heading':HEADINGS[rid],'reviewed_marker_class':marker,
                             'model_review_note':judgement,'human_verification':False,
                             'classification_changed':False})
        assert excerpts
        all_lines=[m.group().strip() for m in re.finditer(r'[^\n]*(?:Python|PyTorch)[^\n]*',text,re.I)]
        for field,value in src['fields'].items():
            for match in re.finditer(r'[^\n]*(?:Python|PyTorch)[^\n]*',value,re.I):
                assert match.group().strip() in all_lines,(rid,field,match.group())
        extra=''
        if rid=='N0490':extra=' The captured description ends mid-phrase in a later bonus item; the reviewed target clause is complete. Completeness here refers to captured fields, not recovery of the entire original web page.'
        if rid in {'E0487','E0495','E0491','E0492','E0489'}:
            extra+=' The same Python/framework sentence occurs in all five Figure advertisements although their complete qualification blocks differ.'
        if rid in {'E0414','E0384','E0415'}:
            extra+=' Apptronik repeats this two-clause construction across three advertisements with 3+ or 5+ years; full-block equality does not capture all of that shared wording.'
        if rid=='N0097':extra+=' The PyTorch wording is 熟练掌握, a strong proficiency expression; interpreting Z as absence of a PyTorch qualification would be particularly misleading.'
        if rid in {'N0460','N0469'}:extra+=' The captured full descriptions are identical despite different titles; both advertise 2027 graduates.'
        sections.append(f"## {rid} — {src['company']} — {src['title']}\n\n"
                        f"Phase-four Q states: Python **{r['Q_a']}**, PyTorch **{r['Q_b']}**. Current v4 states: Python **{current[r['identity_key']]['Q_a']}**, PyTorch **{current[r['identity_key']]['Q_b']}**. Marker class: `{marker}`.\n\n"
                        f"Identity: `{r['identity_key']}`\n\nSource: [{rid} source]({src['source_url']}); captured text version `{src['text_version_hash']}`. "
                        f"Field: `full_description`; heading: **{HEADINGS[rid]}**.\n\n"
                        +'\n\n'.join(f"Exact characters [{start}, {end}):\n\n> {quote}" for quote,start,end in excerpts)
                        +f"\n\nReview: {judgement}{extra}\n")
    out=V4/'analysis/empirical'
    with (out/'discordant_source_review_ledger.csv').open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(evidence[0]));w.writeheader();w.writerows(evidence)
    counts=Counter(note(r['reading_id'])[0] for r in selected)
    facts={'advertisements_reviewed':24,'forward_discordant':22,'reverse_discordant':2,
           'selection_frame':'Phase-four source-review discovery frame, preserved for provenance',
           'current_resolved_forward_discordant':sum(r['task']=='ROBOT_MODEL' and r['both_mentioned']=='1' and (r['Q_a'],r['Q_b'])==('P','Z') for r in current.values()),
           'current_resolved_reverse_discordant':sum(r['task']=='ROBOT_MODEL' and r['both_mentioned']=='1' and (r['Q_a'],r['Q_b'])==('Z','P') for r in current.values()),
           'marker_counts':dict(counts),'exact_excerpt_spans':len(evidence),
           'all_distinct_field_target_lines_covered':True,'source_file_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
           'mode':'Model source review after outcome selection; not independent human coding.',
           'prior_states_changed':False}
    (out/'discordant_source_review_checks.json').write_text(json.dumps(facts,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    intro="""# Source review of the 24 robot-model discordant advertisements

This preserves the phase-four discovery frame of 24 resolved discordant advertisements. The later parenthetical consistency review changes N0798/PyTorch to U, so the current v4 primary data have 23 resolved discordances: 22 forward and one reverse. Both phase-four and current Q states are shown in the ledger. This source-review module itself edits no classification. Full captured descriptions were read, all target-bearing lines in the other distinct source fields were checked, and quotations were verified against character spans and hashes. This is not blind review, independent human coding, or validation of all 496 pairs.

**Finding:** the target sentences document visible operators but do not provide independent evidence that PyTorch is less often a qualification. In all 24 phase-four selected advertisements, both technologies occur in qualification scope. The contrast is narrower: an individually named target without a local choice/example qualifier versus a name in a choice, example or non-exhaustive framework construction. The later N0798/N1044 review also demonstrates that the inherited operator coding was inconsistent for cue-free parenthetical lists; that issue is now represented as uncertainty.

Among the 22 Python-P/PyTorch-Z advertisements, nine use Chinese 等 without an explicit either/or/one-of/such-as marker, nine use explicit English such as/e.g., two explicitly allow alternatives, and two combine alternatives with an illustrative/open list. Both historical reverse cases place Python in an explicit choice; N0562 names PyTorch directly, while N0798 uses the now-unresolved bare framework list. These four forward marker groups correspond to the legacy 18 EXAMPLE, two CHOICE and two CHOICE_AND_EXAMPLE flags. Nine of the 18 EXAMPLE cases are Chinese 等-only cases, for which an inclusive non-exhaustive interpretation deserves particular attention.

Counting example/choice flags among Q=Z cases is partly definitional: the same operators help determine Q. It documents which source constructions underlie the observed contrast; it is not an independent mechanism test or a validation of the narrow construct as employer demand. The source evidence can support a broader qualification-scope H based on any GENERAL/REQUIRED occurrence, retaining alternatives/examples, alongside the narrower Q. H must be labelled as the name's presence in qualification scope, not as a separately mandatory skill. The 24 cases provide direct source support for this conceptual distinction.

The seven earlier semantic switches do not exhaust this construct sensitivity. Reinterpreting 等 must cover all affected qualification occurrences in the analysis frame, not selectively recode these 24 outcome-selected advertisements. Treat admitting examples as a different measure, not as discovering the true answer. A name can exemplify a framework-level qualification without being individually mandatory; both statements can be true.

Template caveat: all five Figure discordant advertisements use the same target sentence, and three Apptronik advertisements share the same Python/framework structure. Their whole qualification blocks differ, so exact full-block weighting does not remove all shared local phrasing. The two Fourier records have identical captured bodies. These are wording patterns, not independent demonstrations of a labor-demand mechanism.

Exact spans below are zero-based, end-exclusive Python character indices. The CSV ledger additionally records each full-description SHA-256 hash. All quotations are captured-source text; source URLs are provenance, not claims of current webpage availability.

"""
    (V4/'audit/discordant_source_review.md').write_text(intro+'\n'.join(sections),encoding='utf-8')
    print(json.dumps(facts,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
