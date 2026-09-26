/* "How This Was Built": renders window.BUILD_LOG (build-log/log.js, written by
   the Scribe's work/tools/build_log.py). Sections: before the agents, team
   diagram, build timeline, one card per agent, coordinator decisions,
   fact-check corrections, websites used. Every field is optional so the page
   keeps working while the log grows. */
(function () {
  "use strict";
  var A = window.AskWhy, esc = A.esc;
  var L = window.BUILD_LOG;
  function $(id) { return document.getElementById(id); }
  if (!L) {
    ["team-diagram", "build-timeline", "agent-cards"].forEach(function (id) {
      if ($(id)) $(id).innerHTML = '<p class="placeholder">[Build log not available yet]</p>';
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
  function para(text) {
    return String(text || "").split(/\n{2,}/).map(function (p) { return "<p>" + esc(p) + "</p>"; }).join("");
  }
  function list(items) {
    if (!items || !items.length) return '<span class="none">none recorded yet</span>';
    return "<ul>" + items.map(function (x) {
      return "<li>" + esc(typeof x === "string" ? x : JSON.stringify(x)) + "</li>";
    }).join("") + "</ul>";
  }
  function shortName(name) {
    var n = String(name || "").split(":")[0].trim();
    if (n.split("(").length > n.split(")").length) n += ")";
    return n;
  }

  /* ---------- 1. Before the agents ---------- */
  var before = L.before_the_agents || {};
  var bHost = $("before-agents");
  if (bHost && (before.summary || before.fingerprint_check)) {
    var h = para(before.summary);
    if (before.fingerprint_explained) h += "<h3>What is a SHA-256 fingerprint?</h3>" + para(before.fingerprint_explained);
    if (before.fingerprint_check) h += "<h3>The fingerprint check</h3>" + para(before.fingerprint_check);
    if (before.lessons && before.lessons.length) {
      h += "<h3>Lessons from assembling the library</h3><ol>" + before.lessons.map(function (l) {
        return "<li><strong>" + esc(l.title || "") + ".</strong> " + esc(l.text || l) + "</li>";
      }).join("") + "</ol>";
    }
    bHost.innerHTML = h;
  }

  /* ---------- 2. Team diagram ---------- */
  var agents = (L.agents || []).slice();
  var planned = (L.briefs_not_yet_assigned || []).map(function (b) {
    var m = /^#\s*Brief:\s*([^\n]+)/.exec(b.text || "");
    return { name: m ? m[1].replace(/\s*\(.*\)\s*$/, "") : b.file, planned: true };
  });
  // A planned brief whose agent already appears (e.g. a second pass) is not drawn twice.
  var started = agents.map(function (a) { return shortName(a.name).toLowerCase(); });
  planned = planned.filter(function (p) { return started.indexOf(shortName(p.name).toLowerCase()) === -1; });
  var nodes = agents.map(function (a) { return { name: a.name, planned: false }; }).concat(planned);

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
  function box(x, y, w, hgt, cls, lines, size, dashed) {
    return '<g class="node ' + cls + '"><rect x="' + (x - w / 2) + '" y="' + (y - hgt / 2) + '" width="' + w + '" height="' + hgt +
      '" rx="10" style="fill:' + (cls === "coord" ? "var(--accent-soft)" : "var(--bg-raised)") + ";stroke:" + (cls === "coord" ? "var(--accent)" : "var(--muted)") +
      '" stroke-width="' + (cls === "coord" ? 3 : 1.5) + '"' + (dashed ? ' stroke-dasharray="6 5"' : "") + "/>" +
      textLines(lines, x, y, size, cls === "coord" ? 700 : 500) + "</g>";
  }
  function drawTeam() {
    var host = $("team-diagram");
    if (!host) return;
    var width = host.clientWidth || 700, svg;
    var title = "The coordinator in the center, connected to each agent. Agents never talk to each other; all work passes through the coordinator.";
    if (width >= 560) {
      var W = 920, H = 700, cx = W / 2, cy = H / 2, rx = 370, ry = 290, n = nodes.length;
      var edges = "", boxes = "";
      nodes.forEach(function (nd, i) {
        var ang = -Math.PI / 2 + (2 * Math.PI * i) / Math.max(n, 1);
        var x = cx + rx * Math.cos(ang), y = cy + ry * Math.sin(ang);
        edges += '<line class="edge" x1="' + cx + '" y1="' + cy + '" x2="' + x.toFixed(1) + '" y2="' + y.toFixed(1) + '"' + (nd.planned ? ' stroke-dasharray="6 6"' : "") + "/>";
        boxes += box(x, y, 136, 58, nd.planned ? "planned" : "agent", wrap(shortName(nd.name), 15), 14, nd.planned);
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
        var x = col ? VW - 4 - bw / 2 : 4 + bw / 2, y = top + row * (bh + gap) + bh / 2;
        e2 += '<line class="edge" x1="' + trunkX + '" y1="' + y + '" x2="' + (col ? x - bw / 2 : x + bw / 2) + '" y2="' + y + '"' + (nd.planned ? ' stroke-dasharray="5 5"' : "") + "/>";
        b2 += box(x, y, bw, bh, nd.planned ? "planned" : "agent", wrap(shortName(nd.name), 18), 14, nd.planned);
      });
      svg = '<svg viewBox="0 0 ' + VW + " " + VH + '" role="img" aria-labelledby="team-title"><title id="team-title">' + esc(title) + "</title>" +
        e2 + b2 + box(VW / 2, 32, 200, 50, "coord", ["Coordinator"], 18) + "</svg>";
    }
    host.innerHTML = svg + '<p class="ui" style="font-size:.82rem;color:var(--muted);text-align:center">Solid boxes: agents that have started. Dashed boxes: agents planned for later steps.</p>';
  }
  drawTeam();
  var rt, lastW = 0;
  window.addEventListener("resize", function () {
    clearTimeout(rt);
    rt = setTimeout(function () { var w = ($("team-diagram") || {}).clientWidth; if (w !== lastW) { lastW = w; drawTeam(); } }, 150);
  });

  /* ---------- 3. Build timeline ---------- */
  var TYPE_LABELS = { decision: "Decision", agent_start: "Agent started", agent_finish: "Agent finished", handoff: "Handoff", review: "Review", web_source: "Website used", correction: "Correction" };
  var tl = $("build-timeline");
  if (tl) {
    var recs = L.timeline || [];
    tl.innerHTML = recs.length ? '<div class="build-tl-wrap" tabindex="0" role="region" aria-label="Build timeline, ' + recs.length + ' events"><ol class="build-tl">' + recs.map(function (r) {
      return '<li><span class="t">' + fmtTime(r.time) + '<span class="chip type">' + esc(TYPE_LABELS[r.type] || r.type || "") + "</span></span>" + esc(r.label || r.title || "") + "</li>";
    }).join("") + "</ol></div>" : '<p class="placeholder">[No events yet]</p>';
  }

  /* ---------- 4. Agent cards ---------- */
  var cards = $("agent-cards");
  if (cards) {
    var coord = L.coordinator || {};
    var html = '<details class="agent-card" id="agent-coordinator"><summary><h3>' + esc(coord.name || "Coordinator") + '</h3><span class="role">' + esc(coord.role || "") + "</span></summary><div class=\"body\">" +
      "<h4>Decisions</h4>" + ((coord.decisions || []).length ? "<ol>" + coord.decisions.map(function (d) {
        return "<li><strong>" + esc(d.title || "") + "</strong> <span class=\"ui\" style=\"font-size:.8rem;color:var(--muted)\">" + fmtTime(d.time) + "</span><br>" + esc(d.detail || "") + "</li>";
      }).join("") + "</ol>" : '<p class="placeholder">none recorded</p>') + "</div></details>";

    html += agents.map(function (a) {
      var runs = a.runs || [];
      var last = runs[runs.length - 1] || {};
      var status = last.finished ? (last.decision || "finished") : "working";
      return '<details class="agent-card" id="agent-' + esc(a.id) + '"><summary><h3>' + esc(a.name) + '</h3> <span class="chip">' + esc(status) + '</span><span class="role">' + esc(a.role || "") + '</span></summary><div class="body">' +
        runs.map(function (r, i) {
          return "<h4>Run " + (i + 1) + "</h4><p class=\"ui\" style=\"font-size:.88rem\">Started " + fmtTime(r.started) + (r.finished ? " · finished " + fmtTime(r.finished) : " · still working") + "</p>" +
            '<p><span class="decision">Coordinator’s decision: ' + esc(r.decision || "pending") + "</span>" + (r.reason ? " — " + esc(r.reason) : "") + "</p>" +
            "<h4>What it read</h4>" + list(r.inputs) + "<h4>What it produced</h4>" + list(r.outputs);
        }).join("") +
        ((a.handoffs || []).length ? "<h4>Handoffs</h4><ul>" + a.handoffs.map(function (h) { return "<li>" + fmtTime(h.time) + ": " + esc(h.from) + " → " + esc(h.to) + ": " + esc(h.what) + "</li>"; }).join("") + "</ul>" : "") +
        ((a.reviews || []).length ? "<h4>Reviews</h4>" + list(a.reviews.map(function (r) { return r.detail || r.title || r; })) : "") +
        (a.brief ? "<details><summary>Read the exact brief it was given" + (a.brief_file ? " (" + esc(a.brief_file) + ")" : "") + "</summary><pre class=\"brief\">" + esc(a.brief) + "</pre>" +
          (a.common_rules_file ? '<p class="ui" style="font-size:.82rem">Every agent also received the common rules (' + esc(a.common_rules_file) + '), shown <a href="#common-rules">below</a>.</p>' : "") + "</details>" : "") +
        "</div></details>";
    }).join("");
    if (L.common_rules && L.common_rules.text) {
      html += '<details class="agent-card" id="common-rules"><summary><h3>Common rules given to every agent</h3><span class="role">' + esc(L.common_rules.file || "") + '</span></summary><div class="body"><pre class="brief">' + esc(L.common_rules.text) + "</pre></div></details>";
    }
    cards.innerHTML = html;
  }

  /* ---------- 5. Corrections and websites ---------- */
  function table(rows, host, empty) {
    if (!host) return;
    if (!rows || !rows.length) { host.innerHTML = '<p class="placeholder">' + empty + "</p>"; return; }
    var cols = [];
    rows.forEach(function (r) { Object.keys(r).forEach(function (k) { if (cols.indexOf(k) === -1) cols.push(k); }); });
    host.innerHTML = '<div class="table-wrap"><table><thead><tr>' + cols.map(function (c) { return "<th>" + esc(c.replace(/_/g, " ")) + "</th>"; }).join("") +
      "</tr></thead><tbody>" + rows.map(function (r) {
        return "<tr>" + cols.map(function (c) {
          var v = r[c];
          if (c === "url" && v) return '<td><a href="' + esc(v) + '" target="_blank" rel="noopener">' + esc(v) + "</a></td>";
          return "<td>" + esc(v == null ? "" : (typeof v === "object" ? JSON.stringify(v) : v)) + "</td>";
        }).join("") + "</tr>";
      }).join("") + "</tbody></table></div>";
  }
  // Corrections read better as cards than as an eight-column table, especially on phones.
  (function corrections(rows, host) {
    if (!host) return;
    if (!rows || !rows.length) { host.innerHTML = '<p class="placeholder">No corrections recorded yet.</p>'; return; }
    var LABELS = { page_item: "Where", what_it_said: "What the draft said", what_the_source_says: "What the source says", fix: "The fix", source: "Source checked", date: "Date", recorded_in: "Recorded in" };
    var skip = { number: 1 };
    host.innerHTML = '<p class="ui" style="font-size:.88rem;color:var(--muted)">' + rows.length + " corrections.</p>" +
      '<ol class="corr-list">' + rows.map(function (r, i) {
        var keys = Object.keys(r).filter(function (k) { return !skip[k] && k !== "page_item" && r[k] != null && r[k] !== ""; });
        return '<li class="corr-item"><h3>' + esc((r.number || i + 1) + ". " + (r.page_item || "")) + "</h3><dl>" +
          keys.map(function (k) {
            var v = r[k];
            return "<dt>" + esc(LABELS[k] || k.replace(/_/g, " ")) + "</dt><dd>" + esc(typeof v === "object" ? JSON.stringify(v) : v) + "</dd>";
          }).join("") + "</dl></li>";
      }).join("") + "</ol>";
  })(L.corrections, $("corrections"));
  table(L.web_sources, $("web-sources"), "No websites recorded yet.");

  var gen = $("log-generated");
  if (gen && L.generated) gen.textContent = "Build log last generated " + fmtTime(L.generated) + ".";
})();
