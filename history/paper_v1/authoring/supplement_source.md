# Supplementary Material

Work Composition and Technology Requirements in Embodied AI Job Advertisements

## S1. Measurement definitions and analytical scopes

This supplement expands the definitions used in Section 2. Supplementary Table S1 maps each analysis to its advertisement scope and unit; Supplementary Table S2 separates technology mention, statement type, and qualification relation. ML, AI and IT denote machine learning, artificial intelligence and information technology, respectively.

[[T0]]

[[TM]]

### S1.1 Functions, activities and work objects

Primary function is single-valued when the advertisement has one clear main work area. Composite function records several independent deliverables when no single one dominates; multi-direction recruitment records a posting that explicitly allows recruitment into alternative work directions. Both preserve the relation expressed in the source rather than splitting one advertisement into several observations. Ambiguous, unmapped, and source-insufficient records remain visible. Secondary functions and activities are multivalued, so their totals need not equal the number of advertisements.

Research activity requires both a concrete research problem or object and methodological exploration or scientific testing. Engineering activity requires implementation, integration, debugging, or delivery of an operational system. Quality-related activity includes verification execution, release decisions, compliance, and defect closure across development and production. The activity numerator includes OWNED and explicit shared responsibility, but excludes PARTICIPATES-only relations. Manufacturing or procurement does not become engineering by occupational title, and experience in quality work does not establish that the advertised role performs quality activity. Each activity is summarized in two directions: its incidence within a function, and the function's share of all advertisements recording that activity.

The 84-advertisement object case study permits multiple objects and counts both owned and participated-in relations. It does not define membership in the technology task strata. Those strata instead use the role's main deliverable: policy or embodied-model training and optimization for robot modeling; runtime, middleware, or robot applications for robot runtime software; and boards, printed circuit boards, or related power and drive systems for board-level circuitry. Membership first restricts to the 23 whole-company boards, then intersects the relevant primary function with the main task. Adding a secondary task retains the primary-function restriction and deduplicates by advertisement and target task.

### S1.2 Technology relations and advertisement-level states

A technology can be mentioned in a duty, an explicitly mandatory qualification, a general qualification, or a preferred qualification. Statement type (W) follows headings and local wording. A heading may set the default scope, but a local modifier can override it. Words describing proficiency—such as “strong” or “deep experience”—do not by themselves turn GENERAL into REQUIRED. Choice and example relations propagate through the ancestors of the technology item. A direct or conjunctive item is UNCONDITIONAL only when no governing choice, example, or unresolved restriction applies. Choice and example may coexist. An unresolved ancestor remains UNRESOLVED; the absence of a modifier from a short excerpt does not justify recoding it as unconditional.

States are resolved independently for every advertisement, technology, statement type, and relation cell. An explicit positive yields (P). Without a positive, source exclusion and non-applicability are retained separately; a relevant unresolved relation yields (U); only the remaining evaluable cases yield (Z). Thus (Z) is “no positive recorded for this cell,” not employer absence. A separate, explicit positive in the same advertisement establishes (P) even if another occurrence is an example. Pending work is not converted to (Z) or (U).

The electromagnetic-compatibility, signal-integrity and power-integrity (EMC/SI/PI) indicator is a predefined technology-family measure. It covers explicit electromagnetic compatibility or immunity, signal-integrity or power-integrity analysis and design, and related electromagnetic interference (EMI), electrostatic discharge (ESD), surge, isolation, grounding, shielding or filtering language when used in those contexts. Procurement of compliant components and generic printed-circuit-board design do not qualify. Family members are unioned at the advertisement level, so several members still count once. An 'or' relation between members of the same family can satisfy the family-level union, while the individual members keep their own relations; a choice across families remains a choice. Altium is a named software package and therefore has a different measurement grain; their rates do not estimate a general contrast between software tools and engineering methods.

### S1.3 Weighting, display and sensitivity

Advertisement weighting answers what share of advertisements in the observed sample records a cell. Firm-equal weighting answers the mean of valid firm-specific shares and includes firms with (P=0) whenever (N>0). It reduces the influence of large recruitment boards while the purposive firm sample remains non-representative. Unknown bounds use (B=P+Z+U), so the firms contributing to a bound may differ from those contributing to a point estimate. Valid zero cells remain in the equal-weight mean; (N=0) remains missing.

Template removal groups advertisements within firm and primary function after normalizing whitespace in duties and retains the lexicographically fixed advertisement identifier. For the engineering decomposition, a missing duties field uses the complete description without an 80-character threshold; technology analyses apply the rule only when duties contain at least 80 characters. This procedure tests sensitivity to repeated text and leaves the number of actual openings unmeasured. The campus/internship screen uses explicit title or qualification language after false-positive checks; missing experience requirements do not imply graduate recruitment. The R1–R3 source screens test progressively narrower observability conditions. They impose observability restrictions rather than define probability samples, and a comparison is unavailable when a screen removes one member of the firm pair.

Review depth varies across records. The 469/760/347 split for specific functions means full-text review, boundary review and judgments carried forward from the first round; the task-sample split is 56/164/28. Full-text and boundary review included model-assisted rereading and adjudication of prior records. The process was not independent human double coding, and no intercoder-reliability estimate is reported.

## S2. Firm scope, work objects and coverage

[[T1A]]

[[T2B]]

[[T2C]]

[[T4D]]

## S3. Full sensitivity results and reproducibility

The supplementary package provides the scenarios and contextual evidence underlying the reported comparisons. Supplementary Table S7 reports every engineering-decomposition scenario, including source screens under which the Galbot–Figure comparison is unavailable because Galbot does not pass the screen. Supplementary Table S8 reports all 20 technology-case scenarios with small-sample marks, unresolved counts and assignment bounds.

[[S3]]

[[T5]]

The contextual evidence archive links 248 task advertisements to 496 advertisement–technology pairs and 456 retained evidence records. Each record preserves a stable advertisement identity, observation version, technology excerpt, its parent sentence or list item, heading position and other relevant evidence from the same advertisement. The three source-text fields used in the analysis are retained. Chinese-language source evidence remains in Chinese. In the article and supplement, quotations translated from Chinese are identified by advertisement ID and as translations, with choice, example and scope language preserved. English-language advertisements remain verbatim.

The reproduction program checks the input manifest and rebuilds the derived analyses, the 15 source-table files and the contextual evidence exports from supplied comma-separated-value (CSV) files and finalized coded records. Its base computation uses Python 3.10 or later and the standard library; optional figure reproduction also requires matplotlib, numpy and an available Chinese font. Reproduction rebuilds links and numerical summaries from those records without repeating semantic coding or assessing coding reliability. The package accompanies the manuscript, and `SUPPLEMENT_GUIDE.md` describes its files and the command for a fresh output directory.

[[F2]]
