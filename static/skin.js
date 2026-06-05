// skin.js — single source of truth for any JS/canvas graph.
// Reads the CSS custom properties defined in app.css so a plugged-in
// calculator NEVER hardcodes a colour and always matches the active theme.
// Call NCSkin.refresh() (the theme switcher does) to re-read after a theme change.
window.NCSkin = (function () {
  const read = () => {
    const css = getComputedStyle(document.documentElement);
    const v = name => css.getPropertyValue(name).trim();
    return {
      paper:   v("--paper"),
      paper2:  v("--paper-2"),
      paper3:  v("--paper-3"),
      ink:     v("--ink"),
      inkSoft: v("--ink-soft"),
      accent:  v("--accent"),
      yes:     v("--yes"),
      rule:    v("--rule"),
      mono:    v("--mono"),
      serif:   v("--serif"),
      sans:    v("--sans"),
    };
  };
  const skin = read();
  skin.refresh = function () { Object.assign(skin, read()); };
  return skin;
})();
