// sidebar.js — in-rail accordion navigation + live filter.
//
// Replaces the old hover/click flyout. Designed to scale to 34+ calculators
// per section (Trig, Calculus) without clutter:
//   * Each SECTION expands in place (one open at a time).
//   * Each SUB-GROUP is a native <details>, collapsed by default.
//   * A live filter box narrows the whole tree by calculator name, expanding
//     only the sections/sub-groups that contain a match.
//
// SEO-safe: every calculator link stays a real <a href> in the DOM at all
// times — collapsing only hides it visually. No JS-only navigation.
// Plug-and-play: reads whatever the registry rendered; no per-calc wiring.
(function () {
  var sidebar = document.getElementById("sidebar");
  if (!sidebar) return;

  var sections = Array.prototype.slice.call(
    sidebar.querySelectorAll(".side-section"));

  // ---- section accordion --------------------------------------------------
  function setOpen(sec, open) {
    sec.classList.toggle("open", open);
    var caretBtn = sec.querySelector(".side-section-caret-btn");
    if (caretBtn) caretBtn.setAttribute("aria-expanded", open ? "true" : "false");
  }
  function closeAllExcept(keep) {
    sections.forEach(function (sec) { if (sec !== keep) setOpen(sec, false); });
  }

  sections.forEach(function (sec) {
    // The caret button toggles the tree in place WITHOUT navigating.
    var caretBtn = sec.querySelector(".side-section-caret-btn");
    if (caretBtn) {
      caretBtn.addEventListener("click", function (e) {
        e.preventDefault();
        var willOpen = !sec.classList.contains("open");
        closeAllExcept(sec);      // one section open at a time
        setOpen(sec, willOpen);
      });
    }
    // The section NAME both expands the tree and navigates to the master page.
    // We open it first (so the destination loads with this section expanded),
    // then let the link follow normally.
    var nameLink = sec.querySelector(".side-section-link");
    if (nameLink) {
      nameLink.addEventListener("click", function () {
        closeAllExcept(sec);
        setOpen(sec, true);
        // no preventDefault — the browser navigates to /section/<id>
      });
    }
  });

  // ---- highlight the calculator / section for the current page ------------
  // Helps a student see "where am I" in a long list. Pure presentation.
  (function highlightCurrent() {
    var path = window.location.pathname;
    var here = sidebar.querySelector('.side-calc[href="' + path + '"]');
    if (here) {
      here.classList.add("is-current");
      here.setAttribute("aria-current", "page");
      var sub = here.closest("details.side-sub");
      if (sub) sub.open = true;                 // reveal its sub-group
      var topic = here.closest("details.side-topic");
      if (topic) topic.open = true;             // and its topic
      var sec = here.closest(".side-section");
      if (sec) setOpen(sec, true);              // and open its section
      return;
    }
    // On a /section/<id> page, open that section in the rail.
    var m = path.match(/^\/section\/([^\/]+)/);
    if (m) {
      var sec2 = sidebar.querySelector('.side-section[data-section="' + m[1] + '"]');
      if (sec2) setOpen(sec2, true);
    }
  })();

  // ---- live filter --------------------------------------------------------
  var input = document.getElementById("side-filter-input");
  var clearBtn = document.getElementById("side-filter-clear");
  var emptyMsg = document.getElementById("side-filter-empty");
  if (!input) return;

  // Remember each section's open/closed + each sub-group's open state so we can
  // restore it when the filter is cleared.
  var savedSubState = null;

  function snapshot() {
    if (savedSubState) return;               // only snapshot once, before filtering
    savedSubState = sections.map(function (sec) {
      return {
        open: sec.classList.contains("open"),
        subs: Array.prototype.slice
          .call(sec.querySelectorAll("details.side-sub, details.side-topic"))
          .map(function (d) { return d.open; })
      };
    });
  }
  function restore() {
    if (!savedSubState) return;
    sections.forEach(function (sec, i) {
      setOpen(sec, savedSubState[i].open);
      var subs = sec.querySelectorAll("details.side-sub, details.side-topic");
      Array.prototype.forEach.call(subs, function (d, j) {
        d.open = savedSubState[i].subs[j];
        d.classList.remove("filter-hit");
      });
    });
    sec_show_all();
    savedSubState = null;
  }
  function sec_show_all() {
    sections.forEach(function (sec) { sec.style.display = ""; });
    sidebar.querySelectorAll(".side-calc").forEach(function (a) {
      a.style.display = "";
    });
    sidebar.querySelectorAll("details.side-sub, details.side-topic").forEach(function (d) {
      d.style.display = "";
    });
  }

  function applyFilter(q) {
    q = q.trim().toLowerCase();
    clearBtn.hidden = q === "";

    if (q === "") { restore(); emptyMsg.hidden = true; return; }

    snapshot();
    var anyHit = false;

    sections.forEach(function (sec) {
      var sectionHasHit = false;
      var subs = sec.querySelectorAll("details.side-sub");

      Array.prototype.forEach.call(subs, function (d) {
        var subHasHit = false;
        var calcs = d.querySelectorAll(".side-calc");
        Array.prototype.forEach.call(calcs, function (a) {
          var hit = (a.getAttribute("data-name") || "").indexOf(q) !== -1;
          a.style.display = hit ? "" : "none";
          if (hit) subHasHit = true;
        });
        d.style.display = subHasHit ? "" : "none";
        d.open = subHasHit;                  // auto-expand groups with matches
        d.classList.toggle("filter-hit", subHasHit);
        if (subHasHit) sectionHasHit = true;
      });

      // Topic wrappers: show/expand only if they contain a matched sub-group.
      var topics = sec.querySelectorAll("details.side-topic");
      Array.prototype.forEach.call(topics, function (tp) {
        var visibleSub = tp.querySelector(
          'details.side-sub:not([style*="display: none"])');
        var topicHasHit = !!visibleSub;
        tp.style.display = topicHasHit ? "" : "none";
        tp.open = topicHasHit;
      });

      sec.style.display = sectionHasHit ? "" : "none";
      setOpen(sec, sectionHasHit);           // auto-open sections with matches
      if (sectionHasHit) anyHit = true;
    });

    emptyMsg.hidden = anyHit;
  }

  var t = null;
  input.addEventListener("input", function () {
    clearTimeout(t);
    t = setTimeout(function () { applyFilter(input.value); }, 80);
  });
  input.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { input.value = ""; applyFilter(""); }
  });
  clearBtn.addEventListener("click", function () {
    input.value = ""; applyFilter(""); input.focus();
  });
})();
