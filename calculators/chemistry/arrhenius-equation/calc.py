"""Arrhenius Equation — chemistry > Chemical Kinetics > Temperature Dependence. Compute the rate constant k = A·e^(−E_a/RT), with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='arrhenius-equation', name='Arrhenius Equation', section="chemistry", topic='Chemical Kinetics', sub='Temperature Dependence',
    order=3,
    tags=['arrhenius', 'activation energy', 'temperature', 'rate constant', 'chemistry'],
    formula='k = A\\,e⁻Eₐ / (R\\,T)',
    summary='Compute the rate constant k = A·e^(−E_a/RT), with symbol legend and real-world examples.',
    viz_template="viz/arrhenius-equation.html",
    scholar='arrhenius',
)
def compute(A=1e10, Ea=50000, T=300, R=8.314):
    import math
    try:
        A = float(A); Ea = float(Ea); T = float(T); R = float(R)
    except (TypeError, ValueError):
        return {"error": "Enter all four values.", "steps": []}
    if T <= 0 or R <= 0:
        return {"error": "Temperature and R must be greater than zero.", "steps": []}
    expo = -Ea / (R * T)
    k = A * math.exp(expo)
    def fmt(x): return ("%g" % round(x, 6))
    def fmtk(x): return ("%.4g" % x)
    steps=[
        {"label":"Step 1 - Write the formula","math":r"\( k = A\,e^{-E_a / (R\,T)} \)","note":"The rate constant grows fast as temperature rises and shrinks as the energy barrier grows."},
        {"label":"Step 2 - Work out the exponent","math":r"\( \dfrac{-E_a}{R\,T} = \dfrac{-%s}{%s \times %s} = %s \)" % (fmt(Ea), fmt(R), fmt(T), fmt(expo)),"note":"How big the energy barrier is compared with the available thermal energy."},
        {"label":"Step 3 - Multiply by A","math":r"\( k = %s \times e^{%s} = %s \)" % (fmt(A), fmt(expo), fmtk(k)),"note":"A is how often molecules collide the right way; the exponential is the fraction with enough energy."},
    ]
    explanation=[
        {"heading":"The formula in plain words","body":"Rate constant = collision frequency \u00d7 (fraction of collisions with enough energy).  The hotter it is, the more molecules clear the energy 'hill', so reactions speed up sharply with temperature."},
        {"heading":"What each letter means","legend":[
            ["k","Rate constant - how fast the reaction goes."],
            ["A","Frequency factor - how often molecules collide with the right aim (the top possible rate)."],
            ["e","The number 2.718... raised to a power - this gives the exponential 'temperature sensitivity'."],
            ["E<sub>a</sub>","Activation energy - the energy 'hill' molecules must climb to react (J/mol)."],
            ["R","Gas constant, 8.314 J/mol\u00b7K - keeps the units consistent."],
            ["T","Temperature in kelvin (K) - higher T means more molecules clear the hill."],
        ]},
        {"heading":"Real life: food lasts longer in the fridge \U0001F9CA","body":"Spoiling reactions follow this law. Cooling food drops T in the exponent, which slashes the rate - so milk that sours in a day on the counter lasts a week in the fridge and longer in the freezer. The Arrhenius equation is why refrigeration works."},
        {"heading":"Real life: why a fever speeds you up - and catalysts \U0001F321\ufe0f","body":"Raising temperature gives more molecules the energy to react, so body chemistry runs faster with a fever. Catalysts (and enzymes in your body) work the other way: they LOWER E_a, the hill height, so reactions fly even at normal temperature without extra heat."},
    ]
    return {"result":"Rate constant k = %s" % fmtk(k),
            "formula_plain":"k = A \u00d7 e^(\u2212E_a / (R\u00d7T))  \u2192  faster when hotter, slower with a bigger barrier",
            "law":"k = A e^(\u2212E_a/RT)","law_label":"Arrhenius Equation",
            "verified":True,"steps":steps,"explanation":explanation,"Ea":Ea}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
