"""Turn each library PDF/HTML into page-marked text in work/text/<manifest id>.txt.
Originals in sources/ are never modified. Pages with no text layer are flagged for OCR."""
import csv, subprocess, sys, os, html, re
out = 'work/text'
for r in csv.DictReader(open('sources/manifest.csv')):
    p = os.path.join('sources', r['folder'], r['filename'])
    if not os.path.exists(p): continue
    dst = os.path.join(out, r['id'] + '.txt')
    if os.path.exists(dst): continue
    if p.endswith('.pdf'):
        t = subprocess.run(['pdftotext', '-layout', p, '-'], capture_output=True, text=True).stdout
        pages = t.split('\f')
        body = ''.join(f'\n=== PAGE {i+1} ===\n{pg}' for i, pg in enumerate(pages) if i < len(pages)-1 or pg.strip())
    elif p.endswith(('.htm', '.html')):
        raw = open(p, encoding='utf-8', errors='replace').read()
        raw = re.sub(r'(?is)<(script|style).*?</\1>', '', raw)
        body = html.unescape(re.sub(r'<[^>]+>', ' ', raw))
        body = re.sub(r'[ \t]+', ' ', body); body = re.sub(r'\n\s*\n+', '\n\n', body)
    else:
        continue  # .txt sources are read directly
    open(dst, 'w').write(body)
    chars = len(re.sub(r'\s|=== PAGE \d+ ===', '', body))
    print(f"{r['id']}\t{chars}")
