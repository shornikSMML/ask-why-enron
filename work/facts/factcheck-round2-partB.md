# Fact-check, Round 2, Part B: Cast, Timeline, Glossary, Enron diagrams, Footnote intro/closing

Agent: Fact-Checker (instance B). Date: 2026-09-26. I did not edit any of the files I reviewed. I checked every claim against the library source itself, not only against the fact card.

## How I checked

- **Fingerprints.** I computed SHA-256 for all 74 library files present on disk and compared each with `sources/download_log.csv`. All 74 match. The two missing files are the known gaps (Batson Second and Third Interim Reports).
- **Cast (`js/cast-data.js`, 22 entries).** I checked every sentence about a named person against the source at the card's locator. That covers roles, dates, dollar amounts, verbs and each legal outcome.
- **Timeline (`js/timeline-data.js`, 60 entries).** I checked every date, dollar amount and named person against the source.
- **Glossary (`js/glossary-data.js`, 124 entries).** I read every entry for errors of general knowledge. I checked the 30 entries that carry Enron-specific or statutory facts against the sources.
- **Diagrams.** I extracted the text of all six SVGs (wide and `-narrow`) and checked every figure and date against the Powers Report, the 10-Q, the 8-K and the 10-K. A script confirmed that the wide and narrow versions carry the same figures (only layout differs).
- **Footnote (`work/drafts/footnote.json`).** I checked the intro, the closing and its "Ask Why" question. I also re-checked Round-1 fixes: all 3 fixed annotations (ctx-01, fn-05, fn-11) plus 3 fixed cards (A-041, B-013, B-065). That is 6 of 21 Round-1 fixes, about 29%.
- **Citations.** All 277 cites in the Cast, Timeline and Glossary point to a card marked OK or FIXED. Each cite's `source_id` and page match its card. Every `source_id` in the four files is a manifest id. No file cites anything in `sources/candidates/`.
- **Reader tips.** Buffett appears nowhere. "Seventh" appears only in Timeline 2001-04, using the ruled wording ("In 2001, Fortune magazine ranked Enron seventh on its list of the 500 largest U.S. companies, measured by revenue."). There is no "at its peak", no "founder" and no "never charged".

## Findings

