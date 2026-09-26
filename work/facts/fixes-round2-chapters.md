# Round 2 fixes to the Story chapters

Agent: Story Writer. Applies every must-fix and should-fix finding in `work/facts/factcheck-round2-partA.md`, and every "note" item (all of them fix wording or citations). Also the coordinator's item 2 (one formation-date wording used in ch1 and ch6) and item 3 (ch4 caption).

Edits were made in `work/drafts/story-src/chN.src.html` by `work/drafts/story-src/apply_round2.py`, then `work/drafts/chN.html` was regenerated with `expand.py`. In the wording below, `[cite CARD]` stands for a citation link generated from that fact card; `[cite CARD!source@locator#pdfpage]` means the link points to that source, locator and PDF page instead of the card's own.

Not done: item 7-5 asks to update card B-079 (or add a transcript card) so the card matches the LeMaistre citation. Cards belong to the Readers, so I did not edit them; the chapter text and citation (hrg-psi-board, p. 90, PDF 100) are unchanged, as the finding allows. Optional item 5 (Watkins letter quote) was skipped: cards F-001 to F-004 had no "checked" value when I looked.

## 1-1 (ch1)

**Old:**

> Investors valued the company highly. The congressional tax staff reported that Enron's <span class="term" data-term="market-capitalization">market capitalization</span> (the total value of all its shares on the stock market) grew from

**New:**

> The congressional tax staff reported, citing an Enron press release, that Enron's <span class="term" data-term="market-capitalization">market capitalization</span> (the total value of all its shares on the stock market) had grown from

## 1-2, 1-4 (and must-fix 2-1) (ch1)

**Old:**

> Enron began trading natural gas through <span class="term" data-term="forward-contract">forward contracts</span> in 1989: agreements to buy or sell gas at a fixed price on a future date. In 1992 it adopted <span class="term" data-term="mark-to-market">mark-to-market accounting</span> for its trading operations, a method explained in Chapter 2. In 1994 it began buying and selling electricity too.[cite A-007]

**New:**

