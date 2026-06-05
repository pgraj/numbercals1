/* ncangle.js — NumberCals shared Degrees/Radians unit toggle.
 *
 * OPT-IN, like nclearn.js: only trig vizzes that include _angle_unit.html and
 * this script get the toggle. Non-trig calculators never load it, so the other
 * ~90 calculators are completely unaffected.
 *
 * Public API:
 *   NCAngle.current()        -> "deg" | "rad"   (session default: "deg")
 *   NCAngle.set(unit)        -> set + broadcast (used by the toggle buttons)
 *   NCAngle.onChange(cb)     -> cb(unit) fires whenever the unit changes
 *   NCAngle.fmtAngle(deg)    -> display string for an angle given in DEGREES,
 *                               rendered in the current unit (e.g. "30°" or
 *                               "0.5236 rad"). Maths itself stays server-side;
 *                               this is only for convenience labels.
 *   NCAngle.label()          -> "degrees" | "radians"
 *   NCAngle.symbol()         -> "°" | "rad"
 *
 * Persistence: in-memory for the session (NOT localStorage — page-level pref,
 * and storage APIs are unavailable in some embeds). Survives input edits and
 * theme changes; resets on full reload, which is fine for a display preference.
 *
 * Events: dispatches a window "nc-angle-change" CustomEvent({detail:{unit}}).
 * Each viz listens and re-calls its own compute() with the new angle_unit so
 * results AND step-by-step working re-derive in the chosen unit.
 */
(function () {
  "use strict";

  var UNIT = "deg";              // session default
  var listeners = [];

  function broadcast() {
    listeners.forEach(function (cb) {
      try { cb(UNIT); } catch (e) { /* never throw */ }
    });
    try {
      window.dispatchEvent(new CustomEvent("nc-angle-change",
        { detail: { unit: UNIT } }));
    } catch (e) { /* old browsers: listeners array still fired above */ }
  }

  var NCAngle = {
    current: function () { return UNIT; },

    set: function (unit) {
      var u = (unit === "rad") ? "rad" : "deg";
      if (u === UNIT) return UNIT;
      UNIT = u;
      // Restyle any toggle buttons present, then notify.
      syncButtons();
      broadcast();
      return UNIT;
    },

    onChange: function (cb) {
      if (typeof cb === "function") listeners.push(cb);
    },

    label: function () { return UNIT === "rad" ? "radians" : "degrees"; },
    symbol: function () { return UNIT === "rad" ? "rad" : "\u00B0"; },

    fmtAngle: function (deg) {
      if (deg === null || deg === undefined || isNaN(deg)) return "";
      if (UNIT === "rad") {
        var r = deg * Math.PI / 180;
        return (Math.round(r * 1e4) / 1e4) + " rad";
      }
      return (Math.round(deg * 1e4) / 1e4) + "\u00B0";
    }
  };

  // ---- Toggle button wiring -------------------------------------------------
  // _angle_unit.html renders buttons with [data-nc-angle="deg"|"rad"]. We wire
  // them here so the partial stays markup-only. Buttons may appear after this
  // script loads, so we also expose syncButtons() and bind on DOMContentLoaded.
  function styleButtons() {
    var s = window.NCSkin || {};
    var ink = s.ink || "#222", accent = s.accent || "#b34a23",
        rule = s.rule || "#ccc", paper2 = s.paper2 || "transparent",
        paper = s.paper || "#fff", sans = s.sans || "sans-serif";
    document.querySelectorAll("[data-nc-angle]").forEach(function (b) {
      var on = b.getAttribute("data-nc-angle") === UNIT;
      b.style.cursor = "pointer";
      b.style.border = "none";
      b.style.padding = "6px 14px";
      b.style.font = "13px " + sans;
      b.style.background = on ? accent : paper2;
      b.style.color = on ? paper : ink;
    });
    document.querySelectorAll(".nc-angle-seg").forEach(function (seg) {
      seg.style.display = "inline-flex";
      seg.style.border = "1px solid " + rule;
      seg.style.borderRadius = "8px";
      seg.style.overflow = "hidden";
      seg.style.margin = "2px 0 10px";
    });
  }

  function syncButtons() {
    document.querySelectorAll("[data-nc-angle]").forEach(function (b) {
      var on = b.getAttribute("data-nc-angle") === UNIT;
      b.classList.toggle("active", on);
      b.setAttribute("aria-pressed", String(on));
    });
    styleButtons();
  }

  function bind() {
    document.querySelectorAll("[data-nc-angle]").forEach(function (b) {
      if (b.__ncBound) return;
      b.__ncBound = true;
      b.addEventListener("click", function () {
        NCAngle.set(b.getAttribute("data-nc-angle"));
      });
    });
    syncButtons();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bind);
  } else {
    bind();
  }
  window.addEventListener("nc-theme-change", styleButtons);

  // Expose for vizzes that build toggles after load.
  NCAngle._bind = bind;
  NCAngle._sync = syncButtons;
  window.NCAngle = NCAngle;
})();
