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

## Revision pass: new library documents and cards G-001 to G-036

Date: 2026-09-27.

### The 11 new documents

- **Manifest and fingerprints.** All 11 are listed in `sources/manifest.csv`. All 11 were downloaded by the owner's action (`download_log.csv`, 2026-09-27 00:07 UTC). I recomputed SHA-256 for all 85 library files on disk, and all 85 match.
- **Status column: please confirm with the owner.** The manifest's `status` column for the 10 documents in `sources/candidates/` still reads **"candidate-unapproved"**, and their folder is still `candidates`. The prepared file `sources/candidates/manifest-rows-to-add.csv` had given them library folders and "to-download". I checked the cards on the coordinator's word that the owner approved them. Rows added by the owner plus his action's download support that. But the status column says otherwise, and CLAUDE.md forbids relying on candidates until he approves them. Please confirm with the owner, or ask him to change the status, before any of these cards reach a published page.

### How I checked

- **HTML sources.** Every quote was checked against the original HTML file, not only the text copy.
- **PDFs with text.** Checked page by page with `pdftotext`.
- **Image-only pages.** The Dec. 12 hearing appendix (PDF 119-122, 128-130) was read on the page images.
- **Claims and verbs.** I read every claim against its source and applied the ruled verbs: DOJ "announced", indictment "alleged", agreement "agreed", court "held".

### Verdicts

| Card | Verdict | Note |
|---|---|---|
| G-001 | FIXED | Verb "pleaded guilty" changed to "announced". |
| G-002 | FIXED | Verb changed to "announced". |
| G-003 | FIXED | Verb changed to "announced". |
| G-004 | FIXED | The release does not state the sentencing date. The claim now says DOJ "announced on September 26, 2006 that Fastow had been sentenced". The **$29M vs $20M** forfeiture disagreement is confirmed; report both, attributed. |
| G-005 | FIXED | Verb changed to "announced". The claim is accurate. The release shows only an agreement to plead and an "expected" plea. It is consistent with F-010 (the separate opinion: pleaded guilty in 2004) and with the Glisan release (charged May 2003). |
| G-006 | FIXED | Verb changed to "announced". |
| G-007 | FIXED | Verb changed to "announced". |
| G-008 | FIXED | Verb changed to "announced". |
| G-009 | FIXED | Verb changed to "announced". |
| G-010 | FIXED | Verb changed to "announced". |
| G-011 | FIXED | Source type is now "DOJ news conference transcript"; verb "announced". The date note (page title 08-22-02, URL 082102) was confirmed in the file. |
| G-012 | FIXED | Same change as G-011. |
| G-013 | FIXED | Same change as G-011. **The note was wrong: the $12M vs $4M figures are not a disagreement.** SEC Fastow complaint para. 9: $4M criminal forfeiture + $8M direct SEC disgorgement = $12M, which is DOJ's "$12 million to satisfy both this plea and a related SEC complaint" (also Cutler, and Batson First Interim n. 8). The "~$23 million" sought in the information is additional; its outcome is not in the library. The Cast and ch7 wording ("agreed to forfeit $4 million, according to the SEC") is correct as far as it goes. Do not present $12M vs $4M as a conflict. If both appear, explain that the $12M covers the plea and the SEC case. `revision-gap-map.md` gap 6 should be read accordingly. |
| G-014 | FIXED | Same change as G-011. |
| G-015 | OK | "alleged"; filed 3/7/02; one count under § 1512(b)(2). |
| G-016 | OK | |
| G-017 | OK | |
| G-018 | FIXED | Line-break hyphen removed from the quote ("therefore"). |
| G-019 | FIXED | The vote line is the reporter's line, so the verb is now "stated", not "held". |
| G-020 | OK | |
| G-021 | OK | |
| G-022 | OK | |
| G-023 | OK | |
| G-024 | OK | |
| G-025 | OK | |
| G-026 | OK | These are recitals, so "stated" is correct. |
| G-027 | FIXED | These are the agreement's terms, so the verb is now "agreed". |
| G-028 | OK | |
| G-029 | FIXED | Source type is now "SEC litigation release (settled action)"; verb "announced". "Without admitting or denying" must accompany any use. |
| G-030 | FIXED | Same change as G-029. |
| G-031 | FIXED | **No oath anywhere in the Dec. 12, 2001 record** (text layer searched for sworn/oath/swear/raise your right). Source type changed from "sworn testimony" to "hearing testimony and record (no oath shown)". |
| G-032 | FIXED | Same source-type change as G-031. Image-checked (PDF 119, 122): verbatim, and identical to the Powers quotation. Verb is now "stated (written statement submitted to the hearing)". |
| G-033 | FIXED | Same source-type change as G-031. The spoken statement does not name Chewco; only the written statement does (PDF 120). Verb is now "told the subcommittees (not shown under oath)". |
| G-034 | FIXED | Same source-type change as G-031. Image-checked (PDF 128). |
| G-035 | FIXED | Same source-type change as G-031. Image-checked (PDF 129-130). |
| G-036 | FIXED | Same source-type change as G-031. Verb is now "told the subcommittees (not shown under oath)". |

