/* Image credits page: one entry per image in window.IMAGE_CREDITS (images/credits.js),
   with a thumbnail, author, license, source link, where it appears on the site
   (window.IMAGE_USAGE, written by work/tools/integrate.py) and, for original
   diagrams, the fact cards it rests on. Each entry is an anchor: credits.html#img-ID. */
(function () {
  "use strict";
  var A = window.AskWhy, esc = A.esc;
  var host = document.getElementById("credits");
  if (!host) return;
  var list = window.IMAGE_CREDITS || [];
  var usage = window.IMAGE_USAGE || {};
  if (!list.length) { host.innerHTML = '<p class="placeholder">[Image credits coming]</p>'; return; }

  function link(url, text) {
    return url ? '<a href="' + esc(url) + '" target="_blank" rel="noopener">' + esc(text || url) + "</a>" : "";
  }
  function row(label, value) { return value ? "<dt>" + esc(label) + "</dt><dd>" + value + "</dd>" : ""; }

  var originals = list.filter(function (i) { return i.is_original_diagram; }).length;
  var html = '<p class="ui" style="font-size:.9rem;color:var(--muted)">' + list.length + " images: " +
    (list.length - originals) + " from public collections, " + originals + " original diagrams and charts drawn for this site.</p>";

  html += '<ol class="credit-list">' + list.map(function (img) {
    var src = A.imageSrc(img);
    var onLight = /\.svg$/i.test(img.file || "") && !img.is_original_diagram;
    var used = (usage[img.id] || []).map(function (u) {
      return '<a href="' + A.ROOT + esc(u.href) + '">' + esc(u.label) + "</a>";
    }).join(", ");
    var cards = (img.fact_cards || []).map(function (c) { return '<span class="chip">' + esc(c) + "</span>"; }).join("");
    var files = '<a href="' + esc(src) + '">' + esc(String(img.file || "").replace(/^images\//, "")) + "</a>" +
      (img.narrow_file ? ' (wide) · <a href="' + esc(A.imageSrc(img, "narrow_file")) + '">' + esc(String(img.narrow_file).replace(/^images\//, "")) + "</a> (phone)" : "");
    return '<li class="credit-item" id="img-' + esc(img.id) + '">' +
      '<a class="thumb' + (onLight ? " on-light" : "") + '" href="' + esc(src) + '"><img src="' + esc(src) + '" alt="' + esc(img.alt || img.title || "") + '" loading="lazy"></a>' +
      "<div><h2>" + esc(img.title || img.id) + "</h2>" +
      (img.description ? "<p>" + esc(img.description) + "</p>" : "") +
      "<dl>" +
      row("Author", img.is_original_diagram ? esc(img.author || "Original diagram for this site") : esc(img.author || "")) +
      row("License", img.license_url ? link(img.license_url, img.license) : esc(img.license || "")) +
      row("Source", img.source_url ? link(img.source_url, img.source_url.replace(/^https?:\/\//, "")) : (img.is_original_diagram ? "Drawn for this site" : "")) +
      row("Credit line", esc(img.credit_line || "")) +
      row("Based on fact cards", cards ? '<span class="card-ids">' + cards + "</span>" : (img.is_original_diagram ? "General explanation; no Enron-specific facts" : "")) +
      row("Shown on", used || "Not currently shown on a page") +
      row("File", files) +
      row("Fingerprint (SHA-256)", img.sha256 ? '<code style="font-size:.75rem">' + esc(img.sha256) + "</code>" : "") +
      "</dl></div></li>";
  }).join("") + "</ol>";

  html += '<p class="ui" style="font-size:.85rem;color:var(--muted);margin-top:1.5rem">Fact cards are the checked notes (one fact, one quotation, one source location) that the agents extracted from the source library. The original diagrams show only facts from cards the fact-checker approved.</p>';
  host.innerHTML = html;
  if (location.hash) { var t = document.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }
})();
