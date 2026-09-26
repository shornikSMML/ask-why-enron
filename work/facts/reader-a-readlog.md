# Reader A read log (The Company & the Accounting)

Agent: Reader A. No web used. Nothing in `sources/` was edited.

## Fingerprints (SHA-256 vs `sources/download_log.csv`)

All files I relied on were re-checked with `sha256sum`. **All matched.**

| Manifest id | File | Result |
|---|---|---|
| powers-report-sec | sources/01-internal-investigation/powers-report-sec-exhibit-99-2.txt | MATCH |
| powers-report | sources/01-internal-investigation/powers-report-2002-02-01.pdf | MATCH (used only for PDF page numbers, via work/text/powers-report.txt) |
| enron-10k-2000 | sources/03-sec-filings/enron-10k-fy2000.txt | MATCH |
| enron-10q-q3-2001 | sources/03-sec-filings/enron-10q-2001-09-30.txt | MATCH |
| enron-8k-nov-2001 | sources/03-sec-filings/enron-8k-2001-11.txt | MATCH |
| enron-8k-nov-2001-ex99-1 | sources/03-sec-filings/enron-8k-2001-11-08-ex99-1-press-release.txt | MATCH |
| enron-8k-dynegy-merger | sources/03-sec-filings/enron-8k-2001-11-09-dynegy-merger.txt | MATCH |
| batson-1st-interim | sources/02-bankruptcy-examiner/batson-first-interim-report-2002-09-21.pdf | MATCH |
| batson-final | sources/02-bankruptcy-examiner/batson-final-report-2003-11-04.pdf | MATCH |
| batson-final-app-a | sources/02-bankruptcy-examiner/batson-final-appendix-a-defined-terms-2003-11-04.pdf | MATCH |
| rpt-jct-vol1 | sources/06-congressional-reports/jcs-3-03-vol1-jct-enron-tax-report.pdf | MATCH |
| rpt-psi-fishtail | sources/06-congressional-reports/sprt-107-82-fishtail-bacchus-sundance-slapshot.pdf | MATCH |
| sec-kopper-complaint | sources/04-sec-enforcement/sec-v-kopper-complaint-2002.htm | MATCH |
| rpt-psi-board | sources/06-congressional-reports/sprt-107-70-role-of-board-report.pdf | MATCH (one paragraph, size-ranking test) |
| doj-skilling-indictment | sources/09-courts-doj/doj-skilling-indictment-2004.pdf | MATCH (para. 1 only, size-ranking test) |

## What I read

**powers-report-sec** (text lines; printed pages; PDF page = printed + 6, checked at printed pp. 3, 43, 87, 100, 125, 133, 200)
- Lines 1-300: cover letter, table of contents.
- Lines 302-1453: Executive Summary and Introduction, printed pp. 1-35 (all).
- Lines 1454-2607: I. Background; II. Chewco A-H, printed pp. 36-67 (all; revenue-recognition section F read only to p. 57).
- Lines 2608-2880: III. LJM history and governance, pp. 68-76.
- Lines 2881-3148, 3240-3300, 3425-3470: IV. Rhythms, pp. 77-88, 92-93.
- Lines 3590-3739: V. Raptors intro and Raptor I start, pp. 97-101.
- Lines 4083-4110, 4191-4225, 4341-4475: Raptors II/IV, III, restructuring, pp. 111, 114-115, 119-122.
- Lines 4557-4856: V.E-F Unwind and Conclusions on the Raptors, pp. 125-134.
- Lines 5329-5380, 5895-5945: VII.A board oversight intro and Fastow compensation, pp. 148-149, 163-165.
- Lines 7134-7230: VIII.E Conclusions on Disclosure, pp. 200-203 (skipped VIII.D, Note 16: Footnote Annotator's).
- Lines 7480-7574: Timeline appendix (2000-2001).
- Grep only (not read in full): section VII.C Watkins letter (for Reader B), VI other LJM transactions.

**powers-report** (PDF text `work/text/powers-report.txt`): page-marker lookups only, to map printed to PDF pages.

**enron-10k-2000** (text lines)
- 1-30 (cover), 93-150 (TOC), 155-354 (Item 1 General, segments, pipelines), 488-640 (Wholesale Services, EnronOnline), 1936-1980 (Item 6 Selected Financial Data), 2335-2345, 2385-2432, 2515-2528 (MD&A), 3700-3790 (Andersen report, income statement), 4150-4200 (Note 1 price risk management / mark-to-market). Note 16 skipped.

**enron-10q-q3-2001** (text lines; printed page numbers are at page bottoms)
- 100-250 (explanatory note, income statement; pp. 3-4), 545-625 and 700-900 (Note 2 recent events, liquidity, Dynegy merger, SEC investigation; pp. 9-14), 932-1180 (Note 3 restatement; pp. 15-18), 2965-3040 (MD&A net income; p. 44), 3325-3375, 3665-3680 (pp. 49, 53).

**enron-8k-nov-2001**: lines 1-50, 144-260 (Table 1, p. 4), 415-470 (pp. 9-10), 855-932 (pp. 18-20).

**enron-8k-nov-2001-ex99-1**: whole document (141 lines).

**enron-8k-dynegy-merger**: whole document (185 lines). Contains no merger terms; exhibits are not in the library.

**batson-final** (OCR text `work/text/batson-final.txt`, PDF p. = printed p. + 3)
- OCR text PDF pp. 1-25 (TOC, I. Introduction, Summary of Conclusions, II. Background, III.A overview incl. six techniques).
- Page images checked: PDF pp. 4, 12, 18, 19, 21, 22, 23, 24.

**batson-final-app-a** (OCR text; PDF p. = printed p. + 1): grep of definitions; page images checked: PDF pp. 8, 9, 11, 12.

**batson-1st-interim**: OCR not ready, so read page images directly: PDF pp. 1-11 and 13-16 (TOC; I.A-D Introduction; II.A Executive Summary start). PDF p. = printed p. + 2.

**rpt-jct-vol1**: OCR not ready, so read page images directly: PDF pp. 5-11 (front matter, contents), 80 (to find page offset), 85-93 (Part Two II.A-B.3, printed pp. 57-65), 110-115 (II.C.3-5, printed pp. 82-87). PDF p. = printed p. + 28.

**rpt-psi-fishtail** (text `work/text/rpt-psi-fishtail.txt`): PDF pp. 3-7 (contents, introduction, summary of transactions; printed pp. 1-3). PDF p. = printed p. + 4.

**sec-kopper-complaint** (text `work/text/sec-kopper-complaint.txt`): para. 9 only.

**rpt-psi-board**: PDF p. 10 (printed p. 6), one paragraph. **doj-skilling-indictment**: PDF p. 1, para. 1.

## Searches run
- `grep -il "seventh.largest|7th largest"` across work/text and sources (size-ranking tip).
- `grep -il buffett work/text/*.txt sources/*/*.txt` (run once, as instructed; result in final report).
