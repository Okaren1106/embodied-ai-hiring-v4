# Work organization and technology qualifications in embodied AI hiring

[中文](README.md) · [Methods and data](docs/METHODS_AND_DATA.md) · [Reproduction](docs/REPRODUCTION.md) · [Publication scope](docs/PUBLICATION_SCOPE.md)

This project studies how embodied AI companies organize work through recruitment and how their advertisements express technology qualifications. It combines a **1,654-advertisement corpus from 24 recruitment entities** with a paired analysis of **248 advertisements and 496 advertisement–technology records**.

The broad study examines primary job functions, activities crossing functional boundaries, work objects, and company differences. The V4 paper asks **what counts as a technology qualification**: a name anywhere in the advertisement, a name in qualification text, or an unconditional technology-specific statement. It shows that these definitions can change the ordering of technologies in the same advertisements.

This repository publishes the complete research package through **V4.0, before the project moved to application-form research**. It includes the original broad study, papers, supplements, captured source text, coding rules, evidence, revision records, analysis code, results, and preceding English manuscript versions.

## Read the research

|Material|Link|
|---|---|
|V4 paper: *What Counts as a Technology Qualification in Embodied AI Hiring?*|[Markdown](paper_v4/release/Research_Working_Manuscript.md) · [Integrated PDF](paper_v4/release/IJM_Research_Reading_Copy.pdf) · [Word](paper_v4/release/IJM_Research_Reading_Copy.docx)|
|V4 supplement|[Markdown](paper_v4/release/Research_Working_Supplement.md) · [PDF](paper_v4/release/IJM_Research_Supplement.pdf) · [Word](paper_v4/release/IJM_Research_Supplement.docx)|
|Broad study, Chinese report|[Markdown](broad_study/REPORT_Astra_final.md) · [PDF](broad_study/document/Astra_final_report.pdf)|
|Detailed explanation in Chinese|[Research questions, methods and findings](docs/研究内容与主要发现.md)|
|Analysis and evidence|[Broad study](broad_study/) · [V4 paired study](paper_v4/)|
|Version history|[Earlier manuscripts](history/) · [Original release archives](archives/)|

## Data and design

The corpus contains two collection waves: 610 advertisements from eight companies captured on 31 August 2026, and 1,044 from 16 additional entities captured on 11 September. Twenty-three entities are company-level recruitment scopes, totaling 1,630 advertisements; Amazon FAR is a separately recorded team with 24 advertisements. Each observation preserves the organization, source job identifier, text version, and source evidence.

The project assigns each advertisement a primary function based on its main continuing deliverable and records multiple activities separately. Qualification analysis covers 1,576 advertisements in 17 concrete functions, using a 354-item catalogue and 22 context cells. The coding distinguishes work responsibilities, general requirements, explicitly required qualifications and preferred qualifications, together with example, choice and conditional relations.

V4 pairs two fixed technologies in each advertisement: Python and PyTorch in 105 robot-learning/model-development advertisements; C++ and Linux in 87 robotics-related software advertisements; and Altium and EMC/SI/PI in 56 board-circuitry advertisements. The software task includes relevant product-stack and infrastructure roles. Three nested textual layers are constructed: **M**, technology mention; **H**, occurrence in general or required qualification context; and **Q**, confirmed unconditional technology-specific qualification expression. Additional constructs admit recorded examples or choices.

Sensitivity analyses use common-mention subsets, firm-equal weights, exact-text and local-clause template weights, leave-one-firm-out calculations, recorded-unknown assignment ranges, and 128 saved semantic readings. An exploratory PyTorch–TensorFlow extension compares technologies of the same class. Source interpretation is model assisted; deterministic Python workflows and separate numerical implementations reproduce the encoded results.

## Main findings

**Work activities cross job-function boundaries.** Of 66 advertisements with research activity, 48 (72.7%) sit outside the research-science primary function. Of 459 advertisements with broad quality activity, 300 (65.4%) sit outside manufacturing, quality and supply chain. Job titles and primary functions capture only part of the work organization.

**Company-wide differences can be driven by job composition.** Across four common functions, Galbot's engineering-activity share exceeds Figure's by 11.10 percentage points. Composition contributes +19.45 points and within-function differences contribute −8.35. Equal weighting of those four functions changes the gap to −9.16 points.

**Qualification definitions change technology rankings.** In the same 105 robot-learning advertisements:

|Construct|Python positives|PyTorch positives|Python minus PyTorch, pp|
|---|---:|---:|---:|
|Mention M|73|83|−9.5|
|Qualification context H|67|79|−11.4|
|Unconditional target-specific Q|42|22|+19.0|
|Q plus all recorded examples|43|65|−21.0|
|Q plus choices and all recorded examples|50|75|−23.8|

The unconditional Python-minus-PyTorch assignment range is +13.3 to +35.2 points; admitting all recorded examples changes it to −24.8 to −4.8. Examples account for much of the difference: a framework named as one example of a class expresses a different qualification relationship from an unqualified statement naming that framework.

**Pairing within advertisements preserves the construct problem.** Among 66 advertisements naming both technologies, qualification-context counts are similar (60 versus 62), but unconditional counts are 37 versus 18. Admitting examples gives 38 versus 51, with a recorded-unknown difference range crossing zero. Keeping the document fixed still leaves the meaning of the qualification measure to be specified.

**Other technology pairs follow different transitions.** C++ is more frequently mentioned than Linux, while Linux has more confirmed unconditional qualifications. Board-circuitry advertisements distinguish named design tools from engineering method families. PyTorch and TensorFlow have equal confirmed relation counts in the 26 advertisements naming both, despite very different visibility across the full task sample.

The findings support a practical approach to vacancy measurement: identify the work domain, preserve the qualification relationship, and assess firm composition and repeated text before interpreting technology rankings. For recruitment practice, explicit treatment of mandatory skills, acceptable substitutes and illustrative tools clarifies what an applicant is expected to bring.

## Reproduce

V4 numerical reproduction requires Python 3.12+ and the standard library:

```bash
git clone https://github.com/Okaren1106/embodied-ai-hiring-v4.git
cd embodied-ai-hiring-v4
python tools/reproduce.py v4
```

Large broad-study tables are losslessly compressed. Restore them and reproduce the broad study with:

```bash
python tools/restore_large_files.py
python tools/reproduce.py broad
```

See the [reproduction guide](docs/REPRODUCTION.md) for storage needs, optional dependencies and independent checks. File hashes and source provenance are recorded in the root manifests.

## Interpretation and version

The unit is a captured advertisement, and the two purposive waves describe the selected organizations. Semantic coding has no independent human double-coding reliability estimate; assignment ranges quantify recorded uncertainty. An inconsistent historical deployment-activity measure was withdrawn and its record is retained. Archived papers preserve their original working-paper status. V4 is the current version of the technology-pair analysis in this release.

Public release: 9 October 2026. See [publication scope and citation](docs/PUBLICATION_SCOPE.md).
