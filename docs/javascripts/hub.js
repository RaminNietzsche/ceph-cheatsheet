document.addEventListener("DOMContentLoaded", function () {
  var hub = document.querySelector(".hub-page");
  if (!hub) return;

  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var nav = hub.querySelector(".hub-nav");

  function getScrollY() {
    return window.scrollY || document.documentElement.scrollTop || 0;
  }

  function scrollToTarget(target) {
    if (!target) return;
    var offset = nav ? nav.offsetHeight + 16 : 16;
    var top = target.getBoundingClientRect().top + getScrollY() - offset;
    window.scrollTo({ top: top, behavior: reducedMotion ? "auto" : "smooth" });
  }

  hub.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener("click", function (e) {
      var id = this.getAttribute("href");
      if (!id || id.length <= 1) return;
      var target = hub.querySelector(id) || document.querySelector(id);
      if (!target) return;
      e.preventDefault();
      scrollToTarget(target);
      if (history.replaceState) {
        history.replaceState(null, "", id);
      }
    });
  });

  if (nav) {
    var updateNav = function () {
      nav.classList.toggle("hub-nav--scrolled", getScrollY() > 24);
    };
    updateNav();
    window.addEventListener("scroll", updateNav, { passive: true });
  }

  var scrollHint = hub.querySelector(".hub-scroll-hint");
  if (scrollHint) {
    var updateHint = function () {
      var hidden = getScrollY() > 120;
      scrollHint.style.opacity = hidden ? "0" : "1";
      scrollHint.style.pointerEvents = hidden ? "none" : "auto";
    };
    updateHint();
    window.addEventListener("scroll", updateHint, { passive: true });
  }

  hub.querySelectorAll(".hub-section__head, .hub-split, .hub-develop-box, .hub-footer").forEach(function (el) {
    el.classList.add("hub-reveal");
  });

  hub.querySelectorAll(".hub-cards").forEach(function (grid) {
    grid.querySelectorAll(".hub-card").forEach(function (card, i) {
      card.classList.add("hub-reveal");
      if (i === 1) card.classList.add("hub-reveal--delay-1");
      if (i === 2) card.classList.add("hub-reveal--delay-2");
    });
  });

  if ("IntersectionObserver" in window) {
    var revealObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("hub-reveal--visible");
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { root: null, rootMargin: "0px 0px -6% 0px", threshold: 0.1 }
    );

    hub.querySelectorAll(".hub-reveal").forEach(function (el) {
      if (reducedMotion) {
        el.classList.add("hub-reveal--visible");
      } else {
        revealObserver.observe(el);
      }
    });
  } else {
    hub.querySelectorAll(".hub-reveal").forEach(function (el) {
      el.classList.add("hub-reveal--visible");
    });
  }

  if (reducedMotion) return;

  function animateCounter(el) {
    var text = el.textContent.trim();
    if (text === "\u221E" || text === "\u221e" || text.indexOf("\u221E") !== -1) return;

    var match = text.match(/^(\d+(?:\.\d+)?)(.*)$/);
    if (!match) return;

    var target = parseFloat(match[1], 10);
    var suffix = match[2] || "";
    var duration = 1400;
    var startTime = null;

    function step(ts) {
      if (!startTime) startTime = ts;
      var progress = Math.min((ts - startTime) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      var current = target * eased;

      el.textContent =
        (Number.isInteger(target) ? Math.round(current) : current.toFixed(2)) + suffix;

      if (progress < 1) requestAnimationFrame(step);
    }

    el.textContent = "0" + suffix;
    requestAnimationFrame(step);
  }

  var statsBlock = hub.querySelector(".hub-hero__stats");
  if (statsBlock && "IntersectionObserver" in window) {
    var statsObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.querySelectorAll(".hub-hero__stat-val").forEach(animateCounter);
          statsObserver.unobserve(entry.target);
        });
      },
      { threshold: 0.4 }
    );
    statsObserver.observe(statsBlock);
  }
});
