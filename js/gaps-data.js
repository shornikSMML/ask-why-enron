// Generated from build-log/gaps.md and sources/candidates/candidates.csv by work/tools/gaps_to_js.py. Do not edit.
window.GAPS = {
 "intro": [
  "Agents record here any claim they wanted to make but could not support from the library. They do **not** search for the source themselves. The Source Scout works through this list, critical gaps first. Candidates the Scout finds go to `sources/candidates/` and may not be cited until the project owner approves them.",
  "Importance: **critical** (a core part of the story is missing or unverified without it), **useful** (would improve accuracy or detail), **minor** (nice to have).",
  "The coordinator merged the agents' own gap files (`work/facts/*-gaps.md`, which give the full wording) into this list after Wave 1 and removed duplicates. \"Raised by\" names every agent that raised the gap."
 ],
 "sections": [
  {
   "title": "Critical",
   "intro": [],
   "columns": [
    "#",
    "Claim we wanted to make",
    "Kind of document that would support it",
    "Raised by",
    "Status"
   ],
   "rows": [
    {
     "#": "1",
     "Claim we wanted to make": "Fastow's criminal case: what he pleaded guilty to, when, and his sentence. The library shows only DOJ listing him as \"convicted to date\" (2004).",
     "Kind of document that would support it": "DOJ plea agreement or press releases on the plea and sentencing, U.S. v. Fastow (S.D. Tex.)",
     "Raised by": "Reader A, Reader B",
     "Status": "candidate: doj-fastow-plea-press-2004; candidate: doj-fastow-sentenced-press-2006. Plea agreement/judgment: paywalled: PACER"
    },
    {
     "#": "2",
     "Claim we wanted to make": "Glisan's criminal case: charge, plea, sentence. The library shows only \"convicted to date.\"",
     "Kind of document that would support it": "DOJ plea agreement, judgment, or press release, U.S. v. Glisan",
     "Raised by": "Reader B",
     "Status": "candidate: doj-glisan-plea-press-2003"
    },
    {
     "#": "3",
     "Claim we wanted to make": "David Duncan's criminal case (the library shows only the SEC complaint and his Fifth Amendment invocation)",
     "Kind of document that would support it": "DOJ information, plea, and later court orders, U.S. v. Duncan (S.D. Tex.); DOJ press release",
     "Raised by": "Reader B, Reader C",
     "Status": "partial. candidate: sec-duncan-litrel-20441 (SEC civil case only). Criminal side: no DOJ press release found in DOJ's April 2002 index; court record paywalled: PACER (S.D. Tex.)"
    },
    {
     "#": "4",
     "Claim we wanted to make": "Skilling's case after the 2010 Supreme Court remand (harmless-error ruling, resentencing)",
     "Kind of document that would support it": "Fifth Circuit opinion on remand (2011); district court resentencing; DOJ press release",
     "Raised by": "Reader B",
     "Status": "candidate: ca5-skilling-2011-remand; candidate: doj-skilling-sentencing-agreement-2013 (agreement, not the judgment). DOJ 2013 resentencing press release located but justice.gov served a bot-check page; not downloaded (owner can save it from a browser). Resentencing judgment: paywalled: PACER"
    },
    {
     "#": "5",
     "Claim we wanted to make": "Andersen's 2002 obstruction indictment and verdict from primary documents, and what happened after the 2005 reversal",
     "Kind of document that would support it": "DOJ press releases; verdict or judgment, U.S. v. Arthur Andersen LLP (S.D. Tex., No. H-02-121); DOJ statement after remand",
     "Raised by": "Reader B, Reader C (also in sources/README \"Still to find\")",
     "Status": "partial. candidate: doj-andersen-indictment-2002; candidate: andersen-scotus-full-usreports (the reversal). DOJ verdict statement (justice.gov/archive/opa/pr/2002/June/02_dag_356.htm) located but the server refused it (HTTP 401) on 3 tries. Verdict/judgment and the Nov 2005 government motion not to retry: paywalled: PACER; no official DOJ release found"
    }
   ]
  },
  {
   "title": "Useful",
   "intro": [],
   "columns": [
    "#",
    "Claim we wanted to make",
    "Kind of document that would support it",
    "Raised by",
    "Status"
   ],
   "rows": [
    {
     "#": "6",
     "Claim we wanted to make": "Kopper's plea (currently seen only second-hand) and sentence",
     "Kind of document that would support it": "DOJ press releases or plea agreement, U.S. v. Kopper (2002)",
     "Raised by": "Reader A, Reader B",
     "Status": "partial. candidate: doj-dag-kopper-plea-transcript-2002 (plea only; sentence not searched (10-candidate limit reached))"
    },
    {
     "#": "7",
     "Claim we wanted to make": "Causey's sentence after his Dec 28, 2005 plea",
     "Kind of document that would support it": "DOJ press release or judgment",
     "Raised by": "Reader B",
     "Status": "candidate: doj-causey-sentenced-press-2006"
    },
    {
     "#": "8",
     "Claim we wanted to make": "Lay's conviction vacated after his death: the order itself (the library has the Fifth Circuit's statement, which is enough for the site)",
     "Kind of document that would support it": "U.S. v. Lay, 456 F. Supp. 2d 869 (S.D. Tex. 2006)",
     "Raised by": "Reader B",
     "Status": "not searched (10-candidate limit reached)"
    },
    {
     "#": "9",
     "Claim we wanted to make": "Full Supreme Court opinion in *Arthur Andersen LLP v. United States* (the library copy is only the Syllabus)",
     "Kind of document that would support it": "Official opinion, supremecourt.gov or U.S. Reports via loc.gov",
     "Raised by": "Coordinator, Reader C",
     "Status": "candidate: andersen-scotus-full-usreports"
    },
    {
     "#": "10",
     "Claim we wanted to make": "Why Dynegy ended the merger (Nov 28, 2001), in a primary filing",
     "Kind of document that would support it": "Enron or Dynegy 8-K of late Nov 2001; Enron's Dec 2001 complaint against Dynegy",
     "Raised by": "Reader A",
     "Status": "not searched (10-candidate limit reached)"
    },
    {
     "#": "11",
     "Claim we wanted to make": "Enron's Oct 16, 2001 earnings press release (the $618M loss and $1.01B charges; reconciling the $544M vs. $462M after-tax figures)",
     "Kind of document that would support it": "The press release as filed with the SEC (8-K exhibit), if any",
     "Raised by": "Reader A",
     "Status": "not searched (10-candidate limit reached)"
    },
    {
     "#": "12",
     "Claim we wanted to make": "How the SEC civil cases ended (Lay, Skilling, Causey, Fastow, Duncan, Merrill executives)",
     "Kind of document that would support it": "SEC litigation releases (e.g. 18543, 19996, 20441, 21523)",
     "Raised by": "Reader B",
     "Status": "partial (Duncan only): candidate: sec-duncan-litrel-20441. Others not searched (10-candidate limit reached)"
    },
    {
     "#": "13",
     "Claim we wanted to make": "Names and outcomes of the Merrill Lynch employees in the Nigerian barge case (convicted, then reversed, per the Fifth Circuit)",
     "Kind of document that would support it": "U.S. v. Brown, 459 F.3d 509 (5th Cir. 2006)",
     "Raised by": "Reader B",
     "Status": "not searched (10-candidate limit reached)"
    },
    {
     "#": "14",
     "Claim we wanted to make": "Whether any outside director was charged or sued (the library shows none, but no document says \"not charged\")",
     "Kind of document that would support it": "DOJ or SEC statement; court record of the securities litigation",
     "Raised by": "Reader B",
     "Status": "not searched (10-candidate limit reached)"
    },
    {
     "#": "15",
     "Claim we wanted to make": "Text of Sherron Watkins's August 2001 letter to Lay",
     "Kind of document that would support it": "The letter as a hearing exhibit (first check whether any library hearing already prints it)",
     "Raised by": "Reader B",
     "Status": "not searched (10-candidate limit reached)"
    },
    {
     "#": "16",
     "Claim we wanted to make": "Outcome of the Labor Department's 401(k) investigation; official lockdown dates (the sources disagree)",
     "Kind of document that would support it": "DOL press release; plan notice; court finding in the ERISA litigation",
     "Raised by": "Reader C",
     "Status": "not searched (10-candidate limit reached)"
    },
    {
     "#": "17",
     "Claim we wanted to make": "Batson Second Interim Report and appendices (D, E, G, L, M, Q): the six accounting techniques, SPE and related-party disclosure analysis",
     "Kind of document that would support it": "The report itself. **Known gap: do not search** (owner)",
     "Raised by": "Reader A, Reader C, Footnote",
     "Status": "not searched (per owner)"
    },
    {
     "#": "18",
     "Claim we wanted to make": "Batson Third Interim Report, App. C (officers)",
     "Kind of document that would support it": "The report itself. **Known gap: do not search** (owner)",
     "Raised by": "Reader A, Reader B",
     "Status": "not searched (per owner)"
    }
   ]
  },
  {
   "title": "Minor",
   "intro": [],
   "columns": [
    "#",
    "Claim we wanted to make",
    "Kind of document that would support it",
    "Raised by",
    "Status"
   ],
   "rows": [
    {
     "#": "19",
     "Claim we wanted to make": "Exact merger terms in the Nov 9, 2001 Dynegy 8-K exhibits (the library copy is the cover filing only)",
     "Kind of document that would support it": "Exhibits 99.1–99.13 to that 8-K (sec.gov)",
     "Raised by": "Reader A",
     "Status": "not searched (10-candidate limit reached)"
    },
    {
     "#": "20",
     "Claim we wanted to make": "How many documents Andersen destroyed",
     "Kind of document that would support it": "Trial record or DOJ document",
     "Raised by": "Reader C",
     "Status": "not searched (10-candidate limit reached)"
    },
    {
     "#": "21",
     "Claim we wanted to make": "The PCAOB's fifth founding board member",
     "Kind of document that would support it": "SEC or PCAOB release, 2002–03",
     "Raised by": "Reader C",
     "Status": "not searched (10-candidate limit reached)"
    },
    {
     "#": "22",
     "Claim we wanted to make": "Whether Watkins, Berardino, or McMahon faced legal action (McMahon: SEC charged 2007, outcome unknown)",
     "Kind of document that would support it": "SEC litigation release 20159 and later",
     "Raised by": "Reader B",
     "Status": "not searched (10-candidate limit reached)"
    },
    {
     "#": "23",
     "Claim we wanted to make": "The Fortune 500 2001 list itself. Probably not needed: Batson and the JCT report already support the ranking, and the magazine is copyrighted",
     "Kind of document that would support it": "Not recommended",
     "Raised by": "Reader A",
     "Status": "not needed"
    }
   ]
  },
  {
   "title": "Reader tips",
   "intro": [],
   "columns": [
    "Tip",
    "Status"
   ],
   "rows": [
    {
     "Tip": "Warren Buffett read Enron's footnote, did not understand it, and threw away the 10-K",
     "Status": "**Excluded** by the Fact-Checker: 7 library documents mention Buffett, none about Enron's footnote or 10-K. See gap 25."
    },
    {
     "Tip": "At its peak, Enron was America's seventh-largest company",
     "Status": "**Allowed, reworded**: \"In 2001, Fortune magazine ranked Enron seventh on its list of the 500 largest U.S. companies, measured by revenue.\" (JCT p. 58; Batson Final n. 27). Not \"at its peak\" (JCT n. 53: fifth on the 2002 list), not \"in the world.\""
    }
   ]
  },
  {
   "title": "Added after Fact-Checker Round 1",
   "intro": [],
   "columns": [
    "#",
    "Claim we wanted to make",
    "Kind of document that would support it",
    "Importance",
    "Raised by",
    "Status"
   ],
   "rows": [
    {
     "#": "24",
     "Claim we wanted to make": "Name Andersen's CEO as the speaker quoted from the Dec 12, 2001 hearing (Powers says only \"Andersen's CEO\")",
     "Kind of document that would support it": "Transcript of the Dec 12, 2001 House Financial Services hearing (govinfo.gov)",
     "Importance": "useful",
     "Raised by": "Fact-Checker",
     "Status": "located, not downloaded (10-candidate limit reached): official govinfo copy, CHRG-107hhrg76958, https://www.govinfo.gov/content/pkg/CHRG-107hhrg76958/pdf/CHRG-107hhrg76958.pdf. Not in manifest."
    },
    {
     "#": "25",
     "Claim we wanted to make": "Buffett reader tip: that he read Enron's footnote, didn't understand it, and discarded the 10-K. Ruled **excluded**: 7 library documents mention Buffett, none on this subject",
     "Kind of document that would support it": "A first-hand record: Buffett's own sworn testimony or a Berkshire shareholder letter",
     "Importance": "minor",
     "Raised by": "Fact-Checker",
     "Status": "excluded from site; open"
    },
    {
     "#": "26",
     "Claim we wanted to make": "Why the Kopper complaint gives Dec 3, 2001 for the bankruptcy when other sources say Dec 2",
     "Kind of document that would support it": "Bankruptcy docket / petition (likely PACER)",
     "Importance": "minor",
     "Raised by": "Fact-Checker",
     "Status": "not searched (10-candidate limit reached)"
    },
    {
     "#": "27",
     "Claim we wanted to make": "Board minutes approving LJM2 (Oct 11 vs. Oct 12, 1999)",
     "Kind of document that would support it": "Enron board minutes (hearing exhibit)",
     "Importance": "minor",
     "Raised by": "Fact-Checker",
     "Status": "not searched (10-candidate limit reached)"
    },
    {
     "#": "28",
     "Claim we wanted to make": "Ratio of Enron's 1999 stock split (explains 6.8M vs. 3.4M Rhythms shares)",
     "Kind of document that would support it": "Enron 10-K for 1999 or an 8-K (sec.gov)",
     "Importance": "minor",
     "Raised by": "Fact-Checker",
     "Status": "not searched (10-candidate limit reached)"
    }
   ]
  },
  {
   "title": "Added during the revision pass",
   "intro": [],
   "columns": [
    "#",
    "Claim we wanted to make",
    "Kind of document that would support it",
    "Importance",
    "Raised by",
    "Status"
   ],
   "rows": [
    {
     "#": "29",
     "Claim we wanted to make": "What later happened to David Duncan's 2002 guilty plea (the library shows the plea but not its date, any sentence, or any later development). The Fact-Checker notes, from memory only, that the plea may have been withdrawn after the 2005 reversal of Andersen's conviction. This must not appear on the site without a source.",
     "Kind of document that would support it": "Court order or DOJ statement in U.S. v. Duncan (S.D. Tex.); likely PACER",
     "Importance": "critical",
     "Raised by": "Fact-Checker",
     "Status": "open"
    },
    {
     "#": "30",
     "Claim we wanted to make": "Kopper's sentence",
     "Kind of document that would support it": "DOJ press release or judgment, U.S. v. Kopper",
     "Importance": "useful",
     "Raised by": "Reader B",
     "Status": "open"
    },
    {
     "#": "31",
     "Claim we wanted to make": "The sentence actually imposed on Skilling after the 2013 agreement",
     "Kind of document that would support it": "Judgment or DOJ press release (2013)",
     "Importance": "useful",
     "Raised by": "Reader B",
     "Status": "open (DOJ page blocked by a bot check; owner may save it from a browser)"
    }
   ]
  },
  {
   "title": "Phase 2 (post-2003)",
   "intro": [
    "Raised by the coordinator's Phase 2 brief to the Source Scout (for \"Why This Matters to You\"). Candidates are in `sources/candidates/phase2/` and may not be cited until the owner approves them."
   ],
   "columns": [
    "#",
    "Claim we wanted to make",
    "Kind of document that would support it",
    "Importance",
    "Raised by",
    "Status"
   ],
   "rows": [
    {
     "#": "P2-1",
     "Claim we wanted to make": "What auditors must do when auditing a company's internal control over financial reporting (current rules)",
     "Kind of document that would support it": "PCAOB Auditing Standard No. 5 (2007) or its current codified version, AS 2201",
     "Importance": "useful",
     "Raised by": "Coordinator (Phase 2 brief)",
     "Status": "candidate: pcaob-as2201-current (current version; 2007 original release located, not downloaded)"
    },
    {
     "#": "P2-2",
     "Claim we wanted to make": "What management's internal control report (SOX §404) must contain, per the SEC's 2003 rule",
     "Kind of document that would support it": "SEC final rule Rel. 33-8238 (2003)",
     "Importance": "useful",
     "Raised by": "Coordinator (Phase 2 brief)",
     "Status": "candidate: sec-33-8238-icfr-final-rule"
    },
    {
     "#": "P2-3",
     "Claim we wanted to make": "What CEOs and CFOs must certify (SOX §302), per the SEC's 2002 rule",
     "Kind of document that would support it": "SEC final rule Rel. 33-8124 (2002)",
     "Importance": "useful",
     "Raised by": "Coordinator (Phase 2 brief)",
     "Status": "candidate: sec-33-8124-certification-final-rule"
    },
    {
     "#": "P2-4",
     "Claim we wanted to make": "The SEC's 2007 guidance to management on evaluating internal control",
     "Kind of document that would support it": "SEC interpretive release Rel. 33-8810 (2007)",
     "Importance": "useful",
     "Raised by": "Coordinator (Phase 2 brief)",
     "Status": "candidate: sec-33-8810-icfr-guidance-2007"
    },
    {
     "#": "P2-5",
     "Claim we wanted to make": "The SEC's 2003 auditor independence rules implementing SOX Title II",
     "Kind of document that would support it": "SEC final rule Rel. 33-8183 (2003)",
     "Importance": "useful",
     "Raised by": "Coordinator (Phase 2 brief)",
     "Status": "candidate: sec-33-8183-auditor-independence (a published correction exists; not downloaded)"
    },
    {
     "#": "P2-6",
     "Claim we wanted to make": "Effects of SOX on smaller companies and on audit-market concentration after 2003",
     "Kind of document that would support it": "GAO reports (e.g. GAO-06-361, GAO-08-163)",
     "Importance": "useful",
     "Raised by": "Coordinator (Phase 2 brief)",
     "Status": "candidate: gao-06-361; candidate: gao-08-163"
    },
    {
     "#": "P2-7",
     "Claim we wanted to make": "The Supreme Court's 2010 ruling on the PCAOB's constitutionality",
     "Kind of document that would support it": "*Free Enterprise Fund v. PCAOB*, 561 U.S. 477 (2010)",
     "Importance": "useful",
     "Raised by": "Coordinator (Phase 2 brief)",
     "Status": "candidate: free-enterprise-fund-v-pcaob-usreports (govinfo U.S. Reports; supremecourt.gov slip-opinion URL returned 404)"
    },
    {
     "#": "P2-8",
     "Claim we wanted to make": "The Dodd-Frank whistleblower program (§§922–924) and the §404(b) exemption for small companies, section text",
     "Kind of document that would support it": "Dodd-Frank Act (Pub. L. 111-203) section text, or the U.S. Code sections it created/amended",
     "Importance": "minor",
     "Raised by": "Coordinator (Phase 2 brief)",
     "Status": "partial. candidate: usc-15-78u-6-2024 (§922 as codified); candidate: usc-15-7262-2024 (§404 as amended, incl. the exemption). §§923–924 not collected (10-candidate limit reached); Act's own session-law text not downloaded (whole Act only)"
    }
   ]
  }
 ],
 "candidates": [
  {
   "id": "doj-fastow-plea-press-2004",
   "date": "2004-01-14",
   "source_body": "DOJ Office of Public Affairs",
   "fills_gap": "1",
   "official_or_mirror": "official",
   "batch": "phase1",
   "in_manifest": true,
   "approved": true,
   "title": "DOJ press release #019: Former Enron CFO Andrew Fastow pleads guilty to conspiracy to commit securities and wire fraud",
   "description": "A press release from DOJ Office of Public Affairs, dated 2004-01-14",
   "scout_sha256": "db70ca7a3c254eec3cb9ffacd9f738e788725cce2e16c3dafa4c1a01a5546d5b",
   "library_sha256": "db70ca7a3c254eec3cb9ffacd9f738e788725cce2e16c3dafa4c1a01a5546d5b",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "doj-fastow-sentenced-press-2006",
   "date": "2006-09-26",
   "source_body": "DOJ Office of Public Affairs",
   "fills_gap": "1",
   "official_or_mirror": "official",
   "batch": "phase1",
   "in_manifest": true,
   "approved": true,
   "title": "DOJ press release #06-647: Former Enron CFO Andrew Fastow sentenced to six years in prison",
   "description": "A press release from DOJ Office of Public Affairs, dated 2006-09-26",
   "scout_sha256": "4ecc117dd8d35a90c0fd7e8747eb9a26135d2a103d3ff68215ee1fcaf2dc1c4d",
   "library_sha256": "4ecc117dd8d35a90c0fd7e8747eb9a26135d2a103d3ff68215ee1fcaf2dc1c4d",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "doj-glisan-plea-press-2003",
   "date": "2003-09-10",
   "source_body": "DOJ Office of Public Affairs",
   "fills_gap": "2",
   "official_or_mirror": "official",
   "batch": "phase1",
   "in_manifest": true,
   "approved": true,
   "title": "DOJ press release #492: Former Enron Treasurer Ben Glisan pleads guilty to conspiracy to commit wire and securities fraud",
   "description": "A press release from DOJ Office of Public Affairs, dated 2003-09-10",
   "scout_sha256": "4f38eff2f0e493d17dd37351563fa1c356d4e019e039ce2568677f273395bb6e",
   "library_sha256": "4f38eff2f0e493d17dd37351563fa1c356d4e019e039ce2568677f273395bb6e",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "sec-duncan-litrel-20441",
   "date": "2008-01-28",
   "source_body": "SEC",
   "fills_gap": "3 (partial: civil side only); 12; 22",
   "official_or_mirror": "official",
   "batch": "phase1",
   "in_manifest": true,
   "approved": true,
   "title": "SEC Litigation Release 20441: SEC v. David B. Duncan (settled civil action)",
   "description": "A litigation release from SEC, dated 2008-01-28",
   "scout_sha256": "f1593a027cd23ef625e8e46883fddd8ee2bf01328c50cf2f598987a0ca1056ba",
   "library_sha256": "9067d44966df886fb1fea49a92305376948cc74115bf9045d738757c9009bc85",
   "same_fingerprint": false,
   "fingerprint_note": "The two copies differ only in a randomly generated tracking script at the bottom of the web page; the text is identical."
  },
  {
   "id": "ca5-skilling-2011-remand",
   "date": "2011-04-06",
   "source_body": "U.S. Court of Appeals 5th Cir.",
   "fills_gap": "4",
   "official_or_mirror": "official",
   "batch": "phase1",
   "in_manifest": true,
   "approved": true,
   "title": "United States v. Skilling - Fifth Circuit opinion on remand from the Supreme Court (No. 06-20885)",
   "description": "A court opinion from U.S. Court of Appeals 5th Cir., dated 2011-04-06",
   "scout_sha256": "c736a8939bf10af3a3a2dcdd1345ba32092ec59b172b3f1a4bcc75d270645133",
   "library_sha256": "c736a8939bf10af3a3a2dcdd1345ba32092ec59b172b3f1a4bcc75d270645133",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "doj-skilling-sentencing-agreement-2013",
   "date": "2013-05-08",
   "source_body": "DOJ Criminal Division Fraud Section (court filing hosted on justice.gov)",
   "fills_gap": "4 (partial)",
   "official_or_mirror": "official",
   "batch": "phase1",
   "in_manifest": true,
   "approved": true,
   "title": "U.S. v. Skilling - Sentencing Agreement (Doc. 1316-1; Cr. No. 4:04-cr-25; S.D. Tex.)",
   "description": "A court filing from DOJ Criminal Division Fraud Section (court filing hosted on justice.gov), dated 2013-05-08",
   "scout_sha256": "91a823b45e9e0efdfb031d98a5946728c6b3bf7d8747cab77a8314d2636275ae",
   "library_sha256": "91a823b45e9e0efdfb031d98a5946728c6b3bf7d8747cab77a8314d2636275ae",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "doj-andersen-indictment-2002",
   "date": "2002-03-07",
   "source_body": "DOJ (Corporate Fraud Task Force archive)",
   "fills_gap": "5 (indictment part)",
   "official_or_mirror": "official",
   "batch": "phase1",
   "in_manifest": true,
   "approved": true,
   "title": "U.S. v. Arthur Andersen LLP - Indictment (S.D. Tex.; filed 3/7/02)",
   "description": "A court filing from DOJ (Corporate Fraud Task Force archive), dated 2002-03-07",
   "scout_sha256": "913af7af2613f4bafd0ea0541fa9d00d271411b548061d00c9bf6ba322d876bc",
   "library_sha256": "913af7af2613f4bafd0ea0541fa9d00d271411b548061d00c9bf6ba322d876bc",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "andersen-scotus-full-usreports",
   "date": "2005-05-31",
   "source_body": "U.S. Supreme Court (via Library of Congress)",
   "fills_gap": "9; 5 (reversal part)",
   "official_or_mirror": "official",
   "batch": "phase1",
   "in_manifest": true,
   "approved": true,
   "title": "Arthur Andersen LLP v. United States; 544 U.S. 696 (2005) - full opinion (official U.S. Reports)",
   "description": "A court opinion from U.S. Supreme Court (via Library of Congress), dated 2005-05-31",
   "scout_sha256": "f19ecad9728680c396756b5ec79c30a11048ef62c8e6ec454e0fb523c584b4de",
   "library_sha256": "f19ecad9728680c396756b5ec79c30a11048ef62c8e6ec454e0fb523c584b4de",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "doj-dag-kopper-plea-transcript-2002",
   "date": "2002-08-21 (see notes)",
   "source_body": "DOJ Office of the Deputy Attorney General",
   "fills_gap": "6 (plea only; not sentence)",
   "official_or_mirror": "official",
   "batch": "phase1",
   "in_manifest": true,
   "approved": true,
   "title": "DOJ transcript: Deputy Attorney General Larry Thompson news conference announcing Enron guilty plea (Kopper)",
   "description": "A transcript from DOJ Office of the Deputy Attorney General, dated 2002-08-21",
   "scout_sha256": "45280a2875c87e2c8d51f3bd4c2b181960074a82c33130c028438299e06e4fae",
   "library_sha256": "45280a2875c87e2c8d51f3bd4c2b181960074a82c33130c028438299e06e4fae",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "doj-causey-sentenced-press-2006",
   "date": "2006-11-15",
   "source_body": "DOJ Office of Public Affairs",
   "fills_gap": "7",
   "official_or_mirror": "official",
   "batch": "phase1",
   "in_manifest": true,
   "approved": true,
   "title": "DOJ press release #06-763: Former Enron Chief Accounting Officer Richard Causey sentenced",
   "description": "A press release from DOJ Office of Public Affairs, dated 2006-11-15",
   "scout_sha256": "d0e69a0de3dc9b9a17df0ce32cf2bc1cb7fe4e212e8b549302694596b66f7ddc",
   "library_sha256": "d0e69a0de3dc9b9a17df0ce32cf2bc1cb7fe4e212e8b549302694596b66f7ddc",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "pcaob-as2201-current",
   "date": "2007 (AS No. 5 adopted); page retrieved 2026-09-27",
   "source_body": "PCAOB",
   "fills_gap": "P2-1",
   "official_or_mirror": "official",
   "batch": "phase2",
   "in_manifest": true,
   "approved": true,
   "title": "PCAOB AS 2201: An Audit of Internal Control Over Financial Reporting That Is Integrated with An Audit of Financial Statements (current codified version of Auditing Standard No. 5)",
   "description": "An auditing standard from PCAOB, dated 2007",
   "scout_sha256": "ad87199f0105cfbda9419cb892c262aaa08933136759c4b498711dd95a4eb611",
   "library_sha256": "79efcc1ac75f4d304928eaacfb679c81b72a6543f5a7365711846bb2ee872ed3",
   "same_fingerprint": false,
   "fingerprint_note": ""
  },
  {
   "id": "sec-33-8238-icfr-final-rule",
   "date": "2003-06-05",
   "source_body": "SEC",
   "fills_gap": "P2-2",
   "official_or_mirror": "official",
   "batch": "phase2",
   "in_manifest": true,
   "approved": true,
   "title": "SEC Final Rule Rel. No. 33-8238: Management's Report on Internal Control Over Financial Reporting and Certification of Disclosure in Exchange Act Periodic Reports",
   "description": "A rule from SEC, dated 2003-06-05",
   "scout_sha256": "1f77e8ab24c59fa0e193f5b1e4670e614a9014ba98a3ef9b3369ed19876b7ba7",
   "library_sha256": "1f77e8ab24c59fa0e193f5b1e4670e614a9014ba98a3ef9b3369ed19876b7ba7",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "sec-33-8124-certification-final-rule",
   "date": "2002-08-29",
   "source_body": "SEC",
   "fills_gap": "P2-3",
   "official_or_mirror": "official",
   "batch": "phase2",
   "in_manifest": true,
   "approved": true,
   "title": "SEC Final Rule Rel. No. 33-8124: Certification of Disclosure in Companies' Quarterly and Annual Reports (SOX Sec. 302)",
   "description": "A rule from SEC, dated 2002-08-29",
   "scout_sha256": "63ab5b29638d901b30250ea5f5d5e2f959f19791ddfb0daafe9b99589f845b97",
   "library_sha256": "63ab5b29638d901b30250ea5f5d5e2f959f19791ddfb0daafe9b99589f845b97",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "sec-33-8810-icfr-guidance-2007",
   "date": "2007-06-20",
   "source_body": "SEC",
   "fills_gap": "P2-4",
   "official_or_mirror": "official",
   "batch": "phase2",
   "in_manifest": true,
   "approved": true,
   "title": "SEC Interpretive Release No. 33-8810: Commission Guidance Regarding Management's Report on Internal Control Over Financial Reporting",
   "description": "A guidance release from SEC, dated 2007-06-20",
   "scout_sha256": "308c75c66a303fc3af7fa18e60534d38fbc62fae029d165e4c29342a7651f471",
   "library_sha256": "308c75c66a303fc3af7fa18e60534d38fbc62fae029d165e4c29342a7651f471",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "sec-33-8183-auditor-independence",
   "date": "2003-01-28",
   "source_body": "SEC",
   "fills_gap": "P2-5",
   "official_or_mirror": "official",
   "batch": "phase2",
   "in_manifest": true,
   "approved": true,
   "title": "SEC Final Rule Rel. No. 33-8183: Strengthening the Commission's Requirements Regarding Auditor Independence",
   "description": "A rule from SEC, dated 2003-01-28",
   "scout_sha256": "f53b25f2ffdd45abcbaa3c5747b64c4ab62a8fae8f6a4a6b80aee34f0c14cbd5",
   "library_sha256": "f53b25f2ffdd45abcbaa3c5747b64c4ab62a8fae8f6a4a6b80aee34f0c14cbd5",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "gao-06-361",
   "date": "2006-04",
   "source_body": "GAO",
   "fills_gap": "P2-6",
   "official_or_mirror": "official",
   "batch": "phase2",
   "in_manifest": true,
   "approved": true,
   "title": "GAO-06-361 Sarbanes-Oxley Act: Consideration of Key Principles Needed in Addressing Implementation for Smaller Public Companies",
   "description": "A report from GAO, dated 2006-04",
   "scout_sha256": "117f53d843530e70d6b94841a6ed432756ce3f3f2499da4b51315ac7546b4357",
   "library_sha256": "117f53d843530e70d6b94841a6ed432756ce3f3f2499da4b51315ac7546b4357",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "gao-08-163",
   "date": "2008-01",
   "source_body": "GAO",
   "fills_gap": "P2-6",
   "official_or_mirror": "official",
   "batch": "phase2",
   "in_manifest": true,
   "approved": true,
   "title": "GAO-08-163 Audits of Public Companies: Continued Concentration in Audit Market for Large Public Companies Does Not Call for Immediate Action",
   "description": "A report from GAO, dated 2008-01",
   "scout_sha256": "783965d12af5ef962447bfb76cf7f972f876515ab5378f55897c726cb5afb5a9",
   "library_sha256": "783965d12af5ef962447bfb76cf7f972f876515ab5378f55897c726cb5afb5a9",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "free-enterprise-fund-v-pcaob-usreports",
   "date": "2010-06-28",
   "source_body": "U.S. Supreme Court (U.S. Reports via govinfo.gov)",
   "fills_gap": "P2-7",
   "official_or_mirror": "official",
   "batch": "phase2",
   "in_manifest": true,
   "approved": true,
   "title": "Free Enterprise Fund v. Public Company Accounting Oversight Board; 561 U.S. 477 (2010) (official U.S. Reports)",
   "description": "A court opinion from U.S. Supreme Court (U.S. Reports via govinfo.gov), dated 2010-06-28",
   "scout_sha256": "c2cabd34788557e1271fb7336c21a238be59f11f00c0d68614e6cd6c70ad42a2",
   "library_sha256": "c2cabd34788557e1271fb7336c21a238be59f11f00c0d68614e6cd6c70ad42a2",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "usc-15-7262-2024",
   "date": "2024 edition",
   "source_body": "GPO (govinfo.gov, U.S. Code)",
   "fills_gap": "P2-8",
   "official_or_mirror": "official",
   "batch": "phase2",
   "in_manifest": true,
   "approved": true,
   "title": "15 U.S.C. 7262 - Management assessment of internal controls (SOX Sec. 404, as amended incl. the Dodd-Frank small-company exemption), U.S. Code 2024 edition",
   "description": "A section of the U.S. Code from GPO (govinfo.gov, U.S. Code), dated 2024",
   "scout_sha256": "9cf4069ab47b250eee4e3b630f2b247adfd913f4b7a9b721b8f4fc441e753eef",
   "library_sha256": "9cf4069ab47b250eee4e3b630f2b247adfd913f4b7a9b721b8f4fc441e753eef",
   "same_fingerprint": true,
   "fingerprint_note": ""
  },
  {
   "id": "usc-15-78u-6-2024",
   "date": "2024 edition",
   "source_body": "GPO (govinfo.gov, U.S. Code)",
   "fills_gap": "P2-8",
   "official_or_mirror": "official",
   "batch": "phase2",
   "in_manifest": true,
   "approved": true,
   "title": "15 U.S.C. 78u-6 - Securities whistleblower incentives and protection (added by Dodd-Frank Sec. 922), U.S. Code 2024 edition",
   "description": "A section of the U.S. Code from GPO (govinfo.gov, U.S. Code), dated 2024",
   "scout_sha256": "529f36f9d45e16681e47823af0aac0fa3c85719d1884c83b6bf908aea48964fa",
   "library_sha256": "529f36f9d45e16681e47823af0aac0fa3c85719d1884c83b6bf908aea48964fa",
   "same_fingerprint": true,
   "fingerprint_note": ""
  }
 ]
};
