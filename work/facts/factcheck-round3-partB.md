# Fact-check, Round 3, Part B: re-check of the Round 2 fixes and the new Cast entries

Agent: Fact-Checker (instance B). Date: 2026-09-26.

## What I checked

- **Fixes as applied.** I read the Round 2 fixes in the data files themselves (`js/cast-data.js`, `js/timeline-data.js`, `js/glossary-data.js`, `work/drafts/footnote.json`, `js/footnote-data.js`, both Chewco SVGs), not only in the writers' fix reports.
- **Cites.** A script checked all 299 Cast, Timeline and Glossary cites against their cards. Fingerprints of the files used all match `download_log.csv`.
- **Page images opened:** `batson-final-app-b-part1` PDF 11.

## 1. Round 2 findings

| # | Item | Status | Reason |
|---|---|---|---|
| 1 | McMahon role | **NOT RESOLVED (citation only)** | The text is now correct ("treasurer until 2000 ..."). But it is cited to card A-037 with the locator widened to "pp. 60-61 and 97". A-037 does not contain that text, and "p. 97" was my own mistake in Round 2: the Glisan sentence is on **p. 95** (PDF 101). New card **F-055** covers it. See required fix C5. |
| 2 | Koenig date | RESOLVED (text) | "January 2001 call with investors (January 22, 2001)". Cite issue: see #9. |
| 3 | McMahon summary | RESOLVED | Now McMahon's own account, attributed to him. |
| 4 | Lay "ultimate responsibility" | **NOT RESOLVED (citation only)** | The text is correct. But the A-062 cite now says "p. 19" while its page is 16 (p. 10), so the link opens the wrong page. New card **F-056** (p. 19, PDF 25). See C6. |
| 5 | Lay status label | RESOLVED | "conviction vacated after his death". Site Builder: add this key to `OUTCOME_LABELS`. |
| 6 | Lay "every count" | RESOLVED | |
| 7 | Berardino subcommittee | RESOLVED | Card B-065 now corrected by me too. |
| 8 | Delainey SEC list | RESOLVED (text); citation, see C4 | The wording correctly names the post, not the person. |
| 9 | Koenig SEC list cite | **NOT RESOLVED (citation only)** | See C3. |
| 10 | Andersen "1985 merger" | RESOLVED | |
| 11 | Merrill criminal trial | RESOLVED | Card B-085 supports it; the text keeps the "unnamed" warning. |
| 12 | Duncan trial testimony (optional) | RESOLVED (text); citation, see C2 | The text is accurate. C-030 does not state the fact itself; only its notes allude to it. New card **F-052** (image-checked). |
| 13, 14 | Optional notes | Not applied | Acceptable. |
| 15 | Timeline 2006-05 | RESOLVED | |
| 16 | Timeline 2002-05-07 | RESOLVED | |
| 17 | Timeline 2003-03-17 | RESOLVED | |
| 18 | Timeline 2001-12-02 | RESOLVED | |
| 19 | Timeline titles | RESOLVED | |
| 20 | Glossary `pcaob` | RESOLVED | |
| 21 | Glossary `vacated` | RESOLVED | |
| 22 | Chewco box and `<desc>` (wide and narrow) | RESOLVED | Visible text and `<desc>` read "The special committee found no evidence the board was told of Kopper's role." The SHA-256 of each SVG matches `credits.json` and `credits.js`. |
| 23 | Chewco footer | RESOLVED | "1997 through mid-2001" |
| 24 | Raptor diagram (note) | n/a | |
| 25 | Footnote intro cite | RESOLVED | `rpt-psi-board` PDF 52 cite added; the quote is verbatim. |
| 26 | Footnote closing cites | RESOLVED | Both Powers cites were added. |
| 27, 29 | Footnote closing text | RESOLVED | "quarterly report filed November 19, 2001". This is also in `js/footnote-data.js`. |
| 28 | fn-05 hedge | RESOLVED | "it seems likely that ..." restored. This is also in `js/footnote-data.js`. |

## 2. New and updated Cast entries

| Entry | Verdict | Notes |
|---|---|---|
| `lea-fastow` | Text PASS; citation fixes needed | Every sentence checks out. Her name comes from Chairman Greenwood ("it appears ..."). The outcome is attributed throughout to the separate opinion. Citations: the second cite uses card F-009 with a different source; it should be **F-051**. The F-009 cite needs page 61 and "p. 55" (see C1, C7). |
| `richard-buy` | PASS; page update | The Fifth Amendment is handled correctly and "charged" is not used near his name. Update the F-011 and F-014 pages (C7). |
| `greg-whalley` | PASS | |
| `vince-kaminski` | PASS; page update | Card A-069 says "sworn statement ... to the examiner's counsel", so "sworn testimony to the bankruptcy examiner" is acceptable. Update the F-014 page (C7). |
| `nancy-temple` | PASS | Both Greenwood quotes are verbatim (lines 285-292). The C-018 wording matches. |
| `raymond-troubh` | PASS; page update | Update the F-015 page (C7). |
| `andrew-fastow` (updated) | PASS | |

