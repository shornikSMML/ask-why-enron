# Reader B, revision pass: read log

Fingerprints: computed `sha256sum` for all 11 files and compared with `sources/download_log.csv` on 2026-09-27. **All 11 matched.** No web used. Nothing in `sources/` edited.

| Manifest id | File | What I read | Fingerprint |
|---|---|---|---|
| doj-fastow-plea-press-2004 | sources/candidates/doj-press-2004-01-14-fastow-pleads-guilty.htm | whole release (work/text lines 1-145) | match |
| doj-fastow-sentenced-press-2006 | sources/candidates/doj-press-2006-09-26-fastow-sentenced.html | whole release (lines 1-54) | match |
| doj-glisan-plea-press-2003 | sources/candidates/doj-press-2003-09-10-glisan-pleads-guilty.htm | whole release (lines 1-129) | match |
| doj-causey-sentenced-press-2006 | sources/candidates/doj-press-2006-11-15-causey-sentenced.html | whole release (lines 1-40) | match |
| doj-dag-kopper-plea-transcript-2002 | sources/candidates/doj-dag-transcript-2002-08-21-kopper-plea.htm | whole transcript (lines 1-480); raw HTML checked for date clues (title tag, links) | match |
| doj-andersen-indictment-2002 | sources/candidates/doj-andersen-indictment-2002.pdf | all 7 pages (text); PDF p. 1 also checked as image (filing stamp) | match |
| andersen-scotus-full-usreports | sources/candidates/arthur-andersen-v-us-544-us-696-2005-usreports.pdf | all 13 pages, 544 U.S. 696-708 (text) | match |
| ca5-skilling-2011-remand | sources/candidates/ca5-us-v-skilling-2011-remand.pdf | pp. 1-5 and 16 in full; searched pp. 6-15 for holdings | match |
| doj-skilling-sentencing-agreement-2013 | sources/candidates/doj-us-v-skilling-sentencing-agreement-2013.pdf | all 7 pages (text) | match |
| sec-duncan-litrel-20441 | sources/candidates/sec-litrel-20441-duncan-2008.htm | whole release (text lines 282-302; rest is SEC site navigation) | match |
| hrg-hfs-enron-investors-pt1 | sources/05-hearings-enron/hhrg-107-hfs-enron-collapse-2001-12-12.pdf | Text: PDF pp. 1-7 (cover, rosters, contents, opening), p. 40 (printed 34, Herdman), pp. 53-55 (printed 47-49, Berardino oral statement); keyword searches of pp. 1-71. Images (no text in work/text for PDF pp. 72-168): PDF pp. 119-122 (printed 113-116, Berardino prepared statement), 128-130 (printed 122-124, letters of Dec 13, 2001 and Jan 21, 2002) | match |

Site files searched (read only) for the gap map: `work/drafts/ch1-7.html`, `work/drafts/footnote.json`, `js/cast-data.js`, `js/timeline-data.js`, `js/glossary-data.js`; also `build-log/gaps.md`, `work/facts/reader-a.json` (card A-048 only) and `work/facts/reader-b.json` (format).

Notes:
- `work/text/hrg-hfs-enron-investors-pt1.txt` is empty for PDF pages 72-168 (the appendix, including Berardino's written statement). Quotes from those pages were transcribed from the page images.
- No OCR text was used.
