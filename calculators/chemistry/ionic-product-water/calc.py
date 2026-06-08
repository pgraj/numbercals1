"""Ionic Product of Water (K_w) — chemistry > Equilibrium & Acids/Bases > Acids & Bases. Calculate K_w = [H⁺][OH⁻] (=10⁻¹⁴ at 25°C), with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='ionic-product-water', name='Ionic Product of Water (K_w)', section="chemistry", topic='Equilibrium & Acids/Bases', sub='Acids & Bases',
    order=3,
    tags=['ionic product', 'water', 'kw', 'chemistry'],
    formula='Kw = [H^+][OH^-] = 10⁻¹⁴',
    summary='Calculate K_w = [H⁺][OH⁻] (=10⁻¹⁴ at 25°C), with symbol legend and real-world examples.',
    viz_template="viz/ionic-product-water.html",
)
def compute(H=1e-7, OH=1e-7):
    try:
        H = float(H); OH = float(OH)
    except (TypeError, ValueError):
        return {"error": "Enter [H\u207a] and [OH\u207b].", "steps": []}
    if H < 0 or OH < 0:
        return {"error": "Concentrations cannot be negative.", "steps": []}
    Kw = H * OH
    def fmt(x): return ("%.3g" % x)
    steps=[
        {"label":"Step 1 - Write the formula","math":r"\( K_w = [H^+]\times[OH^-] \)","note":"Multiply the hydrogen-ion and hydroxide-ion concentrations together."},
        {"label":"Step 2 - Put in your numbers","math":r"\( K_w = (%s)\times(%s) \)" % (fmt(H), fmt(OH)),"note":"[H\u207a] = %s, [OH\u207b] = %s mol/L." % (fmt(H), fmt(OH))},
        {"label":"Step 3 - Multiply","math":r"\( K_w = %s \)" % fmt(Kw),"note":"For water at 25\u00b0C this is always about 1\u00d710\u207b\u00b9\u2074."},
    ]
    explanation=[
        {"heading":"The formula in plain words","body":"Ionic product of water = [H\u207a] \u00d7 [OH\u207b], and in water it is always about 10\u207b\u00b9\u2074.  Because the product is fixed, if one ion goes up the other must come down."},
        {"heading":"What each letter means","legend":[
            ["K<sub>w</sub>","Ionic product of water - the fixed value of [H\u207a]\u00d7[OH\u207b] (about 10\u207b\u00b9\u2074 at 25\u00b0C)."],
            ["[H<sup>+</sup>]","Concentration of hydrogen ions (acidic ions), mol/L."],
            ["[OH<sup>-</sup>]","Concentration of hydroxide ions (basic ions), mol/L."],
        ]},
        {"heading":"Real life: why pH 7 is 'neutral' \U0001F4A7","body":"In pure water the tiny amounts of H\u207a and OH\u207b are equal, and since their product is 10\u207b\u00b9\u2074 each must be 10\u207b\u2077 - giving pH 7. So the familiar 'neutral = 7' comes straight out of this constant; it is not an arbitrary choice."},
        {"heading":"Real life: balancing acids and bases \u2697\ufe0f","body":"Because the product is fixed, adding acid (more H\u207a) automatically forces OH\u207b down, and vice versa. This is the hidden rule behind every acid-base adjustment - in your blood, in a swimming pool, in a chemistry lab - that lets you predict one ion from the other."},
    ]
    return {"result":"Ionic product K_w = %s" % fmt(Kw),
            "formula_plain":"K_w = [H\u207a] \u00d7 [OH\u207b] = 10\u207b\u00b9\u2074 (at 25\u00b0C)  \u2192  the two ions always balance",
            "law":"K_w = [H\u207a][OH\u207b] = 10\u207b\u00b9\u2074","law_label":"Ionic Product of Water",
            "verified":True,"steps":steps,"explanation":explanation,"Kw":Kw,"H":H,"OH":OH}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
