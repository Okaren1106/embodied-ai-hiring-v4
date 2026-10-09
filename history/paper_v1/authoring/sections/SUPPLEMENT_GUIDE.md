# Supplement guide

The supplementary files accompanying the English manuscript include the complete materials prepared for the Chinese v1.4 manuscript under `supplement/original_v1_4`. The links below point to those files, with paths relative to the English manuscript directory.

## Starting points

- [Source README](supplement/original_v1_4/README.md) describes the 15 source tables, three figures and document-building tools.
- [Original supplementary index](supplement/original_v1_4/appendix/补充材料索引.md) maps the seven supplementary groups used by the source study.
- [Measurement definitions](supplement/original_v1_4/appendix/测量说明.md) records the activity, relation, state, task, and technology-family rules.
- [Coding and version provenance](supplement/original_v1_4/appendix/编码与版本来源.md) explains the heterogeneous review history and the limits of the researcher-confirmation record.

## Evidence and analysis files

- S3 contextual evidence: [local filterable index](supplement/original_v1_4/evidence/index.html), [context evidence CSV](supplement/original_v1_4/evidence/context_evidence.csv), [advertisement–technology index CSV](supplement/original_v1_4/evidence/ad_technology_context_index.csv) and [source-text records JSON](supplement/original_v1_4/evidence/records.json).
- All 22 qualification-relation cells: [firm results](supplement/original_v1_4/reproduce/base_v1_0/inputs/core_existing_G_primary_company.csv) and [aggregate results](supplement/original_v1_4/reproduce/base_v1_0/inputs/core_existing_G_primary_aggregates.csv).
- Other analysis outputs: [firm technology results](supplement/original_v1_4/analysis/company_context_distribution.csv), [bidirectional activity measures](supplement/original_v1_4/analysis/activity_bidirectional.csv), [four-function decomposition](supplement/original_v1_4/analysis/decomposition_four_roles.csv), and [sensitivity membership changes](supplement/original_v1_4/analysis/sensitivity_membership_changes.csv).
- Source tables: [combined table JSON](supplement/original_v1_4/tables/table_assets.json) and individual editable CSV files in [`tables`](supplement/original_v1_4/tables/).
- Source figure assets are in [`figures`](supplement/original_v1_4/figures/); publication checks are in [`verification`](supplement/original_v1_4/verification/).

The evidence files preserve Chinese advertisements in Chinese and English advertisements in English. Article quotations translated from Chinese are identified as translations and retain the advertisement identifier, choice or example language, negation, heading scope and uncertainty. The original Chinese text is retained alongside the translation for verification.

## Reproduction

Python 3.10 or later is required. From the English release directory, run:

```text
python supplement/original_v1_4/reproduce/reproduce.py --output /path/to/new_output
```

The output path must not already exist and must be outside `supplement/original_v1_4/reproduce`. The base reproduction uses only the Python standard library, checks the input manifest and rebuilds numerical summaries, table files and contextual exports. Add `--figures` to recreate figures; this requires matplotlib, numpy and a usable Chinese font. Different plotting-library versions may change image bytes without changing the numerical results.

The reproduction package reads the finalized semantic records used in the analysis. It rebuilds numerical outputs without repeating semantic coding or estimating intercoder reliability, and it preserves unresolved states. `M_positive = 0` in `ad_context_correspondence.csv` does not by itself constitute an (M)-level (Z); (G) states are defined separately. The package is supplied with the manuscript; public hosting and licensing arrangements have not yet been established.
