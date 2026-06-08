"""Molality (m) — chemistry > Solutions & Concentration > Concentration Units. Calculate molality m = (n×1000)/W: moles of solute per kilogram of solvent, with symbol legend and real-world examples."""
from core.registry import register


@register(
    slug='molality', name='Molality (m)', section="chemistry", topic='Solutions & Concentration', sub='Concentration Units',
    order=3,
    tags=['molality', 'concentration', 'moles per kg', 'solvent', 'chemistry'],
    formula='m = \\frac{n × 1000}{W}',
    summary='Calculate molality m = (n×1000)/W: moles of solute per kilogram of solvent, with symbol legend and real-world examples.',
    viz_template="viz/molality.html",
)
def compute(n=1, W=1000):
    try:
        n = float(n); W = float(W)
    except (TypeError, ValueError):
        return {"error": "Enter moles of solute and mass of solvent.", "steps": []}
    if W <= 0:
        return {"error": "Mass of solvent must be greater than zero.", "steps": []}
    m = (n * 1000.0) / W
    def fmt(x): return ("%g" % round(x, 6))
    steps = [
        {"label": "Step 1 - Write the formula", "math": r"\( m = \dfrac{n \times 1000}{W} \)",
         "note": "Molality is moles of solute per kilogram of solvent."},
        {"label": "Step 2 - Solvent grams to kilograms", "math": r"\( W = %s \text{ g} = %s \text{ kg} \)" % (fmt(W), fmt(W/1000.0)),
         "note": "The 1000 in the formula converts the solvent mass to kilograms."},
        {"label": "Step 3 - Divide", "math": r"\( m = \dfrac{%s}{%s} = %s \text{ mol/kg} \)" % (fmt(n), fmt(W/1000.0), fmt(m)),
         "note": "Moles of solute divided by kilograms of solvent gives molality."},
    ]
    explanation = [
        {"heading": "The formula in plain words",
         "body": "Molality = moles of solute \u00f7 kilograms of solvent.  Notice it uses the mass of the solvent (the liquid doing the dissolving), not the volume of the whole solution. That makes it immune to temperature changes."},
        {"heading": "What each letter means", "legend": [
            ["m", "Molality - moles of solute per kilogram of solvent (mol/kg)."],
            ["n", "Number of moles of solute dissolved."],
            ["W", "Mass of the solvent alone, in grams."],
            ["1000", "Converts the solvent mass from grams to kilograms."],
        ]},
        {"heading": "Real life: antifreeze in a car \u2744\ufe0f",
         "body": "The amount antifreeze lowers your engine coolant's freezing point depends on molality. Mechanics effectively use a molality calculation to make sure the coolant stays liquid on the coldest night instead of freezing and cracking the engine."},
        {"heading": "Real life: salting icy roads \U0001F9C2",
         "body": "Gritting trucks spread salt to melt ice because dissolved salt lowers water's freezing point - an effect that depends on molality (moles of salt per kg of water). More salt per kilogram means a lower freezing point and clearer roads."},
    ]
    return {"result": "Molality = %s mol/kg" % fmt(m),
            "formula_plain": "m = (n \u00d7 1000) \u00f7 W  \u2192  moles of solute per kilogram of solvent",
            "law": "m = (n \u00d7 1000) / W", "law_label": "Molality",
            "verified": True, "steps": steps, "explanation": explanation, "m": m}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
