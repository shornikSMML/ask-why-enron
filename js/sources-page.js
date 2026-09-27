/* Sources page: lists window.SOURCES grouped by folder, with fingerprints. */
(function () {
  "use strict";
  var A = window.AskWhy, esc = A.esc;
  var host = document.getElementById("source-list");
  if (!host) return;
  var FOLDERS = {
    "01-internal-investigation": "Enron's own board investigation",
    "02-bankruptcy-examiner": "The bankruptcy examiner's reports",
    "03-sec-filings": "Enron's filings with the SEC",
    "04-sec-enforcement": "SEC enforcement cases",
    "05-hearings-enron": "Congressional hearings on Enron",
    "06-congressional-reports": "Congressional reports",
    "07-sox-legislative-history": "How the Sarbanes-Oxley Act was made",
    "08-sox-law-pcaob-profession": "The Sarbanes-Oxley Act, the PCAOB, and the accounting profession",
    "09-courts-doj": "Courts and the Justice Department",
    "candidates": "Added after review: documents the Source Scout found, approved by the owner"
  };
  var S = window.SOURCES || {};
  var groups = {};
  Object.keys(S).forEach(function (id) { var s = S[id]; (groups[s.folder] = groups[s.folder] || []).push(s); });
  var folders = Object.keys(groups).sort();
  var count = Object.keys(S).length, have = 0;
  Object.keys(S).forEach(function (id) { if (S[id].in_library) have++; });
  var summary = document.getElementById("source-count");
  if (summary) summary.textContent = have + " documents in the library (" + count + " listed; " + (count - have) + " known gaps).";

  host.innerHTML = folders.map(function (f) {
    var items = groups[f].sort(function (a, b) { return String(a.date).localeCompare(String(b.date)); });
    return '<section><h2 id="' + esc(f) + '">' + esc(FOLDERS[f] || f) + ' <span class="eyebrow" style="display:block;text-transform:none;letter-spacing:0">sources/' + esc(f) + "/</span></h2>" +
      '<ul class="src-list">' + items.map(function (s) {
        var href = A.sourceHref(s.id);
        return '<li class="src-item" id="src-' + esc(s.id) + '">' +
          "<h3>" + (href ? '<a href="' + esc(href) + '" target="_blank" rel="noopener">' + esc(s.title) + "</a>" : esc(s.title)) + "</h3>" +
          '<div class="meta">' + esc(s.date) + " · " + esc(s.source_body) + " · id <code>" + esc(s.id) + "</code>" +
          (s.url ? ' · <a href="' + esc(s.url) + '" target="_blank" rel="noopener">original web address</a>' : "") + "</div>" +
          (s.in_library
            ? '<span class="sha" title="SHA-256 fingerprint">SHA-256: ' + esc(s.sha256) + "</span>"
            : '<span class="meta"><strong>Not in the library</strong> (known gap; not used by the site).</span>') +
          "</li>";
      }).join("") + "</ul></section>";
  }).join("");
})();
