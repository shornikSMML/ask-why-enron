# Round 2 fixes: Reference Writer (Cast, Timeline, Glossary)

Agent: Reference Writer. Findings from `work/facts/factcheck-round2-partB.md`. For each finding: the field changed, the old text and the new text, copied from the data files. Files: `js/cast-data.js`, `js/timeline-data.js`, `js/glossary-data.js`. No card was edited by me.

After the fixes: `integrate.py --no-log` reported 0 problems and `test_site.py` reported 0 problems. The Cast now has 29 entries (was 23), the Timeline 60, the Glossary 124. There are 299 citations, and every one points to a card marked OK or FIXED.

**#1 (must-fix). `jeffrey-mcmahon` · role**

- Old: Enron treasurer at the time of the March 2001 Chewco buyout; named CFO when Fastow went on leave in October 2001; Enron's president and COO when he testified in February 2002.
- New: Enron's treasurer until 2000, including during early talks in 2000 about buying out Chewco; named CFO when Fastow went on leave in October 2001; president and COO when he testified in February 2002.

**#1/#3 (must-fix / should-fix). `jeffrey-mcmahon` · summary**

- Old: The board's special committee reported that McMahon, as treasurer, proposed a $1 million return for the Chewco investors when Enron bought them out, and that Fastow instead negotiated about $10 million. McMahon testified under oath to the Senate Commerce Committee on February 26, 2002.
- New: McMahon told the board's special committee that in 2000, as treasurer, he proposed a $1 million return for the Chewco investors, and that Fastow later told him he had negotiated $10 million. McMahon testified under oath to the Senate Commerce Committee on February 26, 2002.

**#1/#3 cites. `jeffrey-mcmahon` · cites**

