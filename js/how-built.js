/* "How This Was Built": renders window.BUILD_LOG (build-log/log.js, written by
   work/tools/build_log.py) and window.GAPS (js/gaps-data.js, written by
   work/tools/gaps_to_js.py). Sections: before the agents, at a glance, team
   diagram, build timeline, agent cards (one collapsible block per run),
   how facts were checked (corrections), gaps and candidates, reader tips,
   websites. Every field is optional so the page keeps working while the log grows. */
(function () {
  "use strict";
  var A = window.AskWhy, esc = A.esc;
  var L = window.BUILD_LOG;
  var G = window.GAPS || null;
  function $(id) { return document.getElementById(id); }
  if (!L) {
    ["before-agents", "at-a-glance", "team-diagram", "build-timeline", "agent-cards"].forEach(function (id) {
      if ($(id)) $(id).innerHTML = "<p>The build log could not be loaded.</p>";
    });
    return;
  }

  function fmtTime(t) {
    if (!t) return "";
    var d = new Date(t);
    if (isNaN(d)) return esc(t);
    var M = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    var hh = ("0" + d.getUTCHours()).slice(-2), mm = ("0" + d.getUTCMinutes()).slice(-2);
    return M[d.getUTCMonth()] + " " + d.getUTCDate() + ", " + d.getUTCFullYear() + ", " + hh + ":" + mm + " UTC";
  }
  function clock(t) {
    var d = new Date(t);
    return isNaN(d) ? esc(t || "") : ("0" + d.getUTCHours()).slice(-2) + ":" + ("0" + d.getUTCMinutes()).slice(-2);
  }
  function para(text) {
    return String(text || "").split(/\n{2,}/).map(function (p) { return "<p>" + esc(p) + "</p>"; }).join("");
  }
  // Light markdown for text from gaps.md: escape first, then **bold**, *italic*, `code`.
  function md(text) {
    return esc(text || "")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/(^|[^*])\*([^*\s][^*]*)\*/g, "$1<em>$2</em>")
      .replace(/`([^`]+)`/g, "<code>$1</code>");
  }
  function list(items) {
    if (!items || !items.length) return '<p class="none">none recorded yet</p>';
    return "<ul>" + items.map(function (x) {
      return "<li>" + esc(typeof x === "string" ? x : JSON.stringify(x)) + "</li>";
    }).join("") + "</ul>";
  }
  function shortName(name) {
    var n = String(name || "").split(":")[0].trim();
    if (n.split("(").length > n.split(")").length) n += ")";
    return n;
  }
  function plural(n, one, many) { return n + " " + (n === 1 ? one : (many || one + "s")); }

  var agents = (L.agents || []).slice();
  var S = L.summary || {};

  /* ---------- 1. Before the agents (text as the Scribe wrote it) ---------- */
  var before = L.before_the_agents || {};
  var bHost = $("before-agents");
  if (bHost && (before.summary || before.fingerprint_check)) {
    var h = para(before.summary);
    if (before.fingerprint_explained) h += '<div class="fp-box"><h3>What is a SHA-256 fingerprint?</h3>' + para(before.fingerprint_explained) + "</div>";
    if (before.fingerprint_check) h += "<h3>The fingerprint check</h3>" + para(before.fingerprint_check);
    if (before.lessons && before.lessons.length) {
      h += "<h3>Lessons from assembling the library</h3><ol class=\"lessons\">" + before.lessons.map(function (l) {
        return "<li><strong>" + esc(l.title || "") + ".</strong> " + esc(l.text || l) + "</li>";
      }).join("") + "</ol>";
    }
    bHost.innerHTML = h;
  }

  /* ---------- 2. At a glance ---------- */
  var gHost = $("at-a-glance");
  if (gHost) {
    var stats = [
      [S.agents, "agents"], [S.runs, "agent runs"], [S.library_documents, "documents in the library"],
      [S.sources_cited, "documents cited on the site"], [S.fact_cards_checked, "fact cards checked"],
      [S.corrections, "corrections logged"], [S.candidates_found, "candidate sources awaiting approval"]
    ].filter(function (s) { return s[0] != null; });
    var texts = Array.isArray(S.text) ? S.text : (S.text ? [S.text] : []);
    gHost.innerHTML = stats.length || texts.length ?
      '<div class="glance"><ul class="stat-grid">' + stats.map(function (s) {
        return '<li><span class="stat-n">' + esc(s[0]) + '</span><span class="stat-l">' + esc(s[1]) + "</span></li>";
      }).join("") + "</ul>" + (texts.length ? '<ul class="glance-text">' + texts.map(function (t) { return "<li>" + esc(t) + "</li>"; }).join("") + "</ul>" : "") + "</div>"
      : '<p class="none">No summary in the build log yet.</p>';
  }

  /* ---------- 3. Team diagram ---------- */
  var planned = (L.briefs_not_yet_assigned || []).map(function (b) {
    var m = /^#\s*Brief:\s*([^\n]+)/.exec(b.text || "");
    return { name: m ? m[1].replace(/\s*\(.*\)\s*$/, "") : b.file, planned: true };
  });
  var started = agents.map(function (a) { return shortName(a.name).toLowerCase(); });
  planned = planned.filter(function (p) { return started.indexOf(shortName(p.name).toLowerCase()) === -1; });
  var nodes = agents.map(function (a) { return { name: a.name, runs: (a.runs || []).length, planned: false }; }).concat(planned);

  function wrap(text, max) {
    var words = String(text).split(/\s+/), lines = [], cur = "";
    words.forEach(function (w) {
      if (cur && (cur + " " + w).length > max) { lines.push(cur); cur = w; } else cur = cur ? cur + " " + w : w;
    });
    if (cur) lines.push(cur);
    return lines.slice(0, 3);
  }
  function textLines(lines, x, y, size, weight) {
    var start = y - (lines.length - 1) * size * 0.6;
    return '<text x="' + x + '" y="' + start + '" text-anchor="middle" dominant-baseline="middle" font-size="' + size + '"' +
      (weight ? ' font-weight="' + weight + '"' : "") + ">" +
      lines.map(function (l, i) { return '<tspan x="' + x + '" dy="' + (i ? size * 1.2 : 0) + '">' + esc(l) + "</tspan>"; }).join("") + "</text>";
  }
  function box(x, y, w, hgt, cls, lines, size, dashed, runs) {
    var badge = "";
    if (runs) {
      var bx = x + w / 2 - 4, by = y - hgt / 2 + 4;
      badge = '<g class="runs-badge"><circle cx="' + bx + '" cy="' + by + '" r="11" style="fill:var(--accent);stroke:var(--bg);stroke-width:2"/>' +
        '<text x="' + bx + '" y="' + (by + 0.5) + '" text-anchor="middle" dominant-baseline="middle" font-size="12" font-weight="700" style="fill:var(--bg)">' + runs + "</text></g>";
    }
    return '<g class="node ' + cls + '"><rect x="' + (x - w / 2) + '" y="' + (y - hgt / 2) + '" width="' + w + '" height="' + hgt +
      '" rx="10" style="fill:' + (cls === "coord" ? "var(--accent-soft)" : "var(--bg-raised)") + ";stroke:" + (cls === "coord" ? "var(--accent)" : "var(--muted)") +
      '" stroke-width="' + (cls === "coord" ? 3 : 1.5) + '"' + (dashed ? ' stroke-dasharray="6 5"' : "") + "/>" +
      textLines(lines, x, y, size, cls === "coord" ? 700 : 500) + badge + "</g>";
  }
  function drawTeam() {
    var host = $("team-diagram");
    if (!host) return;
    var width = host.clientWidth || 700, svg;
    var title = "The coordinator in the center, connected to each of " + agents.length + " agents. The number on each box is how many times that agent ran. Agents never talk to each other; all work passes through the coordinator.";
    if (width >= 560) {
      var W = 920, H = 700, cx = W / 2, cy = H / 2, rx = 370, ry = 290, n = nodes.length;
      var edges = "", boxes = "";
      nodes.forEach(function (nd, i) {
        var ang = -Math.PI / 2 + (2 * Math.PI * i) / Math.max(n, 1);
        var x = cx + rx * Math.cos(ang), y = cy + ry * Math.sin(ang);
        edges += '<line class="edge" x1="' + cx + '" y1="' + cy + '" x2="' + x.toFixed(1) + '" y2="' + y.toFixed(1) + '"' + (nd.planned ? ' stroke-dasharray="6 6"' : "") + "/>";
        boxes += box(x, y, 136, 58, nd.planned ? "planned" : "agent", wrap(shortName(nd.name), 15), 14, nd.planned, nd.runs);
      });
      svg = '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-labelledby="team-title"><title id="team-title">' + esc(title) + "</title>" +
        edges + boxes + box(cx, cy, 190, 70, "coord", ["Coordinator"], 21) + "</svg>";
    } else {
      // Phone: coordinator on top, agents in two columns hanging from a trunk line.
      var VW = 360, bw = 158, bh = 56, gap = 14, top = 90, rows = Math.ceil(nodes.length / 2);
      var VH = top + rows * (bh + gap) + 10, trunkX = VW / 2, e2 = "", b2 = "";
      e2 += '<line class="edge" x1="' + trunkX + '" y1="60" x2="' + trunkX + '" y2="' + (top + (rows - 1) * (bh + gap) + bh / 2) + '"/>';
      nodes.forEach(function (nd, i) {
        var col = i % 2, row = Math.floor(i / 2);
        var x = col ? VW - 12 - bw / 2 : 4 + bw / 2, y = top + row * (bh + gap) + bh / 2;
        e2 += '<line class="edge" x1="' + trunkX + '" y1="' + y + '" x2="' + (col ? x - bw / 2 : x + bw / 2) + '" y2="' + y + '"' + (nd.planned ? ' stroke-dasharray="5 5"' : "") + "/>";
        b2 += box(x, y, bw, bh, nd.planned ? "planned" : "agent", wrap(shortName(nd.name), 18), 14, nd.planned, nd.runs);
      });
      svg = '<svg viewBox="0 0 ' + VW + " " + VH + '" role="img" aria-labelledby="team-title"><title id="team-title">' + esc(title) + "</title>" +
        e2 + b2 + box(VW / 2, 32, 200, 50, "coord", ["Coordinator"], 18) + "</svg>";
    }
    host.innerHTML = svg + '<p class="diagram-key">The number on each box is how many times that agent ran.' +
      (planned.length ? " Dashed boxes: agents planned for later steps." : "") + "</p>";
  }
  drawTeam();
  var rt, lastW = 0;
  window.addEventListener("resize", function () {
    clearTimeout(rt);
    rt = setTimeout(function () { var w = ($("team-diagram") || {}).clientWidth; if (w !== lastW) { lastW = w; drawTeam(); } }, 150);
  });

  /* ---------- 4. Build timeline ---------- */
  var TYPE_LABELS = { decision: "Decision", agent_start: "Agent started", agent_finish: "Agent finished", handoff: "Handoff", review: "Review", web_source: "Website used", correction: "Correction", message: "Message" };
  var tl = $("build-timeline");
  if (tl) {
    var recs = (L.timeline || []).slice().sort(function (a, b) { return String(a.time).localeCompare(String(b.time)); });
    var lastDay = "";
    tl.innerHTML = recs.length ? '<p class="ui tl-range">' + plural(recs.length, "event") + (recs.length ? ", from " + fmtTime(recs[0].time) + " to " + fmtTime(recs[recs.length - 1].time) : "") + ".</p>" +
      '<div class="build-tl-wrap" tabindex="0" role="region" aria-label="Build timeline, ' + recs.length + ' events"><ol class="build-tl">' + recs.map(function (r) {
        var day = String(r.time || "").slice(0, 10), dayLabel = "";
        if (day !== lastDay) { lastDay = day; dayLabel = fmtTime(r.time).replace(/, \d\d:\d\d UTC$/, ""); }
        var label = r.label || r.title || (r.reviewed ? "Review: " + r.reviewed : "");
        return '<li class="t-' + esc(r.type || "") + '"><span class="t">' + (dayLabel ? esc(dayLabel) + " · " : "") + clock(r.time) + " UTC" +
          '<span class="chip type">' + esc(TYPE_LABELS[r.type] || r.type || "") + "</span></span>" + esc(label) + "</li>";
      }).join("") + "</ol></div>" : '<p class="none">No events yet.</p>';
  }

  /* ---------- 5. Agent cards ---------- */
  var cards = $("agent-cards");
  if (cards) {
    var coord = L.coordinator || {};
    var msgs = L.messages || [];
    var html = '<details class="agent-card" id="agent-coordinator"><summary><h3>' + esc(coord.name || "Coordinator") + "</h3> " +
      '<span class="chip">' + plural((coord.decisions || []).length, "decision") + "</span>" +
      '<span class="role">' + esc(coord.role || "") + "</span></summary><div class=\"body\">" +
      "<h4>Decisions</h4>" + ((coord.decisions || []).length ? "<ol>" + coord.decisions.map(function (d) {
        return "<li><strong>" + esc(d.title || "") + "</strong> <span class=\"when\">" + fmtTime(d.time) + "</span><br>" + esc(d.detail || "") + "</li>";
      }).join("") + "</ol>" : '<p class="none">none recorded yet</p>') +
      (msgs.length ? "<h4>Follow-up messages to agents</h4><ol>" + msgs.map(function (m) {
        return "<li><strong>To " + esc(m.to || "") + "</strong> <span class=\"when\">" + fmtTime(m.recorded || m.time) + "</span><br>" + esc(m.summary || m.text || "") + "</li>";
      }).join("") + "</ol>" : "") +
      "</div></details>";

    html += agents.map(function (a) {
      var runs = a.runs || [];
      var last = runs[runs.length - 1] || {};
      var status = last.finished ? (last.decision || a.decision || "finished") : "still working";
      return '<details class="agent-card" id="agent-' + esc(a.id) + '"><summary><h3>' + esc(a.name) + "</h3> " +
        '<span class="chip">' + plural(runs.length, "run") + '</span> <span class="chip status">' + esc(status) + "</span>" +
        '<span class="role">' + esc(a.role || "") + '</span></summary><div class="body">' +
        runs.map(function (r, i) {
          var resumed = r.kind === "resumed";
          var head = "Run " + (r.run || i + 1) + (resumed ? " · resumed by a follow-up message" : " · started from a brief") + (r.wave ? " · wave " + esc(r.wave) : "");
          var brief = "";
          if (r.brief) {
            brief = "<details class=\"brief-box\"><summary>Read the exact brief" + (r.brief_file ? " (" + esc(r.brief_file) + ")" : "") + "</summary><pre class=\"brief\">" + esc(r.brief) + "</pre>" +
              (a.common_rules_file ? '<p class="ui small">Every agent also received the <a href="#common-rules">common rules</a>.</p>' : "") + "</details>";
          } else if (r.brief_summary) {
            brief = "<h4>What the coordinator asked</h4><p>" + esc(r.brief_summary) + "</p>";
          }
          var rmsgs = (r.messages || []).filter(function (m) { return !(resumed && m.matched === "resumed this run" && r.brief_summary && r.brief_summary.indexOf(m.summary) !== -1); });
          return '<details class="run"' + (i === runs.length - 1 ? " open" : "") + "><summary>" + head + "</summary>" +
            '<p class="ui small">Started ' + fmtTime(r.started) + (r.finished ? " · finished " + fmtTime(r.finished) : " · still working") + "</p>" +
            brief +
            (rmsgs.length ? "<h4>Messages from the coordinator</h4><ul>" + rmsgs.map(function (m) { return "<li>" + esc(m.summary || "") + (m.matched ? ' <span class="when">(' + esc(m.matched) + ")</span>" : "") + "</li>"; }).join("") + "</ul>" : "") +
            "<h4>What it read</h4>" + list(r.inputs) + "<h4>What it produced</h4>" + list(r.outputs) +
            '<h4>The coordinator&rsquo;s decision</h4><p><span class="decision">' + esc(r.decision || (r.finished ? "recorded without a decision" : "pending")) + "</span>" + (r.reason ? ". " + esc(r.reason) : "") + "</p>" +
            ((r.reviews || []).length ? "<h4>Reviews</h4>" + list(r.reviews.map(function (v) { return (v.reviewed ? v.reviewed + ": " : "") + (v.result || v.detail || ""); })) : "") +
            "</details>";
        }).join("") +
        "</div></details>";
    }).join("");
    if (L.common_rules && L.common_rules.text) {
      html += '<details class="agent-card" id="common-rules"><summary><h3>Common rules given to every agent</h3><span class="role">' + esc(L.common_rules.file || "") + '</span></summary><div class="body"><pre class="brief">' + esc(L.common_rules.text) + "</pre></div></details>";
    }
    cards.innerHTML = html;
    // A link to #common-rules (or #agent-x) opens that card.
    function openTarget() {
      var t = location.hash && document.getElementById(location.hash.slice(1));
      if (t && t.tagName === "DETAILS") { t.open = true; t.scrollIntoView(); }
    }
    window.addEventListener("hashchange", openTarget);
    cards.addEventListener("click", function (e) {
      var a = e.target.closest('a[href^="#"]');
      if (a) { var t = document.getElementById(a.getAttribute("href").slice(1)); if (t && t.tagName === "DETAILS") t.open = true; }
    });
    openTarget();
  }

  /* ---------- 6. Corrections ---------- */
  (function corrections(rows, host) {
    if (!host) return;
    if (!rows || !rows.length) { host.innerHTML = '<p class="none">No corrections recorded yet.</p>'; return; }
    var LABELS = { what_it_said: "What the draft said", what_the_source_says: "What the source says", fix: "The fix", source: "Source checked", date: "Date", recorded_in: "Recorded in" };
    host.innerHTML = '<details class="corr-wrap"><summary>Show all ' + rows.length + " corrections</summary>" +
      '<ol class="corr-list">' + rows.map(function (r, i) {
        var keys = Object.keys(r).filter(function (k) { return k !== "number" && k !== "page_item" && r[k] != null && r[k] !== ""; });
        return '<li class="corr-item"><h3>' + esc((r.number || i + 1) + ". " + (r.page_item || "")) + "</h3><dl>" +
          keys.map(function (k) {
            var v = r[k];
            return "<dt>" + esc(LABELS[k] || k.replace(/_/g, " ")) + "</dt><dd>" + esc(typeof v === "object" ? JSON.stringify(v) : v) + "</dd>";
          }).join("") + "</dl></li>";
      }).join("") + "</ol></details>";
  })(L.corrections, $("corrections"));

  /* ---------- 7. Gaps, candidates, reader tips ---------- */
  var gapsHost = $("gaps"), candHost = $("candidates"), tipsHost = $("reader-tips");
  if (!G) {
    [gapsHost, candHost, tipsHost].forEach(function (h) { if (h) h.innerHTML = '<p class="none">The gaps list could not be loaded.</p>'; });
  } else {
    var sections = G.sections || [];
    var tips = sections.filter(function (s) { return /reader tips/i.test(s.title); })[0];
    var gapSecs = sections.filter(function (s) { return s !== tips; });
    function col(row, re) {
      for (var k in row) if (re.test(k)) return row[k];
      return "";
    }
    if (gapsHost) {
      var total = gapSecs.reduce(function (n, s) { return n + (s.rows || []).length; }, 0);
      gapsHost.innerHTML = '<p class="ui small">' + plural(total, "gap") + " recorded, in order of importance. Each shows the claim the agents wanted to make, the kind of document that would support it, and what happened.</p>" +
        gapSecs.map(function (s) {
          var imp = /critical|useful|minor/i.exec(s.title);
          return '<details class="gap-group"' + (/critical/i.test(s.title) ? " open" : "") + "><summary><h3>" + esc(s.title) + '</h3> <span class="chip">' + plural((s.rows || []).length, "gap") + "</span></summary>" +
            (s.intro || []).map(function (p) { return "<p>" + md(p) + "</p>"; }).join("") +
            '<ol class="gap-list">' + (s.rows || []).map(function (r) {
              var importance = col(r, /^importance$/i) || (imp ? imp[0].toLowerCase() : "");
              return '<li class="gap-item"><p class="gap-claim"><span class="gap-n">' + md(col(r, /^#$/)) + "</span> " + md(col(r, /claim/i)) +
                (importance ? ' <span class="chip">' + md(importance) + "</span>" : "") + "</p><dl>" +
                "<dt>Would need</dt><dd>" + md(col(r, /kind of document/i)) + "</dd>" +
                "<dt>Raised by</dt><dd>" + md(col(r, /raised by/i)) + "</dd>" +
                "<dt>What happened</dt><dd>" + md(col(r, /status/i)) + "</dd></dl></li>";
            }).join("") + "</ol></details>";
        }).join("");
    }
    if (candHost) {
      var cands = G.candidates || [];
      candHost.innerHTML = cands.length ? '<ol class="cand-list">' + cands.map(function (c) {
        return '<li class="cand-item"><p class="cand-title">' + esc(c.title) + "</p>" +
          '<p class="ui small">' + esc(c.source_body || "") + (c.date ? " · " + esc(c.date) : "") +
          (c.official_or_mirror ? " · " + esc(c.official_or_mirror) + " copy" : "") +
          (c.fills_gap ? " · for gap " + esc(c.fills_gap) : "") + "</p>" +
          '<p class="cand-status">Awaiting the owner&rsquo;s approval. Not used on this site.</p></li>';
      }).join("") + "</ol>" : '<p class="none">No candidates recorded.</p>';
    }
    if (tipsHost) {
      tipsHost.innerHTML = tips && (tips.rows || []).length ? '<ol class="tip-list">' + tips.rows.map(function (r) {
        return '<li class="tip-item"><p class="tip-claim">&ldquo;' + md(col(r, /tip/i)) + "&rdquo;</p><p>" + md(col(r, /status/i)) + "</p></li>";
      }).join("") + "</ol>" : '<p class="none">No reader tips recorded.</p>';
    }
  }

  /* ---------- 8. Websites ---------- */
  (function web(rows, host) {
    if (!host) return;
    if (!rows || !rows.length) { host.innerHTML = '<p class="none">No websites recorded yet.</p>'; return; }
    host.innerHTML = '<div class="table-wrap"><table><thead><tr><th>Website</th><th>Used by</th><th>Why</th></tr></thead><tbody>' +
      rows.map(function (r) {
        return "<tr><td>" + (r.url ? '<a href="' + esc(r.url) + '" target="_blank" rel="noopener">' + esc(r.site || r.url) + "</a>" : esc(r.site || "")) + "</td>" +
          "<td>" + esc(r.used_by || "") + "</td><td>" + esc(r.purpose || "") + "</td></tr>";
      }).join("") + "</tbody></table></div>";
  })(L.web_sources, $("web-sources"));

  var gen = $("log-generated");
  if (gen && L.generated) gen.textContent = "Build log last generated " + fmtTime(L.generated) + ".";
})();
