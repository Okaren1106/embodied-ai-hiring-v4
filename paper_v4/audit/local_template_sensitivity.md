# Exact local target-qualification repetition sensitivity

This exploratory analysis was added after the model source review found a shared Python/PyTorch qualification sentence in five Figure advertisements and closely related wording in three Apptronik advertisements. Full-requirements-block equality did not capture all this local repetition. The analysis tests whether giving repeated local target wording less weight changes the within-advertisement result. It is a post hoc repetition diagnostic, not adjustment for company writing style, seniority or an independently sampled template population.

The input is the v4 primary paired advertisement table and the inherited GENERAL/REQUIRED context-evidence parents. The original evidence branches remain frozen; the new Q and expanded constructs come from the separately verified v4 scope table, which propagates all three v3 and seven v4 source adjudications. The final two v4 adjudications represent cue-free peer-framework lists as unresolved for narrow Q, while both named allowed readings satisfy the example-inclusive construct.

## Signature and scope

Each advertisement has two distinct target slots. Each slot retains the complete set of its GENERAL/REQUIRED parent texts, the recorded metric, and an observable scope guard. A nonempty nearest-heading text is normalized and retained. If the heading is absent but the field is explicitly `requirements`, that field supplies the scope guard. If neither is available, the advertisement receives a unique fallback. The full parent is retained: nothing removes experience years, list numbering, punctuation, proficiency terms or local operators.

Normalization consists only of Unicode NFKC, casefold and whitespace collapse. It does not use fuzzy matching, translations, synonym replacement or semantic equivalence. Multiple qualifying parents are retained as a deduplicated set within each target. Target A and target B are never pooled into an unlabeled concatenation. Matching a repeated sentence for only one target is insufficient when the other target's complete retained parent set differs. Different headings or GENERAL/REQUIRED scope also prevent equality. This intentionally conservative rule can miss genuine shared templates.

If either target has no retained qualification parent, or any retained parent has unlocated scope outside the explicit requirements field, the cluster ID is unique to the advertisement. Missing qualification text cannot turn unrelated advertisements into one template. Source-span and source-field SHA-256 checks confirm all 327 qualification-parent occurrences, with every target quote nested inside its retained parent. The signature does not use P/Z/U, so results are not clustered by outcome. It does condition on previously selected qualification-scope evidence.

Within a chosen task/subset, give each observed firm equal weight; within a firm, give each distinct joint local text/scope group equal weight; within a group, give each advertisement equal weight. Thus an advertisement in firm f, group g has weight `1/(F × G_f × n_fg)`. The program independently checks the primary Q endpoints by averaging advertisements within groups, groups within firms, and firms overall. It records exact rational weights. All 128 inherited semantic readings keep primary signatures, membership and weights fixed. Broad constructs are compared under primary source rules only, because a new Q reading does not establish a new broad-scope branch code.

## V4 results

| Robot-model subset | Ads | Firms | Joint local groups | Repeated groups | Ads in repeated groups | Unique fallback ads |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| All advertisements | 105 | 22 | 95 | 6 | 16 | 50 |
| Both technologies mentioned | 66 | 18 | 56 | 6 | 16 | 11 |

The five Figure advertisements E0487, E0495, E0491, E0492 and E0489 form one group. Apptronik E0414 and E0415 form a group, while E0384 is distinct: its experience threshold is three rather than five years. These differences are retained instead of being erased as irrelevant. Qualification wording repeated across companies does not merge firms; weights still average observed firms equally.

All differences below are Python minus PyTorch in percentage points, under equal firms and equal local groups within each firm.

| Construct | All 105 advertisements | Both-mentioned 66 advertisements |
| --- | ---: | ---: |
| Mention M | −7.83 | 0.00 |
| General/required qualification context H | −10.49 | −5.56 |
| Narrow Q: primary unknown range | +13.02 to +29.43 | +15.38 to +45.00 |
| Narrow Q: envelope across all 128 readings | +13.02 to +29.43 | +15.38 to +45.00 |
| Q plus recorded examples: primary unknown range | −14.07 to −0.68 | −21.32 to +2.74 |
| Q plus choices/examples: primary unknown range | −21.32 to −7.94 | −24.43 to −0.37 |

The narrow-Q pattern is not eliminated by these exact local repetitions. The broad-context and expanded-construct comparisons continue to qualify its substantive meaning. The common-mention example-inclusive range crosses zero; the choice/example-inclusive range is slightly negative. The latter endpoint is close to zero and should not be emphasized as a stable population finding. These are outer unknown-assignment bounds, not sampling confidence intervals. The 128 inherited readings do not cover every defensible semantic interpretation, especially systematic alternative treatment of Chinese 等 or cue-free parenthetical examples.

The complete outputs also retain the two secondary task pairs. Runtime has 86 local groups among 87 advertisements and 47 among 48 common-mention advertisements; board/circuit has 54 among 56 and 15 among 17. High fallback counts, particularly for board work, show that this is a limited text-equality diagnostic rather than complete template discovery.

## Inconsistency discovered and corrected

The initial signature inspection found one unique group with conflicting primary Q pairs: N0508 and N0486 at Deep Robotics. Full-source inspection showed all three captured body fields are identical, beyond the local sentence, yet only N0486 had inherited A099's example clarification. That discrepancy prompted complete review of all 46 v3-current unresolved pairs in 44 advertisements, rather than selective correction of this one case. Five changes were adopted in the separate v4 overlay. See `current_u_consistency_review.md` and `v4_overlay_independent_verification.json` for exact identities, sources and propagation checks.

After adoption, no local group has conflicting primary Q pairs. This is a concrete consistency repair found through the repetition analysis; it is not evidence that all resolved codes are error-free. No new state is assigned by the local-weighting script itself. The original v3 data and context branches remain intact.

## Reproduction and limitations

Run `work/empirical/local_template_sensitivity.py` after the v4 paired and scope producers. The script uses only the Python standard library and packaged `source_snapshot` inputs. Outputs begin with `analysis/empirical/local_template_`: membership and signature JSON; exact parent-span audit; group coverage; groups and state patterns; rational advertisement weights; primary construct contrasts; all semantic-reading estimates; envelopes; and input-hash checks.

The comparison with firm-equal results isolates the additional effect of this exact local equality rule; comparison with advertisement weighting simultaneously changes firm weighting. A repeated qualification parent can contain other requirements, while related wording with punctuation or numbering differences remains separate. Scope guards are inherited extraction metadata rather than newly verified headings. Giving every distinct text group equal weight changes the finite-corpus estimand; it is not a variance estimator or a cure for dependence. The source review does not establish a unique correlated annotation-error unit, so no group-level error probability or template-level correction count is claimed.