**Totals:** 36 cards; 11 OK, 25 FIXED, 0 rejected. Most fixes are verbs or source types. The substantive ones are G-004 (sentencing date), G-013 (the forfeiture "disagreement" that is not one) and G-031 to G-036 (no oath).

### Berardino, "sworn witness" (`js/cast-data.js`)

**Supported.** The Cast cites card B-065, the **February 5, 2002** hearing (`hrg-hfs-enron-investors`), and the oath is on the page:
- PDF 124 (lines 7505-7509): "Do you have any objection to testifying under oath? Mr. BERARDINO. No, I do not."
- PDF 125 (lines 7535-7538): "[Witness sworn.] Chairman BAKER. You are now under oath."

The Dec. 12, 2001 record shows no oath.

**Should-fix, for when the writer uses the new cards:** say "a sworn witness before a House subcommittee on February 5, 2002; his December 12, 2001 testimony is not shown as given under oath". Do not describe the December statements (including the Powers quotation, A-048/G-032) as sworn.

### Corrections log

Rows 87-95 in `build-log/corrections.md`.

## Revision pass: final

Date: 2026-09-27. I checked all 64 entries under "Reference Writer" in `work/facts/fixes-revision.md`:
- **In the data files.** Every "New" text is present in `js/cast-data.js`, `js/timeline-data.js` and `js/glossary-data.js`.
- **Against the cards and sources.** Every change was checked against its G-card and against the source. The DOJ releases, the Kopper transcript and the SEC release were checked in the original HTML. The court opinions, indictment and agreement were checked in the PDF text, and the Dec. 12 appendix on the page images.
- **Sweep of all 341 citations:**
  - Every card exists and is OK or FIXED.
  - Every `source_id` matches its card, and every page matches its card.
  - No path to `sources/candidates/` appears in the data.
  - Buffett is absent.
  - The 17 quote-not-found-on-page flags are the same text-copy artifacts ruled on in the Round 3 "Final" section.

### Still open: approval status of the 10 documents

`sources/manifest.csv` still lists the 10 documents in `sources/candidates/` with status **"candidate-unapproved"**. Nothing has changed since my last report. The owner must confirm, or change the status, before publication. This is not a content error.

### Ruling (a): Skilling's label "convicted"

**Accurate and fair; keep it.**
- On April 6, 2011 the Fifth Circuit held that the honest-services error was harmless beyond a reasonable doubt and "AFFIRM[ED] the convictions on all counts" (G-024, PDF 16).
- The 2013 agreement recites that the Supreme Court denied review on April 16, 2012 (G-026).
- All 19 convictions therefore stand. "Later narrowed on appeal" now describes an intermediate step, not the outcome.
- The entry's text still explains the 2010 Supreme Court ruling, including that it affirmed in part and vacated in part, and the 2011 harmless-error ruling. The Timeline has both items.
- Optional: "convicted (upheld 2011)". Not required.

### Ruling (b): Duncan "pleaded guilty"

