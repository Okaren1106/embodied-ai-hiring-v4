# Stage A field mapping

Unit: one public job advertisement at a fixed text version. Advertisements are not headcount.

## Identity

| Field | Meaning | Source |
|---|---|---|
| package_id | Current accepted-reference package | `current_pointer.slot=accepted_reference` → `packages` |
| classification_id | Classification row in the research store | `classifications.classification_id` |
| observation_id | Joined observation row | `classifications.observation_id` → `observations` |
| record_id | Advertisement identity in the accepted package | `classifications.record_id` / `record_json.record_id` |
| text_version_hash | Hash of the frozen body version | `classifications.text_version_hash` / `source.text_version_hash` |
| identity_key | package_id + record_id + text_version_hash | Derived; this is the analysis primary key |
| reading_id | E/N reading number (`origin_review_id` or `packet_id`) | Display only; **not** a key. E0107 is two ads |
| origin_packet_id | Packet id such as P0107 | Display only |

## Job master (`jobs.csv`)

Company, title, location, source URL/path, and `observation_date` (`wave`) come from `observations` joined in the same read transaction. Four-dimension statuses and item counts come from `record_json.reference`. Nested evidence stays in long tables and `accepted_jobs.jsonl`, not as unexplained string lists.

Text-length columns (`duties_chars`, `requirements_chars`, `full_description_chars`) are character counts of observation fields. They are coverage diagnostics, not classified content.

## Long tables

`primary_roles.csv`, `secondary_roles.csv`, `technical_concepts.csv`, `skills.csv`, `activities.csv` keep every original item, including repeated mentions. `item_index` is the original list index. `raw_json` is the original item object. `missing_fields` lists keys expected by the current contract but absent in a legacy object. `end_derived` is `start + len(quote)` only when `end` was omitted; original `end` is not overwritten.

Long tables are not collapsed. Later Q2/Q3 statistics must filter first by `use`, `mention_relation` and activity `relation` (and by requirement-tree conditions), then deduplicate advertisement×label inside that slice. `(record_id, text_version_hash, label_code, context)` is not a complete statistical key: 105 skill groups, 1028 technical groups and 253 activity groups share ad/label/context but differ in requirement strength or ownership. Unique-advertisement coverage is a separate metric and must not replace those rows with one representative.

## Relations and unmapped mentions

`relations.jsonl` stores complete `role_structure` and `requirement_groups` trees plus a node list with `parent_id`. Trees are not flattened to ALL. Node `duties_status` is copied from the original object field `duties_status` (legacy alias `duty_status`).

`unmapped_mentions.csv` stores every `reference.unmapped_mentions` object from every advertisement, including CODED ads. If `dimension` is missing, `dimension_missing=1` and the original object is kept. This is not inferred as skills.

## Company files

`company_profile.csv` is 24 rows for accepted `company_id`s only. Values are copied from the locked copies of `company_landscape.csv`, profiles, hiring audit, evidence ledger, status matrix and boundary events. `inheritance_status=INHERITED_NOT_REVERIFIED`. Empty listing/financing fields mean the inherited files do not encode them.

`company_evidence.csv` keeps ledger, status-matrix and boundary rows separately (`record_kind`). `source_row_or_heading` is the 1-based CSV logical record with the header as row 1. `direct_quote_or_summary` and `supporting_evidence_ids` are exported. GAP and NOT_ESTABLISHED rows are included; 214 rows are not 214 confirmed external facts.

`company_gaps.csv` is company × fact. Gap types: `NO_EXISTING_EVIDENCE`, `DATE_UNKNOWN`, `ENTITY_UNCLEAR`, `CONFLICT`, `NOT_APPLICABLE`. “Not yet searched” is not coded as “searched and not found”.

## T1 / T2

T1 joins inherited organization and hiring-source scope 1:1 from `company_profile`. Those fields remain `INHERITED_NOT_REVERIFIED`; `scope_time_applicability=INHERITED_NOT_ALIGNED_TO_HIRING_WAVE`. Amazon FAR, Boston Dynamics, Fourier and Diligent keep team / whole-company multi-product / channel differences. This is not a Stage B verification.

Shares are proportions of advertisements. `share_*` is in `[0,1]` with 6 decimals; `pct_*` is percent with 2 decimals. `NA` is used when the denominator is 0; it is not written as 0. `small_sample_flag=1` when that company-class count is under 10 (display rule only).
