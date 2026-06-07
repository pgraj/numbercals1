"""Tree Planting Impact: number of trees \u00d7 annual CO2 sequestration \u00d7 years
\u2192 total CO2 absorbed."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

# Source: European Environment Agency widely-cited figure that a mature tree takes
# up ~21-22 kg CO2 per year; US EPA urban-tree method gives ~36.4 lb C/tree/yr
# (~60 kg CO2/yr for a large urban tree). Young/newly planted trees absorb much
# less; the default is a conservative mature-tree value. See FAQ for the range.
# https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator-calculations-and-references
KG_CO2_PER_TREE_YEAR = 21.0
TREE_SOURCE_NAME = "European Environment Agency / US EPA \u2014 tree sequestration"
TREE_SOURCE_URL = "https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator-calculations-and-references"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.2f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "How trees store carbon",
     "body": "As a tree grows it pulls CO\u2082 out of the air and locks the carbon into "
             "its wood, roots and leaves. A mature tree absorbs roughly 21 kg of CO\u2082 a "
             "year \u2014 so a small group of trees, over years, adds up to a real amount."},
    {"heading": "How this is worked out",
     "body": "Number of trees \u00d7 the yearly absorption \u00d7 the number of years. The "
             "calculator uses about " + _f(KG_CO2_PER_TREE_YEAR) + " kg CO\u2082 per tree "
             "per year as a mature-tree average."},
    {"heading": "Big caveats",
     "body": "Young, newly planted trees absorb far LESS than a mature one for their first "
             "years, and not every tree survives. Real rates vary hugely by species, "
             "climate and care. Treat this as an optimistic upper estimate, not a "
             "guarantee \u2014 the true figure for young trees is often much lower."},
]

@register(
    slug="tree-planting-impact",
    name="Tree Planting Impact",
    section="environment",
    topic="Resource Usage",
    sub="Waste & Nature",
    order=1,
    summary="Estimate the CO2 absorbed by planting trees over a number of years (mature-tree average; young trees absorb less).",
    formula="CO2 = trees \u00d7 kg/tree/year \u00d7 years",
    tags=["tree", "planting", "carbon", "co2", "sequestration", "offset", "nature"],
    viz_template="viz/tree-planting-impact.html",
    related=["recycling-impact", "carbon-emission-impact", "ev-savings-impact"],
)
def compute(trees=10.0, years=10.0, **_ignored):
    def num(v):
        if v is None or v == "":
            return None
        return float(v)
    try:
        n = num(trees); y = num(years)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}
    if n is None or y is None:
        return {"error": "Enter the number of trees and the number of years.", "steps": [], "disclaimer": _DISCLAIMER}
    if n < 0 or y < 0:
        return {"error": "Trees and years cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}

    total = n * KG_CO2_PER_TREE_YEAR * y
    tonnes = total / 1000.0
    steps = [
        {"label": "Formula", "math": r"\(\text{CO}_2 = \text{trees} \times " + _f(KG_CO2_PER_TREE_YEAR) + r" \times \text{years}\)",
         "note": "Per-tree yearly absorption times trees times years."},
        {"label": "Substitute", "math": r"\(" + _f(n) + r" \times " + _f(KG_CO2_PER_TREE_YEAR) + r" \times " + _f(y) + r"\)",
         "note": "Mature-tree average."},
        {"label": "Result", "math": r"\(" + _f(total) + r"\ \text{kg CO}_2\)",
         "note": "About " + _f(tonnes) + " tonnes over " + _f(y) + " years."},
    ]
    result = _f(total) + " kg CO\u2082 absorbed (" + _f(tonnes) + " tonnes) over " + _f(y) + " years"

    law = ("A mature tree absorbs about " + _f(KG_CO2_PER_TREE_YEAR) + " kg CO\u2082 per "
           "year. Young trees absorb much less, and survival varies \u2014 treat this as an "
           "optimistic estimate.")
    return {
        "result": result,
        "total_kg": total, "tonnes": tonnes, "factor_used": KG_CO2_PER_TREE_YEAR,
        "trees": n, "years": y,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": law, "law_source_name": TREE_SOURCE_NAME, "law_source_url": TREE_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
