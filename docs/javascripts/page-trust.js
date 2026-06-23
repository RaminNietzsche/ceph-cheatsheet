/* Page trust badges + toasts (human-reviewed / auto-generated / unreviewed). */
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
    if (p.length > 1 && p.charAt(0) === "/") {
      p = p.slice(1);
    }
    return p === "" ? "/" : p;
  }

  function resolveSourceKey(manifest, pathname) {
    var urlPath = normalizeUrlPath(pathname);
    var map = manifest.urlToSource || {};
    if (map[urlPath]) return map[urlPath];
    if (urlPath !== "/" && map["/" + urlPath]) return map["/" + urlPath];
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

  function statusClass(status) {
    if (status === "human-reviewed") return "human";
    if (status === "auto-generated") return "auto";
    return "unreviewed";
  }

  function badgeLabel(status, strings) {
    if (status === "human-reviewed") return strings.badgeHuman;
    if (status === "auto-generated") return strings.badgeAuto;
    return strings.badgeUnreviewed;
  }

  function badgeIcon(status) {
    if (status === "human-reviewed") return "✓";
    if (status === "auto-generated") return "⚙";
    return "i";
  }

  function toastTitle(status, strings) {
    if (status === "human-reviewed") return strings.toastHumanTitle;
    if (status === "auto-generated") return strings.toastAutoTitle;
    return strings.toastUnreviewedTitle;
  }

  function toastBody(status, strings) {
    if (status === "human-reviewed") return strings.toastHumanBody;
    if (status === "auto-generated") return strings.toastAutoBody;
    return strings.toastUnreviewedBody;
  }

  function createBadge(status, strings) {
    var el = document.createElement("div");
    el.className = "page-trust-badge page-trust-badge--" + statusClass(status);
    el.setAttribute("role", "status");

    var icon = document.createElement("span");
    icon.className = "page-trust-badge__icon";
    icon.setAttribute("aria-hidden", "true");
    icon.textContent = badgeIcon(status);

    var label = document.createElement("span");
    label.className = "page-trust-badge__label";
    label.textContent = badgeLabel(status, strings);

    el.appendChild(icon);
    el.appendChild(label);
    return el;
  }

  function showToast(status, strings) {
    var isHuman = status === "human-reviewed";
    var toast = document.createElement("div");
    toast.className = "page-trust-toast page-trust-toast--" + statusClass(status);
    toast.setAttribute("role", isHuman ? "status" : "alert");
    toast.setAttribute("aria-live", "polite");

    var title = document.createElement("div");
    title.className = "page-trust-toast__title";
    title.textContent = toastTitle(status, strings);

    var body = document.createElement("div");
    body.className = "page-trust-toast__body";
    body.textContent = toastBody(status, strings);

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

    var duration = isHuman ? 9000 : 11000;
    window.setTimeout(function () {
      if (toast.parentNode) {
        toast.classList.add("page-trust-toast--hide");
        window.setTimeout(function () {
          toast.remove();
        }, 280);
      }
    }, duration);
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
    var manifest = window.PAGE_TRUST;
    if (!manifest || !manifest.pages) return;

    var locale = detectLocale();
    var status = resolveStatus(manifest, locale);
    if (!status) return;

    var strings = stringsFor(manifest, locale);
    if (!document.querySelector(".hub-page")) {
      mountBadge(createBadge(status, strings));
    }
    showToast(status, strings);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
