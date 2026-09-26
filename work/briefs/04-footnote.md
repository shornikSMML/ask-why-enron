# Brief: Footnote Annotator

**Role:** Produce the content for "The Footnote" page. Show Note 16, "Related Party Transactions," from Enron's 2000 Form 10-K **in full**, annotated phrase by phrase the way an annotated edition explains a difficult poem. Follow `00-common-rules.md`.

**The text:** `sources/03-sec-filings/enron-10k-fy2000.txt`, lines 5863–5962 (Note 16). Also look at lines ~5130–5145, which refer to it. Copy the note's text **exactly** (verbatim, including the original line wording; you may join the lines within a paragraph).

**For each annotated phrase** (aim for 20–35 annotations covering every paragraph), write three short plain-language parts for a reader with no accounting background:
1. **What it said:** plain English.
2. **What it left out:** what a reader couldn't learn from it (for example that the "senior officer" was the CFO, Andrew Fastow; how much he earned; that the "Entities" were the Raptors; that the hedges were backed mainly by Enron's own stock). Every point must be supported by a cited library source.
3. **What the investigations found:** with citations (document, page or section, and the right verb).

**Sources:**
- `powers-report-sec`: the LJM1, LJM2, and Raptor sections, and especially the section on disclosure to investors (it discusses this very footnote). Add page numbers from `powers-report` (the PDF) where you can.
- `sec-fastow-complaint` (allegations about LJM and the Raptors).
- `batson-final`: its discussion of SPE and related-party disclosure (use the table of contents; OCR text in `work/text/batson-final.txt` when ready).
- `rpt-psi-board`: what the board was told or approved about LJM.

**Output:**
- `work/drafts/footnote.json`: `{"title": ..., "source": {...}, "paragraphs": [{"n": 1, "text": "verbatim paragraph", "annotations": [{"id": "fn-01", "phrase": "exact substring of the paragraph", "said": "...", "left_out": "...", "found": "...", "cites": [{"source_id": "...", "pdf_page": n|null, "loc": "...", "quote": "short verbatim"}], "glossary_terms": ["related-party-transaction"]}]}]}`. Every `phrase` must be an exact substring of its paragraph.
- `work/drafts/footnote-glossary-terms.md`: the terms the page needs defined.
- `work/facts/footnote-readlog.md` and `work/facts/footnote-gaps.md`.
