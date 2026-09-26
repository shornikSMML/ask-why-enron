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
