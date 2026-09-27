# Fact-check, Round 1: fact cards and footnote annotations

Agent: Fact-Checker. Date: 2026-09-26. I worked independently of the Readers and the Footnote Annotator and did not rely on any card's quote.

## Summary

| File | Items | OK | FIXED | REJECTED | NEEDS-SOURCE |
|---|---|---|---|---|---|
| `work/facts/reader-a.json` | 97 | 94 | 3 | 0 | 0 |
| `work/facts/reader-b.json` | 86 | 74 | 12 | 0 | 0 |
| `work/facts/reader-c.json` | 81 | 78 | 3 | 0 | 0 |
| `work/drafts/footnote.json` (annotations, including 2 context annotations) | 35 | 32 | 3 | 0 | 0 |
| **Total** | **299** | **278** | **21** | **0** | **0** |

Plus the footnote's intro, closing, and the Note 16 text itself: all OK.

**How I checked**
1. **Fingerprints.** I computed SHA-256 for all 48 library files cited by any card or annotation and compared each with `sources/download_log.csv`. All 48 match. For the Buffett search I also used the text copies of `sox-hrg-banking-v1/-v2/-v3`, `hrg-psi-board`, `hrg-sga-analysts` and `hrg-hec-auditing`.
2. **Verbatim quotes, all 409 of them.** A script normalized each quote and searched for it in the source text, split at ellipses and brackets, and recorded the PDF page where it matched. That covers every card quote, every annotation citation, and the full Note 16 text. Every quote was found. The few that did not match exactly were checked by hand: they were page breaks, two-column layouts, footnotes in the middle of a sentence, OCR misreads, or typesetting hyphens. The last I fixed (correction 12).
3. **Page images.** I opened the page image for every card built from OCR or image-only text: 50 pages covering 66 cards, plus the 4 Batson pages cited in the annotations. Every OCR quote and figure matched the image.
4. **Meaning, verbs and outcomes.** I read every card and every annotation in full: claim, notes, verb and source type. Numbers in the claims were checked against the cited pages and then by hand. The brief asked for every card that names a person or has a date or dollar amount, plus a 25% sample of the rest. Almost every card falls in the first group, so in practice I checked all of them.
5. **Outcomes.** No card calls anyone guilty whose conviction was reversed or vacated. Andersen: B-064, C-038, C-043 always say it was reversed. Lay: B-010 and B-011 say his conviction was vacated. Skilling: B-028 says the Supreme Court affirmed in part and vacated in part, not overturned. No card calls anyone "never charged". Absence cards (B-058, B-082) use "the library documents show no charges". The verbs are right throughout: SEC complaints "alleged", Batson "concluded" at the fact-finder standard, the Powers committee "found", hearing witnesses "testified". Where a witness was not shown sworn, the card says "told the committee" (Powers, Longstreth).

**Most important fix:** annotation **fn-11** on the Footnote page said the $172 million Raptor note correction was separate from Enron's October 2001 $1.2 billion cut to shareholders' equity. The Powers Report says the opposite: that correction ($172M plus $828M) was $1 billion of the $1.2 billion. Fixed and logged. All 15 corrections are in `build-log/corrections.md`.

**Addendum item: Andersen's CEO (card A-048).** Do **not** name Joseph Berardino as the speaker of the December 12, 2001 quote. Powers says only "Andersen's CEO". The library has no transcript of that hearing. The February 2002 transcript names Berardino as CEO and has him refer to an earlier appearance, but it does not show who testified on December 12 or what was said. The site may say: "Andersen's chief executive told Congress in December 2001, as quoted in the Powers Report, ..." I logged a gap for the transcript.

## Reader-tip rulings

### Tip 1: "Warren Buffett read Enron's footnote, didn't understand it, and threw the 10-K away."

