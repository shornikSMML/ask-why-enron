#!/usr/bin/env python3
"""Expand {{CARD(!src)?(@loc)?(#page)?}} markers into site citation anchors.

Card data (source_id, pdf_page, locator) come from work/facts/*.json.
data-page is filled only for PDF sources (per manifest file extension).
Validates: card exists, card checked OK/FIXED, source id in manifest.
"""
import csv, html, json, re, sys, os

ROOT = '/home/user/enron-dryrun'
cards = {}
for f in ['reader-a', 'reader-b', 'reader-c', 'reader-followup']:
    for c in json.load(open(f'{ROOT}/work/facts/{f}.json')):
        cards[c['id']] = c
manifest = {r['id']: r for r in csv.DictReader(open(f'{ROOT}/sources/manifest.csv'))}

PAT = re.compile(r'\{\{([A-CF]-\d{3})(?:!([a-z0-9-]+))?(?:@([^#}]+))?(?:#(\d+))?\}\}')
errors = []
used = []


def default_loc(c):
    l = c['locator']
    parts = []
    pp = l.get('printed_page')
    if pp:
        pp = str(pp)
        parts.append(pp if re.match(r'^(p|pp|para|Syllabus|CRS|Summary|Highlights|116)', pp) else 'p. ' + pp)
    sec = (l.get('section') or '').strip()
    if sec:
        if parts and sec.split()[0].rstrip(',;') == parts[0].split()[0].rstrip(',;'):
            parts = [sec]
        else:
            parts.append(sec)
    src = c['source_id']
    is_pdf = manifest.get(src, {}).get('filename', '').lower().endswith('.pdf')
    lines = str(l.get('lines') or '')
    is_txt = manifest.get(src, {}).get('filename', '').lower().endswith('.txt')
    if is_txt and re.match(r'^~?\d[\d\-, ~]*$', lines) and 'line' not in ', '.join(parts):
        parts.append('lines ' + lines.replace('~', 'about '))
    return ', '.join(parts)


def repl(m):
    cid, src, loc, page = m.groups()
    c = cards.get(cid)
    if not c:
        errors.append(f'unknown card {cid}')
        return m.group(0)
    if c.get('checked') not in ('OK', 'FIXED'):
        errors.append(f'card {cid} not OK/FIXED: {c.get("checked")}')
    src = src or c['source_id']
    if src not in manifest:
        errors.append(f'{cid}: source {src} not in manifest')
    is_pdf = manifest.get(src, {}).get('filename', '').lower().endswith('.pdf')
    if page is None and src == c['source_id'] and loc is None:
        page = c['locator'].get('pdf_page')
    elif page is None and src == c['source_id']:
        page = c['locator'].get('pdf_page')
    if not is_pdf:
        page = ''
    loc = (loc or default_loc(c)).strip()
    used.append(cid)
    return ('<a class="cite" data-src="%s" data-page="%s" data-loc="%s" data-card="%s">source</a>'
            % (src, '' if page in (None, '') else page, html.escape(loc, quote=True), cid))


def main():
    srcdir, outdir = sys.argv[1], sys.argv[2]
    for n in range(1, 8):
        p = os.path.join(srcdir, f'ch{n}.src.html')
        if not os.path.exists(p):
            continue
        txt = open(p).read()
        before = len(used)
        out = PAT.sub(repl, txt)
        left = re.findall(r'\{\{[^}]*\}\}', out)
        if left:
            errors.append(f'ch{n}: unexpanded markers {left}')
        open(os.path.join(outdir, f'ch{n}.html'), 'w').write(out)
        body = re.sub(r'<[^>]+>', ' ', re.sub(r'<a class="cite".*?</a>', '', out))
        words = len(re.findall(r"[A-Za-z0-9$%.,'’-]+", body))
        print(f'ch{n}: {len(used)-before} cites, ~{words} words')
    print('cards used:', len(set(used)))
    if errors:
        print('ERRORS:')
        for e in errors:
            print(' ', e)
        sys.exit(1)


main()
