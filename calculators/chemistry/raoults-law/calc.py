"""Raoult's Law — chemistry > Colligative Properties > Vapour Pressure. Calculate solvent vapour pressure P_A = x_A × P_A° by Raoult's law, with full symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='raoults-law', name="Raoult's Law", section="chemistry", topic='Colligative Properties', sub='Vapour Pressure',
    order=1,
    tags=['raoult', 'vapour pressure', 'evaporation', 'distillation', 'chemistry'],
    formula='PA = xA × PA\\circ',
    summary="Calculate solvent vapour pressure P_A = x_A × P_A° by Raoult's law, with full symbol legend and real-world examples.",
    viz_template="viz/raoults-law.html",
    scholar='raoult',
)
def compute(xA=0.8, P0=100):
    try:
        xA = float(xA); P0 = float(P0)
    except (TypeError, ValueError):
        return {"error": "Enter the solvent mole fraction and pure vapour pressure.", "steps": []}
    if xA < 0 or xA > 1:
        return {"error": "Mole fraction must be between 0 and 1.", "steps": []}
    if P0 < 0:
        return {"error": "Pure vapour pressure cannot be negative.", "steps": []}
    PA = xA * P0
    drop = P0 - PA
    def fmt(v): return ("%g" % round(v, 6))
    steps = [
        {"label": "Step 1 - Write the law", "math": r"\( P_A = x_A \times P_A^{\circ} \)",
         "note": "The vapour pressure of the solvent in the solution equals its pure vapour pressure scaled down by its mole fraction."},
        {"label": "Step 2 - Put in your numbers",
         "math": r"\( P_A = %s \times %s \)" % (fmt(xA), fmt(P0)),
         "note": "x_A = %s (the solvent is this fraction of all particles), P_A\u00b0 = %s (vapour pressure of the pure solvent)." % (fmt(xA), fmt(P0))},
        {"label": "Step 3 - Multiply", "math": r"\( P_A = %s \)" % fmt(PA),
         "note": "Because some particles are now solute, the solvent evaporates less, so the vapour pressure dropped by %s." % fmt(drop)},
    ]
    explanation = [
        {"heading": "The formula in plain words",
         "body": "Vapour pressure of the solvent in a solution = (fraction that is solvent) \u00d7 (vapour pressure when it was pure).  In symbols: P<sub>A</sub> = x<sub>A</sub> \u00d7 P<sub>A</sub>\u00b0.  Dissolving something in a liquid makes it evaporate less, so its vapour pressure goes down."},
        {"heading": "What each letter means", "legend": [
            ["P<sub>A</sub>", "Vapour pressure of the solvent above the solution - how strongly it evaporates now (e.g. mm Hg)."],
            ["x<sub>A</sub>", "Mole fraction of the solvent - what share of all the particles in the liquid are solvent (0 to 1)."],
            ["P<sub>A</sub>\u00b0", "Vapour pressure of the pure solvent, before anything was dissolved in it (the little circle means 'pure')."],
        ]},
        {"heading": "Real life: salt water evaporates slower \U0001F30A",
         "body": "Pure water evaporates faster than salty water. When you dissolve salt, the salt particles take up space at the surface and get in the way of water molecules escaping, so fewer escape and the vapour pressure drops. This is why a glass of salty water left out lasts a little longer than plain water, and it is the first domino behind why sea water boils a touch higher and freezes a touch lower."},
        {"heading": "Real life: why it helps make spirits and perfume \U0001F377",
         "body": "When two liquids mix, each one's vapour pressure follows this law, so the more volatile one dominates the vapour. Distillers and perfume makers use exactly this to separate liquids by boiling: the component with the higher vapour pressure leaves first and is collected. Raoult's law is the rule that predicts what comes off as vapour and in what proportion."},
    ]
    return {"result": "Solvent vapour pressure P_A = %s mm Hg" % fmt(PA),
            "formula_plain": "P_A = x_A \u00d7 P_A\u00b0  \u2192  vapour pressure = solvent fraction \u00d7 pure vapour pressure",
            "law": "P_A = x_A \u00d7 P_A\u00b0", "law_label": "Raoult's Law",
            "verified": True, "steps": steps, "explanation": explanation,
            "xA": xA, "P0": P0, "PA": PA, "drop": drop}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
