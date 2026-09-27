# Reader D read log (Sarbanes-Oxley & the PCAOB)

Agent: Reader D. No web used. Nothing in `sources/` was edited. Output: `work/facts/reader-sox.json` (cards S-001 to S-080) and `work/facts/reader-sox-gaps.md`.

## Fingerprints

I checked all 17 files with `sha256sum` against `sources/download_log.csv`. All 17 matched.

| Manifest id | Result |
|---|---|
| sox-plaw-html | MATCH |
| sox-plaw (PDF; fingerprint only, not read) | MATCH |
| sox-crs-summary | MATCH |
| sox-srpt-107-205 | MATCH |
| sox-hrpt-107-610 | MATCH |
| sox-hrpt-107-414 | MATCH |
| sox-pitt-testimony | MATCH |
| sec-press-2003-52 | MATCH |
| sec-pcaob-101d-order | MATCH |
| sec-pcaob-103-order | MATCH |
| sec-sox704-report | MATCH |
| gao-03-864 | MATCH |
| sox-bush-remarks | MATCH |
| sox-bush-signing-statement | MATCH |
| sox-hrg-banking-v1 | MATCH |
| sox-hrg-banking-v2 | MATCH |
| sox-hrg-banking-v3 | MATCH |

## How locators work in the cards

- The `lines` values are line numbers in the text copy (`work/text/<id>.txt`). For the statute, they differ from the `.htm` source by only a few lines, the same convention as cards C-072 to C-080.
- Page offsets (printed page = PDF page + offset): S. Rept. 107-205: -4. H. Rept. 107-414 and 107-610: 0. CRS: PDF 4 = CRS-1. S. Hrg. 107-948 Vol. I: -14; Vol. II: +490; Vol. III: +1156. SEC 704 report: -4. GAO-03-864: -6 in the front section (PDF 10 = p. 4), and PDF 32 = p. 26. Bush remarks: PDF 1 = p. 1283.
- Every quote was checked by a script against the text copy, allowing for line-break hyphens and two-column layouts (Bush remarks, GAO Highlights). Curly quotation marks are shown as straight ones.
- The text copies of these sources are not OCR (they have a text layer), so `from_ocr` is false on every card.
- Extra card fields: `provision` (SOX section) and `aspect` (`law` = what the statute requires; `problem` = what Congress or witnesses had in mind; `implementation` = what the SEC, PCAOB or GAO did in 2002-2003).

## What I read

- **sox-plaw-html**: Secs. 101-109 (lines 371-1670); Title II, Secs. 201-209 and 301 (1694-2040); Sec. 302 (2040-2105); Secs. 401-402 (2583-2720); Sec. 404 (2793-2815); Sec. 802 (3490-3540); Sec. 806 (3656-3745); Sec. 807 (3760-3790); Sec. 906 (3880-3920); Secs. 1102-1103 (3940-3990); Sec. 1107 and the legislative-history note (4138-4168).
- **sox-srpt-107-205**: PDF 4-38 [contents; pp. 1-34]: introduction, purpose, hearings, and the title-by-title discussion of Titles I-V. I did not read the formal section-by-section part (PDF 53-60) closely because it repeats the statute. Enron keyword search over the whole file.
- **sox-hrpt-107-610**: PDF 1 (cover); PDF 56 (Sec. 705 GAO study naming Enron); PDF 69-70 (joint explanatory statement). Enron keyword search. **Finding:** the joint statement has no section-by-section explanation.
- **sox-hrpt-107-414** (selectively): PDF 18-19 (background, hearings); PDF 47 and 49 (minority views); PDF 53 (minority views, statute of limitations); PDF 55 (LaFalce additional views). Enron keyword search.
- **sox-crs-summary**: whole report, PDF 1-19.
- **sox-pitt-testimony**: whole testimony (one long line in the text copy).
- **sec-press-2003-52**: whole release.
- **sec-pcaob-101d-order**, **sec-pcaob-103-order**: whole files. **Finding:** they are sec.gov landing pages only (title, release number, date). The order texts are not in the library (gap 1).
- **sec-sox704-report**: PDF 1-8 [contents; executive summary pp. 1-4]; PDF 27 [23] fn. 58; PDF 33-34 [29-30] (off-balance sheet; Enron and Dynegy); PDF 36 [32] (Enron case highlight); PDF 44-48 [40-44] (SOX provisions for auditors; proposals; MD&A).
- **gao-03-864** (summary only, for concentration and rotation): PDF 2 (Highlights); PDF 10-12 [4-6] (Results in Brief); PDF 32 [26] (limited choices, Andersen clients).
- **sox-bush-remarks**: PDF 1-4 [pp. 1283-1286].
- **sox-bush-signing-statement**: whole file.
- **sox-hrg-banking-v1/-v2/-v3**: keyword searches only (Enron within 3 lines of provision terms: consult/non-audit, rotation, cooling off, certify, internal control, off-balance/SPE, loans, shred/destroy, whistleblower). Hits I then read:
  - Vol. I: PDF 3 (title page); PDF 15 [1] (Sarbanes opening, Feb 12, 2002); PDF 21-22 [7-8] (Stabenow); PDF 73 [59] and 79-80 [65-66] (Breeden prepared statement); PDF 105 [91] (Hills, skimmed, not used).
  - Vol. II: PDF 56 [546] (Sarbanes/Coffee exchange on bank loans to Enron, not used); PDF 63 [553] and 69 [559] (Walker prepared statement, Mar 5, 2002).
  - Vol. III (Senate floor debate reprinted from the Congressional Record): PDF 69-70 [1225-1226] (Daschle offers the Leahy amendment, July 9, 2002); PDF 77 [1233] (Leahy); PDF 80 [1236] (AFL-CIO letter, not used); PDF 281-284 [1437-1440] (Schumer loan-ban and SPE-study amendments, July 12, 2002).

## Uncertainties and disagreements noted in cards

- **Sec. 201 count:** the statute lists nine prohibited items (the ninth is anything the PCAOB adds); the SEC 704 report says "eight categories" (S-042).
- **Sec. 402:** CRS says it bans loans "of any kind"; the statute has exceptions (S-060). The Senate committee's bill required only disclosure; the ban came from Schumer's floor amendment (S-062, S-063).
- **Sec. 807:** described on the Senate floor as a 10-year felony; enacted at 25 years; the library does not show why (S-076).
- **Sec. 203:** CRS mentions only the lead partner; the statute also covers the reviewing partner.
- **SEC certification rule:** the release number is printed as "34-8124" in the 704 report (S-045).
- **Lay loan figure:** the Senate report's source is a newspaper (S-061).
- **Floor statements and prepared statements** are characterizations by senators or witnesses, not findings; the cards say so.
- **Bush's remarks** do not mention Enron by name.
