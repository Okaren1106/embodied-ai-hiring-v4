## 3. Work composition and activities

### 3.1 Recruitment composition in the observed sample

The whole-firm sample contains 18 firms supplying complete robots or robotic-system products, three cross-embodiment model and software firms, one firm operating a robot-based fulfilment service and one firm combining tactile components with robot products. Amazon Frontier AI and Robotics contributes 24 advertisements as a separately bounded team outside the 23-firm comparisons (Supplementary Table S3).

[[T1A]]

Manufacturing, quality and supply chain is the largest primary function in the whole-firm sample, with 214 of 1,630 advertisements (13.1 per cent). Software and platforms accounts for 180 (11.0 per cent), ML/AI engineering for 156 (9.6 per cent), corporate support for 132 (8.1 per cent), and hardware and electrical engineering for 123 (7.5 per cent). Firm-equal shares leave manufacturing, software and ML/AI engineering near the top, but change the relative positions of corporate support and hardware. Pooled advertisement shares therefore partly reflect recruitment-board size rather than only within-firm composition (Table I).

[[T1B]]

Composition also differs across firms. Software and ML/AI engineering account for 25/184 and 24/184 Galbot advertisements. At Figure, manufacturing, quality and supply chain accounts for 28/126 and software for 11/126; Apptronik has 20/81 hardware advertisements, while Nimble Robotics has 6/34 each in software and manufacturing. Figure 1 retains structural and unresolved records in firm denominators. For Field AI, 23/131 advertisements lack enough text to assign a function—the same count as identified software advertisements—so incomplete text remains visible rather than becoming an observed zero.

[[F1]]

### 3.2 Concentration within functions and distribution across functions

Research activity is concentrated within research science but distributed more widely across the sample. It appears in 18/23 research-science advertisements (78.3 per cent), yet research science contributes only 18/66 advertisements with research activity (27.3 per cent). ML/AI engineering has a lower within-function incidence—36/156, or 23.1 per cent—but supplies 54.5 per cent of all 66 research-activity advertisements. Overall, 48 of the 66 research-activity advertisements (72.7 per cent) lie outside the prespecified corresponding function of research science. These measures answer opposite conditional questions: how common an activity is within a function, and where advertisements containing that activity are located (Table II).

[[T2A]]

Quality-related activity follows the same pattern. Its broad definition covers verification, release, compliance and defect closure as well as manufacturing quality. It appears in 159/214 manufacturing, quality and supply-chain advertisements (74.3 per cent), and those 159 account for 34.6 per cent of the 459 advertisements with quality-related activity. It also appears in hardware (53/123), mechanical (36/89), deployment (34/84), and systems integration (21/31). Of the 459 advertisements, 296 lie outside the prespecified corresponding function and four have ambiguous primary functions; assigning those four either way yields an outside-function share of 64.5–65.4 per cent.

### 3.3 Work objects within the same function

Function matching alone does not establish comparable work in the fixed work-object cases. In ML/AI engineering, model work appears in 12/12 AgiBot advertisements and 22/24 Galbot advertisements; data work appears in 4/12 and 12/24, respectively. In software, 19/25 Galbot advertisements concern robot runtime, compared with 4/6 at Nimble Robotics; two of the six Nimble advertisements also concern fulfilment IT. Objects may co-occur within an advertisement (Supplementary Tables S4 and S5).

[[T2B]]

[[T2C]]

Only three of the 84 advertisements link to a named product; attribution remains unknown for 81. Because these advertisements identify work objects more often than named-product affiliation, the technology analysis narrows comparisons to robot modeling, robot runtime software and board-level circuitry.

## 4. Function composition and engineering activity

Galbot has a higher combined engineering-activity rate than Figure within their four common functions, but the two components point in opposite directions. Engineering activity appears in 46/82 Galbot advertisements (56.1 per cent) and 27/60 Figure advertisements (45.0 per cent), a +11.10-point difference. ML/AI engineering and software jointly account for 49/82 Galbot advertisements (59.8 per cent), compared with 21/60 at Figure (35.0 per cent). This concentration in high-engineering functions produces a +19.45-point composition component. Figure nevertheless records the higher engineering-activity rate within each common function, producing a −8.35-point within-function component (Table III, Panels A and B).

[[T3]]

[[T3B]]

The components remain oppositely signed after excluding campus and internship advertisements (+21.08 and −10.52 points) and after deduplicating identical duty templates (+19.43 and −6.54 points). The total difference remains positive in both cases, at +10.56 and +12.89 points (Supplementary Figure S1).

[[F2]]

The decomposition covers 82/181 activity-evaluable Galbot advertisements and 60/126 Figure advertisements in corporate support; manufacturing, quality and supply chain; ML/AI engineering; and software and platforms. Under source screens R1, R2 and R3, Galbot is ineligible and the firm-pair comparison is unavailable; Supplementary Table S7 reports these cases as missing.

## 5. Technology expression within comparable tasks

