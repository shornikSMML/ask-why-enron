"""Render HTML candidate documents to PDF so the owner can review them as readable pages.
Review copies only: the originals in sources/ are untouched and remain the files that get fingerprinted."""
import sys, pathlib
from playwright.sync_api import sync_playwright
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    pg = b.new_page()
    pg.route("**/*", lambda r: r.continue_() if r.request.url.startswith("file:") else r.abort())  # no web fetches
    for f in sorted(src.glob("*.htm*")):
        pg.goto(f.resolve().as_uri(), wait_until="load")
        dst = out / (f.stem + ".pdf")
        pg.pdf(path=str(dst), format="Letter", print_background=True, margin={"top":"0.5in","bottom":"0.5in","left":"0.5in","right":"0.5in"})
        print(dst.name, pg.evaluate("document.body.innerText.length"))
    b.close()
