# Reader C read log (Andersen, the Watchdogs & Reform)

Agent: Reader C. No web used. Nothing in `sources/` was edited.

## Fingerprints

All 15 files were checked with `sha256sum` against `sources/download_log.csv`. All matched.

| Manifest id | File | SHA-256 |
|---|---|---|
| hrg-hec-andersen-shredding | sources/05-hearings-enron/hhrg-107-80-destruction-of-enron-documents-by-andersen-2002-01-24.pdf | MATCH |
| hrg-hec-auditing | sources/05-hearings-enron/hhrg-107-83-lessons-learned-auditing-the-accounting-industry-2002-02-06.pdf | MATCH |
| batson-final-app-b-part1 | sources/02-bankruptcy-examiner/batson-final-appendix-b-andersen-part1-2003-11-04.pdf | MATCH |
| batson-final-app-b-part2 | sources/02-bankruptcy-examiner/batson-final-appendix-b-andersen-part2-2003-11-04.pdf | MATCH |
| andersen-scotus | sources/09-courts-doj/arthur-andersen-v-us-544-us-696-2005.html | MATCH |
| rpt-sga-watchdogs | sources/06-congressional-reports/sprt-financial-oversight-of-enron-sec-and-watchdogs.pdf | MATCH |
| hrg-sga-analysts | sources/05-hearings-enron/shrg-107-385-watchdogs-didnt-bark-analysts-2002-02-27.pdf | MATCH |
| gao-03-864 | sources/08-sox-law-pcaob-profession/gao-03-864-accounting-firm-consolidation.pdf | MATCH |
| gao-03-1158 | sources/08-sox-law-pcaob-profession/gao-03-1158-accounting-firm-consolidation-selected-data.pdf | MATCH |
| hrg-help-pensions | sources/05-hearings-enron/shrg-107-464-protecting-pensions-2002-02-07.pdf | MATCH |
| gao-02-480t-pensions | sources/05-hearings-enron/gao-02-480t-private-pensions-after-enron-2002-02-27.pdf | MATCH |
| sox-crs-summary | sources/07-sox-legislative-history/crs-rl31554-sox-summary.pdf | MATCH |
| sox-plaw-html | sources/08-sox-law-pcaob-profession/plaw-107-204-sarbanes-oxley-act.htm | MATCH |
| sec-press-2003-52 | sources/08-sox-law-pcaob-profession/sec-press-2003-52-pcaob-organized.htm | MATCH |
| sox-bush-remarks | sources/07-sox-legislative-history/wcpd-2002-bush-remarks-signing-sox-2002-07-30.pdf | MATCH |

## What I read (PDF page numbers; printed page in brackets)

Page offsets I worked out: shredding hearing, auditing hearing and HELP hearing: printed = PDF - 4. Watchdogs report: printed = PDF - 4. Batson App. B Part 1: printed = PDF - 2. Batson App. B Part 2: printed = PDF + 102 (Part 2 PDF 1 = printed 103). GAO-02-480T: printed = PDF - 1. GAO-03-864: body PDF 7 = printed 1.

- **hrg-hec-andersen-shredding** (text copy plus page images): PDF 6-7 [2-3] (Greenwood opening); 30-33 [26-29] (Duncan sworn and takes the Fifth; Greenwood's summary of the staff interview with Duncan); 34-36 [30-32] (panel sworn; Andrews oral testimony); 37-40 [33-36] (Andrews prepared statement); images of PDF 41-43 and 46-49 [37-45] (exhibits; the Oct 12, 2001 Temple e-mail is on PDF 49 [45], image only); 126 and 129-130 [122, 125-126] (Temple testimony); 172-173 and 181-182 [168-169, 177-178] (Andrews on the policy and fees). I also used keyword searches over the whole text copy.
- **hrg-hec-auditing**: PDF 73 [69] (Bono prepared statement); PDF 115-116 [111-112] and 119-120 (Longstreth oral and prepared). Keyword searches for fees and "non-audit".
- **batson-final-app-b-part1** (OCR from `work/ocr-tmp/`, finished during my run): OCR text of PDF 2-8, 11-12, 32, 45-46, 49, 61-66. **Checked against page images:** PDF 3, 4, 6, 7, 11, 12, 32, 45, 49, 61, 62, 63, 65. Every quote I used from this part was checked against the image.
- **batson-final-app-b-part2** (OCR, finished during my run): OCR text of PDF 1, 28-29, 64-66. **Checked against page images:** PDF 28, 29, 65.
- **andersen-scotus**: the whole file (Syllabus only).
- **rpt-sga-watchdogs**: PDF 8-11 [4-7] (introduction and summary); 26 [22] (Enron's auditor and fees); 32 [28] (SEC review, footnote 16); 36 [32] (1992 mark-to-market letter); 93 [89] (Nov 28 downgrades). Keyword searches elsewhere.
- **hrg-sga-analysts**: PDF 6 [2] (Lieberman opening); PDF 9 [5] (Thompson prepared statement). Keyword searches only elsewhere.
- **gao-03-864**: PDF 1-2 (cover, Highlights); 7-8 [1-2]; 18 [12]; 24-25 [18-19]; 107 [101] (Appendix III).
- **gao-03-1158**: PDF 1-2 (cover, Highlights).
- **gao-02-480t-pensions**: PDF 2-4 [1-3] (summary); 7-8 [6-7]; 12-13 [11-12] (lockdown, conclusions, n. 13).
- **hrg-help-pensions**: PDF 5 [1] (Kennedy); 23-24 [19-20] (Bentsen); 32 [28] (Chao prepared statement); 62-63 [58-59] (Lacey); 66-67, 69 [62-63, 65] (Fleetham); 74-75 [70-71] (Prentice).
- **sox-crs-summary**: PDF 1-3 (cover, Summary, Contents); PDF 5 [CRS-2]; PDF 16 [CRS-13].
- **sox-plaw-html**: header; Sec. 101(a)-(c) and (e); 201; 203; 302(a); 404; 802; 806(a). Text-copy lines 17-25, 371-460, 1694-1815, 2040-2080, 2793-2815, 3490-3540, 3656-3700.
- **sec-press-2003-52**: whole press release body.
- **sox-bush-remarks**: PDF 1-3 [pp. 1283-1285].

## Quote checks

Every quote was checked by script against the text copy. The exceptions: the Oct 12 e-mail (C-001) is an image-only page and was read from the image; C-041 leaves out a footnote marker. All other Batson quotes come from OCR text, and each was checked against its page image.
