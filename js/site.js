/* Ask Why: The Rise and Fall of Enron — shared site code.
   Plain JavaScript, no libraries, no network requests. Data arrives through
   <script> files that set window.SOURCES, window.GLOSSARY, window.IMAGE_CREDITS,
   so every page works when opened straight from disk (file://).

   Page renderers (cast.js, timeline.js, footnote.js, how-built.js) load AFTER
   this file, build their HTML, and the shared enhancements below run on
   DOMContentLoaded, which fires after all of them. */
(function () {
  "use strict";

  var CHAPTERS = [
    { n: 1, title: "Origins" },
    { n: 2, title: "The Business Model and Mark-to-Market Accounting" },
    { n: 3, title: "The Special Purpose Entities" },
    { n: 4, title: "Warning Signs and the Whistleblower" },
    { n: 5, title: "The Collapse" },
    { n: 6, title: "Arthur Andersen" },
    { n: 7, title: "Aftermath and Reform" }
  ];

  var body = document.body;
  var ROOT = body.getAttribute("data-root") || "";
  var PAGE = body.getAttribute("data-page") || "";

  /* ---------- small helpers ---------- */
  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
  }
  function store(key, val) {
    try {
      if (val === undefined) return window.localStorage.getItem(key);
      if (val === null) window.localStorage.removeItem(key); else window.localStorage.setItem(key, val);
    } catch (e) { /* storage blocked: preferences just aren't remembered */ }
    return null;
  }
  function wideEnoughForMargins() {
    var col = document.querySelector(".margin-notes");
    return !!col && window.getComputedStyle(col).display !== "none";
  }
  function isNarrow() { return window.matchMedia("(max-width: 700px)").matches; }

  /* ---------- sources ---------- */
  function getSource(id) { return (window.SOURCES || {})[id] || null; }

  // URL of a library file, relative to the current page. PDF pages get #page=N.
  function sourceHref(id, page) {
    var s = getSource(id);
    if (!s || !s.in_library) return null;
    var href = ROOT + "sources/" + s.folder + "/" + s.filename;
    if (s.is_pdf && page) href += "#page=" + encodeURIComponent(page);
    return href;
  }

  // HTML for one source reference: title (linked to the file) + locator.
  // cite = {source_id, pdf_page, loc, quote, card}
  function sourceRefHTML(cite) {
    cite = cite || {};
    var s = getSource(cite.source_id);
    var title = s ? s.title : "[Unknown source id: " + cite.source_id + "]";
    if (!s) console.warn("Ask Why: unknown source id", cite.source_id);
    var href = sourceHref(cite.source_id, cite.pdf_page);
    var html = href
      ? '<a href="' + esc(href) + '" target="_blank" rel="noopener">' + esc(title) + "</a>"
      : "<span>" + esc(title) + (s && !s.in_library ? " (not in library)" : "") + "</span>";
    var loc = [];
    if (cite.loc) loc.push(esc(cite.loc));
    if (cite.pdf_page && s && s.is_pdf) loc.push("PDF page " + esc(cite.pdf_page));
    // A .txt source can name the PDF edition of the same document (pdf_source_id).
    if (cite.pdf_page && cite.pdf_source_id && !(s && s.is_pdf)) {
      var pdfHref = sourceHref(cite.pdf_source_id, cite.pdf_page);
      if (pdfHref) loc.push('<a href="' + esc(pdfHref) + '" target="_blank" rel="noopener">PDF edition, page ' + esc(cite.pdf_page) + "</a>");
    }
    if (loc.length) html += '<span class="loc">' + loc.join(" · ") + "</span>";
    if (cite.quote) html += '<span class="quote">“' + esc(cite.quote) + "”</span>";
    if (cite.card) html += ' <span class="card-id">' + esc(cite.card) + "</span>";
    return html;
  }

  // Build an <a class="cite"> string from a cite object (used by page renderers,
  // so cast/timeline cites become normal numbered notes).
  function citeTag(c) {
    c = c || {};
    return '<a class="cite" data-src="' + esc(c.source_id || c.src || "") + '" data-page="' +
      esc(c.pdf_page == null ? (c.page || "") : c.pdf_page) + '" data-loc="' + esc(c.loc || "") +
      '" data-card="' + esc(c.card || "") + '">source</a>';
  }

  /* ---------- popover (glossary terms; citations on small screens) ---------- */
  var pop, popTrigger;
  function ensurePopover() {
    if (pop) return pop;
    pop = document.createElement("div");
    pop.className = "popover";
    pop.id = "popover";
    pop.setAttribute("role", "dialog");
    pop.setAttribute("aria-modal", "false");
    pop.setAttribute("aria-labelledby", "popover-title");
    pop.hidden = true;
    document.body.appendChild(pop);
    document.addEventListener("click", function (e) {
      if (pop.hidden) return;
      if (pop.contains(e.target) || (popTrigger && popTrigger.contains(e.target))) return;
      closePopover(false);
    });
    return pop;
  }
  function openPopover(trigger, titleHTML, bodyHTML) {
    ensurePopover();
    popTrigger = trigger;
    pop.innerHTML = '<button class="close" type="button" aria-label="Close">×</button>' +
      '<h2 id="popover-title">' + titleHTML + "</h2>" + bodyHTML;
    pop.querySelector(".close").addEventListener("click", function () { closePopover(true); });
    pop.hidden = false;
    if (!isNarrow()) {
      var r = trigger.getBoundingClientRect();
      var w = pop.offsetWidth;
      var left = Math.min(Math.max(8, r.left + window.scrollX), window.scrollX + document.documentElement.clientWidth - w - 8);
      pop.style.left = left + "px";
      pop.style.top = (r.bottom + window.scrollY + 6) + "px";
    } else {
      pop.style.left = ""; pop.style.top = "";
    }
    trigger.setAttribute("aria-expanded", "true");
    pop.querySelector(".close").focus({ preventScroll: true });
  }
  function closePopover(returnFocus) {
    if (!pop || pop.hidden) return;
    pop.hidden = true;
    if (popTrigger) {
      popTrigger.setAttribute("aria-expanded", "false");
      if (returnFocus) popTrigger.focus();
    }
    popTrigger = null;
  }

  /* ---------- citations: numbering, margin notes, endnotes ---------- */
  function processCites(root) {
    var cites = Array.prototype.slice.call((root || document).querySelectorAll("a.cite:not([data-n])"));
    if (!cites.length) return;
    var start = document.querySelectorAll("a.cite[data-n]").length;
    var marginCol = document.querySelector(".margin-notes");
    var endList = document.querySelector(".endnotes ol");
    if (!endList) {
      var host = document.querySelector("[data-endnotes]") || document.querySelector("main .chapter-body") || document.querySelector("main .page") || document.querySelector("main");
      var det = document.createElement("details");
      det.className = "endnotes";
      det.innerHTML = "<summary>Sources for this page</summary><ol></ol>";
      host.appendChild(det);
      endList = det.querySelector("ol");
    }
    cites.forEach(function (a, i) {
      var n = start + i + 1;
      var c = { source_id: a.getAttribute("data-src"), pdf_page: a.getAttribute("data-page"), loc: a.getAttribute("data-loc"), card: a.getAttribute("data-card") };
      var ref = sourceRefHTML(c);
      a.setAttribute("data-n", n);
      a.id = a.id || "cite-" + n;
      a.textContent = n;
      a.href = "#endnote-" + n;
      a.setAttribute("aria-label", "Source note " + n);
      a.setAttribute("aria-haspopup", "dialog");

      var li = document.createElement("li");
      li.id = "endnote-" + n;
      li.innerHTML = ref + ' <a href="#' + a.id + '" aria-label="Back to text">↩</a>';
      endList.appendChild(li);

      if (marginCol) {
        var note = document.createElement("div");
        note.className = "note";
        note.id = "mnote-" + n;
        note.innerHTML = '<span class="n">' + n + "</span>" + ref;
        marginCol.appendChild(note);
        var on = function () { a.classList.add("is-active"); note.classList.add("is-active"); };
        var off = function () { a.classList.remove("is-active"); note.classList.remove("is-active"); };
        a.addEventListener("mouseenter", on); a.addEventListener("mouseleave", off);
        a.addEventListener("focus", on); a.addEventListener("blur", off);
        note.addEventListener("mouseenter", on); note.addEventListener("mouseleave", off);
      }

      a.addEventListener("click", function (e) {
        if (wideEnoughForMargins()) { e.preventDefault(); return; } // note already beside the text
        e.preventDefault();
        if (popTrigger === a && pop && !pop.hidden) { closePopover(true); return; }
        openPopover(a, "Source " + n, '<p class="note-body">' + ref.replace(/<span class="loc">/, '<br><span class="loc">') + "</p>");
      });
    });
    var sum = document.querySelector(".endnotes summary");
    if (sum) sum.textContent = "Sources for this page (" + endList.children.length + ")";
    layoutMarginNotes();
  }

  // Place each margin note level with its citation, pushing down to avoid overlap.
  // Place each margin note level with what it annotates (a citation mark, or for a
  // lens note its paragraph: note._anchor), pushing down to avoid overlap.
  function noteAnchor(note) {
    if (note._anchor) return note._anchor;
    var n = note.id.replace("mnote-", "");
    return document.querySelector('a.cite[data-n="' + n + '"]');
  }
  function layoutMarginNotes() {
    var col = document.querySelector(".margin-notes");
    if (!col) return;
    if (!wideEnoughForMargins()) { col.style.minHeight = ""; return; }
    var colTop = col.getBoundingClientRect().top;
    var lastBottom = 0;
    var items = [];
    Array.prototype.forEach.call(col.querySelectorAll(".note"), function (note, i) {
      var a = noteAnchor(note);
      if (!a || !a.isConnected) { note.style.display = "none"; return; }
      note.style.display = "";
      // lens notes sit beside the top of their paragraph and before same-height citations
      items.push({ note: note, top: a.getBoundingClientRect().top - colTop - 4, order: note._anchor ? 0 : 1, i: i });
    });
    items.sort(function (x, y) { return (x.top - y.top) || (x.order - y.order) || (x.i - y.i); });
    items.forEach(function (it) {
      var top = Math.max(it.top, lastBottom + 10);
      it.note.style.top = top + "px";
      lastBottom = top + it.note.offsetHeight;
    });
    col.style.minHeight = lastBottom + "px";
  }

  /* ---------- glossary terms ---------- */
  function processTerms(root) {
    var G = window.GLOSSARY || {};
    Array.prototype.forEach.call((root || document).querySelectorAll(".term[data-term]:not([data-ready])"), function (el) {
      el.setAttribute("data-ready", "1");
      el.setAttribute("role", "button");
      el.setAttribute("tabindex", "0");
      el.setAttribute("aria-haspopup", "dialog");
      el.setAttribute("aria-expanded", "false");
      var id = el.getAttribute("data-term");
      function show() {
        if (popTrigger === el && pop && !pop.hidden) { closePopover(true); return; }
        var g = G[id];
        var title = g ? esc(g.term || id) : esc(el.textContent);
        var def = g ? esc(g.short || g.definition || "") : '<span class="none">No definition found.</span>';
        openPopover(el, title, "<p>" + def + '</p><p><a href="' + ROOT + "glossary.html#" + encodeURIComponent(id) + '">Open in the glossary →</a></p>');
      }
      el.addEventListener("click", function (e) { e.preventDefault(); show(); });
      el.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") { e.preventDefault(); show(); }
      });
    });
  }

  /* ---------- figures from window.IMAGE_CREDITS ---------- */
  function findImage(id) {
    var list = window.IMAGE_CREDITS || [];
    for (var i = 0; i < list.length; i++) if (list[i].id === id) return list[i];
    return null;
  }
  function creditHTML(img) {
    var parts = [];
    var details = '<a href="' + ROOT + "credits.html#img-" + encodeURIComponent(img.id) + '">Image details</a>';
    if (img.is_original_diagram) {
      parts.push(esc(img.credit_line || "Original diagram for this site"));
      parts.push(details);
      return parts.join(" · ");
    }
    if (img.author) parts.push(esc(img.author));
    if (img.license) parts.push(img.license_url ? '<a href="' + esc(img.license_url) + '" target="_blank" rel="noopener">' + esc(img.license) + "</a>" : esc(img.license));
    if (img.source_url) parts.push('<a href="' + esc(img.source_url) + '" target="_blank" rel="noopener">Source</a>');
    return parts.length ? "Credit: " + parts.join(" · ") : "";
  }
  function imageSrc(img, key) {
    var f = String(img[key || "file"] || "");
    f = f.replace(/^\.?\//, "");
    if (f.indexOf("images/") !== 0) f = "images/" + f;
    return ROOT + f;
  }
  // Below this width the tall "-narrow" version of a diagram is shown.
  var NARROW_MEDIA = "(max-width: 640px)";
  function imageElement(img, alt) {
    var el = document.createElement("img");
    el.src = imageSrc(img);
    el.alt = alt;
    el.loading = "lazy";
    el.decoding = "async";
    el.addEventListener("load", layoutMarginNotes);
    if (!img.narrow_file) return el;
    var pic = document.createElement("picture");
    var source = document.createElement("source");
    source.media = NARROW_MEDIA;
    source.srcset = imageSrc(img, "narrow_file");
    pic.appendChild(source);
    pic.appendChild(el);
    return pic;
  }
  function processFigures(root) {
    Array.prototype.forEach.call((root || document).querySelectorAll("figure[data-image]:not([data-ready])"), function (fig) {
      fig.setAttribute("data-ready", "1");
      var id = fig.getAttribute("data-image");
      if (!fig.id && !document.getElementById("fig-" + id)) fig.id = "fig-" + id; // anchor: #fig-IMAGE_ID
      var img = findImage(id);
      var existing = fig.querySelector("figcaption");
      if (!img) {
        var ph = document.createElement("div");
        ph.className = "figure-missing";
        ph.textContent = "[Image coming: " + id + "]";
        fig.insertBefore(ph, fig.firstChild);
        return;
      }
      var el = imageElement(img, fig.getAttribute("data-alt") || img.alt || img.description || img.title || "");
      fig.classList.add(img.is_original_diagram ? "is-diagram" : "is-photo");
      if (/\.svg$/i.test(img.file || "") && !img.is_original_diagram) fig.classList.add("on-light");
      fig.insertBefore(el, fig.firstChild);
      var cap = existing || document.createElement("figcaption");
      if (!existing) {
        cap.innerHTML = esc(img.title || "");
        fig.appendChild(cap);
      }
      var credit = creditHTML(img);
      if (credit) cap.insertAdjacentHTML("beforeend", '<span class="credit">' + credit + "</span>");
    });
  }

  /* ---------- chapter navigation ---------- */
  function chapterHref(n) { return ROOT + "chapters/ch" + n + ".html"; }
  function buildChapterNav() {
    var n = parseInt(body.getAttribute("data-chapter"), 10);
    var host = document.querySelector("[data-chapter-nav]");
    if (!n || !host) return;
    var prev = CHAPTERS[n - 2], next = CHAPTERS[n];
    var html = "";
    if (prev) html += '<a class="prev" rel="prev" href="' + chapterHref(prev.n) + '"><span class="dir">← Chapter ' + prev.n + "</span>" + esc(prev.title) + "</a>";
    if (next) html += '<a class="next" rel="next" href="' + chapterHref(next.n) + '"><span class="dir">Chapter ' + next.n + " →</span>" + esc(next.title) + "</a>";
    host.innerHTML = html;
    var hint = document.createElement("p");
    hint.className = "key-hint";
    hint.textContent = "Tip: use the ← and → keys to move between chapters.";
    host.parentNode.insertBefore(hint, host.nextSibling);
  }
  function isTyping(e) {
    var t = e.target;
    return e.altKey || e.ctrlKey || e.metaKey || e.shiftKey ||
      (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)));
  }

  /* ---------- header: menu, theme, presentation ---------- */
  function setupHeader() {
    var menu = document.querySelector(".menu-toggle");
    var nav = document.querySelector(".site-nav");
    if (menu && nav) {
      menu.addEventListener("click", function () {
        var open = nav.classList.toggle("open");
        menu.setAttribute("aria-expanded", open ? "true" : "false");
      });
    }
    // mark current page in nav
    var here = location.pathname.split("/").pop() || "index.html";
    Array.prototype.forEach.call(document.querySelectorAll(".site-nav a"), function (a) {
      var target = a.getAttribute("href").split("/").pop();
      if (target === here || (PAGE === "chapter" && a.hasAttribute("data-story"))) a.setAttribute("aria-current", "page");
    });

    var html = document.documentElement;
    var themeBtn = document.getElementById("theme-toggle");
    function effectiveTheme() {
      var t = html.getAttribute("data-theme");
      if (t) return t;
      return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    }
    function labelTheme() {
      if (!themeBtn) return;
      var t = effectiveTheme();
      themeBtn.textContent = t === "dark" ? "Light" : "Dark";
      themeBtn.setAttribute("aria-label", "Switch to " + (t === "dark" ? "light" : "dark") + " theme");
    }
    if (themeBtn) {
      labelTheme();
      themeBtn.addEventListener("click", function () {
        var next = effectiveTheme() === "dark" ? "light" : "dark";
        html.setAttribute("data-theme", next);
        store("askwhy-theme", next);
        labelTheme();
      });
      try { window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", labelTheme); } catch (e) { /* old browsers */ }
    }

    var presBtn = document.getElementById("present-toggle");
    if (presBtn) {
      presBtn.setAttribute("aria-pressed", html.classList.contains("present") ? "true" : "false");
      presBtn.addEventListener("click", function () {
        var on = html.classList.toggle("present");
        presBtn.setAttribute("aria-pressed", on ? "true" : "false");
        store("askwhy-present", on ? "1" : null);
        closePopover(false);
        layoutMarginNotes();
      });
    }
  }

  /* ---------- lenses ---------- */
  // Fallback only. On chapter pages js/lenses.js replaces window.applyLens and
  // AskWhy.applyLens with the full version (bar, notes, summary, URL, keys).
  function applyLens(name) {
    var html = document.documentElement;
    if (!name) html.removeAttribute("data-lens"); else html.setAttribute("data-lens", name);
    return document.querySelectorAll(name ? '[data-lens~="' + name + '"]' : "[data-lens]").length;
  }

  /* ---------- anchors (for pathways and sharing) ---------- */
  // Fixed ids for chapter headings, agreed with the Pathways Designer
  // (work/drafts/pathway-anchor-requests.md). Keyed by the heading's text; pathways
  // depend on these exact ids. A heading not in the table gets an id from its text
  // ("The Raptors" -> #the-raptors) and a console note.
  var HEADING_IDS = {
   "ch1": {
    "Two pipeline companies": "two-pipeline-companies",
    "Kenneth Lay takes charge": "lay-takes-charge",
    "\"From the reservoir to the burner tip\"": "reservoir-to-burner-tip",
    "Growing fast": "growing-fast"
   },
   "ch2": {
    "A trader, not just a pipeline": "a-trader",
    "Revenue and profit": "revenue-and-profit",
    "What mark-to-market accounting means": "what-mark-to-market-means",
    "Marking investments to market": "marking-investments",
    "Why the balance sheet mattered": "balance-sheet"
   },
   "ch3": {
    "Chewco": "chewco",
    "The LJM partnerships": "ljm",
    "Rhythms: a hedge with Enron's own stock": "rhythms",
    "The Raptors": "raptors",
    "What it added up to": "what-it-added-up-to"
   },
   "ch4": {
    "\"Many push limits\"": "many-push-limits",
    "Andersen weighs its client": "andersen-weighs-its-client",
    "A sudden resignation": "a-sudden-resignation",
    "Sherron Watkins": "sherron-watkins",
    "An error comes to light": "an-error-comes-to-light",
    "The watchdogs outside": "watchdogs-outside"
   },
   "ch5": {
    "October 16: the third quarter": "october-16",
    "Questions multiply": "questions-multiply",
    "November 8: the restatement": "november-8-restatement",
    "A rescue attempt": "rescue-attempt",
    "The watchdogs": "the-watchdogs",
    "November 28 to December 2": "november-28-to-december-2",
    "The tip of the iceberg": "tip-of-the-iceberg"
   },
   "ch6": {
    "Enron's auditor": "enrons-auditor",
    "The fees": "the-fees",
    "Errors and what the examiner concluded": "errors-and-examiner",
    "The shredding": "the-shredding",
    "Conviction, collapse, reversal": "conviction-collapse-reversal",
    "The Big Four": "big-four"
   },
   "ch7": {
    "The investigations": "the-investigations",
    "The trials": "the-trials",
    "The employees' savings": "employees-savings",
    "A new law": "a-new-law"
   }
  };
  function slug(text) {
    return String(text || "").toLowerCase().replace(/[\u2018\u2019'"\u201c\u201d]/g, "")
      .replace(/&/g, " and ").replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 60) || "section";
  }
  function normHeading(t) { return String(t || "").replace(/[\u201c\u201d]/g, '"').replace(/[\u2018\u2019]/g, "'").replace(/\s+/g, " ").trim(); }
  function headingIds() {
    var n = parseInt(body.getAttribute("data-chapter"), 10);
    var table = {};
    Object.keys(HEADING_IDS["ch" + n] || {}).forEach(function (k) { table[normHeading(k)] = HEADING_IDS["ch" + n][k]; });
    // the chapter's closing question
    Array.prototype.forEach.call(document.querySelectorAll("#chapter aside.ask-why:not([id])"), function (a) {
      if (!document.getElementById("ask-why")) a.id = "ask-why";
    });
    Array.prototype.forEach.call(document.querySelectorAll("#chapter h2:not([id]), #chapter h3:not([id])"), function (h) {
      if (h.closest("aside.ask-why")) return;
      var fixed = table[normHeading(h.textContent)];
      var base = fixed || slug(h.textContent), id = base, k = 2;
      if (!fixed && n) console.info("Heading without a fixed id, using #" + base + ": " + h.textContent);
      while (document.getElementById(id)) id = base + "-" + k++;
      h.id = id;
    });
  }

  // Find the element for an anchor (exact id). Kept as one function so pathways and
  // tests resolve anchors the same way.
  function resolveAnchor(id) {
    id = String(id || "").replace(/^#/, "");
    var el = id ? document.getElementById(id) : null;
    return { el: el, exact: !!el };
  }

  /* ---------- init ---------- */
  function enhance(root) {
    processTerms(root);
    processFigures(root);
    processCites(root);
  }

  function init() {
    setupHeader();
    buildChapterNav();
    headingIds();
    if (/[?&]cards\b/.test(location.search)) body.classList.add("show-cards");
    enhance(document);
    // Ids added by script (headings, figures) exist only now: honour the #hash.
    if (location.hash && !/[?&]path=/.test(location.search)) {
      var t = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (t) t.scrollIntoView({ block: "start" });
    }

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { closePopover(true); return; }
      if (PAGE !== "chapter" || isTyping(e)) return;
      var n = parseInt(body.getAttribute("data-chapter"), 10);
      if (e.key === "ArrowRight" && CHAPTERS[n]) location.href = chapterHref(n + 1);
      if (e.key === "ArrowLeft" && CHAPTERS[n - 2]) location.href = chapterHref(n - 1);
    });

    var t;
    window.addEventListener("resize", function () { clearTimeout(t); t = setTimeout(layoutMarginNotes, 120); });
    window.addEventListener("load", layoutMarginNotes);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(layoutMarginNotes);
    window.addEventListener("beforeprint", function () {
      Array.prototype.forEach.call(document.querySelectorAll("details.endnotes"), function (d) { d.open = true; });
    });
  }

  window.AskWhy = {
    CHAPTERS: CHAPTERS,
    ROOT: ROOT,
    esc: esc,
    store: store,
    getSource: getSource,
    sourceHref: sourceHref,
    sourceRefHTML: sourceRefHTML,
    citeTag: citeTag,
    creditHTML: creditHTML,
    imageSrc: imageSrc,
    imageElement: imageElement,
    findImage: findImage,
    enhance: enhance,
    isNarrow: isNarrow,
    isTyping: isTyping,
    wideEnoughForMargins: wideEnoughForMargins,
    layoutMarginNotes: layoutMarginNotes,
    openPopover: openPopover,
    closePopover: closePopover,
    applyLens: applyLens,
    slug: slug,
    resolveAnchor: resolveAnchor
  };
  window.applyLens = applyLens;

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
