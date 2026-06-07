"""Energy Usage Impact: electricity use (kWh) \u00d7 country grid factor \u2192 kg CO2e,
with an optional electricity price to show the cost too."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

# --- Grid electricity carbon intensity (lifecycle gCO2eq/kWh) ---------------
# Source: Ember, Yearly Electricity Data, via Our World in Data energy dataset
# (CC-BY 4.0): https://github.com/owid/energy-data  column "carbon_intensity_elec".
# Latest available year per country (2024-2025). Default country: India.
GRID_SOURCE_NAME = "Ember / Our World in Data \u2014 carbon intensity of electricity"
GRID_SOURCE_URL = "https://ourworldindata.org/grapher/carbon-intensity-electricity"
GRID_GCO2_PER_KWH = {
    "IN": 670.1, "AU": 525.2, "US": 384.4, "CN": 525.3, "GB": 217.4, "DE": 329.6,
    "FR": 41.4, "CA": 190.7, "JP": 477.3, "KR": 417.1, "BR": 110.0, "RU": 449.7,
    "ID": 680.2, "MX": 474.0, "ZA": 699.3, "IT": 284.8, "ES": 153.6, "SA": 692.0,
    "TR": 474.7, "NL": 253.6, "PL": 588.6, "SE": 35.3, "NO": 28.1, "NZ": 92.8,
    "AE": 467.5, "SG": 497.1, "GLOBAL": 458.3,
}
GRID_COUNTRY_NAME = {
    "IN": "India", "AU": "Australia", "US": "United States", "CN": "China",
    "GB": "United Kingdom", "DE": "Germany", "FR": "France", "CA": "Canada",
    "JP": "Japan", "KR": "South Korea", "BR": "Brazil", "RU": "Russia",
    "ID": "Indonesia", "MX": "Mexico", "ZA": "South Africa", "IT": "Italy",
    "ES": "Spain", "SA": "Saudi Arabia", "TR": "Turkey", "NL": "Netherlands",
    "PL": "Poland", "SE": "Sweden", "NO": "Norway", "NZ": "New Zealand",
    "AE": "United Arab Emirates", "SG": "Singapore", "GLOBAL": "Global average",
}
def grid_factor(country):
    """Return (gCO2/kWh, country_name) for an ISO-ish code; default India."""
    c = str(country or "IN").upper()
    if c not in GRID_GCO2_PER_KWH:
        c = "IN"
    return GRID_GCO2_PER_KWH[c], GRID_COUNTRY_NAME[c]

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.2f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "Turning kilowatt-hours into carbon",
     "body": "Your meter measures electricity in kilowatt-hours (kWh). Each kWh carries a "
             "carbon cost that depends on how your country generates power. Multiply your "
             "kWh by that grid factor and you get the CO\u2082 released."},
    {"heading": "Why country matters",
     "body": "The same appliance run for the same time emits very different amounts of "
             "CO\u2082 depending on the grid. A coal-heavy grid can be ten times more "
             "carbon-intensive than a hydro- or nuclear-heavy one, so the country you pick "
             "changes the answer a lot."},
    {"heading": "The optional cost",
     "body": "If you enter your electricity price per kWh, the calculator also shows what "
             "that energy costs. Carbon and money often move together \u2014 using less "
             "energy cuts both."},
]

@register(
    slug="energy-usage-impact",
    name="Energy Usage Impact",
    section="environment",
    topic="Resource Usage",
    sub="Energy & Water",
    order=0,
    summary="Convert electricity use (kWh) into kg CO2e using your country's grid factor, with an optional cost estimate.",
    formula="CO2e = kWh \u00d7 grid factor",
    tags=["energy", "electricity", "kwh", "carbon", "co2", "grid", "cost"],
    viz_template="viz/energy-usage-impact.html",
    related=["carbon-emission-impact", "water-usage-impact", "household-carbon-reduction"],
)
def compute(country="IN", kwh=100.0, price_per_kwh=None, **_ignored):
    def num(v):
        if v is None or v == "":
            return None
        return float(v)
    try:
        E = num(kwh); price = num(price_per_kwh)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}
    if E is None:
        return {"error": "Enter the electricity used in kWh.", "steps": [], "disclaimer": _DISCLAIMER}
    if E < 0:
        return {"error": "Electricity used cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}

    g, country_name = grid_factor(country)
    co2 = E * g / 1000.0

    steps = [
        {"label": "Formula", "math": r"\(\text{CO}_2\text{e} = \text{kWh} \times \text{grid factor}\)",
         "note": "Grid factor in g CO2e/kWh."},
        {"label": "Substitute", "math": r"\(" + _f(E) + r" \times " + _f(g) + r"\ \text{g/kWh}\)",
         "note": "Grid factor for " + country_name + "."},
        {"label": "Result", "math": r"\(" + _f(co2) + r"\ \text{kg CO}_2\text{e}\)",
         "note": "Grams converted to kilograms."},
    ]
    result = _f(co2) + " kg CO\u2082e from " + _f(E) + " kWh in " + country_name
    cost = None
    if price is not None:
        if price < 0:
            return {"error": "Price cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}
        cost = E * price
        steps.append({"label": "Cost", "math": r"\(" + _f(E) + r" \times " + _f(price) + r"\)",
                      "note": "Electricity used times your price per kWh."})
        result += "  \u00b7  cost " + _f(cost)

    law = ("Electricity's carbon depends on the generation mix. The grid factor for "
           + country_name + " is " + _f(g) + " g CO\u2082e per kWh (lifecycle).")
    return {
        "result": result, "country": country_name,
        "co2_kg": co2, "grid_factor": g, "cost": cost,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": law, "law_source_name": GRID_SOURCE_NAME, "law_source_url": GRID_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
