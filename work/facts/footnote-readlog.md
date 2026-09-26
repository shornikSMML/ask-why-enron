# Footnote Annotator: read log

The fingerprint of every file below was checked with `sha256sum` against `sources/download_log.csv` before use. All matched.

| manifest id | file | fingerprint | what was read |
|---|---|---|---|
| enron-10k-2000 | sources/03-sec-filings/enron-10k-fy2000.txt | MATCH | Note 16, lines 5863-5962 (the whole note); Note 15 references, lines 5125-5160; officers list, lines 1500-1508; signature page, lines 6335-6362; Item 13 heading (line 3281) |
| powers-report-sec | sources/01-internal-investigation/powers-report-sec-exhibit-99-2.txt | MATCH | Table of contents, lines 90-295; Summary lines 360-470, 660-900, 1095-1103; IV Rhythms, lines 2881-3010 and 3240-3500 (printed pp. 77-94); V Raptors, lines 3590-3870, 4040-4300, 4341-4425, 4557-4612 (pp. 97-126); VI Other LJM transactions, lines 4848-4900 and 5160-5330 (pp. 134-147); VIII Related-Party Disclosure Issues, lines 6372-6590 and 6860-7250 (pp. 178-184, 192-203); Appendix B timeline, lines 7440-7574 |
| powers-report | sources/01-internal-investigation/powers-report-2002-02-01.pdf | MATCH | Not read page by page. Used `work/text/powers-report.txt` only to map quotes to PDF page numbers. The offset is PDF page = printed page + 6 throughout the body; Appendix B's Jan-June 2000 timeline is PDF p. 216 |
| sec-fastow-complaint | sources/04-sec-enforcement/sec-v-fastow-complaint-2002.htm | MATCH | Text copy `work/text/sec-fastow-complaint.txt`, whole complaint (305 lines), paragraphs 1-77 |
| rpt-psi-board | sources/06-congressional-reports/sprt-107-70-role-of-board-report.pdf | MATCH | Text copy, PDF pp. 22-23 (Andersen Feb. 2001 e-mail), 28-30 (board approval of LJM), 36-37 (oversight of Fastow's compensation), 51-52 (Raptors; Inadequate Public Disclosure; Watkins letter). Printed page = PDF page - 4 |
| batson-final | sources/02-bankruptcy-examiner/batson-final-report-2003-11-04.pdf | MATCH | OCR text `work/text/batson-final.txt` (complete, 140 pages): searched throughout; read PDF pp. 1-2 (TOC), 6, 11-13, 21-25, 42-48. **Page images checked by eye** for every quote used: PDF pp. 6, 12, 13, 22, 23, 24, 42, 47, 48. Printed page = PDF page - 3 |
| enron-8k-nov-2001 | sources/03-sec-filings/enron-8k-2001-11.txt | MATCH | Lines 1-140 and 410-800 (LJM section, Table 2 notes, sections C-H). Not named in the brief; used because it is Enron's own later, fuller description of the same transactions |
| enron-10q-q3-2001 | sources/03-sec-filings/enron-10q-2001-09-30.txt | MATCH | Fingerprint only; not read |

## Method notes
- All 125 quotations in `work/drafts/footnote.json` were checked automatically against the source text (whitespace and quote marks normalized). Batson quotations come from OCR text and were also compared with the page images.
- Paragraph text of Note 16 was copied from the 10-K programmatically: lines were joined and runs of spaces collapsed. There are no other changes.
- No web use.
