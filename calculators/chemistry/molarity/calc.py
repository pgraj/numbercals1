"""Molarity (M) — chemistry > Solutions & Concentration > Concentration Units. Calculate molarity M = (w×1000)/(M_w×V): moles of solute per litre, with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='molarity', name='Molarity (M)', section="chemistry", topic='Solutions & Concentration', sub='Concentration Units',
    order=1,
    tags=['molarity', 'concentration', 'moles per litre', 'chemistry'],
    formula='M = \\frac{w × 1000}{Mw × V}',
    summary='Calculate molarity M = (w×1000)/(M_w×V): moles of solute per litre, with symbol legend and real-world examples.',
    viz_template="viz/molarity.html",
)
def compute(w=4.9, Mw=98, V=1000):
    try:
        w = float(w); Mw = float(Mw); V = float(V)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for mass, molar mass, and volume.", "steps": []}
    if Mw <= 0 or V <= 0:
        return {"error": "Molar mass and volume must be greater than zero.", "steps": []}
    n = w / Mw
    M = (w * 1000.0) / (Mw * V)
    def fmt(x): return ("%g" % round(x, 6))
    steps = [
        {"label": "Step 1 - Write the formula", "math": r"\( M = \dfrac{w \times 1000}{M_w \times V} \)",
         "note": "Molarity is moles of solute per litre of solution."},
        {"label": "Step 2 - Turn grams into moles", "math": r"\( n = \dfrac{w}{M_w} = \dfrac{%s}{%s} = %s \text{ mol} \)" % (fmt(w), fmt(Mw), fmt(n)),
         "note": "Divide the mass by the molar mass to count how many moles you have."},
        {"label": "Step 3 - Divide by litres", "math": r"\( M = \dfrac{%s}{%s} = %s \text{ mol/L} \)" % (fmt(n), fmt(V/1000.0), fmt(M)),
         "note": "The volume %s mL is %s L; dividing moles by litres gives molarity." % (fmt(V), fmt(V/1000.0))},
    ]
    explanation = [
        {"heading": "The formula in plain words",
         "body": "Molarity = moles of solute \u00f7 litres of solution.  The formula M = (w \u00d7 1000) \u00f7 (M<sub>w</sub> \u00d7 V) just lets you put in mass (grams) and volume (millilitres) directly: it turns grams into moles and millilitres into litres for you."},
        {"heading": "What each letter means", "legend": [
            ["M", "Molarity - moles of solute per litre of solution (mol/L)."],
            ["w", "Mass of the solute you dissolved, in grams."],
            ["M<sub>w</sub>", "Molar mass of the solute (grams per mole) - how heavy one mole is."],
            ["V", "Volume of the final solution, in millilitres."],
            ["1000", "Converts millilitres to litres so the answer comes out per litre."],
        ]},
        {"heading": "Real life: mixing a sports drink or medicine \U0001F964",
         "body": "When a nurse prepares a drip or you mix a rehydration sachet into water, the strength that matters is how many particles of the active stuff are in each litre - that is molarity. Too concentrated can harm, too dilute does nothing. Getting the mol/L right is literally life-and-death in a hospital pharmacy."},
        {"heading": "Real life: pool and aquarium chemicals \U0001F3CA",
         "body": "When you dose chlorine into a pool or treat a fish tank, the instructions are really a molarity calculation in disguise - a certain amount of chemical per volume of water. Add the right moles per litre and it works; guess wrong and you get cloudy water or harm the fish."},
    ]
    return {"result": "Molarity = %s mol/L" % fmt(M),
            "formula_plain": "M = (w \u00d7 1000) \u00f7 (M_w \u00d7 V)  \u2192  moles of solute per litre of solution",
            "law": "M = (w \u00d7 1000) / (M\u1d65 \u00d7 V)", "law_label": "Molarity",
            "verified": True, "steps": steps, "explanation": explanation, "M": M, "n": n}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
