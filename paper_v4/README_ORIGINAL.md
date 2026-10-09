# IJM technology qualification research upgrade v4

This private research package extends the v3 study. The original corpus and v3 archive remain unchanged. The current manuscript is written by the requested GPT-5.6 Sol agent and revised against the actual analyses and source audits. Publisher-policy processing and author metadata will be handled by the human author, as instructed; no submission has been made.

## Read the paper

- `release/IJM_Research_Reading_Copy.docx`: integrated article with tables and figures.
- `release/IJM_Main_Working_Text.docx`: article with insertion markers and figure captions.
- `release/IJM_Research_Tables.docx`: the three main tables, separately editable.
- `release/IJM_Research_Supplement.docx`: definitions, source decisions and additional results.
- `release/Research_Working_Manuscript.md` and `Research_Working_Supplement.md`: editable text sources.
- `release/figures/`: PDF/SVG vector figures and PNG previews.
- `release/研究升级与投稿准备说明.md`: Chinese guide to the changes, results and remaining evidence limits.

The final reading/main/tables/supplement documents have 14/13/3/7 pages. The main Word count plus five 280-word object allowances is approximately 6,926 words; the structured abstract including keywords and classification has 215 words. Final acceptance covers all 37 rendered pages, 10 numerical tables and 141 document-content checks. Review hashes are in `verification/`.

The files remain research working manuscripts until the author finishes the author-controlled submission steps. Their source-interpretation evidence is model-assisted; independent code checks are not described as independent human coding.

## What changed scientifically

The study now compares technology visibility M, GENERAL/REQUIRED qualification context H and unconditional target-specific qualification expression Q. It distinguishes uncertainty within a construct from changing which relations the construct includes. Same-advertisement contrasts, common-mention subsets, complete joint states, firm and template weights, source reviews and classification-breakdown distances replace reliance on a small collection of company rankings.

Seven declared source corrections produce 169 Q positives, 284 nonpositives and 43 unresolved pairs on the unchanged 496-row main frame. Complete reviews cover the 46 previously unresolved pairs, the expanded-numerator source cases and cue-free peer-framework lists. A separate PyTorch–TensorFlow extension adds a same-class comparison in the same 105 robot-model advertisements. It is an exploratory boundary check, not an independent replication. The stage memos in `stages/` record each improvement and the changes it made to the whole-paper argument.

## Reproduce the numbers offline

Use standard Python 3.12 or later from any working directory:

```text
python REPRODUCE.py
```

The entry point verifies the packaged input hashes, applies the declared overlay in a new derived file, generates numerical outputs and runs separate implementations of the key calculations. It requires no network connection and no access to the original research repository. `source_snapshot/` holds 16 immutable v3 inputs. `data/` holds the declared v4 corrections and their phase history. Source-review notes are explicit inputs in `work/literature_validation/` and `extensions/framework_control/data/`; running the scripts checks and aggregates these saved decisions, rather than generating new semantic judgments.

`work/verify_isolated.py` recreates the entry point in a fresh directory and compares its generated CSV/JSON outputs byte for byte. `work/check_protected_sources.py` is a separate workspace audit of all 767 original v3 files and requires the adjacent historical v3 directory; it is not a dependency of numerical reproduction.

The final isolated run reproduced all 89 generated CSV/JSON outputs byte for byte. `work/package_release.py` makes the private ZIP, verifies every member and repeats the same numerical entry point from the extracted archive. Its receipt, `verification/final_package_verification.json`, is outside the archive so its archive checksum is not self-referential. `PACKAGE_MANIFEST.json` inside the archive lists every other member with its SHA-256 hash. Temporary Word exports, page images and isolated build directories are omitted from the portable ZIP; their compact acceptance reports are included.

Figures are optional: `work/make_research_figures.py` requires matplotlib. Word authoring is optional: `work/build_documents.py` requires python-docx. The delivered documents were produced with the Codex bundled runtime. On this Windows host, LibreOffice was absent; local Word was used invisibly for PDF export, followed by bundled PDFium page rendering. Render images and logs are internal verification artifacts, not research observations.

## File map and evidence limits

`analysis/paired/` contains the main contrasts, scope states and weights. `analysis/empirical/` contains company comparisons, exact local-template results, hypothetical editing distances and independent audits. `analysis/example_increments/` contains source-level expansion and cue admission analyses. `extensions/framework_control/` contains the TensorFlow extension and its source annotations. `literature/` records primary-source references and what was actually read. `audit/` preserves conceptual and source challenges. `verification/` contains hashes, reproduction and document checks.

The finite corpus is purposively captured. Bounds assign recorded unresolved states and are not confidence intervals, population estimates or guarantees against resolved-label error. The explicit relation sets and coupled readings are named assumptions. No regression identifies technology demand, no actual recruiter screening outcome is observed, and the many computational checks do not estimate semantic accuracy. Existing historical results remain identifiable as historical; the current article uses the seven-correction v4 layer.

`audit/final_whole_paper_review.md` explains the scientific stopping decision. Further progress would require independent semantic or behavioral evidence. This release closes the present research upgrade, without claiming that the topic cannot be improved or that the journal has accepted it. The initial quick-review draft under `review/supporting/` is a historical intake record, not a final exhaustive referee report.

The package contains captured third-party source text and private research records. It has not been publicly archived or pushed to the separately published pipeline repository.
