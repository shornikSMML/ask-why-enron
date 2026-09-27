/* Pathways (Phase 2): guided routes through the site.
   Data: window.PATHWAYS (js/pathways-data.js, from work/drafts/pathways.json): an array
   (or {pathways: [...]}) of {id, title, for_whom, minutes, intro,
   stops: [{page, anchor, label, bridge}], closing_question, handout}.
   Any page opened with ?path=ID&stop=N shows a slim bar under the header with the
   pathway, the stop number, the bridge text and previous/next links, then scrolls to
   and highlights the stop's anchor (Cast entries, Timeline items, footnote annotations,
   chapter headings...). Also renders pathways.html (the index) and
   pathway-handout.html?path=ID (a printable handout). */
(function () {
  "use strict";
  var A = window.AskWhy;
  if (!A) return;
  var esc = A.esc, ROOT = A.ROOT;

  function list() {
    var P = window.PATHWAYS || [];
    if (!Array.isArray(P)) P = P.pathways || Object.keys(P).map(function (k) { return P[k]; });
    return P;
  }
  function find(id) {
    var P = list();
    for (var i = 0; i < P.length; i++) if (P[i].id === id) return P[i];
    return null;
  }
  function param(name) {
    var m = new RegExp("[?&]" + name + "=([^&#]*)").exec(location.search);
    return m ? decodeURIComponent(m[1]) : null;
  }
  function anchorOf(stop) { return String(stop.anchor || "").replace(/^#/, ""); }
  // URL for stop n (1-based) of pathway p, relative to the current page.
  function stopHref(p, n, useFallback) {
    var s = p.stops[n - 1];
    if (useFallback && s.fallback) s = s.fallback;
    var page = String(s.page || "index.html"), hash = "";
    var hi = page.indexOf("#");
    if (hi !== -1) { hash = page.slice(hi + 1); page = page.slice(0, hi); }
    var a = anchorOf(s) || hash;
    return ROOT + page + (page.indexOf("?") === -1 ? "?" : "&") + "path=" + encodeURIComponent(p.id) + "&stop=" + n +
      (useFallback ? "&via=fallback" : "") + (a ? "#" + encodeURIComponent(a) : "");
  }
  // Bridges that state a fact carry card citations: show them as a small source line.
  function citeLine(cites) {
    if (!cites || !cites.length) return "";
    return '<span class="pw-src">Source' + (cites.length > 1 ? "s" : "") + ": " + cites.map(function (c) {
      return A.sourceRefHTML({ source_id: c.source_id, pdf_page: c.pdf_page != null ? c.pdf_page : c.page, loc: c.loc, card: c.card })
        .replace('<span class="loc">', ' <span class="loc">');
    }).join("; ") + "</span>";
  }
  function minutes(p) { return p.minutes ? "about " + esc(p.minutes) + " minutes" : ""; }
  function isSample() { return !!window.PATHWAYS_SAMPLE; }
  var SAMPLE_FLAG = '<span class="sample-flag phase2-sample">Sample pathway data</span>';

  /* ---------- the bar on any page ---------- */
  function showBar() {
    var id = param("path"), n = parseInt(param("stop"), 10);
    if (!id) return;
    var p = find(id);
    var header = document.querySelector(".site-header");
    var bar = document.createElement("nav");
    bar.className = "pathway-bar";
    bar.setAttribute("aria-label", "Pathway");
    if (!p || !p.stops || !p.stops.length || !(n >= 1 && n <= p.stops.length)) {
      bar.innerHTML = '<div class="pw-inner"><p>This pathway link is out of date. <a href="' + ROOT + 'pathways.html">See all pathways</a>.</p></div>';
      header.parentNode.insertBefore(bar, header.nextSibling);
      console.warn("Pathway not found:", id, n);
      return;
    }
    var N = p.stops.length, s = p.stops[n - 1];
    bar.innerHTML = '<div class="pw-inner">' +
      '<p class="pw-where"><a href="' + ROOT + "pathways.html#" + esc(p.id) + '">Pathway: ' + esc(p.title) + "</a>" +
      ' <span class="pw-count">Stop ' + n + " of " + N + "</span>" + (s.label ? ' <span class="pw-label">' + esc(s.label) + "</span>" : "") + "</p>" +
      (s.bridge ? '<p class="pw-bridge">' + esc(s.bridge) + (s.cites && s.cites.length ? " " + citeLine(s.cites) : "") + "</p>" : "") +
      (n === N && p.closing_question ? '<p class="pw-closing"><strong>To finish:</strong> ' + esc(p.closing_question) + "</p>" : "") +
      '<p class="pw-nav">' +
      (n > 1 ? '<a class="pw-prev" rel="prev" href="' + esc(stopHref(p, n - 1)) + '">&larr; Previous stop</a>' : '<span class="pw-prev is-off">&larr; Previous stop</span>') +
      (n < N ? '<a class="pw-next" rel="next" href="' + esc(stopHref(p, n + 1)) + '">Next stop &rarr;</a>' : '<a class="pw-next" href="' + ROOT + "pathways.html#" + esc(p.id) + '">Finish &rarr;</a>') +
      '<a class="pw-leave" href="' + esc(location.pathname.split("/").pop() + location.hash) + '">Leave pathway</a>' +
      (isSample() ? " " + SAMPLE_FLAG : "") + "</p></div>";
    header.parentNode.insertBefore(bar, header.nextSibling);
    document.body.classList.add("on-pathway");
    // A compact copy stays at the bottom of the screen after the reader scrolls down.
    var mini = document.createElement("nav");
    mini.className = "pw-mini";
    mini.setAttribute("aria-label", "Pathway, short");
    mini.innerHTML = '<span class="pw-mini-where">' + esc(p.title) + " · " + n + "/" + N + "</span>" +
      (n > 1 ? '<a href="' + esc(stopHref(p, n - 1)) + '" aria-label="Previous stop">&larr;</a>' : "") +
      (n < N ? '<a href="' + esc(stopHref(p, n + 1)) + '">Next stop &rarr;</a>' : '<a href="' + ROOT + "pathways.html#" + esc(p.id) + '">Finish &rarr;</a>');
    document.body.appendChild(mini);
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) { mini.classList.toggle("show", !es[0].isIntersecting); }).observe(bar);
    } else mini.classList.add("show");

    // Keep the pathway when the reader switches lens or uses in-page links: nothing to do,
    // the query string stays. Scroll to and highlight the stop's target.
    var viaFallback = param("via") === "fallback" && s.fallback;
    var a = anchorOf(viaFallback ? s.fallback : s) || location.hash.slice(1);
    if (a) {
      var r = A.resolveAnchor(a), t = r.el;
      if (!t && s.fallback && !viaFallback) {
        // The stop's section doesn't exist yet: go to the stop's fallback instead.
        console.info("Pathway " + p.id + " stop " + n + ": #" + a + " not on this page; using the stop's fallback");
        location.replace(stopHref(p, n, true));
        return;
      }
      if (!t) { console.warn("Pathway " + p.id + " stop " + n + ": anchor #" + a + " not found on this page"); A.pathwayStop = { id: p.id, stop: n, anchor: a, resolved: null }; return; }
      if (!r.exact) console.info("Pathway " + p.id + " stop " + n + ": #" + a + " matched #" + t.id);
      A.pathwayStop = { id: p.id, stop: n, anchor: a, resolved: t.id, exact: r.exact, fallback: !!viaFallback };
      if (!/^(chapter|main)$/.test(t.id) && t.tagName !== "ARTICLE") t.classList.add("pw-target");
      if (t.tagName === "DETAILS") t.open = true;
      var go = function () { t.scrollIntoView({ block: "start" }); };
      go();
      window.addEventListener("load", function () { setTimeout(go, 50); });
    }
  }

  /* ---------- pathways.html ---------- */
  function renderIndex() {
    var host = document.getElementById("pathway-list");
    if (!host) return;
    var P = list();
    if (!P.length) { host.innerHTML = '<p class="none">The pathways could not be loaded.</p>'; return; }
    host.innerHTML = (isSample() ? "<p>" + SAMPLE_FLAG + " Layout test only; the real pathways are being written.</p>" : "") +
      '<ol class="pathway-cards">' + P.map(function (p) {
        var stops = p.stops || [];
        return '<li class="pathway-card" id="' + esc(p.id) + '">' +
          "<h2>" + esc(p.title) + "</h2>" +
          '<p class="pw-meta">' + (p.for_whom ? "For " + esc(String(p.for_whom).replace(/^for\s+/i, "")) : "") + (p.for_whom && p.minutes ? " · " : "") + minutes(p) + " · " + stops.length + " stops</p>" +
          (p.intro ? "<p>" + esc(p.intro) + "</p>" : "") +
          '<p class="pw-actions">' + (stops.length ? '<a class="btn" href="' + esc(stopHref(p, 1)) + '">Start the pathway &rarr;</a> ' : "") +
          '<a class="pw-handout-link" href="' + ROOT + "pathway-handout.html?path=" + encodeURIComponent(p.id) + '">Printable handout</a></p>' +
          (stops.length ? '<details class="pw-stops"><summary>See the ' + stops.length + " stops</summary><ol>" + stops.map(function (s, i) {
            return '<li><a href="' + esc(stopHref(p, i + 1)) + '">' + esc(s.label || s.page) + "</a>" + (s.bridge ? '<span class="pw-stop-bridge">' + esc(s.bridge) + (s.cites && s.cites.length ? " " + citeLine(s.cites) : "") + "</span>" : "") + "</li>";
          }).join("") + "</ol></details>" : "") +
          "</li>";
      }).join("") + "</ol>";
    if (location.hash) { var t = document.getElementById(location.hash.slice(1)); if (t) { t.classList.add("pw-target"); t.scrollIntoView(); } }
  }

  /* ---------- pathway-handout.html?path=ID ---------- */
  function renderHandout() {
    var host = document.getElementById("pathway-handout");
    if (!host) return;
    var p = find(param("path"));
    if (!p) {
      host.innerHTML = '<h1>Pathway handout</h1><p>Choose a pathway on the <a href="pathways.html">Pathways page</a>.</p>';
      return;
    }
    document.title = p.title + " · Handout · Ask Why";
    var h = p.handout || {};
    if (typeof h === "string") h = { text: h };
    var hstops = h.stops || [];
    var qs = h.discussion_questions || h.questions || [];
    var closing = h.closing_question || p.closing_question;
    host.innerHTML = (isSample() ? "<p>" + SAMPLE_FLAG + "</p>" : "") +
      '<p class="eyebrow">Ask Why: The Rise and Fall of Enron · Pathway handout</p>' +
      "<h1>" + esc(h.title || p.title) + "</h1>" +
      '<p class="pw-meta">' + (h.subtitle ? esc(h.subtitle) : (p.for_whom ? "For " + esc(String(p.for_whom).replace(/^for\s+/i, "")) : "") + (p.minutes ? " · " + minutes(p) : "")) + "</p>" +
      (h.intro || p.intro ? "<p>" + esc(h.intro || p.intro) + "</p>" : "") +
      (h.text ? String(h.text).split(/\n{2,}/).map(function (t) { return "<p>" + esc(t) + "</p>"; }).join("") : "") +
      "<h2>Stops</h2><ol class=\"handout-stops\">" + (p.stops || []).map(function (ps, i) {
        var txt = hstops[i];
        var line = typeof txt === "string" ? esc(txt) : "<strong>" + esc(ps.label || "") + "</strong>" + (ps.bridge ? ": " + esc(ps.bridge) : "");
        return "<li>" + line +
          '<span class="handout-where">' + esc((ps.page || "").replace(/\?.*$/, "") + (anchorOf(ps) ? "#" + anchorOf(ps) : "")) + "</span>" +
          (ps.cites && ps.cites.length ? '<span class="handout-src">' + citeLine(ps.cites) + "</span>" : "") + "</li>";
      }).join("") + "</ol>" +
      (hstops.length && p.stops && hstops.length !== p.stops.length ? '<p class="none">(The handout lists ' + hstops.length + " stops; the pathway has " + p.stops.length + ".)</p>" : "") +
      (qs.length ? "<h2>Questions for discussion</h2><ol>" + qs.map(function (q) { return "<li>" + esc(q) + "</li>"; }).join("") + "</ol>" : "") +
      (closing ? '<aside class="ask-why"><h2>Ask Why</h2><p>' + esc(closing) + "</p></aside>" : "") +
      '<p class="handout-actions"><button type="button" class="btn" onclick="window.print()">Print this handout</button> ' +
      '<a href="pathways.html#' + esc(p.id) + '">Back to pathways</a></p>' +
      '<p class="handout-foot">Online: open the Ask Why site and choose Pathways, then &ldquo;' + esc(p.title) + "&rdquo;.</p>";
  }

  A.pathways = { list: list, find: find, stopHref: stopHref };

  function init() { showBar(); renderIndex(); renderHandout(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
