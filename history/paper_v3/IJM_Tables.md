Table I. Technology mentions and direct qualification expressions

| Task and technology | Ads B | Mention M | Q states
P / Z / U | Confirmed
P/B % | Conditional
P/(B−U) % | Q bounds
% |
| --- | --- | --- | --- | --- | --- | --- |
| Robot learning
Python | 105 | 73 | 42 / 46 / 17 | 40.0 | 47.7 | 40.0–56.2 |
| Robot learning
PyTorch | 105 | 83 | 23 / 77 / 5 | 21.9 | 23.0 | 21.9–26.7 |
| Robot runtime
C++ | 87 | 80 | 38 / 26 / 23 | 43.7 | 59.4 | 43.7–70.1 |
| Robot runtime
Linux | 87 | 52 | 47 / 39 / 1 | 54.0 | 54.7 | 54.0–55.2 |
| Board circuitry
Altium | 56 | 24 | 5 / 51 / 0 | 8.9 | 8.9 | 8.9–8.9 |
| Board circuitry
EMC/SI/PI | 56 | 36 | 15 / 41 / 0 | 26.8 | 26.8 | 26.8–26.8 |

Notes: Q is the advertisement-level union of unconditional GENERAL and REQUIRED expressions. P denotes a confirmed positive, Z no recorded positive within the coding scope, and U unresolved scope. Bounds are [P/B, (P+U)/B], not confidence intervals. Conditional proportions exclude U. Robot learning includes model development. EMC/SI/PI denotes the compatibility, signal-integrity and power-integrity method family. The two technologies within each task reuse the same advertisements. Source: calculations from the captured job-advertisement corpus.

Table II. Main company differences on fixed and evaluable task bases

| Technology | Mention gap
pp | Confirmed Q gap
pp | Conditional Q gap
pp | Q difference bounds
pp | Interpretation |
| --- | --- | --- | --- | --- | --- |
| Python | +30.2 | +52.4 | +53.6 | +19.0 to +63.5 | Supported retention |
| PyTorch | -29.4 | -1.6 | +1.2 | -1.6 to +9.5 | Conditional reversal; bounds overlap |
| Linux | +23.8 | +27.5 | +33.3 | +27.5 to +33.8 | Supported retention |

Notes: All gaps are Galbot minus XSquare. Task bases are 18 and 21 advertisements for Python and PyTorch, and 16 and 10 for Linux. M and confirmed Q use these full bases. Conditional Q excludes each firm’s U cases. Q difference bounds assign unknowns in the two firms to opposite endpoints. All three comparisons pass the minimum evaluable-cell threshold of ten; they reuse the same two firms and are not independent replications. Positive bounds support Galbot’s higher direct-expression share. Source: calculations from the captured job-advertisement corpus.

Table III. Conditional ordering and fixed-base bounds for all eligible comparisons

| Min N | Task and technology | Pairs | Supported retention | Supported reversal | Conditional reversal with overlap | Same direction with overlap |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | All combinations | 3 | 2 | 0 | 1 | 0 |
| 5 | Robot learning
Python | 6 | 3 | 2 | 1 | 0 |
| 5 | Robot learning
PyTorch | 6 | 3 | 1 | 1 | 1 |
| 5 | Robot runtime
C++ | 3 | 0 | 1 | 1 | 1 |
| 5 | Robot runtime
Linux | 15 | 14 | 1 | 0 | 0 |
| 5 | Board circuitry
Altium | 1 | 1 | 0 | 0 | 0 |
| 5 | Board circuitry
EMC/SI/PI | 1 | 1 | 0 | 0 | 0 |
| 5 | All combinations | 32 | 22 | 5 | 3 | 2 |

Notes: Each firm must meet the minimum separately for evaluable M, G and Q; N is their minimum. Retention and reversal are relative to mention ordering. Supported categories require the Q difference bounds to exclude zero. Overlap categories describe conditional point ordering only. No mention tie, conditional tie or zero bound endpoint occurs. The 32 comparisons at five include all three comparisons at ten; rows share firms and advertisements. Bounds are finite-corpus assignment ranges, not sampling intervals. Source: calculations from the captured job-advertisement corpus.
