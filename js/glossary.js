/* Glossary page: renders window.GLOSSARY into #glossary, alphabetically,
   with a filter box. Each entry's id is its anchor (glossary.html#id). */
(function () {
  "use strict";
  var A = window.AskWhy, esc = A.esc;
  var host = document.getElementById("glossary");
  var search = document.getElementById("gloss-search");
  if (!host) return;
  var G = window.GLOSSARY || {};
  var ids = Object.keys(G);
  if (!ids.length) {
    host.innerHTML = '<p class="none">The glossary data could not be loaded.</p>';
    if (search) search.parentNode.hidden = true;
    return;
  }
  ids.sort(function (a, b) { return String(G[a].term || a).localeCompare(String(G[b].term || b)); });
  host.innerHTML = '<dl class="gloss-list">' + ids.map(function (id) {
    var g = G[id];
    var see = (g.see_also || g.see || []).map(function (s) { return '<a href="#' + esc(s) + '">' + esc(G[s] ? G[s].term : s) + "</a>"; }).join(", ");
    return '<dt id="' + esc(id) + '">' + esc(g.term || id) + "</dt>" +
      "<dd><p>" + esc(g.short || g.definition || "") + "</p>" +
      (g.long ? "<p>" + esc(g.long) + "</p>" : "") +
      ((g.cites && g.cites.length) ? "<p>" + g.cites.map(A.citeTag).join("") + "</p>" : "") +
      (see ? '<p class="ui" style="font-size:.85rem">See also: ' + see + "</p>" : "") + "</dd>";
  }).join("") + "</dl>";
  if (search) {
    search.addEventListener("input", function () {
      var q = search.value.trim().toLowerCase();
      Array.prototype.forEach.call(host.querySelectorAll("dt"), function (dt) {
        var dd = dt.nextElementSibling;
        var hit = !q || (dt.textContent + " " + dd.textContent).toLowerCase().indexOf(q) !== -1;
        dt.hidden = dd.hidden = !hit;
      });
    });
  }
})();
