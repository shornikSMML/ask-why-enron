"""
download_sources.py  -  fetch every document listed in manifest.csv

HOW TO RUN (from inside the sources/ folder):
    python download_sources.py

WHAT IT DOES, IN PLAIN ENGLISH
  1. Reads manifest.csv, one row per document.
  2. Skips rows marked "not-online" (e.g., Batson reports that must come from PACER).
  3. Skips any file you already have, so it is safe to run again.
  4. Downloads each file into its folder (01-internal-investigation, 02-..., etc.).
  5. Checks that a ".pdf" really is a PDF. Government sites sometimes send back
     an error page instead of the file; those get flagged "CHECK".
  6. Writes download_log.csv: what arrived, its size, and a SHA-256 "fingerprint".
     If anyone later edits a file, its fingerprint changes, and that shows the file
     is no longer the original.

ONE THING TO EDIT BEFORE RUNNING
  sec.gov blocks downloads that don't identify who is asking. Put your name and
  email in CONTACT below. The SEC asks for this; it is not sent anywhere else.
  (If you run this through GitHub Actions, you type it into a box instead and
  don't need to edit this file.)

FILE SIZE LIMIT
  GitHub refuses files over 100 MB. Anything bigger is deleted after download
  and logged as TOO BIG, so it never breaks the upload.
"""

import csv
import os
import hashlib
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

CONTACT = os.environ.get("SEC_CONTACT") or "Your Name your.email@example.edu"   # <-- EDIT THIS LINE
PAUSE_SECONDS = 1.5                             # be polite to government servers
MAX_MB = 95                                     # GitHub hard limit is 100 MB

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "manifest.csv"
LOG = HERE / "download_log.csv"


def fingerprint(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def looks_wrong(path):
    """Return a warning if the file isn't what its name says it is."""
    head = path.read_bytes()[:1024].lstrip().lower()
    if path.suffix.lower() == ".pdf" and not head.startswith(b"%pdf"):
        return "named .pdf but is not a PDF (probably an error page)"
    if path.stat().st_size < 2000:
        return "very small file - open it and check"
    return ""


def main():
    if "example.edu" in CONTACT:
        print("Please edit the CONTACT line at the top of this script first.")
        return

    with open(MANIFEST, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    log = []
    for n, row in enumerate(rows, 1):
        label = f"[{n}/{len(rows)}] {row['id']}"
        dest = HERE / row["folder"] / row["filename"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        entry = {"id": row["id"], "file": f"{row['folder']}/{row['filename']}",
                 "result": "", "bytes": "", "sha256": "", "checked_at": "", "message": ""}

        if row["status"] == "not-online" or not row["url"].strip():
            entry["result"] = "SKIPPED"
            entry["message"] = "not available online - see notes in manifest"
            print(f"{label}: skipped (not online)")
        elif dest.exists() and dest.stat().st_size > 0:
            entry["result"] = "ALREADY HAD"
            print(f"{label}: already downloaded")
        else:
            try:
                req = urllib.request.Request(row["url"], headers={"User-Agent": CONTACT})
                with urllib.request.urlopen(req, timeout=120) as resp:
                    dest.write_bytes(resp.read())
                entry["result"] = "OK"
                print(f"{label}: downloaded")
            except Exception as e:
                entry["result"] = "FAILED"
                entry["message"] = str(e)[:200]
                print(f"{label}: FAILED - {e}")
            time.sleep(PAUSE_SECONDS)

        if dest.exists() and dest.stat().st_size > MAX_MB * 1024 * 1024:
            size_mb = dest.stat().st_size / 1024 / 1024
            dest.unlink()
            entry["result"] = "TOO BIG"
            entry["message"] = f"{size_mb:.0f} MB is over GitHub's limit; keep this one outside the repo"
            print(f"{label}: too big for GitHub ({size_mb:.0f} MB), removed")

        if dest.exists() and dest.stat().st_size > 0:
            entry["bytes"] = dest.stat().st_size
            entry["sha256"] = fingerprint(dest)
            entry["checked_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
            warning = looks_wrong(dest)
            if warning:
                entry["result"] = "CHECK"
                entry["message"] = warning
        log.append(entry)

    with open(LOG, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(log[0].keys()))
        w.writeheader()
        w.writerows(log)

    counts = {}
    for e in log:
        counts[e["result"]] = counts.get(e["result"], 0) + 1
    print("\nSummary:", ", ".join(f"{k}: {v}" for k, v in counts.items()))
    print(f"Details saved to {LOG.name}. Look at any FAILED, CHECK, or TOO BIG rows.")


if __name__ == "__main__":
    main()
