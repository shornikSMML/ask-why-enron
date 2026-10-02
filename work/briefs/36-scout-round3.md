# Brief: Source Scout, round 3 (documents identified through the owner's private finding aid)

Same rules as before: `work/briefs/11-scout.md`, `work/briefs/26-scout-phase2.md`, and `CLAUDE.md` MISSING SOURCES.

- Official sources only: justice.gov, sec.gov (including EDGAR), dol.gov, uscourts.gov / ca5.uscourts.gov, govinfo.gov.
- **At most 10 candidates.** Save them to `sources/candidates/round3/`, with rows in `sources/candidates/round3/candidates.csv` (same columns as before, status `candidate-unapproved`).
- **If any site shows a bot check, CAPTCHA, or refusal, stop trying that URL and record it. Never try to get around it.** See the "Safety notes" on the How This Was Built page for why.
- **Don't fetch anything from bankrupt.com or tinyurl.com.** They are unofficial.
- Don't summarize candidates' contents for anyone.
- **The finding aid behind this list is a copyrighted newsletter in a private repository.** Do not open it, and do not mention its contents in any public file. In `candidates.csv`, describe each document only by its official title, date, and source, and say which gap it fills by gap number or a short neutral phrase.

**Targets, in priority order** (dates and numbers are leads to verify, not facts):
1. DOJ press release(s) on **Lea Fastow**: April 7, 2004 (plea agreement rejected or withdrawn) and May 6, 2004 (plea and sentence). Two documents; take both if found.
2. ***United States v. Brown*, 459 F.3d 509 (5th Cir. 2006)**: the Merrill Lynch Nigerian barge appeal. Fifth Circuit opinions site (case no. likely 05-20319 or similar) or govinfo.
3. **DOL press release, May 12, 2004**: the settlement with Enron's outside directors and others in *Chao v. Enron Corp.* (S.D. Tex. H-03-2257).
4. **DOJ press release on Michael Kopper's sentencing** (around Sept–Nov 2006).
5. **SEC litigation release on *SEC v. Merrill Lynch & Co.*** (S.D. Tex. H-03-0946, filed March 17, 2003; the $80M settlement).
6. **DOJ press release on Arthur Andersen's sentencing** (October 2002).
7. **SEC litigation release or press release on CIBC's settlement** (December 22, 2003).
8. **DOJ press release on the sentencing of the three former NatWest bankers** (Bermingham, Darby, Mulgrew; February 2008), or their November 2007 plea if the sentencing release isn't found.
9. **DOJ release on the deferred prosecution agreements** with Merrill Lynch (September 2003) and/or CIBC (December 2003).
10. **Dynegy's Form 8-K or press release of November 28, 2001** announcing the end of the merger (EDGAR, Dynegy Inc.).

If you can't find a target, record what you tried and move on. You may substitute one of these lower-priority targets, within the limit of 10:
- the DOL release of Feb 16, 2006 (401(k) settlement proceeds);
- Enron's October 16, 2001 earnings release (an EDGAR 8-K, if one was filed);
- the DOJ release on Mark Koenig's sentencing.

**Outputs:**
- the candidate files and `candidates.csv`;
- `work/facts/scout-websites-round3.md`, listing every URL and its result;
- updated gap statuses in `build-log/gaps.md`;
- a final report.
