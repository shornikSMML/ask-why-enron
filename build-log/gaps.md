# Gaps: sources the library does not have

Agents record here any claim they wanted to make but could not support from the library. They do **not** search for the source themselves. The Source Scout works through this list, critical gaps first. Candidates the Scout finds go to `sources/candidates/` and may not be cited until the project owner approves them.

Importance: **critical** (a core part of the story is missing or unverified without it), **useful** (would improve accuracy or detail), **minor** (nice to have).

The coordinator merged the agents' own gap files (`work/facts/*-gaps.md`, which give the full wording) into this list after Wave 1 and removed duplicates. "Raised by" names every agent that raised the gap.

## Critical

| # | Claim we wanted to make | Kind of document that would support it | Raised by | Status |
|---|---|---|---|---|
| 1 | Fastow's criminal case: what he pleaded guilty to, when, and his sentence. The library shows only DOJ listing him as "convicted to date" (2004). | DOJ plea agreement or press releases on the plea and sentencing, U.S. v. Fastow (S.D. Tex.) | Reader A, Reader B | candidate: doj-fastow-plea-press-2004; candidate: doj-fastow-sentenced-press-2006. Plea agreement/judgment: paywalled: PACER |
| 2 | Glisan's criminal case: charge, plea, sentence. The library shows only "convicted to date." | DOJ plea agreement, judgment, or press release, U.S. v. Glisan | Reader B | candidate: doj-glisan-plea-press-2003 |
| 3 | David Duncan's criminal case (the library shows only the SEC complaint and his Fifth Amendment invocation) | DOJ information, plea, and later court orders, U.S. v. Duncan (S.D. Tex.); DOJ press release | Reader B, Reader C | partial. candidate: sec-duncan-litrel-20441 (SEC civil case only). Criminal side: no DOJ press release found in DOJ's April 2002 index; court record paywalled: PACER (S.D. Tex.) |
| 4 | Skilling's case after the 2010 Supreme Court remand (harmless-error ruling, resentencing) | Fifth Circuit opinion on remand (2011); district court resentencing; DOJ press release | Reader B | candidate: ca5-skilling-2011-remand; candidate: doj-skilling-sentencing-agreement-2013 (agreement, not the judgment). DOJ 2013 resentencing press release located but justice.gov served a bot-check page; not downloaded (owner can save it from a browser). Resentencing judgment: paywalled: PACER |
| 5 | Andersen's 2002 obstruction indictment and verdict from primary documents, and what happened after the 2005 reversal | DOJ press releases; verdict or judgment, U.S. v. Arthur Andersen LLP (S.D. Tex., No. H-02-121); DOJ statement after remand | Reader B, Reader C (also in sources/README "Still to find") | partial. candidate: doj-andersen-indictment-2002; candidate: andersen-scotus-full-usreports (the reversal). DOJ verdict statement (justice.gov/archive/opa/pr/2002/June/02_dag_356.htm) located but the server refused it (HTTP 401) on 3 tries. Verdict/judgment and the Nov 2005 government motion not to retry: paywalled: PACER; no official DOJ release found. Round 3: candidate: doj-dag-statement-andersen-sentence-2002-10-16 (sentencing) |

## Useful

