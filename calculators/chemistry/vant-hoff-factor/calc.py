"""van 't Hoff Factor (i) — chemistry > Colligative Properties > Dissociation. Calculate the van 't Hoff factor i = observed/calculated: particles per dissolved unit, with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='vant-hoff-factor', name="van 't Hoff Factor (i)", section="chemistry", topic='Colligative Properties', sub='Dissociation',
    order=5,
    tags=["van't hoff", 'dissociation', 'ions', 'colligative', 'chemistry'],
    formula='i = \\frac{\\text{observed effect}}{\\text{calculated effect}}',
    summary="Calculate the van 't Hoff factor i = observed/calculated: particles per dissolved unit, with symbol legend and real-world examples.",
    viz_template="viz/vant-hoff-factor.html",
    scholar='vant-hoff',
)
def compute(observed=2, calculated=1):
    try:
        observed = float(observed); calculated = float(calculated)
    except (TypeError, ValueError):
        return {"error": "Enter the observed and calculated values.", "steps": []}
    if calculated == 0:
        return {"error": "The calculated value cannot be zero.", "steps": []}
    i = observed / calculated
    def fmt(x): return ("%g" % round(x, 6))
    steps=[
        {"label":"Step 1 - Write the formula","math":r"\( i = \dfrac{\text{observed effect}}{\text{calculated effect}} \)","note":"Compare the effect you actually measure with the effect expected if the solute did not split."},
        {"label":"Step 2 - Put in your numbers","math":r"\( i = \dfrac{%s}{%s} \)" % (fmt(observed), fmt(calculated)),"note":"observed = %s (what you measured), calculated = %s (no-splitting prediction)." % (fmt(observed), fmt(calculated))},
        {"label":"Step 3 - Divide","math":r"\( i = %s \)" % fmt(i),"note":"This is how many particles each dissolved unit actually makes."},
    ]
    explanation=[
        {"heading":"The formula in plain words","body":"van 't Hoff factor = the effect you actually see \u00f7 the effect you'd expect if the solute stayed in one piece.  It counts how many particles each dissolved unit really breaks into."},
        {"heading":"What each letter means","legend":[
            ["i","van 't Hoff factor - the real number of particles per dissolved unit (no units)."],
            ["observed","The colligative effect you actually measure (e.g. the real freezing-point drop)."],
            ["calculated","The effect predicted assuming the solute does NOT split into pieces."],
        ]},
        {"heading":"Real life: why salt melts ice better than sugar \U0001F9C2","body":"A spoon of salt (NaCl) splits into two ions, so it has about double the ice-melting punch of the same amount of sugar, which does not split (i \u2248 1). That is why roads are salted, not sugared - the van 't Hoff factor of 2 doubles the effect."},
        {"heading":"Real life: rehydration salts and IV fluids \U0001F4A7","body":"Medical fluids must match the body's particle count. Because salts split into multiple ions, doctors must count the actual particles (using i) - not just the grams - so the fluid has the right osmotic strength for your cells. Getting i wrong would make the fluid too strong or too weak."},
    ]
    return {"result":"van 't Hoff factor i = %s" % fmt(i),
            "formula_plain":"i = observed effect \u00f7 calculated effect  \u2192  particles per dissolved unit",
            "law":"i = observed / calculated","law_label":"van 't Hoff Factor",
            "verified":True,"steps":steps,"explanation":explanation,"i":i}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
