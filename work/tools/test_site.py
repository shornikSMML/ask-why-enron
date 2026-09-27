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
  - every link into sources/ points to a file listed in sources/manifest.csv;
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
    "cast.html", "timeline.html", "glossary.html", "footnote.html", "how-built.html", "sources.html", "credits.html",
    "pathways.html", "pathway-handout.html?path=first-reading", "why-it-matters.html", "banks.html"]
LENS_IDS = ["money", "auditors", "board", "knew"]
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
  // Placeholder sections of the new Phase 2 page shells and the flags on SAMPLE lens and
  // pathway data are expected until the writers deliver; they are reported as notes.
  const pending = [];
  document.querySelectorAll('.placeholder, .sample-flag, .figure-missing').forEach(e => {
    const t = (e.textContent || '').trim().slice(0, 60);
    if (e.matches('.shell-placeholder, .phase2-sample')) pending.push(t);
    else bad.push('leftover placeholder: ' + t);
  });
  const txt = document.body.innerText;
  const m = txt.match(new RegExp(LEFTOVER, 'g'));
  if (m) bad.push('leftover placeholder text: ' + [...new Set(m)].join(', '));
  if (!document.querySelector('footer.site-footer')) bad.push('no site footer');
  // Every link, image or script pointing into sources/ is collected; Python checks each
  // against sources/manifest.csv (a listed file is fine wherever it lives).
  const srcLinks = new Set();
  document.querySelectorAll('[href], [src], [srcset]').forEach(e => {
    const v = e.getAttribute('href') || e.getAttribute('src') || e.getAttribute('srcset') || '';
    let u; try { u = new URL(v, location.href); } catch (err) { return; }
    if (u.protocol === 'file:' && u.pathname.indexOf('/sources/') !== -1) srcLinks.add(decodeURIComponent(u.pathname));
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
  return {bad, pending, files: [...links], srcLinks: [...srcLinks], cites: document.querySelectorAll('a.cite').length,
          terms: document.querySelectorAll('.term[data-term]').length, figures: document.querySelectorAll('figure[data-image]').length};
}"""


def manifest_files():
    """Paths (relative to sources/) of every file listed in sources/manifest.csv."""
    import csv
    with (ROOT / "sources" / "manifest.csv").open(newline="", encoding="utf-8") as f:
        return {f"{r['folder']}/{r['filename']}" for r in csv.DictReader(f) if r.get("id")}


def unlisted_source(path, listed):
    """Return the sources/-relative path if it is not a manifest file, else None."""
    rel = Path(path).resolve()
    try:
        rel = rel.relative_to((ROOT / "sources").resolve()).as_posix()
    except ValueError:
        return None
    return None if rel in listed else rel


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
    """file:// URL for a site path that may carry ?query and #hash."""
    import re as _re
    m = _re.match(r"([^?#]*)(.*)", p)
    return (ROOT / m.group(1)).as_uri() + m.group(2)


def shot_name(p):
    import re as _re
    return _re.sub(r"[^A-Za-z0-9_-]+", "-", p.replace(".html", "")).strip("-")


def phase2_tests(browser, problems, notes):
    """Lenses on every chapter, keyboard shortcuts, and every pathway stop."""
    # --- lenses: matching, highlight, overlap (desktop); overflow (360px) ---
    ctx = browser.new_context(viewport={"width": 1440, "height": 900})
    page = ctx.new_page()
    errs = []
    page.on("pageerror", lambda e: errs.append(str(e)))
    sample = None
    for n in range(1, 8):
        page.goto(url(f"chapters/ch{n}.html?lens=off")); page.wait_for_timeout(200)
        if sample is None:
            sample = page.evaluate("!!window.LENSES_SAMPLE")
        rep = page.evaluate("AskWhy.checkAllLenses()")
        tot = {"notes": 0, "matched": 0}
        for lens, r in rep["lenses"].items():
            tot["notes"] += r["notes"]; tot["matched"] += r["matched"]
            for u in r["unmatched"]:
                problems.append(f"[lens] ch{n} {lens}: note does not match a paragraph: {u}")
            for u in r["untagged"]:
                problems.append(f"[lens] ch{n} {lens}: note is on a paragraph not tagged data-lens={lens}: {u}")
            for u in r["byText"]:
                problems.append(f"[lens] ch{n} {lens}: para_index does not follow the agreed count: {u}")
        notes.append(f"lens ch{n}: {rep['paragraphs']} paragraphs, {tot['matched']}/{tot['notes']} notes matched")
        for lens in LENS_IDS:
            page.evaluate(f"applyLens('{lens}')"); page.wait_for_timeout(80)
            hl = page.locator("p.lens-hit").count()
            tagged = page.locator(f'#chapter p[data-lens~="{lens}"]').count()
            if hl != tagged:
                problems.append(f"[lens] ch{n} {lens}: {hl} highlighted but {tagged} tagged")
            ov = page.evaluate("""() => { const ns=[...document.querySelectorAll('.margin-notes .note')].filter(n=>n.style.display!=='none').map(n=>n.getBoundingClientRect()).sort((a,b)=>a.top-b.top);
                for (let i=1;i<ns.length;i++) if (ns[i].top < ns[i-1].bottom - 1) return true; return false; }""")
            if ov:
                problems.append(f"[lens] ch{n} {lens}: margin notes overlap")
            if lens == "knew" and page.locator(".knew-strip").count() != 1:
                problems.append(f"[lens] ch{n}: Who Knew What, When strip missing")
            if n == 3:
                page.screenshot(path=str(SHOTS / f"desktop-light-ch3-lens-{lens}.png"))
        page.evaluate("applyLens(null)")
    if sample:
        notes.append("lenses: running on SAMPLE data (work/drafts/lenses.json not delivered yet)")
    # print view with a lens on: only that lens's notes
    page.goto(url("chapters/ch3.html?lens=money")); page.wait_for_timeout(200)
    page.emulate_media(media="print")
    vis = page.evaluate("[...document.querySelectorAll('.lens-print')].filter(e=>getComputedStyle(e).display!=='none').length")
    other = page.evaluate("[...document.querySelectorAll('.lens-print .lens-tag')].filter(e=>!/Follow the Money/.test(e.textContent)).length")
    notes.append(f"print ch3 money lens: {vis} lens notes printed")
    if other:
        problems.append("print: notes from another lens are printed")
    page.screenshot(path=str(SHOTS / "print-ch3-lens-money.png"), full_page=True)
    page.emulate_media(media="screen")
    # keyboard shortcuts
    page.goto(url("chapters/ch3.html?lens=off")); page.wait_for_timeout(200)
    for key, want in (("1", "money"), ("2", "auditors"), ("3", "board"), ("4", "knew"), ("0", None)):
        page.keyboard.press(key); page.wait_for_timeout(80)
        got = page.evaluate("document.documentElement.getAttribute('data-lens')")
        in_url = page.evaluate("new URLSearchParams(location.search).get('lens')")
        if got != want or in_url != want:
            problems.append(f"[keys] key {key}: lens {got!r}, URL lens {in_url!r}, expected {want!r}")
    # remembered per browser
    page.keyboard.press("3"); page.goto(url("chapters/ch4.html")); page.wait_for_timeout(200)
    if page.evaluate("document.documentElement.getAttribute('data-lens')") != "board":
        problems.append("[keys] lens not remembered on the next chapter")
    page.keyboard.press("0")
    # presentation mode with a lens
    page.goto(url("chapters/ch3.html?lens=money")); page.wait_for_timeout(150)
    page.locator("#present-toggle").click(); page.wait_for_timeout(200)
    page.screenshot(path=str(SHOTS / "desktop-light-ch3-lens-money-presentation.png"))
    page.locator("#present-toggle").click()
    if errs:
        problems.extend("[lens] page error: " + e for e in errs)
    ctx.close()

    # dark theme with a lens
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, color_scheme="dark")
    page = ctx.new_page(); page.goto(url("chapters/ch5.html?lens=knew")); page.wait_for_timeout(250)
    page.screenshot(path=str(SHOTS / "desktop-dark-ch5-lens-knew.png"))
    ctx.close()

    # 360 px and phone: each lens on each chapter, no sideways scrolling; tap a lens note
    ctx = browser.new_context(viewport={"width": 360, "height": 740}, has_touch=True, is_mobile=True)
    page = ctx.new_page()
    for n in range(1, 8):
        for lens in LENS_IDS:
            page.goto(url(f"chapters/ch{n}.html?lens={lens}")); page.wait_for_timeout(120)
            ov = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
            if ov > 0:
                problems.append(f"[360px] ch{n} lens {lens}: horizontal overflow {ov}px")
    page.goto(url("chapters/ch3.html?lens=money")); page.wait_for_timeout(200)
    if page.locator(".lens-mark").count():
        page.locator(".lens-mark").first.click(); page.wait_for_timeout(150)
        if not page.locator("#popover").is_visible():
            problems.append("phone: lens note did not open when tapped")
        page.screenshot(path=str(SHOTS / "phone-light-ch3-lens-note-open.png"))
    page.goto(url("chapters/ch3.html?lens=knew")); page.wait_for_timeout(200)
    page.screenshot(path=str(SHOTS / "phone-light-ch3-lens-knew.png"), full_page=False)
    ctx.close()

    # --- pathways: every stop resolves to an existing page and anchor ---
    ctx = browser.new_context(viewport={"width": 1440, "height": 900})
    page = ctx.new_page()
    page.goto(url("pathways.html")); page.wait_for_timeout(150)
    paths = page.evaluate("AskWhy.pathways.list().map(p => ({id: p.id, n: (p.stops||[]).length, stops: (p.stops||[]).map(s => ({page: s.page, anchor: s.anchor, fallback: s.fallback || null}))}))")
    psample = page.evaluate("!!window.PATHWAYS_SAMPLE")
    notes.append(f"pathways: {len(paths)} ({'SAMPLE data' if psample else 'from work/drafts/pathways.json'}): " + ", ".join(f"{p['id']} ({p['n']} stops)" for p in paths))
    import re as _re
    def stop_url(pid, i, st):
        pg = st.get("page") or "index.html"
        a = (st.get("anchor") or "").lstrip("#")
        return url(pg + ("&" if "?" in pg else "?") + f"path={pid}&stop={i}" + (f"#{a}" if a else ""))
    shots = 0
    used_fallback = []
    for pw_ in paths:
        for i, st in enumerate(pw_["stops"], 1):
            pg = (st["page"] or "").split("#")[0]
            file_part = pg.split("?")[0]
            if not (ROOT / file_part).exists():
                problems.append(f"[pathway] {pw_['id']} stop {i}: page {file_part} does not exist")
                continue
            page.goto(stop_url(pw_["id"], i, st)); page.wait_for_timeout(150)
            page.wait_for_load_state(); page.wait_for_timeout(100)   # a fallback redirect may have happened
            if page.locator(".pathway-bar .pw-count").count() != 1:
                problems.append(f"[pathway] {pw_['id']} stop {i}: pathway bar missing on {pg}")
            anchor = (st.get("anchor") or "").lstrip("#")
            r = page.evaluate("AskWhy.pathwayStop || null")
            if anchor:
                if not r or not r.get("resolved"):
                    problems.append(f"[pathway] {pw_['id']} stop {i}: #{anchor} not found on {file_part}" + (" (nor its fallback)" if st.get("fallback") else ""))
                else:
                    hidden = page.evaluate("""(id) => { const t = document.getElementById(id), h = document.querySelector('.site-header');
                        const hb = getComputedStyle(h).position === 'sticky' ? h.getBoundingClientRect().bottom : 0;
                        return t.getBoundingClientRect().top < hb - 1; }""", r["resolved"])
                    if hidden and r["resolved"] not in ("chapter",):
                        problems.append(f"[pathway] {pw_['id']} stop {i}: #{r['resolved']} is hidden under the header after the jump")
                if r and r.get("resolved") and r.get("fallback"):
                    used_fallback.append(f"{pw_['id']} stop {i}: {file_part}#{anchor} -> fallback #{r['resolved']}")
            here = page.url
            m = _re.search(r"[?&]lens=([a-z]+)", here)
            if m and page.evaluate("document.documentElement.getAttribute('data-lens')") != m.group(1):
                problems.append(f"[pathway] {pw_['id']} stop {i}: lens {m.group(1)} not switched on")
            m = _re.search(r"[?&]tag=([a-z-]+)", here)
            if m and page.locator('#tl-filters button[aria-pressed="true"]').get_attribute("data-tag") != m.group(1):
                problems.append(f"[pathway] {pw_['id']} stop {i}: timeline tag {m.group(1)} not applied")
            if i == 1 or (shots < 5 and file_part in ("cast.html", "timeline.html", "footnote.html", "banks.html", "why-it-matters.html", "glossary.html")):
                page.screenshot(path=str(SHOTS / f"desktop-light-pathway-{pw_['id']}-stop{i}.png"))
                if i != 1:
                    shots += 1
    # anchors promised in work/drafts/pathway-anchor-requests.md, even if no pathway uses them yet
    page.goto(url("timeline.html")); page.wait_for_timeout(150)
    for tid in ("tl-2001-10-lockdown", "tl-2001-10-special-committee", "tl-1992"):
        if not page.locator(f"#{tid}").count():
            problems.append(f"[anchors] timeline.html#{tid} missing")
    page.goto(url("footnote.html#fn-06")); page.wait_for_timeout(200)
    if page.locator("#anno-panel .phrase").count() == 0 or "fn-06" not in (page.evaluate("document.querySelector('mark.anno.is-active') && document.querySelector('mark.anno.is-active').id") or ""):
        problems.append("[anchors] footnote.html#fn-06 did not open annotation fn-06")
    for n in range(1, 8):
        page.goto(url(f"chapters/ch{n}.html")); page.wait_for_timeout(100)
        auto = page.evaluate("[...document.querySelectorAll('#chapter h2')].filter(h=>!h.closest('aside.ask-why')).map(h=>h.id)")
        if not page.locator("#ask-why").count():
            problems.append(f"[anchors] ch{n}: #ask-why missing")
        notes.append(f"anchors ch{n}: " + " ".join("#" + a for a in auto))
    for f in used_fallback:
        notes.append("pathway stop uses its fallback (main section not written yet): " + f)
    page.goto(url("pathways.html")); page.wait_for_timeout(150)
    page.screenshot(path=str(SHOTS / "desktop-light-pathways.png"), full_page=True)
    if paths:
        page.goto(url(f"pathway-handout.html?path={paths[0]['id']}")); page.wait_for_timeout(150)
        page.emulate_media(media="print")
        page.screenshot(path=str(SHOTS / "print-pathway-handout.png"), full_page=True)
        page.emulate_media(media="screen")
    ctx.close()
    ctx = browser.new_context(viewport={"width": 390, "height": 844}, has_touch=True, is_mobile=True)
    page = ctx.new_page()
    if paths and paths[0]["n"] > 1:
        page.goto(url("pathways.html")); page.wait_for_timeout(100)
        page.goto(stop_url(paths[0]["id"], 2, paths[0]["stops"][1])); page.wait_for_timeout(250)
        page.screenshot(path=str(SHOTS / "phone-light-pathway-bar.png"))
        ov = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
        if ov > 0:
            problems.append(f"phone: pathway page overflow {ov}px")
    ctx.close()


