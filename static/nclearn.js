/* nclearn.js — NumberCals shared learning engine (Trigonometry build, Stage 1)
 *
 * Gives a calculator two MODES behind an .nc-seg-style toggle:
 *   - Steps     : delegates to the EXISTING window.NCSteps.render(data.steps).
 *                 NCLearn does NOT reinvent step rendering; it only reveals the
 *                 shared #nc-steps panel that _steps.html already provides.
 *   - Animation : a per-calc requestAnimationFrame canvas loop with pause/play.
 *
 * Public API (one call per viz, after each compute):
 *   NCLearn.mount({
 *     slug:  "<calc-slug>",
 *     panel: <the .viz-panel element>,
 *     data:  <compute() response; carries .steps>,
 *     drawFrame(ctx, t, data) { ... }   // OPTIONAL. Omit -> no Animation button.
 *   });
 *
 * Behaviour:
 *   - drawFrame omitted  -> only the Steps button shows. Existing non-trig calcs
 *     never call mount(), so they are completely unaffected.
 *   - Colours come ONLY from window.NCSkin tokens. On "nc-theme-change" the
 *     controls restyle and the current animation frame is redrawn.
 *   - prefers-reduced-motion: starts paused, never auto-loops.
 *   - Default state is PAUSED with an obvious "▶ Play" affordance, so pages are
 *     calm on load even when motion is allowed.
 *   - Re-calling mount() for the same slug re-uses the existing controls and just
 *     refreshes data (so live-updating inputs don't stack canvases or listeners).
 *
 * No external libraries. No edits to core files. Loaded per trig viz alongside
 * nclearn.css.
 */
