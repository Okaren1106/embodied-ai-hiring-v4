# Supplementary Material

## A. Supplementary results and reproducibility

The supplementary package provides the scenarios and contextual evidence underlying the reported comparisons. Supplementary Table S7 reports every engineering-decomposition scenario, including source screens under which the Galbot–Figure comparison is unavailable because Galbot does not pass the screen. Supplementary Table S8 reports all 20 technology-case scenarios with small-sample marks, unresolved counts and assignment bounds.

[[S3]]

[[T5]]

The contextual evidence archive links 248 task advertisements to 496 advertisement–technology pairs and 456 retained evidence records. Each record preserves a stable advertisement identity, observation version, technology excerpt, its parent sentence or list item, heading position and other relevant evidence from the same advertisement. The three source-text fields used in the analysis are retained. Chinese-language source evidence remains in Chinese. In the article and supplement, quotations translated from Chinese are identified by advertisement ID and as translations, with choice, example and scope language preserved. English-language advertisements remain verbatim.

The reproduction program checks the input manifest and rebuilds the derived analyses, the 15 source-table files and the contextual evidence exports from supplied comma-separated-value (CSV) files and finalized coded records. Its base computation uses Python 3.10 or later and the standard library; optional figure reproduction also requires matplotlib, numpy and an available Chinese font. Reproduction rebuilds links and numerical summaries from those records without repeating semantic coding or assessing coding reliability. The package accompanies the manuscript, and `SUPPLEMENT_GUIDE.md` describes its files and the command for a fresh output directory.
