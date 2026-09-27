# Reader B follow-up: read log

Agent: Reader B (follow-up, brief 14). No web used. Cards: `work/facts/reader-followup.json` (F-001 to F-015).

## Fingerprints (sha256sum compared with the `sha256` column of the same file's row in `sources/download_log.csv`)
All matched: rpt-psi-board, batson-1st-interim, batson-final, batson-final-app-d, powers-report-sec, enron-10k-2000, enron-10q-q3-2001, hrg-hec-andersen-shredding, hrg-hec-collapse-pt1, hrg-hec-collapse-pt2, hrg-hec-collapse-pt3, hrg-hec-collapse-pt4, hrg-commerce-skilling-watkins, hrg-commerce-lay-powers, hrg-psi-board, rpt-sga-watchdogs, skilling-scotus-2010, ca5-skilling-2009.

## Pages and lines read
| Document | What was read |
|---|---|
| rpt-psi-board | text PDF pp. 16, 27-28, 49-52 (printed 12, 23-24, 45-48); page images PDF 61-63 (App. 2, the Watkins letter; no text layer) |
| batson-1st-interim | OCR text PDF pp. 1-4; **page image PDF 4 (printed p. 2) checked**: the Lay quote matches exactly |
| batson-final | OCR text lines 900-921; **page image PDF 22 (printed p. 19, n. 41) checked** |
| batson-final-app-d | grep hits only (names list, line 211; Whalley 1075-1083; Buy 2740 ff.) |
| powers-report-sec | lines 395-412 (p. 4), 590-630 (pp. 9-10), 1268-1305 (pp. 30-31), 1715-1760 (p. 44), 2135-2150 (p. 54), 2630-2745 (pp. 69-72), 3140-3262 (pp. 84-87), 4530-4626 (pp. 124-127) |
| enron-10k-2000 | grep for gross/revenue terms; lines 4151-4171 (Accounting for Price Risk Management) |
| enron-10q-q3-2001 | lines 2465-2482 (p. 37, Note 12) |
| hrg-hec-collapse-pt2 | PDF pp. 25-27 (printed 21-23), text lines 1455-1580; lines 4670-4705 (printed 76-77) |
| hrg-hec-collapse-pt3 | page images PDF 72-74, 121-122, 134-135 (checked). Scratch OCR of image-only exhibit pages PDF 72-326 was used for searching only |
| hrg-hec-collapse-pt4 | text lines 3180-3330 (Stupak reading the letter); page images PDF 120-121 (checked). Scratch OCR of image-only pages PDF 96-451 was used for searching only |
| hrg-hec-andersen-shredding | text lines 1-40, 140-300 (printed pp. 1-3), 1915-1925, 2030-2080 (printed p. 30), 3265-3310 |
| hrg-commerce-skilling-watkins | lines 4780-4830 (printed p. 75), 5588-5600 (printed p. 87) |
| hrg-hec-collapse-pt1 | lines 2593-2597, 3370-3410 (Troubh) |
| skilling-scotus-2010 | lines 428-436 (syllabus, opinion list), 4050-4095 (PDF 93, printed p. 450, n. 12) |
| ca5-skilling-2009 | lines 318-336 (PDF 9, n. 5) |
| rpt-sga-watchdogs, all hearings, SEC/DOJ texts | grep only (gross revenue; names) |

**Name searches** covered every `work/text/*.txt` file and every `.txt`/`.htm`/`.html` file in `sources/0*/`. Files in `sources/candidates/` were excluded: they are not approved, so they were not used or cited.

## Scratch OCR
The hearing exhibits are image-only pages. To search them for the Watkins letter, I ran tesseract on them in the scratchpad. The output is not saved in the repo. Nothing in the cards is quoted from that OCR. Every quote comes from a text layer or was read from the page image.
