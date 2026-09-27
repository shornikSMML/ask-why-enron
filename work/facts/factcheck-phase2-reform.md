# Fact-Checker (instance C), Phase 2: "Why This Matters to You" and the SOX map diagram

I checked two items:
- `work/drafts/why-it-matters.html`, built from `work/drafts/reform-src/why-it-matters.src.html`. It has 71 citations to 70 distinct cards.
- `images/diagram-sox-map.svg` and `images/diagram-sox-map-narrow.svg`, with the fact cards listed for them in `images/credits.json`.

I edited neither file. I used no web.

Method:
- I read every sentence against its card. Where a card was not enough, I read the source itself: the statute text, S. Rept. 107-205, the Powers Report (lines 900-915), the PSI board report (p. 50, PDF 54) and the other library files named below.
- I re-ran `expand.py` into scratch. The output is identical to `why-it-matters.html`, so the page matches its source.
- The diagram fingerprints match `credits.json`: `sha256` 2582826... and `narrow_sha256` a1aa660....
- As instructed, I ignored the six new glossary terms.

## Verdicts

| Item | Verdict |
|---|---|
| `why-it-matters.html` | **PASS WITH FIXES.** There are no high-severity problems. Items 1-14 below must be fixed before the page ships (medium) or should be fixed (low). |
| `diagram-sox-map.svg` / `-narrow.svg` | **PASS WITH FIXES.** Items 15-19. The wide and narrow versions have identical text, so each fix applies to both. |

## What passed

- **§201 (ruling 1):** the page says "eight named ... plus any other service the PCAOB bans by rule" and gives the SEC's "eight categories" in parentheses with attribution. The diagram uses the same wording. Correct.
- **§402 (ruling 2):** the page follows the statute ("with exceptions set out in the statute"). It does not use CRS's "of any kind". Correct. The diagram does not cover §402.
- **§807 (ruling 3):** both the page and the diagram give 25 years (statute) and Daschle's "10-year felony" (floor). Neither explains the change. Correct.
- **Lay's figures (ruling 4):** the Wall Street Journal-based "$70 million" is not used. The page uses the PSI report's "over $77 million ... October 2000 to October 2001", attributed to the subcommittee's report and with its time period. It does not merge figures from other sources. Correct, apart from the citation locator (item 5). The diagram does not use a Lay figure.
- **No post-2003 facts:** the latest dated facts are April 25, 2003 (PCAOB, C-081) and July 2003 (GAO, S-023). The "today" section says plainly that the library stops at 2003. The one remaining problem is present-tense advice (items 10-13).
- **Andersen's conviction** is mentioned once, and in the same sentence as the 2005 reversal (C-038 with G-018). The diagram does not mention Andersen.
- **Verbs:**
  - Statute paragraphs use "requires" or equivalent operative verbs.
  - Floor statements (S-065, S-070, S-071, S-076) use "said" or "described".
  - Prepared statements (S-030, S-038) use "said".
  - The indictment (G-016) uses "alleged".
  - The examiner (C-031) uses "concluded".
  - The committee report uses "stated".
- **Tone:** neutral throughout. The page uses "use" rather than the PSI finding's word "abuse" (B-016), which is acceptable because the quoted finding is not being reproduced. Nothing is sensational.
- **Cards:** every cited card is checked OK or FIXED. All quotes match their cards verbatim.

## Findings

