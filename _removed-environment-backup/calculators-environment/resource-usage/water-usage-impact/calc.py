"""Water Usage Impact: litres of municipal water \u2192 embedded energy (supply +
treatment) \u2192 CO2 via the country grid factor."""
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

# Embodied energy of municipal water (supply + distribution + wastewater treatment),
# before any home water heating. Source: typical literature values \u2014 US supply
# national average ~0.37 kWh/m3 (World Bank ESMAP) plus wastewater treatment
# ~0.5 kWh/m3 (lower end of 0.5-2.0 kWh/m3 range). Combined default ~0.6 kWh/m3.
WATER_KWH_PER_M3 = 0.6
WATER_SOURCE_NAME = "World Bank ESMAP / MDPI \u2014 energy intensity of water"
WATER_SOURCE_URL = "https://www.esmap.org/sites/default/files/esmap-files/FINAL_EECI-WWU_TR001-12_Resized.pdf"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    if abs(x) < 1: return ("%.3f" % x).rstrip("0").rstrip(".")
    return ("%.2f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "Water has a carbon cost too",
     "body": "Clean tap water does not arrive for free: it must be pumped, treated and "
             "distributed, and the wastewater treated afterwards \u2014 all of which uses "
             "electricity. So every litre carries a small hidden carbon footprint."},
    {"heading": "How it is worked out",
     "body": "The calculator multiplies your litres by the energy needed per cubic metre "
             "(about " + _f(WATER_KWH_PER_M3) + " kWh per 1000 L for supply plus "
             "treatment), then turns that electricity into CO\u2082 using your country's "
             "grid factor."},
    {"heading": "What this leaves out",
     "body": "This is the energy to supply and treat the water only. It does NOT include "
             "heating water at home (a hot shower's carbon is mostly the water heater, not "
             "the supply). Figures also vary widely by region, water source and treatment "
             "method."},
]

@register(
    slug="water-usage-impact",
    name="Water Usage Impact",
    section="environment",
    topic="Resource Usage",
    sub="Energy & Water",
    order=1,
    summary="Estimate the CO2 from the energy used to supply and treat municipal water, using your country's grid factor.",
    formula="CO2e = litres \u2192 kWh \u00d7 grid factor",
    tags=["water", "usage", "carbon", "co2", "energy", "treatment", "footprint"],
    viz_template="viz/water-usage-impact.html",
    related=["energy-usage-impact", "carbon-emission-impact", "recycling-impact"],
)
def compute(country="IN", litres=1000.0, **_ignored):
    def num(v):
        if v is None or v == "":
            return None
        return float(v)
    try:
        L = num(litres)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}
    if L is None:
        return {"error": "Enter the water used in litres.", "steps": [], "disclaimer": _DISCLAIMER}
    if L < 0:
        return {"error": "Water used cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}

    g, country_name = grid_factor(country)
    m3 = L / 1000.0
    kwh = m3 * WATER_KWH_PER_M3
    co2 = kwh * g / 1000.0

    steps = [
        {"label": "Energy", "math": r"\(\dfrac{" + _f(L) + r"}{1000} \times " + _f(WATER_KWH_PER_M3) + r"\ \text{kWh/m}^3\)",
         "note": "Litres to cubic metres, times the energy per m\u00b3 = " + _f(kwh) + " kWh."},
        {"label": "To CO2", "math": r"\(" + _f(kwh) + r" \times " + _f(g) + r"\ \text{g/kWh}\)",
         "note": "Using the grid factor for " + country_name + "."},
        {"label": "Result", "math": r"\(" + _f(co2) + r"\ \text{kg CO}_2\text{e}\)", "note": "Grams to kilograms."},
    ]
    result = _f(co2) + " kg CO\u2082e to supply " + _f(L) + " L of water in " + country_name

    law = ("Supplying and treating water uses about " + _f(WATER_KWH_PER_M3)
           + " kWh per 1000 litres; that electricity's carbon depends on the grid ("
           + country_name + ": " + _f(g) + " g CO\u2082e/kWh). Excludes home heating.")
    return {
        "result": result, "country": country_name,
        "co2_kg": co2, "kwh": kwh, "grid_factor": g,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": law, "law_source_name": WATER_SOURCE_NAME, "law_source_url": WATER_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
