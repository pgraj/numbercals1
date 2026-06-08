"""Osmotic Pressure (π = CRT) — chemistry > Colligative Properties > Osmosis. Calculate osmotic pressure π = CRT, with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='osmotic-pressure', name='Osmotic Pressure (π = CRT)', section="chemistry", topic='Colligative Properties', sub='Osmosis',
    order=2,
    tags=['osmotic pressure', 'osmosis', 'colligative', "van't hoff", 'chemistry'],
    formula='π = C × R × T',
    summary='Calculate osmotic pressure π = CRT, with symbol legend and real-world examples.',
    viz_template="viz/osmotic-pressure.html",
    scholar='vant-hoff',
)
def compute(C=0.1, R=0.0821, T=300):
    try:
        C = float(C); R = float(R); T = float(T)
    except (TypeError, ValueError):
        return {"error": "Enter concentration, R, and temperature.", "steps": []}
    if T <= 0 or R <= 0:
        return {"error": "R and temperature must be greater than zero.", "steps": []}
    pi = C * R * T
    def fmt(x): return ("%g" % round(x, 6))
    steps = [
        {"label": "Step 1 - Write the formula", "math": r"\( \pi = C \times R \times T \)",
         "note": "Osmotic pressure rises with concentration and temperature."},
        {"label": "Step 2 - Put in your numbers", "math": r"\( \pi = %s \times %s \times %s \)" % (fmt(C), fmt(R), fmt(T)),
         "note": "C = %s mol/L, R = %s (gas constant), T = %s K." % (fmt(C), fmt(R), fmt(T))},
        {"label": "Step 3 - Multiply", "math": r"\( \pi = %s \text{ atm} \)" % fmt(pi),
         "note": "This is the pressure needed to stop solvent flowing into the solution."},
    ]
    explanation=[
        {"heading":"The formula in plain words",
         "body":"Osmotic pressure = concentration \u00d7 gas constant \u00d7 temperature.  It is the push needed to STOP pure solvent from flowing into a solution through a membrane. Notice it looks just like the gas law - dissolved particles behave a lot like a gas."},
        {"heading":"What each letter means","legend":[
            ["\u03c0","Osmotic pressure - the pressure needed to stop osmosis (atm). (Greek letter 'pi'.)"],
            ["C","Molar concentration of the solution (mol/L) - how crowded the dissolved particles are."],
            ["R","The gas constant, 0.0821 L\u00b7atm/mol\u00b7K - a fixed number of nature."],
            ["T","Temperature in kelvin (K) - warmer solutions push harder."],
        ]},
        {"heading":"Real life: why a wilted plant perks up in water \U0001F331",
         "body":"Plant cells pull in water by osmosis because the inside is more concentrated than the water outside. That inflow creates pressure that keeps stems and leaves stiff and upright. A thirsty, wilted plant droops; give it water and osmotic pressure puffs the cells back up so it stands tall again."},
        {"heading":"Real life: cleaning seawater into drinking water \U0001F30A",
         "body":"Reverse osmosis desalination pushes seawater against a membrane with MORE than its osmotic pressure, forcing pure water through backwards and leaving the salt behind. Knowing the osmotic pressure tells engineers exactly how hard to push - it is the science behind drinking water on ships and in dry countries."},
    ]
    return {"result":"Osmotic pressure \u03c0 = %s atm" % fmt(pi),
            "formula_plain":"\u03c0 = C \u00d7 R \u00d7 T  \u2192  pressure to stop solvent crossing the membrane",
            "law":"\u03c0 = C \u00d7 R \u00d7 T","law_label":"Osmotic Pressure",
            "verified":True,"steps":steps,"explanation":explanation,"pi":pi,"C":C}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