**Ruling: EXCLUDE. Logged as gap (`factcheck-gaps.md` #1).**

I searched every text copy in `work/text/`, plus the `.txt` SEC filings and the Powers Report, for "Buffett" and the misspelling "Buffet". Reader A's search missed the misspelling. Buffett is mentioned in seven documents. **None connects Buffett to Enron's footnote, its 10-K, or any reading of Enron's filings.** Here is what each says:

| Document | Where | What the mention actually says |
|---|---|---|
| `hrg-sga-analysts` (Feb 27, 2002) | PDF 56, line ~3392, testimony of Thomas A. Bowman, CFA (Association for Investment Management and Research), sworn | General investing advice: "Warren Buffett ... advises that if you don't understand the company, don't buy it." Nothing about Enron's filings. This is the closest in spirit, and it is still not support. |
| `hrg-hec-auditing` (Feb 6, 2002) | PDF 128-132, lines 7164, 7191, 7436 (prepared statement of David L. Sokol, MidAmerican) | Buffett as MidAmerican's largest investor, who planned to invest in utilities if PUHCA were repealed. |
| `hrg-hec-auditing` | PDF 141, line ~8013 (James Chanos, answering a question) | Chanos paraphrases Buffett's questions about stock-option accounting. |
| `hrg-hec-auditing` | PDF 153, line ~8771 (Rep. Ganske) | A congressman recalls that Buffett said he could not figure out how to value high-tech companies. General, and not about Enron. |
| `hrg-psi-board` (May 7, 2002) | PDF 30, lines 1704-1714 (Robert Jaedicke) | Buffett's 1999 letter to NYSE chairman Grasso about audit committees. |
| `hrg-psi-board` | lines 3598-3790 (Sen. Durbin) | Berkshire Hathaway annual report: stock options and a joke about repricing options. |
| `sox-hrg-banking-v1` | lines 6508, 6831 | Robert Denham's biography; Buffett as a member of a plain-English disclosure group 26 years earlier. |
| `sox-hrg-banking-v2` | PDF 600, line 29215 (SEC Chairman Pitt) | Buffett's questions for audit committees at an SEC roundtable on March 4 [2002]. |
| `sox-hrg-banking-v3` | about 35 mentions, lines 14997-24982 | Nearly all about expensing stock options (Buffett's op-ed in the Washington Post, Apr. 9, 2002, read into the record; senators citing him). Two mentions sit near "post-Enron reform", but about options, not the footnote. |

**What would be needed:** a first-hand, attributable record in an official or primary source. That could be Buffett's own sworn testimony or a statement in an official record (hearing transcript, SEC filing, or his Berkshire Hathaway shareholder letter). It would have to say that he read Enron's related-party footnote or 10-K and gave up on it. A press anecdote or retelling would not be enough, and copyrighted interviews could not be quoted. Importance: minor. The story does not need it. Card A-064 and the Footnote page already show from primary sources that readers could not understand Note 16.

### Tip 2: "At its peak, Enron was America's seventh-largest company."

**Ruling: MAY BE STATED, but only in attributed form with the measure given. Do not say "at its peak."**

What the library says (image-checked where OCR):
- **JCT staff report** (`rpt-jct-vol1`, printed p. 58, PDF 86, image-checked): "Enron reported consolidated revenues of $101 billion for 2000, and ranked seventh on the Fortune 500 list of the country's largest companies for 2001." Footnote 53 adds: "Enron moved up to fifth place on the Fortune 500 list for 2002, and was sixth on Fortune's 2002 Global 500."
- **Batson Final Report** n. 27 (PDF 18, image-checked) and **First Interim Report** n. 1 (PDF 3, image-checked), same words: "Fortune magazine ranked Enron as the seventh largest corporation in the world, based upon revenues," citing *The 500 Largest U.S. Corporations*, Fortune, Apr. 16, 2001. Internal inconsistency: the text says "in the world", but the list cited is the U.S. list.
- **SEC Kopper complaint** para. 9: "Prior to December 2, 2001, Enron was reportedly the seventh largest corporation in the United States." This is an allegation, hedged with "reportedly", and it gives no measure.
- **Skilling indictment** para. 1: "the seventh largest corporation in the United States"; p. 9 (line ~389): "seventh-ranked company in the United States, according to the leading index of the 'Fortune 500.'" These are allegations.
- **Senate PSI reports** (`rpt-psi-board` pp. 1, 6; `rpt-psi-fishtail` p. 1): "listed as the seventh largest company in the United States". No measure given.
- Many hearing statements by members repeat the phrase. They are not findings.

**Why not "at its peak":** by the JCT's own footnote, the 2002 Fortune list (based on 2001 revenue) ranked Enron **fifth**. "Seventh" was not its peak ranking. Also, the ranking is by **revenue**, which is not profit or market value, and Enron's revenue was swollen by counting the full value of its trades (cards A-018, A-024).

**Wording the site may use:**
> "In 2001, *Fortune* magazine ranked Enron seventh on its list of the 500 largest U.S. companies, measured by revenue."

Cite `rpt-jct-vol1`, p. 58 (PDF 86) and `batson-final`, p. 15 n. 27 (PDF 18). A shorter form is also acceptable in running text: "then ranked seventh among U.S. companies by revenue (*Fortune*, 2001)". Do not use: "America's seventh-largest company" without the measure and the year, "seventh-largest in the world", or "at its peak".

## Source disagreements: how the site should present each

Default: give the primary figure with attribution and note the difference. I pick a figure only where one source is clearly the correction of another.

| # | Topic | What the sources say | Card(s) | How the site should present it |
|---|---|---|---|---|
| 1 | Restatement figures (net income cuts, 1997-2000) | Nov 8 8-K/press release: -96/-113/-250/-132 ($M). Nov 19 10-Q: -79/-139/-258/-137 (restated net income 26/564/635/842). Powers: -28/-133/-248/-99 (Chewco and LJM1 only, without audit adjustments). Batson: $586M aggregate (the 8-K figure). Debt increases (+711/561/685/628) are the same in all. | A-039, A-084, A-085, A-086, A-087 | Use the **10-Q** figures. The 10-Q says it refines the 8-K ("further refinement"), so it is a correction, not a rival. Footnote: "Enron's first estimate on Nov 8 was slightly different." Use Powers figures only when discussing Chewco and LJM1 alone, and label them. Cards state all of this accurately. |
| 2 | Q3 2001 loss | $618M (Oct 16 release, per Batson), $635M (Nov 8 8-K restated), $644M (Nov 19 10-Q) | A-075, A-077 | "Enron first announced a $618 million third-quarter loss; its quarterly report filed Nov 19 showed $644 million." Stated accurately. |
| 3 | Raptor termination charge | $710M pre-tax: all agree. After tax: $544M (Oct 16 release; Powers pp. 98, 128; Batson) vs $462M (10-Q, charge "related to the acquisition of the Raptor SPEs", plus a separate $31M after-tax NPW warrant write-down) | A-058, fn-18 | Lead with "$710 million before taxes." If an after-tax figure is needed: "Enron's Oct 16 announcement put it at $544 million after taxes; its later 10-Q reported $462 million." Stated accurately. |
| 4 | $1.2B equity reduction split | Powers: $1B error correction + ~$200M termination. 10-Q: $270M "not related to the restatement". | A-059, C-030, fn-11 | "About $1 billion of the $1.2 billion corrected an accounting error; the rest (about $200 million, per Powers) related to ending the Raptors." fn-11 corrected (it had this backwards). |
| 5 | LJM2 formation and approval date | Formed Oct 1999 (Powers) vs "funded/founded in December 1999" (Batson First Interim p. 3; Final n. 29). Board approval Oct 11 (Powers: "later that day") vs Oct 12 (PSI: "the following day"). | A-041, B-072 | "The board approved LJM2 in October 1999; it began investing in December 1999, according to the bankruptcy examiner." Avoid a single day, or say "Oct. 11 or 12". A-041 note corrected. |
| 6 | Bankruptcy filing date | Dec 2, 2001: Powers, Batson (all reports), JCT, PSI, Skilling indictment, App. B. Dec 3: SEC Kopper complaint only. | A-013, A-092, C-059 | Use **December 2, 2001**. Don't cite the Kopper complaint for the date. No footnote needed. |
| 7 | Andersen's fees from Enron, 2000 | $52M ($25M audit, $27M consulting): Senate Governmental Affairs staff. ~$54M: Batson App. B, from Andersen's internal presentation (Andersen's fiscal year ended Aug 31). $47.9M: April 2001 Audit Committee presentation, and the Batson Final Report's own main text (p. 39). Andersen's Andrews testified $25M was audit-related, "essentially half". | C-019, C-020, C-021, C-022, C-024 | "About $50 million in 2000 (sources give $47.9 to $54 million, depending on the accounting year and categories), roughly half for the audit itself." Attribute any exact figure. |
| 8 | Skilling's promotion to President/COO | Dec 1996 (SEC First Amended Complaint) vs Jan 1997 (indictment, SEC Second Amended Complaint, CA5) | B-017 | "January 1997" citing the indictment. The later SEC complaint agrees, so the Dec 1996 date looks like an early error. Optional footnote. |
| 9 | Skilling's pay 1998-2001 | "more than $14 million" salary and bonus (SEC) vs "more than $8 million" (DOJ press release) | B-020 | Attribute each ("the SEC alleged..."). Don't combine them or pick one. |
| 10 | Skilling's charges | 20 securities fraud counts (Feb 2004) vs 14 (July 2004 superseding indictment, per CA5) | B-021, B-025 | Always give the date with any count total. Trial result: 19 convictions, 9 acquittals (CA5, SCOTUS agree). |
| 11 | Lay's stock/loan figures | $77.5M advances Jan-Nov 2001 (SEC); "over $77 million" Oct 2000-Oct 2001 (PSI); "over $94 million" May 1999-Oct 2001 (Batson); $26.0M from 918,104 shares Aug-Oct 2001 (DOJ) | B-005, B-014, B-016 | Different periods, not a contradiction. Always give the period and the source. |
| 12 | Director service dates | Jaedicke, John H. Duncan, Blake: PSI and Batson differ. Batson n. 130 says pre-1985 dates are HNG or InterNorth boards. | B-073, B-076, B-077 | Use PSI dates for service on the Enron board, or say "director since the mid-1980s". Note that Batson counts predecessor boards. |
| 13 | Kopper's Chewco loan to Southampton | $750,000 (Kopper complaint) vs $680,000 (Fastow complaint) | B-040 | Both are SEC allegations. Omit the figure, or give both. |
| 14 | Merrill complaint date | Header "February 12, 2003" vs signature, footer and Spotlight: March 17, 2003 | B-083 | Use March 17, 2003. |
| 15 | Powers committee start | Formed Oct 28 (Powers); "began its review on Oct 26" (10-Q); announced Oct 31 (10-Q, Batson). Report dated Feb 1, 2002; delivered Feb 2 (JCT). | A-066 | "Formed in late October 2001; its report is dated February 1, 2002." |
| 16 | InterNorth-HNG acquisition date | July 1, 1985 (JCT, image-checked), with "effective June 1, 1985" for financial reporting; "May 1985" (Batson App. D, citing a newspaper) | A-001, A-002, B-002 | Use **July 1, 1985** (JCT). B-002 note added. |
| 17 | Enron headcount | ~20,600 at end-2000 (10-K); "more than 20,000" (PSI); ~25,000 at bankruptcy (JCT, citing McMahon affidavit) | A-012, A-016 | Give the date with any figure. |
| 18 | Cash raised through SPEs, of the $25.1B "additional debt" | "Approximately $13 billion" (Batson First Interim) vs "$14 billion" (Final) | A-087 | "About $13-14 billion." |
| 19 | Backbone (dark fiber) profit | $67M (Note 16 and 8-K) vs $54M gain (Powers) | fn-28 | Present both, as the annotation already does. |
| 20 | Raptor derivatives' notional amount | $2.1B (10-K, 2000), >$1.5B by Nov 2000 (Powers), ~$1.9B (8-K) | fn-16 | Different dates and groupings; the annotation already says so. |
| 21 | "Most Innovative Company" streak | "fifth consecutive year" as of Feb 2001 (Batson) vs six years (JCT) | A-014 | Both can be true. Say "several years running". |
| 22 | 401(k) lockdown dates | Oct 20-Nov 19 (Fleetham's notice); "October 16 lockdown" (Rep. Bentsen); late Sept for PGE (Lacey) | C-065, C-066, C-067 | State that accounts differ; quote the notice dates as Fleetham's. |
| 23 | Analysts rating Enron "buy" | 15 of 15 (staff report); 15 of 16 early Oct (Sen. Thompson) | C-057, C-058 | Use the staff report; mention the variation. |
| 24 | Seventh-largest | See Tip 2 ruling | A-011 to A-016 | See Tip 2. |
| 25 | Kaminski's first name | "Vincent" (Powers) vs "Wincenty" (Batson) | A-049, A-069 | "Vince Kaminski" in text; no footnote needed. |
| 26 | Lay "founder" (SCOTUS) vs joined predecessor 1984 / HNG CEO 1984 (Batson, JCT) | B-002, B-018 | Avoid "founder". Say "led Enron from its formation in 1986". |

Every card that mentions one of these disagreements states it accurately. The exceptions are A-041 (approval date shown as undisputed) and B-002 (no warning about the acquisition date), both now fixed, plus fn-11 (above).

## Notes for writers

- The Batson conclusions are civil ("sufficient evidence from which a fact-finder could conclude"). Never shorten them to "Batson found X breached". Cards A-071, A-097, B-012, B-013, B-053, B-080, C-027, C-028 and C-031 now all carry the hedge.
- Conclusions summarizing the Batson Second and Third Interim Reports (not in the library) may be cited to the Final Report or its appendices that state them (A-067, A-071, B-053, C-032). Say "the examiner had concluded in an earlier report".
- Greenwood's summaries of Duncan's staff interview (C-002 to C-006) are second-hand. Duncan took the Fifth. Attribute them to the chairman.
- Senators' quotations of Watkins's memo (B-055 note) are not the memo itself. Where possible, use the PSI report's quotations of her Aug 15, 2001 letter, which the Footnote page already cites.

## Every card and annotation checked

Verdicts are also written into each item as `"checked"` and `"checker_note"`.

### Reader A (`work/facts/reader-a.json`)

| id | verdict | note |
|---|---|---|
| A-001 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-002 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-003 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-004 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-005 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-006 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-007 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-008 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-009 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-010 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-011 | OK | Verbatim; claim and verb OK. Image-checked. Image-checked JCT p. 58 (PDF 86). See seventh-largest ruling in factcheck-round1.md. |
| A-012 | OK | Verbatim; claim and verb OK. |
| A-013 | OK | Verbatim; claim and verb OK. Verbatim at para. 9. SEC allegation with hedge 'reportedly'. Do not use this complaint for the bankruptcy date (it alone says Dec 3). See seventh-largest ruling. |
| A-014 | OK | Verbatim; claim and verb OK. Image-checked. Image-checked Batson Final p. 15 n. 27 (PDF 18): 'seventh largest corporation in the world, based upon revenues', citing Fortune's 'The 500 Largest U.S. Corporations'. See ruling. |
| A-015 | OK | Verbatim; claim and verb OK. Image-checked. Image-checked Batson First Interim p. 1 n. 1 (PDF 3). Same wording as Final n. 27. |
| A-016 | OK | Verbatim; claim and verb OK. Verbatim. Note also JCT n. 53 says Enron moved up to FIFTH on the Fortune 500 for 2002, so do not write 'at its peak ... seventh'. See ruling. |
| A-017 | OK | Verbatim; claim and verb OK. |
| A-018 | OK | Verbatim; claim and verb OK. |
| A-019 | OK | Verbatim; claim and verb OK. |
| A-020 | OK | Verbatim; claim and verb OK. |
| A-021 | OK | Verbatim; claim and verb OK. |
| A-022 | OK | Verbatim; claim and verb OK. |
| A-023 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-024 | OK | Verbatim; claim and verb OK. |
| A-025 | OK | Verbatim; claim and verb OK. |
| A-026 | OK | Verbatim; claim and verb OK. |
| A-027 | OK | Verbatim; claim and verb OK. |
| A-028 | OK | Verbatim; claim and verb OK. |
| A-029 | OK | Verbatim; claim and verb OK. |
| A-030 | OK | Verbatim; claim and verb OK. |
| A-031 | OK | Verbatim; claim and verb OK. |
| A-032 | OK | Verbatim; claim and verb OK. |
| A-033 | OK | Verbatim; claim and verb OK. |
| A-034 | OK | Verbatim; claim and verb OK. |
| A-035 | OK | Verbatim; claim and verb OK. |
| A-036 | OK | Verbatim; claim and verb OK. |
| A-037 | OK | Verbatim; claim and verb OK. |
| A-038 | OK | Verbatim; claim and verb OK. Verbatim; a footnote interrupts the sentence in the text file (p. 65). |
| A-039 | OK | Verbatim; claim and verb OK. |
| A-040 | OK | Verbatim; claim and verb OK. |
| A-041 | FIXED | Note corrected: the approval date IS disputed between sources. Powers (p. 71, lines ~2707-2737) says the Finance Committee met Oct 11, 1999 and Winokur presented its recommendation to the full Board 'later that day'. The Senate PSI report (p. 26, PDF 30, lines 1744-1749) says the Board approved 'the following day', October 12, 1999. Say 'in October 1999' or give both dates with attribution. |
| A-042 | OK | Verbatim; claim and verb OK. |
| A-043 | OK | Verbatim; claim and verb OK. Verbatim across a page break. |
| A-044 | OK | Verbatim; claim and verb OK. |
| A-045 | OK | Verbatim; claim and verb OK. |
| A-046 | OK | Verbatim; claim and verb OK. |
| A-047 | OK | Verbatim; claim and verb OK. |
| A-048 | FIXED | Addendum ruling: Powers (p. 83) quotes 'Andersen's CEO' without naming him and without saying he was under oath. The library has no transcript of the Dec 12, 2001 hearing. hrg-hfs-enron-investors (Feb 5, 2002) lists Joseph Berardino as Andersen's CEO and has him refer to an earlier appearance, but that does not confirm he was the Dec 12 speaker. Do NOT name him for this quote. Removed Berardino from 'people'; changed the claim to 'told Congress' and the source type to the Powers Report quoting testimony. Gap logged (Dec 12, 2001 House Financial Services Capital Markets subcommittee transcript). |
| A-049 | OK | Verbatim; claim and verb OK. |
| A-050 | OK | Verbatim; claim and verb OK. |
| A-051 | OK | Verbatim; claim and verb OK. |
| A-052 | OK | Verbatim; claim and verb OK. |
| A-053 | OK | Verbatim; claim and verb OK. |
| A-054 | OK | Verbatim; claim and verb OK. |
| A-055 | OK | Verbatim; claim and verb OK. |
| A-056 | OK | Verbatim; claim and verb OK. |
| A-057 | OK | Verbatim; claim and verb OK. |
| A-058 | OK | Verbatim; claim and verb OK. Verified: 10-Q line 3673 '$710 million ($462 million after tax)'; Powers line 4653 '$544 million after taxes'. Disagreement stated accurately. |
| A-059 | OK | Verbatim; claim and verb OK. Verified Powers lines 3647-3651 and n. 60 (lines 4600-4612): $1B + ~$200M. 10-Q $270M figure noted. |
| A-060 | OK | Verbatim; claim and verb OK. |
| A-061 | OK | Verbatim; claim and verb OK. |
| A-062 | OK | Verbatim; claim and verb OK. |
| A-063 | OK | Verbatim; claim and verb OK. |
| A-064 | OK | Verbatim; claim and verb OK. |
| A-065 | OK | Verbatim; claim and verb OK. Verbatim across a page break. |
| A-066 | OK | Verbatim; claim and verb OK. |
| A-067 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-068 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-069 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-070 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-071 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-072 | OK | Verbatim; claim and verb OK. |
| A-073 | OK | Verbatim; claim and verb OK. |
| A-074 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-075 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-076 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-077 | OK | Verbatim; claim and verb OK. |
| A-078 | OK | Verbatim; claim and verb OK. |
| A-079 | OK | Verbatim; claim and verb OK. |
| A-080 | OK | Verbatim; claim and verb OK. |
| A-081 | OK | Verbatim; claim and verb OK. |
| A-082 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-083 | OK | Verbatim; claim and verb OK. |
| A-084 | OK | Verbatim; claim and verb OK. |
| A-085 | OK | Verbatim; claim and verb OK. Verified 10-Q restatement table (lines ~990-1062): restated NI 26/564/635/842; equity 5,309/6,600/8,724/10,289. |
| A-086 | OK | Verbatim; claim and verb OK. |
| A-087 | OK | Verbatim; claim and verb OK. Image-checked. Image-checked Batson Final pp. 16-17 (PDF 19-20). |
| A-088 | OK | Verbatim; claim and verb OK. |
| A-089 | OK | Verbatim; claim and verb OK. |
| A-090 | OK | Verbatim; claim and verb OK. |
| A-091 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-092 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-093 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-094 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-095 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-096 | OK | Verbatim; claim and verb OK. Image-checked. |
| A-097 | FIXED | Claim was incomplete in a way that could mislead readers about the outside directors. Batson Final pp. 10-11 (PDF 13-14, image-checked) also concludes there is sufficient evidence for a fact-finder to conclude that CERTAIN outside directors breached their duty of good faith in approving the Rhythms and certain Raptor hedges. Added that. Civil standard only. |

### Reader B (`work/facts/reader-b.json`)

| id | verdict | note |
|---|---|---|
| B-001 | OK | Verbatim; claim and verb OK. |
| B-002 | FIXED | Added a source disagreement to notes: Batson App. D (p. 11, citing a newspaper article) dates the InterNorth-HNG acquisition to May 1985; the JCT report (p. 59, PDF 87, image-checked) gives July 1, 1985 (effective June 1, 1985 for financial reporting). Use the JCT date. |
| B-003 | OK | Verbatim; claim and verb OK. |
| B-004 | OK | Verbatim; claim and verb OK. |
| B-005 | OK | Verbatim; claim and verb OK. |
| B-006 | OK | Verbatim; claim and verb OK. |
| B-007 | OK | Verbatim; claim and verb OK. |
| B-008 | OK | Verbatim; claim and verb OK. |
| B-009 | OK | Verbatim; claim and verb OK. |
| B-010 | OK | Verbatim; claim and verb OK. |
| B-011 | OK | Verbatim; claim and verb OK. |
| B-012 | OK | Verbatim; claim and verb OK. Image-checked. |
| B-013 | FIXED | Claim tightened: the examiner's conclusion covers only the outside directors who were on the Board at the time of each approval (June 1999 for Rhythms; May-August 2000 for the three Raptors), not all outside directors. The Final Report summary (p. 11) says 'certain of the Outside Directors'. Verified against page image PDF 9. |
| B-014 | OK | Verbatim; claim and verb OK. Image-checked. |
| B-015 | OK | Verbatim; claim and verb OK. Image-checked. |
| B-016 | OK | Verbatim; claim and verb OK. |
| B-017 | OK | Verbatim; claim and verb OK. Image-checked. |
| B-018 | OK | Verbatim; claim and verb OK. |
| B-019 | OK | Verbatim; claim and verb OK. |
| B-020 | OK | Verbatim; claim and verb OK. |
| B-021 | OK | Verbatim; claim and verb OK. |
| B-022 | OK | Verbatim; claim and verb OK. Image-checked. Image-checked PDF 51-52. Reminder for writers: at trial Skilling was convicted on one insider-trading count and acquitted on nine (B-025). |
| B-023 | OK | Verbatim; claim and verb OK. |
| B-024 | OK | Verbatim; claim and verb OK. Image-checked. |
| B-025 | OK | Verbatim; claim and verb OK. |
| B-026 | OK | Verbatim; claim and verb OK. |
| B-027 | OK | Verbatim; claim and verb OK. |
| B-028 | OK | Verbatim; claim and verb OK. |
| B-029 | OK | Verbatim; claim and verb OK. |
| B-030 | OK | Verbatim; claim and verb OK. |
| B-031 | OK | Verbatim; claim and verb OK. |
| B-032 | OK | Verbatim; claim and verb OK. |
| B-033 | OK | Verbatim; claim and verb OK. |
| B-034 | OK | Verbatim; claim and verb OK. |
| B-035 | OK | Verbatim; claim and verb OK. |
| B-036 | OK | Verbatim; claim and verb OK. Image-checked. |
| B-037 | OK | Verbatim; claim and verb OK. |
| B-038 | OK | Verbatim; claim and verb OK. |
| B-039 | OK | Verbatim; claim and verb OK. |
| B-040 | OK | Verbatim; claim and verb OK. |
| B-041 | OK | Verbatim; claim and verb OK. |
| B-042 | OK | Verbatim; claim and verb OK. |
| B-043 | OK | Verbatim; claim and verb OK. |
| B-044 | OK | Verbatim; claim and verb OK. |
| B-045 | OK | Verbatim; claim and verb OK. |
| B-046 | OK | Verbatim; claim and verb OK. |
| B-047 | OK | Verbatim; claim and verb OK. |
| B-048 | OK | Verbatim; claim and verb OK. |
| B-049 | OK | Verbatim; claim and verb OK. |
| B-050 | OK | Verbatim; claim and verb OK. |
| B-051 | OK | Verbatim; claim and verb OK. |
| B-052 | OK | Verbatim; claim and verb OK. |
| B-053 | OK | Verbatim; claim and verb OK. Image-checked. |
| B-054 | FIXED | Quote contained typesetting line-break hyphens copied from the transcript (e.g. 'account- ant'). Replaced with the words as printed, so the quote can be used as is. Wording otherwise verbatim. |
| B-055 | OK | Verbatim; claim and verb OK. |
| B-056 | OK | Verbatim; claim and verb OK. |
| B-057 | OK | Verbatim; claim and verb OK. |
| B-058 | OK | Verbatim; claim and verb OK. Absence-of-evidence card; no quote needed. Writers must use the exact wording 'The library documents show no charges against her.' |
| B-059 | OK | Verbatim; claim and verb OK. Image-checked. |
| B-060 | OK | Verbatim; claim and verb OK. Image-checked. |
| B-061 | OK | Verbatim; claim and verb OK. |
| B-062 | FIXED | Quote contained typesetting line-break hyphens copied from the transcript (e.g. 'account- ant'). Replaced with the words as printed, so the quote can be used as is. Wording otherwise verbatim. |
| B-063 | OK | Verbatim; claim and verb OK. |
| B-064 | OK | Verbatim; claim and verb OK. |
| B-065 | FIXED | Removed '(the first was in mid-December 2001)': the library contains no transcript of Berardino's earlier appearance. The Feb 2002 transcript shows only that he said 'When I last appeared before this committee' and that members referred to a Dec 12, 2001 subcommittee hearing; it does not say Berardino testified on that date. |
| B-066 | FIXED | Quote contained typesetting line-break hyphens copied from the transcript (e.g. 'account- ant'). Replaced with the words as printed, so the quote can be used as is. Wording otherwise verbatim. |
| B-067 | OK | Verbatim; claim and verb OK. |
| B-068 | FIXED | Quote contained typesetting line-break hyphens copied from the transcript (e.g. 'account- ant'). Replaced with the words as printed, so the quote can be used as is. Wording otherwise verbatim. |
| B-069 | OK | Verbatim; claim and verb OK. Image-checked. |
| B-070 | OK | Verbatim; claim and verb OK. Image-checked. |
| B-071 | OK | Verbatim; claim and verb OK. |
| B-072 | OK | Verbatim; claim and verb OK. |
| B-073 | FIXED | Quote contained typesetting line-break hyphens copied from the transcript (e.g. 'account- ant'). Replaced with the words as printed, so the quote can be used as is. Wording otherwise verbatim. (B-073 and B-074: printed page offset in rpt-psi-board is PDF = printed + 4.) |
| B-074 | FIXED | Quote contained typesetting line-break hyphens copied from the transcript (e.g. 'account- ant'). Replaced with the words as printed, so the quote can be used as is. Wording otherwise verbatim. (B-073 and B-074: printed page offset in rpt-psi-board is PDF = printed + 4.) |
| B-075 | FIXED | Locator corrected: lines 1345-1346 and 1420 are on PDF p. 24 (printed p. 14), not PDF 25 / p. 15. Claim softened: Duncan said the Powers Report and press reports 'indicate' that certain members of management and the outside auditors knew of the problems; he did not assert it from his own knowledge. |
| B-076 | OK | Verbatim; claim and verb OK. |
| B-077 | OK | Verbatim; claim and verb OK. |
| B-078 | FIXED | Quote contained typesetting line-break hyphens copied from the transcript (e.g. 'account- ant'). Replaced with the words as printed, so the quote can be used as is. Wording otherwise verbatim. |
| B-079 | FIXED | The Senate staff report's quotation differs slightly from the hearing transcript. Transcript (hrg-psi-board, PDF p. 100, printed p. 90, line 6041): 'We had never had any responsibility to monitor this.' If quoting LeMaistre, quote the transcript and cite hrg-psi-board PDF 100. Blake's words are also in the transcript at the same place. |
| B-080 | OK | Verbatim; claim and verb OK. Image-checked. |
| B-081 | OK | Verbatim; claim and verb OK. Image-checked. |
| B-082 | OK | Verbatim; claim and verb OK. Absence-of-evidence card; no quote needed. Spotlight index reviewed: no outside director listed. Do not write 'never charged'. |
| B-083 | OK | Verbatim; claim and verb OK. |
| B-084 | OK | Verbatim; claim and verb OK. |
| B-085 | OK | Verbatim; claim and verb OK. |
| B-086 | OK | Verbatim; claim and verb OK. |

### Reader C (`work/facts/reader-c.json`)

| id | verdict | note |
|---|---|---|
| C-001 | OK | Verbatim; claim and verb OK. Image-checked PDF 49 (printed p. 45). E-mail header shows 10/12/2001 08:53 AM (time faint). |
| C-002 | OK | Verbatim; claim and verb OK. |
| C-003 | OK | Verbatim; claim and verb OK. |
| C-004 | OK | Verbatim; claim and verb OK. |
| C-005 | OK | Verbatim; claim and verb OK. |
| C-006 | OK | Verbatim; claim and verb OK. |
| C-007 | OK | Verbatim; claim and verb OK. |
| C-008 | OK | Verbatim; claim and verb OK. |
| C-009 | OK | Verbatim; claim and verb OK. |
| C-010 | OK | Verbatim; claim and verb OK. |
| C-011 | OK | Verbatim; claim and verb OK. |
| C-012 | OK | Verbatim; claim and verb OK. |
| C-013 | OK | Verbatim; claim and verb OK. Verbatim at PDF 39 (prepared statement); same words also appear in the oral statement at PDF 36. |
| C-014 | OK | Verbatim; claim and verb OK. |
| C-015 | OK | Verbatim; claim and verb OK. |
| C-016 | OK | Verbatim; claim and verb OK. |
| C-017 | OK | Verbatim; claim and verb OK. |
| C-018 | OK | Verbatim; claim and verb OK. |
| C-019 | OK | Verbatim; claim and verb OK. |
| C-020 | OK | Verbatim; claim and verb OK. |
| C-021 | OK | Verbatim; claim and verb OK. Image-checked. Image-checked PDF 11-12 (table and n. 14-15). Note: the Batson Final Report main text (p. 39, PDF 42, image-checked) itself uses $47.9 million for 2000 fees, so the examiner uses both figures. |
| C-022 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-023 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-024 | OK | Verbatim; claim and verb OK. |
| C-025 | OK | Verbatim; claim and verb OK. |
| C-026 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-027 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-028 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-029 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-030 | FIXED | Added clarification: the $1 billion equity overstatement here is the same error the Powers Report describes ($172M in Q2 2000 + $828M in Q1 2001), which made up $1 billion of the $1.2 billion reduction in shareholders' equity Enron disclosed on Oct 16, 2001 (Powers pp. 98, 125-126 and n. 60). The examiner's n. 206 says it is unrelated to the '$1 billion earnings restatement' of Oct 16 (the $1.01 billion after-tax charges). Do not merge the two $1 billion figures. Verified against page image PDF 65. |
| C-031 | FIXED | Claim reworded to match the examiner's standard: App. B p. 3-4 says the evidence 'is sufficient to permit a fact-finder to conclude' that Andersen failed this duty; it is not a finding that Andersen did fail. Verified against page image PDF 5-6. |
| C-032 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-033 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-034 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-035 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-036 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-037 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-038 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-039 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-040 | OK | Verbatim; claim and verb OK. Image-checked. |
| C-041 | FIXED | Removed an unsupported statement from notes ('Headcount is U.S. per the article'): the examiner does not say the 28,000 figure is U.S.-only, and the Chicago Tribune article is not in the library. Also removed a duplicated sentence. Verified against page image PDF 63. |
| C-042 | OK | Verbatim; claim and verb OK. |
| C-043 | OK | Verbatim; claim and verb OK. |
| C-044 | OK | Verbatim; claim and verb OK. |
| C-045 | OK | Verbatim; claim and verb OK. |
| C-046 | OK | Verbatim; claim and verb OK. Verbatim; quote spans PDF 7-8. |
| C-047 | OK | Verbatim; claim and verb OK. |
| C-048 | OK | Verbatim; claim and verb OK. |
| C-049 | OK | Verbatim; claim and verb OK. Verbatim at PDF 107 (two-column layout in text copy). |
| C-050 | OK | Verbatim; claim and verb OK. Verbatim; spans PDF 24-25. |
| C-051 | OK | Verbatim; claim and verb OK. Verbatim in Highlights (two-column layout in text copy). |
| C-052 | OK | Verbatim; claim and verb OK. Verbatim in Highlights (two-column layout in text copy). |
| C-053 | OK | Verbatim; claim and verb OK. |
| C-054 | OK | Verbatim; claim and verb OK. |
| C-055 | OK | Verbatim; claim and verb OK. |
| C-056 | OK | Verbatim; claim and verb OK. |
| C-057 | OK | Verbatim; claim and verb OK. |
| C-058 | OK | Verbatim; claim and verb OK. |
| C-059 | OK | Verbatim; claim and verb OK. |
| C-060 | OK | Verbatim; claim and verb OK. |
| C-061 | OK | Verbatim; claim and verb OK. |
| C-062 | OK | Verbatim; claim and verb OK. |
| C-063 | OK | Verbatim; claim and verb OK. |
| C-064 | OK | Verbatim; claim and verb OK. |
| C-065 | OK | Verbatim; claim and verb OK. |
| C-066 | OK | Verbatim; claim and verb OK. |
| C-067 | OK | Verbatim; claim and verb OK. |
| C-068 | OK | Verbatim; claim and verb OK. |
| C-069 | OK | Verbatim; claim and verb OK. |
| C-070 | OK | Verbatim; claim and verb OK. |
| C-071 | OK | Verbatim; claim and verb OK. Verbatim (two-column layout in text copy). |
| C-072 | OK | Verbatim; claim and verb OK. |
| C-073 | OK | Verbatim; claim and verb OK. |
| C-074 | OK | Verbatim; claim and verb OK. |
| C-075 | OK | Verbatim; claim and verb OK. |
| C-076 | OK | Verbatim; claim and verb OK. |
| C-077 | OK | Verbatim; claim and verb OK. |
| C-078 | OK | Verbatim; claim and verb OK. |
| C-079 | OK | Verbatim; claim and verb OK. |
| C-080 | OK | Verbatim; claim and verb OK. |
| C-081 | OK | Verbatim; claim and verb OK. |

### Footnote annotations (`work/drafts/footnote.json`)

| id | verdict | note |
|---|---|---|
| intro | OK | Both Powers quotes verified verbatim. |
| ctx-01 | FIXED | FIXED. 'left_out' stated as fact that the contributions were made through Osprey certificates. The Powers table (p. 146) lists LJM purchases of Osprey equity described as equity in a limited partner / an affiliate of Whitewing, and the amounts match ($15M; $26M + $6.5M = $32.5M), but no source states the link. Hedged the wording. |
| ctx-02 | OK | All cites verbatim; text supported; verbs OK. |
| fn-01 | OK | All cites verbatim; text supported; verbs OK. Batson citation image-checked (Final Report PDF 6). |
| fn-02 | OK | All cites verbatim; text supported; verbs OK. |
| fn-03 | OK | All cites verbatim; text supported; verbs OK. PSI p. 33 also says 'Nor had any other Board member taken any steps to obtain this information', which supports 'no board member'. |
| fn-04 | OK | All cites verbatim; text supported; verbs OK. |
| fn-05 | FIXED | FIXED. The old text said the 1999 wording was 'reasonable and no less favorable' and implied a single change to the 2000 wording. Powers (p. 196, lines 6979-6993) shows that wording was in the Q2 and Q3 1999 10-Qs; the 1999 10-K actually dropped 'reasonable'; Q1 2000 restored it in another form; the 2000 10-K used 'reasonable compared to'. Rewrote to 'mid-1999 quarterly reports' and 'changed several times', and added the citation (verbatim). |
| fn-06 | OK | All cites verbatim; text supported; verbs OK. Batson citations image-checked (Final Report PDF 13 n. 17; PDF 22 n. 41). |
| fn-07 | OK | All cites verbatim; text supported; verbs OK. |
| fn-08 | OK | All cites verbatim; text supported; verbs OK. |
| fn-09 | OK | All cites verbatim; text supported; verbs OK. |
| fn-10 | OK | All cites verbatim; text supported; verbs OK. |
| fn-11 | FIXED | FIXED. The old text said the $172 million correction was 'separate from the $1.2 billion cut to shareholders' equity that Enron announced in October 2001.' The Powers Report says the opposite: the $172M (Raptor I) + $828M (Raptors II and IV) correction made up $1 billion of that $1.2 billion reduction (p. 98, lines 3647-3651; pp. 125-126 and n. 60, lines 4569-4612). Rewrote the last sentences and added the n. 60 citation (verbatim). |
| fn-12 | OK | All cites verbatim; text supported; verbs OK. |
| fn-13 | OK | All cites verbatim; text supported; verbs OK. |
| fn-14 | OK | All cites verbatim; text supported; verbs OK. |
| fn-15 | OK | All cites verbatim; text supported; verbs OK. |
| fn-16 | OK | All cites verbatim; text supported; verbs OK. |
| fn-17 | OK | All cites verbatim; text supported; verbs OK. Batson citation image-checked (Final Report PDF 42). The same page gives Andersen's 2000 fees as $47.9 million. |
| fn-18 | OK | All cites verbatim; text supported; verbs OK. Note for writers: the $544 million after-tax figure is Enron's Oct 16, 2001 announcement (Powers p. 98). Enron's Q3 10-Q later put the Raptor charge at $462 million after tax (10-Q line 3673); the $710 million pre-tax figure is not disputed. |
| fn-19 | OK | All cites verbatim; text supported; verbs OK. |
| fn-20 | OK | All cites verbatim; text supported; verbs OK. PSI p. 25 confirms 'the entire meeting lasted 1 hour'. |
| fn-21 | OK | All cites verbatim; text supported; verbs OK. |
| fn-22 | OK | All cites verbatim; text supported; verbs OK. |
| fn-23 | OK | All cites verbatim; text supported; verbs OK. |
| fn-24 | OK | All cites verbatim; text supported; verbs OK. |
| fn-25 | OK | All cites verbatim; text supported; verbs OK. |
| fn-26 | OK | All cites verbatim; text supported; verbs OK. |
| fn-27 | OK | All cites verbatim; text supported; verbs OK. Quote verbatim (text file has a page break inside it). |
| fn-28 | OK | All cites verbatim; text supported; verbs OK. |
| fn-29 | OK | All cites verbatim; text supported; verbs OK. |
| fn-30 | OK | All cites verbatim; text supported; verbs OK. Batson citation image-checked (Final Report PDF 23). |
| fn-31 | OK | All cites verbatim; text supported; verbs OK. |
| fn-32 | OK | All cites verbatim; text supported; verbs OK. |
| fn-33 | OK | All cites verbatim; text supported; verbs OK. |
| closing | OK | PSI quote verified verbatim at PDF 52. |
| Note 16 text | OK | Note 16 text re-checked word for word against sources/03-sec-filings/enron-10k-fy2000.txt lines 5863-5962 (and context lines 5134-5143) by the Fact-Checker: matches after the stated whitespace normalization. |
