/* Force hub dark theme (slate) on all pages for consistent look */
(function () {
  var key = "__palette";
  try {
    localStorage.setItem(key, JSON.stringify({ index: 0, color: { scheme: "slate" } }));
  } catch (e) {
    /* ignore */
  }
  document.body.setAttribute("data-md-color-scheme", "slate");
  document.addEventListener("DOMContentLoaded", function () {
    document.body.setAttribute("data-md-color-scheme", "slate");
  });
})();
