# English document build

Run from the English release root with Python 3.10 or later:

```text
python -m pip install -r authoring/requirements.txt
python authoring/make_figures.py
python authoring/build_documents.py
```

The first program redraws the English figures from retained fixed inputs, changing labels and layout only. The second builds four DOCX files, Markdown counterparts, English table CSV/JSON files, and figure aliases. The numerical analysis reproduction command is separately documented in SUPPLEMENT_GUIDE.md.

The English build was verified with python-docx 1.2.0 and matplotlib 3.11.2. PNGs use 400 dpi and PDF/SVG retain vector graphics. Font and renderer versions can change pagination and image bytes. The supplied PDFs were exported by Microsoft Word and inspected page by page; regenerate and inspect them after editing. No research coding is rerun by these document programs.

On Windows with Microsoft Word installed, `authoring/export_pdf.ps1` exports the four PDFs from isolated temporary copies and records Word page/word statistics. It requires an interactive user session for Word COM automation.
