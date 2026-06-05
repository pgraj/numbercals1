// Theme switcher: light / sepia / dark.
// Sets data-theme on <html>, persists to localStorage, marks the active
// button, and refreshes NCSkin so any open canvas graph recolours live.
(function () {
  const root = document.documentElement;
  const buttons = document.querySelectorAll("[data-theme-set]");

  function apply(theme) {
    root.setAttribute("data-theme", theme);
    try { localStorage.setItem("nc-theme", theme); } catch (e) {}
    buttons.forEach(b =>
      b.classList.toggle("active", b.dataset.themeSet === theme));
    // Refresh the shared palette so canvas-based graphs can repaint.
    if (window.NCSkin && window.NCSkin.refresh) window.NCSkin.refresh();
    // Let any graph listen for this to redraw itself.
    window.dispatchEvent(new CustomEvent("nc-theme-change", { detail: theme }));
  }

  buttons.forEach(b =>
    b.addEventListener("click", () => apply(b.dataset.themeSet)));

  // Mark the active button on load (theme was already applied in <head>).
  const current = root.getAttribute("data-theme") || "sepia";
  buttons.forEach(b =>
    b.classList.toggle("active", b.dataset.themeSet === current));

  // Sidebar toggle (mobile).
  const toggle = document.getElementById("nav-toggle");
  const sidebar = document.getElementById("sidebar");
  if (toggle && sidebar) {
    toggle.addEventListener("click", () => sidebar.classList.toggle("open"));
  }
})();
