"""Mole Fraction (x) — chemistry > Solutions & Concentration > Concentration Units. Calculate mole fraction x_A = n_A/(n_A+n_B): a component's share of the total moles, with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='mole-fraction', name='Mole Fraction (x)', section="chemistry", topic='Solutions & Concentration', sub='Concentration Units',
    order=4,
    tags=['mole fraction', 'concentration', 'composition', 'chemistry'],
    formula='xA = \\frac{nA}{nA + nB}',
    summary="Calculate mole fraction x_A = n_A/(n_A+n_B): a component's share of the total moles, with symbol legend and real-world examples.",
    viz_template="viz/mole-fraction.html",
)
def compute(nA=1, nB=2):
    try:
        nA = float(nA); nB = float(nB)
    except (TypeError, ValueError):
        return {"error": "Enter moles for both components.", "steps": []}
    tot = nA + nB
    if tot <= 0:
        return {"error": "Total moles must be greater than zero.", "steps": []}
    xA = nA / tot; xB = nB / tot
    def fmt(x): return ("%g" % round(x, 6))
    steps = [
        {"label": "Step 1 - Write the formula", "math": r"\( x_A = \dfrac{n_A}{n_A + n_B} \)",
         "note": "Mole fraction of A is its share of all the particles present."},
        {"label": "Step 2 - Add up all the moles", "math": r"\( n_A + n_B = %s + %s = %s \)" % (fmt(nA), fmt(nB), fmt(tot)),
         "note": "Find the total number of moles in the mixture."},
        {"label": "Step 3 - Divide A by the total", "math": r"\( x_A = \dfrac{%s}{%s} = %s \)" % (fmt(nA), fmt(tot), fmt(xA)),
         "note": "And x_B = %s; the two add up to 1, a handy check." % fmt(xB)},
    ]
    explanation = [
        {"heading": "The formula in plain words",
         "body": "Mole fraction of A = moles of A \u00f7 total moles of everything.  It is simply A's share of all the particles, written as a number between 0 and 1. All the fractions in a mixture add up to exactly 1."},
        {"heading": "What each letter means", "legend": [
            ["x<sub>A</sub>", "Mole fraction of component A - its share of all particles (0 to 1)."],
            ["n<sub>A</sub>", "Number of moles of component A."],
            ["n<sub>B</sub>", "Number of moles of component B (the other component)."],
            ["n<sub>A</sub>+n<sub>B</sub>", "Total moles of all particles in the mixture."],
        ]},
        {"heading": "Real life: the air you breathe \U0001F32C\ufe0f",
         "body": "Air is about 0.78 nitrogen and 0.21 oxygen by mole fraction - meaning roughly 78 of every 100 air particles are nitrogen. Each gas's mole fraction also equals its share of the total air pressure, which is how we describe what is in the atmosphere."},
        {"heading": "Real life: mixing drinks or fuel blends \u26FD",
         "body": "When fuels are blended (like ethanol into petrol) or drinks are mixed, the proportions that control how the mixture behaves are mole fractions - the share of particles of each kind, not just the volumes poured. It is the honest way to describe 'how much of each is really in here'."},
    ]
    return {"result": "Mole fraction x_A = %s (and x_B = %s)" % (fmt(xA), fmt(xB)),
            "formula_plain": "x_A = n_A \u00f7 (n_A + n_B)  \u2192  A's share of all the particles",
            "law": "x\u2090 = n\u2090 / (n\u2090 + n\u2087)", "law_label": "Mole Fraction",
            "verified": abs((xA+xB)-1.0) < 1e-9, "steps": steps, "explanation": explanation,
            "xA": xA, "xB": xB}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
