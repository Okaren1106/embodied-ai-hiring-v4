# Empirical upgrade: direction and available data

Prepared 2026-09-26 before new computations. This is an exploratory, post-result analysis proposal; no preregistration, new independent coding or population sampling is claimed.

## What is already implemented

The v3 analysis already contains fixed-base mention, confirmed qualification, conditional qualification and unknown-assignment bounds; every eligible firm pair; a fixed-base versus conditional decomposition; 128 coupled source-admissible reading combinations; task-boundary restrictions; and evaluability coverage. Repeating those calculations or adding arbitrary regressions would not constitute a substantive advance.

The apparent firm heterogeneity at the strict threshold concerns the same two firms. Lowering a denominator threshold expands the comparison but does not create precision or representative coverage. The main scientific outcome should therefore be a within-task account of what qualification expressions add to mentions, with cross-firm ordering presented as limited local evidence.

## Available files and fields

| Input | Coverage and useful fields | What it does not supply |
| --- | --- | --- |
| `analysis_E_english_v3_0/analysis/ad_technology_current.csv` | 496 unique advertisement–technology rows, 248 advertisements; immutable identity, reading ID, company, task, M, G, R, Q, choice/example indicator, three prior clarification flags | Independent error rate, seniority, template identity, hiring outcomes |
| `analysis_E_english_v3_0/source_v2/analysis/diagnostic_comparison.csv` | 105 stratified diagnostic pairs; prior/fresh/adjudicated states, source quotations, task-scope flags | Random validation of all 496 pairs; independent human gold standard |
| `analysis_E_english_v3_0/data/sensitivity_policy.json` | Seven coupled ambiguity groups containing 10 observed reading disagreements, generating 128 deterministic readings | Probabilities or relative plausibility for readings |
| `analysis_E_english_v3_0/analysis/admissible_reading_pairs.csv` | Existing all-reading firm differences and denominators | Unrecognized P/Z classification errors |
| `analysis_E_english_v3_0/source_v2/work/provenance/profile_records.csv` | Corpus-level source wave, headquarters, raw advertised location, deterministic language and core membership | Comparable seniority or team/product boundaries |
| Stage D `tables/Q3_ads_final.csv` | Broader task and fine-task coding with source quote, version, review scope and reviewer lineage | Independent validation or later hiring behavior |
| Stage D `tables/Q3_states_final.csv` | Broader advertisement–label–metric–branch state matrix, including primary-task identifiers; enables extensions beyond core 248 | Automatic comparability of every label or task, source-independent measurement |
| Stage D `tables/Q4_dedup_membership.csv` | Same-company same-function exact normalized duty template clusters and requirements-equality flag | Near-duplicate templates, jointly evaluated seniority effects |

Full Stage D paths have prefix `reports/2026-09-14_company_data_analysis/stage_d_integrated_v2/run_20260917_astra_core_q2_v3/`.

## Selected bounded addition

Compute an adversarial **classification-error breakdown analysis** for cross-firm directions that survive every recorded unknown assignment and all 128 admissible readings. This fills a stated gap in v3: those bounds cover recorded unknowns, not undetected errors in resolved P/Z states.

For each fixed-base firm comparison, orient A as the supported higher-Q firm and B as lower-Q. After unfavorable U assignment, the supporting margin is `P_A/B_A − (P_B+U_B)/B_B`. Ask for the smallest number of resolved pair states whose P↔Z correction would reduce this margin to zero or below, at fixed task membership, denominators and U sets. A mistaken A positive contributes 1/B_A; a missed B positive contributes 1/B_B. Primary sensitivity keeps the mention indicator fixed and permits B Z→P only if M=1, respecting Q⊆M. A broader sensitivity permits corrections among M=0 rows too and must be labelled joint mention/qualification error.

Repeat across all 128 admissible readings, returning the smallest breakdown count, the attainable range of counts, and a concrete example set of advertisement identities. These are adversarial distances, not estimated numbers of wrong codes. They offer a check on whether stable semantic-readings results warrant language such as robust firm ordering.

The root task is separately handling within-advertisement technology comparisons, exact template grouping and firm weighting. This subtask will not duplicate them. Any broader matrix extension should follow a substantive task–technology question and a consistent coding frame; using the largest available row count is not an objective by itself.
