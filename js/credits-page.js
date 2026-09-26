/* Image credits page: renders window.IMAGE_CREDITS as a table. */
(function () {
  "use strict";
  var A = window.AskWhy, esc = A.esc;
  var host = document.getElementById("credits");
  if (!host) return;
  var list = window.IMAGE_CREDITS || [];
  if (!list.length) { host.innerHTML = '<p class="placeholder">[Image credits coming]</p>'; return; }
  host.innerHTML = '<div class="table-wrap"><table><thead><tr><th>Image</th><th>Author</th><th>License</th><th>Source</th></tr></thead><tbody>' +
    list.map(function (img) {
      return '<tr id="img-' + esc(img.id) + '"><td><a href="' + esc(A.imageSrc(img)) + '">' + esc(img.title || img.id) + "</a>" +
        (img.description ? '<br><span class="meta" style="font-size:.8rem;color:var(--muted)">' + esc(img.description) + "</span>" : "") + "</td>" +
        "<td>" + (img.is_original_diagram ? "Original diagram for this site" : esc(img.author || "")) + "</td>" +
        "<td>" + (img.license_url ? '<a href="' + esc(img.license_url) + '" target="_blank" rel="noopener">' + esc(img.license) + "</a>" : esc(img.license || "")) + "</td>" +
        "<td>" + (img.source_url ? '<a href="' + esc(img.source_url) + '" target="_blank" rel="noopener">Link</a>' : "") + "</td></tr>";
    }).join("") + "</tbody></table></div>";
})();
