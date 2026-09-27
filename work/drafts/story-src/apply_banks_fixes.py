#!/usr/bin/env python3
"""Fixes to banks.src.html from work/facts/factcheck-phase2-banks-page.md.
Run with --cards to apply only the K-061/K-062 repoints (must-fix #1, #2).
Without it, applies the text fixes (#3, #4, #5, #7, #8 and notes #6, #9, #10).
Old text must occur exactly once. Appends old/new to work/facts/fixes-phase2-banks.md.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

TEXT = [
("#3 (must-fix): Ask Why states the SEC's allegation correctly",
 'Citigroup said it relied on Arthur Andersen\'s review, and Merrill Lynch, the SEC alleged, relied on Enron\'s word that Andersen had approved the accounting. When a deal',
 'Citigroup said it relied on Arthur Andersen\'s review. Merrill Lynch, the SEC alleged, had Enron sign a letter saying Andersen had approved the accounting, without ever speaking to Andersen itself. When a deal'),
("#5 (should-fix): 'assured us' attributed to the internal Merrill document; #4 (should-fix): Fastow guarantee paraphrased, not quoted",
 'The SEC alleged that in December 1999 Merrill bought an interest in Nigerian barges owned by Enron after Enron "assured us that we will be taken out of our investment within six months,"{{K-019}} and that Fastow said "this guarantee could not be in writing as it would defeat Enron\'s ability to recognize a gain on the sale."{{K-020}}',
 'The SEC alleged that in December 1999 Merrill bought an interest in Nigerian barges owned by Enron after, according to an internal Merrill document the SEC quoted, Enron had "assured us that we will be taken out of our investment within six months."{{K-019}} The SEC also alleged that Fastow told Merrill\'s bankers the guarantee could not be put in writing, because that would stop Enron from recognizing a gain on the sale.{{K-020}}'),
("#6 (note): the complaint's alternative return figure",
 'the SEC\'s complaint says 22.5 percent a year,{{K-019}}',
 'the SEC\'s complaint says 22.5 percent a year (or $250,000 plus 15 percent),{{K-019}}'),
("#7 (should-fix): Furst and Tilney met the staff voluntarily first",
 'Two Merrill bankers, Robert Furst and Schuyler Tilney, were sworn at a July 2002 Senate hearing and declined to answer questions, invoking their Fifth Amendment right.',
 'Two Merrill bankers, Robert Furst and Schuyler Tilney, had met voluntarily with the Senate staff. Sworn at a July 2002 hearing, they declined to answer questions after learning that one of the deals was under Justice Department investigation, invoking their Fifth Amendment right.'),
("#8 (should-fix): the cash flow is Roach's simplified version",
 'Chase sent cash to Mahonia, Mahonia paid Enron, and Enron\'s later "deliveries" flowed back to Chase with interest built in.{{K-002}}',
 'In what he called a simplified version, Chase sent cash to Mahonia, Mahonia paid Enron, and Enron\'s later "deliveries" flowed back to Chase with interest built in.{{K-002}}'),
("#10 (note): the RBS banker's indictment",
 'Absence from the library does not prove that no action was taken.',
 'The examiner did note that one RBS banker was indicted in 2002 on allegations about a separate LJM1-related sale; the outcome is not in the library.{{K-053}} Absence from the library does not prove that no action was taken.'),
]

CARDS = [
("#1 (must-fix): $4.7 billion cited to its own card K-061",
 '{{K-004!batson-final-app-g@p. 62#64}}', '{{K-061}}'),
("#2 (must-fix): Senate staff's 15 percent cited to its own card K-062",
 '{{K-019!rpt-psi-fishtail@p. 2, Introduction#6}}', '{{K-062}}'),
]


def main():
    cards_mode = '--cards' in sys.argv
    edits = CARDS if cards_mode else TEXT
    p = os.path.join(HERE, 'banks.src.html')
    t = open(p).read()
    for fid, old, new in edits:
        if t.count(old) != 1:
            print('NOT APPLIED', fid, t.count(old)); sys.exit(1)
        t = t.replace(old, new)
    if not cards_mode:
        # note #9: spelling used by the sources
        n = t.count('Toronto-Dominion')
        t = t.replace('Toronto-Dominion', 'Toronto Dominion')
        edits = edits + [("#9 (note): 'Toronto-Dominion' -> 'Toronto Dominion' (%d places, as the sources spell it)" % n,
                          'Toronto-Dominion', 'Toronto Dominion')]
    open(p, 'w').write(t)
    strip = lambda s: re.sub(r'\{\{([^}]*)\}\}', r'[cite \1]', s)
    fp = os.path.join(ROOT, 'work', 'facts', 'fixes-phase2-banks.md')
    head = [] if os.path.exists(fp) else ['# Fixes to "The Banks" page (Phase 2)', '']
    out = head + ['', '# Story Writer: %s' % ('citation repoints' if cards_mode else 'text fixes'), '',
                  'From `work/facts/factcheck-phase2-banks-page.md`. Edited `work/drafts/story-src/banks.src.html` '
                  '(script `apply_banks_fixes.py`), regenerated `work/drafts/banks.html`. `[cite CARD]` = citation built '
                  'from that card. Diagram items #11-#14 belong to the diagram owner and were not touched.', '']
    for fid, old, new in edits:
        out += ['## ' + fid, '', '**Old:**', '', '> ' + strip(old), '', '**New:**', '', '> ' + strip(new), '']
    open(fp, 'a').write('\n'.join(out) + '\n')
    print('applied', len(edits))


main()
