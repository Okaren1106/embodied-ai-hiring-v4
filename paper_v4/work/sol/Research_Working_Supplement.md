# INTERNAL AI-ASSISTED RESEARCH WORKING SUPPLEMENT — NOT FOR SUBMISSION

This supplement accompanies `Research_Working_Manuscript.md`. It is an internal, AI-assisted research work product. Human author metadata and venue-policy clearance are absent. Reported computations have separate implementation checks; source interpretation remains model-assisted rather than independently human coded.

# Supplement to “What Counts as a Technology Qualification in Embodied AI Hiring?”

## S1. Corpus construction and identity

The accepted corpus contains 1,654 versioned public advertisements from 24 entities. The first wave captured 610 advertisements from eight firms on 31 August 2026. The second captured 1,044 advertisements from 16 entities on 11 September 2026. Selection required an identifiable organization, research relevance, readable current details and stable source identifiers. Failed sources were recorded during construction. The corpus is purposive and does not rank excluded firms.

Composite identity joins corpus, entity, source advertisement identifier and text-version hash. Headquarters, advertised location and source language remain distinct. Coding uses the captured language; country is not inferred from language. The 23-company comparison excludes the separately bounded 24-advertisement Amazon Frontier AI and Robotics team.

Primary function follows the advertisement's main continuing deliverable. The technology sample intersects function with a responsibility-defined primary task. It contains 105 robot-learning/model-development advertisements, 87 advertisements in a broader robotics-software task and 56 board-circuitry advertisements. The robotics-software task includes relevant product-stack and infrastructure roles; it is not a pure runtime or middleware population. The tasks are mutually exclusive. Each advertisement has exactly two fixed targets, producing 496 rows.

## S2. Qualification relation architecture

The relation table stores measurement type, metric, branch and state. The qualification metrics used here are GENERAL and REQUIRED; the separate PREFERRED metric is excluded from H, Q and their alternatives. Within GENERAL and REQUIRED, branches distinguish UNCONDITIONAL from choice, example, conditional and unresolved constructions.

The working manuscript uses these constructs:

- **M (mention):** the target is explicitly named in duties or qualifications.
- **H (qualification-context association):** the target has any known GENERAL or REQUIRED context branch, including unconditional, choice, example, conditional or unresolved branches.
- **Q (unconditional technology-specific qualification statement):** GENERAL or REQUIRED is positive only under an unconditional target-specific reading. P, Z and U remain separate.
- **Q+E:** the relation set admits unconditional and example readings within GENERAL or REQUIRED, including a recorded ambiguous relation when every live reading is in that set.
- **Q+C+E:** the admitted relation set includes unconditional, example and choice readings within GENERAL or REQUIRED.

Conditional branches and the separate PREFERRED metric are not added to Q+E or Q+C+E. P, Z and U are construct-specific states. A Q-unknown becomes positive in an expansion if every live interpretation belongs to the expanded admitted set; it remains U only when inclusion is still unresolved under that rule. These alternatives are distinct estimands, not competing accuracy labels. A source phrase can be correctly represented as an example while researchers reasonably disagree about whether an example counts as target demand.

Production checks report 496 state rows, 456 linked evidence spans, exact span/hash verification, and rowwise \(Q^P\subseteq H\subseteq M\), where \(Q^P\) is the confirmed-positive narrow-Q indicator. A separate implementation passed 3,608 scope checks. These checks do not provide independent human semantic validation.

## S3. Scope totals

**Supplementary Table S1. Counts under nested and alternative constructs**

