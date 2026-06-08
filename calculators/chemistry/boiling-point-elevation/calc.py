"""Elevation in Boiling Point (ΔT_b) — chemistry > Colligative Properties > Freezing & Boiling Points."""
from core.registry import register


@register(
    slug="boiling-point-elevation", name="Elevation in Boiling Point (\u0394T_b)", section="chemistry",
    topic="Colligative Properties", sub="Freezing & Boiling Points", order=4,
    tags=["boiling point", "elevation", "colligative", "cooking", "chemistry"],
    formula="\u0394T_b = K_b \u00d7 m",
    summary="Calculate boiling-point elevation \u0394T_b = K_b\u00d7m, with symbol legend and real-world examples.",
    viz_template="viz/boiling-point-elevation.html",
    scholar="raoult",
)
def compute(Kb=0.52, m=1):
    try:
        Kb = float(Kb); m = float(m)
    except (TypeError, ValueError):
        return {"error": "Enter the boiling constant and molality.", "steps": []}
    dT = Kb * m
    def fmt(x): return ("%g" % round(x, 6))
    steps = [
        {"label": "Step 1 - Write the formula", "math": r"\( \Delta T_b = K_b \times m \)",
         "note": "How far the boiling point rises = the solvent's boiling constant times the molality."},
        {"label": "Step 2 - Put in your numbers", "math": r"\( \Delta T_b = %s \times %s \)" % (fmt(Kb), fmt(m)),
         "note": "K_b = %s (a property of the solvent), molality m = %s mol/kg." % (fmt(Kb), fmt(m))},
        {"label": "Step 3 - Multiply", "math": r"\( \Delta T_b = %s\,^{\circ}C \)" % fmt(dT),
         "note": "The boiling point is pushed UP by this many degrees."},
    ]
    explanation = [
        {"heading": "The formula in plain words",
         "body": "Rise in boiling point = boiling constant of the solvent \u00d7 how concentrated the solution is (molality).  Dissolving something makes a liquid boil at a HIGHER temperature than when it was pure."},
        {"heading": "What each letter means", "legend": [
            ["\u0394T<sub>b</sub>", "How many degrees the boiling point rises (\u00b0C). (\u0394 means 'change in'.)"],
            ["K<sub>b</sub>", "Boiling-point constant of the solvent - degrees of rise per unit molality. For water it is 0.52."],
            ["m", "Molality - moles of solute per kilogram of solvent."],
        ]},
        {"heading": "Real life: salted pasta water \U0001F35D",
         "body": "Adding salt to cooking water raises its boiling point a little, so the water gets slightly hotter than 100\u00b0C before boiling. The everyday effect is tiny (about half a degree), so salt is really added for flavour - but the principle is real and is the same one used in industry."},
        {"heading": "Real life: engine coolant and boiling sugar \U0001F699",
         "body": "Car coolant contains additives that RAISE its boiling point so it does not boil away on a hot motorway climb. Sweet-makers boiling sugar syrup also watch the boiling point climb as the syrup concentrates - candy thermometers depend on it."},
    ]
    return {"result": "Boiling point raised by \u0394T_b = %s \u00b0C" % fmt(dT),
            "formula_plain": "\u0394T_b = K_b \u00d7 m  \u2192  how far the boiling point rises",
            "law": "\u0394T_b = K_b \u00d7 m", "law_label": "Boiling Point Elevation",
            "verified": True, "steps": steps, "explanation": explanation, "dT": dT}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
