#!/usr/bin/env python3
"""Smoke-test the static site with Playwright + the pre-installed Chromium.

Loads every page over file:// at desktop (1440x900), projector (1920x1080)
and phone (390x844) sizes; reports console errors, page errors and horizontal
overflow; saves screenshots to work/screens/. Also runs a few interaction
checks (citation notes, glossary pop-up, footnote keyboard stepping,
presentation and theme toggles, timeline filter).

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
VIEWPORTS = {"desktop": (1440, 900), "projector": (1920, 1080), "phone": (390, 844)}
SHOT_PAGES = {"index.html", "chapters/ch1.html", "chapters/ch3.html", "cast.html", "timeline.html",
              "footnote.html", "how-built.html", "sources.html", "glossary.html"}


def chromium_path():
    base = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    hits = sorted(glob.glob(f"{base}/chromium-*/chrome-linux/chrome"))
    return hits[-1] if hits else None


def url(p):
    return (ROOT / p).as_uri()


def main():
    SHOTS.mkdir(parents=True, exist_ok=True)
    problems, notes = [], []
    missing_optional = not (ROOT / "images" / "credits.js").exists()
    with sync_playwright() as pw:
        exe = chromium_path()
        browser = pw.chromium.launch(executable_path=exe) if exe else pw.chromium.launch()
        for vname, (w, h) in VIEWPORTS.items():
            for scheme in (["light", "dark"] if vname == "desktop" else ["light"]):
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
                    if p in SHOT_PAGES:
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
        page.locator('#tl-filters button[data-tag="law"]').click()
        vis = page.locator(".tl-item:not([hidden])").count()
        notes.append(f"timeline filter 'law': {vis} visible items")
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
    for n in notes:
        print("NOTE", n)
    for pr in problems:
        print("PROBLEM", pr)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
