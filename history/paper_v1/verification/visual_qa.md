# Final visual verification

Date: 2026-09-21. All 38 pages of the four final English documents were inspected as individual full-size page images. Contact sheets were used only for navigation and preliminary checks.

| Document | Pages inspected | Reviewer |
| --- | --- | --- |
| English_Manuscript_IJM | 1–14 | Coordinating editor, Astra |
| IJM_Main_Text | 1–12 | GPT-5.6 Sol, separate final visual pass |
| IJM_Tables | 1–5 | Coordinating editor, Astra |
| Supplementary_Material | 1–7 | GPT-5.6 Sol, separate final visual pass |

The secondary review is recorded in visual_qa_secondary.md. These are document-production checks, not independent research coding or semantic validation.

## Rendering and checks

The document skill's canonical renderer was attempted but could not run because its LibreOffice dependency was unavailable in this Windows runtime. Microsoft Word instead exported PDFs from isolated temporary copies of the DOCX files. The four PDFs were rendered with pypdfium2 at scale 1.6; page counts were checked against Word's own statistics. The supplied DOCX files were not modified by PDF export.

Every final page was checked for clipping, overlapping text, missing glyphs, broken equations, overflowing columns, displaced rows, detached section headings or captions, page numbering, and visible editing residue. The three English figures were also inspected individually. Equations are native editable Word math; tables contain editable cells. Split supplementary tables repeat their headers. No blocking visual defect remains.

Earlier figure-legend crowding, equation-bracket rendering, and awkward header wrapping were corrected before the final review. The full 19-row Table I fits on reader page 5 and on separate-tables page 1. The reader's Table I note continues on page 6. Supplementary Table S2 ends on page 1, and its complete note starts on page 2; this is a minor continuity limitation, with no missing content or ambiguous intervening table. The final reference and figure-caption pages have intentional remaining whitespace.

Seven centered insertion callouts remain only in IJM_Main_Text because its tables and figures are supplied separately. These are publishing placement instructions, not drafting prompts. The complete reader manuscript contains the displays themselves and has no such callouts. No model-role labels or editing instructions appear in the manuscript prose.

## Limits

Pagination was verified using the installed Microsoft Word renderer. Other Word versions and font substitutions can change pagination. This review does not certify PDF accessibility, font embedding, journal acceptance, authorship declarations, or publisher eligibility for the recorded editorial assistance.
