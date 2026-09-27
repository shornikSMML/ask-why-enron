# Phase 2 fact-check: Pathways and "Other notes in the same report"

Fact-Checker A, 2026-09-27. I did not edit any draft. Fixes go in `work/drafts/pathways.json`, `work/drafts/footnote-others.json` and `footnote-others-intro.txt`. Then re-run `work/tools/integrate.py`, because `js/footnote-others-data.js` is generated from these drafts.

## Method

- **Fingerprints.** I re-checked the fingerprints against `sources/download_log.csv`. All three match:
  - enron-10k-2000 (940e08b2…)
  - enron-10q-q3-2001 (6a2a8be8…)
  - enron-8k-nov-2001 (d7479137…)
- **Excerpts.** A script compared each of the 18 excerpts with the source lines it cites, after normalizing whitespace.
- **Cited quotes.** A script matched each of the 40 quotes in `cites` against its file:
  - For .txt sources, at the stated lines.
  - For PDFs, on the stated page of the `work/text` copy, ignoring punctuation and OCR noise.
  - The Batson quotes (A-067, A-068, A-070) had already been checked against the page images.
- **Claims.** I read every "said / left out / found" claim against the 10-K, 10-Q and 8-K text. I read these directly:
  - 10-K lines 4153-4175, 4430-4505, 4634-4686, 4950-5210, 5810-5852, 6324-6331
  - 10-Q lines 2120-2200
  - 8-K lines 55-75 and 270-285
  - Powers lines 3655-3665 and 4850-4868
  - PSI board report PDF pp. 19-24
  - SGA watchdogs report PDF pp. 33-34
- **Pathways.** I read all 7 pathways and 68 stops: intros, bridges, closing questions, handout stops and discussion questions. I checked every fact against the cited card, and also against what the target page actually says. The target pages were:
  - ch2-ch6 sections
  - the Cast entries for Fastow, Kopper, Lay, Skilling, Duncan, Temple, Berardino, Merrill Lynch executives, and JPMorgan/Citi
  - the timeline entries tl-1992, tl-1999-12, tl-2002-07-30, tl-2003-04-25 and tl-2003-07-28, plus the `auditors` tag set
  - Why It Matters, sections #s302 to #today
  - the restatement chart SVG
  - the Glossary ids

**Mechanical result:**
- 18 of 18 excerpts are verbatim at their lines.
- 40 of 40 cited quotes are found at their stated lines or page.
- Every card cited in pathways.json is checked (OK or FIXED).

## Findings

