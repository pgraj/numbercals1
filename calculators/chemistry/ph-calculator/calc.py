"""pH Calculator — chemistry > Equilibrium & Acids/Bases > Acids & Bases. Calculate pH = −log[H⁺] and classify acidity, with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='ph-calculator', name='pH Calculator', section="chemistry", topic='Equilibrium & Acids/Bases', sub='Acids & Bases',
    order=2,
    tags=['ph', 'acid', 'base', 'chemistry'],
    formula='\\text{pH} = -\\log[H^+]',
    summary='Calculate pH = −log[H⁺] and classify acidity, with symbol legend and real-world examples.',
    viz_template="viz/ph-calculator.html",
)
def compute(H=1e-3):
    import math
    try:
        H = float(H)
    except (TypeError, ValueError):
        return {"error": "Enter the hydrogen ion concentration [H\u207a].", "steps": []}
    if H <= 0:
        return {"error": "[H\u207a] must be greater than zero.", "steps": []}
    pH = -math.log10(H)
    def fmt(x): return ("%g" % round(x, 4))
    nature = "acidic" if pH < 7 else ("basic (alkaline)" if pH > 7 else "neutral")
    steps=[
        {"label":"Step 1 - Write the formula","math":r"\( \text{pH} = -\log[H^+] \)","note":"pH turns the hydrogen-ion concentration into an easy 0-14 number."},
        {"label":"Step 2 - Put in your number","math":r"\( \text{pH} = -\log(%s) \)" % fmt(H),"note":"[H\u207a] = %s mol/L is the concentration of hydrogen ions." % fmt(H)},
        {"label":"Step 3 - Take the log","math":r"\( \text{pH} = %s \)" % fmt(pH),"note":"This solution is %s." % nature},
    ]
    explanation=[
        {"heading":"The formula in plain words","body":"pH = minus the log of the hydrogen-ion concentration.  It squashes a huge range of acidity into a simple 0-14 scale: low pH = acidic, 7 = neutral, high pH = basic."},
        {"heading":"What each letter means","legend":[
            ["pH","A 0-14 number for how acidic or basic something is. Lower = more acidic."],
            ["log","Base-10 logarithm - it compresses the huge range of concentrations."],
            ["[H<sup>+</sup>]","Concentration of hydrogen ions in mol/L (the brackets mean 'concentration of'). More H\u207a = more acidic."],
            ["\u2212 (minus)","Flips the usually-negative log into a friendly positive pH number."],
        ]},
        {"heading":"Real life: your stomach, soap and shampoo \U0001F9F4","body":"Stomach acid is about pH 2 (very acidic, to digest food); soap is basic around pH 9-10; 'pH-balanced' shampoo is made close to your skin's natural pH so it doesn't sting or dry you out. Reading pH is how products are matched to your body."},
        {"heading":"Real life: pools, soil and fish tanks \U0001F3CA","body":"Pool water is kept near pH 7.4 so it doesn't sting eyes or corrode pipes; gardeners test soil pH because plants only thrive in the right range; aquarium owners watch pH so their fish stay healthy. A simple test strip is reading this formula."},
    ]
    return {"result":"pH = %s (%s)" % (fmt(pH), nature),
            "formula_plain":"pH = \u2212log[H\u207a]  \u2192  how acidic (low) or basic (high) a solution is",
            "law":"pH = \u2212log[H\u207a]","law_label":"pH",
            "verified":True,"steps":steps,"explanation":explanation,"pH":pH,"nature":nature}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
