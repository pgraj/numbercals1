// Home scientific calculator: standard/scientific toggle + DEG/RAD toggle.
// Two parallel strings: `shown` (display text) and `expr` (evaluated JS).
(function () {
  const display = document.getElementById("calc-display");
  const keysWrap = document.getElementById("calc-keys");

  let shown = "";
  let expr  = "";
  let justEvaluated = false;
  let angleMode = "DEG";

  const SCI = ["sin","cos","tan","π","(",")",
               "asin","acos","atan","e","^","√",
               "log","ln","%","7","8","9",
               "!","C","⌫","4","5","6",
               "/","*","-","1","2","3",
               "+","±",".","0","00","="];
  const STD = ["C","⌫","%","/","7","8","9","*",
               "4","5","6","-","1","2","3","+",
               "±","0",".","="];

  const OPS = "+-*/^";
  const FUNCS = ["sin","cos","tan","asin","acos","atan","log","ln"];
  const TRIG  = ["sin","cos","tan"];
  const INVTRIG = ["asin","acos","atan"];

  function render(keys, mode) {
    keysWrap.className = "keys " + mode;
    keysWrap.innerHTML = "";
    keys.forEach(k => {
      const b = document.createElement("button");
      b.textContent = k;
      if (OPS.includes(k) || k === "√" || k === "%" ||
          FUNCS.includes(k) || k === "π" || k === "e" || k === "!") b.className = "op";
      if (k === "=") b.className = "eq";
      b.onclick = () => press(k);
      keysWrap.appendChild(b);
    });
  }

  function append(showText, exprText) {
    if (justEvaluated) {
      if (OPS.includes(showText)) { /* continue from result */ }
      else { shown = ""; expr = ""; }
      justEvaluated = false;
    }
    shown += showText;
    expr  += exprText;
  }

  function press(k) {
    if (k === "C") { shown = ""; expr = ""; justEvaluated = false; }
    else if (k === "⌫") {
      if (justEvaluated) { shown = ""; expr = ""; justEvaluated = false; }
      else { shown = shown.slice(0, -1); expr = expr.slice(0, -1); }
    }
    else if (k === "=") {
      const v = evaluate(expr);
      shown = String(v);
      expr  = (v === "Error") ? "" : String(v);
      justEvaluated = true;
    }
    else if (k === "±") {
      if (shown.startsWith("-")) { shown = shown.slice(1); expr = expr.slice(1); }
      else { shown = "-" + shown; expr = "-" + expr; }
    }
    else if (k === "π") { append("π", "Math.PI"); }
    else if (k === "e") { append("e", "Math.E"); }
    else if (k === "√") { append("√(", "Math.sqrt("); }
    else if (k === "^") { append("^", "**"); }
    else if (k === "%") { append("%", "/100"); }
    else if (TRIG.includes(k)) {
      const fn = {sin:"Math.sin", cos:"Math.cos", tan:"Math.tan"}[k];
      if (angleMode === "DEG") append(k + "(", fn + "((Math.PI/180)*(");
      else                     append(k + "(", fn + "(");
    }
    else if (INVTRIG.includes(k)) {
      const fn = {asin:"Math.asin", acos:"Math.acos", atan:"Math.atan"}[k];
      if (angleMode === "DEG") append(k + "(", "(180/Math.PI)*" + fn + "(");
      else                     append(k + "(", fn + "(");
    }
    else if (k === "log") { append("log(", "Math.log10("); }
    else if (k === "ln")  { append("ln(",  "Math.log("); }
    else if (k === "!")   { append("!", "!"); }
    else { append(k, k); }

    display.textContent = shown || "0";
  }

  function evaluate(raw) {
    try {
      if (!raw.trim()) return 0;
      const opens = (raw.match(/\(/g) || []).length;
      const closes = (raw.match(/\)/g) || []).length;
      let safe = raw + ")".repeat(Math.max(0, opens - closes));
      safe = safe.replace(/(\d+(?:\.\d+)?)!/g, (_, n) => factorial(+n));
      const v = Function('"use strict";return (' + safe + ")")();
      return Number.isFinite(v) ? +v.toPrecision(12) : "Error";
    } catch { return "Error"; }
  }
  function factorial(n){ if(n<0||!Number.isInteger(n))return NaN; let r=1; for(let i=2;i<=n;i++)r*=i; return r; }

  // ---- standard / scientific toggle ----
  const bStd = document.getElementById("mode-standard");
  const bSci = document.getElementById("mode-scientific");
  // Give the mode buttons the shared segmented-toggle look (replaces the old .op).
  bStd.classList.add("nc-seg"); bSci.classList.add("nc-seg");
  function setMode(keys, mode){
    render(keys, mode);
    bSci.classList.toggle("active", mode === "scientific");
    bStd.classList.toggle("active", mode === "standard");
    // DEG/RAD only affects trig, which standard mode doesn't have — hide it there.
    if (typeof angleWrap !== "undefined") {
      angleWrap.style.display = (mode === "scientific") ? "inline-flex" : "none";
    }
    updateStatus();
  }
  bStd.onclick = () => setMode(STD, "standard");
  bSci.onclick = () => setMode(SCI, "scientific");

  // ---- DEG / RAD toggle (injected, with clear active state) ----
  const modeRow = bStd.parentElement;
  const angleWrap = document.createElement("span");
  angleWrap.style.marginLeft = "auto";
  angleWrap.style.display = "inline-flex";
  angleWrap.style.gap = "6px";
  const bDeg = document.createElement("button");
  const bRad = document.createElement("button");
  bDeg.textContent = "DEG"; bRad.textContent = "RAD";
  bDeg.classList.add("nc-seg"); bRad.classList.add("nc-seg");
  function setAngle(m){
    angleMode = m;
    bDeg.classList.toggle("active", m === "DEG");
    bRad.classList.toggle("active", m === "RAD");
    updateStatus();
  }
  bDeg.onclick = () => setAngle("DEG");
  bRad.onclick = () => setAngle("RAD");
  angleWrap.appendChild(bDeg); angleWrap.appendChild(bRad);
  modeRow.appendChild(angleWrap);

  // ---- small status line: spells out the current modes in words ----
  const status = document.createElement("div");
  status.id = "calc-status";
  status.className = "calc-status";
  // place it just under the mode row
  modeRow.insertAdjacentElement("afterend", status);
  function updateStatus(){
    const isSci = bSci.classList.contains("active");
    status.textContent = isSci
      ? `Scientific · angles in ${angleMode === "DEG" ? "degrees (DEG)" : "radians (RAD)"}`
      : `Standard`;
  }

  // ---- initial state ----
  setMode(SCI, "scientific");
  setAngle("DEG");
})();
