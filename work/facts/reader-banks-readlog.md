# Reader E (The Banks): read log

Agent: Reader E: The Banks. Date: 2026-09-27. No web used. Nothing in `sources/` was edited.

## Fingerprints
For every file below, SHA-256 was computed with `sha256sum` and compared with `sources/download_log.csv`. **All matched.**

## OCR run
`batson-final-app-e`, `-app-f` and `-app-g` had no OCR text yet (only empty page markers). I ran `work/tools/ocr.sh` on each (output to `work/text/<id>.txt`, logged in `work/ocr.log`: app-e 102 pages, app-f 100 pages, app-g 68 pages). Every quote taken from an OCR text (Batson Final Report and Appendices E, F, G) was checked against the page image with the Read tool.

## What was read
"Lines" are line numbers in `work/text/<id>.txt`. "PDF p." is the page a viewer shows.

| Manifest id | File | Read | Fingerprint |
|---|---|---|---|
| rpt-psi-fishtail | 06-congressional-reports/sprt-107-82-fishtail-bacchus-sundance-slapshot.pdf | Whole report (PDF pp. 1-41; lines 1-2281). Printed page = PDF page minus 4 | MATCH |
| hrg-psi-banks-v1 | 05-hearings-enron/shrg-107-618-v1-role-of-financial-institutions.pdf | Text layer: PDF pp. 19-21 (July 23 opening, Levin); pp. 31-35 (oath; Roach testimony); pp. 47-48 (Stumpp); pp. 76-81 (Chase panel oath, Dellapina statement, questioning on Chase email); pp. 109-112 (Citigroup panel oath, Bushnell, start of Caplan); pp. 179, 189-192 (July 30 opening; Furst, Tilney, Martin). Grep for "prepa", "loves these", "oath/sworn" | MATCH |
| hrg-psi-banks-v2 | 05-hearings-enron/shrg-107-618-v2-role-of-financial-institutions.pdf | PDF pp. 1-4 only (title, contents, witness list); it is the exhibits/appendix volume. Grep for "loves these" (no hits) | MATCH |
| sec-jpm-citi-press | 04-sec-enforcement/sec-press-2003-87-jpmorgan-citigroup.htm | Whole release body (line 248) | MATCH |
| sec-merrill-complaint | 04-sec-enforcement/sec-v-merrill-lynch-complaint-2003.htm | Whole complaint (lines 1-260, paras. 1-69 and prayer) | MATCH |
| sec-enron-spotlight | 04-sec-enforcement/sec-enron-spotlight-index.html | Lines 1-135 (enforcement list); grep for banks | MATCH |
| ca5-skilling-2009 | 09-courts-doj/ca5-us-v-skilling-2009.pdf | PDF pp. 19-20 (lines 688-716, Brown fn. 12); pp. 60-61 (lines 2340-2380, plea agreements) | MATCH |
| batson-final | 02-bankruptcy-examiner/batson-final-report-2003-11-04.pdf | OCR text: PDF pp. 7-9, 15-17, 20, 24-25; 66-84 (Sections VII-VIII, all three banks); 96-99, 104-107 (Section IX). **Page images checked: 7, 8, 15, 16, 20, 66, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 97, 98, 104, 105, 106** | MATCH |
| batson-final-app-e | 02-bankruptcy-examiner/batson-final-appendix-e-rbs-2003-11-04.pdf | OCR text: PDF pp. 1-6 (title, TOC, Introduction and Overview); pp. 99-102 (end of IV.B, IV.C Conclusions). **Page images checked: 5, 6, 101, 102** | MATCH |
| batson-final-app-f | 02-bankruptcy-examiner/batson-final-appendix-f-csfb-2003-11-04.pdf | OCR text: PDF pp. 2, 4-8 (TOC, Introduction); p. 35 (Conclusions regarding CSFB's analysts); pp. 95-100 (IV.C Conclusions; V preference). **Page images checked: 5, 35, 95, 96** | MATCH |
| batson-final-app-g | 02-bankruptcy-examiner/batson-final-appendix-g-toronto-dominion-2003-11-04.pdf | OCR text: PDF pp. 2-6 (TOC, Introduction); pp. 64-68 (end of IV.B, IV.C Conclusions, V preference). **Page images checked: 4, 6, 64, 65** | MATCH |

Note: the brief asked for the "conclusions sections only" of Appendices E, F and G. I also read each appendix's short Introduction and Overview (which summarizes the conclusions and gives the dollar effects) and, in App. F, the separate "Conclusions regarding CSFB's Securities Analysts". I did not read the detailed transaction sections.

## Existing cards checked to avoid duplicates
A-070, A-071, A-072, A-073, A-074, A-087, B-040, B-048, B-083, B-084, B-085, B-086, C-059. New cards refer to these in their notes rather than repeating them.

## Websites used
None.