| # | Claim we wanted to make | Kind of document that would support it | Raised by | Status |
|---|---|---|---|---|
| 6 | Kopper's plea (currently seen only second-hand) and sentence | DOJ press releases or plea agreement, U.S. v. Kopper (2002) | Reader A, Reader B | partial. candidate: doj-dag-kopper-plea-transcript-2002 (plea only; sentence not searched (10-candidate limit reached)). Round 3: sentencing release not found in DOJ national archive indexes Aug 2006–Mar 2007 |
| 7 | Causey's sentence after his Dec 28, 2005 plea | DOJ press release or judgment | Reader B | candidate: doj-causey-sentenced-press-2006 |
| 8 | Lay's conviction vacated after his death: the order itself (the library has the Fifth Circuit's statement, which is enough for the site) | U.S. v. Lay, 456 F. Supp. 2d 869 (S.D. Tex. 2006) | Reader B | not searched (10-candidate limit reached) |
| 9 | Full Supreme Court opinion in *Arthur Andersen LLP v. United States* (the library copy is only the Syllabus) | Official opinion, supremecourt.gov or U.S. Reports via loc.gov | Coordinator, Reader C | candidate: andersen-scotus-full-usreports |
| 10 | Why Dynegy ended the merger (Nov 28, 2001), in a primary filing | Enron or Dynegy 8-K of late Nov 2001; Enron's Dec 2001 complaint against Dynegy | Reader A | Round 3: sec.gov (EDGAR) refused requests (403, "undeclared automated tool"); not retrieved |
| 11 | Enron's Oct 16, 2001 earnings press release (the $618M loss and $1.01B charges; reconciling the $544M vs. $462M after-tax figures) | The press release as filed with the SEC (8-K exhibit), if any | Reader A | Round 3: not attempted; sec.gov refused requests |
| 12 | How the SEC civil cases ended (Lay, Skilling, Causey, Fastow, Duncan, Merrill executives) | SEC litigation releases (e.g. 18543, 19996, 20441, 21523) | Reader B | partial (Duncan only): candidate: sec-duncan-litrel-20441. Others not searched (10-candidate limit reached). Round 3: Merrill Lynch release (lr18038, unverified number) refused by sec.gov (403); not retrieved |
| 13 | Names and outcomes of the Merrill Lynch employees in the Nigerian barge case (convicted, then reversed, per the Fifth Circuit) | U.S. v. Brown, 459 F.3d 509 (5th Cir. 2006) | Reader B | candidate: ca5-us-v-brown-2006 (round 3) |
| 14 | Whether any outside director was charged or sued (the library shows none, but no document says "not charged") | DOJ or SEC statement; court record of the securities litigation | Reader B | not searched (10-candidate limit reached) |
| 15 | Text of Sherron Watkins's August 2001 letter to Lay | The letter as a hearing exhibit (first check whether any library hearing already prints it) | Reader B | not searched (10-candidate limit reached) |
| 16 | Outcome of the Labor Department's 401(k) investigation; official lockdown dates (the sources disagree) | DOL press release; plan notice; court finding in the ERISA litigation | Reader C | Round 3: dol.gov refused the request (403 "Access Denied"); not retrieved |
| 17 | Batson Second Interim Report and appendices (D, E, G, L, M, Q): the six accounting techniques, SPE and related-party disclosure analysis | The report itself. **Known gap: do not search** (owner) | Reader A, Reader C, Footnote | not searched (per owner) |
| 18 | Batson Third Interim Report, App. C (officers) | The report itself. **Known gap: do not search** (owner) | Reader A, Reader B | not searched (per owner) |

## Minor

| # | Claim we wanted to make | Kind of document that would support it | Raised by | Status |
|---|---|---|---|---|
| 19 | Exact merger terms in the Nov 9, 2001 Dynegy 8-K exhibits (the library copy is the cover filing only) | Exhibits 99.1–99.13 to that 8-K (sec.gov) | Reader A | not searched (10-candidate limit reached) |
| 20 | How many documents Andersen destroyed | Trial record or DOJ document | Reader C | not searched (10-candidate limit reached) |
| 21 | The PCAOB's fifth founding board member | SEC or PCAOB release, 2002–03 | Reader C | not searched (10-candidate limit reached) |
| 22 | Whether Watkins, Berardino, or McMahon faced legal action (McMahon: SEC charged 2007, outcome unknown) | SEC litigation release 20159 and later | Reader B | not searched (10-candidate limit reached) |
| 23 | The Fortune 500 2001 list itself. Probably not needed: Batson and the JCT report already support the ranking, and the magazine is copyrighted | Not recommended | Reader A | not needed |

## Reader tips
| Tip | Status |
|---|---|
| Warren Buffett read Enron's footnote, did not understand it, and threw away the 10-K | **Excluded** by the Fact-Checker: 7 library documents mention Buffett, none about Enron's footnote or 10-K. See gap 25. |
| At its peak, Enron was America's seventh-largest company | **Allowed, reworded**: "In 2001, Fortune magazine ranked Enron seventh on its list of the 500 largest U.S. companies, measured by revenue." (JCT p. 58; Batson Final n. 27). Not "at its peak" (JCT n. 53: fifth on the 2002 list), not "in the world." |

