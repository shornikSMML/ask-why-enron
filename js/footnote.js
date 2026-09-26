/* The Footnote page: renders window.FOOTNOTE (see work/briefs/04-footnote.md).
   Each annotated phrase becomes a highlighted, focusable <mark>. The panel
   (beside the text on wide screens, a bottom sheet on phones) shows
   "What it said / What it left out / What the investigations found".
   Keys: j or → = next annotation, k or ← = previous, Esc closes the sheet. */
(function () {
  "use strict";
  var A = window.AskWhy, esc = A.esc;
  var FN = window.FOOTNOTE;
  var textHost = document.getElementById("fn-text");
  var panel = document.getElementById("anno-panel");
  var headHost = document.getElementById("fn-head");
  if (!textHost || !panel) return;

  if (!FN || !FN.paragraphs) {
    textHost.innerHTML = '<p class="placeholder">[Footnote text and annotations coming]</p>';
    return;
  }

  // intro / closing may be a plain string or {text, cites}
  function textWithCites(part) {
    if (!part) return "";
    if (typeof part === "string") return esc(part);
    return esc(part.text || "") + (part.cites || []).map(A.citeTag).join("");
  }

  if (headHost) {
    var src = FN.source || {};
    var srcLine = "";
    if (src.source_id) {
      var locText = src.loc || [src.section, src.lines ? "lines " + String(src.lines).replace(/\s*\(.*\)\s*$/, "") : ""].filter(Boolean).join(", ");
      srcLine = "Source: " + A.sourceRefHTML({ source_id: src.source_id, pdf_page: src.pdf_page, loc: locText })
        .replace('<span class="loc">', ' <span class="loc">(').replace(/<\/span>$/, ")</span>");
    }
    headHost.innerHTML = (FN.sample ? '<p><span class="sample-flag">Sample data</span></p>' : "") +
      "<h1>" + esc(FN.title || "The Footnote") + "</h1>" +
      (FN.intro ? '<p class="lede">' + textWithCites(FN.intro) + "</p>" : "") +
      (srcLine ? '<p class="fn-source">' + srcLine + "</p>" : "");
  }

  var annos = []; // in reading order

  // Wrap each annotation's phrase (an exact substring of its paragraph).
  function renderParagraph(p) {
    var text = String(p.text || "");
    var spans = [];
    (p.annotations || []).forEach(function (a) {
      var from = 0, idx = -1;
      // first occurrence that does not overlap an earlier span
      while ((idx = text.indexOf(a.phrase, from)) !== -1) {
        var end = idx + a.phrase.length, clash = false;
        for (var i = 0; i < spans.length; i++) if (idx < spans[i].end && end > spans[i].start) { clash = true; break; }
        if (!clash) break;
        from = idx + 1;
      }
      if (!a.phrase || idx === -1) { console.warn("Footnote: phrase not found or overlapping in paragraph " + (p.n != null ? p.n : p.id) + ": " + a.id); return; }
      spans.push({ start: idx, end: idx + a.phrase.length, a: a });
    });
    spans.sort(function (x, y) { return x.start - y.start; });
    var html = "", pos = 0;
    spans.forEach(function (s) {
      annos.push(s.a);
      var k = annos.length;
      html += esc(text.slice(pos, s.start)) +
        '<mark class="anno" tabindex="0" role="button" data-anno="' + esc(s.a.id) + '" aria-label="Annotation ' + k + '">' +
        esc(text.slice(s.start, s.end)) + "<sup>" + k + "</sup></mark>";
      pos = s.end;
    });
    html += esc(text.slice(pos));
    if (p.kind === "heading") return '<p class="fn-heading" id="fn-p' + esc(p.n) + '">' + html + "</p>";
    var label = p.n != null ? "Paragraph " + esc(p.n) : "";
    return '<p id="fn-p' + esc(p.n != null ? p.n : p.id) + '">' + (label ? '<span class="fn-para-n">' + label + "</span>" : "") + html + "</p>";
  }

  var out = '<div class="fn-note">' + FN.paragraphs.map(renderParagraph).join("") + "</div>";
  if (FN.source && FN.source.verbatim_note) out += '<p class="fn-verbatim">' + esc(FN.source.verbatim_note) + "</p>";
  var ctx = FN.context_passages || [];
  if (ctx.length) {
    out += '<section class="fn-context" aria-labelledby="fn-ctx-h"><h2 id="fn-ctx-h">Elsewhere in the same report</h2>' +
      ctx.map(function (c) {
        return '<figure class="fn-ctx-item"><figcaption>' + esc(c.where || "") + "</figcaption>" + renderParagraph(c) + "</figure>";
      }).join("") + "</section>";
  }
  if (FN.closing) {
    out += '<section class="fn-closing" aria-labelledby="fn-close-h"><h2 id="fn-close-h">Looking back</h2><p>' + textWithCites(FN.closing) + "</p>" +
      (FN.closing.ask_why ? '<aside class="ask-why"><h2>Ask Why</h2><p>' + esc(FN.closing.ask_why) + "</p></aside>" : "") + "</section>";
  }
  out += "<div data-endnotes></div>";
  textHost.innerHTML = out;

  var marks = Array.prototype.slice.call(textHost.querySelectorAll("mark.anno"));
  var current = -1;

  function citesHTML(cites) {
    if (!cites || !cites.length) return "";
    return '<h3>Sources</h3><ol class="cites">' + cites.map(function (c) {
      return "<li>" + A.sourceRefHTML(c).replace('<span class="loc">', ' <span class="loc">— ') + "</li>";
    }).join("") + "</ol>";
  }
  function termsHTML(terms) {
    if (!terms || !terms.length) return "";
    var G = window.GLOSSARY || {};
    return "<h3>Terms</h3><p>" + terms.map(function (t) {
      var label = G[t] ? (G[t].term || t) : t.replace(/-/g, " ");
      return '<span class="term" data-term="' + esc(t) + '">' + esc(label) + "</span>";
    }).join(", ") + "</p>";
  }

  function show(i, focusMark) {
    if (i < 0 || i >= annos.length) return;
    current = i;
    var a = annos[i];
    marks.forEach(function (m, j) { m.classList.toggle("is-active", j === i); m.setAttribute("aria-pressed", j === i ? "true" : "false"); });
    panel.innerHTML =
      '<button class="close" type="button" aria-label="Close annotation">×</button>' +
      '<h2 id="anno-title">Annotation ' + (i + 1) + "</h2>" +
      '<p class="phrase">“' + esc(a.phrase) + "”</p>" +
      "<h3>What it said</h3><p>" + esc(a.said || "") + "</p>" +
      "<h3>What it left out</h3><p>" + esc(a.left_out || "") + "</p>" +
      "<h3>What the investigations found</h3><p>" + esc(a.found || "") + "</p>" +
      citesHTML(a.cites) + termsHTML(a.glossary_terms) +
      '<div class="anno-controls"><span class="count">' + (i + 1) + " of " + annos.length + "</span>" +
      '<button class="filter-btn" type="button" data-step="-1"' + (i === 0 ? " disabled" : "") + '>← Previous</button>' +
      '<button class="filter-btn" type="button" data-step="1"' + (i === annos.length - 1 ? " disabled" : "") + ">Next →</button></div>";
    panel.classList.add("open");
    panel.setAttribute("aria-labelledby", "anno-title");
    A.enhance(panel);
    panel.scrollTop = 0;
    var m = marks[i];
    var sheet = window.matchMedia("(max-width: 999px)").matches;
    document.body.style.paddingBottom = sheet ? panel.offsetHeight + "px" : "";
    if (m && (focusMark || sheet)) {
      if (focusMark) m.focus({ preventScroll: true });
      var r = m.getBoundingClientRect();
      var sheetTop = panel.classList.contains("open") && window.matchMedia("(max-width: 999px)").matches ? panel.getBoundingClientRect().top : window.innerHeight;
      if (r.top < 70 || r.bottom > sheetTop - 10) window.scrollBy({ top: r.top - Math.min(140, sheetTop / 3), behavior: "smooth" });
    }
  }
  function closeSheet() {
    panel.classList.remove("open");
    document.body.style.paddingBottom = "";
    if (marks[current]) marks[current].focus();
  }

  panel.addEventListener("click", function (e) {
    var step = e.target.closest("[data-step]");
    if (step) { show(current + parseInt(step.getAttribute("data-step"), 10), true); return; }
    if (e.target.closest(".close")) closeSheet();
  });
  // Wide screens with a mouse: hovering a phrase (briefly) shows its annotation in the side panel.
  var hoverTimer;
  var canHover = window.matchMedia("(hover: hover) and (min-width: 1000px)");
  marks.forEach(function (m, i) {
    m.addEventListener("click", function () { show(i, false); });
    m.addEventListener("mouseenter", function () {
      if (!canHover.matches) return;
      clearTimeout(hoverTimer);
      hoverTimer = setTimeout(function () { if (current !== i) show(i, false); }, 180);
    });
    m.addEventListener("mouseleave", function () { clearTimeout(hoverTimer); });
    m.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); show(i, false); }
    });
  });

  document.addEventListener("keydown", function (e) {
    var t = e.target;
    if (e.altKey || e.ctrlKey || e.metaKey || (t && /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
    if (e.key === "j" || e.key === "ArrowRight") { e.preventDefault(); show(current < 0 ? 0 : Math.min(current + 1, annos.length - 1), true); }
    else if (e.key === "k" || e.key === "ArrowLeft") { e.preventDefault(); show(current < 0 ? 0 : Math.max(current - 1, 0), true); }
    else if (e.key === "Escape" && panel.classList.contains("open")) closeSheet();
  });

  // Initial panel content (wide screens show it; phones keep the sheet closed).
  panel.innerHTML = '<button class="close" type="button" aria-label="Close annotation">×</button>' +
    '<h2>How to read this page</h2><p class="anno-empty">Select any highlighted phrase to see what it said, what it left out, and what the investigations later found. ' +
    "On a keyboard, press <kbd>j</kbd> or <kbd>→</kbd> for the next note and <kbd>k</kbd> or <kbd>←</kbd> for the previous one.</p>" +
    '<p class="anno-empty">' + annos.length + " annotations.</p>";
})();