> Enron began trading natural gas through <span class="term" data-term="forward-contract">forward contracts</span> in 1989: agreements to buy or sell gas at a fixed price on a future date.[cite A-007@p. 61, Part Two, II.B.2#89] Enron told the congressional tax staff that it adopted <span class="term" data-term="mark-to-market">mark-to-market accounting</span>, a method explained in Chapter 2, for its trading operations in 1992.[cite A-007] The sources differ on the year: a Senate staff report found that Enron applied the method to a subsidiary's 1991 results.[cite C-055] In 1994 Enron began buying and selling electricity too.[cite A-007]

## 1-3 (ch1)

**Old:**

> from the reservoir to the burner tip."[cite A-006]

**New:**

> from the reservoir to the burner tip ..."[cite A-006]

## 1-5 (and coordinator item 2: formation date) (ch1)

**Old:**

> From the start, the new company had the same outside <span class="term" data-term="auditor">auditor</span>: Arthur Andersen, which had audited InterNorth and became Enron's auditor when the combined company was formed.[cite C-026]

**New:**

> Arthur Andersen, which had audited InterNorth, became the outside <span class="term" data-term="auditor">auditor</span> of the combined company formed when InterNorth acquired Houston Natural Gas in July 1985, which took the name Enron in April 1986.[cite C-026][cite A-001]

## coordinator item 2: formation date (ch1)

**Old:**

> Lay would lead Enron from its formation in 1986 until early 2002.

**New:**

> Lay would lead the company until early 2002.

## 2-1 (must-fix) (ch2)

**Old:**

> Enron adopted it for its trading operations in 1992.[cite A-007]

**New:**

> The sources differ on when Enron started using it. Enron told the congressional tax staff that it adopted the method for its trading operations in 1992.[cite A-007] The Senate staff report described below found that Enron applied it to a subsidiary's 1991 results, a year earlier than the SEC had agreed to.[cite C-055]

## 2-5 (supports 2-1) (ch2)

**Old:**

> The staff wrote: "Apparently, the SEC did not respond further to this correspondence."[cite C-055]

**New:**

> The staff wrote: "Apparently, the SEC did not respond further to this correspondence and Enron went ahead and reported EGS's 1991 financial information using the mark-to-market method." (EGS, Enron Gas Services, was the subsidiary.)[cite C-055]

## 2-2 (ch2)

**Old:**

> Enron reported that its trading volumes rose 59 percent in 2000, EnronOnline's first full year.[cite A-018]

**New:**

> Enron reported that EnronOnline helped its wholesale volumes rise 59 percent in 2000, EnronOnline's first full year.[cite A-018]

## 2-3 (ch2)

**Old:**

> Years later, the court-appointed bankruptcy examiner concluded that if Enron had not used six particular accounting techniques, it would have reported $22.1 billion of debt for 2000, not $10.2 billion.[cite A-067]

**New:**

> Years later, the court-appointed bankruptcy examiner, in an earlier report summarized in his final one, concluded that six particular accounting techniques let Enron report $10.2 billion of debt at the end of 2000 rather than $22.1 billion.[cite A-067]

## 2-4 (ch2)

**Old:**

> The committee found that Enron used such arrangements in many parts of its business, including for its Houston headquarters.[cite A-029]

**New:**

> The committee reported that it had been told Enron used such arrangements in many parts of its business, including for its headquarters building in Houston.[cite A-029]

## 2-6 (note) (ch2)

**Old:**

> By 2000, Enron's annual report described a company

**New:**

> By 2000, Enron's annual report to the SEC (its Form 10-K) described a company

## 2-6 (note) (ch2)

**Old:**

> Its 2000 annual report stated that

**New:**

> Its 2000 Form 10-K stated that

## 2-6 (note) (ch2)

**Old:**

> printed in its 2000 annual report, said

**New:**

> printed in its 2000 Form 10-K, said

## 2-6 (note) (ch2)

**Old:**

> Enron's annual report explained:

**New:**

> Enron's Form 10-K explained:

## 2-7 (note) (ch2)

**Old:**

> In later years it reports only the changes in its estimate.

**New:**

> In later years it reports only changes in the contract's estimated value, as time passes and forecasts change.

## 3-1 (ch3)

**Old:**

> The board's special committee, which investigated Enron after its collapse, summarized

**New:**

> The board's special committee, which investigated Enron in late 2001 and early 2002, summarized

## 3-2 (ch3)

**Old:**

> and that it saw no evidence that Kopper's role was disclosed to, or approved by, Lay or the board.[cite A-033]

**New:**

> It found no written record that Kopper's role was disclosed to the board. Lay said he was never told. Skilling said he had approved Kopper's role himself and believed he had discussed it with the board; the committee said his approval did not satisfy Enron's Code of Conduct.[cite A-033]

## 3-3 (ch3)

**Old:**

> When Enron bought out Chewco's interest in March 2001, the committee found, Kopper and another Chewco investor received about $10.5 million on their $125,000 investment.[cite A-037]

**New:**

> In all, including Enron's buyout of Chewco's interest in March 2001, the committee found that Kopper and another Chewco investor received about $10.5 million on their $125,000 investment.[cite A-037]

## 3-7 (note) (ch3)

**Old:**

> LJM2 attracted about 50 investors with $394 million in commitments.[cite A-041]

**New:**

> The committee understood that LJM2 had about 50 investors with $394 million in commitments, though it could not be certain because LJM2 declined to give it information.[cite A-041]

## 3-8 (note) (ch3)

**Old:**

> the right to sell its Rhythms shares at $56 a share.[cite A-046]

**New:**

> the right to sell its Rhythms shares at $56 a share in June 2004.[cite A-046]

## 3-4 (ch3)

**Old:**

> In early 2000, a team led by Enron's head of research, Vince Kaminski, estimated a 68% probability that the structure would default on what it owed Enron.[cite A-049]

**New:**

> Enron's head of research, Vince Kaminski, told the committee that in early 2000 his team had estimated a 68% probability that the structure would default on what it owed Enron. (Causey told the committee he did not recall that figure.)[cite A-049]

## 3-6 (note) (ch3)

**Old:**

> When the Rhythms deal was unwound in 2000, Fastow and several Enron employees secretly invested in a partnership called Southampton Place. The special committee found that

**New:**

> When the Rhythms deal was unwound in 2000, Fastow and several Enron employees invested in a partnership called Southampton Place, without the knowledge of virtually anyone else at Enron, the special committee found. It found that

## 3-9 (note) (ch3)

**Old:**

> there's a chance that the mortgage company will object."[cite A-069]

**New:**

> there's a chance that the mortgage company will object ..."[cite A-069]

## 3-5 (ch3)

**Old:**

> From mid-2000 to late 2001, the committee calculated, Enron's pre-tax earnings would have been 72% lower without them.[cite A-054]

**New:**

> From July 2000 through September 2001, not counting the $710 million charge to end the Raptors, the committee calculated that Enron's pre-tax earnings would have been 72% lower without them, though it noted it could not know what Enron would otherwise have done.[cite A-054]

## 4-3 (ch4)

**Old:**

> Another Andersen partner confirmed through his lawyer that the handwriting was Duncan's and that the risk profile was discussed with the committee.[cite B-063]

**New:**

> The annotated document itself was not given to the committee during the meeting, but another Andersen partner confirmed through his lawyer that the handwriting was Duncan's and that the risk profile was discussed with the committee.[cite B-063]

## 4-2 (ch4)

**Old:**

> But he said he never heard terms such as "form over substance" used.

**New:**

> But he said that, as far as he recalled, he never heard phrases such as "pushing the limits" or "form over substance" used.

## 4-1 (ch4)

**Old:**

> As Chapter 3 described, in early 2000 a team led by the head of research, Vince Kaminski, estimated a 68% chance that the Rhythms hedge structure would fail to pay what it owed Enron.[cite A-049]

**New:**

> As Chapter 3 described, the head of research, Vince Kaminski, told the special committee that in early 2000 his team had estimated a 68% chance that the Rhythms hedge structure would fail to pay what it owed Enron. (Causey said he did not recall that figure.)[cite A-049]

## 4-5 (ch4)

**Old:**

> <figcaption>Congress held many hearings on Enron in 2002. Much of what is known about the warning signs, including Sherron Watkins's account, comes from sworn testimony at hearings like this one.</figcaption>

**New:**

> <figcaption>A Senate Governmental Affairs Committee hearing on Enron, January 24, 2002, as identified in the photo's source caption. Congress held many hearings on Enron in 2002; Sherron Watkins testified at a different one, before the Senate Commerce Committee, in February.</figcaption>

## 4-6 (note) (ch4)

**Old:**

> from mid- or late June to August 2001 she worked directly for him.[cite B-054]

**New:**

> from mid- or late June to August 2001 she worked directly for him.[cite B-054@pp. 10-11, Statement of Sherron Watkins#15]

## 4-4 (ch4)

**Old:**

> because under the SEC's review cycle Enron was not due again until 2002.[cite C-053]

**New:**

> partly because under the SEC's review cycle Enron was not due again until 2002.[cite C-053]

## 5-1 (ch5)

**Old:**

> Sources differ on the after-tax amount: Enron's October 16 announcement put it at $544 million, while its later quarterly report put it at $462 million.[cite A-058]

**New:**

> Sources differ on the after-tax amount.[cite A-058] Enron's October 16 announcement put it at $544 million,[cite A-058!batson-final@p. 15, n. 29, II.A Events of Fall 2001#18] while its later quarterly report put it at $462 million.[cite A-058!enron-10q-q3-2001@p. 52, Item 2. MD&A, line 3673]

## 5-4 (ch5)

**Old:**

> Enron's stock, which closed at $34.30 on October 16, fell to $13.90 by October 31.[cite A-091@p. 83, Part Two, II.C.4#111]

**New:**

> Enron's stock, at $34.30 on October 16 according to the congressional tax staff, fell to $13.90 by the close of trading on October 31.[cite A-091@p. 83, Part Two, II.C.4#111] (A congressman gave a different figure for October 16: $30.72 at the close.[cite C-065])

## 5-2 (ch5)

**Old:**

> On October 24, Enron announced that Fastow was on leave and would be replaced as chief financial officer. On October 31, the SEC opened a formal investigation.[cite A-081]

**New:**

> On October 24, Enron announced that Fastow was on leave and would be replaced as chief financial officer.[cite A-081!powers-report-sec@pp. 30-31, Introduction, lines 1258-1267] On October 31, the SEC opened a formal investigation.[cite A-081]

## 5-8 (note) (ch5)

**Old:**

> Enron's board also formed a special committee, chaired by William Powers Jr., to investigate

**New:**

> Enron's board also formed a special committee, later chaired by William Powers Jr., to investigate

## 5-7 (note) (ch5)

**Old:**

> should not be relied upon."[cite A-083]

**New:**

> should not be relied upon."[cite A-083@p. 1, Press release, Nov 8, 2001 (Exhibit 99.1), lines 44-47]

## 5-3 (ch5)

**Old:**

> The examiner's reports put the portion raised through special purpose entities at about $13 billion to $14 billion.[cite A-087]

**New:**

> The examiner's reports put the portion raised through special purpose entities at about $13 billion to $14 billion.[cite A-087][cite A-087!batson-1st-interim@p. 7#9]

## 5-6 (note) (ch5)

**Old:**

> Why Dynegy withdrew is disputed; Enron claimed wrongful termination.[cite A-092]

**New:**

> Why Dynegy withdrew is disputed: the bankruptcy examiner wrote that Dynegy abandoned the merger "allegedly because of undisclosed liabilities of Enron,"[cite A-091!batson-1st-interim@p. 6, n. 21#8] and Enron claimed wrongful termination.[cite A-092]

## 5-5 (ch5)

**Old:**

> He concluded that in 2000, six accounting techniques

**New:**

> In an earlier report, summarized in his final one, he had concluded that in 2000, six accounting techniques

## coordinator item 2: formation date (ch6)

**Old:**

> Arthur Andersen audited Enron from the time the combined company was formed in 1985.[cite C-026]

**New:**

> Arthur Andersen, which had audited InterNorth, became the auditor of the combined company formed when InterNorth acquired Houston Natural Gas in July 1985, which took the name Enron in April 1986.[cite C-026][cite A-001]

## 6-3 (ch6)

**Old:**

> Andersen disputed the label. Its executive C.E. Andrews testified that "the audit-related fees on Enron were $25 million, essentially half of the total fee," and another partner said much of the so-called consulting was work auditors typically do.[cite C-020]

**New:**

> Andersen disputed the label. Its executive C.E. Andrews testified that "the audit-related fees on Enron were $25 million, essentially half of the total fee." Andersen partner Michael Odom added that a lot of the consulting was work typically done by the auditor.[cite C-020]

## 6-4 (note) (ch6)

**Old:**

> Andersen accountants later acknowledged three errors in the Enron audits. One was letting Enron record the Raptor IOUs as assets, which overstated Enron's equity by $1 billion. Another was wrongly concluding

**New:**

> Andersen accountants later acknowledged three errors in the Enron audits. One was approving the "aggregation," or pooling, of the Raptors' credit. Another was letting Enron record the Raptor IOUs as assets, which overstated Enron's equity by $1 billion. The third was wrongly concluding

## 6-1 (ch6)

**Old:**

> The examiner saw the evidence as pointing two ways. On one side, it suggested that "Enron officers withheld information from Andersen in numerous instances."[cite C-029] On the other, it suggested "a concerted effort

**New:**

> The examiner found evidence that "Enron officers withheld information from Andersen in numerous instances."[cite C-029] But he said that did not explain the whole story of Andersen's role. Going beyond it, he wrote, "the evidence suggests a concerted effort

## 6-6 (note) (ch6)

**Old:**

> The firm did not survive.

**New:**

> The firm did not survive as an operating business.

## 6-5 (note) (ch6)

**Old:**

> its headcount fell from 28,000 to about 150.[cite C-041]

**New:**

> its headcount fell from 28,000 to about 150, plus a few dozen others, mainly lawyers.[cite C-041]

## 6-2 (ch6)

**Old:**

> In 2005, the Supreme Court unanimously reversed Andersen's conviction. It held that the jury instructions

**New:**

> In 2005, the Supreme Court unanimously reversed Andersen's conviction and sent the case back to the lower court. According to the Syllabus (a summary prepared by the Court's Reporter of Decisions, not part of the opinion), the Court held that the jury instructions

## 6-2 (ch6)

**Old:**

> The official summary of the decision (its Syllabus) notes that

**New:**

> The Syllabus also notes that

## 5-8 (note, same point) (ch7)

**Old:**

> formed a special committee in late October 2001, chaired by William Powers Jr.,

**New:**

> formed a special committee in late October 2001, later chaired by William Powers Jr.,

## 7-4 (note) (ch7)

**Old:**

> Five directors, past and present, testified under oath in May 2002.[cite B-073]

**New:**

> Five directors, past and present, testified under oath in May 2002.[cite B-073][cite B-073@p. 2, Subcommittee Investigation#6]

## 7-7 (note) (ch7)

**Old:**

> We asked probing questions."[cite B-075]

**New:**

> We asked probing questions ..."[cite B-075]

## 7-1 (ch7)

**Old:**

> Lay obtained over $77 million in cash this way and repaid it only with Enron stock.[cite B-016]

**New:**

> Lay obtained over $77 million in cash this way and repaid it only with Enron stock.[cite B-016@p. 50, Factual Basis (Excessive Compensation)#54]

## 7-2 (ch7)

**Old:**

> J.P. Morgan Chase agreed to pay $135 million and Citigroup $120 million to settle charges that they helped Enron disguise loans.[cite B-086]

**New:**

> J.P. Morgan Chase agreed to pay $135 million and Citigroup $120 million to settle SEC charges. Of Citigroup's payment, $101 million related to its Enron dealings and the rest to another company, Dynegy. The charges concerned helping Enron disguise loans.[cite B-086]

## 7-3 (ch7)

**Old:**

> One employee testified that her notice said

**New:**

> One employee told the committee, in her written statement, that her notice said

## 7-3 (ch7)

**Old:**

> The congressman testified that the plan lost

**New:**

> The congressman told the committee that the plan lost

## 7-8 (note) (ch7)

**Old:**

> must certify each annual and quarterly report,[cite C-076] with criminal penalties of up to 20 years in prison for a willfully false certification.[cite C-077]

**New:**

> must certify each annual and quarterly report,[cite C-076] and a separate certification carries criminal penalties of up to 20 years in prison if willfully false.[cite C-077]

## 7-6 (note) (ch7)

**Old:**

> Protection for employees who report suspected securities fraud to regulators, Congress, or a supervisor.

**New:**

> Protection for employees who report suspected fraud against shareholders or violations of SEC rules to regulators, Congress, or a supervisor.