| Task | Target | Ads | M | H | Q P / U | Q+E P / U | Q+C+E P / U |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Robot learning | Python | 105 | 73 | 67 | 42 / 17 | 43 / 17 | 50 / 17 |
| Robot learning | PyTorch | 105 | 83 | 79 | 22 / 6 | 65 / 4 | 75 / 4 |
| Robotics software | C++ | 87 | 80 | 74 | 38 / 19 | 39 / 19 | 55 / 19 |
| Robotics software | Linux | 87 | 52 | 50 | 47 / 1 | 48 / 1 | 49 / 1 |
| Board circuitry | Altium | 56 | 24 | 21 | 5 / 0 | 7 / 0 | 21 / 0 |
| Board circuitry | EMC/SI/PI | 56 | 36 | 20 | 15 / 0 | 20 / 0 | 20 / 0 |

Notes: P denotes a positive for the named construct. U is the unresolved count after applying that construct's admission rule; it need not equal narrow-Q U. H is a known GENERAL or REQUIRED context occurrence, excludes the separate PREFERRED metric and has no P/Z/U interpretation in this table. A separate implementation reproduced the scope construction and aggregates.

The large PyTorch transition from Q to Q+E is the central construct boundary. The 43 additional PyTorch positives comprise 41 Z-to-P transitions under admitted example relations and two U-to-P transitions whose unconditional-or-example readings are both admitted. Across Python and PyTorch, the total is 44 transitions: 42 from Z and two from U. These are construct changes, not corrections toward a known true label.

## S4. Paired state and weighting design

Every task advertisement contributes both target rows. For narrow Q, the advertisement-level difference has lower contribution \(1(Q_a=P)-1(Q_b\neq Z)\) and upper contribution \(1(Q_a\neq Z)-1(Q_b=P)\). Positive weights aggregate those outer contributions.

Three weights are used:

1. advertisement equal;
2. firm equal, calculated among firms present in the analysis subset; and
3. firm-by-exact-text, where qualification text is Unicode NFKC, case and whitespace normalized, exact clusters receive equal total weight within firms, and firms then receive equal weight.

There are 99 exact full-qualification-text clusters among 105 robot-learning advertisements and 61 among 66 common-mention advertisements. Robotics-software and board samples contain no exact duplicates under this rule, so their firm and firm-by-exact-full-text results coincide. The rule does not detect near duplicates, common clauses or cross-firm templates.

**Supplementary Table S2. Robot-learning narrow-Q weighting results**

| Sample | Weight | Ads | Firms | Confirmed Python−PyTorch pp | Outer range pp |
| --- | --- | ---: | ---: | ---: | ---: |
| All robot-learning ads | Advertisement | 105 | 22 | +19.05 | +13.33 to +35.24 |
|  | Firm equal | 105 | 22 | +20.21 | +14.63 to +31.29 |
|  | Firm × exact text | 105 | 22 | +20.20 | +14.59 to +31.24 |
| Both mentioned | Advertisement | 66 | 18 | +28.79 | +21.21 to +51.52 |
|  | Firm equal | 66 | 18 | +27.78 | +17.04 to +47.08 |
|  | Firm × exact text | 66 | 18 | +27.98 | +17.24 to +47.15 |

Notes: This table concerns Q only. It diagnoses concentration in the narrow construct; it does not resolve whether examples belong in the estimand.

The local-parent diagnostic instead groups the normalized joint target-specific qualification text and scope signature within each firm. It yields 95 groups in the 105-advertisement robot-learning sample and 56 in the 66-advertisement common-mention subset. Six repeated groups contain 16 advertisements in either subset. Missing or unlocated target-parent evidence receives an advertisement-specific fallback. Equal weight is assigned first to firms, then local groups and then advertisements within a group.

**Supplementary Table S3. Robot-learning contrasts under local-parent weighting**

| Sample | Construct | Confirmed Python−PyTorch pp | Outer range pp |
| --- | --- | ---: | ---: |
| All 105 advertisements | M | −7.83 | −7.83 to −7.83 |
|  | H | −10.49 | −10.49 to −10.49 |
|  | Q | +18.60 | +13.02 to +29.43 |
|  | Q plus all recorded examples | −11.52 | −14.07 to −0.68 |
|  | Q plus choices/all recorded examples | −18.77 | −21.32 to −7.94 |
| Both mentioned, 66 | H | −5.56 | −5.56 to −5.56 |
|  | Q | +26.12 | +15.38 to +45.00 |
|  | Q plus all recorded examples | −16.14 | −21.32 to +2.74 |
|  | Q plus choices/all recorded examples | −19.25 | −24.43 to −0.37 |

