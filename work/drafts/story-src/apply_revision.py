#!/usr/bin/env python3
"""Revision pass (brief 19) for the Story chapters: uses new cards G-001...G-036.
Old text must occur exactly once; nothing is written if any edit fails.
Appends a "Story Writer" section to work/facts/fixes-revision.md.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

F = [
# ---------------- ch6 ----------------
("Gap 24: name Berardino; written statement, no oath", 6,
 'Andersen\'s chief executive told Congress in December 2001, as quoted in the Powers Report: "When we reviewed this transaction again in October 2001, we determined that our team\'s initial judgment that the 3 percent test was met was in error."{{A-048}}',
 'Andersen\'s chief executive, Joseph Berardino, wrote in a statement submitted to a House hearing on December 12, 2001, later quoted in the Powers Report: "When we reviewed this transaction again in October 2001, we determined that our team\'s initial judgment that the 3 percent test was met was in error."{{G-032}}{{A-048}}'),
("Gap 5/9: indictment's allegation added beside the Syllabus citation", 6,
 'Andersen instructed its employees to destroy documents under its document retention policy.{{C-042}}',
 'Andersen instructed its employees to destroy documents under its document retention policy.{{C-042}} The federal indictment later alleged that "Tons of paper relating to the Enron audit were promptly shredded."{{G-016}}'),
("Gap 5: indictment details and jury deliberations", 6,
 'On March 7, 2002, a federal grand jury indicted Andersen for obstruction of justice.{{C-048}} After a trial in Houston, the firm was convicted on June 15, 2002.{{C-038}}',
 'On March 7, 2002, a federal grand jury indicted Andersen on one count of obstruction of justice. The indictment alleged that between about October 10 and November 9, 2001, Andersen had corruptly persuaded its employees to withhold and destroy records.{{G-015}}{{C-048}} After a trial in Houston, the firm was convicted on June 15, 2002.{{C-038}} The Supreme Court later recounted that the jury deliberated for seven days, declared itself deadlocked, was urged by the judge to keep trying, and returned a guilty verdict after three more days.{{G-022}}'),
("Gap 9: cite the full Supreme Court opinion instead of the Syllabus", 6,
 'In 2005, the Supreme Court unanimously reversed Andersen\'s conviction and sent the case back to the lower court. According to the Syllabus (a summary prepared by the Court\'s Reporter of Decisions, not part of the opinion), the Court held that the jury instructions "failed to convey properly the elements" of the crime.{{C-043}} The jury had been told it could convict even if Andersen honestly believed its conduct was lawful. The Syllabus also notes that "Under ordinary circumstances, it is not wrongful for a manager to instruct his employees to comply with a valid document retention policy."{{C-044}} The reversal did not declare Andersen innocent; it found that the jury had been wrongly instructed. What happened in the case afterward is not covered by the library\'s documents.',
 'On May 31, 2005, the Supreme Court unanimously reversed Andersen\'s conviction and sent the case back to the lower court.{{G-019}} Chief Justice Rehnquist wrote for the Court: "We hold that the jury instructions failed to convey properly the elements of a \'corrup[t] persua[sion]\' conviction under § 1512(b), and therefore reverse."{{G-018}} The jury had been told it could convict even if Andersen honestly and sincerely believed its conduct was lawful; the Court wrote that "it is striking how little culpability the instructions required."{{G-020}} The instructions also let the jury convict without finding any link between the shredding and a particular official proceeding that Andersen had in mind.{{G-021}} The reversal did not declare Andersen innocent; it found that the jury had been wrongly instructed. What happened in the case after it was sent back is still not covered by the library\'s documents.'),
("Gap 3: Duncan's plea and SEC settlement terms", 6,
 'Duncan\'s own case took longer. In 2008, the SEC alleged that he had been reckless in not knowing that the audit reports he signed on Enron\'s statements for 1998 through 2000 were materially false and misleading.{{B-060}} The SEC\'s Enron index describes that case as a "settled action"; its terms are not in the library.{{B-061}}',
 'Duncan faced cases of his own. He pleaded guilty in 2002. The Justice Department described the charge as obstructing an SEC investigation into Enron;{{G-008}} the Supreme Court\'s opinion calls it witness tampering.{{G-023}} The library does not give the date of his plea, the charging document, or what later happened to the plea. In 2008, the SEC alleged that he had been reckless in not knowing that the audit reports he signed on Enron\'s statements for 1998 through 2000 were materially false and misleading.{{B-060}} He settled that case the day it was filed, without admitting or denying the allegations: he agreed to a permanent court order against violating the antifraud laws and to a permanent suspension from practicing before the SEC as an accountant, subject to court approval.{{G-029}} The same day, three other Andersen partners, including Michael Odom, consented, without admitting or denying the findings, to SEC orders finding improper professional conduct in their Enron work; each was barred from practicing before the SEC.{{G-030}}'),
# ---------------- ch7 ----------------
("Gaps 1, 2, 6: Kopper, Fastow, Glisan", 7,
 'agreed to forfeit $4 million, according to the SEC.{{B-039}}',
 'agreed to forfeit $4 million, according to the SEC.{{B-039}} Together with $8 million he agreed to pay in the SEC\'s civil case, that made $12 million, the total the Justice Department announced for "both this plea and a related SEC complaint."{{B-039}}{{G-013}} His sentence is still not in the library.'),
("Gap 1: Fastow's plea and sentence (forfeiture figures disagree)", 7,
 'In February 2004 the Justice Department listed Fastow among the defendants "convicted to date" in its Enron cases.{{B-033}} The library\'s documents do not say what he was convicted of or what sentence he received. The former treasurer, Ben Glisan, was also listed as convicted.{{B-049}}',
 'The terms of that settlement are not in the library. The Justice Department announced that on January 14, 2004, Fastow pleaded guilty to two counts of conspiracy to commit securities and wire fraud and agreed to cooperate with the investigation.{{G-001}} Under his plea agreement, the department said, he would serve ten years in prison and forfeit more than $29 million.{{G-002}} On September 26, 2006, the department announced that he had been sentenced to six years in prison; that release said the plea agreement required him to forfeit more than $20 million.{{G-004}} The two releases give different forfeiture figures, and the library does not explain the difference, or why the sentence was shorter than the ten years first agreed. The former treasurer, Ben Glisan, pleaded guilty on September 10, 2003 to conspiracy to commit wire and securities fraud, and under his plea agreement was sentenced the same day to five years in prison, the Justice Department announced.{{G-006}}'),
("Gap 7: Causey's sentence", 7,
 'The SEC later settled its civil case against him and barred him from serving as an officer or director of a public company.{{B-045}}',
 'The Justice Department announced that on November 15, 2006 he was sentenced to 66 months in prison.{{G-009}} The SEC later settled its civil case against him and barred him from serving as an officer or director of a public company.{{B-045}}'),
("Gap 4: Skilling after 2010", 7,
 'What happened after that is not covered by the library\'s documents.</p>',
 'In April 2011 the appeals court held that the error was harmless, affirmed all of his convictions, and again ordered a new sentence.{{G-024}} According to a 2013 agreement between Skilling and the government, the Supreme Court declined to review that ruling in April 2012.{{G-026}} In that agreement, the two sides agreed to recommend a sentence of 168 to 210 months, and Skilling agreed to give up any further challenges to his convictions.{{G-027}} The sentence the court actually imposed after that agreement is not in the library.</p>'),
("Gap 9: cite the full opinion", 7,
 'Arthur Andersen\'s conviction, as Chapter 6 described, was reversed in 2005.{{C-043}}',
 'Arthur Andersen\'s conviction, as Chapter 6 described, was reversed in 2005.{{G-018}}'),
]


def main():
    texts = {n: open(os.path.join(HERE, f'ch{n}.src.html')).read() for n in range(1, 8)}
    bad = []
    for fid, ch, old, new in F:
        if texts[ch].count(old) != 1:
            bad.append((fid, ch, texts[ch].count(old)))
            continue
        texts[ch] = texts[ch].replace(old, new)
    if bad:
        print('NOT APPLIED', bad)
        sys.exit(1)
    for n, t in texts.items():
        open(os.path.join(HERE, f'ch{n}.src.html'), 'w').write(t)
    strip = lambda s: re.sub(r'\{\{([^}]*)\}\}', r'[cite \1]', s)
    out = ['', '# Story Writer (chapters)', '',
           'Revision pass per `work/briefs/19-writers-revision.md`. Edits in `work/drafts/story-src/chN.src.html` '
           '(script `apply_revision.py`); `expand.py` now also reads `work/facts/reader-revision.json` (G-cards); '
           '`work/drafts/chN.html` regenerated. `[cite CARD]` = citation link generated from that card.',
           '',
           'Still open and said plainly in the text: Kopper\'s sentence; Fastow\'s SEC settlement terms; the reason for '
           'the $29M vs $20M forfeiture difference and for six years vs the agreed ten; Duncan\'s plea date, charging '
           'document and what happened to the plea; what happened to Andersen after the 2005 remand; the sentence '
           'actually imposed on Skilling after the 2013 agreement.',
           '',
           'Not changed: ch6 still cites the Syllabus (card C-042) for "Andersen instructed its employees to destroy '
           'documents"; no G-card covers the opinion\'s equivalent passage, so I added the indictment allegation (G-016) '
           'beside it rather than citing an uncarded page of the full opinion. Kopper $4M vs $12M is presented as '
           'consistent ($4M + $8M), not as a conflict. ch1-ch5 had no statements the new cards answer.',
           '']
    for fid, ch, old, new in F:
        out += [f'## {fid} (ch{ch})', '', '**Old:**', '', '> ' + strip(old), '', '**New:**', '', '> ' + strip(new), '']
    with open(os.path.join(ROOT, 'work', 'facts', 'fixes-revision.md'), 'a') as fh:
        fh.write('\n'.join(out) + '\n')
    print(f'applied {len(F)} edits')


main()
