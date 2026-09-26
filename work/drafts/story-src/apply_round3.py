#!/usr/bin/env python3
"""Round 3 fixes (work/facts/factcheck-round3-partA.md) to the Story source drafts.
Old text must occur exactly once; nothing is written if any edit fails.
Appends a "Round 3" section to work/facts/fixes-round2-chapters.md.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

F = [
("1-5 / formation (split sentence)", 1,
 'became the outside <span class="term" data-term="auditor">auditor</span> of the combined company formed when InterNorth acquired Houston Natural Gas in July 1985, which took the name Enron in April 1986.{{C-026}}{{A-001}}',
 'became the outside <span class="term" data-term="auditor">auditor</span> of the combined company formed when InterNorth acquired Houston Natural Gas in July 1985.{{C-026}} The combined company took the name Enron in April 1986.{{A-001}}'),
("1-5 / formation (split sentence)", 6,
 'became the auditor of the combined company formed when InterNorth acquired Houston Natural Gas in July 1985, which took the name Enron in April 1986.{{C-026}}{{A-001}}',
 'became the auditor of the combined company formed when InterNorth acquired Houston Natural Gas in July 1985.{{C-026}} The combined company took the name Enron in April 1986.{{A-001}}'),
("3-2 (typo)", 3,
 'CalPERS," It found no written record',
 'CalPERS." It found no written record'),
("5-1 (replacement text from Round 3, section 2)", 5,
 'Sources differ on the after-tax amount.{{A-058}} Enron\'s October 16 announcement put it at $544 million,{{A-058!batson-final@p. 15, n. 29, II.A Events of Fall 2001#18}} while its later quarterly report put it at $462 million.{{A-058!enron-10q-q3-2001@p. 52, Item 2. MD&A, line 3673}}',
 'Sources differ on the after-tax amount. The special committee and the bankruptcy examiner put it at $544 million,{{A-058}}{{F-021}} the figure in Enron\'s October 16 announcement, where that charge also covered losses on some other investments.{{F-016}} Enron\'s later quarterly report put the Raptor charges at $462 million after tax.{{F-017@p. 53, Item 2. MD&A, lines 3672-3674}}'),
("5-2 (card repoint to F-018)", 5,
 '{{A-081!powers-report-sec@pp. 30-31, Introduction, lines 1258-1267}}',
 '{{F-018}}'),
("5-3 (card repoint to F-019)", 5,
 '{{A-087!batson-1st-interim@p. 7#9}}',
 '{{F-019}}'),
("5-6 (card repoint to F-020)", 5,
 '{{A-091!batson-1st-interim@p. 6, n. 21#8}}',
 '{{F-020}}'),
("4-5 (optional caption refinement)", 4,
 '<figcaption>A Senate Governmental Affairs Committee hearing on Enron, January 24, 2002, as identified in the photo\'s source caption.',
 '<figcaption>The Senate Governmental Affairs Committee\'s opening hearing into the Enron bankruptcy, as identified by the photo\'s source; Wikimedia Commons dates it January 24, 2002.'),
("Coordinator item 4: one Watkins-letter phrase (card F-004)", 4,
 'She was responding to a request for questions for an all-employee meeting set for August 16.{{B-055}}',
 'She was responding to a request for questions for an all-employee meeting set for August 16.{{B-055}} The letter, reprinted in full as an appendix to the Senate subcommittee staff report, says: "I am incredibly nervous that we will implode in a wave of accounting scandals."{{F-004@p. 57, Appendix 2, letter to Kenneth Lay (page image)#61}} (This is the letter\'s own wording. The staff report\'s quotation of the same sentence elsewhere differs slightly.)'),
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
    out = ['', '', '# Round 3', '',
           'Fixes required by `work/facts/factcheck-round3-partA.md`, plus the optional ch4 caption refinement and the '
           'coordinator\'s optional item 4 (one Watkins-letter phrase). Applied by `work/drafts/story-src/apply_round3.py`; '
           '`expand.py` now also reads `work/facts/reader-followup.json` so F-cards can be cited.',
           '',
           'Watkins phrase: I quote the letter itself as printed in the Senate subcommittee staff report, Appendix 2 '
           '(printed p. 57, PDF 61, page image), per card F-004. I did not use the report\'s own quotation '
           '("a wave accounting scandals", card F-002), which the Fact-Checker confirmed is a misquote. The phrase is '
           'identical in the House hearing reprint (hrg-hec-collapse-pt4, tab 14), per F-004; the shorter "Rex Rogers" '
           'version is not the one quoted.',
           '']
    for fid, ch, old, new in F:
        out += [f'## {fid} (ch{ch})', '', '**Old:**', '', '> ' + strip(old), '', '**New:**', '', '> ' + strip(new), '']
    with open(os.path.join(ROOT, 'work', 'facts', 'fixes-round2-chapters.md'), 'a') as fh:
        fh.write('\n'.join(out))
    print(f'applied {len(F)} edits')


main()