Notes: This is a repetition diagnostic. Exact local wording does not control all templates, firm style or job composition.

## S5. Common-mention joint states

**Supplementary Table S4. Narrow-Q joint states**

| Pair | P/P | P/Z | P/U | Z/P | Z/Z | Z/U | U/P | U/Z | U/U | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Python / PyTorch | 14 | 22 | 1 | 1 | 11 | 2 | 3 | 10 | 2 | 66 |
| C++ / Linux | 24 | 1 | 1 | 5 | 1 | 0 | 15 | 1 | 0 | 48 |
| Altium / EMC/SI/PI | 2 | 3 | 0 | 3 | 9 | 0 | 0 | 0 | 0 | 17 |

The first state refers to the first named target. The current 22-to-one resolved robot-learning discordance is a property of narrow Q. It is not an independent validation of the operator exclusions that help produce it.

## S6. Source scope review

A deterministic join links all 496 target rows to the preserved context index with no key failure. In the current robot-learning common-mention states, all 22 Python-P/PyTorch-Z records contain a PyTorch choice-or-example flag. One resolved reverse record remains. An earlier source-review frame contained two reverse records; consistent treatment of bare parenthetical framework lists moved one from PyTorch P to U.

Full-source review of these 24 discordant records classifies the 22 PyTorch contexts as:

- nine Chinese `等`-only constructions;
- nine explicit “such as” or “e.g.” constructions;
- two choice constructions; and
- two combined choice/example constructions.

The two records that were reverse cases in the earlier frame have choice flags for Python. This full-source review was checked against the saved source scope but remains model-assisted rather than an independent human recode. It supports the descriptive branch inventory, not the claim that one construct is uniquely correct.

The interpretive issue is substantive. A phrase such as “familiar with mainstream deep-learning frameworks such as PyTorch” does not unconditionally require PyTorch, but it places PyTorch inside an applicant qualification and may indicate that PyTorch experience satisfies a broader framework requirement. Q codes the target-specific unconditional statement; H and Q+E preserve the broader relation.

The broader increment review covers all 44 robot-learning target–advertisement transitions from current-Q nonpositive or unresolved to Q-plus-example positive. Forty-three concern PyTorch and one concerns Python. Forty-two are Z-to-P transitions and two are U-to-P transitions under the expanded relation set. Cue families are:

- 17 clear non-exhaustive cues: seven “such as,” five “e.g.” and five Chinese “如,” all for PyTorch;
- 25 Chinese “等”-only open lists: 24 for PyTorch and one for Python; and
- two bare parenthetical lists for PyTorch, without “such as,” “e.g.,” “如” or “等.” Their live readings are unconditional or example, so they remain U under Q but are P under Q+E.

These categories support admission-rule alternatives, not accuracy labels. Table S5 shows that the full-sample reversal appears when the “等”-only class is admitted; clear cues alone leave the outer range crossing zero.

**Supplementary Table S5. Example-admission rules for Python−PyTorch**

| Admission rule | Full sample Python P/U | Full sample PyTorch P/U | Full range pp | Both-mentioned Python P/U | Both-mentioned PyTorch P/U | Both-mentioned range pp |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Narrow Q | 42 / 17 | 22 / 6 | +13.33 to +35.24 | 37 / 15 | 18 / 5 | +21.21 to +51.52 |
| Q plus 17 clear-cue cases | 42 / 17 | 39 / 6 | −2.86 to +19.05 | 37 / 15 | 30 / 5 | +3.03 to +33.33 |
| Q plus recorded examples except bare parentheses | 43 / 17 | 63 / 6 | −24.76 to −2.86 | 38 / 15 | 49 / 5 | −24.24 to +6.06 |
| Q plus all recorded examples | 43 / 17 | 65 / 4 | −24.76 to −4.76 | 38 / 15 | 51 / 3 | −24.24 to +3.03 |