(function () {
  "use strict";

  var REDUCED = false;
  try {
    REDUCED = window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  } catch (e) { REDUCED = false; }

  // Registry of mounted instances, keyed by slug, so repeated compute() calls
  // refresh rather than duplicate.
  var INSTANCES = {};

  function skin() { return window.NCSkin || {}; }

  function el(tag, cls) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    return n;
  }

  function styleToggle(inst) {
    var s = skin();
    var ink = s.ink || "#222";
    var accent = s.accent || "#b5651d";
    var rule = s.rule || "#ccc";
    var paper2 = s.paper2 || "transparent";
    inst.seg.style.display = "inline-flex";
    inst.seg.style.border = "1px solid " + rule;
    inst.seg.style.borderRadius = "8px";
    inst.seg.style.overflow = "hidden";
    inst.seg.style.margin = "4px 0 12px";
    [inst.btnSteps, inst.btnAnim].forEach(function (b) {
      if (!b) return;
      b.style.cursor = "pointer";
      b.style.border = "none";
      b.style.padding = "6px 14px";
      b.style.font = "13px " + (s.sans || "sans-serif");
      b.style.background = b.classList.contains("active") ? accent : paper2;
      b.style.color = b.classList.contains("active")
        ? (s.paper || "#fff") : ink;
    });
    if (inst.playBtn) {
      inst.playBtn.style.cursor = "pointer";
      inst.playBtn.style.border = "1px solid " + rule;
      inst.playBtn.style.borderRadius = "6px";
      inst.playBtn.style.padding = "4px 12px";
      inst.playBtn.style.font = "13px " + (s.sans || "sans-serif");
      inst.playBtn.style.background = paper2;
      inst.playBtn.style.color = ink;
      inst.playBtn.style.marginBottom = "8px";
    }
  }

  function setActive(inst, mode) {
    inst.mode = mode;
    var stepsOn = mode === "steps";
    inst.btnSteps.classList.toggle("active", stepsOn);
    inst.btnSteps.setAttribute("aria-pressed", String(stepsOn));
    if (inst.btnAnim) {
      inst.btnAnim.classList.toggle("active", !stepsOn);
      inst.btnAnim.setAttribute("aria-pressed", String(!stepsOn));
    }
    // The shared steps panel lives outside the viz (from _steps.html).
    var stepsPanel = document.getElementById("nc-steps");
    if (stepsOn) {
      if (stepsPanel) stepsPanel.style.display = "";
      inst.animWrap.style.display = "none";
      stopLoop(inst);
    } else {
      if (stepsPanel) stepsPanel.style.display = "none";
      inst.animWrap.style.display = "";
      // Animation revealed: draw a static first frame; respect reduced-motion.
      drawOnce(inst, inst.t || 0);
      if (!REDUCED && inst.playing) startLoop(inst);
    }
    styleToggle(inst);
  }

  function drawOnce(inst, t) {
    if (!inst.drawFrame || !inst.ctx) return;
    var cv = inst.canvas, ctx = inst.ctx;
    ctx.clearRect(0, 0, cv.width, cv.height);
    try { inst.drawFrame(ctx, t, inst.data); } catch (e) { /* never throw */ }
  }

  function startLoop(inst, explicit) {
    // Reduced-motion suppresses AUTOMATIC looping only. An explicit user click
    // on Play is always honoured (accessibility intent is "don't auto-play",
    // not "forbid motion the user asked for").
    if (inst.raf) return;
    if (REDUCED && !explicit) return;
    inst.playing = true;
    if (inst.playBtn) inst.playBtn.textContent = "⏸ Pause";
    inst.start = null;
    var DURATION = 4200; // ms per loop
    function step(ts) {
      if (inst.start === null) inst.start = ts;
      var elapsed = (ts - inst.start) % DURATION;
      inst.t = elapsed / DURATION; // 0..1
      drawOnce(inst, inst.t);
      inst.raf = window.requestAnimationFrame(step);
    }
    inst.raf = window.requestAnimationFrame(step);
  }

  function stopLoop(inst) {
    if (inst.raf) {
      window.cancelAnimationFrame(inst.raf);
      inst.raf = null;
    }
    inst.playing = false;
    if (inst.playBtn) inst.playBtn.textContent = "▶ Play";
  }

  function togglePlay(inst) {
    if (inst.playing) stopLoop(inst);
    else startLoop(inst, true);   // explicit user request
  }

  function build(inst) {
    // Toggle group (.nc-seg look reused via inline styling + class hook).
    inst.seg = el("div", "nc-seg nclearn-seg");
    inst.seg.setAttribute("role", "group");
    inst.seg.setAttribute("aria-label", "Learning view");

    inst.btnSteps = el("button", "active");
    inst.btnSteps.type = "button";
    inst.btnSteps.textContent = "Steps";
    inst.btnSteps.setAttribute("aria-pressed", "true");
    inst.seg.appendChild(inst.btnSteps);

    if (inst.drawFrame) {
      inst.btnAnim = el("button");
      inst.btnAnim.type = "button";
      inst.btnAnim.textContent = "Animation";
      inst.btnAnim.setAttribute("aria-pressed", "false");
      inst.seg.appendChild(inst.btnAnim);
    }

    // Animation container (canvas + play/pause), hidden until Animation chosen.
    inst.animWrap = el("div", "nclearn-anim");
    inst.animWrap.style.display = "none";
    if (inst.drawFrame) {
      inst.playBtn = el("button", "nclearn-play");
      inst.playBtn.type = "button";
      inst.playBtn.textContent = "▶ Play";
      inst.animWrap.appendChild(inst.playBtn);

      inst.canvas = el("canvas", "nclearn-canvas");
      inst.canvas.width = 640;
      inst.canvas.height = 320;
      inst.canvas.style.cssText =
        "display:block;width:100%;height:auto;max-width:640px;margin-top:6px";
      inst.animWrap.appendChild(inst.canvas);
      inst.ctx = inst.canvas.getContext("2d");
    }

    // Insert the toggle just before the shared steps panel if present, else at
    // the end of the viz panel; the anim container goes right after the toggle.
    var anchor = document.getElementById("nc-steps");
    if (anchor && anchor.parentNode) {
      anchor.parentNode.insertBefore(inst.seg, anchor);
      anchor.parentNode.insertBefore(inst.animWrap, anchor);
    } else {
      inst.panel.appendChild(inst.seg);
      inst.panel.appendChild(inst.animWrap);
    }

    // Wire events.
    inst.btnSteps.addEventListener("click", function () { setActive(inst, "steps"); });
    if (inst.btnAnim) {
      inst.btnAnim.addEventListener("click", function () { setActive(inst, "anim"); });
    }
    if (inst.playBtn) {
      inst.playBtn.addEventListener("click", function () { togglePlay(inst); });
    }

    // Theme: restyle controls and redraw the current frame.
    window.addEventListener("nc-theme-change", function () {
      styleToggle(inst);
      if (inst.mode === "anim") drawOnce(inst, inst.t || 0);
    });
  }

  var NCLearn = {
    mount: function (opts) {
      if (!opts || !opts.panel || !opts.slug) return;
      var inst = INSTANCES[opts.slug];
      if (inst) {
        // Refresh data only; keep DOM, listeners, and current mode.
        inst.data = opts.data;
        inst.drawFrame = opts.drawFrame || inst.drawFrame;
        if (inst.mode === "anim") drawOnce(inst, inst.t || 0);
        return inst;
      }
      inst = {
        slug: opts.slug,
        panel: opts.panel,
        data: opts.data,
        drawFrame: opts.drawFrame || null,
        mode: "steps",
        t: 0,
        raf: null,
        playing: false
      };
      INSTANCES[opts.slug] = inst;
      build(inst);
      setActive(inst, "steps");   // Steps default; calm on load.
      styleToggle(inst);
      return inst;
    },
    // exposed for testing / introspection
    _instances: INSTANCES,
    _reducedMotion: function () { return REDUCED; }
  };

  window.NCLearn = NCLearn;
})();
