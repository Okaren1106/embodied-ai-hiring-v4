"""Collect verified v4 empirical facts and the portable module input manifest."""
from pathlib import Path
import json, csv, hashlib

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'analysis/empirical'

def read(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def load(name):return json.loads((OUT/name).read_text(encoding='utf-8'))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    (OUT/'final_empirical_facts_phase4.json').write_bytes((ROOT/'work/empirical/history/final_empirical_facts_phase4.json').read_bytes())
    overlay=load('v4_overlay_independent_verification.json')
    company=load('company_rebuild_checks.json')
    local=load('local_template_checks.json')
    scope=load('qualification_scope_independent_verification.json')
    paired=load('paired_independent_verification.json')
    breakdown=load('paired_breakdown_independent_verification.json')
    sensitivity=load('classification_breakdown_checks.json')
    framework=load('framework_independent_verification.json')
    assert all(x['status']=='PASS' for x in [overlay,company,local,scope,paired,breakdown,framework])
    state_hash=sha(ROOT/'analysis/v4_ad_technology_current.csv')
    assert state_hash==company['source_state_sha256']==sensitivity['inputs']['current']['sha256']
    assert state_hash==overlay['before_after_and_inputs_sha256']['analysis/v4_ad_technology_current.csv']
    facts={'version':'v4 adopted source-correction layer','state_sha256':state_hash,
           'Q_counts':overlay['Q_after'],'reviewed_v3_U_pairs':46,'reviewed_advertisements':44,
           'adopted_U_to_Z':5,'adopted_resolved_to_U':2,'total_adopted_corrections':7,'independent_human_validation':False,
           'previous_phase_facts':'analysis/empirical/final_empirical_facts_phase4.json',
           'current_Q_U_to_example_inclusive_P':scope['U_to_P_transitions'],
           'verification_checks':{'overlay':overlay['independent_checks'],'paired':paired['arithmetic_and_identity_checks'],
              'qualification_scope':scope['independent_arithmetic_and_span_checks'],
              'paired_breakdown':breakdown['arithmetic_feasibility_and_optimality_checks'],
              'v3_company_values_reconstructed':company['v3_saved_comparison_values_reconstructed'],
              'company_sensitivity_endpoints':sensitivity['exact_interval_endpoint_validations'],
              'local_parent_source_spans':local['parent_evidence_occurrences_verified']},
           'framework_control_independent_checks':framework['independent_arithmetic_and_source_checks'],
           'framework_control':{k:framework[k] for k in ['model_task_ads','both_framework_mentions','preferred_scope_excluded_advertisements','verified_harmonized_contrasts','verified_coupled_diagnostics','coupled_zero_caveat']},
           'company_summary':company['primary_summary'],'company_classification_changes':company['classification_changes'],
           'no_new_company_comparison_keys':not company['new_company_comparison_keys'],
           'all_128_company_keys_stable':company['all_128_primary_key_sets_identical'],
           'company_breakdown_summary':sensitivity['summaries'],
           'robot_model_scope_contrasts':scope['verified_robot_model_contrasts'],
           'paired_breakdown_primary_robot_model':breakdown['primary_robot_model'],
           'local_template_coverage':local['coverage'],'local_Q_semantic_envelopes':local['Q_semantic_envelopes'],
           'local_robot_model_constructs':local['robot_model_primary_contrasts'],
           'local_Q_inconsistent_signature_groups':local['unique_scope_groups_with_different_primary_Q'],
           'caveats':['All new analyses are post hoc and conditional on the selected corpus and targets.',
                      'Unknown-state ranges are conservative assignment bounds, not confidence intervals.',
                      'H and example/choice expansions change the construct; they do not estimate a latent true narrow Q.',
                      'Exact local wording weighting diagnoses repetition; it does not control company style or seniority.',
                      'Coding-breakdown counts are hypothetical adversarial distances, not detected or estimated error rates.']}
    (OUT/'final_empirical_facts.json').write_text(json.dumps(facts,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    scripts=['current_u_consistency_review.py','verify_v4_overlay_independent.py','rebuild_company_comparisons.py',
             'classification_breakdown.py','discordant_source_review.py','verify_paired_independent.py',
             'verify_scope_independent.py','verify_paired_breakdown_independent.py','local_template_sensitivity.py',
             'bare_parenthetical_review.py','verify_framework_independent.py','finalize_empirical_facts.py']
    frozen=['analysis/ad_technology_current.csv','analysis/current_firm_pairs.csv','analysis/current_task_summary.csv',
            'source_v2/analysis/diagnostic_comparison.csv','data/sensitivity_policy.json','data/analysis_revision_ledger.json',
            'source_v2/data/inputs/records.json','source_v2/data/inputs/context_evidence.csv']
    generated=['analysis/v4_ad_technology_current.csv','analysis/paired/paired_advertisements.csv',
               'analysis/paired/paired_summary.csv','analysis/paired/leave_one_firm_out.csv',
               'analysis/paired/semantic_reading_summaries.csv','analysis/paired/semantic_envelopes.csv',
               'analysis/paired/qualification_scope_states.csv','analysis/paired/qualification_scope_contrasts.csv',
               'analysis/paired/paired_breakdown_readings.csv',
               'extensions/framework_control/outputs/tensorflow_states_105.csv',
               'extensions/framework_control/outputs/paired_states_105.csv',
               'extensions/framework_control/outputs/source_review_26.csv',
               'extensions/framework_control/outputs/framework_contrasts.csv',
               'extensions/framework_control/outputs/coupled_reading_diagnostic.csv']
    manifest={'scripts':scripts,'script_root':'Path(__file__).resolve().parents[2]',
              'frozen_inputs':[{'relative_to_source_snapshot':f,'bytes':(ROOT/'source_snapshot'/f).stat().st_size,
                               'sha256':sha(ROOT/'source_snapshot'/f)} for f in frozen],
              'fixed_v4_inputs':[{'path':f,'sha256':sha(ROOT/f)} for f in ['data/v4_source_corrections.json','extensions/framework_control/data/source_review_annotations.json']],
              'archived_review_inputs':[{'path':f,'sha256':sha(ROOT/f)} for f in
                 ['data/v4_source_corrections_phase4.json','work/empirical/bare_parenthetical_correction_payload.json','work/empirical/history/final_empirical_facts_phase4.json']],
              'support_modules':['_phase4_review_frame.py'],
              'runtime_dependencies':['Python standard library only'],'generated_input_dependencies':generated,
              'notes':['All scripts require the packaged source_snapshot; no external v3 fallback.',
                       'Root apply_v4_overlay.py precedes consumers of v4_ad_technology_current.csv.',
                       'current_u_consistency_review.py preserves the frozen 46-U review frame and precedes verify_v4_overlay_independent.py.',
                       'rebuild_company_comparisons.py precedes classification_breakdown.py.',
                       'Root paired_analysis.py/qualification_scope.py/paired_breakdown.py must run before their respective verifiers and local_template_sensitivity.py.',
                       'Historical source-review frames are rebuilt from source_snapshot plus data/v4_source_corrections_phase4.json. The bare-parenthetical payload and archived phase4 facts are fixed review-provenance inputs under work/empirical.',
                       'finalize_empirical_facts.py runs last.',
                       'discordant_source_packet.json and current_u_review_packet.json are temporary reading packets, not runtime dependencies; exclude them from release.',
                       'No production analysis module is imported by independent verifiers.']}
    (ROOT/'work/empirical/module_input_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    summary='''# Final empirical verification after the v4 overlay

Seven source corrections were adopted without changing the 496-pair frame: Q = 169 P, 284 Z, 43 U. The complete unresolved-state review covered 46 previously unresolved pairs in 44 advertisements and all 101 target-bearing source-field occurrences, yielding five U-to-Z corrections. The later bounded parenthetical review identified two inconsistently coded cue-free framework lists, one previously P and one Z; both are now U. The earlier five-correction results are archived in final_empirical_facts_phase4.json. This is model source review and arithmetic verification, not independent human coding.

The independent overlay, paired, scope and paired-breakdown checks passed (2,139; 11,083; 3,608; 22,656 checks). The company rebuild reproduced 1,820 frozen-v3 comparison values before constructing the v4 frame; all 128 semantic readings retain the same company identities. Threshold five still gives 32 comparisons across nine companies, with 22 supported retained directions, five supported reversals, three overlapping conditional reversals, one overlapping conditional retention, and one conditional tie. The tie is Deep Robotics–Galbot/PyTorch, previously an overlapping conditional retention. Threshold ten retains three comparisons across two companies. Do not reuse the old 22/5/3/2 four-category summary.

For all 105 robot-model advertisements, Python–PyTorch narrow-Q bounds are +13.33 to +35.24 percentage points; example expansion changes the construct and yields −24.76 to −4.76. In the 66 common-mention advertisements, these ranges are +21.21 to +51.52 and −24.24 to +3.03. H remains 67/79 in all 105 and 60/62 in the common-mention group. Broad qualification scope therefore cannot be described as favoring Python. The two newly unresolved parenthetical lists are P under the example-inclusive measure because both named admissible relations, unconditional and example, satisfy that broader construct; neither is marked as an explicit example cue. Current narrow-Q counts are 42/22 (U17/6) in all advertisements and 37/18 (U15/5) in common mentions.

Exact local target-qualification repetition gives 56 joint groups among the 66 common-mention advertisements at 18 firms. With equal firms, then equal local groups within firm, narrow-Q bounds remain +15.38 to +45.00 across all 128 inherited readings. H is −5.56 points; the primary example expansion is −21.32 to +2.74 and the choice/example expansion is −24.43 to −0.37. For all 105 advertisements, the corresponding Q envelope is +13.02 to +29.43 and example-expanded bounds are −14.07 to −0.68. This checks exact repeated local wording, not company-style control. Parent text scope and target slots are retained; missing/unlocated scope uses unique advertisement fallbacks. All 327 parent spans matched their captured source. The N0508/N0486 inconsistency that this diagnostic uncovered has been resolved by the overlay; zero identical local groups now have conflicting primary Q pairs.

For the pooled model narrow-Q direction, 14 adversarial resolved-label edits or seven edited advertisements suffice to remove strict support; the ad-cost calculation allows both target labels to change within an edited advertisement. Under equal firms, the all-advertisement distance is four labels/four advertisements and the common-mention distance is four labels/three advertisements. These are hypothetical distances, not observed mistakes. The five lower-threshold company reversals remain four one-edit and one two-edit illustrations. The original 24-advertisement discordant-source review is a preserved discovery frame; the current primary model data have 22 forward and one reverse resolved discordance, because N0798 is now Z/U.

The bounded TensorFlow comparison independently passed 3,176 arithmetic/source checks across the same 105 model advertisements and 26 framework co-mentions. All 315 captured fields were scanned; four preferred-only cases stay outside H. Among co-mentions, both frameworks have H=22, Q=0 P/2 U, example-inclusive=17 P/1 U, and choice/example-inclusive=21 P/1 U. The independent unknown ranges are respectively ±7.69, ±3.85 and ±3.85 percentage points. A zero difference under shared completion requires the explicit same-operator assumption for the bare slash N0149 and the cue-free framework list N0798. Current PyTorch and the extension harmonization agree after the seven main corrections; the inherited/harmonized discrepancy belongs only to the preserved historical extension output.

Use `analysis/empirical/final_empirical_facts.json` for exact numeric values, `audit/local_template_sensitivity.md` for the local-text design and limitations, and `work/empirical/module_input_manifest.json` for portable execution dependencies. Old v3 numeric references are historical only. Source-review rationale remains in `audit/current_u_consistency_review.md` and `audit/discordant_source_review.md`.
'''
    (ROOT/'audit/final_empirical_update.md').write_text(summary,encoding='utf-8')
    print(json.dumps({'status':'PASS','facts':'analysis/empirical/final_empirical_facts.json','module_scripts':len(scripts),
                      'snapshot_inputs':len(frozen),'verification_checks':facts['verification_checks']},indent=2))

if __name__=='__main__':main()
