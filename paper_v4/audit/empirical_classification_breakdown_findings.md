# What the additional empirical analysis changes

The new computation qualifies the cross-firm ordering claims. Stability across the recorded unknown states and 128 admissible semantic readings does **not** imply stability to previously unrecognized classification error. At the lower comparison threshold, four of the five supported mention-to-qualification reversals would lose their qualification-direction support after one adversarial resolved-state correction; the fifth needs two. These are sensitivity distances, not detected mistakes.

This is useful as a limitation and a way to calibrate claims. It is not a sufficient standalone methodological novelty for an IJM article. The stronger empirical narrative should concern the substantive distinction between technology presence and the articulation of candidate qualifications, demonstrated on comparable advertisements. Firm ordering remains a secondary application whose usable coverage is narrow.

## Design and exact computation

The analysis reads the v4 derived 496 advertisement–technology states after all seven source corrections, a freshly rebuilt eligibility frame, and the seven inherited coupled reading switches. It reconstructs all 128 readings without changing source data. Thirty-two comparisons at N≥5 cover nine companies; three at N≥10 cover two. The latter are included in the former and must not be added as extra comparisons. The company rebuild first reproduced 1,820 frozen-v3 comparison values and then recomputed every cell's eligibility; no new company-pair keys enter under v4 or its 128 readings. One overlapping conditional retention (Deep Robotics–Galbot/PyTorch) becomes an overlapping conditional tie, so the old 22/5/3/2 four-category total is superseded by 22/5/3/1 plus one tie.

For each originally supported direction, orient H as the higher-Q firm and L as the lower-Q firm. The least favorable difference is

`d = P_H/B_H − (P_L+U_L)/B_L`.

A resolved H positive corrected to Z decreases d by `1/B_H`; a resolved L nonpositive corrected to P decreases d by `1/B_L`. The minimum integer pair `(i,j)` satisfying `i/B_H+j/B_L≥d` determines the smallest number of errors that could remove strict directional support. Task membership, B, the unresolved set and the reading-specific states are fixed while calculating this distance. A zero endpoint counts as loss of strict support, not as proof of reversal.

The primary variant keeps M fixed and permits L Z→P only among recorded mentions. This preserves the logical restriction Q⊆M. It does not turn any mention absence into a qualification positive. A broader, separately labelled scenario allows joint mention/qualification detection error; its results concern Q direction only and do not preserve the original mention ordering.

The calculation is repeated for each reading. The minimum across readings asks when the claim of support under **every** recorded reading first fails. It does not establish that the direction fails under every reading. The output separately reports the number of corrections needed to make the entire U interval opposite-or-tied in each reading. Counts are advertisement–technology states; shared companies and advertisements mean that counts cannot be summed across comparisons or interpreted as independent events.

## Results

Of 27 directions supported under all recorded readings at N≥5, ten are one correction from losing support and eighteen are two or fewer corrections away. These 27 comprise 22 retained mention directions and five reversed directions. Of the five reversals, four need one correction and one needs two. Restricting attention to retained directions, six need one correction and thirteen need at most two. These counts use the fixed-mention primary sensitivity.

| Technology | Reversal comparison | Higher Q firm | Smallest supporting margin, pp | Minimum resolved corrections to lose support |
| --- | --- | --- | ---: | ---: |
| Python | Deep Robotics–Galbot | Galbot | 4.17 | 1 |
| Python | Deep Robotics–Figure | Figure | 8.93 | 1 |
| PyTorch | Galbot–Figure | Galbot | 22.22 | 2 |
| C++ | LimX Dynamics–Field AI | Field AI | 15.00 | 1 |
| Linux | PaXini Tech–X Square | X Square | 2.86 | 1 |

The main-threshold Python direction is four corrections from losing support in every reading considered separately. The main Linux direction is four corrections away under the primary coding and three to five across admissible readings; consequently its support under every reading first fails at three corrections. PyTorch has no supported direction initially, so assigning it a positive breakdown count would be misleading.

Allowing joint mention/qualification detection errors weakens the lower-threshold directions further: thirteen of 27 need one correction and twenty-two need at most two. The five reversal results are unchanged. At N≥10, Python remains four corrections away; the minimum for Linux becomes two. This broader scenario should not replace the fixed-mention result because it changes the measurement layer held constant.

## What is and is not learned

The low counts arise partly from small firm cells: one corrected observation shifts a five-advertisement share by 20 percentage points. A large difference can therefore have a small breakdown count, as in the 15-point C++ comparison. The result is finite-corpus fragility, not a sampling standard error. No distribution of coding errors, probability of a mistaken ordering, or actual error count is estimated. The source diagnostic does not identify a population error rate and cannot supply one here.

The witnesses in the output are arbitrary admissible combinations chosen to demonstrate mathematical attainability. They do **not** identify records believed to be wrong and do not authorize recoding. Other source-supported readings could exist outside the seven recorded groups. The analysis still conditions on the task boundaries, missing-source treatment and chosen technologies.

For the paper: retain one short paragraph acknowledging that the lower-threshold reversals are small-cell illustrations; place the full breakdown table and algorithm in the supplement. Do not replace the original unknown bounds, and do not describe the new output as confidence intervals or validation. Do not lead the manuscript with the five reversals as a robust industry pattern.

## Reproduction and verification

Run from the repository root:

`python analysis_E_english_v4_0/work/empirical/classification_breakdown.py`

Run `rebuild_company_comparisons.py` first. Inputs and SHA-256 hashes are recorded in `analysis_E_english_v4_0/analysis/empirical/classification_breakdown_checks.json`. The algorithm reconstructs 8,960 interval endpoints against the separately rebuilt v4 comparison outputs and cross-checks exhaustive integer minimization against an independent largest-weight-first solution. It verifies that every input hash is unchanged. These are arithmetic checks, not independent source coding.

Outputs:

- `classification_breakdown_readings.csv`: all 128 readings × 35 threshold-labelled pair keys × two error regimes.
- `classification_breakdown_envelopes.csv`: primary and range of minimum correction counts for each comparison.
- `classification_breakdown_summary.csv`: coverage and counts by threshold and original classification.
- `classification_breakdown_witnesses.csv`: hypothetical correction identities for the primary reading and one-correction cases, explicitly labelled as sensitivity witnesses.
- `classification_breakdown_checks.json`: exact reconstruction checks and source hashes.