| # | file | location | problem | what the source says (locator) | required fix | severity |
|---|---|---|---|---|---|---|
| 1 | js/cast-data.js | `jeffrey-mcmahon`, role | Says McMahon was "Enron treasurer at the time of the March 2001 Chewco buyout." That is wrong. By then he had left the Treasurer's job and the Finance group. Glisan succeeded him as Treasurer in May 2000. | Powers p. 61 (SEC text lines ~2388-2391): "By mid-2000 ... By this point, McMahon had left the Treasurer's position and the Finance group." p. 97 (line 3551): "In May 2000, Glisan succeeded McMahon as Treasurer of Enron." The buyout talks began "During the first quarter of 2000" (p. 60, lines 2325-2330). The buyout closed March 26, 2001 (p. 61). | Reword, e.g.: "Enron's treasurer until 2000, including during early talks in 2000 about buying out Chewco; named CFO when Fastow went on leave in October 2001; president and COO when he testified in February 2002." | **must-fix** |
| 2 | js/cast-data.js (and card B-051) | `mark-koenig`, outcome_text | Says Koenig pleaded guilty "in part for a statement he made on an April 2001 call with analysts." The Fifth Circuit's footnote 3 is attached to his statement on the **January 22, 2001** earnings call. Card B-051 has the same error, which Round 1 missed. | ca5-skilling-2009 PDF pp. 5-6 (lines 184-204 and n. 3): "on January 22, 2001, Enron released its earnings report ... He also listened silently as Mark Koenig ... assured investors that non-core business revenues were a 'fairly small' amount of EBS's earnings" [n. 3: "Koenig pleaded guilty to securities fraud for this statement, among others."] | Change to "a statement he made on a January 2001 call with investors (January 22, 2001)". Correct card B-051 too. | **must-fix** |
| 3 | js/cast-data.js | `jeffrey-mcmahon`, summary | "The board's special committee reported that McMahon ... proposed a $1 million return ... and that Fastow instead negotiated about $10 million." The committee is reporting what McMahon told it, and the talks were in 2000, not at the 2001 buyout. | Powers p. 60 (lines 2348-2356): "McMahon told us that ... he proposed to Fastow that the buyout be structured to provide a $1 million return ... McMahon said that Fastow ... later reported back to McMahon that he had negotiated a payment of $10 million." | "McMahon told the board's special committee that in 2000, as treasurer, he proposed a $1 million return for the Chewco investors, and that Fastow later told him he had negotiated $10 million." | should-fix |
| 4 | js/cast-data.js | `kenneth-lay`, summary | "found that Lay, as CEO, bore ultimate responsibility" drops what the responsibility was for. As written it reads as ultimate responsibility for everything. | Powers p. 19 (lines 906-912): "As CEO, he had the ultimate responsibility for taking reasonable steps to ensure that the officers reporting to him performed their oversight duties properly ... Ultimately, a large measure of the responsibility rests with the CEO." | "found that, as CEO, Lay had ultimate responsibility for making sure the officers reporting to him did their oversight jobs, and that 'a large measure of the responsibility rests with the CEO.'" | should-fix |
| 5 | js/cast-data.js | `kenneth-lay`, outcome_status | The label "conviction vacated (died before appeal)" asserts something the entry's own text says the library does not show ("The library does not say whether he had filed an appeal"). | ca5-skilling-2009 PDF 15 n. 9: "On July 5, 2006, Lay died, causing the court to vacate his conviction and dismiss his indictment." Nothing about an appeal. | Label: "conviction vacated after his death". | should-fix |
| 6 | js/cast-data.js | `kenneth-lay`, outcome_text | "In May 2006 a jury convicted him on every count against him" comes right after the list of July 2004 charges, which include bank fraud and false statements. Together they imply the jury convicted him of all the charged counts. The Fifth Circuit's sentence speaks only of the counts at that trial, and it notes counts were dropped before and during trial. | ca5-skilling-2009 PDF 15 (lines 527-550): "the government eliminated four additional counts ... The jury convicted Lay of every count against him." | "In May 2006, according to the Fifth Circuit, the jury convicted him of every count against him at that trial." | should-fix |
| 7 | js/cast-data.js (and card B-065) | `joseph-berardino`, summary | Says he testified "to the House Financial Services Committee." The February 5, 2002 hearing was held by its Capital Markets subcommittee. | hrg-hfs-enron-investors PDF 115: "SUBCOMMITTEE ON CAPITAL MARKETS, INSURANCE, AND GOVERNMENT SPONSORED ENTERPRISES, COMMITTEE ON FINANCIAL SERVICES ... Chairman BAKER. I would like to call this hearing of the Capital Markets Subcommittee to order." Oath: PDF 125 "[Witness sworn.]" | "testified under oath to a House Financial Services subcommittee (Capital Markets) on February 5, 2002". | should-fix |
| 8 | js/cast-data.js | `david-delainey`, outcome_text | "The SEC charged Delainey on October 30, 2003" has no cite in the entry. The SEC list does not name him. It describes the defendant by title, and the name comes from matching that title to the DOJ release. | sec-enron-spotlight line 91: "SEC Charges Former Chief Executive Officer of Enron North America and Enron Energy Services with Violating Federal Securities Laws (Litigation Release No. 18435, Oct. 30, 2003)". DOJ #099 names Delainey as "former Enron North America and EES Chief Executive Officer". | Add a `sec-enron-spotlight` cite. Word it as: "The SEC's list of Enron cases records an October 30, 2003 case against the former CEO of Enron North America and Enron Energy Services, the post Delainey held." | should-fix |
| 9 | js/cast-data.js | `mark-koenig`, outcome_text and role | The SEC charge date (August 25, 2004) and his title come from the SEC list, but the entry cites only CA5 (B-051). | sec-enron-spotlight line 63: "SEC Charges Mark E. Koenig, Former Executive Vice-President and Director of Investor Relations at Enron (Litigation Release No. 18849, August 25, 2004)". | Add a `sec-enron-spotlight` cite (Lit. Rel. 18849). | should-fix |
| 10 | js/cast-data.js | `arthur-andersen` role vs `kenneth-lay` role | The Cast contradicts itself. Andersen audited "from Enron's formation in 1985", while Lay was chairman "from its formation in 1986". Each is sourced (Batson vs SEC), but side by side they confuse readers. | batson-final-app-b-part1 PDF 3 n. 1 (Enron formed 1985 from HNG and InterNorth); sec-lay-complaint p. 3 ("from its formation in 1986"); JCT p. 59: renamed Enron Corp. April 1986. | Andersen: "Enron's outside auditor from the 1985 merger that created Enron (it had audited InterNorth)". Lay can keep the SEC wording. | should-fix |
| 11 | js/cast-data.js | `merrill-lynch-executives`, outcome_text | "no library document names any of them in a criminal case" is literally true but incomplete. The library says four Merrill Lynch employees were tried criminally over the barge deal, convicted, and had their convictions reversed. It does not name them. | ca5-skilling-2009 PDF 19 and n. 12: "The government tried two Enron employees and four Merrill Lynch employees ... The jury acquitted one Enron employee and convicted the other five defendants; only the Merrill Lynch employees appealed." PDF 20: "we reversed the defendants' convictions" (United States v. Brown, 459 F.3d 509 (5th Cir. 2006)). | Add: "The Fifth Circuit's 2009 opinion says four unnamed Merrill Lynch employees were convicted at trial over the barge deal and that their convictions were reversed on appeal in 2006. It does not name them, so the library does not show whether these four executives were among them." | should-fix |
| 12 | js/cast-data.js | `david-duncan`, outcome_text | Optional addition. The library shows Duncan testified at Andersen's criminal trial in May 2002. | batson-final-app-b-part1 PDF 11 (line ~400) and many later footnotes: "Andersen Criminal Trial Transcript ... (testimony of David Duncan, May 14, 2002)"; rpt-sga-watchdogs PDF 28 n. 104. | You may add: "He testified at Andersen's criminal trial in May 2002 (as cited by the bankruptcy examiner)." Keep "The library contains no documents on any criminal case against him." | note |
| 13 | js/cast-data.js | `michael-kopper`, outcome_text | Correct. The bankruptcy examiner corroborates it: $4M forfeiture + $8M disgorgement = the $12M the examiner reports. | batson-1st-interim PDF 5 n. 8: "Mr. Kopper pled guilty ... Mr. Kopper agreed to surrender $12 million in assets". | Optional second cite (`batson-1st-interim`, PDF 5). | note |
| 14 | js/cast-data.js | `merrill-lynch-executives` | Furst and Tilney also testified under oath before the Senate PSI in 2002 (before the SEC complaint). | hrg-psi-banks-v1 PDF 189 (lines 11712-11723): "Mr. FURST. I do. Mr. TILNEY. I do." | Optional. | note |
| 15 | js/timeline-data.js | 2006-05 "Lay and Skilling are convicted" | "a jury convicted Lay on every count against him" has the same issue as #6. | ca5-skilling-2009 PDF 15. | "convicted Lay of every count against him at that trial". | should-fix |
| 16 | js/timeline-data.js | 2002-05-07 "Directors testify to the Senate" | "All rejected any share of responsibility" is the subcommittee's characterization, stated as fact. | rpt-psi-board PDF 18: "During the hearing, all five Board witnesses explicitly rejected any share of responsibility for Enron's collapse." | "The subcommittee reported that all five rejected any share of responsibility for Enron's collapse." | should-fix |
| 17 | js/timeline-data.js | 2003-03-17 Merrill | "through the 1999 barge deal" leaves out the second deal the SEC alleged, the energy option contracts. | sec-merrill-complaint para. 1. | "through two 1999 year-end deals, including the Nigerian barge 'sale'". | note |
| 18 | js/timeline-data.js | 2001-12-02 | "the largest U.S. bankruptcy until WorldCom's" is the JCT staff's statement, which cites bankruptcydata.com. | rpt-jct-vol1 p. 58 (PDF 86) and n. 55. | Optional: "according to the Joint Committee on Taxation staff". | note |
| 19 | js/timeline-data.js | titles "The hidden debt", "Propping up the Raptors", "Record revenue on paper" | These titles lean slightly toward judgment. The text under each is accurate. | n/a (tone) | Consider "Debt on and off the balance sheet", "A temporary fix for the Raptors", "Record reported revenue". | note |
| 20 | js/glossary-data.js | `pcaob`, long | "five members, only two of whom may be CPAs" is wrong. The Act requires exactly two. | sox-plaw-html Sec. 101(e)(2) (lines 446-451): "Two members, and only 2 members, of the Board shall be or have been certified public accountants". | "five members, exactly two of whom must be (or have been) CPAs". | should-fix |
| 21 | js/glossary-data.js | `vacated`, long | "including when a defendant dies before his appeal is finished," followed directly by Lay, implies Lay had an appeal pending. The library does not say so. | ca5-skilling-2009 PDF 15 n. 9 (no mention of an appeal). | "including when a defendant dies before his case is final". | should-fix |
| 22 | images/diagram-chewco-ljm.svg and -narrow.svg (box text and `<desc>`) | Chewco box | "The board was not told of Kopper's role" states as fact what the committee put as an absence of evidence. | Powers p. 8 (Exec. Summary) and pp. 46-47: "we have seen no evidence that his participation was ever disclosed to, or approved by, either Kenneth Lay ... or the Board of Directors." | "The special committee found no evidence the board was told of Kopper's role." | should-fix |
| 23 | images/diagram-chewco-ljm.svg and -narrow.svg | footer | "would restate 1997–2000": the 8-K also restated the first two quarters of 2001. | enron-8k-nov-2001-ex99-1 p. 1: "restatement of its financial statements for 1997 through 2000 and the first two quarters of 2001". | Optional: "1997 through mid-2001". | note |
| 24 | images/diagram-raptor.svg and -narrow.svg | footnote * | Checked and correct. Sources disagree, though: the Batson First Interim Report says "Raptor SPE II" held NewPower warrants, while Powers says Raptor III (Porcupine). The diagram follows Powers, which gives the detailed account. | batson-1st-interim PDF 5 (line ~150); Powers pp. 114-118 (Raptor III). | None required. | note |
| 25 | work/drafts/footnote.json | intro | "yet almost no reader could tell what was going on" goes beyond the cited Powers wording ("did not ... enable a reader ... to understand what was going on"). "About one page long" has no cite. The Senate staff report supports both. | rpt-psi-board PDF 52 (printed p. 48): "The 1999 and 2000 footnotes, each of which is about one page in length ... The 2000 footnote, in particular, is nearly unintelligible". | Add a cite to `rpt-psi-board` PDF 52 in the intro, or reword to the Powers finding. | should-fix |
| 26 | work/drafts/footnote.json | closing | The closing quotes Powers twice ("to some extent", "understand what was going on") but its `cites` list only `rpt-psi-board`. Every quotation needs a visible citation where it appears. | Powers p. 201 (line ~7163) and p. 197 (line ~7020), both already cited in the intro. | Copy the two Powers cites into `closing.cites`. | should-fix |
| 27 | work/drafts/footnote.json | closing | "Enron described the same dealings again in its filings of November 2001" is inexact. The staff compared Note 16 with a single filing, the Q3 10-Q filed November 19, 2001 (a nine-page description). | rpt-psi-board PDF 52: "the disclosure provided by Enron on November 19, 2001, its 10-Q filing for the third quarter of 2001 ... Enron's 2001 filing provides a nine-page description". | "in its quarterly report filed November 19, 2001". | should-fix |
| 28 | work/drafts/footnote.json | fn-05, "found" (spot re-check of a Round-1 fix) | The Round-1 fix itself is correct (the wording history matches Powers p. 196). But the same field says the committee "found that 'many of them could only have been entered into with related parties.'" That drops the committee's hedge. | Powers p. 199 (lines 7085-7086): "Indeed, based on the terms of the deals, it seems likely that many of them could only have been entered into with related parties." | "It said that 'it seems likely that many of them could only have been entered into with related parties.'" | should-fix |
| 29 | work/drafts/footnote.json | closing | "After the scandal broke" is mild but judging. | n/a (tone) | Optional: "After Enron's problems became public". | note |

