# Fact-check, Round 3, Part A: re-check of the chapter fixes

Agent: Fact-Checker (instance A). Date: 2026-09-26.

**Inputs.** I checked each fix in `work/facts/fixes-round2-chapters.md` against the regenerated `work/drafts/ch1.html` ... `ch7.html`. I re-ran the citation extraction on all seven chapters (ch1 27 citations, ch2 19, ch3 36, ch4 28, ch5 37, ch6 48, ch7 58).

**Source checks.**
- Every source I newly relied on was checked against the source itself.
- Page images checked: Batson First Interim PDF 4, 5, 8, 9 and Batson Final PDF 18.
- Fingerprints re-checked: `batson-1st-interim` and `hrg-psi-board` match `download_log.csv`. The other sources were already checked in Round 2 and all matched.

## 1. Each Round 2 finding

| # | ch | status | comment |
|---|---|---|---|
| 1-1 | 1 | RESOLVED | "citing an Enron press release" matches JCT n. 52. |
| 1-2 | 1 | RESOLVED | 1992 is now attributed to Enron. The 1991 disagreement is stated and cited (C-055, SGA p. 32). |
| 1-3 | 1 | RESOLVED | The ellipsis matches the page image. |
| 1-4 | 1 | RESOLVED | A-007 (same source) plus PDF 89, p. 61 supports the 1989 fact. The card's notes already record it. |
| 1-5 / formation (coordinator item 2) | 1, 6 | **NOT RESOLVED** | The facts are right: InterNorth acquired HNG on July 1, 1985 (JCT p. 59, PDF 87), and the name changed to Enron Corp. in April 1986 (JCT p. 59). But the fix introduced a grammar error. In "...InterNorth acquired Houston Natural Gas in July 1985, which took the name Enron in April 1986", the "which" attaches to Houston Natural Gas. That says HNG took the Enron name, which is wrong: InterNorth, the acquirer, was renamed. **Required (ch1 and ch6):** "... when InterNorth acquired Houston Natural Gas in July 1985. The combined company took the name Enron in April 1986." |
| Lay sentence (coordinator item 2) | 1 | RESOLVED | "Lay would lead the company until early 2002" is supported by JCT n. 62. |
| 2-1 (must-fix) | 2 | RESOLVED | Both years are given and attributed. "A year earlier than the SEC had agreed to" matches SGA: "a year earlier than the SEC had approved". |
| 2-2 | 2 | RESOLVED | Matches 10-K lines 2396-2398. |
| 2-3 | 2 | RESOLVED | |
| 2-4 | 2 | RESOLVED | |
| 2-5 | 2 | RESOLVED | The full sentence is verbatim. |
| 2-6, 2-7 | 2 | RESOLVED | |
| 3-1 | 3 | RESOLVED | |
| 3-2 | 3 | **NOT RESOLVED (typo introduced)** | The content is correct and verified (Powers lines 1818-1836). But the text now reads `"an SPE not affiliated with either Enron or CalPERS," It found no written record ...`. The comma inside the quote marks is followed by a capital "It". **Required:** `...CalPERS." It found ...` |
| 3-3 | 3 | RESOLVED | |
| 3-4 | 3 | RESOLVED | |
| 3-5 | 3 | RESOLVED | Q3 2000 to Q3 2001 is July 2000 to September 2001. The exclusion and the caveat match Powers lines 3654-3667. |
| 3-6 ... 3-9 | 3 | RESOLVED | |
| 4-1 | 4 | RESOLVED | |
| 4-2 | 4 | RESOLVED | |
| 4-3 | 4 | RESOLVED | Matches PSI n. 32 (PDF 21). |
| 4-4 | 4 | RESOLVED | |
| 4-5 caption (coordinator item 3) | 4 | RESOLVED | The hearing is identified (credits.json; `hrg-sga-fall-of-enron` is dated 2002-01-24). Watkins testified before Senate Commerce on 2002-02-26. Note, optional: Watkins also testified to a House subcommittee on Feb 14, 2002 (`hrg-hec-collapse-pt3`). "At a different one" is still true. Also, the date comes from the Commons file page, not the source caption, so "as identified in the photo's source caption" slightly overstates. Optional wording: "identified by its source as the committee's opening Enron hearing, January 24, 2002". |
| 4-6 | 4 | RESOLVED | B-054 (same source) at PDF 15 supports the sentence. |
| 5-1 | 5 | **NOT RESOLVED** | See section 2. |
| 5-2 | 5 | RESOLVED in text; **card change required** | The text is correct (Powers lines 1258-1267). The citation must point to the new card **F-018**, not A-081 (a 10-Q card). |
| 5-3 | 5 | RESOLVED in text; **card change required** | The second citation must point to **F-019**, not A-087 (a Batson Final card). |
| 5-4 | 5 | RESOLVED | C-065 (same source) contains the $30.72 figure. |
| 5-5 | 5 | RESOLVED | |
| 5-6 | 5 | RESOLVED in text; **card change required** | The quote is verbatim (image-checked, PDF 8). The citation must point to **F-020**, not A-091 (a JCT card). |
| 5-7 | 5 | RESOLVED | Card A-083's own locator still says lines 22-37. That is card housekeeping; the quote is at lines 44-47. |
| 5-8 | 5, 7 | RESOLVED | |
| 6-1 | 6 | RESOLVED | "Going beyond it" is a fair rendering of "Transcending these circumstances". |
| 6-2 | 6 | RESOLVED | |
| 6-3 | 6 | RESOLVED | Card C-020's claim still says "so-called". That is not shown to readers, but should be cleaned up. |
| 6-4, 6-5, 6-6 | 6 | RESOLVED | The aggregation error matches App. B p. 62 (PDF 64). |
| 7-1 | 7 | RESOLVED | B-016 (same source, rpt-psi-board) at PDF 54. The card's claim and notes contain the $77M sentence verbatim from p. 50. The card and the new locator together support the sentence. |
| 7-2 | 7 | RESOLVED | Note, optional: "The charges concerned helping Enron disguise loans" slightly overstates the $19M Dynegy part, but the previous sentence makes the split clear. |
| 7-3 | 7 | RESOLVED | |
| 7-4 | 7 | RESOLVED | B-073 (same source). The claim includes "testified under oath", and p. 2 (PDF 6) says "testified under oath". |
| 7-5 | 7 | RESOLVED | I updated card B-079 (see section 3). |
| 7-6, 7-7, 7-8 | 7 | RESOLVED | |