Notes: “Clear cue” means “such as,” “e.g.” or Chinese “如.” “等”-only open lists enter the last two expanded rules. U is recomputed for each admission rule; ambiguity entirely within its admitted relation set becomes P.

## S7. Exploratory PyTorch–TensorFlow framework control

The after-discovery extension retains the same 105 robot-learning advertisements and adds literal TensorFlow as a target. All 79 presumed nonmatches were checked across captured fields. Twenty-six advertisements name TensorFlow, and all 26 also name PyTorch. Full-source review found both framework names under the same predicate in every matched advertisement and no separate target-specific qualification occurrence. Four occurrences are PREFERRED-only and therefore enter M but not H.

**Supplementary Table S6. PyTorch−TensorFlow contrasts among 26 joint mentions**

| Construct | PyTorch P/U | TensorFlow P/U | Confirmed gap pp | Outer range pp |
| --- | ---: | ---: | ---: | ---: |
| M | 26 / 0 | 26 / 0 | 0.0 | 0.0 to 0.0 |
| H | 22 / 0 | 22 / 0 | 0.0 | 0.0 to 0.0 |
| Q | 0 / 2 | 0 / 2 | 0.0 | −7.69 to +7.69 |
| Q plus examples | 17 / 1 | 17 / 1 | 0.0 | −3.85 to +3.85 |
| Q plus choices/examples | 21 / 1 | 21 / 1 | 0.0 | −3.85 to +3.85 |

Notes: Outer ranges assign target unknowns independently. When only the documented same-predicate unknowns receive coupled completions, every difference is zero. The comparison was specified after the Python–PyTorch result was known and is diagnostic rather than a holdout test. Source review was model-assisted, not an independent human validation.

## S8. Semantic readings versus scope alternatives

The original diagnostic selected 105 advertisement–technology pairs from 94 advertisements using a fixed hash order within prior-G strata. A fresh model reading produced 16 Q differences. Three explicit-example PyTorch cases were clarified from U to Z in the current narrow Q. A subsequent full review of the 46 remaining U rows and repeated parent clauses resolved five additional U states to Z: one PyTorch and four C++ states. A final same-predicate audit then moved two bare-parenthetical PyTorch records to Q-U for consistent treatment: N0798 from P and N1044 from Z. Both remain P under Q+E and Q+C+E because their live unconditional and example readings are admitted. These seven v4 amendments are stored in an overlay; frozen v3 inputs remain unchanged. Ten list/slash cases form seven coupled switches, yielding 128 combinations. Three readings inconsistent with the fixed modifier rule remain in an all-fresh stress test.

Those 128 readings vary the state under the existing narrow-Q definition. They do not enumerate every possible semantic interpretation and do not test a different example-inclusive estimand. The working manuscript therefore reports semantic envelopes for Q and separate scope alternatives for Q+E and Q+C+E.

Unknown assignment adds another layer. It moves recorded U states to binary endpoints within a construct. It does not decide whether a known example should be in that construct. These layers must not be combined into a single “robustness” label.

## S9. Firm comparisons and classification breakdown

Firm cells retain the fixed task base B, mention counts, GENERAL and Q states, conditional proportions and assignment ranges. Eligibility requires both firms to have at least N evaluable observations in mention, GENERAL and Q. N=10 yields three comparisons, all Galbot–XSquare. N=5 yields 32 comparisons across nine companies; the three stricter pairs recur.

**Supplementary Table S7. Narrow-Q comparison classifications**

