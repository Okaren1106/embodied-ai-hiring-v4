# Numeric and editorial cross-reference audit

Date: 2026-09-21  
Scope: bounded audit of the final English release and `work/sections` against the frozen Chinese v1.4 table assets. This audit did not recode advertisements, rerun semantic classification, or provide independent semantic validation.

## Conclusion

The final checked release preserves the source table numbers and the consolidated display structure. No remaining numerical-cell, formula, prose-denominator, table-number, figure-number, or untranslated-table-note discrepancy was found in the checked scope.

Two cross-reference defects were found during the audit and were corrected by the coordinating editor before the final pass: Supplementary Table S2 referred to a nonexistent “Supplementary Section S4”, and Table IV, Panel B referred to an S4 label that did not appear in the English Supplement Guide. The final S2 note points to the English Supplement Guide; Table IV, Panel B points to the supplementary data, whose guide contains an “All 22 qualification-relation cells” entry. This audit did not edit either manuscript note.

The earlier prose issue involving 159 is also resolved in both `work/sections/results.md` and the rebuilt release. The final sentence now distinguishes the two denominators correctly:

- `159/214 = 74.3%` is incidence within manufacturing, quality and supply chain;
- `159/459 = 34.6%` is that function’s share of all advertisements with quality-related activity.

This was a known correction from `prose_audit.md`, not a new discrepancy discovered in this pass.

## Files and objects checked

The audit compared:

- the frozen source `analysis_E_revision_v1_4/release/tables/table_assets.json`;
- `analysis_E_english_v1_0/work/sections/table_assets_en.json`;
- `analysis_E_english_v1_0/release/tables/table_assets_en.json` and all 15 released table CSV files;
- `release/authoring/display_crosswalk.json`;
- `release/English_Manuscript_IJM.md`, `IJM_Main_Text.md`, `IJM_Tables.md`, `Supplementary_Material.md`, and `SUPPLEMENT_GUIDE.md`;
- `release/figures/figure_assets_en.json` and the three English PNG figures;
- the five rendered pages of `IJM_Tables.pdf` and seven rendered pages of `Supplementary_Material.pdf` through the current contact sheets.

The machine-readable computation and file-hash record is [numeric_asset_audit.json](numeric_asset_audit.json). The reproducible checker is [audit_numeric_assets.py](audit_numeric_assets.py).

## Table-cell and order preservation

All 15 source asset keys occur in the same order in both the work translation and release translation. The source, work, and release versions each contain 108 rows. Every row retains the same number of cells.

For every source-to-English row cell, the checker compared ordered numeric tokens, including signed values, fractions, decimals, ranges, and the `*` small-sample marker. Results:

| Check | Result |
| --- | ---: |
| Source table assets | 15 |
| Source rows | 108 |
| Work rows | 108 |
| Release rows | 108 |
| Numeric-token or `*` mismatches, source → work | 0 |
| Numeric-token or `*` mismatches, source → release | 0 |
| Release CSV row mismatches against release JSON | 0 |

The audit also confirmed that width metadata is unchanged where supplied. Titles, headers and notes were allowed to change for translation and consolidated journal numbering; numeric cells and row order were not.

## Recomputed identities

The checker ran 175 source-linked arithmetic tests; all passed. The tests cover:

- T1A entity and advertisement totals: 24 entities and 1,654 advertisements, of which 23 whole firms account for 1,630;
- the sum of all T1B function/structural rows and each displayed ad-weighted percentage;
- every T2A within-function percentage and activity-distribution percentage;
- the 84-advertisement total across T2B and T2C;
- all three T3 identities in which total difference equals composition plus within-function components;
- T3B direct sums: Galbot has 46/82 engineering-positive advertisements and Figure 27/60, a difference of 11.10 percentage points; ML/AI engineering plus software account for 49/82 and 21/60 advertisements, respectively;
- all T4A mention percentages;
- all T4B point values and unknown-assignment bounds using `N=P+Z` and `B=N+U`;
- every T4C identity `P+Z+U=mentions`, every `P/mentions` percentage, and every `Z+U` denominator in the choice/example column;
- all 20 T5 scenario bounds, the identity `B=N+U`, and every `*` marker for `0<N<10`;
- the quality-related outside-function assignment bounds: `296/459 = 64.5%` and `(296+4)/459 = 65.4%` after rounding.