- Old: A-037 (powers-report-sec, PDF 70, pp. 60-64, II.G Enron's Repurchase of Chewco's Limited Partnership Interest); A-081 (enron-10q-q3-2001, p. 14, Note 2 Recent Events - SEC Investigation); B-052 (sec-enron-spotlight, Enron-Related Enforcement Actions list (Lit. Rel. 20159, June 20, 2007)); B-053 (batson-final-app-d, PDF 3, p. 1, App. D, I. Introduction); B-036 (batson-final-app-d, PDF 6, p. 4, App. D, I. Introduction, and n. 10)
- New: A-037 (powers-report-sec, PDF 70, pp. 60-61 and 97, II.G Enron's Repurchase of Chewco; V.A Raptor I); A-081 (enron-10q-q3-2001, p. 14, Note 2 Recent Events - SEC Investigation); B-052 (sec-enron-spotlight, Enron-Related Enforcement Actions list (Lit. Rel. 20159, June 20, 2007)); B-053 (batson-final-app-d, PDF 3, p. 1, App. D, I. Introduction); B-036 (batson-final-app-d, PDF 6, p. 4, App. D, I. Introduction, and n. 10)

Note: the "until 2000" and "early talks in 2000" wording comes from Powers pp. 60-61 and 97, as quoted in finding #1. It is cited to card A-037 with the locator widened to those pages. No card covers Powers p. 97 directly; the Fact-Checker may prefer a new card.

**#2 (must-fix) / #9. `mark-koenig` · outcome_text**

- Old: The Fifth Circuit's 2009 Skilling opinion notes that Koenig pleaded guilty to securities fraud, in part for a statement he made on an April 2001 call with analysts. The SEC charged him on August 25, 2004. The library does not give the date of his plea, his sentence, or how the SEC case ended.
- New: The Fifth Circuit's 2009 Skilling opinion notes that Koenig pleaded guilty to securities fraud, in part for a statement he made on a January 2001 call with investors (January 22, 2001). The SEC's list of Enron cases records that it charged him on August 25, 2004. The library does not give the date of his plea, his sentence, or how the SEC case ended.

**#2/#9 cites. `mark-koenig` · cites**

- Old: B-051 (ca5-skilling-2009, PDF 6, p. 6, I.A, footnote 3)
- New: B-051 (ca5-skilling-2009, PDF 6, p. 6, I.A, footnote 3); B-051 (sec-enron-spotlight, Enron-Related Enforcement Actions list (Lit. Rel. 18849, Aug. 25, 2004))

**#4. `kenneth-lay` · summary**

- Old: Lay had been chairman and CEO of Houston Natural Gas, which InterNorth bought in 1985. Although Houston Natural Gas was the smaller company, its managers took control, and Lay became chairman and CEO of the combined company in February 1986. He handed the CEO job to Jeffrey Skilling in February 2001 and took it back when Skilling resigned that August. The board's special committee (the Powers Committee) found that Lay, as CEO, bore ultimate responsibility.
- New: Lay had been chairman and CEO of Houston Natural Gas, which InterNorth bought in 1985. Although Houston Natural Gas was the smaller company, its managers took control, and Lay became chairman and CEO of the combined company in February 1986. He handed the CEO job to Jeffrey Skilling in February 2001 and took it back when Skilling resigned that August. The board's special committee (the Powers Committee) found that, as CEO, Lay had ultimate responsibility for making sure the officers reporting to him did their oversight jobs, and that "a large measure of the responsibility rests with the CEO."

**#5. `kenneth-lay` · outcome_status**

- Old: conviction vacated (died before appeal)
- New: conviction vacated after his death

Note for the Site Builder: `conviction vacated after his death` is not a key in `OUTCOME_LABELS` in `js/cast.js`. The page shows it as written, with a console *warning* (not an error; the test passes). Add it as a key to silence the warning.

**#6. `kenneth-lay` · outcome_text**

- Old: In July 2004 the SEC sued Lay, alleging fraud and insider trading; the library does not show how that civil case ended. A superseding indictment unsealed on July 8, 2004 charged him with conspiracy, securities fraud, wire fraud, bank fraud and making false statements to banks. In May 2006 a jury convicted him on every count against him. Lay died on July 5, 2006. According to the Fifth Circuit, his death caused the trial court to vacate (cancel) his conviction and dismiss the indictment, so in law he does not stand convicted. The library does not say whether he had filed an appeal. Earlier, on February 12, 2002, he was sworn in before a Senate committee and then declined to answer questions, invoking his Fifth Amendment right; that is not evidence of guilt. In a civil (non-criminal) analysis, the bankruptcy examiner concluded there was sufficient evidence for a fact-finder to conclude that Lay breached duties he owed Enron as an officer and director.
- New: In July 2004 the SEC sued Lay, alleging fraud and insider trading; the library does not show how that civil case ended. A superseding indictment unsealed on July 8, 2004 charged him with conspiracy, securities fraud, wire fraud, bank fraud and making false statements to banks. In May 2006, according to the Fifth Circuit, the jury convicted him of every count against him at that trial. Lay died on July 5, 2006. According to the Fifth Circuit, his death caused the trial court to vacate (cancel) his conviction and dismiss the indictment, so in law he does not stand convicted. The library does not say whether he had filed an appeal. Earlier, on February 12, 2002, he was sworn in before a Senate committee and then declined to answer questions, invoking his Fifth Amendment right; that is not evidence of guilt. In a civil (non-criminal) analysis, the bankruptcy examiner concluded there was sufficient evidence for a fact-finder to conclude that Lay breached duties he owed Enron as an officer and director.

**#4 cites (A-062 locator now p. 19). `kenneth-lay` · cites**

- Old: B-001 (sec-lay-complaint, PDF 3, p. 3, Second Amended Complaint, para. 7 (Defendants)); A-002 (rpt-jct-vol1, PDF 88, p. 60, Part Two, II.B.1); A-005 (rpt-jct-vol1, PDF 88, p. 60, Part Two, II.B.1); A-062 (powers-report-sec, PDF 16, p. 10 (Lay p. 19), Executive Summary - The LJM Transactions; The Participants); B-003 (sec-lay-complaint, PDF 1, p. 1, Second Amended Complaint, para. 1 (Summary)); B-006 (doj-lay-charged-press, DOJ press release #470, July 8, 2004); B-010 (ca5-skilling-2009, PDF 15, p. 15, II. Trial and Sentence); B-011 (ca5-skilling-2009, PDF 15, p. 15, II. Trial and Sentence, footnote 9); B-008 (hrg-commerce-lay-powers, PDF 29, p. 25, Statement of Kenneth L. Lay); A-097 (batson-final, PDF 12, pp. 9-11, I.C Summary of Conclusions)
- New: B-001 (sec-lay-complaint, PDF 3, p. 3, Second Amended Complaint, para. 7 (Defendants)); A-002 (rpt-jct-vol1, PDF 88, p. 60, Part Two, II.B.1); A-005 (rpt-jct-vol1, PDF 88, p. 60, Part Two, II.B.1); A-062 (powers-report-sec, PDF 16, p. 19, Executive Summary - The Participants); B-003 (sec-lay-complaint, PDF 1, p. 1, Second Amended Complaint, para. 1 (Summary)); B-006 (doj-lay-charged-press, DOJ press release #470, July 8, 2004); B-010 (ca5-skilling-2009, PDF 15, p. 15, II. Trial and Sentence); B-011 (ca5-skilling-2009, PDF 15, p. 15, II. Trial and Sentence, footnote 9); B-008 (hrg-commerce-lay-powers, PDF 29, p. 25, Statement of Kenneth L. Lay); A-097 (batson-final, PDF 12, pp. 9-11, I.C Summary of Conclusions)

**#7. `joseph-berardino` · summary**

- Old: Berardino testified under oath to the House Financial Services Committee on February 5, 2002, and announced changes at Andersen, including an independent oversight board chaired by Paul Volcker. He argued that the auditor's pass/fail report gives the same clean opinion to aggressive financial statements as to prudent ones.
- New: Berardino testified under oath to a House Financial Services subcommittee (Capital Markets) on February 5, 2002, and announced changes at Andersen, including an independent oversight board chaired by Paul Volcker. He argued that the auditor's pass/fail report gives the same clean opinion to aggressive financial statements as to prudent ones.

Note: card B-065's claim still says "the House Financial Services Committee". The card needs the same correction; I did not edit cards.

**#8. `david-delainey` · outcome_text**

- Old: The SEC charged Delainey on October 30, 2003. A Justice Department press release of February 2004 lists him among defendants "convicted to date." The library gives no details of his plea or trial, the charge, or his sentence, and does not show how the SEC case ended.
- New: The SEC's list of Enron cases records an October 30, 2003 case against the former CEO of Enron North America and Enron Energy Services, the post Delainey held. A Justice Department press release of February 2004 lists him among defendants "convicted to date." The library gives no details of his plea or trial, the charge, or his sentence, and does not show how the SEC case ended.

**#8 cites. `david-delainey` · cites**

- Old: B-050 (doj-skilling-charged-press, DOJ press release #099, Feb. 19, 2004); B-036 (batson-final-app-d, PDF 6, p. 4, App. D, I. Introduction, and n. 10)
- New: B-050 (doj-skilling-charged-press, DOJ press release #099, Feb. 19, 2004); B-036 (batson-final-app-d, PDF 6, p. 4, App. D, I. Introduction, and n. 10); B-050 (sec-enron-spotlight, Enron-Related Enforcement Actions list (Lit. Rel. 18435, Oct. 30, 2003))

Note: the added `sec-enron-spotlight` cites (Delainey, Koenig) carry the card id whose notes name that listing (B-050 note: Spotlight line 91; B-051 note: Spotlight line 63). Their `source_id` differs from the card's main source by design.

**#10. `arthur-andersen` · role**

- Old: Enron's outside auditor from Enron's formation in 1985 until Enron dismissed it on January 17, 2002. In 2001, the fourth-largest U.S. accounting firm.
- New: Enron's outside auditor from the 1985 merger that created Enron (it had audited InterNorth) until Enron dismissed it on January 17, 2002. In 2001, the fourth-largest U.S. accounting firm.

**#11. `merrill-lynch-executives` · outcome_text**

- Old: On March 17, 2003 the SEC charged Merrill Lynch and the four executives with aiding and abetting Enron's securities fraud (alleged). The SEC's complaint says Davis, Tilney and Furst asserted the Fifth Amendment in SEC testimony. The library does not show how the SEC case ended for any of them, and no library document names any of them in a criminal case.
- New: On March 17, 2003 the SEC charged Merrill Lynch and the four executives with aiding and abetting Enron's securities fraud (alleged). The SEC's complaint says Davis, Tilney and Furst asserted the Fifth Amendment in SEC testimony. The library does not show how the SEC case ended for any of them. The Fifth Circuit's 2009 opinion says four unnamed Merrill Lynch employees were convicted at trial over the barge deal and that their convictions were reversed on appeal in 2006. It does not name them, so the library does not show whether these four executives were among them.

**#11 cites. `merrill-lynch-executives` · cites**

- Old: B-083 (sec-merrill-complaint, Complaint, para. 1 (Summary)); B-084 (sec-merrill-complaint, Complaint, paras. 9-12 (Defendants))
- New: B-083 (sec-merrill-complaint, Complaint, para. 1 (Summary)); B-084 (sec-merrill-complaint, Complaint, paras. 9-12 (Defendants)); B-085 (ca5-skilling-2009, PDF 19, p. 19, III (discussion of United States v. Brown), footnote 12)

**#12 (optional, applied). `david-duncan` · outcome_text**

- Old: On January 24, 2002, sworn before a House subcommittee, Duncan declined on his lawyer's advice to answer questions, invoking his constitutional protection against self-incrimination; that is not evidence of guilt. On January 28, 2008 the SEC filed a complaint alleging he was reckless in not knowing that the audit reports he signed on Enron's 1998-2000 financial statements were materially false. The SEC's list describes it as a "settled action" and records a related proceeding against him on January 30, 2008; the terms are not in the library. The library contains no documents on any criminal case against him.
- New: On January 24, 2002, sworn before a House subcommittee, Duncan declined on his lawyer's advice to answer questions, invoking his constitutional protection against self-incrimination; that is not evidence of guilt. On January 28, 2008 the SEC filed a complaint alleging he was reckless in not knowing that the audit reports he signed on Enron's 1998-2000 financial statements were materially false. The SEC's list describes it as a "settled action" and records a related proceeding against him on January 30, 2008; the terms are not in the library. He testified at Andersen's criminal trial in 2002, as cited by the bankruptcy examiner. The library contains no documents on any criminal case against him.

Note on #12: written as "in 2002", not "May 2002". It is cited to card C-030, whose notes say the acknowledgments are sourced to Duncan's testimony at the Andersen trial. The May 14, 2002 date is only in the finding, not on a card.

**#13, #14 (optional notes):** not applied. There are no cards for batson-1st-interim PDF 5 n. 8 or for hrg-psi-banks-v1 PDF 189. They can be added if the Fact-Checker makes cards.

**Coordinator item 3: Andrew Fastow (F-010). `andrew-fastow` · outcome_status**

- Old: convicted
- New: pleaded guilty

**Coordinator item 3: Andrew Fastow. `andrew-fastow` · outcome_text**

- Old: On October 2, 2002 the SEC charged Fastow, alleging he ran a scheme to defraud Enron's security holders and enrich himself. The SEC's list of Enron cases includes a January 14, 2004 release titled "SEC Settles Civil Fraud Charges Filed Against Andrew S. Fastow"; the settlement terms are not in the library. Justice Department press releases of February 19 and July 8, 2004 list him among defendants "convicted to date." The library does not say whether he pleaded guilty or was convicted at trial, what crime he was convicted of, or his sentence. He later testified as a government witness at the Skilling and Lay trial. The bankruptcy examiner had concluded, in a civil analysis, that there was sufficient evidence for a fact-finder to conclude he breached his duties to Enron.
- New: On October 2, 2002 the SEC charged Fastow, alleging he ran a scheme to defraud Enron's security holders and enrich himself. The SEC's list of Enron cases includes a January 14, 2004 release titled "SEC Settles Civil Fraud Charges Filed Against Andrew S. Fastow"; the settlement terms are not in the library. Justice Department press releases of February 19 and July 8, 2004 list him among defendants "convicted to date." According to a separate opinion in Skilling v. United States (2010), he pleaded guilty in 2004. The library does not show the charge or the sentence. He later testified as a government witness at the Skilling and Lay trial. The bankruptcy examiner had concluded, in a civil analysis, that there was sufficient evidence for a fact-finder to conclude he breached his duties to Enron.

## Timeline

**#15 · 2006-05 · text**

- Old: After a four-month trial, a jury convicted Lay on every count against him, and Skilling on 19 counts while acquitting him on nine insider-trading counts. Skilling was later sentenced to 292 months in prison.
- New: After a four-month trial, a jury convicted Lay of every count against him at that trial, and Skilling on 19 counts while acquitting him on nine insider-trading counts. Skilling was later sentenced to 292 months in prison.

**#16 · 2002-05-07 · text**

- Old: Five Enron directors testified under oath to the Senate Permanent Subcommittee on Investigations. All rejected any share of responsibility.
- New: Five Enron directors testified under oath to the Senate Permanent Subcommittee on Investigations. The subcommittee reported that all five rejected any share of responsibility for Enron's collapse.

**#17 (note, applied) · 2003-03-17 · text**

- Old: The SEC alleged that Merrill Lynch and four of its executives aided and abetted Enron's fraud through the 1999 barge deal.
- New: The SEC alleged that Merrill Lynch and four of its executives aided and abetted Enron's fraud through two 1999 year-end deals, including the Nigerian barge "sale."

**#18 (note, applied) · 2001-12-02 · text**

- Old: Enron and 13 affiliates filed for Chapter 11 bankruptcy in New York, the largest U.S. bankruptcy until WorldCom's in July 2002.
- New: Enron and 13 affiliates filed for Chapter 11 bankruptcy in New York, the largest U.S. bankruptcy until WorldCom's in July 2002, according to the Joint Committee on Taxation staff.

**#19 (note, applied) · 2001-11-19 · title**

- Old: The hidden debt
- New: Debt on and off the balance sheet

**#19 · 2000-12-22 · title**

- Old: Propping up the Raptors
- New: A temporary fix for the Raptors

**#19 · 2000-12-31 · title**

- Old: Record revenue on paper
- New: Record reported revenue

## Glossary

**#20 · `pcaob` · long**

- Old: Before the PCAOB, the accounting profession largely regulated itself. The PCAOB is overseen by the SEC and has five members, only two of whom may be CPAs. In President Bush's words at the signing, "The auditors will be audited."
- New: Before the PCAOB, the accounting profession largely regulated itself. The PCAOB is overseen by the SEC and has five members, exactly two of whom must be (or have been) CPAs. In President Bush's words at the signing, "The auditors will be audited."

**#21 · `vacated` · long**

- Old: Courts vacate judgments for many reasons, including when a defendant dies before his appeal is finished. According to the Fifth Circuit, Kenneth Lay's death in 2006 caused the trial court to vacate his conviction and dismiss his indictment.
- New: Courts vacate judgments for many reasons, including when a defendant dies before his case is final. According to the Fifth Circuit, Kenneth Lay's death in 2006 caused the trial court to vacate his conviction and dismiss his indictment.

## Coordinator item 4
No file of mine cites `rpt-psi-board` n. 155 (checked: no Cast, Timeline or Glossary cite uses rpt-psi-board PDF 49).

## New Cast entries (coordinator item 2)

Built from the F-cards, read with their `checker_note`. Where an entry connects to facts already on checked cards, it also cites those (A-041, A-049, A-058, A-063, A-069, C-001, C-018). They are listed so they can be re-checked.

### `lea-fastow` (new)

- name: Lea Fastow
- role: Andrew Fastow's wife; had earlier worked in Enron's Finance group. A separate opinion in Skilling v. United States (2010) describes her as an assistant treasurer.
- summary: The board's special committee found that, during certain periods, back-office tasks for the Chewco partnership appear to have been performed by Fastow's wife, who had previously worked in Enron's Finance group. It did not know whether she was paid for this work. The committee's report does not name her; a House subcommittee chairman identified her as Lea Fastow.
- outcome_status: pleaded guilty
- outcome_text: According to a separate opinion in Skilling v. United States (2010), the Enron Task Force indicted Lea Fastow in 2003, and she pleaded guilty in 2004. That opinion (by Justice Sotomayor, joined by two other justices) mentions this only as background, in a list of news coverage before Skilling's trial; it is not the Court's holding or a record of her case. The library does not show the charge or her sentence.
- cites: F-009 (powers-report-sec, p. 54, II (Chewco), management of Chewco); F-009 (hrg-hec-collapse-pt2, PDF 80, p. 76, statement of Chairman Greenwood); F-010 (skilling-scotus-2010, PDF 93, p. 450, n. 12, Opinion of Sotomayor, J. (concurring in part and dissenting in part), n. 12)

### `richard-buy` (new)

- name: Richard Buy
- role: Enron's chief risk officer; head of its Risk Assessment and Control group.
- summary: The board relied on Buy and chief accounting officer Richard Causey to review and approve the LJM transactions. The special committee found that neither "ignored his responsibilities," but that both interpreted their roles very narrowly. Vince Kaminski told the committee he had brought his concerns about the 1999 Rhythms deal to Buy; Buy said he did not recall those discussions.
- outcome_status: no charges shown in library
- outcome_text: The library documents show no charges against him. On February 7, 2002, sworn in alongside Causey at a House Energy and Commerce oversight hearing, Buy declined to answer any questions, invoking his Fifth Amendment right. That is not evidence of guilt.
- cites: F-011 (powers-report-sec, p. 10, Executive Summary); A-041 (powers-report-sec, PDF 78, pp. 70-73, III.A Formation and Authorization of LJM Cayman, L.P. and LJM2); F-014 (powers-report-sec, p. 84 (continues p. 85), IV (Rhythms hedge), C.3 'Pricing and Credit Capacity'); F-012 (hrg-hec-collapse-pt2, PDF 27, p. 23, Testimony of Richard A. Causey and Richard B. Buy)

### `greg-whalley` (new)

- name: Greg Whalley
- role: Enron's president and chief operating officer from August 2001; member of the Office of the Chairman with Lay.
- summary: Enron reported that after Skilling resigned in August 2001 and Lay took back the CEO job, Whalley was promoted to president and COO. The board's special committee found that in mid-September 2001 Lay and Whalley directed Causey to terminate the Raptors, which Enron did on September 28, 2001.
- outcome_status: no charges shown in library
- outcome_text: The library documents show no charges against him.
- cites: F-013 (enron-10q-q3-2001, p. 37, Notes to Consolidated Financial Statements, Note 12 (Business Segment Information)); A-058 (powers-report-sec, PDF 133, pp. 127-128, V.E Unwind of the Raptors)

### `vince-kaminski` (new)

- name: Vince Kaminski
- role: Head of Enron's Research Group, which handled complex option pricing and modeling. (The Powers Report calls him Vincent; the bankruptcy examiner, Wincenty.)
- summary: Kaminski told the board's special committee that he was very uncomfortable with the 1999 Rhythms deal with LJM1 and brought his concerns to his supervisor, Richard Buy, who said he did not recall those discussions; the committee noted sharply different recollections. In early 2000 his group estimated a 68% probability that the Rhythms structure would default. In sworn testimony to the bankruptcy examiner, he compared the Raptor hedges to buying house insurance from your own spouse.
- outcome_status: no charges shown in library
- outcome_text: The library documents show no charges against him. He appears in the library as a witness.
- cites: F-014 (powers-report-sec, p. 84 (continues p. 85), IV (Rhythms hedge), C.3 'Pricing and Credit Capacity'); A-049 (powers-report-sec, PDF 93, p. 87, IV.E Unwinding the Transaction); A-069 (batson-final, PDF 22, p. 19, n. 41, III.A Overview, footnote 41)

### `nancy-temple` (new)

- name: Nancy Temple
- role: In-house attorney at Arthur Andersen.
- summary: On October 12, 2001 Temple e-mailed an Andersen partner suggesting that the Enron audit team be reminded of the firm's document-retention policy. She testified that she was first asked on September 28, 2001 to join a call about an Enron accounting issue, and that until October 12 she gave legal advice, after consulting her supervisor and others, on documentation and retention. At a January 2002 hearing the House subcommittee chairman called her mid-October e-mails "highly unusual and of questionable timing," and in the same statement said, "We have no reason at this point to doubt her good intentions."
- outcome_status: no charges shown in library
- outcome_text: The library documents show no charges against her. She testified under oath before the House Energy and Commerce oversight subcommittee on January 24, 2002.
- cites: C-001 (hrg-hec-andersen-shredding, PDF 49, p. 45, Hearing record exhibit (e-mail dated 10/12/2001 from Nancy A. Temple to Michael C. Odom)); C-018 (hrg-hec-andersen-shredding, PDF 126, p. 122, Questioning of Temple by Chairman Tauzin); F-008 (hrg-hec-andersen-shredding, PDF 7, p. 3, Opening statement of Chairman Greenwood)

### `raymond-troubh` (new)

- name: Raymond Troubh
- role: One of two new directors added to Enron's board after October 2001 and appointed to its Special Investigative Committee (the Powers Committee).
- summary: Neither Troubh nor William Powers had been on the board when the transactions under investigation took place. The report's sections judging the board are the views of Powers and Troubh alone; Herbert Winokur, the committee's third member, did not join them.
- outcome_status: no charges shown in library
- outcome_text: The library documents show no charges against him. He appears in the library as an investigator.
- cites: F-015 (powers-report-sec, p. 31 (and p. 9 n. 1), I. Introduction (the Special Investigative Committee)); A-063 (powers-report-sec, PDF 28, pp. 22-24, Executive Summary - The Participants: The Board of Directors)

Notes on the new entries:
- **Lea Fastow:** attributed throughout to "a separate opinion in Skilling v. United States (2010)". No charge or sentence is given, and the candidates-folder DOJ release is not used. Her name comes from Chairman Greenwood's statement (hrg-hec-collapse-pt2 PDF 80, per the F-009 notes); Powers does not name her. The status label is "pleaded guilty", the only label that fits. The text says it is background in a separate opinion.
- **Richard Buy:** the text says he declined to answer (F-012), invoked the Fifth, and that "That is not evidence of guilt." The word "charged" is not used near his name except in "no charges shown".
- **Nancy Temple:** the second Greenwood quote ("We have no reason at this point to doubt her good intentions") comes from the F-008 notes, which the checker verified (line 292). Both quotes are attributed to the subcommittee chairman.
- **Raymond Troubh:** the role follows F-015's wording ("added to Enron's board after October 2001").