| N | Pairs | Supported retention | Supported reversal | Conditional reversal overlap | Conditional retention overlap | Conditional tie overlap |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 10 | 3 | 2 | 0 | 1 | 0 | 0 |
| 5 | 32 | 22 | 5 | 3 | 1 | 1 |

The adversarial breakdown orients each supported pair from higher to lower Q. A resolved positive removed from the higher firm changes the margin by \(1/B_H\); a mentioned resolved nonpositive changed to positive in the lower firm changes it by \(1/B_L\). Exhaustive integer search finds the minimum edits that make the least-favorable margin zero or negative.

At N=5, 27 directions are supported in all 128 narrow-Q readings. Ten lose strict support after one adverse correction, 18 after at most two and 21 after at most three. Of the five supported reversals, four need one correction and one needs two. These are mathematical witnesses, not records believed to be wrong.

## S10. Process and evidential limits

The author reviewed the accepted corpus and resolved project-level task and function rules. The preserved package does not document an independent human second code for every technology relation. Model-assisted source reading, coordinating adjudication, deterministic computation and independent arithmetic verification are distinct activities.

The earlier paired implementation was independently rebuilt without importing the production script and passed 11,083 identity and arithmetic comparisons. It verified weights, joins, leave-one-firm-out values and 128 reading envelopes. The independent audit of paired-breakdown outputs passed 22,656 checks. A separate qualification-scope implementation passed 3,608 checks covering state nesting, metric reconciliation and evidence links. The framework-control implementation passed 3,176 independent checks of inventories, states and contrasts. Production checks also verify the source spans and hashes. None of these computational audits validates source meaning as an independent human recode.

The project also faces a venue-policy issue. Emerald's current narrative policy prohibits generative-AI copywriting and contains restrictions on using LLMs to generate, manipulate or report data and results, while allowing transparent analytical assistance and copy-editing of author-created text. The exact application to model-assisted text classification requires publisher interpretation. This supplement is therefore an internal evidence document, not a policy-cleared submission artifact.

## S11. Reproduction map

Primary v4 inputs and outputs are located under:

- `analysis_E_english_v4_0/source_snapshot/analysis/ad_technology_current.csv`
- `analysis_E_english_v4_0/source_snapshot/source_v2/data/inputs/context_index.csv`
- `analysis_E_english_v4_0/source_snapshot/source_v2/data/inputs/context_evidence.csv`
- `analysis_E_english_v4_0/analysis/paired/paired_summary.csv`
- `analysis_E_english_v4_0/analysis/paired/paired_joint_states.csv`
- `analysis_E_english_v4_0/analysis/paired/qualification_scope_states.csv`
- `analysis_E_english_v4_0/analysis/paired/qualification_scope_summary.csv`
- `analysis_E_english_v4_0/analysis/paired/qualification_scope_contrasts.csv`
- `analysis_E_english_v4_0/analysis/example_increments/admission_rule_contrasts.csv`
- `analysis_E_english_v4_0/analysis/example_increments/example_increment_ledger.csv`
- `analysis_E_english_v4_0/analysis/v4_ad_technology_current.csv`
- `analysis_E_english_v4_0/analysis/v4_overlay_checks.json`
- `analysis_E_english_v4_0/extensions/framework_control/outputs/framework_contrasts.csv`
- `analysis_E_english_v4_0/extensions/framework_control/outputs/source_review_26.csv`
- `analysis_E_english_v4_0/analysis/empirical/classification_breakdown_envelopes.csv`

Run `python REPRODUCE.py` from `analysis_E_english_v4_0` as the 20-step offline reproduction entry point. The production scripts include `work/apply_v4_overlay.py`, `work/paired_analysis.py`, `work/paired_context.py`, `work/qualification_scope.py`, `work/paired_breakdown.py` and `work/empirical/classification_breakdown.py`. Input hashes and check counts accompany the output directories. The frozen v3 materials identify the source version; reproduction uses the packaged `source_snapshot` and does not depend on a neighboring v3 directory.
