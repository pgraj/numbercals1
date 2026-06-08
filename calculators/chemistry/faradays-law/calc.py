"""Faraday's Law of Electrolysis — chemistry > Electrochemistry > Electrolysis. Calculate mass deposited in electrolysis W = EIt/96500, with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='faradays-law', name="Faraday's Law of Electrolysis", section="chemistry", topic='Electrochemistry', sub='Electrolysis',
    order=3,
    tags=['faraday', 'electrolysis', 'electroplating', 'chemistry'],
    formula='W = \\frac{E\\,I\\,t}{96500}',
    summary='Calculate mass deposited in electrolysis W = EIt/96500, with symbol legend and real-world examples.',
    viz_template="viz/faradays-law.html",
    scholar='faraday',
)
def compute(E=1, I=2, t=965):
    try:
        E = float(E); I = float(I); t = float(t)
    except (TypeError, ValueError):
        return {"error": "Enter equivalent weight, current, and time.", "steps": []}
    if I < 0 or t < 0:
        return {"error": "Current and time cannot be negative.", "steps": []}
    Q = I*t
    W = (E * I * t) / 96500.0
    def fmt(x): return ("%g" % round(x, 5))
    steps=[
        {"label":"Step 1 - Write the formula","math":r"\( W = \dfrac{E \times I \times t}{96500} \)","note":"The mass deposited depends on how much electric charge you pass."},
        {"label":"Step 2 - Find the charge passed","math":r"\( Q = I \times t = %s \times %s = %s \text{ C} \)" % (fmt(I), fmt(t), fmt(Q)),"note":"Charge = current \u00d7 time, in coulombs."},
        {"label":"Step 3 - Convert charge to mass","math":r"\( W = \dfrac{%s \times %s}{96500} = %s \text{ g} \)" % (fmt(E), fmt(Q), fmt(W)),"note":"Dividing by 96500 (the Faraday constant) turns charge into moles of substance."},
    ]
    explanation=[
        {"heading":"The formula in plain words","body":"Mass deposited = (equivalent weight \u00d7 current \u00d7 time) \u00f7 96500.  The more electric charge you push through, the more metal builds up on the electrode."},
        {"heading":"What each letter means","legend":[
            ["W","Mass of substance deposited or dissolved at the electrode, in grams."],
            ["E","Equivalent weight = molar mass \u00f7 electrons needed per ion."],
            ["I","Electric current, in amperes (amps)."],
            ["t","Time the current flows, in seconds."],
            ["96500","The Faraday constant - the charge carried by one mole of electrons (coulombs)."],
        ]},
        {"heading":"Real life: gold-plated jewellery and chrome \U0001F48D","body":"Electroplating coats cheap metal with a thin layer of gold, silver or chrome by passing current through a solution. This formula tells the manufacturer exactly how much current and time give the right thickness - too little looks patchy, too much wastes precious metal."},
        {"heading":"Real life: refining the copper in your wires \U0001F50C","body":"The copper in household wiring is purified by electrolysis - current pulls pure copper onto an electrode and leaves impurities behind. Faraday's law sets how much pure copper you get per amp-hour, which is core to the whole electrical industry."},
    ]
    return {"result":"Mass deposited W = %s g" % fmt(W),
            "formula_plain":"W = (E \u00d7 I \u00d7 t) \u00f7 96500  \u2192  more charge means more metal deposited",
            "law":"W = EIt / 96500","law_label":"Faraday's Law",
            "verified":True,"steps":steps,"explanation":explanation,"W":W,"Q":Q}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