## Added after Fact-Checker Round 1

| # | Claim we wanted to make | Kind of document that would support it | Importance | Raised by | Status |
|---|---|---|---|---|---|
| 24 | Name Andersen's CEO as the speaker quoted from the Dec 12, 2001 hearing (Powers says only "Andersen's CEO") | Transcript of the Dec 12, 2001 House Financial Services hearing (govinfo.gov) | useful | Fact-Checker | located, not downloaded (10-candidate limit reached): official govinfo copy, CHRG-107hhrg76958, https://www.govinfo.gov/content/pkg/CHRG-107hhrg76958/pdf/CHRG-107hhrg76958.pdf. Not in manifest. |
| 25 | Buffett reader tip: that he read Enron's footnote, didn't understand it, and discarded the 10-K. Ruled **excluded**: 7 library documents mention Buffett, none on this subject | A first-hand record: Buffett's own sworn testimony or a Berkshire shareholder letter | minor | Fact-Checker | excluded from site; open |
| 26 | Why the Kopper complaint gives Dec 3, 2001 for the bankruptcy when other sources say Dec 2 | Bankruptcy docket / petition (likely PACER) | minor | Fact-Checker | not searched (10-candidate limit reached) |
| 27 | Board minutes approving LJM2 (Oct 11 vs. Oct 12, 1999) | Enron board minutes (hearing exhibit) | minor | Fact-Checker | not searched (10-candidate limit reached) |
| 28 | Ratio of Enron's 1999 stock split (explains 6.8M vs. 3.4M Rhythms shares) | Enron 10-K for 1999 or an 8-K (sec.gov) | minor | Fact-Checker | not searched (10-candidate limit reached) |

## Added during the revision pass

| # | Claim we wanted to make | Kind of document that would support it | Importance | Raised by | Status |
|---|---|---|---|---|---|
| 29 | What later happened to David Duncan's 2002 guilty plea (the library shows the plea but not its date, any sentence, or any later development). The Fact-Checker notes, from memory only, that the plea may have been withdrawn after the 2005 reversal of Andersen's conviction. This must not appear on the site without a source. | Court order or DOJ statement in U.S. v. Duncan (S.D. Tex.); likely PACER | critical | Fact-Checker | open |
| 30 | Kopper's sentence | DOJ press release or judgment, U.S. v. Kopper | useful | Reader B | open. Round 3: not found in DOJ national archive indexes Sept–Nov 2006 (also Aug 2006, Dec 2006–Mar 2007); may exist only as a U.S. Attorney release |
| 31 | The sentence actually imposed on Skilling after the 2013 agreement | Judgment or DOJ press release (2013) | useful | Reader B | open (DOJ page blocked by a bot check; owner may save it from a browser) |

## Phase 2 (post-2003)

Raised by the coordinator's Phase 2 brief to the Source Scout (for "Why This Matters to You"). Candidates are in `sources/candidates/phase2/` and may not be cited until the owner approves them.

