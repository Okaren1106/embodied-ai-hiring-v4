# Stage A analysis rules

## Input lock

All Stage A counts are computed from `accepted_jobs.jsonl`. r3 recomputes from that snapshot plus `locked_inputs/`: company landscape, evidence ledger, status matrix, hiring audit, boundary events, 24 profiles, and measurement rules. The lock manifest stores each file hash, including extract_meta.json. Recompute verifies the complete inventory, snapshot and metadata before deriving tables; a mismatch stops the run before publication. Recompute does not query the live database and does not reread live company CSVs or live rules.

The 1648-ad automatic-classification baseline is a different observation set and is not in any Stage A denominator.

`human_validated=false` is original provenance. It does not overturn the user-confirmed human-review completion status recorded elsewhere.

## Counting

1. One advertisement counts once in T1/T2.
2. Composite-function and alternative-direction ads still count once, as those two structure classes. Component functions stay in `role_structure` / relations, not as extra T2 primary counts.
3. Primary and secondary roles are separate tables and are never cartesian-joined before counting.
4. Multi-label dimensions keep every long-table row. Q2/Q3 must filter by use/relation first, then advertisement-label dedup inside that slice. Unique-ad coverage is separate.
5. Default Q1 denominator is all accepted ads of that company, including unspecified primary states.
6. The coded-primary subset denominator is `primary_status=CODED` only, and is named separately.
7. Company-equal: mean of company shares. Ad-weighted: pool ads, then compute. Zero denominators are `NA`.
8. Skill `UNMAPPED` is not `NOT_MENTIONED` and is not `SOURCE_UNASSESSABLE`. Stage A keeps coverage counts; skill-specific denominators wait for later indicators.
9. `use`, `context`, `relation`, requirement-tree relations (`ALL`/`OR`/`EXAMPLE`/`UNRESOLVED`) and negated/background/unresolved states are retained. Optional/example/equivalent-alternative relations are not turned into must-have items.
10. Duplicate candidates are not dropped. They are listed in `quality_issues.json` / the quality report.

## Adaptation of legacy objects

- Missing `dimension` on an unmapped mention: keep empty, set `dimension_missing`.
- Missing evidence `end`: derive `start+len(quote)` into `end_derived` only.
- Missing `use`/`context`/`relation`: leave empty; do not guess `DUTY_USE` or `OWNED`.
- Role-structure node status: map `duties_status` (canonical) and `duty_status` (alias).
- Non-object items: wrap as `{'_original': value}` and record a quality issue.

## Company inheritance

Stage A does not search the web. Inherited commercialization codes, UNKNOWN values, and open questions remain as found. Dates: fact event date, publication date, retrieval/profile date, and hiring observation date stay in separate columns. Locators are captured when the locked CSV is read, not renumbered after grouping.
