"""Depression in Freezing Point (ΔT_f) — chemistry > Colligative Properties > Freezing & Boiling Points. Calculate freezing-point depression ΔT_f = K_f×m, with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='freezing-point-depression', name='Depression in Freezing Point (ΔT_f)', section="chemistry", topic='Colligative Properties', sub='Freezing & Boiling Points',
    order=3,
    tags=['freezing point', 'depression', 'colligative', 'antifreeze', 'chemistry'],
    formula='Δ Tf = Kf × m',
    summary='Calculate freezing-point depression ΔT_f = K_f×m, with symbol legend and real-world examples.',
    viz_template="viz/freezing-point-depression.html",
    scholar='raoult',
)
def compute(Kf=1.86, m=1):
    try:
        Kf = float(Kf); m = float(m)
    except (TypeError, ValueError):
        return {"error": "Enter the freezing constant and molality.", "steps": []}
    dT = Kf * m
    def fmt(x): return ("%g" % round(x, 6))
    steps=[
        {"label":"Step 1 - Write the formula","math":r"\( \Delta T_f = K_f \times m \)","note":"How far the freezing point drops = the solvent's freezing constant times the molality."},
        {"label":"Step 2 - Put in your numbers","math":r"\( \Delta T_f = %s \times %s \)" % (fmt(Kf), fmt(m)),"note":"K_f = %s (a property of the solvent), molality m = %s mol/kg." % (fmt(Kf), fmt(m))},
        {"label":"Step 3 - Multiply","math":r"\( \Delta T_f = %s\,^{\circ}C \)" % fmt(dT),"note":"The freezing point is pushed DOWN by this many degrees."},
    ]
    explanation=[
        {"heading":"The formula in plain words","body":"Drop in freezing point = freezing constant of the solvent \u00d7 how concentrated the solution is (molality).  Dissolving something makes a liquid freeze at a LOWER temperature than when it was pure."},
        {"heading":"What each letter means","legend":[
            ["\u0394T<sub>f</sub>","How many degrees the freezing point drops (\u00b0C). (\u0394 means 'change in'.)"],
            ["K<sub>f</sub>","Freezing-point constant of the solvent - degrees of drop per unit molality. For water it is 1.86."],
            ["m","Molality - moles of solute per kilogram of solvent."],
        ]},
        {"heading":"Real life: salting icy roads and paths \U0001F9C2","body":"Spreading salt on ice works because dissolved salt lowers water's freezing point, so the ice melts even though the temperature is still below normal freezing. The more salt dissolved (higher molality), the lower the freezing point and the more ice clears."},
        {"heading":"Real life: antifreeze and making ice cream \U0001F366","body":"Antifreeze stops car coolant freezing on a cold night by lowering its freezing point. And old-fashioned ice-cream makers pack salt around the ice so the salty melt gets well below 0\u00b0C, cold enough to freeze the cream. Same principle, two everyday uses."},
    ]
    return {"result":"Freezing point lowered by \u0394T_f = %s \u00b0C" % fmt(dT),
            "formula_plain":"\u0394T_f = K_f \u00d7 m  \u2192  how far the freezing point drops",
            "law":"\u0394T_f = K_f \u00d7 m","law_label":"Freezing Point Depression",
            "verified":True,"steps":steps,"explanation":explanation,"dT":dT}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