def main():
    SHOTS.mkdir(parents=True, exist_ok=True)
    problems, notes = [], []
    ref_totals = {}
    listed = manifest_files()
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
                        if ref["pending"]:
                            # page shells and SAMPLE Phase 2 data: a note while content is being
                            # written (ASKWHY_ALLOW_PENDING=1), otherwise a problem.
                            msg = f"{p}: {len(ref['pending'])}x placeholder/sample: " + "; ".join(sorted(set(ref["pending"])))
                            (notes if os.environ.get("ASKWHY_ALLOW_PENDING") else problems).append(msg)
                        for f in ref["files"]:
                            if not Path(f).exists():
                                problems.append(f"[refs] {p}: link target missing on disk: {f}")
                        for f in ref["srcLinks"]:
                            u = unlisted_source(f, listed)
                            if u:
                                problems.append(f"[refs] {p}: links to sources/{u}, which is not listed in sources/manifest.csv")
                    if p in SHOT_PAGES and vname != "small":
                        name = shot_name(p)
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

        page.goto(url("sources.html")); page.wait_for_timeout(200)
        n_src = page.locator(".src-item").count()
        notes.append(f"sources page: {n_src} documents listed; manifest has {len(listed)} rows")
        if n_src != len(listed):
            problems.append(f"sources page lists {n_src} documents, manifest has {len(listed)}")

        page.goto(url("footnote.html")); page.wait_for_timeout(200)
        n_anno, fn_files = footnote_all_cite_links(page)
        notes.append(f"footnote: {n_anno} annotations opened, {len(fn_files)} distinct source files linked")
        for f in sorted(fn_files):
            if not Path(f).exists():
                problems.append(f"[refs] footnote annotation link target missing on disk: {f}")
            u = unlisted_source(f, listed)
            if u:
                problems.append(f"[refs] footnote annotation links to sources/{u}, which is not listed in sources/manifest.csv")

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
        phase2_tests(browser, problems, notes)
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
