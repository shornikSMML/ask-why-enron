# Reader B (The People & the Law): read log

Agent: Reader B. Date: 2026-09-26. No web used. Nothing in `sources/` was edited.

## Fingerprints
For every file below, SHA-256 was computed with `sha256sum` and compared with `sources/download_log.csv`. **All matched.**

## What was read
"Lines" are line numbers in `work/text/<id>.txt`. "PDF p." is the page a viewer shows. Printed page numbers are in the fact cards where they are known.

| Manifest id | File | Read | Fingerprint |
|---|---|---|---|
| sec-fastow-complaint | 04-sec-enforcement/sec-v-fastow-complaint-2002.htm | Whole complaint (lines 1-305): summary, defendant, paras. 9, 14-66, claims | MATCH |
| sec-kopper-complaint | 04-sec-enforcement/sec-v-kopper-complaint-2002.htm | Whole complaint (lines 1-147) | MATCH |
| sec-skilling-causey-complaint | 04-sec-enforcement/sec-v-skilling-causey-complaint-2004.htm | Lines 1-90 (paras. 1-19); lines 229-260 (paras. 60-64); grep for resignation / insider trading | MATCH |
| sec-lay-complaint | 04-sec-enforcement/sec-v-lay-complaint-2004.pdf | PDF pp. 1-5 (paras. 1-9); pp. 32-33 (paras. 81-82); p. 41 (paras. 101-103) | MATCH |
| sec-glisan-complaint | 04-sec-enforcement/sec-v-glisan-complaint-2003.htm | Lines 1-60 (paras. 1-12); grep for plea/consent (none found) | MATCH |
| sec-merrill-complaint | 04-sec-enforcement/sec-v-merrill-lynch-complaint-2003.htm | Lines 1-80 (paras. 1-20); grep for settle/dates | MATCH |
| sec-duncan-complaint | 04-sec-enforcement/sec-v-duncan-complaint-2008.pdf | PDF pp. 1-3 and 15-16 (text layer); **page image p. 2 checked** | MATCH |
| sec-jpm-citi-press | 04-sec-enforcement/sec-press-2003-87-jpmorgan-citigroup.htm | Full press-release body | MATCH |
| sec-enron-spotlight | 04-sec-enforcement/sec-enron-spotlight-index.html | Whole enforcement-actions list (lines 1-140) | MATCH |
| doj-skilling-indictment | 09-courts-doj/doj-skilling-indictment-2004.pdf | PDF pp. 1-5 (intro, principal conspirators); p. 41 (Count Two heading); pp. 51-55 (insider-trading counts, forfeiture); **page images pp. 3 and 51 checked** | MATCH |
| doj-skilling-charged-press | 09-courts-doj/doj-press-2004-02-19-skilling-charged.htm | Whole release | MATCH |
| doj-lay-charged-press | 09-courts-doj/doj-press-2004-07-08-lay-charged.htm | Whole release | MATCH |
| ca5-skilling-2009 | 09-courts-doj/ca5-us-v-skilling-2009.pdf | PDF pp. 1-2 (lines 1-78); p. 6 (fn. 3); pp. 15-16 (II. Trial and Sentence, fn. 9); pp. 19-20 (Brown discussion, fn. 12); p. 60 (plea agreements); pp. 103-104 (sentencing, IX. Conclusion) | MATCH |
| skilling-scotus-2010 | 09-courts-doj/skilling-v-us-561-us-358-2010.pdf | PDF pp. 1-2 and 9 (Syllabus, Held, disposition); pp. 11-12 (Part I background); p. 15 (Causey plea); pp. 18-20 (verdict, sentence, CA5); p. 57 (remand) | MATCH |
| andersen-scotus | 09-courts-doj/arthur-andersen-v-us-544-us-696-2005.html | Syllabus opening and "Held" (lines ~1-45) | MATCH |
| batson-final-app-d | 02-bankruptcy-examiner/batson-final-appendix-d-lay-skilling-outside-directors-2003-11-04.pdf | OCR text PDF pp. 1-15 (title, TOC, Introduction incl. Conclusions, Lay/Skilling biographies); pp. 32-35 (outside director chart); pp. 180-182 (VII. Conclusions). **Page images checked: pp. 1, 3, 5, 6, 7, 8, 9, 13, 34, 181.** | MATCH |
| rpt-psi-board | 06-congressional-reports/sprt-107-70-role-of-board-report.pdf | PDF pp. 5-8 (investigation, witnesses, findings, recommendations); p. 18 (directors' response); pp. 20-21 (Feb 1999 Audit Committee, Duncan note); p. 23 (Jaedicke); pp. 28, 30 (LJM approvals); pp. 53-54 (Lay credit line) | MATCH |
| hrg-psi-board | 05-hearings-enron/shrg-107-511-role-of-board-2002-05-07.pdf | PDF pp. 23-29 (oath, statements of J. Duncan, Winokur); p. 36 (Blake); pp. 41-42 (Jaedicke questioning) | MATCH |
| hrg-commerce-skilling-watkins | 05-hearings-enron/shrg-107-1141-collapse-of-enron-corp-2002-02-26.pdf | PDF pp. 14-16 (oath, Watkins statement); pp. 22-23 (Skilling statement); p. 25 and p. 48 (Q&A on Watkins memo) | MATCH |
| hrg-commerce-lay-powers | 05-hearings-enron/shrg-107-773-collapse-of-enron-2002-02-12.pdf | PDF pp. 29-32 (Lay oath and Fifth Amendment statement; Powers statement) | MATCH |
| hrg-hec-andersen-shredding | 05-hearings-enron/hhrg-107-80-destruction-of-enron-documents-by-andersen-2002-01-24.pdf | PDF pp. 30-31 (David Duncan sworn, invokes Fifth) | MATCH |
| hrg-hfs-enron-investors | 05-hearings-enron/hhrg-107-51-pt2-enron-collapse-investors-2002-02-04.pdf | PDF pp. 124-126 (Berardino sworn, statement); date headings (lines 150-190, 6912) | MATCH |

## Notes on scope
- `hrg-hec-andersen-shredding`, `hrg-hfs-enron-investors` and `andersen-scotus` are not in my brief's document list. I used them only for David Duncan and Joseph Berardino, who are on the brief's list of people and whose testimony is in no listed document. I read only the pages above.
- `batson-final-app-d`: the OCR text was a 3-page stub when I started. The full OCR (254 pages) arrived during the work (`work/ocr.log`: "batson-final-app-d done"). I read it last, as instructed.
- The text layers of `doj-skilling-indictment` and `sec-duncan-complaint` are noisy publisher OCR. I checked every quote from them against the page image. The cards set `from_ocr: true` for these.