## 2. The reused card ids on new citations

- **Same source as the card** (1-4 A-007, 4-6 B-054, 5-4 C-065, 5-7 A-083, 7-1 B-016, 7-4 B-073): the card and the new locator together support each sentence. **Confirmed.**
- **Different source from the card** (5-1 ×2, 5-2, 5-3, 5-6): these need proper cards. I added **F-016 to F-021** to `work/facts/reader-followup.json`. Each is fully checked: fingerprint OK, quote verbatim, and OCR quotes checked against the page image.
  - **F-016** (`batson-1st-interim`, PDF 4-5): the Oct 16 release's $544M charge covered losses on New Power, broadband and technology investments *and* the LJM2 (Raptor) termination.
  - **F-017** (`enron-10q-q3-2001`, **p. 53**, lines 3672-3674): "$710 million ($462 million after tax) related to the acquisition of the Raptor SPEs".
  - **F-018** (`powers-report-sec`, lines 1258-1267): Oct 22 and Oct 24.
  - **F-019** (`batson-1st-interim`, PDF 9): "Approximately $13 billion".
  - **F-020** (`batson-1st-interim`, PDF 8, n. 21): Dynegy "allegedly because of undisclosed liabilities of Enron".
  - **F-021** (`batson-final`, PDF 18, n. 29): the examiner's $544M after-tax charge for the Raptor termination.

