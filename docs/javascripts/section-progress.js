/* Section hub progress bars (data from reports/content-inventory.csv via page-trust-data.js). */
(function () {
  "use strict";

  var SECTION_CLASS = {
    "hub-page--cheatsheet": "cheatsheet",
    "hub-page--arch": "arch",
    "hub-page--dev": "dev",
  };

  function detectLocale() {
    var lang = (document.documentElement.getAttribute("lang") || "en").toLowerCase();
    if (lang.indexOf("fa") === 0) return "fa";
    if (lang.indexOf("zh") === 0) return "zh";
    var path = location.pathname;
    if (/^\/fa(\/|$)/.test(path)) return "fa";
    if (/^\/zh(\/|$)/.test(path)) return "zh";
    return "en";
  }

  function pct(count, total) {
    if (!total) return 0;
    return Math.round((100 * count) / total);
  }

  function progressBar(label, count, total) {
    var value = pct(count, total);
    var row = document.createElement("div");
    row.className = "hub-progress__row";

    var head = document.createElement("div");
    head.className = "hub-progress__head";
    head.innerHTML =
      '<span class="hub-progress__label">' +
      label +
      '</span><span class="hub-progress__pct">' +
      value +
      "%</span>";

    var track = document.createElement("div");
    track.className = "hub-progress__track";
    track.setAttribute("role", "progressbar");
    track.setAttribute("aria-valuemin", "0");
    track.setAttribute("aria-valuemax", "100");
    track.setAttribute("aria-valuenow", String(value));
    track.setAttribute("aria-label", label);

    var fill = document.createElement("div");
    fill.className = "hub-progress__fill";
    fill.style.width = value + "%";
    track.appendChild(fill);

    row.appendChild(head);
    row.appendChild(track);
    return row;
  }

  function renderSectionProgress() {
    var manifest = window.PAGE_TRUST;
    if (!manifest || !manifest.sections) return;

    var hub = document.querySelector(".hub-page.hub-page--section");
    if (!hub) return;

    var sectionKey = null;
    Object.keys(SECTION_CLASS).some(function (cls) {
      if (hub.classList.contains(cls)) {
        sectionKey = SECTION_CLASS[cls];
        return true;
      }
      return false;
    });
    if (!sectionKey) return;

    var stats = manifest.sections[sectionKey];
    if (!stats || !stats.total) return;

    var locale = detectLocale();
    var strings =
      (manifest.progressStrings && manifest.progressStrings[locale]) ||
      (manifest.progressStrings && manifest.progressStrings.en) ||
      {};

    var host = hub.querySelector(".hub-hero__stats");
    if (!host || hub.querySelector(".hub-progress")) return;

    var wrap = document.createElement("div");
    wrap.className = "hub-progress";
    wrap.setAttribute("aria-label", strings.title || "Documentation progress");

    var meta = document.createElement("p");
    meta.className = "hub-progress__meta";
    meta.textContent =
      (strings.title || "Documentation progress") +
      " · " +
      stats.total +
      " " +
      (strings.pages || "pages");
    wrap.appendChild(meta);

    wrap.appendChild(progressBar(strings.enComplete || "EN complete", stats.enComplete, stats.total));
    wrap.appendChild(progressBar(strings.faComplete || "FA complete", stats.faComplete, stats.total));
    wrap.appendChild(progressBar(strings.zhComplete || "ZH complete", stats.zhComplete, stats.total));
    wrap.appendChild(
      progressBar(strings.humanReview || "Human reviewed", stats.humanReviewed, stats.total)
    );
    wrap.appendChild(
      progressBar(strings.contentComplete || "Content complete", stats.contentComplete, stats.total)
    );

    host.insertAdjacentElement("afterend", wrap);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", renderSectionProgress);
  } else {
    renderSectionProgress();
  }
})();
