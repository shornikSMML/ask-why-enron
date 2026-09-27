/* Timeline: renders window.TIMELINE into #timeline, grouped by year,
   with tag filters and year jump links. Dates: "YYYY", "YYYY-MM" or "YYYY-MM-DD". */
(function () {
  "use strict";
  var A = window.AskWhy, esc = A.esc;
  var host = document.getElementById("timeline");
  var filterHost = document.getElementById("tl-filters");
  var jumpHost = document.getElementById("tl-years");
  if (!host) return;
  var items = (window.TIMELINE || []).slice();
  if (!items.length) { host.innerHTML = '<p class="none">The timeline data could not be loaded.</p>'; return; }

  var MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
  function fmt(d) {
    var p = String(d || "").split("-");
    if (p.length === 1) return p[0];
    var m = MONTHS[parseInt(p[1], 10) - 1] || p[1];
    return p.length === 2 ? m + " " + p[0] : m + " " + parseInt(p[2], 10) + ", " + p[0];
  }
  items.sort(function (a, b) { return String(a.date).localeCompare(String(b.date)); });
  // Stable anchors for pathways: an item's own id if it has one, else "tl-" + date,
  // with -2, -3... for a second or third item on the same date (in date order).
  var usedIds = {};
  function itemId(it) {
    if (it._id) return it._id;
    var base = it.id ? String(it.id) : "tl-" + String(it.date || "undated"), id = base, k = 2;
    while (usedIds[id]) id = base + "-" + k++;
    usedIds[id] = true;
    it._id = id;
    return id;
  }

  var years = [], byYear = {}, tags = {};
  items.forEach(function (it) {
    var y = String(it.date).slice(0, 4);
    if (!byYear[y]) { byYear[y] = []; years.push(y); }
    byYear[y].push(it);
    (it.tags || []).forEach(function (t) { tags[t] = true; });
  });

  host.innerHTML = years.map(function (y) {
    return '<section class="tl-section" data-year="' + y + '"><h2 class="tl-year" id="y' + y + '">' + y + '</h2><ol class="tl-list">' +
      byYear[y].map(function (it) {
        return '<li class="tl-item' + (it.epilogue ? " epilogue" : "") + '" id="' + esc(itemId(it)) + '" data-tags="' + esc((it.tags || []).join(" ")) + '">' +
          '<span class="date">' + esc(fmt(it.date)) + "</span>" +
          "<h3>" + esc(it.title) + "</h3>" +
          "<p>" + esc(it.text) + (it.cites || []).map(A.citeTag).join("") + "</p>" +
          '<div class="tags">' + (it.tags || []).map(function (t) { return '<span class="chip">' + esc(t) + "</span>"; }).join("") + "</div>" +
          "</li>";
      }).join("") + "</ol></section>";
  }).join("");

  if (jumpHost) {
    jumpHost.innerHTML = years.map(function (y) { return '<li><a href="#y' + y + '">' + y + "</a></li>"; }).join("");
  }

  var tagList = Object.keys(tags).sort();
  if (filterHost && tagList.length) {
    filterHost.innerHTML = '<span class="label" id="tl-filter-label">Show:</span>' +
      '<button type="button" class="filter-btn" data-tag="" aria-pressed="true">All</button>' +
      tagList.map(function (t) { return '<button type="button" class="filter-btn" data-tag="' + esc(t) + '" aria-pressed="false">' + esc(t) + "</button>"; }).join("");
    filterHost.addEventListener("click", function (e) {
      var b = e.target.closest("button[data-tag]");
      if (!b) return;
      var tag = b.getAttribute("data-tag");
      Array.prototype.forEach.call(filterHost.querySelectorAll("button"), function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      Array.prototype.forEach.call(host.querySelectorAll(".tl-item"), function (li) {
        li.hidden = !!tag && (" " + li.getAttribute("data-tags") + " ").indexOf(" " + tag + " ") === -1;
      });
      Array.prototype.forEach.call(host.querySelectorAll(".tl-section"), function (sec) {
        sec.hidden = !sec.querySelector(".tl-item:not([hidden])");
      });
    });
    // ?tag=legal (e.g. from a pathway) starts with that filter on.
    var m = /[?&]tag=([a-z-]+)/.exec(location.search);
    if (m) {
      var btn = filterHost.querySelector('button[data-tag="' + m[1] + '"]');
      if (btn) btn.click(); else console.warn("Timeline: unknown tag in URL:", m[1]);
    }
  }
})();
