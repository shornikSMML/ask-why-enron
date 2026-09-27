# Fact-check, Phase 2: lens notes, summaries, Ask Why questions and "Who Knew What, When" strips

Agent: Fact-Checker (instance A). Date: 2026-09-27.
Scope: `work/drafts/lenses.json` (Lens Writer), all seven chapters. I checked 81 notes, 106 summary bullets, 44 strip entries and 28 Ask Why questions, with 334 citations in all. I did not edit the file.

## How I checked

**1. Mechanical checks (script, every item).**
- **Paragraph position.** Each note's `para_index` and `para_start` match the paragraph in the current `work/drafts/chN.html`. I counted by the file's own rule: skip `<p class="dek">` and the Ask Why aside, and strip citation links. All 81 match.
- **Lens tag.** The paragraph each note points to carries that lens in its `data-lens` attribute. All 81 match.
- **Citations.** Every `card` exists in the reader, followup, revision or footnotes files, and is checked OK or FIXED. Every `source_id` is a manifest id and equals the card's source. Every `page` equals the card's `pdf_page`. No citation points to an unapproved candidate file.

**2. Content checks.**
- I read every item against its cited card's claim, quote and notes. Wherever an item adds a detail, date, figure or verb, I checked the source at the locator.
- New pages read this pass: Powers lines 2340-2392, 3143-3172 and 4471; 8-K line 426; the indictment's para. 8; hrg-hfs-enron-investors-pt1 lines 2896-2912; the Watkins transcript lines 5588-5600; hrg-help-pensions PDF 74.
- Sources and pages already verified in Rounds 1-3 were not re-read.

**3. Strips.** I checked every "was told", "were told", "received", "knew" and "learned" against the source's own verb, and I checked who is said to have said it.

**4. Outcomes, verbs and tone.** Outcomes are stated correctly throughout:
- Lay's conviction was vacated.
- Andersen's conviction was reversed, and the lens never calls the firm "innocent".
- Skilling's convictions were affirmed on remand.
- The indictment and SEC material is framed as "alleged".
- Taking the Fifth is never treated as guilt.
- The outside directors: "The library documents show no charges."

No item makes a new accusation, apart from the must-fix items below, which state warnings or receipt as fact where the source only records one person's testimony. Buffett does not appear.

## Findings

Severity: **must-fix** = factually wrong or unsupported; **should-fix** = wording, verb, attribution or tone; **note** = optional.

