Table I. Primary functions in whole-firm recruitment

| Primary function | Ads | Ad-weighted % | Firm-equal % |
| --- | --- | --- | --- |
| Manufacturing, quality and supply chain | 214 | 13.1 | 13.0 |
| Software and platforms | 180 | 11.0 | 10.8 |
| ML/AI engineering | 156 | 9.6 | 9.7 |
| Corporate support | 132 | 8.1 | 6.7 |
| Hardware and electrical engineering | 123 | 7.5 | 8.2 |
| Commercial and customer-facing work | 117 | 7.2 | 7.3 |
| Product and program management | 106 | 6.5 | 5.9 |
| Mechanical and electromechanical engineering | 89 | 5.5 | 5.6 |
| Deployment and field service | 84 | 5.2 | 5.2 |
| Control and planning | 75 | 4.6 | 6.2 |
| Data and analytics | 70 | 4.3 | 4.5 |
| Simulation, evaluation and measurement toolchains | 60 | 3.7 | 3.3 |
| Perception | 47 | 2.9 | 2.6 |
| Systems engineering and cross-domain integration | 31 | 1.9 | 2.1 |
| Industrial and experience design | 23 | 1.4 | 1.3 |
| Research science | 23 | 1.4 | 1.1 |
| Robot operations | 22 | 1.3 | 2.7 |
| Composite and multi-direction recruitment | 30 | 1.8 | 1.6 |
| Ambiguous, unmapped or insufficient-source | 48 | 2.9 | 2.5 |

Notes: Ad-weighted percentages use all 1,630 whole-firm advertisements as the denominator: 1,552 advertisements assigned to specific functions and 78 structural or unresolved records. Firm-equal percentages average the within-firm shares. Source: calculations from the job-advertisement corpus.

Table II. Activity within functions and the distribution of activity advertisements

| Activity | Primary function | Activity / function N | Within function % | Activity / total activity | Activity distribution % |
| --- | --- | --- | --- | --- | --- |
| Research activity | Research science | 18/23 | 78.3 | 18/66 | 27.3 |
| Research activity | ML/AI engineering | 36/156 | 23.1 | 36/66 | 54.5 |
| Research activity | Perception | 5/47 | 10.6 | 5/66 | 7.6 |
| Quality-related activity | Manufacturing, quality and supply chain | 159/214 | 74.3 | 159/459 | 34.6 |
| Quality-related activity | Hardware and electrical engineering | 53/123 | 43.1 | 53/459 | 11.5 |
| Quality-related activity | Mechanical and electromechanical engineering | 36/89 | 40.4 | 36/459 | 7.8 |
| Quality-related activity | Deployment and field service | 34/84 | 40.5 | 34/459 | 7.4 |
| Quality-related activity | Systems engineering and integration | 21/31 | 67.7 | 21/459 | 4.6 |

Notes: Function counts are limited to advertisements for which activity status could be evaluated. Research activity appears in 66 advertisements and quality-related activity in 459. The text reports the main contributing functions; activity_bidirectional.csv provides every category, including zeros, structural categories and unknowns. Research science and manufacturing, quality and supply chain were prespecified as the corresponding functions; they were not selected from the results. Source: calculations from the job-advertisement corpus.

Table III, Panel A. Engineering-activity decomposition across sensitivity scenarios

| Scenario | Galbot coverage | Figure coverage | Total gap pp | Composition pp | Within function pp |
| --- | --- | --- | --- | --- | --- |
| Main scope | 82/181 | 60/126 | +11.10 | +19.45 | -8.35 |
| Exclude campus and internship ads | 63/126 | 60/122 | +10.56 | +21.08 | -10.52 |
| Deduplicate duty templates | 79/177 | 59/118 | +12.89 | +19.43 | -6.54 |

Notes: Galbot minus Figure, within the fixed set of four common functions. Coverage denominators are advertisements for which activity status could be evaluated in each scenario. Supplementary Table S7 reports the complete scenarios and missing comparisons. pp denotes percentage points. Source: calculations from the job-advertisement corpus.

Table III, Panel B. Function counts and components of the primary decomposition

| Primary function | Galbot activity/ads | Figure activity/ads | Galbot/Figure shares % | Composition pp | Within function pp |
| --- | --- | --- | --- | --- | --- |
| Corporate support | 0/13 | 1/11 | 15.9 / 18.3 | -0.11 | -1.55 |
| Manufacturing, quality and supply chain | 3/20 | 5/28 | 24.4 / 46.7 | -3.66 | -1.02 |
| ML/AI engineering | 20/24 | 10/10 | 29.3 / 16.7 | +11.55 | -3.83 |
| Software and platforms | 23/25 | 11/11 | 30.5 / 18.3 | +11.67 | -1.95 |