**Why 5-1 is NOT RESOLVED.** The sentence "Enron's October 16 announcement put it at $544 million" is cited to Batson Final n. 29. But n. 29 does not mention the announcement. Its "Id." points to the Q3 10-Q, and the 10-Q itself says $462M. The announcement's own $544M line covered more than the Raptors (F-016; page image checked). The 10-Q figure is also on p. 53, not p. 52.

**Required replacement text (ch5, 5-1):**
> The Raptor part of those charges was about $710 million before taxes. Sources differ on the after-tax amount. The special committee and the bankruptcy examiner put it at $544 million[A-058][F-021], the figure in Enron's October 16 announcement, where that charge also covered losses on some other investments[F-016]. Enron's later quarterly report put the Raptor charges at $462 million after tax[F-017].

Citations:
- A-058: powers-report-sec, pp. 127-128.
- F-021: batson-final, PDF 18.
- F-016: batson-1st-interim, PDF 4.
- F-017: enron-10q-q3-2001, p. 53, lines 3672-3674.

**Card repointing required for the writer:**

| citation | point to card |
|---|---|
| ch5, Oct 24 citation | F-018 |
| ch5, second $13-14B citation | F-019 |
| ch5, Dynegy "allegedly" citation | F-020 |
| ch5, 5-1 citations | as listed above |

## 3. Card B-079

Updated in `work/facts/reader-b.json`:
- **Source:** `source_id` changed to `hrg-psi-board`, file `shrg-107-511-role-of-board-2002-05-07.pdf`.
- **Locator:** PDF 100, p. 90, `work/text/hrg-psi-board.txt` lines 6041-6046.
- **Quote:** "We had never had any responsibility to monitor this." (verbatim).
- **Type and verb:** source_type is now "sworn testimony" (witnesses sworn, lines 1259-1269) and the verb is "testified".
- **Notes:** record the report's variant wording.
- **Status:** `checked` = FIXED.

The ch7 citation (hrg-psi-board, PDF 100) now matches the card.

## 4. New or changed sentences read for introduced errors

- Two errors were introduced: the "which" attachment in the formation sentence (ch1, ch6) and the comma/capital typo in ch3.
- Every other changed sentence was read against its source. No new errors, stronger verbs, or unsupported details were found. The ch4 caption is correct (optional refinements are in the table above).

## 5. Corrections log