**Round-1 fixes re-checked and confirmed correct:**
- **fn-11:** the $1 billion ($172M + $828M) is part of the $1.2 billion. Powers pp. 98, 125-126 and n. 60, lines 3647-3651 and 4565-4612.
- **ctx-01:** the Osprey amounts are hedged correctly. Powers table p. 146 matches 10-K lines 5135-5136.
- **fn-05:** the wording history is correct. Powers p. 196, lines 6975-6990.
- **A-041:** the PSI report says Oct 12 and Powers says "later that day". rpt-psi-board lines 1744-1749; Powers line ~2732.
- **B-013:** "Outside Directors who were members of the Board in June 1999 / May through August 2000". batson-final-app-d PDF 9.
- **B-065:** the removal of the December 2001 date holds. hrg-hfs-enron-investors PDF 124-125.

**Checked with no problem found (Cast outcomes):**
- Skilling: 19 guilty / 9 acquitted; 292 months; CA5 affirmed Jan 6, 2009 and vacated the sentence; SCOTUS June 24, 2010 affirmed in part, vacated in part.
- Fastow and Glisan: DOJ lists of those "convicted to date", in the Feb 19 and Jul 8, 2004 releases.
- Kopper: guilty plea Aug 21, 2002, per the SEC's Fastow complaint para. 9.
- Causey: guilty plea Dec 28, 2005 (SCOTUS p. 372; CA5 p. 15); SEC settlement Feb 9, 2007.
- Andersen: indicted Mar 7, 2002; convicted Jun 15, 2002; SCOTUS unanimously reversed May 31, 2005 (Syllabus: "delivered the opinion for a unanimous Court").
- Duncan: took the Fifth under oath Jan 24, 2002; SEC settled action Jan 28, 2008.
- Watkins, the directors, Powers and Batson: no charges shown; the verbs are right.
- JPM/Citi: $135M and $120M ($101M Enron-related).
- Oaths confirmed: Watkins, Skilling and McMahon (hrg-commerce-skilling-watkins lines 713-722); the five directors (rpt-psi-board p. 2); Lay (B-008).
- Restatement chart: all 12 figures match the 10-Q table, lines ~1004-1014.
- Raptor diagram: all figures match Powers ($30M each; "about $41 million per Raptor, in less than six months each time", p. 128; $39.5M Raptor III; $537M + $50M note; $532M of $650M; Dec 22, 2000; $504M; >$800M; $710M; $35M).