| # | Item | Problem | Source | Required fix | Severity |
|---|---|---|---|---|---|
| P-1 | pathways: footnotes, stop 5 (Note 9) bridge **and** handout stop | "Note 9 listed JEDI and Whitewing, each 50% owned and not consolidated." The 50% figure is a *net voting interest*. Note 9's own footnote (a) warns that income-sharing ratios can differ. This is the same point fixed in N-014 and repeated in the note-9 "left out" text. | 10-K lines 5020-5043; N-014 | Replace with: "Note 9 listed JEDI and Whitewing, each with a 50% voting interest and not consolidated." | should-fix |
| P-2 | pathways: spes, closing question (bridge and handout) | "if an independent owner had at least 3% of its value at risk". The rule as the site states it (A-030) is 3% of the SPE's *assets*, plus control by that owner. | Powers lines 451-463; A-030 | Replace "3% of its value at risk" with "3% of its assets at risk". | minor |
| P-3 | pathways: mark-to-market, stop 1 | "fair value and unrealized gain, come up at every later stop" overstates. They do not come up at the restatement chart or at every other stop. | — | Replace "come up at every later stop" with "come up again and again". | minor |
| P-4 | pathways: andersen, stop 9 | "from the 1985 merger". The timeline item and ch6 describe InterNorth buying Houston Natural Gas. | timeline 1985-07-01; ch6 "Enron's auditor" | Replace "from the 1985 merger" with "from InterNorth's 1985 purchase of Houston Natural Gas". | minor |
| P-5 | pathways: banks, intro | "'prepays,' deals that looked like trades but worked like loans" states a characterization of real banks' deals without attribution. Chapter 5 and the Cast attribute it to the Senate subcommittee staff. | A-072 | Replace with: "'prepays,' deals that Senate investigators found looked like trades but worked like loans". | minor |
| P-6 | card A-072 (cited at banks stop 1): information only, no pathway change | The card correctly paraphrases the PSI report's "sham asset sale ... just before the end of the year 2000". The SEC complaint dates the Merrill barge deal to December 1999, which is what the timeline and the Banks page use. The pathway bridge does not repeat either date, so nothing is wrong on the pages. | rpt-psi-fishtail PDF 5 (p. 1); sec-merrill-complaint para. 1 | Optional: if the Banks page ever quotes that PSI sentence, note the date difference. | info |
| F-1 | footnote-others note-1, excerpt 3 (lines 4170-4172) and "said" | The excerpt stops mid-sentence at "management's best estimate". The source continues "considering various factors including closing exchange and over-the-counter quotations, time value and volatility factors underlying the commitments." Cutting it there, and then quoting "management's best estimate" in "said", hides that the note named market quotations as one input. | 10-K lines 4170-4174 | Extend the excerpt to the full sentence (lines 4170-4174, text as in the source). Or end it with "…" and add to "said": "…'management's best estimate,' considering factors that include exchange and over-the-counter quotations." | should-fix |
| F-2 | note-1, "left out" | "A search of the whole 10-K finds no mention of SPEs or of those rules." The phrase "special purpose", the abbreviation "SPE" and the 3% rule are indeed absent (I searched the whole file). But Note 16 does describe the Raptor SPEs, calling them "the Entities" (lines 5876-5913). The q3-10q entry says so itself. "No mention of SPEs" therefore overstates. | 10-K full-text search; lines 5876-5913 | Replace with: "A search of the whole 10-K finds no use of the term 'special purpose entity' and no statement of those rules." | should-fix |
| F-3 | note-1, "found" | "the board 'did not object …'". The PSI text says "Board members were told about a dispute … and did not object". | rpt-psi-board PDF 24, p. 20; N-009 | Replace with: "…found that in May 2000 board members were told of an internal dispute over valuation and 'did not object when the company decided to go with the more aggressive valuation model.'" | minor |
| F-4 | note-3, "said" | "$1,899 million of income before interest and taxes" drops part of the note's own definition. The note says "income before interest, taxes and certain unallocated expenses". | 10-K lines 4450-4452 | Replace with: "$1,899 million of income before interest, taxes and certain unallocated expenses". | should-fix |
| F-5 | note-3, "found" (96%) | "He concluded that in 2000, six accounting techniques … produced 96%". The Final Report summarizes this from an earlier interim report. Chapter 5 words it that way. | batson-final PDF 21, p. 18; A-067 | Optional, for consistency with ch5: "In his Final Report he summarized an earlier conclusion that in 2000 …". | minor |
| F-6 | note-4, "found" (buy-backs) | "Enron bought back five of the seven assets it sold in the last two quarters of 1999" reads as if it covered all of Enron's asset sales. Powers is describing sales **to the LJM partnerships**, and says the buy-backs came "after the close of the relevant financial reporting period". The cite is tagged card N-012, which is about Note 4's gains. The finding is card A-044. The entry's `cards` list also names A-046 (the Rhythms share transfer) where A-044 is meant. | Powers lines 4850-4868; A-044 | Replace with: "It also found that Enron bought back five of the seven assets it had sold to the LJM partnerships in the last two quarters of 1999, in some cases within three months." Change that cite's `card` from N-012 to A-044. In `cards`, replace A-046 with A-044. | should-fix |
| F-7 | note-4, "found" (Raptors) | "let Enron avoid reporting 'almost $1 billion in losses …'" leaves out the period and the income-statement point. | Powers lines 3655-3659 | Replace with: "…found that from the third quarter of 2000 through the third quarter of 2001, the Raptors let Enron avoid reflecting 'almost $1 billion in losses on its merchant investments' on its income statement." | minor |
| F-8 | note-4 and note-9, "found" (SGA red flags) | Neutrality. The same SGA paragraph that lists these warning items says: "None of these items … in and of itself, is necessarily an indication of fraud". | rpt-sga-watchdogs PDF 34, p. 30 | Optional: in note-9, add "The staff added that none of these items was, on its own, necessarily a sign of fraud." | minor |
| F-9 | note-9, "left out" (Kopper) | "…says that an Enron employee, Michael Kopper, ran it" is a claim about a real person with no visible citation. A-032 is not in `cites` or `cards`. | Powers lines 1702-1727; A-032 | Add a cite to A-032 (powers-report-sec, pdf_page 49, "Powers Report, pp. 43-44, II.A Formation of Chewco (lines 1702-1727)") and add A-032 to `cards`. | should-fix |
| F-10 | note-9, "left out" (Whitewing debt) | "It does not mention Whitewing's debt or Enron's promise to issue shares to cover it; those appear only in Note 10 and, in full, in the 2001 10-Q." Note 10 has the Share Settlement Agreement: extra shares if Enron's stock falls below $48.55. It does **not** mention Whitewing's (Osprey's) debt, or Enron's liability for a shortfall on that debt. No part of the 10-K does; "Whitewing" appears only at the lines listed in the source column. | 10-K lines 5170-5192; 10-Q lines 2124-2133 | Replace the sentence with: "It does not mention Whitewing's debt. Enron's promise to deliver extra shares to Whitewing if its stock fell appears only in Note 10; Whitewing's debt, and Enron's duty to cover any shortfall, appear only in the 2001 10-Q (see below)." | should-fix |
| F-11 | note-15, "said" | "$264 million of letters of credit". The note says Enron guaranteed affiliates' performance "in connection with letters of credit", and $264 million of such guarantees were outstanding. | 10-K lines 5838-5841; N-024 | Replace with: "$264 million of guarantees tied to affiliates' letters of credit". | minor |
| F-12 | q3-10q, "said" | "Nearly eight months after the annual report was signed" is correct: the 10-K was signed March 30, 2001, and the 10-Q is dated November 19, 2001. But there is no cite for the 10-K signing date. | 10-K lines 6327-6331 | Add cite: enron-10k-2000, pdf_page null, "Enron 2000 Form 10-K, Signatures (lines 6327-6331)", quote "on this 30th day of March, 2001". | minor |
| F-13 | q3-10q, "said" | "up to $3.9 billion could come due". The 10-Q says a trigger "could require Enron to repay, refinance or cash collateralize" facilities totaling $3.9 billion. | 10-Q lines 715-720 | Replace with: "Enron could have to repay, refinance or put up cash for as much as $3.9 billion". | minor |
| F-14 | q3-10q, "left out" | "Its notes gave trigger prices but no dollar amounts". Note 10 does give dollar figures, for example the $1.0 billion liquidation value of the Series B preferred held by Whitewing (line 5191). What is missing is the size of the debt that could come due. | 10-K lines 5189-5192 | Replace with: "Its notes gave trigger prices but no dollar amount for the debt that could come due, named neither trust, …". | minor |

## Items checked and found supported (no change)

**Footnote intro.** "About twenty numbered notes" is right: the 10-K's notes run from 1 to 20. The rest of the intro is framing.

**note-1:**
- The consolidation sentence and the mark-to-market paragraph.
- The 8-K "should have been consolidated" and "should not be relied upon" quotes: 8-K lines 61-65 and 71-72, where it is a determination "by Enron and its auditors".
- PSI "regularly informed … invited scrutiny": PDF 19, p. 15.

**note-3:**
- $21,458M and $19,918M: fair value table, line 4444.
- About $5.5 billion a year earlier, before reserves: credit table, line 4502, $5,471M.
- The notional-amount warning.
- $381M of securitization gains and $545M from Whitewing.
- "See Notes 4 and 9".
- The "concurrently enters into swaps" quote.
- Batson "bridge financings" and "retained substantially all" (A-068, image-checked).

**note-4:**
- $601M vs $1,086M.
- Valuation methods.
- $104M, $756M and $628M.
- The "refined" VaR model (Item 7A note (c)).
- The SGA "flashing red light", which is correctly given as a witness's testimony reported by staff.

**note-9:**
- $5,294M.
- JEDI 50%/$399M, JEDI II 50%/$220M, Whitewing 50%/$558M.
- JEDI equity earnings of $197M.
- $632M and $192M in sales to Whitewing.
- "Separate legal entities".
- 8-K Restatement 1 quote.
- Powers $126M quote.
- "Should not be added together", consistent with the N-014 and N-017 ruling.
- SGA "at or near 50 percent".
- The 3% vs 50% distinction (A-030).

**note-15:**
- $1,863M and $556M.
- The MD&A trigger text and the $28.20-$55.00 range.
- Note 10 $48.55.
- Note 11: 54.8M shares, 22.5M of them with related parties.
- SGA $4B vs 10-Q $3.9B, with the difference stated.
- $1.0B due to Whitewing at September 30, 2001.
- Batson "essentially a recourse basis".
- OR vs AND triggers, correctly contrasted.

**q3-10q:**
- Osprey: $2.4B debt.
- Marlin: $915M, tied to Azurix.
- $59.78 and $34.13 triggers.
- The shortfall clause.
- $9.00 on November 16.
- 30 million Raptor shares.
- Going-concern warning.
- "Osprey" and "Marlin" absent from the 10-K (full-text search).
- Raptors called "the Entities".
- PSI nine-page contrast (N-029).

**Pathways.** Every other bridge, intro, closing question and handout item is framing or matches its cards and the target page. Specifically:
- Fastow and the LJM approvals (A-040, A-041). The Cast uses "alleged", "pleaded guilty" and "sentenced", and the two forfeiture figures differ as the bridge says.
- "Four years" of statements (A-083).
- The Dynegy disagreement is stated in ch5.
- Lay's vacated conviction and Skilling's open items match the Cast.
- The 1991 vs 1992 start matches tl-1992.
- "Not a normal hedge" echoes the Powers quote in ch3.
- The restatement chart shows reported and restated profit for 1997-2000.
- Kopper was "put in [Fastow's] place" (A-032; Cast).
- LJM2 controls (A-041).
- Duncan's handwritten note (B-063). Jaedicke "testified … as far as he recalled", as in ch4.
- Fee disagreement and Andersen's dispute over the label (ch6).
- "Errors and what the examiner concluded" exists in ch6.
- Temple's e-mail is quoted in ch6; the Cast says no charges are shown.
- The Supreme Court reversal, 2005.
- The GAO found / not yet found (ch6).
- Certification (C-076).
- Watkins "testified she sent" (B-055).
- The PCAOB ready date (C-081).
- "Where the library's documents stop" is present in Why It Matters #today.
- Note 9 → Note 16 "the Related Party" (N-015).
- The Q3 10-Q nine-page contrast (N-029).
- C-054, the SEC review "likely to have prompted questions".
- "Year-end deals with Merrill Lynch" (tl-1999-12, B-083).
- The JPMorgan/Citi "without admitting or denying" wording (B-086).
- Merrill executives "outcome not in library".

The verbs are right throughout: "alleged", "pleaded guilty", "concluded … fact-finder", "testified" (for sworn settings only), "found" and "reported". The tone is neutral.

**Anchors (not a fact issue).** Many anchors in pathways.json still depend on `pathway-anchor-requests.md`: h2 ids, figure ids, timeline item ids, `?tag=`, `#fn-NN`, and `#note-N`. The Site Builder should confirm they resolve before the pathways go live.

## Correction applied (logged)

- Card N-012, notes field: the cross-reference A-046 is changed to A-044, the card for the buy-back finding. See `build-log/corrections.md` row 167.
- No draft was edited.

## Verdicts

| Item | Verdict |
|---|---|
| Pathway: first-reading | PASS |
| Pathway: mark-to-market | PASS (P-3 minor) |
| Pathway: spes | PASS (P-2 minor) |
| Pathway: andersen | PASS (P-4 minor) |
| Pathway: sox | PASS |
| Pathway: footnotes | PASS AFTER FIX P-1 |
| Pathway: banks | PASS (P-5 minor) |
| Footnote intro | PASS |
| note-1 | PASS AFTER FIXES F-1, F-2 (F-3 minor) |
| note-3 | PASS AFTER FIX F-4 (F-5 minor) |
| note-4 | PASS AFTER FIX F-6 (F-7, F-8 minor) |
| note-9 | PASS AFTER FIXES F-9, F-10 |
| note-15 | PASS (F-11 minor) |
| q3-10q | PASS (F-12 to F-14 minor) |

**Totals:** 7 should-fix (P-1, F-1, F-2, F-4, F-6, F-9, F-10), 12 minor, 1 information-only. There are no critical errors: every excerpt is verbatim, and no uncited accusation appears.

## Final

Re-check of `fixes-phase2-pathways.md` (P-1 to P-5) and `fixes-phase2-footnote-others.md` (F-1 to F-14), Fact-Checker A, 2026-09-27.

**How I checked.** I read each changed field in `work/drafts/pathways.json` and `work/drafts/footnote-others.json`. I also confirmed that the regenerated files `js/pathways-data.js` and `js/footnote-others-data.js` carry the new wording.

**Pathways.**
- All five fixes are applied as written, in both the bridge and the handout where the text appears in both.
- None of the old wording remains anywhere in pathways.json.

**Other notes.**
- All 14 fixes are applied as written.
- The script re-check passes:
  - All 18 excerpts are verbatim at their lines, including note-1 excerpt 3, which now covers lines 4170-4174 and is the full sentence.
  - All quotes in the .txt sources appear at their stated lines. This includes the new A-032 Kopper quote (Powers lines 1702-1727) and the new 10-K signing-date quote (lines 6327-6331).
  - The new SGA "None of these items ..." quote appears on PDF page 34.
  - The remaining PDF quotes match once punctuation and OCR noise are ignored, as before.
- The note-4 buy-back cite now points to A-044, and A-046 has been replaced in its `cards` list.
- note-9 now lists A-032, and cites it.

No new problems found.

**Logged.** The applied corrections are rows 168-186 in `build-log/corrections.md`.

| Item | Final verdict |
|---|---|
| Pathways: first-reading, mark-to-market, spes, andersen, sox, footnotes, banks | PASS |
| Footnote intro | PASS |
| note-1, note-3, note-4, note-9, note-15, q3-10q | PASS |
