// Generic viz: builds inputs from the calc's parameter list and renders results.
(function () {
  const panel = document.querySelector(".viz-panel");
  if (!panel) return;
  const slug = panel.dataset.slug;
  const inputsEl = document.getElementById("viz-inputs");
  const outEl = document.getElementById("viz-out");

  // Parameter specs per slug. (Kept declarative so a calc can add inputs
  // without touching JS; future: fetch from /api/params/<slug>.)
  const PARAMS = {
    "quadratic": [["a", 1], ["b", -3], ["c", 2]],
    "compound-interest": [["principal", 1000], ["rate_pct", 5], ["years", 10], ["n", 12]],
  };
  const spec = PARAMS[slug] || [];

  spec.forEach(([name, def]) => {
    const label = document.createElement("label");
    label.textContent = name.replace(/_/g, " ");
    const input = document.createElement("input");
    input.type = "number"; input.id = "in-" + name; input.value = def;
    label.appendChild(input);
    inputsEl.appendChild(label);
  });

  async function run() {
    const body = {};
    spec.forEach(([name]) => body[name] = +document.getElementById("in-" + name).value);
    try {
      const r = await fetch("/api/compute/" + slug, {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
      const data = await r.json();
      outEl.innerHTML = Object.entries(data)
        .map(([k, v]) => `${k.replace(/_/g, " ")}: <b>${v}</b>`).join(" · ");
    } catch (e) { outEl.textContent = "compute error"; }
  }
  document.getElementById("viz-run").onclick = run;
  run();
})();
