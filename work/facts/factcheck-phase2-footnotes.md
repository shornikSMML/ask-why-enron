# Fact-check, Phase 2: "Reading the Footnotes" cards N-001 to N-032

Agent: Fact-Checker (instance A). Date: 2026-09-27.
Inputs: `work/facts/reader-footnotes.json` and `work/facts/footnotes-map.md`.
Method: the same as Round 1.

## Summary

| Items | OK | FIXED | REJECTED | NEEDS-SOURCE |
|---|---|---|---|---|
| 32 | 21 | 11 | 0 | 0 |

## How I checked

1. **Fingerprints.** I checked the SHA-256 of all 7 sources the cards use against `sources/download_log.csv`: `enron-10k-2000`, `enron-10q-q3-2001`, `enron-8k-nov-2001`, `powers-report-sec`, `rpt-psi-board`, `rpt-sga-watchdogs` and `batson-final`. All 7 match.
2. **Verbatim quotes, all 32.** A script normalized each quote and found it in its source.
   - 29 quotes matched exactly.
   - N-010 and N-019 matched once typesetting hyphens and dashes were normalized.
   - N-031 comes from OCR text, so I checked it against the page image (Batson Final PDF 24). It is verbatim.
   - I checked each match against the card's locator. Line ranges are right; two .txt citations wrongly carried PDF page numbers (fixed, below).
3. **Claims, verbs and notes.** I read each card's claim and notes against the source text around the locator, not just the quoted line. All 32 cards have a date, dollar amount or share figure, so every one was opened at the source.
   - Verbs are right throughout: company filings "stated/reported", Senate staff "found", Powers "found", Batson "concluded".
   - No card names a person as having done wrong beyond what the source says.

## The three disagreements the coordinator named

- **"$4 billion" (Senate staff) vs "$3.9 billion" (Q3 2001 10-Q).**
  - N-022 and N-028 state both figures, with attribution. The Senate staff figure cites the 10-Q and an interview (SGA n. 133).
  - Writers: give the 10-Q's $3.9 billion as the filing's figure, and quote "a whopping $4 billion" only as the staff's words.
- **Note 9 JEDI figures are not to be combined.**
  - N-014 already warned not to add Powers's $126 million (JEDI's Enron-stock income in Q1 2000) to Note 9's $197 million (JEDI's 2000 equity earnings). Neither source links the two. The warning is kept.
  - I added two more cautions. In N-014: the "50%" figures are *voting* interests, and Note 9 says income-sharing ratios can differ. In N-021: Note 11's "about 12 million shares with JEDI" and Powers's "JEDI held 12 million shares of Enron stock" are separately sourced, and no document says they are the same shares.
- **The 50-percent vs 3-percent rules.**
  - N-019 correctly warns that the SGA staff's "at or near 50 percent" point concerns ordinary equity-method affiliates. The 3% outside-equity test governed SPEs (A-030).
  - N-022 and N-025 also keep two different trigger rules apart. The 2000 10-K triggers are a stock-price decline **or** a downgrade. The 10-Q's Osprey and Marlin triggers need **both** at once ("concurrent with").

## Corrections (logged as rows #110 to #120 in `build-log/corrections.md`)

