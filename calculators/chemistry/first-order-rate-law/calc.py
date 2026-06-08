"""First Order Rate Law — chemistry > Chemical Kinetics > Rate Laws. Find the first-order rate constant k = (2.303/t)log([A]₀/[A]), with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='first-order-rate-law', name='First Order Rate Law', section="chemistry", topic='Chemical Kinetics', sub='Rate Laws',
    order=2,
    tags=['first order', 'rate constant', 'kinetics', 'half-life', 'chemistry'],
    formula='k = \\frac{2.303}{t}\\,\\log\\frac{[A]₀}{[A]}',
    summary='Find the first-order rate constant k = (2.303/t)log([A]₀/[A]), with symbol legend and real-world examples.',
    viz_template="viz/first-order-rate-law.html",
)
def compute(A0=1, A=0.5, t=693):
    import math
    try:
        A0 = float(A0); A = float(A); t = float(t)
    except (TypeError, ValueError):
        return {"error": "Enter the starting amount, the amount left, and the time.", "steps": []}
    if t <= 0 or A0 <= 0 or A <= 0:
        return {"error": "Amounts and time must be greater than zero.", "steps": []}
    if A > A0:
        return {"error": "The amount left cannot be more than you started with.", "steps": []}
    ratio = A0 / A
    k = (2.303 / t) * math.log10(ratio)
    def fmt(x): return ("%g" % round(x, 6))
    steps=[
        {"label":"Step 1 - Write the formula","math":r"\( k = \dfrac{2.303}{t}\,\log\dfrac{[A]_0}{[A]} \)","note":"This finds the rate constant k for a reaction whose speed depends on one reactant."},
        {"label":"Step 2 - Find the ratio left","math":r"\( \dfrac{[A]_0}{[A]} = \dfrac{%s}{%s} = %s \)" % (fmt(A0), fmt(A), fmt(ratio)),"note":"How many times bigger the start was than what remains."},
        {"label":"Step 3 - Take the log and finish","math":r"\( k = \dfrac{2.303}{%s}\times\log(%s) = %s \text{ s}^{-1} \)" % (fmt(t), fmt(ratio), fmt(k)),"note":"The 2.303 turns the base-10 log into the natural log the maths needs."},
    ]
    explanation=[
        {"heading":"The formula in plain words","body":"Rate constant k = (2.303 \u00f7 time) \u00d7 log(starting amount \u00f7 amount left).  A 'first-order' reaction loses the same FRACTION of itself in each equal slice of time - it decays exponentially, like radioactivity."},
        {"heading":"What each letter means","legend":[
            ["k","Rate constant - how fast this reaction decays, per second (s\u207b\u00b9). Bigger k = faster."],
            ["t","Time that has passed, in seconds."],
            ["[A]<sub>0</sub>","The amount of reactant you STARTED with (the little 0 means 'at the start')."],
            ["[A]","The amount of reactant LEFT now."],
            ["2.303","A fixed number that converts a base-10 log into a natural log."],
        ]},
        {"heading":"Real life: medicine leaving your body \U0001F48A","body":"Most drugs clear from your blood in a first-order way - a fixed fraction every hour. That fixed pattern gives each medicine a 'half-life', which is exactly why a label says 'every 8 hours': it keeps the drug in the helpful range. This rate constant is how pharmacists set safe doses."},
        {"heading":"Real life: carbon dating ancient things \U0001F9B4","body":"Living things absorb carbon-14, which then decays in a first-order way with a known half-life of about 5,730 years. By measuring how much is left in an old bone or wood and using this same maths, scientists work out how long ago it died - dating fossils and archaeology."},
    ]
    return {"result":"Rate constant k = %s s\u207b\u00b9" % fmt(k),
            "formula_plain":"k = (2.303 \u00f7 t) \u00d7 log([A]\u2080 \u00f7 [A])  \u2192  the decay rate constant",
            "law":"k = (2.303/t) log([A]\u2080/[A])","law_label":"First Order Rate Law",
            "verified":True,"steps":steps,"explanation":explanation,"k":k}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