**Is "pleaded guilty" the right outcome label?**
- **Andrew Fastow: yes.** Justice Sotomayor's opinion says "In 2004, Andrew and Lea Fastow both pleaded guilty". The DOJ's February 19, 2004 release already listed him as "convicted to date", which is consistent with a plea before that date. Two library sources agree, and the text attributes the plea to the separate opinion.
- **Lea Fastow: yes, with a caution.** It is the accurate label for what the footnote says: "convicted" would be vaguer and "charged" would understate it. But its only source is a background list of news "highlights" in a separate opinion. That is acceptable only because the entry's text says so. Do not add a charge, a sentence or the DOJ candidate release. The Site Builder should keep the attribution sentence visible next to the badge; nothing else is required.

## 3. The writer's three flags

1. **Card B-065.** Fixed by me: "Subcommittee on Capital Markets, Insurance, and Government Sponsored Enterprises". Marked FIXED.
2. **McMahon "until 2000" on A-037 widened to p. 97.** Not adequate. A cite must point to a card whose own quote and locator support the sentence, and A-037's card says nothing about when McMahon left the job. I added card **F-055** (Powers p. 95, PDF 101: "In May 2000, Glisan succeeded McMahon as Treasurer of Enron."; plus p. 62, PDF 68: "By this point, McMahon had left the Treasurer's position and the Finance group."). Restore A-037's own locator.
3. **SEC-list cites on B-050 and B-051 with a different `source_id`.** Not acceptable. Round 1 verified each card's quote only at its own source. A cite whose `source_id` differs from its card's source is not backed by a checked quote. The integrity check also flags these mismatches. I added checked cards **F-053** (Koenig, SEC list line 63) and **F-054** (Delainey, SEC list line 91).

**Numbering note.** Fact-Checker A added its own F-016 to F-021 to the same file at the same time. I numbered my new cards **F-051 to F-056** to avoid a clash.

## Required changes in `js/cast-data.js` (Reference Writer)

| # | Entry | Change |
|---|---|---|
| C1 | `lea-fastow` | Cite 2 (`hrg-hec-collapse-pt2`): card F-009 becomes **F-051**; page 80; loc "p. 76, questioning by Chairman Greenwood, Feb. 7, 2002". |
| C2 | `david-duncan` | Cite for the trial-testimony sentence: C-030 becomes **F-052** (`batson-final-app-b-part1`, page 11, loc "p. 9, nn. 13-14"). You may write "in May 2002". |
| C3 | `mark-koenig` | SEC-list cite: card B-051 becomes **F-053** (`sec-enron-spotlight`, page null, loc "Enron-Related Enforcement Actions list (Lit. Rel. 18849, Aug. 25, 2004)"). |
| C4 | `david-delainey` | SEC-list cite: card B-050 becomes **F-054** (`sec-enron-spotlight`, page null, loc "... (Lit. Rel. 18435, Oct. 30, 2003)"). |
| C5 | `jeffrey-mcmahon` | Restore the A-037 loc to "pp. 60-64, II.G Enron's Repurchase of Chewco's Limited Partnership Interest" (page 70). Add **F-055** (`powers-report-sec`, page 101, loc "p. 95, IV.F; p. 62, II.G.1"). |
| C6 | `kenneth-lay` | Restore A-062's loc to the card's own locator (p. 10, page 16), or drop it. Add **F-056** (`powers-report-sec`, page 25, loc "p. 19, Executive Summary - The Participants") for the "ultimate responsibility" sentence. |
| C7 | `lea-fastow`, `richard-buy`, `vince-kaminski`, `raymond-troubh` | Set the page on cites to cards whose `pdf_page` I have now filled in: F-009 → 61 (loc "p. 55"); F-011 → 16; F-014 → 90; F-015 → 37. |
| C8 | `charles-lemaistre`, `norman-blake` | Card B-079 was moved by Fact-Checker A to the hearing transcript. Change these cites to `source_id` `hrg-psi-board`, page 100, loc "p. 90, Testimony of Charles LeMaistre (questioning by Sen. Levin)". The entry text already matches the transcript. |

