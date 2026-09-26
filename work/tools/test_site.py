#!/usr/bin/env python3
"""Smoke-test the static site with Playwright + the pre-installed Chromium.

Loads every page over file:// at desktop (1440x900), projector (1920x1080)
and phone (390x844) sizes; reports console errors, page errors and horizontal
overflow; saves screenshots to work/screens/. Also runs a few interaction
checks (citation notes, glossary pop-up, footnote keyboard stepping,
presentation and theme toggles, timeline filter).

Reference checks (on every page, as rendered):
  - every a.cite resolves to a source in window.SOURCES that is in the library;
  - every .term resolves to a window.GLOSSARY entry;
  - every figure[data-image] resolves to a window.IMAGE_CREDITS entry;
  - every citation link target, image and narrow image file exists on disk;
  - no leftover placeholders or "Sample" flags.
Diagram checks: the phone uses the -narrow SVG; the manual dark theme reaches
the SVG diagrams even when the system setting is light.

Run:  PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers python3 work/tools/test_site.py
"""
import glob
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
SHOTS = ROOT / "work" / "screens"
PAGES = ["index.html"] + [f"chapters/ch{i}.html" for i in range(1, 8)] + [
    "cast.html", "timeline.html", "glossary.html", "footnote.html", "how-built.html", "sources.html", "credits.html"]
VIEWPORTS = {"desktop": (1440, 900), "projector": (1920, 1080), "phone": (390, 844), "small": (360, 740)}
SHOT_PAGES = set(PAGES)  # every page, every viewport, light and dark (the 360px size is checked but not photographed)
LEFTOVER_RE = r"\[[^\]]*\bcoming\]|SAMPLE|TODO|\[Draft"

REF_JS = """(LEFTOVER) => {
  const S = window.SOURCES || {}, G = window.GLOSSARY || {}, C = window.IMAGE_CREDITS || [];
  const ids = new Set(C.map(c => c.id));
  const bad = [];
  const links = new Set();
  document.querySelectorAll('a.cite').forEach(a => {
    const id = a.getAttribute('data-src'), s = S[id];
    if (!s) bad.push('cite ' + (a.getAttribute('data-n') || '?') + ': unknown source id "' + id + '"');
    else if (!s.in_library) bad.push('cite ' + a.getAttribute('data-n') + ': source "' + id + '" not in library');
  });
  document.querySelectorAll('.term[data-term]').forEach(t => {
    const id = t.getAttribute('data-term');
    if (!G[id]) bad.push('term "' + id + '" not in GLOSSARY');
  });
  document.querySelectorAll('figure[data-image]').forEach(f => {
    const id = f.getAttribute('data-image');
    if (!ids.has(id)) bad.push('figure "' + id + '" not in IMAGE_CREDITS');
  });
  document.querySelectorAll('.placeholder, .sample-flag, .figure-missing').forEach(e => {
    bad.push('leftover placeholder: ' + (e.textContent || '').trim().slice(0, 60));
  });
  const txt = document.body.innerText;
  const m = txt.match(new RegExp(LEFTOVER, 'g'));
  if (m) bad.push('leftover placeholder text: ' + [...new Set(m)].join(', '));
  if (!document.querySelector('footer.site-footer')) bad.push('no site footer');
  // No link, image or script may point into sources/candidates/ (not part of the library).
  document.querySelectorAll('[href], [src], [srcset]').forEach(e => {
    const v = e.getAttribute('href') || e.getAttribute('src') || e.getAttribute('srcset') || '';
    if (/sources\/candidates\//.test(v)) bad.push('links into sources/candidates/: ' + v);
  });
  // Every link to a local file must exist (checked on disk by Python); same-page #anchors must exist.
  document.querySelectorAll('a[href]').forEach(a => {
    if (a.protocol !== 'file:') return;
    const raw = a.getAttribute('href');
    if (raw.startsWith('#')) {
      const id = decodeURIComponent(raw.slice(1));
      if (id && !document.getElementById(id)) bad.push('broken same-page link: ' + raw);
      return;
    }
    links.add(decodeURIComponent(a.pathname));
  });
  document.querySelectorAll('.endnotes li a[href], .anno-panel a[href], .fn-source a[href]').forEach(a => {
    if (a.protocol === 'file:' && a.pathname.indexOf('/sources/') !== -1) links.add(decodeURIComponent(a.pathname));
  });
  document.querySelectorAll('img[src], source[srcset]').forEach(e => {
    const u = new URL(e.getAttribute('src') || e.getAttribute('srcset'), location.href);
    if (u.protocol === 'file:') links.add(decodeURIComponent(u.pathname));
  });
  return {bad, files: [...links], cites: document.querySelectorAll('a.cite').length,
          terms: document.querySelectorAll('.term[data-term]').length, figures: document.querySelectorAll('figure[data-image]').length};
}"""


def footnote_all_cite_links(page):
    """The footnote's source links live in annotation panels that open one at a time: open each."""
    files = set()
    n = page.locator("mark.anno").count()
    for i in range(n):
        page.locator("mark.anno").nth(i).click()
        for href in page.evaluate("""() => [...document.querySelectorAll('#anno-panel a[href]')]
                .filter(a => a.protocol === 'file:' && a.pathname.indexOf('/sources/') !== -1)
                .map(a => decodeURIComponent(a.pathname))"""):
            files.add(href)
    return n, files