| # | Location | Problem | Source | Required fix | Severity |
|---|---|---|---|---|---|
| 1 | Page, §302 "The Enron problem": "It also found that Lay, as chief executive, bore ultimate responsibility.{{A-062}}" | Overstates the finding about a real person. Powers says Lay "had the ultimate responsibility for taking reasonable steps to ensure that the officers reporting to him performed their oversight duties properly" and that "a large measure of the responsibility rests with the CEO". It does not say he bore ultimate responsibility without qualification. | powers-report-sec lines 906-912 (Exec. Summary, p. 19) | Write: "It also found that Lay, as chief executive, had 'the ultimate responsibility' for making sure the officers reporting to him carried out their oversight of the partnerships." | medium |
| 2 | Page, PCAOB "The Enron problem": "Witnesses said inspections 'must no longer be left to peer reviews ...'{{S-017}}" | The quoted words are the committee report's paraphrase, not a witness's words. The report says: "A number of witnesses emphasized, for example, that inspections must no longer be left to ..." | sox-srpt-107-205 p. 7 (PDF 11), lines 595-598 | Write: "The Senate committee's report said a number of witnesses emphasized that inspections 'must no longer be left to ...'" | medium |
| 3 | Page, §404 "The Enron problem": "the Senate report noted that GAO had recommended ... in 1996, and that the SEC had not adopted it.{{S-050}}" | The report quotes former Comptroller General Bowsher saying this. It is not the committee's own statement. | sox-srpt-107-205 p. 31 (PDF 35), lines 2104-2119 | Write: "the Senate report quoted former Comptroller General Charles Bowsher, who said GAO had recommended ... in 1996 and the SEC had not adopted it." | medium |
| 4 | Page, independence "What it means for you": "If you are ever offered a senior finance job at a company you audited, the cooling-off rule applies to you." | This misstates §206 and presents it as a current rule. The ban falls on the audit firm, not the employee. It covers only the CEO, CFO, controller, chief accounting officer or equivalent, only someone who worked on that audit, and only within one year. Other "senior finance jobs" are not covered. | sox-plaw-html Sec. 206, lines 1898-1906; S-037, S-040 | Example: "Under the 2002 law, if someone who worked on the audit becomes the company's CEO, CFO, controller or chief accounting officer within a year, the firm may not keep auditing that company." | medium |
| 5 | Page, §402 paragraph, B-016 citation | The citation points to p. 3 (PDF 7), the finding. The "$77 million, October 2000 to October 2001, repaid with Enron stock" detail is on p. 50 (PDF 54). A reader following the link will not find the figure. | rpt-psi-board p. 50 (PDF 54), text lines ~3276-3280 (verified) | Add a second citation for the figure: `{{B-016@p. 50, Board oversight of Lay's credit line#54}}`. Keep the p. 3 citation for the finding. | medium |
| 6 | Page, §404 "What it means for you": "Many entry-level jobs involve carrying out, testing, or documenting controls ..." | A specific claim about current job practice with no library source. | none in library | Soften to a general statement, e.g. "Jobs in finance and accounting can involve carrying out or checking controls, such as ..." | medium |
| 7 | Page, PCAOB "What the law requires": "Once the Board was running, it became illegal for an unregistered firm ...{{S-004}}" | Imprecise. Registration became mandatory 180 days after the SEC's Sec. 101(d) determination, not when the Board started running. | sox-plaw-html Sec. 102(a), lines 571-575 | Write: "Starting 180 days after the SEC declared the Board ready, it became illegal ..." Don't give a calendar date (the date is arithmetic only; see S-004). | low |
| 8 | Page, §404 "What the law requires": "A separate section requires every audit report to describe the auditor's testing of internal controls.{{S-006}}" | Sec. 103 requires the PCAOB's auditing standards to include this requirement. The Act does not impose it directly. | sox-plaw-html Sec. 103(a)(2)(A)(iii), lines 692-713 | Write: "Section 103 requires the Board's auditing standards to make every audit report describe ..." | low |
| 9 | Page, §401 sentence: "Section 401 requires companies to disclose all material off-balance-sheet arrangements ...{{S-052}}" | The section requires the SEC to issue rules within 180 days that make reports disclose them. | sox-plaw-html Sec. 401(a), lines 2598-2608 | Write: "Section 401 requires the SEC to issue rules making companies disclose ..." | low |
| 10 | Page, §302 "What it means for you": "Expect them to ask how you got those numbers." | A prediction about current workplace practice. | none | Write: "They may ask how you got those numbers." | low |
| 11 | Page, PCAOB "What it means for you": "the 2002 law means your firm's work can be inspected by outsiders" | Present tense describes current practice. It is acceptable only as a statement of the 2002 law. | S-008; "today" section | Write: "under the 2002 law, your firm's work could be inspected by the Board ..." The scholarship sentence is fine. Optionally add "if Congress funds it" to match S-013. | low |
| 12 | Page, whistleblower "What it means for you": "this one made punishing people for it illegal" | Scope is left out. §806 covers employees of public companies, reports through the channels it names, and gives a civil remedy. | sox-plaw-html Sec. 806; C-080, S-069 | Write: "... made it illegal for a public company to punish employees for reporting through those channels." | low |
| 13 | Page, independence "The Enron problem": "Andersen's witnesses testified that much of the so-called consulting was audit-type work.{{C-020}}" | Per C-020, partner Michael Odom said this. C.E. Andrews testified only that audit-related fees were $25 million, "essentially half". | hrg-hec-andersen-shredding p. 178 (C-020) | Write: "An Andersen partner testified that much of the so-called consulting was audit-type work." | low |
| 14 | Page, independence "The Enron problem": "Andersen's own policy rotated the lead partner after seven years, not five.{{C-036}}" and "{{S-026}} ... 73 percent of accounting firms' total fees" | (a) The first sentence has no attribution. The source is the examiner's account of Audit Committee minutes. (b) S-026 says "on average". | batson-final-app-b-part2 p. 131 (C-036); sox-srpt-107-205 p. 15 (S-026) | (a) Add "according to the bankruptcy examiner's report". (b) Write "on average, 73 percent". | low |
| 15 | Diagram row 2, problem: "No required yearly report on whether a company's internal controls work" | Too broad. The same Senate report says banks had faced a similar requirement since 1991 (FDI Act Sec. 36). The problem was that the SEC had not adopted GAO's 1996 recommendation for public companies. | sox-srpt-107-205 p. 31 (PDF 35), lines 2104-2129 (S-050) | Write: "No required yearly report on whether a public company's internal controls work" (or "for most public companies"). | medium |
| 16 | Diagram row 5, §806: "can complain to the Labor Department within 90 days, then go to court" | Suggests a free choice to go to court. Court is available only if Labor has not decided within 180 days. | sox-plaw-html Sec. 806, 1514A(b)(1)(B), lines 3706-3713 (S-069) | Write: "... within 90 days; if there is no decision in 180 days, can go to court". | medium |
| 17 | Diagram row 4, §202: "The audit committee must approve in advance every service the auditor provides" | Leaves out the small de minimis exception for non-audit services. | sox-plaw-html Sec. 202, 10A(i)(1)(B) (S-033) | Add "(with a small exception)" or "almost every service". | low |
| 18 | Diagram row 5, §802: "Two new crimes for destroying or falsifying records; auditors must keep audit work papers 5 years" | Blurs the two crimes. §802's two new crimes are 18 U.S.C. 1519 (destroying or falsifying records) and 1520 (auditors failing to keep work papers). | sox-plaw-html Sec. 802 (C-079); S-065 | Write: "Two new crimes: destroying or falsifying records (up to 20 years), and auditors failing to keep audit work papers for 5 years (§802)." | low |
| 19 | Page `<figcaption>` for the diagram: "The parts of Sarbanes-Oxley on this page, and the Enron problems each one answers." | The diagram covers five parts. It leaves out §§401, 402 and 1102, which the page discusses. Its problem column summarizes congressional statements (the diagram's own footer says so). | diagram footer | Write: "Five parts of Sarbanes-Oxley covered on this page, and the problems lawmakers and witnesses linked to each." | low |

## Notes (no fix required)

- **Diagram row 4, "Audit partners must rotate (§203)":** this gives no period. Adding "after 5 years" would be accurate, per C-075 (statute lines 1802-1812).
- **Diagram footer and credits:** these match the sources used. `fact_cards` in `credits.json` covers every row.
- **Page placement of §§401 and 402:** they sit under the §404 heading. The text introduces them as "Two related rules", which is acceptable. The editor may prefer a separate subsection.
- **C-021:** the examiner also uses $47.9 million for 2000 fees (Final Report p. 39). The page says "Sources give different figures" and links to Chapter 6, which is sufficient.

## Final

I re-checked the fixes against `work/facts/fixes-phase2-reform.md`, the rebuilt page and both SVGs.
- Rebuilding the page from its source reproduces `why-it-matters.html` exactly: 72 citations to 70 cards, all checked OK or FIXED.
- The SVG fingerprints match the updated `credits.json` (27290af... and 855e5dc...).
- The applied corrections are logged in `build-log/corrections.md`, rows 151-166.

| # | Verdict | Note |
|---|---|---|
| 1 | OK | "the ultimate responsibility" is verbatim (Powers lines 907-908). The scope matches: his officers' oversight of the partnerships. |
| 2 | OK | Now attributed to the committee's report. |
| 3 | OK | Now attributed to Bowsher, as the report quotes him. |
| 4 | **FAIL** | See the required fix below. |
| 5 | **FAIL (minor)** | The second citation works: data-page 54, p. 50, where the "$77 million ... October 2000 to October 2001 ... exclusively with Enron stock" figure appears (text lines 3281-3284). But its label, "Board oversight of Lay's credit line", is not a heading in the report. The passage falls under Finding (5), which starts on p. 49 (PDF 53). |
| 6 | OK | "can involve" is a general statement and makes no claim about current practice. |
| 7 | OK | Matches §102(a). No calendar date is given. |
| 8 | OK | Matches §103(a)(2)(A)(iii). |
| 9 | OK | Matches §401(a). |
| 10, 11, 11b, 12 | OK | These are now framed as possibilities or as "under the 2002 law". The funding condition matches §109(c)(2). The §806 scope (public companies, named channels) is correct. |
| 13, 14a, 14b | OK | Attributions and "on average" now match C-020, C-036 and S-026. |
| 15-18 (diagram) | OK | All four fixes appear in the visible text and the description of both the wide and narrow SVGs. Checked against §§404/S-050, 806(b)(1)(B), 202 (10A(i)(1)(B)) and 802 (18 U.S.C. 1519, 1520). |
| 19 | OK | Caption fixed. |

### Required fixes

**Item 4 (cooling-off, §206).** The applied sentence was my own suggested wording. Checked against the law, it is inaccurate:
- §206 bars the firm from performing an audit if one of these officers "was employed by that registered independent public accounting firm and participated in any capacity in the audit of that issuer during the 1-year period preceding the date of the initiation of the audit" (sox-plaw-html lines 1898-1906).
- "May not keep auditing that company" suggests a permanent bar. The bar actually lasts only until more than a year separates the person's audit work from the start of the next audit.
- "Within a year" attaches the one-year window to the hiring. The law attaches it to the person's audit work.

Replace:
> Under the 2002 law, if someone who worked on the audit becomes the company's CEO, CFO, controller or chief accounting officer within a year, the firm may not keep auditing that company.

with:
> Under the 2002 law, if someone from the audit firm who worked on a company's audit becomes that company's CEO, CFO, controller or chief accounting officer, the firm may not audit the company again until more than a year has passed since that person last worked on its audit.

**Item 5 (citation label).** In `reform-src/why-it-matters.src.html`, replace `{{B-016@p. 50, Board oversight of Lay's credit line#54}}` with `{{B-016@p. 50, Finding (5), Excessive Compensation#54}}`, then rebuild.

### Overall

- **`why-it-matters.html`: PASS once the two fixes above are applied.** Nothing else is outstanding. A re-check needs only those two sentences.
- **`diagram-sox-map.svg` / `-narrow.svg`: PASS.**

## Revision 2

This section checks the revision-2 update to "Why This Matters to You", against `work/facts/fixes-revision2-reform.md` and the current source.
- I read every changed or added sentence against its T-card, and against the source where the card was not enough: 33-8238 lines 24, 316-330; GAO-06-361 PDF 11 and 32; GAO-08-163 PDF 19; *Free Enterprise Fund* PDF 1, 5, 6, 16, 32-33 (Part IV heading at line 1375); 15 U.S.C. 78u-6 lines 14, 32-34.
- Rebuilding the page from its source reproduces `why-it-matters.html` exactly: 104 citations to 95 cards, all checked OK or FIXED. The new citations with an override source or locator resolve to the right file and PDF page: T-008 to gao-06-361 PDF 32; T-022 to gao-08-163 PDF 19; T-039 to PDF 1; T-040 to PDF 6; T-041 to PDF 16; T-042 to PDF 32 (opinion) and PDF 5 (Syllabus).
- As instructed, I ignored the four new glossary terms.
- The two earlier Final fixes have now been applied: the cooling-off sentence and the B-016 label (item 5 in the Final section). Both re-check OK and are logged as corrections rows 196-197.

### How the page follows the revision-2 rulings

| Ruling | Verdict |
|---|---|
| 404 compliance dates | **OK.** The page says the 2003 rule "first set" June 15, 2004, that the SEC "moved the dates" in February 2004 to November 15, 2004 and July 15, 2005 (GAO-06-361 p. 27), and that more extensions followed by spring 2006. |
| Syllabus and opinion labels | **OK.** The facts behind the suit and the 5-4 line-up are labeled "According to the Syllabus" and cited to the Syllabus pages. The holding is quoted from the opinion (p. 492, Part III). Removal at will and the Board's validity are cited to the opinion, pp. 508-509, Part IV. "Continue to function as before" is given "In the Syllabus's words". The Syllabus is also explained correctly. |
| Proposals kept as proposals | **OK.** The page says "if adopted by the SEC ... in 2006 these were proposals, not law." |
| "10 to 30 percent, in total" | **OK.** It includes "voluntarily" and "sanctions over $1 million". |
| "Nine categories" wording | **OK.** The page says: "its 2003 rule release counts the Act's list, including the catch-all, as 'nine categories'", next to the 704 report's "eight". The main sentence keeps "eight named ... plus any other service the PCAOB bans by rule". |
| Nothing about the orders' contents | **OK.** Nothing on the page describes what the April 2003 orders contained or names SSAE No. 10. |

The quotes are verbatim: T-022, T-023, T-026, T-041, the T-042 Syllabus quote, T-046 and T-053. AS 2201 is presented as the "current version" of AS No. 5, as ruled.

### Findings

| # | Location | Problem | Source | Required fix | Severity |
|---|---|---|---|---|---|
| R2-1 | `#s302` "What it means for you": "Under the SEC's 2002 rule, those executives also certify that they have evaluated the company's disclosure controls and procedures within 90 days before filing.{{T-004}}" | Out of date in a "for you" paragraph. The SEC's June 2003 rule changed the evaluation date for disclosure controls to "as of the end of the period" covered by the report. The 90-day window no longer applied after 2003. | sec-33-8238 III, "Final Disclosure Requirements", line 330: "We are adopting as proposed the change of the evaluation date for disclosure controls to 'as of the end of the period' covered by the quarterly or annual report." | Replace with: "Under the SEC's rules, those executives also certify that they have evaluated the company's <span class="term" data-term="disclosure-controls">disclosure controls and procedures</span>.{{T-004}}" If the writer wants to mention the timing, Reader D must first make a card for 33-8238 line 330; don't cite T-004 for it. | medium |
| R2-2 | `#s404` "What it means for you": "Since 2010, companies that are not accelerated filers no longer need the auditor's attestation{{T-026}}" | Can be misread. In SEC terms a "large accelerated filer" is a separate category from an "accelerated filer" (T-050), so "not accelerated filers" could seem to include the largest companies. The statute says "neither a 'large accelerated filer' nor an 'accelerated filer'". The sentence also leaves out the 2012 emerging-growth-company exemption. | usc-15-7262-2024 (c), line 19; (b), line 17 | Write: "Since 2010, companies that are neither accelerated filers nor large accelerated filers no longer need the auditor's attestation, and since 2012 neither do emerging growth companies,{{T-026}}{{T-027}} but management's own report is still required." | medium |
| R2-3 | `#independence` "What it means for you": "other audit partners rotate after seven years with a two-year break,{{T-031}}" | Slightly broader than the rule. It covers only "partners subject to the rotation requirements", who rotate "after no more than seven years". | sec-33-8183 line 370 | Write: "other audit partners covered by the rule rotate after no more than seven years, with a two-year break," | low |

### Notes (no fix required)

- **The `accelerated-filer` glossary entry** (which replaces the removed T-050 sentence): it must present the $75 million / $700 million public-float thresholds as the SEC's December 2005 definitions as GAO described them (T-050), not as today's rule.
- **"By spring 2006, GAO reported, the SEC had extended the smaller companies' deadline several more times"** is supported by GAO-06-361 p. 6 ("subsequently extended the deadline several times, with the latest extension to July 15, 2007"). GAO is describing SEC actions here, so "reported" is acceptable.
- **`#pcaob` "for you":** dropping the "under the 2002 law" hedge is acceptable now. The *Free Enterprise Fund* opinion (pp. 508-509) confirms the Board continues to operate, and the sentence says only that work "could be inspected".

### Verdict (Revision 2)

**`why-it-matters.html`: PASS once R2-1 and R2-2 are fixed (medium). R2-3 is a low fix.** Nothing else is outstanding. A re-check needs only those three sentences.