| Card | What was wrong | Fix |
|---|---|---|
| N-005 | The notes inferred "the book roughly doubled during 2000" from the $11,860M figure, which is an average of month-end values, not a starting point. | Replaced with the 10-K's own year-end figures: $21,458M at end-2000 vs $5,471M at end-1999 (credit-risk table). |
| N-006 | The notes stressed the 23-29-year maximum terms without the note's own counterweight. | Added the counterweight from the note: maximum terms "are not indicative of likely future cash flows", and the weighted average maturity was about 1.5 years. |
| N-008 | The claim said "credit reserves of $452 million". | The table line is "Credit and other reserves". Claim reworded. |
| N-009 | The JCT cross-reference was wrong (p. 86). JCT also gives a different figure from PSI. | Corrected to p. 87 n. 141 (PDF 115). Recorded the disagreement: JCT says $8-10 billion for the price-risk adjustment, PSI says $10 billion. |
| N-014 | The 50% figures were given with no qualification. | Added the caution that 50% is a voting interest and income sharing can differ. |
| N-017 | The locator gave `pdf_page 64` for a .txt source. | Set to null. The printed page and line numbers are kept. |
| N-018 | The claim misread the 10-Q as saying "Whitewing invested through ... Osprey". | The 10-Q says Whitewing was formed by Enron and investors "investing through an entity named Osprey". Claim reworded. |
| N-019 | The notes cited a secondary figure (Bratton, via SGA) of "$23.4B of balance-sheet assets", which conflicts with Enron's reported $65.5B. | Warning added: do not use it or the 22.6% share. |
| N-021 | The two separately sourced "12 million share" figures could be read as the same shares. | Caution added. |
| N-029 | The notes gave PSI's "$27 billion off-balance-sheet" without comment. | Warning added: do not equate it with the $25.116B of additional "debt" in the Nov 19, 2001 bank presentation (A-087). They are different measures from different sources. |
| N-030 | The locator gave `pdf_page 184` for a .txt source. | Set to null. |

## Verdict per card

- **OK (21):** N-001, N-002, N-003, N-004, N-007, N-010, N-011, N-012, N-013, N-015, N-016, N-020, N-022, N-023, N-024, N-025, N-026, N-027, N-028, N-031, N-032.
- **FIXED (11):** N-005, N-006, N-008, N-009, N-014, N-017, N-018, N-019, N-021, N-029, N-030.

Each card now carries `checked` and a `checker_note` with its exact locator lines. All 32 cards are fit for use in the "Reading the Footnotes" pathway.

## Notes for writers

- **Verbs.** N-009, N-010 and N-029 are Senate PSI findings: write "the Senate subcommittee staff found". N-019, N-027 and N-028 are Senate Governmental Affairs staff: write "the committee staff reported". N-019 and N-028 attribute points to "experts" and "a witness", and that attribution must stay.
- **N-031** is the pathway's closing lesson. It is a direct examiner conclusion, so "the bankruptcy examiner concluded" is right. No "a fact-finder could conclude" hedge is needed here.
- **Where the details are.** The 2000 10-K never uses the words "special purpose", "Osprey" or "Marlin". The stock-price obligations are in Notes 10 and 11 and the MD&A, not in Notes 14-15. The cards say this correctly.
- **The Q3 2001 10-Q repeats some passages.** The Whitewing and Osprey passage appears twice (lines 2124-2162 and about 4860-4900). Cite the Note 8 copy (p. 32) that the cards use.

## Read log

- **enron-10k-2000** (.txt), lines: 1942-1944, 2944-2960, 3095-3120, 4091-4108, 4233-4240, 4376-4520, 4634-4690, 5014-5151, 5165-5210, 5322-5338, 5678-5690, 5808-5858. I also text-searched the whole file for "special purpose", "nonconsolidat", "Osprey" and "Marlin".
- **enron-10q-q3-2001** (.txt), lines: 1540-1565, 2118-2200 (plus grep hits at 719, 4681, 4868, 4897).
- **enron-8k-nov-2001** (.txt), lines: 51-72, 263-296.
- **powers-report-sec** (.txt), lines: 2252-2312, 6368-6395.
- **rpt-psi-board**, PDF pages (text copy): 19, 24, 40, 51, 52.
- **rpt-sga-watchdogs**, PDF pages (text copy): 29, 30, 33, 34.
- **batson-final**: PDF 24, checked on the page image in Round 2.
- **rpt-jct-vol1**: text copy PDF 115 (n. 141), to check N-009's cross-reference. The fingerprint matched in Round 2.

No web used and no gaps logged.
