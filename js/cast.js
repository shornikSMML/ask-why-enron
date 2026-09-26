/* Cast of Characters: renders window.CAST into #cast.
   Outcome labels are deliberately neutral: same color for every outcome,
   plain factual wording. The label is only a summary; outcome_text (with
   citations) says precisely what happened. */
(function () {
  "use strict";
  var A = window.AskWhy, esc = A.esc;
  var OUTCOME_LABELS = {
    "convicted": "Convicted",
    "pleaded-guilty": "Pleaded guilty",
    "conviction-vacated": "Conviction vacated",
    "conviction-reversed": "Conviction reversed",
    "conviction-narrowed": "Conviction narrowed on appeal",
    "acquitted": "Acquitted",
    "sec-settled": "Settled with the SEC",
    "charged": "Charged",
    "civil-only": "Civil case only",
    "not-charged": "Not charged",
    "not-covered": "Outcome not covered by our sources",
    "other": "See details",
    // Wording used in the Reference Writer's brief (10-reference-writer.md):
    "convicted \u2014 later narrowed on appeal": "Convicted; later narrowed on appeal",
    "conviction vacated (died before appeal)": "Conviction vacated (died before appeal)",
    "conviction vacated after his death": "Conviction vacated after his death",
    "conviction reversed": "Conviction reversed",
    "pleaded guilty": "Pleaded guilty",
    "SEC settlement": "SEC settlement",
    "charged \u2014 outcome not in library": "Charged; outcome not in our sources",
    "not charged (per source)": "Not charged (per source)",
    "no charges shown in library": "No charges shown in our sources",
    "not accused of wrongdoing": "Not accused of wrongdoing"
  };
  function labelFor(status) {
    if (OUTCOME_LABELS[status]) return OUTCOME_LABELS[status];
    var norm = String(status || "").replace(/\s+-{1,2}\s+/g, " \u2014 ");
    if (OUTCOME_LABELS[norm]) return OUTCOME_LABELS[norm];
    if (status) { console.warn("Cast: unlisted outcome_status shown as written:", status); return status.charAt(0).toUpperCase() + status.slice(1); }
    return OUTCOME_LABELS.other;
  }
  var host = document.getElementById("cast");
  if (!host) return;
  var list = window.CAST || [];
  if (!list.length) { host.innerHTML = '<p class="none">The Cast of Characters data could not be loaded.</p>'; return; }

  host.innerHTML = list.map(function (p) {
    var label = labelFor(p.outcome_status);
    var cites = (p.cites || []).map(A.citeTag).join("");
    return '<article class="person" id="' + esc(p.id) + '">' +
      (p.image ? '<figure data-image="' + esc(p.image) + '" data-alt="' + esc(p.name) + '"></figure>' : "") +
      "<h2>" + esc(p.name) + "</h2>" +
      '<p class="role">' + esc(p.role) + "</p>" +
      "<p>" + esc(p.summary) + "</p>" +
      '<div class="outcome"><span class="outcome-label">' + esc(label) + "</span>" +
      "<p>" + esc(p.outcome_text) + cites + "</p></div>" +
      "</article>";
  }).join("");
})();
