"""Normality (N) — chemistry > Solutions & Concentration > Concentration Units. Calculate normality N = (w×1000)/(E×V): reactive equivalents per litre, with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='normality', name='Normality (N)', section="chemistry", topic='Solutions & Concentration', sub='Concentration Units',
    order=2,
    tags=['normality', 'concentration', 'equivalents', 'titration', 'chemistry'],
    formula='N = \\frac{w × 1000}{E × V}',
    summary='Calculate normality N = (w×1000)/(E×V): reactive equivalents per litre, with symbol legend and real-world examples.',
    viz_template="viz/normality.html",
)
def compute(w=4.9, E=49, V=1000):
    try:
        w = float(w); E = float(E); V = float(V)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for mass, equivalent weight, and volume.", "steps": []}
    if E <= 0 or V <= 0:
        return {"error": "Equivalent weight and volume must be greater than zero.", "steps": []}
    eq = w / E
    N = (w * 1000.0) / (E * V)
    def fmt(x): return ("%g" % round(x, 6))
    steps = [
        {"label": "Step 1 - Write the formula", "math": r"\( N = \dfrac{w \times 1000}{E \times V} \)",
         "note": "Normality is gram-equivalents of solute per litre of solution."},
        {"label": "Step 2 - Find gram-equivalents", "math": r"\( \text{eq} = \dfrac{w}{E} = \dfrac{%s}{%s} = %s \)" % (fmt(w), fmt(E), fmt(eq)),
         "note": "Divide mass by equivalent weight to count reactive units."},
        {"label": "Step 3 - Divide by litres", "math": r"\( N = \dfrac{%s}{%s} = %s \text{ eq/L} \)" % (fmt(eq), fmt(V/1000.0), fmt(N)),
         "note": "Dividing equivalents by the volume in litres gives normality."},
    ]
    explanation = [
        {"heading": "The formula in plain words",
         "body": "Normality = reactive equivalents of solute \u00f7 litres of solution.  It is like molarity, but instead of counting moles it counts 'reactive units' - how many protons an acid can give, or electrons a reaction can move."},
        {"heading": "What each letter means", "legend": [
            ["N", "Normality - gram-equivalents of solute per litre (eq/L)."],
            ["w", "Mass of the solute you dissolved, in grams."],
            ["E", "Equivalent weight = molar mass \u00f7 number of reactive units (e.g. protons for an acid)."],
            ["V", "Volume of the final solution, in millilitres."],
            ["1000", "Converts millilitres to litres so the answer is per litre."],
        ]},
        {"heading": "Real life: testing pool or drinking water \U0001F4A7",
         "body": "Water-testing kits measure acidity and hardness by titration, and titrations work in equivalents - the reactive capacity of what is dissolved. Normality is the natural unit there, because at the endpoint the equivalents of the two chemicals exactly match, making the calculation simple."},
        {"heading": "Real life: neutralising an acid spill \u2697\ufe0f",
         "body": "If acid spills in a lab, you neutralise it with a base. How much base you need depends on matching reactive equivalents, not just grams - a strong, multi-proton acid needs more base per gram. Normality captures that reactive punch directly, which is why safety chemists think in equivalents."},
    ]
    return {"result": "Normality = %s eq/L" % fmt(N),
            "formula_plain": "N = (w \u00d7 1000) \u00f7 (E \u00d7 V)  \u2192  reactive equivalents per litre",
            "law": "N = (w \u00d7 1000) / (E \u00d7 V)", "law_label": "Normality",
            "verified": True, "steps": steps, "explanation": explanation, "N": N, "eq": eq}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