I appended 35 rows (#23 to #57) to `build-log/corrections.md`. There is one row per Round 2 finding (or group of notes) applied to the chapters, plus the Round 3 B-079 card fix. Rows for 1-5, 3-2 and 5-1 say that a Round 3 fix is still pending.

The Part B instance is appending to the same file at the same time. If its rows also started at #23, the coordinator should renumber.

## Verdicts

| chapter | verdict | remaining required fixes |
|---|---|---|
| ch1 | **FAIL** (one-line fix) | Formation sentence: split it so that "the combined company", not HNG, took the name Enron. |
| ch2 | **PASS** | none |
| ch3 | **FAIL** (one-line fix) | `CalPERS," It found` → `CalPERS." It found` |
| ch4 | **PASS** | none (optional caption refinement) |
| ch5 | **FAIL** | Replace the 5-1 sentence with the text in section 2. Repoint the citations to F-016, F-017, F-018, F-019, F-020, F-021. Use p. 53 for the 10-Q. |
| ch6 | **FAIL** (one-line fix) | Same formation-sentence fix as ch1. |
| ch7 | **PASS** | none |

All remaining fixes are mechanical and fully specified above. After they are applied, ch1, ch3 and ch6 need only a glance. ch5 needs a quick check of the new sentence and the citation targets.

## Final

Final check after the Story Writer applied the Round 3 fixes (see "# Round 3" in `work/facts/fixes-round2-chapters.md`). Date: 2026-09-26.

**The required fixes, re-checked against the sources**
- **ch1 and ch6, formation sentence: RESOLVED.** Both chapters now read "...when InterNorth acquired Houston Natural Gas in July 1985. The combined company took the name Enron in April 1986." Each sentence has its own citation: C-026 (Batson App. B n. 1, PDF 3) and A-001 (JCT p. 59, PDF 87).
- **ch3, typo: RESOLVED.** The text now reads `CalPERS." It found no written record ...`.
- **ch5, 5-1 (after-tax charge): RESOLVED.** The text matches the Round 3 replacement exactly. Citations:
  - A-058 (Powers pp. 127-128)
  - F-021 (batson-final PDF 18, n. 29)
  - F-016 (batson-1st-interim PDF 4)
  - F-017 (10-Q p. 53, lines 3672-3674)
- **ch5, card repoints: RESOLVED.** The citations now point to F-018 (Powers lines 1258-1267), F-019 (batson-1st-interim PDF 9) and F-020 (batson-1st-interim PDF 8, n. 21).

**The new ch4 sentence on Watkins's letter: CORRECT.**
- **Wording:** the quote "I am incredibly nervous that we will implode in a wave of accounting scandals." is verbatim. I read it on the page image of the letter as reprinted in the staff report, rpt-psi-board Appendix 2, printed p. 57, PDF 61.
- **Card:** F-004 (checked FIXED). Its source and locator match the citation: rpt-psi-board, `data-page="61"`, p. 57.
- **Version:** this is the full letter as printed in PSI Appendix 2. Card F-004 records that the House reprint (hrg-hec-collapse-pt4, tab 14) has the same wording. It is not the shorter "Rex Rogers" version.
- **The note that the staff report's quotation differs:** accurate. The report's own text (Finding 4, printed p. 45, PDF 49) prints "nervous that [Enron] will implode in a wave accounting scandals", with "of" missing and "[Enron]" in place of "we" (card F-002, verified in the text layer).
- **Framing:** "reprinted in full as an appendix" is accurate.
- **Consistency with The Footnote page:** the chapter's later note says the letter is quoted "as the Senate subcommittee staff reported it" there. That page quotes a different sentence ("the footnotes don't adequately explain the transactions"), which F-003 confirms matches the letter. So there is no inconsistency.

I made no changes to the ch4 addition, so I added no correction row for it.

**The ch4 caption: CORRECT.** It reads "the Senate Governmental Affairs Committee's opening hearing into the Enron bankruptcy, as identified by the photo's source; Wikimedia Commons dates it January 24, 2002." This matches credits.json, and the manifest dates `hrg-sga-fall-of-enron` to 2002-01-24. The statement that Watkins testified before Senate Commerce in February matches the manifest date for `hrg-commerce-skilling-watkins`, 2002-02-26.

**Whole-chapter sweep (all 255 citations in ch1-ch7)**
- **Cards:** every `data-card` exists in reader-a, reader-b, reader-c or reader-followup, and every one is checked **OK** or **FIXED**.
- **Sources:** every `data-src` is a manifest id.
- **Card and source agree:** no citation's source differs from its card's source (the B-079 mismatch was fixed in Round 3).
- **Candidates:** no file from `sources/candidates/` is cited.
- **Buffett:** absent.

**Corrections log:** in `build-log/corrections.md`, rows #26 (1-5, formation), #34 (3-2) and #44 (5-1) now say "Round 3 (done)". Rows #45, #46 and #48 now name the final cards F-018, F-019 and F-020.

### Final verdicts

| chapter | verdict |
|---|---|
| ch1 | **PASS** |
| ch2 | **PASS** |
| ch3 | **PASS** |
| ch4 | **PASS** |
| ch5 | **PASS** |
| ch6 | **PASS** |
| ch7 | **PASS** |

No required fixes remain for chapters 1-7.

## Revision pass

Date: 2026-09-27. Scope: the ch6 and ch7 sentences changed under "Story Writer (chapters)" in `work/facts/fixes-revision.md`, followed by a whole-chapter sweep of ch6 and ch7.

**The new documents are approved library documents.**
- The 11 new ids are in `sources/manifest.csv`. They were added by the owner's own commit (44168d9, "Add files via upload", [owner's contact email]), and the download action logged them as `OK` with fingerprints.
- I recomputed SHA-256 for all 11, and **all match `download_log.csv`**. Ten are filed in the folder `sources/candidates/`; the eleventh (`hrg-hfs-enron-investors-pt1`) is in `05-hearings-enron`.
- Citing them is allowed: they are in the manifest, not only in `candidates.csv`.
- Note for the coordinator: the site's links will point into a folder named "candidates". That may confuse readers, but it is not a sourcing problem.

