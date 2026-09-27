# Fact-Checker (instance C), Phase 2: Sarbanes-Oxley cards S-001 to S-080

Checked: all 80 cards in `work/facts/reader-sox.json` (Reader D). No web used; nothing in `sources/` edited.

## Summary

- **Result:** 28 OK, 52 FIXED, 0 REJECTED. Every quote was found verbatim at its locator (74 by exact script match; 6 by manual reading: two-column pages S-023, S-025, S-046; page break S-072; curly/backtick quotes and footnote marker S-017, S-068).
- **12 substantive fixes** to claims or notes (S-010, S-019, S-021, S-024, S-032, S-040, S-048, S-056, S-060, S-064, S-072, S-079). The other 40 FIXED cards had only their verb changed to match the source type.
- **Verbs now follow the coordinator's rule.** Statute: "requires" (S-012 "permits"; S-078 "records"). Committee report: "stated". Senators on the floor or at a hearing: "said". Witness prepared statements and Pitt's written testimony: "said", not "testified". Signing statement: "stated". Bush's remarks: "said". SEC orders: "issued". SEC press release: "announced". GAO, CRS and SEC reports: "reported" or "stated".
- **Corrections logged:** `build-log/corrections.md` rows 122-137.
- **Fingerprints:** all matched `sources/download_log.csv`. Checked: sox-plaw-html, sox-srpt-107-205, sox-hrpt-107-414, sox-hrpt-107-610, sox-crs-summary, sox-pitt-testimony, sox-hrg-banking-v1, -v2, -v3, sec-sox704-report, gao-03-864, sox-bush-remarks, sox-bush-signing-statement, sec-pcaob-101d-order, sec-pcaob-103-order, sec-press-2003-52; and, for the Lay-loan cross-check, sec-lay-complaint and rpt-jct-vol1.

## Watch-list rulings

1. **Sec. 201: nine items vs. "eight categories" (S-042).** The statute (Exchange Act 10A(g), lines 1708-1720) lists eight named services plus a ninth, "any other service that the Board determines, by regulation, is impermissible." The SEC's 704 report (p. 41) says "eight categories" and does not mention the ninth. Both are accurate descriptions of different things. **Site wording:** "The Act bans eight named kinds of non-audit services, plus any other service the PCAOB bans by rule." Don't write "eight categories" or "nine categories" without saying which count is meant.
2. **Sec. 402: CRS "of any kind" vs. the statute's exceptions (S-060).** CRS-8 says Sec. 402 "prohibits personal loans of any kind." That overstates it. Sec. 13(k)(1)-(3) exempts loans outstanding at enactment (if not materially changed), consumer credit, credit cards, open-end credit, home-improvement and manufactured-home loans, and broker margin loans made in the ordinary course on public terms, plus bank loans covered by Federal Reserve insider-lending rules. Schumer himself said "with certain narrow exceptions" (v3 p. 1437). Claim fixed. **Follow the statute. Never quote CRS's "of any kind" as the rule.**
3. **Sec. 807: 10 vs. 25 years (S-075, S-076).** Both are verified. On July 9, 2002 Daschle described the Leahy amendment's crime as "a tough new 10-year felony" (v3 p. 1226). The enacted 18 U.S.C. 1348 says "not more than 25 years" (statute line 3783; CRS-10 agrees). No library source says when or why the maximum changed, and the conference statement has no section-by-section explanation (confirmed, PDF 69-70). Present both figures and don't explain the change. Don't confuse this with Bush's "from 5 to 20 years" (signing remarks p. 1285), which is about other fraud penalties.
4. **Lay "$70 million" (S-061).** The quote is verified. The Senate report's footnote 59 rests entirely on the *Wall Street Journal* (May 3, 2002), so **it must not be stated as fact.** Allowed: "The Senate Banking Committee's report, citing the Wall Street Journal, said ..." Library sources give figures for different periods, and they must not be merged:
   - the SEC **alleged** Lay sold "over $70 million in Enron stock" in 2001 to repay advances on an unsecured line of credit (sec-lay-complaint p. 41, para. 101). Card B-005: $77,525,000 in advances, Jan 25-Nov 27, 2001.
   - the JCT staff report says there were 25 withdrawals in 2001 totaling $77.5 million, "of which all but $7.5 million was repaid" (rpt-jct-vol1 PDF 43 [p. 15]; checked against the page image). It doesn't say how they were repaid. Note that JCT counts 25 transactions and B-005 counts twenty.
   - the bankruptcy **examiner concluded** Lay borrowed and repaid with stock "over $94 million", May 1999-Oct 2001 (card B-014).
   Reader D's gap 11 can be closed. The library has investigative sources, so the Scout doesn't need to look for one.