def chromium_path():
    base = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    hits = sorted(glob.glob(f"{base}/chromium-*/chrome-linux/chrome"))
    return hits[-1] if hits else None


def url(p):
    return (ROOT / p).as_uri()


def main():
    SHOTS.mkdir(parents=True, exist_ok=True)
    problems, notes = [], []
    ref_totals = {}
    missing_optional = not (ROOT / "images" / "credits.js").exists()
    with sync_playwright() as pw:
        exe = chromium_path()
        browser = pw.chromium.launch(executable_path=exe) if exe else pw.chromium.launch()
        for vname, (w, h) in VIEWPORTS.items():
            for scheme in ["light", "dark"]:
                ctx = browser.new_context(viewport={"width": w, "height": h}, color_scheme=scheme)
                for p in PAGES:
                    page = ctx.new_page()
                    errs = []
                    page.on("console", lambda m, errs=errs: errs.append(m.text) if m.type == "error" else None)
                    page.on("pageerror", lambda e, errs=errs: errs.append("pageerror: " + str(e)))
                    page.goto(url(p))
                    page.wait_for_timeout(250)
                    for e in errs:
                        if missing_optional and "ERR_FILE_NOT_FOUND" in e:
                            continue  # images/credits.js not delivered yet (Image agent)
                        problems.append(f"[{vname}/{scheme}] {p}: console error: {e}")
                    ov = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
                    if ov > 0:
                        problems.append(f"[{vname}/{scheme}] {p}: horizontal overflow {ov}px")
                    if vname == "desktop" and scheme == "light":
                        ref = page.evaluate(REF_JS, LEFTOVER_RE)
                        ref_totals[p] = ref
                        for b in ref["bad"]:
                            problems.append(f"[refs] {p}: {b}")
                        for f in ref["files"]:
                            if not Path(f).exists():
                                problems.append(f"[refs] {p}: link target missing on disk: {f}")
                    if p in SHOT_PAGES and vname != "small":
                        name = p.replace("/", "-").replace(".html", "")
                        page.screenshot(path=str(SHOTS / f"{vname}-{scheme}-{name}.png"), full_page=(vname == "phone" or p in {"chapters/ch1.html", "footnote.html"}))
                    page.close()
                ctx.close()

        # ---- interaction checks ----
        ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        page = ctx.new_page()
        page.goto(url("chapters/ch1.html"))
        page.wait_for_timeout(300)
        n_cites = page.locator("a.cite[data-n]").count()
        n_margin = page.locator(".margin-notes .note").count()
        n_end = page.locator(".endnotes li").count()
        notes.append(f"ch1 desktop: {n_cites} cites, {n_margin} margin notes, {n_end} endnotes")
        if not (n_cites == n_margin == n_end and n_cites > 0):
            problems.append("ch1: cite/note counts differ")
        overlap = page.evaluate("""() => { const ns=[...document.querySelectorAll('.margin-notes .note')].map(n=>n.getBoundingClientRect());
            for (let i=1;i<ns.length;i++) if (ns[i].top < ns[i-1].bottom) return true; return false; }""")
        if overlap:
            problems.append("ch1: margin notes overlap")
        page.locator(".term").first.click()
        if not page.locator("#popover").is_visible():
            problems.append("ch1: glossary pop-up did not open")
        page.keyboard.press("Escape")
        page.locator("#present-toggle").click()
        page.wait_for_timeout(200)
        fs = page.evaluate("getComputedStyle(document.documentElement).fontSize")
        notes.append(f"presentation mode root font-size: {fs}")
        page.screenshot(path=str(SHOTS / "desktop-light-ch1-presentation.png"))
        page.reload(); page.wait_for_timeout(200)
        if "present" not in (page.evaluate("document.documentElement.className") or ""):
            problems.append("presentation mode not remembered after reload")
        page.locator("#present-toggle").click()
        page.locator("#theme-toggle").click()
        if page.evaluate("document.documentElement.getAttribute('data-theme')") != "dark":
            problems.append("theme toggle did not switch to dark")
        page.screenshot(path=str(SHOTS / "desktop-manualdark-ch1.png"))
        page.locator("#theme-toggle").click()
        page.keyboard.press("ArrowRight"); page.wait_for_load_state(); page.wait_for_timeout(150)
        if not page.url.endswith("ch2.html"):
            problems.append("ArrowRight did not go to chapter 2: " + page.url)
        page.keyboard.press("ArrowLeft"); page.wait_for_load_state(); page.wait_for_timeout(150)
        if not page.url.endswith("ch1.html"):
            problems.append("ArrowLeft did not return to chapter 1")

        page.goto(url("footnote.html")); page.wait_for_timeout(200)
        page.keyboard.press("j"); page.keyboard.press("j")
        t = page.locator("#anno-panel h2").inner_text()
        if t != "Annotation 2":
            problems.append("footnote j/j gave: " + t)
        page.keyboard.press("k")
        if page.locator("#anno-panel h2").inner_text() != "Annotation 1":
            problems.append("footnote k did not step back")
        page.screenshot(path=str(SHOTS / "desktop-light-footnote-active.png"))

        page.goto(url("timeline.html")); page.wait_for_timeout(200)
        page.locator('#tl-filters button[data-tag="legal"]').click()
        vis = page.locator(".tl-item:not([hidden])").count()
        notes.append(f"timeline filter 'legal': {vis} visible items")
        if vis == 0:
            problems.append("timeline filter 'legal' shows no items")

        page.goto(url("footnote.html")); page.wait_for_timeout(200)
        n_anno, fn_files = footnote_all_cite_links(page)
        notes.append(f"footnote: {n_anno} annotations opened, {len(fn_files)} distinct source files linked")
        for f in sorted(fn_files):
            if not Path(f).exists():
                problems.append(f"[refs] footnote annotation link target missing on disk: {f}")

        # Manual dark theme with a LIGHT system setting: the SVG diagrams must switch too.
        page.goto(url("chapters/ch3.html")); page.wait_for_timeout(200)
        page.evaluate("localStorage.removeItem('askwhy-theme')")
        fig = page.locator('figure[data-image="diagram-raptor"] img')
        fig.scroll_into_view_if_needed(); page.wait_for_timeout(300)
        def diagram_corner_brightness():
            box = fig.bounding_box()
            png = page.screenshot(clip={"x": box["x"] + 4, "y": box["y"] + 4, "width": 6, "height": 6})
            from io import BytesIO
            from PIL import Image
            px = Image.open(BytesIO(png)).convert("L").getpixel((3, 3))
            return px
        light_px = diagram_corner_brightness()
        page.locator("#theme-toggle").click(); page.wait_for_timeout(300)
        dark_px = diagram_corner_brightness()
        page.screenshot(path=str(SHOTS / "desktop-manualdark-ch3-raptor.png"))
        notes.append(f"diagram background brightness: light theme {light_px}, manual dark theme {dark_px}")
        if not (light_px > 200 and dark_px < 60):
            problems.append(f"diagram did not follow the manual theme toggle (light {light_px}, dark {dark_px})")
        page.locator("#theme-toggle").click()
        page.evaluate("localStorage.removeItem('askwhy-theme')")
        ctx.close()

        ctx = browser.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True)
        page = ctx.new_page()
        page.goto(url("chapters/ch1.html")); page.wait_for_timeout(200)
        page.locator("a.cite").first.click()
        if not page.locator("#popover").is_visible():
            problems.append("phone: citation tap did not open note")
        page.screenshot(path=str(SHOTS / "phone-light-ch1-note-open.png"))
        page.goto(url("footnote.html")); page.wait_for_timeout(200)
        page.locator("mark.anno").first.click(); page.wait_for_timeout(350)
        page.screenshot(path=str(SHOTS / "phone-light-footnote-sheet.png"))
        if not page.evaluate("document.getElementById('anno-panel').classList.contains('open')"):
            problems.append("phone: footnote bottom sheet did not open")
        page.goto(url("chapters/ch3.html")); page.wait_for_timeout(200)
        for fid in ("diagram-spe-basic", "diagram-chewco-ljm", "diagram-raptor"):
            loc = page.locator(f'figure[data-image="{fid}"] img')
            loc.scroll_into_view_if_needed(); page.wait_for_timeout(200)
            cur = loc.evaluate("i => i.currentSrc")
            if "-narrow.svg" not in cur:
                problems.append(f"phone: {fid} did not use its narrow version ({cur})")
        page.locator('figure[data-image="diagram-raptor"]').screenshot(path=str(SHOTS / "phone-light-ch3-raptor.png"))
        page.goto(url("index.html")); page.locator(".menu-toggle").click(); page.wait_for_timeout(100)
        page.screenshot(path=str(SHOTS / "phone-light-menu-open.png"))
        ov = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
        if ov > 0:
            problems.append(f"phone menu open: overflow {ov}px")
        ctx.close()

        ctx = browser.new_context(viewport={"width": 360, "height": 740})
        for p in PAGES:
            page = ctx.new_page(); page.goto(url(p)); page.wait_for_timeout(150)
            ov = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
            if ov > 0:
                problems.append(f"[360px] {p}: horizontal overflow {ov}px")
            page.close()
        ctx.close()
        pdf_page = browser.new_page()
        pdf_page.goto(url("chapters/ch1.html")); pdf_page.wait_for_timeout(200)
        pdf_page.emulate_media(media="print")
        pdf_page.screenshot(path=str(SHOTS / "print-ch1.png"), full_page=True)
        browser.close()

    if missing_optional:
        notes.append("images/credits.js does not exist yet; its file-not-found message was ignored.")
    for p, r in ref_totals.items():
        if r["cites"] or r["terms"] or r["figures"]:
            notes.append(f"refs {p}: {r['cites']} cites, {r['terms']} terms, {r['figures']} figures, {len(r['files'])} linked files checked")
    for n in notes:
        print("NOTE", n)
    for pr in problems:
        print("PROBLEM", pr)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