**Each changed sentence against its card and source** (read in the source; the Berardino quote checked on the page image)

| ch | change | card(s) | verdict |
|---|---|---|---|
| 6 | Berardino named; "wrote in a statement submitted to a House hearing on December 12, 2001, later quoted in the Powers Report" | G-032, A-048 | **OK.** The quote is verbatim on the statement's p. 116 (PDF 122, page image): "When we reviewed this transaction again in October 2001, we determined that our team's initial judgment that the 3 percent test was met was in error." The header reads "Remarks of Joseph F. Berardino, Managing Partner – Chief Executive Officer, Andersen ... December 12, 2001". The chapter does not call it sworn, which is correct: the record shows no oath (G-031). *Note:* the citation's `data-page` is 119 (the first page of the statement). The quote is on **PDF 122**; changing `data-page` to 122 is recommended. |
| 6 | Indictment: "later alleged that 'Tons of paper relating to the Enron audit were promptly shredded.'" | G-016 | **OK.** Verbatim at indictment p. 5 (line 240). The verb "alleged" is correct. |
| 6 | "indicted Andersen on one count ... alleged that between about October 10 and November 9, 2001, Andersen had corruptly persuaded its employees to withhold and destroy records" | G-015, C-048 | **OK.** Matches "The Charge", para. 13 (a single charge), and 544 U.S. at 702 ("one count"). |
| 6 | "The Supreme Court later recounted that the jury deliberated for seven days, declared itself deadlocked, was urged by the judge to keep trying, and returned a guilty verdict after three more days." | G-022 | **OK.** 544 U.S. at 702. "Urged by the judge to keep trying" is a fair plain-language gloss of the "Allen charge". "Recounted" is the right verb, since this is background in the opinion. |
| 6 | "On May 31, 2005 ... unanimously reversed ... and sent the case back" | G-019 (+ G-018 notes) | **OK.** The date is from the header "Decided May 31, 2005". The opinion itself reads "Rehnquist, C. J., delivered the opinion for a unanimous Court" and "reversed and remanded". |
| 6 | Rehnquist quote "We hold that the jury instructions failed to convey properly the elements of a 'corrup[t] persua[sion]' conviction under § 1512(b), and therefore reverse." | G-018 | **OK.** Verbatim at 544 U.S. at 698 (the printed "there-fore" is a line-break hyphen). The verb "held" is correct. |
| 6 | "honestly and sincerely believed ..."; "it is striking how little culpability the instructions required" | G-020 | **OK.** Verbatim at p. 706. |
| 6 | "without finding any link between the shredding and a particular official proceeding that Andersen had in mind" | G-021 | **OK.** Matches pp. 707-708. |
| 6 | Duncan: "He pleaded guilty in 2002. The Justice Department described the charge as obstructing an SEC investigation into Enron; the Supreme Court's opinion calls it witness tampering. The library does not give the date of his plea, the charging document, or what later happened to the plea." | G-008, G-023 | **OK. The required statement is present and plain**: "The library does not give ... what later happened to the plea." DOJ lines 118-121 and 544 U.S. at 702 are both verbatim-consistent. *Optional wording:* "According to the Justice Department, he pleaded guilty in 2002", since only DOJ gives the year, and "the exact date of his plea". |
| 6 | SEC case "settled ... the day it was filed, without admitting or denying ... permanent court order ... permanent suspension ... subject to court approval"; Bauer, Lowther and Odom "consented, without admitting or denying the findings ... each was barred from practicing before the SEC" | G-029, G-030 | **OK.** Matches Lit. Rel. 20441: "filing and simultaneous settlement"; "subject to court approval"; "denied the privilege of appearing or practicing before the Commission". "Alleged" is kept for the 2008 complaint. |
| 7 | Kopper: $4M + $8M = $12M, the total DOJ "announced for 'both this plea and a related SEC complaint.'" | B-039, G-013 | **OK.** The quote is verbatim (transcript lines 37-38). The arithmetic matches SEC ¶9. The sentence still says his sentence is not in the library. |
| 7 | Fastow: DOJ "announced" the Jan 14, 2004 plea to two conspiracy counts and cooperation; agreement: ten years and >$29M; Sept 26, 2006: six years, >$20M; the differences are unexplained | G-001, G-002, G-004 | **OK.** Matches release #019 (lines 19-32, 71-76) and #06-647 (lines 12-20). The disagreement is stated and attributed, with no figure chosen. |
| 7 | Glisan: pleaded guilty Sept 10, 2003; sentenced the same day to five years under the plea agreement; "the Justice Department announced" | G-006 | **OK.** Release #492, lines 16-26 (60 months). |
| 7 | Causey: DOJ announced a 66-month sentence on Nov 15, 2006 | G-009 | **OK.** Release #06-763, lines 10-15. |
| 7 | Skilling: 2011 "held that the error was harmless, affirmed all of his convictions, and again ordered a new sentence"; "According to a 2013 agreement ... the Supreme Court declined to review that ruling in April 2012"; "the two sides agreed to recommend a sentence of 168 to 210 months ... give up any further challenges"; the imposed sentence is not in the library | G-024, G-026, G-027 | **OK.** CA5 2011 conclusion verbatim-consistent; agreement ¶¶ 6-10. The verbs "held", "according to", "agreed" are correct. *Optional wording:* "to recommend a guidelines range of 168 to 210 months", since the agreement recommends a range, not a sentence. |
| 7 | "Arthur Andersen's conviction ... was reversed in 2005" now cites G-018 | G-018 | **OK.** |

