# Sources: "Ask Why" (Enron → Big 4 → Sarbanes-Oxley → PCAOB)

This folder holds the **primary sources** the agents may rely on. They are mostly U.S. government works (public domain) or documents filed in the public record. That mirrors Mollick's annotated *Waste Land*, which used a public-domain text, and it teaches students that **an agent's output is only as trustworthy as its sources**.

`manifest.csv` is the master list: one row per document, with title, date, the body that published it, the URL, and a status. `download_sources.py` fetches everything in the manifest. `download_log.csv` (created after a run) records what arrived, its size, and a fingerprint, so you can show that the files were not altered.

## Folder map

| Folder | What's in it | Why it matters for the demo |
|---|---|---|
| `01-internal-investigation` | Powers Report (Feb 2002), both a PDF and the official copy filed with the SEC | Enron's own board committee explains LJM, the Raptors, and the SPEs. The spine of "what happened" |
| `02-bankruptcy-examiner` | Batson examiner reports (first interim, final). Second and third interim reports and the final-report appendices are listed but are **not on the open web** | Court-appointed deep dive into the accounting and the banks' role (prepays, FAS 140 transactions) |
| `03-sec-filings` | 2000 10-K, Q3 2001 10-Q, Nov 8 2001 restatement 8-K and its press release, Nov 9 2001 Dynegy merger 8-K | What Enron *told* investors. Compare with what the investigations found |
| `04-sec-enforcement` | SEC complaints (Fastow, Kopper, Skilling/Causey, Lay, Glisan, Merrill Lynch, Duncan of Andersen); JPM/Citi settlement; SEC's Enron index page | Allegations as the regulator framed them; the auditor and the banks as defendants |
| `05-hearings-enron` | 16 congressional hearings, Jan–Jul 2002 (now including Senate Judiciary and the Senate HELP pension hearing), plus GAO's pension testimony | Sworn testimony: Watkins, Skilling, McMahon, Powers, Berardino (Andersen), Pitt (SEC), analysts, bankers, board members; Lay taking the Fifth |
| `06-congressional-reports` | Senate PSI board report; Governmental Affairs report on the SEC and the private-sector watchdogs; PSI "Fishtail, Bacchus, Sundance, and Slapshot" report on the banks; Joint Committee on Taxation Enron report | Congress's findings after the hearings |
| `07-sox-legislative-history` | Senate Banking "Accounting Reform and Investor Protection" hearings (3 vols.); House Financial Services CARTA hearings (Serial 107-60); S. Rept. 107-205; H. Rept. 107-414 (Oxley's CARTA bill); H. Rept. 107-610 (conference report); Pitt's CARTA testimony; CRS summary; President Bush's signing remarks and signing statement | **The public hearings behind SOX.** How Congress got from Enron to the PCAOB and auditor independence rules |
| `08-sox-law-pcaob-profession` | Sarbanes-Oxley Act text (PDF + HTML); GAO studies on accounting-firm consolidation; SEC orders of April 25, 2003 declaring the PCAOB ready and adopting its interim standards; SEC Sec. 704 enforcement study | The law itself, and GAO's account of the move from the Big 5 to the Big 4 |
| `09-courts-doj` | *Arthur Andersen v. U.S.* (2005); Skilling indictment; DOJ press releases; 5th Circuit *U.S. v. Skilling*; Supreme Court *Skilling v. U.S.* (2010) | How the criminal cases actually came out |

## Rules for the agents (fact-checker thread)

These are real people. Most are still living. Some were convicted and some were never charged. The fact-checker agent should enforce these rules:

1. **Every factual claim about a person cites a document in this folder** (file and page or section). No citation, no claim.
2. **Use the right verb for the source.** An SEC complaint or indictment *alleges*. A guilty plea or verdict *establishes*. Hearing testimony is what a witness *said under oath*. The Powers Report is what a board committee *found*.
3. **Check how each case ended before calling anyone guilty.** Examples to verify against the sources:
   - Andersen's conviction was **reversed** by the Supreme Court in 2005, after the firm had already collapsed.
   - Kenneth Lay was convicted in 2006 but **died before his appeal**, so his conviction was vacated.
   - Skilling's conviction was **partly narrowed** by the Supreme Court in 2010 (*Skilling v. U.S.*, honest-services fraud).
   - Many board members, bankers, and employees named in hearings were **never charged**.
4. **Dates and dollar amounts come from the documents, not from memory.**
5. **Prefer the official copy.** Where two copies exist (Powers PDF on a university mirror vs. SEC filing), cite the official one.

## Provenance notes

- Most files come from **govinfo.gov** (GPO), **sec.gov**, **gao.gov**, and **justice.gov**. These are federal works and are in the public domain.
- The **Powers Report** and **Batson reports** were produced for Enron's board and the bankruptcy court. They are public records rather than federal works, and some copies are hosted on university or third-party mirrors (noted in `manifest.csv`). Say so if the site republishes large excerpts.
- The CRS summary comes via EveryCRSReport.com, a mirror of Congressional Research Service reports.

## How to download

1. Open `download_sources.py` and put your name and email in the `CONTACT` line. sec.gov refuses downloads that don't say who is asking.
2. From inside this folder, run `python download_sources.py` (or ask Claude Code to run it).
3. Open `download_log.csv`. Every row should say `OK`, `ALREADY HAD`, or `SKIPPED`. Look at any `FAILED` or `CHECK` row: `CHECK` usually means a site sent back an error page instead of the document.
4. Safe to re-run. It only fetches files you don't already have.

## Status column

- `to-download`: URL listed; the script will fetch it.
- `not-online`: no free public copy found. The notes say where to get it (usually PACER, In re Enron Corp., Bankr. S.D.N.Y. No. 01-16034, or the University of Pennsylvania's Biddle Law Library, collection NBA.049).
- A few URLs were built from govinfo.gov's standard pattern instead of seen directly; their notes say "verify". The download log will show if one fails.

## Pass 2 changes (Sept 2026)

- Added 19 documents: Senate Judiciary and Senate HELP hearings, GAO pension testimony, House Financial Services CARTA hearings, the SOX conference report, Bush's signing remarks and statement, the SEC's PCAOB orders and press release, the SEC Sec. 704 study, *Skilling v. U.S.* (2010), and two more Enron 8-K documents.
- Confirmed the Nov 2001 8-K is the Nov 8 restatement filing.
- Corrected the House E&C auditing hearing to Feb 6, 2002, Serial 107-83.
- Correction to the pass-1 note: the prepay analysis is **Appendix E of the Second Interim Report**, not Appendix D. (Appendix D covers Enron's disclosure of its SPEs.)
- Found Batson's full appendix list via Penn's finding aid. Useful ones: Second Interim App. E (prepays), M (FAS 140), Q (impact of the six accounting techniques); Third Interim App. C (Enron officers), D (Citigroup), E (JPMorgan); Final Report App. B (Andersen), D (Lay, Skilling, outside directors).

## Still to find (next pass)

- Batson second and third interim reports and final-report appendices (PACER or Penn; not free online)
- Senate Judiciary: "Penalties for White Collar Crime" (S.Hrg. 107-923, June–July 2002), which fed SOX's criminal provisions
- PCAOB's first auditing standard (AS No. 1, 2003) and first inspection reports of the Big 4
- DOJ outcomes for Fastow and Kopper (plea agreements) and Andersen's 2002 obstruction verdict, to support the fact-checker's "how did it end" checks