| # | Claim we wanted to make | Kind of document that would support it | Importance | Raised by | Status |
|---|---|---|---|---|---|
| P2-1 | What auditors must do when auditing a company's internal control over financial reporting (current rules) | PCAOB Auditing Standard No. 5 (2007) or its current codified version, AS 2201 | useful | Coordinator (Phase 2 brief) | candidate: pcaob-as2201-current (current version; 2007 original release located, not downloaded) |
| P2-2 | What management's internal control report (SOX §404) must contain, per the SEC's 2003 rule | SEC final rule Rel. 33-8238 (2003) | useful | Coordinator (Phase 2 brief) | candidate: sec-33-8238-icfr-final-rule |
| P2-3 | What CEOs and CFOs must certify (SOX §302), per the SEC's 2002 rule | SEC final rule Rel. 33-8124 (2002) | useful | Coordinator (Phase 2 brief) | candidate: sec-33-8124-certification-final-rule |
| P2-4 | The SEC's 2007 guidance to management on evaluating internal control | SEC interpretive release Rel. 33-8810 (2007) | useful | Coordinator (Phase 2 brief) | candidate: sec-33-8810-icfr-guidance-2007 |
| P2-5 | The SEC's 2003 auditor independence rules implementing SOX Title II | SEC final rule Rel. 33-8183 (2003) | useful | Coordinator (Phase 2 brief) | candidate: sec-33-8183-auditor-independence (a published correction exists; not downloaded) |
| P2-6 | Effects of SOX on smaller companies and on audit-market concentration after 2003 | GAO reports (e.g. GAO-06-361, GAO-08-163) | useful | Coordinator (Phase 2 brief) | candidate: gao-06-361; candidate: gao-08-163 |
| P2-7 | The Supreme Court's 2010 ruling on the PCAOB's constitutionality | *Free Enterprise Fund v. PCAOB*, 561 U.S. 477 (2010) | useful | Coordinator (Phase 2 brief) | candidate: free-enterprise-fund-v-pcaob-usreports (govinfo U.S. Reports; supremecourt.gov slip-opinion URL returned 404) |
| P2-8 | The Dodd-Frank whistleblower program (§§922–924) and the §404(b) exemption for small companies, section text | Dodd-Frank Act (Pub. L. 111-203) section text, or the U.S. Code sections it created/amended | minor | Coordinator (Phase 2 brief) | partial. candidate: usc-15-78u-6-2024 (§922 as codified); candidate: usc-15-7262-2024 (§404 as amended, incl. the exemption). §§923–924 not collected (10-candidate limit reached); Act's own session-law text not downloaded (whole Act only) |

## Round 3 (documents identified by the owner)

Targets supplied by the coordinator's round 3 brief. Candidates are in `sources/candidates/round3/` and may not be cited until the owner approves them.

| # | Claim we wanted to make | Kind of document that would support it | Importance | Raised by | Status |
|---|---|---|---|---|---|
| R3-1 | Lea Fastow's case: what happened to her plea agreement (April 2004) and her sentence (May 2004) | DOJ press releases | useful | Coordinator (round 3 brief) | candidate: doj-lea-fastow-statement-2004-04-07; candidate: doj-lea-fastow-sentenced-2004-05-06 |
| R3-2 | The three former NatWest bankers' case: plea and sentence | DOJ press releases (Nov 2007 plea; Feb 2008 sentencing) | useful | Coordinator (round 3 brief) | candidate: doj-british-bankers-sentenced-2008-02-22 (Nov 2007 plea release located, not downloaded) |
| R3-3 | DOJ's agreements with Merrill Lynch (Sept 2003) and CIBC (Dec 2003) | DOJ press releases or the agreements | useful | Coordinator (round 3 brief) | candidate: doj-merrill-executives-charged-2003-09-17; candidate: doj-cibc-agreement-2003-12-22 |
| R3-4 | Labor Department settlement with Enron's outside directors and others, *Chao v. Enron Corp.* (May 2004); 401(k) settlement proceeds (Feb 2006) | DOL press releases | useful | Coordinator (round 3 brief) | dol.gov refused the request (403 "Access Denied"); not retrieved, not retried. Owner may save it from a browser |
| R3-5 | SEC settlements with Merrill Lynch (2003) and CIBC (Dec 2003) | SEC litigation or press releases | useful | Coordinator (round 3 brief) | sec.gov refused requests (403 "Request Rate Threshold Exceeded", then "Undeclared Automated Tool"); not retrieved, not retried |
| R3-6 | Why Dynegy ended the merger (Nov 28, 2001) | Dynegy 8-K or press release (EDGAR) | useful | Coordinator (round 3 brief) | sec.gov refused requests; not retrieved (see gap 10) |
| R3-7 | Mark Koenig's sentence | DOJ press release | minor | Coordinator (round 3 brief, substitute) | not found in DOJ national archive indexes checked (Aug 2006–Mar 2007) |

