/* Page trust badges + toasts (human-reviewed vs auto-generated). */
(function () {
  "use strict";

  function detectLocale() {
    var lang = (document.documentElement.getAttribute("lang") || "en").toLowerCase();
    if (lang.indexOf("fa") === 0) return "fa";
    if (lang.indexOf("zh") === 0) return "zh";
    var path = location.pathname;
    if (/^\/fa(\/|$)/.test(path)) return "fa";
    if (/^\/zh(\/|$)/.test(path)) return "zh";
    return "en";
  }

  function normalizeUrlPath(pathname) {
    var p = pathname || "/";
    p = p.replace(/\/index\.html$/i, "").replace(/\/+$/, "");
    p = p.replace(/^\/(en|fa|zh)(?=\/|$)/, "") || "/";
    return p === "" ? "/" : p;
  }

  function resolveSourceKey(manifest, pathname) {
    var urlPath = normalizeUrlPath(pathname);
    var map = manifest.urlToSource || {};
    if (map[urlPath]) return map[urlPath];
    if (urlPath !== "/" && map[urlPath + "/"]) return map[urlPath + "/"];
    return null;
  }

  function resolveStatus(manifest, locale) {
    var source = resolveSourceKey(manifest, location.pathname);
    if (!source) return null;
    var entry = (manifest.pages || {})[source];
    if (!entry) return null;
    return entry[locale] || entry.en || null;
  }

  function stringsFor(manifest, locale) {
    var all = manifest.strings || {};
    return all[locale] || all.en || {};
  }

  function createBadge(status, strings) {
    var el = document.createElement("div");
    el.className =
      "page-trust-badge page-trust-badge--" +
      (status === "human-reviewed" ? "human" : "auto");
    el.setAttribute("role", "status");

    var icon = document.createElement("span");
    icon.className = "page-trust-badge__icon";
    icon.setAttribute("aria-hidden", "true");
    icon.textContent = status === "human-reviewed" ? "✓" : "⚙";

    var label = document.createElement("span");
    label.className = "page-trust-badge__label";
    label.textContent =
      status === "human-reviewed" ? strings.badgeHuman : strings.badgeAuto;

    el.appendChild(icon);
    el.appendChild(label);
    return el;
  }

  function showToast(status, strings) {
    var isHuman = status === "human-reviewed";
    var toast = document.createElement("div");
    toast.className =
      "page-trust-toast page-trust-toast--" + (isHuman ? "human" : "auto");
    toast.setAttribute("role", isHuman ? "status" : "alert");
    toast.setAttribute("aria-live", "polite");

    var title = document.createElement("div");
    title.className = "page-trust-toast__title";
    title.textContent = isHuman ? strings.toastHumanTitle : strings.toastAutoTitle;

    var body = document.createElement("div");
    body.className = "page-trust-toast__body";
    body.textContent = isHuman ? strings.toastHumanBody : strings.toastAutoBody;

    var actions = document.createElement("div");
    actions.className = "page-trust-toast__actions";

    var close = document.createElement("button");
    close.type = "button";
    close.className = "page-trust-toast__close";
    close.textContent = strings.toastDismiss;
    close.addEventListener("click", function () {
      toast.classList.add("page-trust-toast--hide");
      window.setTimeout(function () {
        toast.remove();
      }, 280);
    });

    actions.appendChild(close);
    toast.appendChild(title);
    toast.appendChild(body);
    toast.appendChild(actions);
    document.body.appendChild(toast);

    window.requestAnimationFrame(function () {
      toast.classList.add("page-trust-toast--visible");
    });

    window.setTimeout(function () {
      if (toast.parentNode) {
        toast.classList.add("page-trust-toast--hide");
        window.setTimeout(function () {
          toast.remove();
        }, 280);
      }
    }, isHuman ? 9000 : 12000);
  }

  function mountBadge(badge) {
    var content = document.querySelector(".md-content__inner");
    if (!content) return;
    var h1 = content.querySelector("h1");
    if (h1) {
      h1.insertAdjacentElement("afterend", badge);
      return;
    }
    content.insertBefore(badge, content.firstChild);
  }

  function init() {
    if (document.querySelector(".hub-page")) return;

    var manifest = window.PAGE_TRUST;
    if (!manifest || !manifest.pages) return;

    var locale = detectLocale();
    var status = resolveStatus(manifest, locale);
    if (!status) return;

    var strings = stringsFor(manifest, locale);
    mountBadge(createBadge(status, strings));
    showToast(status, strings);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
