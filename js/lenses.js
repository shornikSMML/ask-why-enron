/* Lenses (Phase 2): read a chapter through one lens at a time.
   Data: window.LENSES (js/lenses-data.js, from work/drafts/lenses.json):
     { "ch3": { "money": { notes: [{para_index, para_start, text, cites:[{card, source_id, page, loc}]}],
                           summary: ["..."], ask_why: "..." },
                "knew":  { ..., strip: [{date, who|person, what, cites|cite}] } } }
   Paragraph matching: para_index counts the chapter's <p> elements from 1, skipping
   the dek and the Ask Why box (work/drafts/lens-requests.md); the paragraph must start
   with para_start. Other numberings and a unique text match are accepted with a
   console warning. Unmatched notes are reported in window.AskWhy.lensReport and by
   work/tools/test_site.py. Summary bullets and strip entries may be strings or
   {text, cites} / {date, who, what, cites}; a top-level "_meta" key is ignored.
   State: ?lens=money in the URL, remembered per browser. Keys: 1-4 choose, 0 turns off. */
(function () {
  "use strict";
  var A = window.AskWhy;
  if (!A) return;
  var esc = A.esc;
  var body = document.body;
  var html = document.documentElement;

  var LENSES = [
    { id: "money", key: "1", name: "Follow the Money", short: "Money", blurb: "Where the cash came from, where it went, and how it was reported." },
    { id: "auditors", key: "2", name: "The Auditors", short: "Auditors", blurb: "What the outside auditors saw, said and did." },
    { id: "board", key: "3", name: "The Board", short: "Board", blurb: "What Enron's board of directors approved, asked and was told." },
    { id: "knew", key: "4", name: "Who Knew What, When", short: "Who knew", blurb: "What the documents show each person or body knew or was told, and when." }
  ];
  var BY_ID = {};
  LENSES.forEach(function (l) { BY_ID[l.id] = l; });
  var STORE_KEY = "askwhy-lens";

  var chapterN = parseInt(body.getAttribute("data-chapter"), 10);
  var isChapter = body.getAttribute("data-page") === "chapter" && !!chapterN;
  var data = (window.LENSES || {})["ch" + chapterN] || {};
  var sample = !!window.LENSES_SAMPLE;
  var current = null;
  var report = { chapter: chapterN, lenses: {} };

  /* ---------- the chapter's paragraphs (computed once, before anything is inserted) ---------- */
  function contentParagraphs() {
    var art = document.getElementById("chapter");
    if (!art) return [];
    var inside = false, out = [];
    var walker = document.createTreeWalker(art, NodeFilter.SHOW_COMMENT | NodeFilter.SHOW_ELEMENT);
    var node;
    while ((node = walker.nextNode())) {
      if (node.nodeType === 8) {
        if (/CONTENT START/.test(node.nodeValue)) inside = true;
        else if (/CONTENT END/.test(node.nodeValue)) inside = false;
      } else if (inside && node.tagName === "P") out.push(node);
    }
    return out;
  }
  var PARAS = [];
  function norm(s) {
    return String(s || "").toLowerCase().replace(/[‘’“”"'`]/g, "").replace(/[^a-z0-9$%.]+/g, " ").replace(/\s+/g, " ").trim();
  }
  function paraText(p) {
    // text without citation numbers
    var clone = p.cloneNode(true);
    Array.prototype.forEach.call(clone.querySelectorAll("a.cite, .lens-mark"), function (e) { e.remove(); });
    return clone.textContent;
  }
  function startsWith(p, start) {
    var a = norm(paraText(p)), b = norm(start);
    if (!b) return false;
    return a.indexOf(b) === 0 || a.indexOf(b.split(" ").slice(0, 6).join(" ")) === 0;
  }
  // Convention (work/drafts/lens-requests.md): para_index counts the chapter's <p>
  // elements from 1, skipping <p class="dek"> and any <p> inside <aside class="ask-why">.
  // Other conventions (0-based, dek included) are tried next, then a unique text match.
  function matchParagraph(note) {
    var idx = parseInt(note.para_index, 10);
    var body = PARAS.filter(function (p) { return !p.classList.contains("dek") && !p.closest("aside.ask-why"); });
    if (!isNaN(idx) && body[idx - 1] && startsWith(body[idx - 1], note.para_start)) return { p: body[idx - 1], how: "index" };
    var noDek = PARAS.filter(function (p) { return !p.classList.contains("dek"); });
    var tries = isNaN(idx) ? [] : [body[idx], PARAS[idx], PARAS[idx - 1], noDek[idx], noDek[idx - 1]];
    for (var i = 0; i < tries.length; i++) if (tries[i] && startsWith(tries[i], note.para_start)) return { p: tries[i], how: "other-index" };
    var hits = PARAS.filter(function (p) { return startsWith(p, note.para_start); });
    if (hits.length === 1) return { p: hits[0], how: "text" };
    return { p: null, how: hits.length > 1 ? "ambiguous" : "none" };
  }

  /* ---------- rendering helpers ---------- */
  function refs(cites) {
    cites = cites || [];
    if (!Array.isArray(cites)) cites = [cites];
    if (!cites.length) return "";
    return '<span class="lens-src">' + cites.map(function (c) {
      return A.sourceRefHTML({ source_id: c.source_id, pdf_page: c.pdf_page != null ? c.pdf_page : c.page, loc: c.loc, card: c.card })
        .replace('<span class="loc">', ' <span class="loc">');
    }).join("; ") + "</span>";
  }
  var MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  function fmtDate(d) {
    var m = /^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?$/.exec(String(d || "").trim());
    if (!m) return String(d || "");
    if (!m[2]) return m[1];
    var mon = MONTHS[parseInt(m[2], 10) - 1] || m[2];
    return m[3] ? mon + " " + parseInt(m[3], 10) + ", " + m[1] : mon + " " + m[1];
  }
  function noteBody(n) { return "<p>" + esc(n.text || "") + "</p>" + (refs(n.cites) ? "<p class=\"lens-src-line\">Source: " + refs(n.cites) + "</p>" : ""); }

  var inserted = [];
  function clear() {
    inserted.forEach(function (el) { if (el.parentNode) el.parentNode.removeChild(el); });
    inserted = [];
    Array.prototype.forEach.call(document.querySelectorAll(".lens-hit, .lens-noted"), function (p) { p.classList.remove("lens-hit", "lens-noted"); });
  }
  function add(el, parent, before) {
    parent.insertBefore(el, before || null);
    inserted.push(el);
    return el;
  }

  function render(lensId) {
    clear();
    var L = BY_ID[lensId];
    if (!L) return 0;
    var d = data[lensId] || {};
    var hits = document.querySelectorAll('#chapter [data-lens~="' + lensId + '"]');
    Array.prototype.forEach.call(hits, function (p) { p.classList.add("lens-hit"); });

    var col = document.querySelector(".margin-notes");
    var rep = report.lenses[lensId] = { notes: (d.notes || []).length, matched: 0, unmatched: [], untagged: [], byText: [] };
    (d.notes || []).forEach(function (n, i) {
      var m = matchParagraph(n);
      var label = "note " + (i + 1) + " (" + (n.para_key || "para_index " + n.para_index) + ': "' + String(n.para_start || "").slice(0, 40) + '")';
      if (!m.p) {
        rep.unmatched.push(label + " — " + m.how);
        console.warn("Lens " + lensId + ": could not match " + label);
        return;
      }
      rep.matched++;
      if (m.how !== "index") { rep.byText.push(label + " — " + m.how); console.warn("Lens " + lensId + ": para_index does not follow the agreed count (" + m.how + "): " + label); }
      if (!(" " + (m.p.getAttribute("data-lens") || "") + " ").match(new RegExp(" " + lensId + " "))) {
        rep.untagged.push(label);
        console.warn("Lens " + lensId + ": note is on a paragraph not tagged " + lensId + ": " + label);
      }
      m.p.classList.add("lens-noted");
      var k = i + 1;
      // inline mark (tap target on phones; highlights the margin note on wide screens)
      var mark = document.createElement("button");
      mark.type = "button";
      mark.className = "lens-mark";
      mark.setAttribute("data-lens-note", k);
      mark.setAttribute("aria-label", L.name + " note " + k);
      mark.setAttribute("aria-haspopup", "dialog");
      mark.innerHTML = '<span aria-hidden="true">' + esc(L.short) + " " + k + "</span>";
      add(mark, m.p);
      // margin note (wide screens)
      var note = null;
      if (col) {
        note = document.createElement("div");
        note.className = "note lens-note";
        note.id = "lnote-" + k;
        note._anchor = m.p;
        note.innerHTML = '<span class="lens-tag">' + esc(L.name) + " · " + k + "</span>" + noteBody(n);
        add(note, col);
      }
      // print copy, right after the paragraph (only the active lens is ever rendered)
      var pr = document.createElement("aside");
      pr.className = "lens-print";
      pr.innerHTML = '<span class="lens-tag">' + esc(L.name) + " · " + k + "</span>" + noteBody(n);
      add(pr, m.p.parentNode, m.p.nextSibling);

      var on = function () { mark.classList.add("is-active"); if (note) note.classList.add("is-active"); };
      var off = function () { mark.classList.remove("is-active"); if (note) note.classList.remove("is-active"); };
      mark.addEventListener("mouseenter", on); mark.addEventListener("mouseleave", off);
      mark.addEventListener("focus", on); mark.addEventListener("blur", off);
      if (note) { note.addEventListener("mouseenter", on); note.addEventListener("mouseleave", off); }
      mark.addEventListener("click", function (e) {
        e.preventDefault();
        if (A.wideEnoughForMargins() && note) { on(); note.scrollIntoView({ block: "nearest" }); return; }
        A.openPopover(mark, esc(L.name) + " · note " + k, '<div class="note-body">' + noteBody(n) + "</div>");
      });
    });

    // Who Knew What, When: dated strip at the top of the chapter
    var strip = d.strip || [];
    if (lensId === "knew") {
      var sec = document.createElement("section");
      sec.className = "knew-strip";
      sec.setAttribute("aria-label", "Who knew what, when, in this chapter");
      sec.innerHTML = "<h2>Who knew what, when</h2>" + (strip.length ? '<ol>' + strip.map(function (s) {
        return '<li><span class="k-date"><time datetime="' + esc(s.date || "") + '">' + esc(fmtDate(s.date)) + "</time></span>" + '</span><span class="k-who">' + esc(s.who || s.person || s.body || "") + "</span>" +
          '<span class="k-what">' + esc(s.what || s.text || "") + "</span>" + (refs(s.cites || s.cite) ? '<span class="k-src">' + refs(s.cites || s.cite) + "</span>" : "") + "</li>";
      }).join("") + "</ol>" : '<p class="none">No dated entries for this chapter.</p>');
      var dek = document.querySelector("#chapter .dek") || document.querySelector("#chapter h1");
      add(sec, dek.parentNode, dek.nextSibling);
    }

    // Summary and lens Ask Why at the end of the chapter
    var host = document.querySelector("#chapter [data-endnotes]") || document.querySelector("#chapter .chapter-nav");
    if (host && ((d.summary || []).length || d.ask_why)) {
      var sum = document.createElement("section");
      sum.className = "lens-summary";
      sum.setAttribute("aria-labelledby", "lens-sum-h");
      sum.innerHTML = '<h2 id="lens-sum-h">Through the lens: ' + esc(L.name) + "</h2>" +
        ((d.summary || []).length ? "<ul>" + d.summary.map(function (b) { return "<li>" + esc(typeof b === "string" ? b : b.text || "") + (typeof b === "object" && b.cites ? " " + refs(b.cites) : "") + "</li>"; }).join("") + "</ul>" : "") +
        (d.ask_why ? '<aside class="ask-why lens-ask"><h2>Ask Why · ' + esc(L.name) + "</h2><p>" + esc(d.ask_why) + "</p></aside>" : "");
      add(sum, host.parentNode, host);
    }

    rep.highlighted = hits.length;
    A.layoutMarginNotes();
    return hits.length;
  }

  /* ---------- lens bar ---------- */
  var bar, status;
  function buildBar() {
    var eyebrow = document.querySelector("#chapter .eyebrow");
    if (!eyebrow) return;
    bar = document.createElement("div");
    bar.className = "lens-bar";
    bar.setAttribute("role", "group");
    bar.setAttribute("aria-label", "Read this chapter through a lens");
    bar.innerHTML = '<span class="lens-label">Read through a lens</span>' +
      '<div class="lens-btns">' +
      '<button type="button" class="lens-btn" data-lens-btn="" aria-pressed="true" title="Key 0">Off</button>' +
      LENSES.map(function (l) {
        return '<button type="button" class="lens-btn" data-lens-btn="' + l.id + '" aria-pressed="false" title="Key ' + l.key + '">' + esc(l.name) + "</button>";
      }).join("") + "</div>" +
      '<p class="lens-status" aria-live="polite"></p>' +
      (sample ? '<p class="lens-sample"><span class="sample-flag phase2-sample">Sample lens data</span> Layout test only; the real lens notes are being written.</p>' : "");
    eyebrow.parentNode.insertBefore(bar, eyebrow.nextSibling);
    status = bar.querySelector(".lens-status");
    bar.addEventListener("click", function (e) {
      var b = e.target.closest("[data-lens-btn]");
      if (b) setLens(b.getAttribute("data-lens-btn") || null, true);
    });
  }
  function updateBar() {
    if (!bar) return;
    Array.prototype.forEach.call(bar.querySelectorAll("[data-lens-btn]"), function (b) {
      b.setAttribute("aria-pressed", (b.getAttribute("data-lens-btn") || null) === current ? "true" : "false");
    });
    var L = BY_ID[current];
    if (!L) { status.innerHTML = "Keys <kbd>1</kbd>&ndash;<kbd>4</kbd> choose a lens; <kbd>0</kbd> turns it off."; return; }
    var r = report.lenses[current] || {};
    status.innerHTML = "<strong>" + esc(L.name) + ".</strong> " + esc(L.blurb) + " " +
      (r.highlighted ? r.highlighted + " highlighted paragraph" + (r.highlighted === 1 ? "" : "s") : "No paragraphs in this chapter are marked for this lens") +
      (r.matched ? ", " + r.matched + " note" + (r.matched === 1 ? "" : "s") : "") + ".";
  }

  /* ---------- state: URL, storage ---------- */
  function urlLens() {
    var m = /[?&]lens=([a-z]+)/.exec(location.search);
    return m ? (m[1] === "off" ? "" : m[1]) : null;
  }
  function writeUrl() {
    try {
      var u = new URL(location.href);
      if (current) u.searchParams.set("lens", current); else u.searchParams.delete("lens");
      history.replaceState(history.state, "", u.pathname + (u.search ? u.search : "") + u.hash);
    } catch (e) { /* file:// quirks: state still applies */ }
  }
  function setLens(name, fromUser) {
    name = BY_ID[name] ? name : null;
    current = name;
    if (name) html.setAttribute("data-lens", name); else html.removeAttribute("data-lens");
    A.closePopover(false);
    var n = render(name);
    if (!name) clear();
    updateBar();
    if (fromUser) { A.store(STORE_KEY, name || null); writeUrl(); }
    A.layoutMarginNotes();
    return name ? n : 0;
  }

  function init() {
    if (!isChapter) return;
    PARAS = contentParagraphs();
    report.paragraphs = PARAS.length;
    buildBar();
    var fromUrl = urlLens();
    var start = fromUrl !== null ? fromUrl : A.store(STORE_KEY);
    setLens(start || null, false);
    if (fromUrl !== null) writeUrl();
    document.addEventListener("keydown", function (e) {
      if (A.isTyping(e)) return;
      if (e.key === "0") { setLens(null, true); e.preventDefault(); return; }
      for (var i = 0; i < LENSES.length; i++) if (e.key === LENSES[i].key) { setLens(LENSES[i].id, true); e.preventDefault(); return; }
    });
    window.addEventListener("beforeprint", function () { A.layoutMarginNotes(); });
  }

  // Public API
  function applyLens(name) { return setLens(name || null, true); }
  window.applyLens = applyLens;
  A.applyLens = applyLens;
  A.LENSES = LENSES;
  A.lensReport = report;
  A.currentLens = function () { return current; };
  A.checkAllLenses = function () {
    // used by the tests: render each lens once and return the full report
    var keep = current;
    LENSES.forEach(function (l) { setLens(l.id, false); });
    setLens(keep, false);
    return report;
  };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
