/* Copy-to-clipboard success feedback (#31) */
document.addEventListener("DOMContentLoaded", function () {
  if (document.querySelector(".hub-page")) return;

  document.querySelectorAll(".md-clipboard").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var el = btn;
      el.classList.add("copy-success");
      window.setTimeout(function () {
        el.classList.remove("copy-success");
      }, 1500);
    });
  });
});
