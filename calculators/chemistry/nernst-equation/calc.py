"""Nernst Equation — chemistry > Electrochemistry > Cell Potential. Calculate cell voltage E = E° − (0.0591/n)logQ, with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='nernst-equation', name='Nernst Equation', section="chemistry", topic='Electrochemistry', sub='Cell Potential',
    order=1,
    tags=['nernst', 'cell potential', 'battery', 'chemistry'],
    formula='E = E\\circ - \\frac{0.0591}{n}\\log Q',
    summary='Calculate cell voltage E = E° − (0.0591/n)logQ, with symbol legend and real-world examples.',
    viz_template="viz/nernst-equation.html",
    scholar='nernst',
)
def compute(E0=1.1, n=2, Q=10):
    import math
    try:
        E0 = float(E0); n = float(n); Q = float(Q)
    except (TypeError, ValueError):
        return {"error": "Enter E\u00b0, n, and Q.", "steps": []}
    if n <= 0:
        return {"error": "Number of electrons n must be greater than zero.", "steps": []}
    if Q <= 0:
        return {"error": "Reaction quotient Q must be greater than zero.", "steps": []}
    corr = (0.0591/n)*math.log10(Q)
    E = E0 - corr
    def fmt(x): return ("%g" % round(x, 5))
    steps=[
        {"label":"Step 1 - Write the formula","math":r"\( E = E^{\circ} - \dfrac{0.0591}{n}\,\log Q \)","note":"Start from the standard voltage, then adjust for the actual concentrations."},
        {"label":"Step 2 - Put in your numbers","math":r"\( E = %s - \dfrac{0.0591}{%s}\,\log(%s) \)" % (fmt(E0), fmt(n), fmt(Q)),"note":"E\u00b0 = %s V, n = %s electrons, Q = %s." % (fmt(E0), fmt(n), fmt(Q))},
        {"label":"Step 3 - Work out the correction","math":r"\( E = %s - %s = %s \text{ V} \)" % (fmt(E0), fmt(corr), fmt(E)),"note":"As the cell runs and Q changes, the voltage shifts away from E\u00b0."},
    ]
    explanation=[
        {"heading":"The formula in plain words","body":"Real voltage = standard voltage \u2212 a correction for the actual concentrations.  It tells you a battery's true voltage right now, not just the ideal value - which is why batteries fade as they drain."},
        {"heading":"What each letter means","legend":[
            ["E","The actual voltage of the cell right now (volts)."],
            ["E\u00b0","The standard voltage - the voltage when everything is at standard 1 mol/L (the circle means 'standard')."],
            ["n","Number of electrons the reaction moves each cycle."],
            ["Q","Reaction quotient - how far the reaction has gone (ratio of products to reactants right now)."],
            ["0.0591","A bundled constant for room temperature (25\u00b0C)."],
        ]},
        {"heading":"Real life: why your phone battery dies \U0001F50B","body":"As a battery discharges, its reactants get used up and Q rises, so the Nernst equation says the voltage drops. That is exactly why your phone slows charging near 100% and why a nearly-flat battery gives a lower voltage - the equation predicts the fade."},
        {"heading":"Real life: nerves firing in your body \U0001F9E0","body":"The tiny voltages your nerve and muscle cells use to send signals come from differences in ion concentrations across their membranes - and those voltages are set by the Nernst equation. Every heartbeat and thought rides on this formula."},
    ]
    return {"result":"Cell voltage E = %s V" % fmt(E),
            "formula_plain":"E = E\u00b0 \u2212 (0.0591/n) log Q  \u2192  the cell's real voltage right now",
            "law":"E = E\u00b0 \u2212 (0.0591/n) log Q","law_label":"Nernst Equation",
            "verified":True,"steps":steps,"explanation":explanation,"E":E,"E0":E0}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