Notes: The common-scope denominators are 82 for Galbot and 60 for Figure. Activity counts / advertisements recover the within-function engineering-activity rates. The composition and within-function components sum to +19.45 and −8.35 percentage points, respectively. Source: calculations from the job-advertisement corpus.

Table IV, Panel A. Technology mentions and statement types

| Task and technology | M positive/N | Ad-weighted % | Firm-equal % | Duties | Required | General | Preferred |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Robot modeling — Python | 73/105 | 69.5 | 66.9 | 3 | 2 | 65 | 6 |
| Robot modeling — PyTorch | 83/105 | 79.0 | 74.5 | 1 | 4 | 75 | 4 |
| Robot runtime software — C++ | 80/87 | 92.0 | 91.4 | 13 | 1 | 73 | 6 |
| Robot runtime software — Linux | 52/87 | 59.8 | 50.2 | 9 | 0 | 50 | 6 |
| Board-level circuitry — Altium | 24/56 | 42.9 | 35.2 | 5 | 0 | 21 | 5 |
| Board-level circuitry — EMC / SI / PI | 36/56 | 64.3 | 67.8 | 27 | 0 | 20 | 11 |

Notes: The last four columns count statement types among advertisements with a mention; each count can be divided by the M-positive count in that row, and types may overlap. DUTY combines the focal person’s use and development statements at the advertisement level. Firm-equal means include firms with a positive valid denominator and zero positives. EMC/SI/PI is a family indicator for compatibility, integrity and related protection methods; its members are unioned and deduplicated by advertisement. It is therefore broader than the single Altium tool. Supplementary Section S1 provides family members and branching rules. Source: calculations from the job-advertisement corpus.

Table IV, Panel B. Unconditional statements in general qualifications

| Task and technology | G positive/N | U | Ad-weighted % | Firm-equal % | Unknown bounds % |
| --- | --- | --- | --- | --- | --- |
| Robot modeling — Python | 40/88 | 17 | 45.5 | 41.7 | 38.1 to 54.3 |
| Robot modeling — PyTorch | 20/97 | 8 | 20.6 | 20.4 | 19.0 to 26.7 |
| Robot runtime software — C++ | 38/64 | 23 | 59.4 | 51.5 | 43.7 to 70.1 |
| Robot runtime software — Linux | 47/86 | 1 | 54.7 | 46.0 | 54.0 to 55.2 |
| Board-level circuitry — Altium | 5/56 | 0 | 8.9 | 8.8 | 8.9 to 8.9 |
| Board-level circuitry — EMC / SI / PI | 15/56 | 0 | 26.8 | 28.2 | 26.8 to 26.8 |

Notes: G here displays only GENERAL—UNCONDITIONAL and does not combine explicitly REQUIRED statements. The point estimate is P/N, where N=P+Z. Unknown-assignment bounds run from P/B to (P+U)/B, where B=N+U; they are not confidence intervals. All 22 qualification-relation cells are provided in the supplementary data. Source: calculations from the job-advertisement corpus.

Table V. General-qualification context among technology mentions

| Task and technology | Mentions | G positive P | P/mentions % | No G positive Z | G unknown U | Choice/example in Z+U |
| --- | --- | --- | --- | --- | --- | --- |
| Robot modeling — Python | 73 | 40 | 54.8 | 16 | 17 | 11/33 |
| Robot modeling — PyTorch | 83 | 20 | 24.1 | 55 | 8 | 52/63 |
| Robot runtime software — C++ | 80 | 38 | 47.5 | 19 | 23 | 16/42 |
| Robot runtime software — Linux | 52 | 47 | 90.4 | 4 | 1 | 2/5 |
| Board-level circuitry — Altium | 24 | 5 | 20.8 | 19 | 0 | 17/19 |
| Board-level circuitry — EMC / SI / PI | 36 | 15 | 41.7 | 21 | 0 | 6/21 |

Notes: P, Z and U are mutually exclusive among mention advertisements and sum to the mention count. P / mentions uses all mention advertisements in the row as its denominator and retains U; the Table IV, Panel B point estimate uses P+Z for the relevant context within the task. In the last column, the denominator is Z+U and the numerator counts advertisements containing at least one choice expression, example expression, or both. These expressions may overlap with PREFERRED, DUTY, REQUIRED and unresolved branches, so this column is not an exhaustive mutually exclusive decomposition. Source: calculations from the job-advertisement corpus.