### 5.1 Mentions and statement types

Technology prevalence varies across the three matched tasks. Python and PyTorch appear in 73/105 and 83/105 robot-modeling advertisements. C++ and Linux appear in 80/87 and 52/87 robot-runtime-software advertisements. Altium appears in 24/56 board-level-circuitry advertisements, while the electromagnetic-compatibility, signal-integrity and power-integrity (EMC/SI/PI) method family appears in 36/56. The family indicator unions compatibility, integrity and related protection methods, so its measurement grain differs from that of a single named design tool (Table IV, Panel A).

[[T4A]]

Statement type adds information that mention counts omit. Of 73 Python mentions, 65 appear in GENERAL, six in PREFERRED, two in REQUIRED and three in DUTY statements; categories may overlap. The corresponding C++ counts are 73, six, one and 13. EMC/SI/PI appears in duties in 27/36 mention advertisements, including nine duty-only cases, while Altium appears in duties in 5/24. Technologies can therefore describe work content as well as qualifications.

### 5.2 Contextual qualification of mentions

Panel B isolates GENERAL—UNCONDITIONAL, meaning that the named technology appears without a local choice or example relation in general qualifications. It does not combine explicitly REQUIRED statements, and “unconditional” describes the relation around the technology name rather than a binding hiring rule. The resulting point estimates differ from raw mentions: 40/88 for Python, 20/97 for PyTorch, 38/64 for C++, 47/86 for Linux, 5/56 for Altium and 15/56 for EMC/SI/PI. Their unknown-assignment bounds reflect only recorded $U$ cases and are not confidence intervals (Table IV, Panel B).

[[T4B]]

Within mention advertisements, PyTorch has GENERAL—UNCONDITIONAL status in 20/83; 55 record Z and eight U. Of those other 63 records, 52 contain choice or example wording. Altium has this status in 5/24, while 17 of the other 19 contain choice or example wording. Linux reaches 47/52 (90.4 per cent). Table V includes $U$ in the mention denominator; Table IV, Panel B uses $P+Z$ in the task-level context cell.

[[T4C]]

Examples from the source text illustrate these relations. A Paxini board-level advertisement refers to electronic design automation (EDA) and printed circuit board (PCB) design; in translation, it states, “Familiar with at least one EDA tool (e.g., Altium Designer, PADS, etc.) for schematic drawing and PCB layout design” (N0339). The requirement concerns at least one EDA tool; Altium and PADS define examples within that choice. By comparison, an English-language Agility Robotics advertisement states exactly, “Deep experience with Altium for component generation and schematic entry” (E0329). Its later Bonus Points passage adds a choice or preference qualification for Altium, but that later wording does not erase the earlier GENERAL—UNCONDITIONAL positive.

Example and choice relations are also distinct. An AgiBot advertisement states, in translation, “Familiar with deep-learning frameworks such as PyTorch, JAX and TensorFlow” (N0440); a Fourier advertisement similarly states, in translation, “Familiar with mainstream deep-learning frameworks such as PyTorch” (N0460). Both provide examples, but neither specifies the “at least one” relation present in N0339. A Unitree advertisement refers to electromagnetic compatibility and interference (EMC/EMI); in translation, it states, “Responsible for EMC/EMI electromagnetic-compatibility design and testing” (E0099). Because this sentence appears under duties, it records work content rather than a qualification. These examples support treating M, W and G as separate dimensions rather than successive levels of requirement intensity.

### 5.3 Firm cases and sensitivity

The six indicators yield 120 firm–technology points across 22 robot-modeling, 20 runtime-software and 18 board-level-circuitry firms. Only two firms have Python or PyTorch mention denominators of at least ten; each board-level indicator has one. C++ has 17 valid GENERAL—UNCONDITIONAL firm denominators, but only one reaches ten (Supplementary Table S6).

[[T4D]]

Within these limits, the direction of the Galbot–X Square Robot Python comparison is preserved across the defined scenarios. Mentions are 14/18 at Galbot and 10/21 at X Square Robot. GENERAL—UNCONDITIONAL counts are 12/16 with U=2 and 3/14 with U=7, giving non-overlapping unknown-assignment bounds of 66.7–77.8 and 14.3–47.6 per cent. Deduplicating templates or excluding campus and internship advertisements preserves the direction; adding secondary tasks leaves membership unchanged (Figure 2 and Supplementary Table S8).

[[F3]]

The C++ case supports a more limited statement. Mentions are frequent at both firms—14/16 at Galbot and 9/10 at X Square Robot—but GENERAL—UNCONDITIONAL counts of 9/11 with U=5 and 3/4 with U=6 produce overlapping bounds; the latter valid denominator is four. At Apptronik, seven of 12 board-level advertisements mention Altium, but only one records it as GENERAL—UNCONDITIONAL. Of the other six, one uses example wording alone and five combine choice and example wording. Across these cases, mention prevalence, semantic qualification and denominator size jointly determine what the comparison can support.