## Counts and verdicts

| File | must-fix | should-fix | note | Verdict |
|---|---|---|---|---|
| `js/cast-data.js` | 2 | 9 | 3 | **PASS AFTER FIXES** |
| `js/timeline-data.js` | 0 | 2 | 3 | **PASS AFTER FIXES** |
| `js/glossary-data.js` | 0 | 2 | 0 | **PASS AFTER FIXES** |
| `images/diagram-chewco-ljm.svg` (+ `-narrow`) | 0 | 1 | 1 | **PASS AFTER FIXES** |
| `images/diagram-raptor.svg` (+ `-narrow`) | 0 | 0 | 1 | **PASS** |
| `images/chart-restatement.svg` (+ `-narrow`) | 0 | 0 | 0 | **PASS** |
| `work/drafts/footnote.json` (intro, closing, spot re-check) | 0 | 4 | 1 | **PASS AFTER FIXES** |
| Fact cards (outside my files, source of #2 and #7) | B-051: 1 | B-065: 1 | | fix with the Cast |

Verdict lines:
- js/cast-data.js: PASS AFTER FIXES
- js/timeline-data.js: PASS AFTER FIXES
- js/glossary-data.js: PASS AFTER FIXES
- images/diagram-chewco-ljm(.svg, -narrow.svg): PASS AFTER FIXES
- images/diagram-raptor(.svg, -narrow.svg): PASS
- images/chart-restatement(.svg, -narrow.svg): PASS
- work/drafts/footnote.json (intro/closing/spot re-check): PASS AFTER FIXES

## Read log (all fingerprints matched `download_log.csv`)

- `powers-report-sec` (SEC .txt), lines:
  - Lay: 900-915
  - Chewco buyout: 2300-2400
  - LJM1: 2625-2650
  - Raptors: 3644-3712
  - Distributions: 4148-4158, 4565-4615, 4672-4692
  - Disclosure: 6975-7090, 7155-7175
  - Osprey table: 5238-5290
  - Timeline: 7505-7520, 7564
  - Plus greps for McMahon and Glisan
- `ca5-skilling-2009`: PDF 1, 5-6, 15-16, 19-20, 104
- `skilling-scotus-2010`: PDF 9, 11, 15 (headers)
- `andersen-scotus`: Syllabus in full
- `doj-lay-charged-press`: lines 15-40, 195-235
- `doj-skilling-charged-press`: lines 150-175
- `sec-enron-spotlight`: lines 30-140
- `sec-fastow-complaint`: para. 9
- `sec-merrill-complaint`: paras. 9-12
- `sec-jpm-citi-press`: settlement amounts
- `hrg-commerce-skilling-watkins`: PDF 14, 16, 23
- `hrg-commerce-lay-powers`: PDF 29, 31
- `hrg-hfs-enron-investors`: PDF 115, 124-126, plus the index
- `hrg-hec-andersen-shredding`: PDF 30-31, 36, 39
- `hrg-psi-board`: PDF 24, 28, 41, 100
- `hrg-psi-banks-v1`: PDF 189 (greps)
- `rpt-psi-board`: PDF 5-7, 18, 21, 51-52
- `rpt-sga-watchdogs`: PDF 28, 36
- `gao-03-864`: PDF 18, 107 (greps)
- `batson-final-app-d`: PDF 6-9 (OCR)
- `batson-1st-interim`: PDF 5 (OCR)
- `batson-final-app-b-part1`: greps for Duncan
- `enron-10q-q3-2001`: restatement table, lines 985-1062
- `enron-10k-2000`: lines 5128-5140
- `enron-8k-nov-2001-ex99-1`: greps
- `sox-plaw-html`: lines 440-452, 1805-1812

**OCR sources.** No quotes were taken from OCR text for new findings. The Batson App. D and First Interim passages I used support notes only, and they match the Round-1 image checks.

## Gaps

No new gaps. The existing gaps still stand: the Koenig plea date and sentence; Fastow's, Glisan's and Delainey's charges and sentences; Duncan's criminal case; and how the SEC's civil cases against Lay, Skilling, McMahon and the Merrill executives ended.
