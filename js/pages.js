/* inner-page extras, after site.js. active nav, drawer groups, the page
   heading animation, and anchor offsets for the fixed header. */
(function () {
  "use strict";

  function onReady(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  onReady(function () {
    /* two ways to match: the data-nav key or the file name. key wins, so a
       case study lights up Client Stories and not its own name. */
    var file = window.location.pathname.split("/").pop() || "index.html";
    var navKey = document.body.getAttribute("data-nav") || "";

    [].forEach.call(
      document.querySelectorAll(".nav-link, .mobile-nav-link, .mobile-nav-sub a"),
      function (link) {
        var href = link.getAttribute("href") || "";
        var key = link.getAttribute("data-nav-key") || "";
        var target = href.split("#")[0].split("/").pop();
        var match = (navKey && key === navKey) || (target && target === file);
        link.classList.toggle("active", !!match);
      }
    );

    /* collapsible groups in the mobile drawer. */
    [].forEach.call(document.querySelectorAll(".mobile-nav-group-toggle"), function (t) {
      t.addEventListener("click", function () {
        var group = t.closest(".mobile-nav-group");
        if (group) group.classList.toggle("open");
      });
    });

    /* site.js only splits .section-title and .hero-title, and these are
       .page-title, so build the markup it expects by hand. */
    var reduce =
      window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    var pageTitle = document.querySelector(".page-title");
    if (pageTitle && !pageTitle.dataset.revealReady) {
      var tokens = [];
      [].forEach.call(pageTitle.childNodes, function (node) {
        var cls = node.nodeType === 1 ? node.className || "" : "";
        (node.textContent || "").split(/\s+/).forEach(function (word) {
          if (word) tokens.push({ text: word, cls: cls });
        });
      });

      pageTitle.innerHTML = tokens
        .map(function (t) {
          return (
            '<span class="r-word"><span' +
            (t.cls ? ' class="' + t.cls + '"' : "") +
            ">" +
            t.text +
            "</span></span>"
          );
        })
        .join(" ");

      pageTitle.classList.add("reveal-h");
      pageTitle.dataset.revealReady = "1";

      [].forEach.call(pageTitle.querySelectorAll(".r-word > span"), function (s, i) {
        s.style.transitionDelay = i * 55 + "ms";
      });

      if (reduce) {
        pageTitle.classList.add("is-in");
      } else {
        setTimeout(function () {
          pageTitle.classList.add("is-in");
        }, 180);
      }
    }

    /* anchors offset 92px so the fixed header doesn't cover the target */
    [].forEach.call(document.querySelectorAll('a[href^="#"]'), function (a) {
      a.addEventListener("click", function (e) {
        var id = a.getAttribute("href");
        if (!id || id.length < 2) return;
        var target = document.querySelector(id);
        if (!target) return;
        e.preventDefault();
        window.scrollTo({
          top: target.getBoundingClientRect().top + window.scrollY - 92,
          behavior: reduce ? "auto" : "smooth"
        });
      });
    });
  });
})();
