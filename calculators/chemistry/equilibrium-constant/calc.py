"""Equilibrium Constant (K_c) — chemistry > Equilibrium & Acids/Bases > Equilibrium. Calculate K_c = [Products]/[Reactants], with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='equilibrium-constant', name='Equilibrium Constant (K_c)', section="chemistry", topic='Equilibrium & Acids/Bases', sub='Equilibrium',
    order=1,
    tags=['equilibrium', 'kc', 'chemistry'],
    formula='Kᴄ = \\frac{[\\text{Products}]}{[\\text{Reactants}]}',
    summary='Calculate K_c = [Products]/[Reactants], with symbol legend and real-world examples.',
    viz_template="viz/equilibrium-constant.html",
)
def compute(products=4, reactants=2):
    try:
        products = float(products); reactants = float(reactants)
    except (TypeError, ValueError):
        return {"error": "Enter the product and reactant terms.", "steps": []}
    if reactants == 0:
        return {"error": "The reactant term cannot be zero.", "steps": []}
    Kc = products / reactants
    def fmt(x): return ("%g" % round(x, 6))
    note = "K_c > 1: products are favoured." if Kc>1 else ("K_c < 1: reactants are favoured." if Kc<1 else "K_c = 1: evenly balanced.")
    steps=[
        {"label":"Step 1 - Write the formula","math":r"\( K_c = \dfrac{[\text{Products}]}{[\text{Reactants}]} \)","note":"K_c compares how much product sits at balance versus how much reactant."},
        {"label":"Step 2 - Put in your numbers","math":r"\( K_c = \dfrac{%s}{%s} \)" % (fmt(products), fmt(reactants)),"note":"Products term = %s, reactants term = %s (at equilibrium)." % (fmt(products), fmt(reactants))},
        {"label":"Step 3 - Divide","math":r"\( K_c = %s \)" % fmt(Kc),"note":note},
    ]
    explanation=[
        {"heading":"The formula in plain words","body":"Equilibrium constant = (amount of products) \u00f7 (amount of reactants) once the reaction has settled.  A big K_c means the reaction mostly finishes (lots of product); a small K_c means it barely gets going."},
        {"heading":"What each letter means","legend":[
            ["K<sub>c</sub>","Equilibrium constant - the product-to-reactant ratio at balance (no units here)."],
            ["[Products]","Concentration term for the products at equilibrium (the square brackets mean 'concentration of')."],
            ["[Reactants]","Concentration term for the reactants at equilibrium."],
        ]},
        {"heading":"Real life: making ammonia for fertiliser \U0001F33E","body":"The Haber process makes ammonia for the fertiliser that feeds the world. Engineers choose pressure and temperature to push K_c toward products, squeezing out the most ammonia. Billions of people are fed because of getting this equilibrium right."},
        {"heading":"Real life: fizzy drinks and your breath \U0001FAE7","body":"Dissolved CO\u2082 in a drink, and CO\u2082 in your blood, both sit in an equilibrium described by a constant like this. It is why your body can load and unload carbon dioxide as you breathe - shifting the balance back and forth."},
    ]
    return {"result":"Equilibrium constant K_c = %s" % fmt(Kc),
            "formula_plain":"K_c = [Products] \u00f7 [Reactants]  \u2192  which side the reaction favours",
            "law":"K_c = [Products] / [Reactants]","law_label":"Equilibrium Constant",
            "verified":True,"steps":steps,"explanation":explanation,"P":products,"R":reactants,"Kc":Kc,"note":note}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