| # | chapter / lens / item | problem | source | required fix | severity |
|---|---|---|---|---|---|
| G-1 | all chapters, 76 citations with `source_id` `powers-report-sec` | These carry a PDF `page` (e.g. 42, 104, 133) copied from the cards. `powers-report-sec` is a .txt file; the numbers belong to the separate PDF copy (`powers-report`). `_meta` says `page` is null for .txt sources. The chapters leave `data-page` empty for Powers. | `_meta.cites`; site-notes (data-page only for PDFs) | Set `page` to null on every `powers-report-sec` citation. Keep `loc`. | should-fix |
| 1-1 | ch1 / money / note 1 (p13) | "all three Enron 2000 targets were about reported net income and how fast it grew". The JCT does not say what the 15% and double-digit growth targets measured. Lay's quoted release speaks of earnings per share. | rpt-jct-vol1 p. 63 (PDF 91), p. 64 (PDF 92) | "all three Enron 2000 targets were about reported earnings and how fast they grew". | should-fix |
| 1-2 | ch1 / board / summary 3 | Directors' 1985 start dates: the Winokur date is carried by B-076, a hearing card, only through the PSI list quoted in its claim. The examiner's earlier dates are mentioned but not cited. | rpt-psi-board p. 2 (PDF 6); batson-final-app-d n. 130 (via B-077 notes) | Optional: cite B-073 or B-077 (rpt-psi-board PDF 6) for both dates, and add a batson-final-app-d citation for the examiner's dates. | note |
| 2-1 | ch2 / knew / note 1 (p12) | "the SEC's accounting office **agreed to** mark-to-market accounting". Stronger than the source. | rpt-sga-watchdogs p. 32 (PDF 36): "would not object to the proposed change" | "said it would not object to mark-to-market accounting for an Enron subsidiary starting in 1992". | should-fix |
| 2-2 | ch2 / knew / strip 2 (1999) | WHO is "EnronOnline customers", but the text is about what later readers of the 10-K were told. | enron-10k-2000 lines 2392-2398 | Either WHO "Readers of the 2000 Form 10-K" with date 2001, or keep 1999 and rewrite the text as the launch only. | should-fix |
| 2-3 | ch2 / knew / summary 3 | "understanding it took expertise" is the writer's own judgment. | none | Optional: remove it or rephrase as a question. | note |
| 2-4 | ch2 / knew / strip 3 | The $22.1 billion conclusion is from the examiner's earlier (Second Interim) report, summarized in the Final. | batson-final p. 18 (PDF 21) | Optional: "The bankruptcy examiner, in an earlier report, later concluded ...". | note |
| 3-1 | ch3 / board / note 5 (p20) | "twice the Raptors were rescued **without a loss being recorded**". Wrong for the March 2001 restructuring: Enron recorded a $36.6 million credit reserve then. "Rescued" is also loaded. | powers-report-sec line 4471: "the restructuring allowed Enron to record only a $36.6 million credit reserve"; line ~4394: no reserve for year-end 2000 | "The Board: twice the Raptors' credit problem was fixed so that Enron avoided a large charge: no reserve at the end of 2000, and only a $36.6 million reserve in March 2001 instead of a charge of more than $500 million. The committee saw no evidence ...". | **must-fix** |
| 3-2 | ch3 / money / note 5 (p19) and summary 3 | The 72% figure appears without the committee's conditions. The chapter was corrected for this in Round 2 (item 3-5). | powers-report-sec lines 3654-3667 | Add "not counting the $710 million charge to end the Raptors" and "the committee noted it could not know what Enron would otherwise have done" (short form in the summary). | should-fix |
| 3-3 | ch3 / money / note 4 (p12) | "the pattern was to sell near the end of a quarter and buy back later, with LJM making a profit each time" generalizes seven 1999 sales, of which five were bought back. It drops the committee's caveat, which the card's notes say to include. | powers-report-sec lines 666-682 | "In seven sales near the ends of two 1999 quarters, Enron later bought back five, and LJM made a profit every time; the committee noted plausible, more innocent explanations for some buybacks." | should-fix |
| 3-4 | ch3 / money / note 6 (p21) | "Enron itself disclosed on November 8, 2001 that it believed Fastow had received more than $30 million" is cited only to the Powers card A-060. The statement is in Enron's 8-K. | enron-8k-nov-2001 line 426 (p. 9) | Add a citation to `enron-8k-nov-2001` (p. 9, line 426), or drop the sentence. | should-fix |
| 3-5 | ch3 / knew / summary 3 and strip 5 | "Kaminski's research group estimated a 68% probability" / strip WHO "Enron's research group: Estimated ..." is stated as fact. It is Kaminski's account to the committee, and Causey did not recall it. The chapter was fixed for this in Round 2. | powers-report-sec lines 3250-3262 ("Kaminski told us") | "Kaminski told the committee that his group estimated, in early 2000, a 68% probability ...". | should-fix |
| 3-6 | ch3 / money / note 3 (p8) | The McMahon account is correctly hedged ("the committee was told"). For balance: Fastow told the committee he did not take part in the negotiations, which the committee found contrary to other evidence. | powers-report-sec n. 17 (lines 2360-2370) | Optional: add "Fastow said he did not take part; the committee found that contrary to other evidence." | note |
| 4-1 | ch4 / knew / note 3 (p10) | "from August 15, 2001, **the documents show** that Lay had been warned in writing." No document shows receipt. The source is Watkins's testimony that she sent, and gave, Lay the anonymous letter. Lay did not testify. | hrg-commerce-skilling-watkins p. 12 (PDF 16): "I sent Mr. Lay an anonymous letter on August 15"; PDF 91 lines 5594-5596: "I gave him the anonymous letter on August 15" | "Who Knew What, When: Watkins testified that she gave Lay her anonymous letter on August 15, 2001. The letter said, as the Senate subcommittee staff quoted it, ...". | **must-fix** |
| 4-2 | ch4 / knew / strip 4 (2001-08-15, WHO: Kenneth Lay) | "**Received** Watkins's anonymous letter" is stated as fact. Only Watkins's testimony supports it. | same as 4-1 | "Watkins testified that she gave him her anonymous letter that day. It said: 'I am incredibly nervous that we will implode in a wave of accounting scandals.'" Keep the F-004 citation for the letter's wording. | **must-fix** |
| 4-3 | ch4 / knew / note 1 (p5) | "senior Andersen partners had put in writing how 'aggressive' Enron's accounting was". The writing is one partner's (Michael Jones's) Feb 6, 2001 e-mail describing the meeting. | batson-final-app-b-part1 p. 44 n. 131 (PDF 46); rpt-sga-watchdogs p. 22 (PDF 26) | "by February 2001, an Andersen partner's e-mail about the client-retention meeting noted how 'aggressive' Enron's accounting was, the Senate staff found." | should-fix |
| 4-4 | ch4 / knew / summary 1 | "Andersen's partners described Enron's accounting as pushing limits in February 1999". The February 1999 words are one partner's (Duncan's) handwritten note. | rpt-psi-board p. 17 (PDF 21) | "Andersen's lead partner wrote in February 1999 that many practices 'push limits'; a partner's February 2001 e-mail called the accounting 'aggressive' ...". | should-fix |
| 4-5 | ch4 / auditors / note 2 (p6) | "John Stewart testified ... that he found **the removal** unprofessional". Stewart called **Enron's request** unprofessional, and was upset that the firm agreed. | batson-final-app-b-part1 p. 43 (PDF 45): "[I] thought it was unprofessional for Enron to make such a request ... and I was upset that the firm had agreed to it" | "... testified that he found Enron's request unprofessional and was upset that the firm had agreed to it." Also: "the request ... came from the client's chief accounting officer, Bass was told". | should-fix |
| 4-6 | ch4 / auditors / summary 3 | "Andersen agreed to Causey's request to remove ... Bass" is stated as fact. The examiner reports what Bass was told. The chapter uses "was told". | batson-final-app-b-part1 p. 43 (PDF 45) | "In early 2001, the examiner reported, Carl Bass was told that Causey had asked for his removal from the Enron engagement and that Andersen had agreed." | should-fix |
| 4-7 | ch4 / board / summary 2 | "he never heard terms such as 'form over substance' used" drops "That I recall". The chapter was fixed for this in Round 2 (item 4-2). | hrg-psi-board p. 32 (PDF 42) | "... but that, as far as he recalled, he never heard terms such as 'form over substance' used." | should-fix |
| 4-8 | ch4 / knew / note 5 (p14) | "the dates matter here", placed next to the August warnings, invites the reader to infer what Lay knew on September 26. The SEC's allegation stands on its own, and the letter was about Raptor accounting, not the quarter's results. | sec-lay-complaint ¶81; B-055, B-056 | Drop "the dates matter here." Keep: "The SEC alleged these September 26 statements were false and misleading. Lay was later convicted, but his conviction was vacated after his death (Chapter 7)." | should-fix |
| 4-9 | ch4 / knew / Ask Why | "warnings reached ... Enron's chairman". For Lay, the source is Watkins's testimony. | as 4-1 | "... warnings reached Andersen's partners, Enron's accountants and, Watkins testified, Enron's chairman ...". | should-fix |
| 5-1 | ch5 / money / note 5 (p12) | "terms making loans come due early if Enron's credit rating **or** stock price fell". For the $3.9 billion, the 10-Q says a trigger needed **both** a loss of investment grade **and** a low stock price. The $690 million note also became payable only "absent Enron posting collateral". | enron-10q-q3-2001 lines 700-718 | "... terms that could make debts come due early if Enron's credit rating fell (for some, only if its stock price was also low). One downgrade meant a $690 million note would come due unless Enron posted collateral, and about $3.9 billion more could follow." | should-fix |
| 5-2 | ch5 / knew / note 3 (p14) | "the analysts had the same public news as everyone else" is not in the source, and may not be true of analysts. | rpt-sga-watchdogs p. 5 (PDF 9) | Delete that clause: "Who Knew What, When: most analysts kept recommending the stock after the bad news. The Senate staff tied this to their firms' investment-banking interests." | should-fix |
| 5-3 | ch5 / money / note 7 (p19) | "The Senate staff also found a sham sale ...": "sham" is the staff's word. | rpt-psi-fishtail p. 3 (PDF 7) | Put the word in quotation marks: "what the Senate staff called a 'sham' sale". | note |
| 5-4 | ch5 / knew / strip 1 (WHO: "Investors on the conference call") | The source says the $1.2B cut was disclosed on the analyst conference call. | batson-final p. 15 (PDF 18); Powers p. 30 | Optional: WHO "Analysts and investors on Enron's conference call". | note |
| 6-1 | ch6 / knew / Ask Why | "Andersen's lawyer **reminded the Enron team** of the retention policy on October 12." Temple e-mailed partner Michael Odom suggesting "it might be useful to consider reminding the engagement team". She did not remind the team herself. Also, the shredding "appears to have stopped shortly after" November 9 (Andersen's words). | hrg-hec-andersen-shredding PDF 49 (e-mail image, "To: Michael C. Odom"); PDF 39 | "Andersen's lawyer suggested on October 12 that the Enron team be reminded of the retention policy, and, by Andersen's account, the shredding stopped shortly after November 9. ..." | **must-fix** |
| 6-2 | ch6 / knew / summary 3 | "Andersen's lawyer e-mailed a reminder of the retention policy on October 12" is loose for the same reason as 6-1. | as 6-1 | "Andersen's lawyer e-mailed a partner on October 12 suggesting the engagement team be reminded of the retention policy; ..." | should-fix |
| 6-3 | ch6 / auditors / note 7 (p12) | "Duncan did not testify himself" is ambiguous and, read broadly, wrong: Duncan testified at Andersen's 2002 criminal trial, as the examiner cites repeatedly. | hrg-hec-andersen-shredding p. 27 (PDF 31); batson-final-app-b-part1 nn. 13, 202-207 | "Duncan declined to answer questions at the hearing." | should-fix |
| 6-4 | ch6 / auditors / note 5 (p8) | "thirty meetings of about an hour each ... is limited time to explain the accounting of a company as complex as Enron" is the writer's judgment. | batson-final-app-b-part2 p. 131 n. 472 (PDF 29) | Replace it with the source: "Duncan wrote in December 2000 that the presentation had to fit 'about a 30 – 45 minute presentation', so 'we necessarily have to stay at a certain level.'" Or phrase it as a question. | should-fix |
| 6-5 | ch6 / auditors / note 12 (p19) | "84 percent of large public companies said they wanted more audit firms" reads as all large companies. It was a survey. | gao-03-1158 Highlights (C-052) | "84 percent of the large public companies GAO surveyed ...". | note |
| 6-6 | ch6 / money / summary 2 | "Andersen testified that much of the 'consulting' was work typically done by the auditor". It was Andersen partner Michael Odom, as the chapter now says. | hrg-hec-andersen-shredding p. 178 (PDF 182) | "Andersen partner Michael Odom testified ...". | note |
| 6-7 | ch6 / auditors / note 6 (p9) | Quotes the Syllabus while the chapter now quotes the full opinion. Correctly labeled, so acceptable. | andersen-scotus-full-usreports p. 704 | Optional: cite the full opinion for the same words. | note |
| 7-1 | ch7 / knew / strip 1 (2001-10-15, WHO: Jan Fleetham) | "Received a letter dated October 8 ..." is stated as fact. The source is her written statement to an unsworn hearing. | hrg-help-pensions p. 65 (PDF 69); no oath in that transcript (Round 2, item 7-3) | "Told the committee, in her written statement, that on October 15 she received a letter dated October 8 ...". | should-fix |
| 7-2 | ch7 / money / note 4 (p11) and summary 4 | "The plan's chairman testified" and "a congressman testified". No oath appears in the HELP hearing. The chapter uses "told the committee". Also, Prentice chaired the plan's Administrative Committee. | hrg-help-pensions PDF 23, 74 | "The chairman of the plan's administrative committee told the committee ..."; "a congressman told the committee ...". | should-fix |

Checked with no problems (examples):
- **ch1:** revenue, assets and net-income ratios; the 1985 acquisition; the Enron 2000 strip; the SEC 1992 strip.
- **ch2:** all money notes; the 150% and 10% growth figures.
- **ch3:** Chewco figures; the LJM1 and LJM2 approval strips; the board code-of-conduct note (F-006, F-007, including the directors' "applied, not waived" disagreement); the Kaminski/Buy disagreement.
- **ch4:** the Watkins August 22 strip (attributed); the Lay forum strip (alleged); the Skilling strip.
- **ch5:** all strips; the $613M sum (79 + 139 + 258 + 137); the debt figures; the "tip of the iceberg" timing note.
- **ch6:** the indictment allegations (G-015, G-017), clearly labeled; Berardino's spoken statement (G-033, verbatim at lines 2906-2909); the Temple, Duncan and SEC timeline strips; the GAO notes.
- **ch7:** Lay's credit-line periods reconciled; Kopper's $12M; Fastow's two forfeiture figures; the Batson conclusions on the directors (with hedges); Lay's unsworn interview with the examiner; Skilling on remand; Fastow's admissions ("the Justice Department announced").

## Counts and verdicts

| chapter | must-fix | should-fix | note | verdict |
|---|---|---|---|---|
| ch1 | 0 | 1 (+ G-1) | 1 | PASS AFTER FIXES |
| ch2 | 0 | 2 (+ G-1) | 2 | PASS AFTER FIXES |
| ch3 | 1 | 4 (+ G-1) | 1 | PASS AFTER FIXES |
| ch4 | 2 | 6 (+ G-1) | 0 | PASS AFTER FIXES |
| ch5 | 0 | 2 (+ G-1) | 2 | PASS AFTER FIXES |
| ch6 | 1 | 3 (+ G-1) | 3 | PASS AFTER FIXES |
| ch7 | 0 | 2 (+ G-1) | 0 | PASS AFTER FIXES |
| **Total** | **4** | **20 + G-1** | **9** | |

- **Must-fix items:**
  - 3-1: the March 2001 Raptor fix did record a $36.6M reserve.
  - 4-1 and 4-2: Lay's receipt of the Watkins letter must be attributed to her testimony.
  - 6-1: Temple suggested a reminder to a partner; she did not remind the team.
- All four are one-sentence rewrites, with wording given above. After the fixes, a re-check of the changed items only is enough.
- The mechanical layer is clean: paragraph positions, lens tags, card status and source ids all pass.

No web was used and no gaps were logged. Fingerprints for every source read this pass were verified in earlier rounds, and none has changed since.
