"""Hess's Law — chemistry > Thermochemistry > Reaction Enthalpy. Calculate reaction enthalpy ΔH = ΣΔH(products) − ΣΔH(reactants), with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='hess-law', name="Hess's Law", section="chemistry", topic='Thermochemistry', sub='Reaction Enthalpy',
    order=1,
    tags=['hess', 'enthalpy', 'thermochemistry', 'chemistry'],
    formula='Δ H = Σ Δ Hproduᴄts - Σ Δ Hreₐᴄtₐnts',
    summary='Calculate reaction enthalpy ΔH = ΣΔH(products) − ΣΔH(reactants), with symbol legend and real-world examples.',
    viz_template="viz/hess-law.html",
    scholar='hess',
)
def compute(products=-400, reactants=-250):
    try:
        products = float(products); reactants = float(reactants)
    except (TypeError, ValueError):
        return {"error": "Enter the total enthalpies of products and reactants.", "steps": []}
    dH = products - reactants
    def fmt(x): return ("%g" % round(x, 4))
    nature = "exothermic - it releases heat (\u0394H < 0)" if dH<0 else ("endothermic - it absorbs heat (\u0394H > 0)" if dH>0 else "no net heat change")
    steps=[
        {"label":"Step 1 - Write the formula","math":r"\( \Delta H = \sum \Delta H_{\text{products}} - \sum \Delta H_{\text{reactants}} \)","note":"Add up the products' enthalpies, then subtract the reactants'. (\u03a3 means 'sum of'.)"},
        {"label":"Step 2 - Put in your numbers","math":r"\( \Delta H = %s - %s \)" % (fmt(products), fmt(reactants)),"note":"Total products = %s, total reactants = %s." % (fmt(products), fmt(reactants))},
        {"label":"Step 3 - Subtract","math":r"\( \Delta H = %s \text{ kJ/mol} \)" % fmt(dH),"note":"Negative gives out heat; positive takes in heat."},
    ]
    explanation=[
        {"heading":"The formula in plain words","body":"Reaction heat = (total energy of products) \u2212 (total energy of reactants).  The clever part (Hess's law): the answer is the same no matter what route the reaction takes, because energy only cares about start and end."},
        {"heading":"What each letter means","legend":[
            ["\u0394H","The heat released or absorbed by the reaction (kJ/mol). Negative = gives out heat."],
            ["\u03a3","'Sum of' - add up all the items that follow."],
            ["\u0394H<sub>products</sub>","The heat content (formation enthalpy) of the products."],
            ["\u0394H<sub>reactants</sub>","The heat content of the starting reactants."],
        ]},
        {"heading":"Real life: the energy (calories) in your food \U0001F35E","body":"The Calorie count on a food label is a reaction-heat measurement: how much energy is released when the food's molecules are 'burned' in your body. Hess's law lets scientists add up the steps to get that total energy - it is on every packet you eat."},
        {"heading":"Real life: hand warmers and cold packs \U0001F525","body":"A pocket hand warmer uses an exothermic reaction (negative \u0394H) to give out heat; an instant cold pack uses an endothermic one (positive \u0394H) to suck heat in. This subtraction tells you which way the heat flows and how much - the difference between warm and cold."},
    ]
    return {"result":"Reaction enthalpy \u0394H = %s kJ/mol - %s" % (fmt(dH), nature),
            "formula_plain":"\u0394H = \u03a3\u0394H(products) \u2212 \u03a3\u0394H(reactants)  \u2192  heat released (\u2212) or absorbed (+)",
            "law":"\u0394H = \u03a3\u0394H(products) \u2212 \u03a3\u0394H(reactants)","law_label":"Hess's Law",
            "verified":True,"steps":steps,"explanation":explanation,"dH":dH,"nature":nature}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
