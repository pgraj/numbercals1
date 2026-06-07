"""Recycling Impact: kg of material recycled instead of landfilled \u2192 kg CO2e
avoided, using EPA WARM mixed-recyclables factor."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

# Source: US EPA WARM v16 / Greenhouse Gas Equivalencies: recycling instead of
# landfilling mixed municipal waste avoids 2.83 metric tons CO2e per short ton
# (= 2.83 t / 907.18 kg = ~3.12 kg CO2e per kg). Per-material values differ \u2014
# aluminium and paper save far more, glass less; see FAQ and WARM for specifics.
# https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator-calculations-and-references
AVOIDED_KG_PER_KG = 2.83 * 1000.0 / 907.18472  # ~3.12 kg CO2e per kg mixed recyclables
RECYCLE_SOURCE_NAME = "US EPA \u2014 WARM / Greenhouse Gas Equivalencies"
RECYCLE_SOURCE_URL = "https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator-calculations-and-references"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.2f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "Why recycling avoids CO\u2082",
     "body": "Making something from recycled material usually takes far less energy than "
             "making it from scratch, and keeping waste out of landfill avoids the methane "
             "it would give off there. Both effects together are the 'avoided' emissions."},
    {"heading": "How this is worked out",
     "body": "The calculator uses the US EPA's average figure for mixed recyclables: about "
             + _f(AVOIDED_KG_PER_KG) + " kg of CO\u2082e avoided for every kilogram "
             "recycled instead of landfilled. Multiply by how much you recycle and you get "
             "the total avoided."},
    {"heading": "Materials differ a lot",
     "body": "This is an average across typical household recyclables. Aluminium and paper "
             "save much more per kilogram (aluminium especially), while glass saves less. "
             "For a single material, the EPA's WARM tool gives a material-specific factor."},
]

@register(
    slug="recycling-impact",
    name="Recycling Impact",
    section="environment",
    topic="Resource Usage",
    sub="Waste & Nature",
    order=0,
    summary="Estimate the CO2e avoided by recycling mixed materials instead of sending them to landfill (EPA WARM average).",
    formula="avoided = kg recycled \u00d7 EPA factor",
    tags=["recycling", "waste", "carbon", "co2", "landfill", "avoided", "epa"],
    viz_template="viz/recycling-impact.html",
    related=["tree-planting-impact", "carbon-emission-impact", "water-usage-impact"],
)
def compute(kg=10.0, **_ignored):
    def num(v):
        if v is None or v == "":
            return None
        return float(v)
    try:
        m = num(kg)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}
    if m is None:
        return {"error": "Enter the mass recycled in kilograms.", "steps": [], "disclaimer": _DISCLAIMER}
    if m < 0:
        return {"error": "Mass recycled cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}

    avoided = m * AVOIDED_KG_PER_KG
    steps = [
        {"label": "Formula", "math": r"\(\text{avoided} = \text{kg} \times " + _f(AVOIDED_KG_PER_KG) + r"\)",
         "note": "EPA mixed-recyclables factor (kg CO2e avoided per kg)."},
        {"label": "Substitute", "math": r"\(" + _f(m) + r" \times " + _f(AVOIDED_KG_PER_KG) + r"\)",
         "note": "Kilograms recycled instead of landfilled."},
        {"label": "Result", "math": r"\(" + _f(avoided) + r"\ \text{kg CO}_2\text{e avoided}\)",
         "note": "Emissions kept out of the atmosphere."},
    ]
    result = _f(avoided) + " kg CO\u2082e avoided by recycling " + _f(m) + " kg"

    law = ("Recycling mixed waste instead of landfilling it avoids about "
           + _f(AVOIDED_KG_PER_KG) + " kg CO\u2082e per kilogram, per the US EPA WARM "
           "model. Per-material savings vary (aluminium and paper save more, glass less).")
    return {
        "result": result,
        "avoided_kg": avoided, "factor_used": AVOIDED_KG_PER_KG,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": law, "law_source_name": RECYCLE_SOURCE_NAME, "law_source_url": RECYCLE_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
