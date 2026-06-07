"""Carbon Emission Impact: estimate kg CO2e from an everyday activity \u2014
electricity use (kWh \u00d7 country grid factor), petrol use (litres), or driving
distance (km \u00f7 economy \u2192 litres \u2192 CO2)."""
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

# --- Petrol -----------------------------------------------------------------
# Source: GHG Protocol / ADEME standard factor; cross-check US EPA 8.887 kg CO2
# per US gallon (= 2.35 kg/L). https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator-calculations-and-references
PETROL_KG_PER_L = 2.31
PETROL_SOURCE_NAME = "US EPA \u2014 Greenhouse Gas Equivalencies (petrol)"
PETROL_SOURCE_URL = "https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator-calculations-and-references"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.2f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "How the estimate works",
     "body": "Every activity has an 'emission factor' \u2014 the kilograms of CO\u2082 it "
             "releases per unit. Multiply how much you did (kWh of electricity, litres of "
             "petrol, or kilometres driven) by that factor and you get the carbon "
             "footprint in kilograms of CO\u2082-equivalent."},
    {"heading": "Why electricity depends on your country",
     "body": "A kilowatt-hour in France (mostly nuclear) carries far less CO\u2082 than one "
             "in India or South Africa (more coal). That is why the calculator asks for "
             "your country \u2014 it picks the right grid factor. Petrol, by contrast, "
             "releases about the same CO\u2082 per litre everywhere it is burned."},
    {"heading": "What 'CO\u2082e' means",
     "body": "CO\u2082-equivalent bundles all greenhouse gases into one number, expressed as "
             "the amount of CO\u2082 that would have the same warming effect. It lets you "
             "compare very different activities on one scale."},
]

@register(
    slug="carbon-emission-impact",
    name="Carbon Emission Impact",
    section="environment",
    topic="Carbon & Emissions",
    sub="Footprint",
    order=0,
    summary="Estimate the kg CO2e of electricity use, petrol use or driving, using country-specific grid factors and a standard petrol factor.",
    formula="CO2e = activity \u00d7 emission factor",
    tags=["carbon", "emission", "co2", "footprint", "electricity", "petrol", "driving"],
    viz_template="viz/carbon-emission-impact.html",
    related=["energy-usage-impact", "ev-savings-impact", "household-carbon-reduction"],
)
def compute(activity="electricity", country="IN",
            kwh=100.0, litres=50.0, distance_km=500.0, economy_l_per_100km=8.0,
            **_ignored):
    try:
        act = str(activity or "electricity").strip().lower()
    except Exception:
        act = "electricity"

    def num(v):
        if v is None or v == "":
            return None
        return float(v)

    g, country_name = grid_factor(country)

    try:
        if act == "electricity":
            E = num(kwh)
            if E is None:
                return {"error": "Enter the electricity used in kWh.", "steps": [], "disclaimer": _DISCLAIMER}
            if E < 0:
                return {"error": "Electricity used cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}
            co2 = E * g / 1000.0  # g/kWh -> kg
            law = ("Electricity's carbon depends on how it is generated. The grid factor for "
                   + country_name + " is " + _f(g) + " g CO\u2082e per kWh (lifecycle).")
            law_name, law_url = GRID_SOURCE_NAME, GRID_SOURCE_URL
            steps = [
                {"label": "Formula", "math": r"\(\text{CO}_2\text{e} = \text{kWh} \times \text{grid factor}\)",
                 "note": "Grid factor in g CO2e per kWh, converted to kg."},
                {"label": "Substitute", "math": r"\(" + _f(E) + r" \times " + _f(g) + r"\ \text{g/kWh}\)",
                 "note": "Grid factor for " + country_name + "."},
                {"label": "Result", "math": r"\(" + _f(co2) + r"\ \text{kg CO}_2\text{e}\)",
                 "note": "Divide by 1000 to convert grams to kilograms."},
            ]
            result = _f(co2) + " kg CO\u2082e from " + _f(E) + " kWh in " + country_name
            factor_used = g; factor_unit = "g CO\u2082e/kWh"

        elif act == "petrol":
            L = num(litres)
            if L is None:
                return {"error": "Enter the petrol used in litres.", "steps": [], "disclaimer": _DISCLAIMER}
            if L < 0:
                return {"error": "Petrol used cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}
            co2 = L * PETROL_KG_PER_L
            law = ("Burning one litre of petrol releases about " + _f(PETROL_KG_PER_L)
                   + " kg of CO\u2082 \u2014 roughly the same anywhere, because it is set by "
                     "the fuel's chemistry, not the local grid.")
            law_name, law_url = PETROL_SOURCE_NAME, PETROL_SOURCE_URL
            steps = [
                {"label": "Formula", "math": r"\(\text{CO}_2 = \text{litres} \times " + _f(PETROL_KG_PER_L) + r"\)",
                 "note": "Standard petrol factor in kg CO2 per litre."},
                {"label": "Substitute", "math": r"\(" + _f(L) + r" \times " + _f(PETROL_KG_PER_L) + r"\)",
                 "note": "Litres of petrol burned."},
                {"label": "Result", "math": r"\(" + _f(co2) + r"\ \text{kg CO}_2\)", "note": "Carbon dioxide released."},
            ]
            result = _f(co2) + " kg CO\u2082 from " + _f(L) + " L of petrol"
            factor_used = PETROL_KG_PER_L; factor_unit = "kg CO\u2082/L"

        elif act == "driving":
            D = num(distance_km); eco = num(economy_l_per_100km)
            if D is None or eco is None:
                return {"error": "Enter the distance (km) and fuel economy (L/100km).", "steps": [], "disclaimer": _DISCLAIMER}
            if D < 0 or eco < 0:
                return {"error": "Distance and fuel economy cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}
            L = D * eco / 100.0
            co2 = L * PETROL_KG_PER_L
            law = ("Burning one litre of petrol releases about " + _f(PETROL_KG_PER_L)
                   + " kg of CO\u2082. Driving "+ _f(D) +" km at " + _f(eco)
                   + " L/100km burns " + _f(L) + " litres.")
            law_name, law_url = PETROL_SOURCE_NAME, PETROL_SOURCE_URL
            steps = [
                {"label": "Litres used", "math": r"\(L = \dfrac{" + _f(D) + r" \times " + _f(eco) + r"}{100}\)",
                 "note": "Distance times economy per 100 km."},
                {"label": "CO2", "math": r"\(" + _f(L) + r" \times " + _f(PETROL_KG_PER_L) + r"\)",
                 "note": "Litres times the petrol factor."},
                {"label": "Result", "math": r"\(" + _f(co2) + r"\ \text{kg CO}_2\)", "note": "Carbon dioxide released."},
            ]
            result = _f(co2) + " kg CO\u2082 driving " + _f(D) + " km"
            factor_used = PETROL_KG_PER_L; factor_unit = "kg CO\u2082/L"

        else:
            return {"error": "Choose an activity: electricity, petrol or driving.", "steps": [], "disclaimer": _DISCLAIMER}
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": result,
        "activity": act, "country": country_name,
        "co2_kg": co2, "factor_used": factor_used, "factor_unit": factor_unit,
        "grid_factor": g,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": law, "law_source_name": law_name, "law_source_url": law_url,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