- **The text passes.** It says plainly: "The library has no charging document or judgment for him, and does not show the date of the plea, any sentence, or what later happened to the plea." Both sources are attributed: the DOJ's "obstructing an SEC investigation" and the Supreme Court's "later pleaded guilty to witness tampering", quoted verbatim.
- **The label fails.** The outcome badge "pleaded guilty" alone presents a 2002 event as how his case ended, and the library cannot show how it ended. The rules say to check how each case ended before calling anyone guilty. There is a specific reason for care here. His plea concerned the same document destruction for which Andersen's conviction was reversed in 2005. From general knowledge, not from the library, I believe his plea may later have been withdrawn. That must not appear on the site unless a library document supports it. It is the reason the label must not read as final.
- **Required fix (writer):** set Duncan's `outcome_status` to **"pleaded guilty (2002); later history not in library"**, and add that key to `OUTCOME_LABELS` in `js/cast.js`.
- **Gap:** logged as **critical** (#6 in `work/facts/factcheck-gaps.md`) for the Source Scout: court or DOJ records of what happened to the plea.

### Item 3: the four merged Timeline items

**Pass. No citation or accuracy was lost.**

| Merged item | Now in | Citation kept | Check |
|---|---|---|---|
| 1985 Andersen | 1985-07-01 | C-026 | Wording matches C-026. |
| 2001-10-12 Temple e-mail | 2001-10-23 | C-001 | The Oct. 12 date and content are preserved. |
| 2002-05-24 Batson appointed | 2003-11-04 | A-095 | "approved ... in May 2002" matches A-095. |
| 2002-05-07 directors | 2002-07-08 | B-073, B-074 | "testified under oath" (PSI p. 2) and "the subcommittee reported" are preserved. |

The Timeline has 58 items from 1985 to 2006, which is under 60, plus 3 epilogue items (2010, 2011, 2013).

### Other findings and required fixes

| # | Where | Problem | Fix | Severity |
|---|---|---|---|---|
| R-1 | Cast (`jeffrey-skilling`, `arthur-andersen`, `joseph-berardino`), Timeline (2002-03-07, 2006-05-25, 2011-04-06, 2013-05-08), Glossary (`harmless-error`) | G-card cites carry range strings as `page` (e.g. "1-2, 16", "119, 121-122"). These cannot form a `#page=` link. My fault in the revision check: I did not catch it on the cards. | Cards corrected (single PDF page; range kept in `section`). Writer: set each cite's `page` to its card's new `pdf_page`: G-015 → 6, G-024 → 16, G-025 → 16, G-026 → 2, G-027 → 2, G-031 → 1, G-032 → 122. Re-run the cite check. | **must-fix** |
| R-2 | Cast `david-duncan` `outcome_status` | See ruling (b). | "pleaded guilty (2002); later history not in library" | **must-fix** |
| R-3 | Cast `david-duncan` `outcome_text` | "consented, subject to court approval, to a permanent injunction ... and to a permanent suspension". Only the injunction was subject to court approval; the suspension is an SEC administrative order. | "... he consented to a permanent injunction against violating the antifraud laws (subject to court approval) and to an order permanently suspending him from practicing before the SEC as an accountant." | should-fix |
| R-4 | Timeline 2013-05-08 | "agreed to jointly recommend a sentence of 168 to 210 months". The agreement recommends a guidelines range. | "agreed to jointly recommend a sentencing range of 168 to 210 months". | should-fix |
| R-5 | Cast `michael-kopper` | "He added that the charging document ..." comes after a sentence about the SEC's figures, so "He" is unclear. | "The Deputy Attorney General added that ..." | should-fix |

**Checked and correct, no change needed:**
- **Skilling:** R1-R4; Oct. 23, 2006 sentence date and the 2011 and 2013 facts.
- **Fastow:** R5-R7; both forfeiture figures attributed; 10 vs 6 years unexplained, as the library leaves it.
- **Lea Fastow:** R8-R10.
- **Glisan:** R11-R13.
- **Causey:** R14-R15.
- **Delainey:** R16-R17; "does not show whether he pleaded guilty or was tried" is correct.
- **Kopper:** R18-R19; $12M = $4M + $8M explained correctly.
- **Andersen:** R23-R24.
- **Berardino:** R25-R27; "sworn" only for Feb. 5, 2002, and the Powers words tied to the written statement, verbatim "was in error".
- **Timeline:** R28-R58, apart from R-4. The 2004-01-14 SEC settlement is cited to B-032 (SEC list, Jan. 14, 2004).
- **Glossary:** R59-R64. The four new definitions are correct as general knowledge.

### Corrections log and gaps

- **Corrections log:** rows 106-109 in `build-log/corrections.md`. Row 106 is made (cards); rows 107-109 are pending the writer.
- **Gaps:** #6 in `work/facts/factcheck-gaps.md` (critical).

### Verdicts

| File | Verdict | Remaining |
|---|---|---|
| `js/cast-data.js` | **FAIL until fixed** | R-1 and R-2 are must-fix; R-3 and R-5 are should-fix. |
| `js/timeline-data.js` | **FAIL until fixed** | R-1 (page fields) is must-fix; R-4 is should-fix. Text accuracy passes. |
| `js/glossary-data.js` | **FAIL until fixed** | R-1 (`harmless-error` cite page → 16). Definitions pass. |
| Cards G-001 to G-036 | **PASS** | After the page fix made today. |

All three files pass once R-1 and R-2 are made. Both are mechanical changes. Publication also waits on the owner confirming the approval status of the 10 documents.
