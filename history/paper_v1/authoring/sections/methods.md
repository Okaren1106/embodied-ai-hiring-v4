## 2. Data and measurement

### 2.1 Sample and observation unit

The data comprise public job advertisements from firms whose documented work concerns humanoid or general-purpose robots, robot foundation models, robot learning and manipulation, mobile manipulation, or related components, software, and deployment services. A firm need not manufacture a complete robot, but its work must connect clearly to physical robotic systems. A team within a large corporation enters only when its organizational and recruitment scope can be separated.

The purposive, nonprobability sample was assembled from public product information, company information and recruitment-source checks. Selection reflects research relevance, business scope and source accessibility. Recruitment sources include Feishu, Moka, Greenhouse, Lever, Workday, Ashby and firm-operated pages. Source checks assessed readable job detail, stable identifiers and core fields; coverage remains limited to the accessible boards. The first snapshot contains 610 advertisements from eight firms observed on 31 August 2026. A second adds 1,044 advertisements from 16 entities observed on 11 September 2026, widening the range of products and business models. The combined corpus contains 1,654 advertisements from 24 entities across two dated observations rather than a simultaneous census. Unreachable sources retain unknown status and are not treated as zero recruitment. Because online advertisements can differ systematically from the underlying population of jobs and firms (Fabo and Mýtna Kureková, 2022; Tsvetkova et al., 2024), claims remain confined to this firm sample; industry-wide parameters lie outside the study's scope.

The main comparison covers 1,630 advertisements from 23 whole-company recruitment boards; 24 Amazon Frontier AI and Robotics advertisements remain a separately bounded team. “Whole company” refers to the accessible board, whose coverage of every job or worker could not be verified. Support and nontechnical advertisements remain in the denominator. The observation is a versioned advertisement identified by entity, source job identifier and text version, so counts refer to advertisements rather than vacancies, hires or employees. Source-insufficient records remain in overall composition; eligibility for other analyses is dimension-specific.

### 2.2 Functions, activities, objects, and tasks

Primary function records the advertisement's main work area. The corpus contains 1,576 advertisements in 17 specific functions, including 1,552 within the 23-company scope. The other 78 whole-company records comprise 19 composite, 11 multi-direction, 15 ambiguous, two unmapped, and 31 source-insufficient advertisements. All 1,630 remain in the composition denominator. Secondary functions and activities are multivalued and cannot be added to primary-function counts.

Research, engineering, and quality-related activities remain separate from function. Research requires a concrete problem or object plus methodological exploration or scientific testing; tuning, optimization, and innovation language alone do not suffice. Engineering covers implementation, integration, debugging, and operational-system delivery, but not manufacturing or procurement by default. Broad quality-related activity includes verification execution, release decisions, compliance, and defect closure. Activities can overlap, but each needs task evidence. Numerators count work owned by the role, including explicit shared responsibility; assistance alone does not enter. Activity is evaluable for 1,599 whole-company advertisements, excluding the 31 source-insufficient records only from this dimension.

Work object and task are also separate. An 84-advertisement case set records whether machine-learning/artificial-intelligence (ML/AI) engineering and software roles concern models, data, robot runtime systems, or fulfilment information technology; objects may overlap, and 81 cases lack named-product attribution. The technology analysis instead defines three mutually exclusive main-task groups within the relevant primary function: 105 robot-modeling, 87 robot-runtime-software and 56 board-level-circuitry advertisements. Function, activity, object and task therefore answer different questions.

### 2.3 Technology expression and unresolved records

Technology measurement has three dimensions (summarized with the analysis scopes in Supplementary Tables S1–S2). $M$ records an advertisement-level mention in the role's duties or qualifications. $W$ records statement type—DUTY, REQUIRED, GENERAL, or PREFERRED—from headings and local wording; types may overlap. $G$ combines statement type with the relation around the technology. The main text focuses on GENERAL—UNCONDITIONAL: a direct general qualification without a governing choice, example, or unresolved relation. GENERAL covers ordinary experience, familiarity, or ability; REQUIRED needs explicit mandatory language or required-skills scope and is counted separately. “Unconditional” describes the encoded relation, not an invariably binding hiring rule.

Within the evaluable $P$/$Z$/$U$ subset, each $G$ cell has one mutually exclusive state; source exclusion and non-applicability remain separate. $P$ denotes an explicit positive. $Z$ means no positive was recorded within the available evidence and coding scope; it does not establish that the employer has no such requirement. $U$ denotes an unresolved object, responsibility, or relation affecting the cell. If $N=P+Z$, the reported point value is $P/N$. With $B=N+U$, assigning all recorded unknowns first to nonpositive and then to positive gives

\[
\left[\frac{P}{B},\;\frac{P+U}{B}\right].
\]

These bounds are not confidence intervals and exclude unrecognized coding errors. A separate explicit positive in the same advertisement takes precedence for that cell; an example elsewhere does not cancel it. Six technologies generate 496 advertisement–technology pairs from 248 advertisements and 456 linked evidence records.

### 2.4 Comparison rules and sensitivity

Advertisement-weighted rates pool counts and valid denominators. Firm-equal rates average firm-specific $P/N$ over firms with $N>0$, including valid zero-positive firms. Bounds can use a different firm set because they require $B>0$. Group summaries need at least three firms and a pooled valid denominator of 20; $0<N<10$ is flagged as small.

For engineering activity, a symmetric Kitagawa decomposition compares Galbot ($A$) with Figure ($B$) over a fixed set $K$ of four common functions. Let $w_{jk}$ denote function $k$'s advertisement share and $r_{jk}$ its within-function engineering-activity rate for firm $j$. Let $R_j$ be the pooled engineering-activity rate, equal to the weighted average of the function-specific rates:

\[
R_A-R_B=\sum_{k\in K}(w_{Ak}-w_{Bk})\frac{r_{Ak}+r_{Bk}}{2}
+\sum_{k\in K}(r_{Ak}-r_{Bk})\frac{w_{Ak}+w_{Bk}}{2}.
\]

The first term is composition and the second the within-function-rate component (Kitagawa, 1955). Their sum is an arithmetic identity and carries no causal interpretation. The fixed set contains the four functions for which each firm has at least ten evaluable advertisements.

Sensitivity analyses remove exact within-scope duty-text templates, exclude explicit internship, campus or graduate advertisements, and add secondary tasks while retaining the primary-function restriction. Source screens cover firms for which every advertisement is evaluable for activity (R1). R2 further requires an official source rated GOOD—publicly structured or regular, with stable identifiers and reasonably complete text—or EXCELLENT, which additionally indicates more complete structured fields and support for repeated collection, and no source-insufficient primary-function record; R3 retains from R2 only advertisements with descriptions of at least 200 characters. They retain 17 firms/968 advertisements, 11/576 and 11/557. A comparison becomes unavailable if a screen removes one firm. The scenarios and six technologies were defined before preparation of this manuscript but remain exploratory; “prespecified” refers to that sequence rather than preregistration. Coding depth varies: among 1,576 specific-function records, 469 received full-text review, 760 boundary review and 347 were carried forward from the first round; the corresponding task-sample counts are 56, 164 and 28. Review included model-assisted rereading and adjudication of prior records rather than independent double coding, and no intercoder-reliability study was conducted.