## Other points for writers

- **S-019:** the two SEC order files are landing pages only. The site may say the SEC issued orders under Secs. 101(d) and 103(a)(3)(B) on April 25, 2003, and that the SEC and PCAOB "announced" the Board was ready (sec-press-2003-52). It may not say what the interim standards were (Reader D gap 1 stands).
- **S-079:** the Senate had already replaced the entire House text. In conference, the House accepted a substitute for both versions.
- **Floor speeches** (S-056, S-063, S-065, S-070): Schumer's statements about Fastow's $30 million in fees and about Raptor (v3 p. 1439), his "$5 billion" in loans, and Leahy's "fire them" gloss are characterizations. Take Enron facts from the Powers/Batson/SEC cards.
- **Breeden's "$25 million each year"** (S-030): this is his estimate. Don't use it as Andersen's fee.

## Card-by-card verdicts

| Card | Verdict | Note |
|---|---|---|
| S-001 | FIXED | Statute; verb set to 'requires'. Claim matches Sec. 101(d). 270-day arithmetic (Apr 26, 2003) re-computed and correct; it is the card's arithmetic, not a source statement. |
| S-002 | FIXED | Statute; verb set to 'requires'. Claim matches 101(e)(4)-(5) (lines 463-494). |
| S-003 | FIXED | Statute; verb set to 'requires'. 'Fixed retirement payments' = 'fixed continuing payments ... under standard arrangements for the retirement' (lines 452-461). |
| S-004 | FIXED | Statute; verb set to 'requires'. Late-October 2003 date in notes is arithmetic (Oct 22, 2003), not a source statement; do not print it as the registration deadline. |
| S-005 | FIXED | Statute; verb set to 'requires'. Claim matches 102(b)(2)(A)-(B). |
| S-006 | FIXED | Statute; verb set to 'requires'. (ii) and (iii) confirmed at lines 703-713. |
| S-007 | FIXED | Statute; verb set to 'requires'. Same-time SEC approval confirmed at lines 789-793. |
| S-008 | FIXED | Statute; verb set to 'requires'. Three-year rule confirmed at lines 850-853. |
| S-009 | FIXED | Statute; verb set to 'requires'. Transmission to SEC and state regulators confirmed at 104(g)(1). |
| S-010 | FIXED | FIXED: the claim implied suspension, revocation and bars were available for any violation; Sec. 105(c)(5) limits them (and the higher fines) to intentional/knowing/reckless conduct or repeated negligence. Verb set to 'requires'. |
| S-011 | FIXED | Statute; verb set to 'requires'. Exception for initial/transitional standards confirmed (107(b)(2)). |
| S-012 | FIXED | Statute; verb set to 'permits' (the SEC 'may recognize'). Claim summarizes 19(b)(1)(A)(i)-(v) accurately. |
| S-013 | FIXED | Statute; verb set to 'requires'. SEC budget approval confirmed at 109(b); scholarship use is subject to appropriations (109(c)(2)). |
| S-014 | OK | Committee report quoting O'Malley's testimony (fn. 3); 'ten days of hearings' confirmed. Attribute: 'the committee report quoted O'Malley'. |
| S-015 | OK | Committee report quoting Volcker (fn. 4). Verified. |
| S-016 | OK | Committee report fn. 5. Verified. |
| S-017 | OK | Committee report; inspection rationale confirmed at PDF 13 [p. 9], section D. |
| S-018 | OK | Title page confirmed; full printed title begins 'The Legislative History of the Sarbanes-Oxley Act of 2002:'. 'Ten hearings' confirmed at S. Rept. 107-205 PDF 6 [p. 2]. |
| S-019 | FIXED | FIXED: the landing page for Rel. 33-8222 gives only its title; the claim no longer says what the order did, only what Sec. 103(a)(3)(B) covers. Added the SEC/PCAOB announcement (sec-press-2003-52, fingerprint OK; verb 'announced'). Verb for the orders: 'issued'. |
| S-020 | OK | SEC report to Congress. The sentence covers 'the accounting and auditing process'. Verified. |
| S-021 | FIXED | FIXED: 'supported' overstated Pitt's words ('shares many characteristics that the Commission believes are necessary'). Verb set to 'said' (written testimony). |
| S-022 | OK | Committee report. Verified. |
| S-023 | OK | GAO report (Highlights, two-column page; quote read down the left column). Report dated July 2003; Sec. 701 mandate confirmed. |
| S-024 | FIXED | FIXED: source says 'For most large public companies, the maximum number of choices'; claim had said 'the largest companies' choice'. |
| S-025 | FIXED | Official record of presidential remarks; verb set to 'said'. Two-column page confirmed. |
| S-026 | OK | Committee report citing SEC figures. Verified. |
| S-027 | OK | Committee report. Verified. |
| S-028 | OK | Committee report. Verified; Superior Bank and industry announcement notes confirmed. |
| S-029 | OK | Committee report. Verified. |
| S-030 | FIXED | Prepared statement in the hearing record: Breeden's characterization, not a finding; verb set to 'said'. Do not use his '$25 million each year' as a fee fact. |
| S-031 | FIXED | Additional views of one member (LaFalce), not the committee; verb set to 'said'. Verified. |
| S-032 | FIXED | FIXED: Pitt compared these tools with one specific suggestion, not with all alternatives; claim now quotes his comparison. Verb set to 'said'. |
| S-033 | FIXED | Statute; verb set to 'requires'. 5% de minimis exception confirmed (lines 1760-1778). |
| S-034 | OK | Committee report. Levitt, Hills and O'Malley quotes confirmed at PDF 25 [p. 21]. |
| S-035 | FIXED | Statute; verb set to 'requires'. Verified. |
| S-036 | FIXED | Statute; verb set to 'requires'. Verified. |
| S-037 | FIXED | Statute; verb set to 'requires'. Verified. |
| S-038 | FIXED | Prepared statement; verb set to 'said'. Verified. |
| S-039 | FIXED | Prepared statement (Walker, Mar 5, 2002); verb set to 'said'. Verified. |
| S-040 | FIXED | FIXED: 'top finance posts' was inaccurate (CEO is covered); CEO example now attributed to the committee. |
| S-041 | FIXED | Statute; verb set to 'requires'. Verified. |
| S-042 | OK | SEC report: its list names eight services and omits the statute's ninth item ('any other service that the Board determines, by regulation, is impermissible', Sec. 201, line 1719). Site wording: 'The Act bans eight named services plus any other service the PCAOB bans by rule (the SEC's 2003 report counts eight categories).' Never write 'eight' or 'nine categories' without that explanation. |
| S-043 | FIXED | Statute; verb set to 'requires'. Verified. |
| S-044 | OK | Committee report. 'In effect the bill adopts this proposal' confirmed. |
| S-045 | OK | SEC report fn. 103 confirmed; release number printed 'Rel. No. 34-8124' split across lines. Cite title and date only. |
| S-046 | FIXED | Official record of presidential remarks; verb set to 'said'. Verified. |
| S-047 | OK | Signing statement: the President's reading, not law. Verified. |
| S-048 | FIXED | FIXED (notes only): removed unsupported 'Sec. 906 was a Senate floor addition'. Verb set to 'requires'. |
| S-049 | FIXED | Statute; verb set to 'requires'. Verified. |
| S-050 | OK | Committee report quoting Bowsher (fn. 63, Mar 19, 2002). Verified. |
| S-051 | OK | Committee report: statement of intent, not a result. Verified. |
| S-052 | FIXED | Statute; verb set to 'requires'. Verified. |
| S-053 | FIXED | Statute; verb set to 'requires'. Verified. |
| S-054 | OK | Committee report. Verified. |
| S-055 | FIXED | Prepared statement; verb set to 'said'. Verified, including the 'does not mean ... violates GAAP' balance. |
| S-056 | FIXED | FIXED: 'with Senator Shelby' -> 'for himself and Senator Shelby' (clerk's reading); amendment number added; 'matches' -> 'closely matches'. Verb set to 'said'. |
| S-057 | OK | SEC report. Verified. |
| S-058 | OK | SEC report fn. 58 verified; Enron highlight on PDF 34 [p. 30] uses 'alleged'; A.A.E.R. No. 1640 dated Oct. 2, 2002 (fn., line 1728). |
| S-059 | FIXED | Pitt's written testimony; verb set to 'said'. Verified. |
| S-060 | FIXED | FIXED: claim listed only one statutory exception; now lists all in 13(k)(1)-(3). CRS-8's 'of any kind' overstates the ban - follow the statute. Verb set to 'requires'. |
| S-061 | OK | Quote verified (fn. 59). The $70 million figure rests on a newspaper (Wall Street Journal, May 3, 2002) cited by the committee. It must NOT be stated as fact. Allowed: 'The Senate committee's report, citing the Wall Street Journal, said ...'. Other library sources give different figures for different periods: the SEC alleged Lay sold over $70 million in Enron stock in 2001 to repay advances on his line of credit (sec-lay-complaint p. 41, para. 101; card B-005: advances of $77,525,000, Jan 25-Nov 27, 2001); the JCT staff report says 25 withdrawals in 2001 totaling $77.5 million, all but $7.5 million repaid (rpt-jct-vol1 PDF 43 [p. 15], checked against the page image); the bankruptcy examiner concluded Lay borrowed and repaid with stock over $94 million, May 1999-Oct 2001 (card B-014). If the site needs a figure, use one of these with its attribution and period; do not merge them. |
| S-062 | OK | Committee report. Verified. |
| S-063 | FIXED | Floor statement: Schumer's characterization; verb set to 'said'. Amendment 4295 agreed to (PDF 282 [p. 1438]); Congressional Record for Friday, July 12, 2002. Schumer himself said the ban has 'certain narrow exceptions'. His '$5 billion' is his figure. |
| S-064 | FIXED | FIXED: 'became the basis of the Act's criminal provisions' was an inference; now states only that Title VIII carries the same name (Sec. 801, line 3487). Verb set to 'said'. |
| S-065 | FIXED | Floor statement; verb set to 'said'. Verified; do not quote the 'As we say' sentence. Andersen's conviction was later reversed (2005) - cite from library outcome cards. |
| S-066 | FIXED | Prepared statement; verb set to 'said'. Verified. |
| S-067 | FIXED | Statute; verb set to 'requires'. Verified. |
| S-068 | OK | Signing statement. Verified (source uses ``corruptly''; straight quotes in card). |
| S-069 | FIXED | Statute; verb set to 'requires'. 180-day court option and remedies (incl. attorney fees) confirmed at lines 3700-3747. |
| S-070 | FIXED | Floor statement; verb set to 'said'. Printed under July 9, 2002. Verified. |
| S-071 | FIXED | Floor statement; verb set to 'said'. Verified. |
| S-072 | FIXED | FIXED: 'She later wrote' -> the committee bill 'included her amendment' (S. Rept. 107-205, PDF 29 [p. 25], lines 1727-1731); 'it appears' kept as her impression. Verb set to 'said'. |
| S-073 | OK | Signing statement. Statute wording 'any Member of Congress or any committee of Congress' confirmed (line 3687). |
| S-074 | FIXED | Statute; verb set to 'requires'. Verified. |
| S-075 | FIXED | Statute; verb set to 'requires'. Maximum is 25 years (line 3783). Also covers attempts and schemes to obtain money by false pretenses. |
| S-076 | FIXED | Floor statement; verb set to 'said'. Both figures verified: Daschle described a '10-year felony' (July 9, 2002); enacted Sec. 807 sets 'not more than 25 years' (card S-075). The library does not explain the change; do not explain it. Do not confuse with Bush's 'from 5 to 20 years' (signing remarks), which refers to other fraud penalties. |
| S-077 | OK | CRS report. Verified. |
| S-078 | FIXED | Legislative-history note printed at the end of the Public Law; verb set to 'records'. Senate 'passed, amended, in lieu of S. 2673' (i.e., passed H.R. 3763 as amended). 'Approved July 30, 2002' confirmed. |
| S-079 | FIXED | FIXED: the claim said the Senate text replaced the House bill 'in conference'. The statement says the Senate amendment struck the House bill and the House receded 'with an amendment that is a substitute for the House bill and the Senate amendment'. Confirmed no section-by-section explanation (PDF 69-70). |
| S-080 | OK | SEC report executive summary; 515 actions from 227 investigations, 126 revenue-recognition matters, 18 audit firms and 89 auditors confirmed (PDF 5-7). |
