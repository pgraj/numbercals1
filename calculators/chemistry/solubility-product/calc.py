"""Solubility Product (K_sp) — chemistry > Equilibrium & Acids/Bases > Equilibrium. Calculate K_sp = [A⁺][B⁻] for a sparingly soluble salt, with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='solubility-product', name='Solubility Product (K_sp)', section="chemistry", topic='Equilibrium & Acids/Bases', sub='Equilibrium',
    order=4,
    tags=['solubility product', 'ksp', 'precipitation', 'chemistry'],
    formula='Ksp = [A^+][B^-]',
    summary='Calculate K_sp = [A⁺][B⁻] for a sparingly soluble salt, with symbol legend and real-world examples.',
    viz_template="viz/solubility-product.html",
)
def compute(Aplus=1e-5, Bminus=1e-5):
    try:
        Aplus = float(Aplus); Bminus = float(Bminus)
    except (TypeError, ValueError):
        return {"error": "Enter the two ion concentrations.", "steps": []}
    if Aplus < 0 or Bminus < 0:
        return {"error": "Concentrations cannot be negative.", "steps": []}
    Ksp = Aplus * Bminus
    def fmt(x): return ("%.4g" % x)
    steps=[
        {"label":"Step 1 - Write the formula","math":r"\( K_{sp} = [A^+]\times[B^-] \)","note":"For a salt AB that splits into A\u207a and B\u207b, multiply the two ion concentrations."},
        {"label":"Step 2 - Put in your numbers","math":r"\( K_{sp} = (%s)\times(%s) \)" % (fmt(Aplus), fmt(Bminus)),"note":"[A\u207a] = %s, [B\u207b] = %s mol/L at saturation." % (fmt(Aplus), fmt(Bminus))},
        {"label":"Step 3 - Multiply","math":r"\( K_{sp} = %s \)" % fmt(Ksp),"note":"A small K_sp means the salt barely dissolves."},
    ]
    explanation=[
        {"heading":"The formula in plain words","body":"Solubility product = the two dissolved ion concentrations multiplied together, at the point where no more salt will dissolve.  A tiny K_sp means a barely-soluble salt."},
        {"heading":"What each letter means","legend":[
            ["K<sub>sp</sub>","Solubility product - how much of a barely-soluble salt can dissolve before it starts to fall out as solid."],
            ["[A<sup>+</sup>]","Concentration of the positive ion from the salt (mol/L)."],
            ["[B<sup>-</sup>]","Concentration of the negative ion from the salt (mol/L)."],
        ]},
        {"heading":"Real life: kidney stones and kettle scale \U0001FAA8","body":"When dissolved salts in your body or in hard water go past their K_sp, they fall out as solids - kidney stones in the body, chalky scale inside kettles and pipes. The solubility product is the tipping point where 'dissolved' turns into 'solid lump'."},
        {"heading":"Real life: cleaning toxic metals from water \U0001F4A7","body":"Water treatment removes poisonous metals by adding something that makes them exceed their K_sp, so they precipitate out as solids that can be filtered away. Knowing K_sp tells engineers exactly how to drop the metals out of the water safely."},
    ]
    return {"result":"Solubility product K_sp = %s" % fmt(Ksp),
            "formula_plain":"K_sp = [A\u207a] \u00d7 [B\u207b]  \u2192  how much salt can dissolve before it precipitates",
            "law":"K_sp = [A\u207a][B\u207b]  for  AB \u2192 A\u207a + B\u207b","law_label":"Solubility Product",
            "verified":True,"steps":steps,"explanation":explanation,"Ksp":Ksp}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