The three English figure images were also inspected. Supplementary Figure S1 reproduces the three T3 component triples. Figure 2 displays the five intended firm–technology cases with the same M and G fractions and U counts as the corresponding main-scenario T5 rows. Figure 1 retains each firm’s full advertisement denominator and the unresolved columns described in its note.

## Key prose claims

Nineteen load-bearing numerical statements in the final combined manuscript were checked against the source cells or the direct computations above. All passed. The checked claims include:

| Claim family | Checked value |
| --- | --- |
| Corpus and main scope | 1,654/24; 1,630/23 |
| Research activity | 18/23; 18/66; 36/156; 48/66 = 72.7% outside research science |
| Quality-related activity | 159/214 = 74.3%; 159/459 = 34.6%; 64.5–65.4% outside the corresponding function |
| Engineering decomposition | 46/82 versus 27/60; +11.10 = +19.45 − 8.35 percentage points |
| Composition mechanism | 49/82 = 59.8% versus 21/60 = 35.0% |
| Task mention counts | 73/105, 83/105, 80/87, 52/87, 24/56, 36/56 |
| Task-level GENERAL—UNCONDITIONAL values | 40/88, 20/97, 38/64, 47/86, 5/56, 15/56 |
| Mention-level context | PyTorch 20/83 with Z=55 and U=8; Linux 47/52 = 90.4% |
| Firm coverage | 120 points across 22, 20 and 18 firms |
| Python firm case | 14/18 versus 10/21; G 12/16, U=2 versus 3/14, U=7; bounds 66.7–77.8% versus 14.3–47.6% |
| C++ firm case | 14/16 versus 9/10; G bounds overlap |
| Apptronik Altium case | 7/12 mentions and one GENERAL—UNCONDITIONAL positive |

No prose statement was treated as verified merely because it appeared in an English table. Derived values were recomputed from declared source cells; copied values were traced to the matching source row.

## Consolidated display labels and notes

The 18-entry display crosswalk is internally consistent:

- main tables: T1B → Table I; T2A → Table II; T3/T3B → Table III, Panels A/B; T4A/T4B → Table IV, Panels A/B; T4C → Table V;
- supplementary tables: T0–T5/S3 map to Supplementary Tables S1–S8 as declared;
- figures: F1 → Figure 1; F3 → Figure 2; F2 → Supplementary Figure S1.

All expected display titles occur in the combined manuscript or supplement. A targeted search found no remaining use of source labels such as Table 1a–5d, Table A1/A2, Supplementary Table A1/A2, Figure 3, or internal phrases such as “source asset” in the final English manuscript, separate tables file, or supplementary material.

All English table and figure titles and notes were checked for Han characters; none remain. The unchanged Chinese source package under `release/supplement/original_v1_4` intentionally retains its original language and numbering and was not treated as an English-translation defect.

The rendered IJM table pages and supplementary pages show the consolidated labels and the checked values without an observed row shift, missing panel, or clipped numerical column. This was a bounded visual reconciliation of the existing renders, not a complete typography or accessibility review.

## Boundaries

- The audit did not rerun `reproduce.py`, regenerate classifications, inspect all 1,654 advertisements, or estimate coding reliability.
- It does not establish that translated category labels or prose interpretations are independently semantically valid. It verifies numeric preservation, declared arithmetic, selected prose claims, and editorial cross-references.
- Firm-equal percentages were preserved exactly from the source assets but were not independently recomputed from the 120-row company distribution or raw advertisement records.
- The three figures were checked against displayed source-table values and labels; their underlying plotting program was not rerun.
- Citation accuracy, literature coverage, journal fit, and the full manuscript’s substantive argument are outside this audit.
- No manuscript, table asset, figure asset, source file, or project-state file was modified by this audit. Only the audit Markdown, JSON record, and checker script were written under `analysis_E_english_v1_0/verification`.