**Whole-chapter sweep, ch6 and ch7** (57 and 66 citations; card files reader-a/b/c, followup and revision)
- **Cards:** every `data-card` exists and is checked **OK** or **FIXED**.
- **Sources:** every `data-src` is a manifest id.
- **Card and source agree:** no citation's source differs from its card's source.
- **Candidates:** no file listed only in `candidates.csv` is cited. The approved ids filed in the candidates folder are cited through their manifest ids, which is correct.
- **Buffett:** absent.
- **Outcomes:**
  - Verbs: "announced" for DOJ and the SEC release, "alleged" for the indictment and SEC complaint, "agreed" for agreements, "held" for courts.
  - Lay: still vacated.
  - Andersen: still reversed, not "innocent", and the post-remand history is still stated as not in the library.
  - Skilling: now affirmed on remand, with the imposed sentence still stated as not in the library.

**Corrections log:** I appended 10 rows (#96 to #105) to `build-log/corrections.md`, one per changed item. I made no edits to the chapters.

### Revision-pass verdicts

| chapter | verdict | required fixes |
|---|---|---|
| ch6 | **PASS** | None. Recommended: set the Berardino citation's `data-page` to 122. Optionally attribute "in 2002" to DOJ and say "exact date". |
| ch7 | **PASS** | None. Optional: "a guidelines range of 168 to 210 months". |
