"""Henry's Law — chemistry > Colligative Properties > Gas Solubility. Calculate gas pressure P = k_H × x by Henry's law, with full symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='henrys-law', name="Henry's Law", section="chemistry", topic='Colligative Properties', sub='Gas Solubility',
    order=6,
    tags=['henry', 'gas solubility', 'fizzy drink', 'pressure', 'chemistry'],
    formula='P = kH × x',
    summary="Calculate gas pressure P = k_H × x by Henry's law, with full symbol legend and real-world examples.",
    viz_template="viz/henrys-law.html",
    scholar='henry',
)
def compute(kH=1000, x=0.002):
    try:
        kH = float(kH); x = float(x)
    except (TypeError, ValueError):
        return {"error": "Enter Henry's constant and the gas mole fraction.", "steps": []}
    if kH < 0 or x < 0:
        return {"error": "Values cannot be negative.", "steps": []}
    P = kH * x
    def fmt(v): return ("%g" % round(v, 6))
    steps = [
        {"label": "Step 1 - Write the law", "math": r"\( P = k_H \times x \)",
         "note": "The pressure of the gas above the liquid equals Henry's constant times how much gas is dissolved."},
        {"label": "Step 2 - Put in your numbers",
         "math": r"\( P = %s \times %s \)" % (fmt(kH), fmt(x)),
         "note": "k_H = %s (how hard this gas resists dissolving), x = %s (fraction of the liquid that is dissolved gas)." % (fmt(kH), fmt(x))},
        {"label": "Step 3 - Multiply", "math": r"\( P = %s \)" % fmt(P),
         "note": "This is the gas pressure that keeps that much gas dissolved. More pressure forces in more gas."},
    ]
    explanation = [
        {"heading": "The formula in plain words",
         "body": "Pressure of the gas = Henry's constant \u00d7 amount of gas dissolved.  In symbols: P = k<sub>H</sub> \u00d7 x.  The more you squeeze gas above a liquid (higher P), the more gas dissolves into it (higher x).  Let the pressure go, and the gas escapes."},
        {"heading": "What each letter means", "legend": [
            ["P", "Pressure of the gas sitting above the liquid (e.g. atm). Higher pressure pushes more gas in."],
            ["k<sub>H</sub>", "Henry's constant - a fixed number for each gas + liquid + temperature. A big k<sub>H</sub> means the gas does not dissolve easily."],
            ["x", "Mole fraction of the gas dissolved in the liquid - what share of the liquid's particles are the dissolved gas (a number between 0 and 1)."],
        ]},
        {"heading": "Real life: opening a fizzy drink \U0001F964",
         "body": "A cola bottle is sealed under high CO\u2082 pressure, so lots of gas stays dissolved (the drink looks still). The moment you twist the cap, the pressure above the liquid drops to normal air pressure - so the liquid can no longer hold all that gas, and it rushes out as the fizz and 'pssst' you hear. Leave it open and it slowly goes flat. That is Henry's law: less pressure = less dissolved gas."},
        {"heading": "Real life: divers and 'the bends' \U0001F93F",
         "body": "Deep underwater the high pressure forces extra nitrogen from a diver's air to dissolve in their blood. If they shoot up to the surface too fast, the pressure drops suddenly and that nitrogen fizzes out as bubbles in the body - exactly like opening a soda - which is dangerous. Divers rise slowly so the gas leaves gently through the lungs."},
    ]
    return {"result": "Gas pressure P = %s" % fmt(P),
            "formula_plain": "P = k_H \u00d7 x  \u2192  pressure = Henry's constant \u00d7 dissolved-gas fraction",
            "law": "P = k_H \u00d7 x", "law_label": "Henry's Law",
            "verified": True, "steps": steps, "explanation": explanation,
            "kH": kH, "x": x, "P": P}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