**After these changes:**
- Re-run the cite/card check. Every cite's `source_id` and page must equal its card's.
- **Site Builder:** add "conviction vacated after his death" to `OUTCOME_LABELS` in `js/cast.js`.

**Other files:** no changes are required in the Timeline, Glossary, footnote or diagrams. Their cites all match their cards.

## Cards I changed (Round 3)

- **B-065:** "Committee" changed to "Subcommittee on Capital Markets ...". Marked FIXED.
- **F-007, F-009, F-011, F-014, F-015:** `pdf_page` filled in. F-009's printed page corrected from p. 54 to p. 55 and marked FIXED.
- **F-051 to F-056:** new, each checked at its own source. F-052 was checked against the page image.

## Corrections log

Rows 58-85 in `build-log/corrections.md`: one row per Round 2 finding that was applied to the Cast, Timeline, Glossary, footnote or diagram, plus rows for the Round 3 card changes. The rows for C1-C8 note where the writer's change is still pending.

## Verdicts

| File | Verdict | Remaining required fixes |
|---|---|---|
| `js/cast-data.js` | **FAIL** until C1-C8 are made | All are citation-to-card fixes. No factual text errors remain. C1-C6 and C8 are must-fix (the cite points to a card whose source or page does not match). C7 is should-fix. |
| `js/timeline-data.js` | **PASS** | none |
| `js/glossary-data.js` | **PASS** | none |
| `work/drafts/footnote.json` / `js/footnote-data.js` (intro, closing, fn-05) | **PASS** | none |
| `images/diagram-chewco-ljm.svg` (+ `-narrow`) | **PASS** | none |
| `images/diagram-raptor.svg` (+ `-narrow`) | **PASS** | none |
| `images/chart-restatement.svg` (+ `-narrow`) | **PASS** | none |

## Final

**C1-C8 verified in `js/cast-data.js`: all done.**
- C1: Lea Fastow's House-hearing cite now uses F-051 (page 80).
- C2: Duncan's trial-testimony sentence now cites F-052 (page 11, "p. 9, nn. 13-14"). C-030 is no longer cited there.
- C3: Koenig's SEC-list cite now uses F-053. His B-051 cite remains, correctly, for the Fifth Circuit.
- C4: Delainey's SEC-list cite now uses F-054. His B-050 cite remains, correctly, for the DOJ release.
- C5: McMahon now cites F-055 (page 101), and A-037's locator is back to "pp. 60-64".
- C6: Lay now cites F-056 (page 25, p. 19), and A-062's locator is back to "p. 10 (Lay p. 19)".
- C7: the page is now set on every cite to an F-card: F-009 → 61 ("p. 55"), F-011 → 16, F-014 → 90, F-015 → 37.
- C8: LeMaistre and Blake now cite B-079 as `hrg-psi-board`, page 100, "p. 90".
- The label "conviction vacated after his death" is now a key in `js/cast.js`.
- No names, roles, summaries or outcome texts changed.

**Sweep of the Cast, Timeline and Glossary (301 cites)**
- **Cards:** every cite's card exists and is marked OK or FIXED.
- **Sources:** every `source_id` is a manifest id and equals its card's source.
- **Pages:** every page equals its card's `pdf_page`.
- **Quote on page:** for 221 cites with a page, a script looked for the card's quote on that PDF page of the text copy.
  - 204 were found there.
  - The other 17 were checked by hand. All are text-copy artifacts at the correct page: OCR noise ("August 14,2001"), soft or line-break hyphens, two-column layout, quotes that run across a page break (GAO PDF 7-8 and 24-25), and one image-only page (the Temple e-mail, C-001, image-checked in Round 1).
  - One is a card note, not an error: A-046's quote comes from the Executive Summary, p. 13. Its PDF page (86) is where the facts the Timeline cites appear.
- **Candidates:** no file cites anything in `sources/candidates/`.
- **Buffett:** "Buffett" or "Buffet" does not appear anywhere in the three files.

**Corrections log.** The pending rows for C1-C7 in `build-log/corrections.md` now say "verified done". Row 86 was added for C8.

**Final verdicts**

| File | Verdict |
|---|---|
| `js/cast-data.js` | **PASS** |
| `js/timeline-data.js` | **PASS** |
| `js/glossary-data.js` | **PASS** |
| `work/drafts/footnote.json` / `js/footnote-data.js` (intro, closing, fn-05) | **PASS** |
| `images/diagram-chewco-ljm.svg` (+ `-narrow`) | **PASS** |
| `images/diagram-raptor.svg` (+ `-narrow`) | **PASS** |
| `images/chart-restatement.svg` (+ `-narrow`) | **PASS** |

No required fixes remain for Part B.
