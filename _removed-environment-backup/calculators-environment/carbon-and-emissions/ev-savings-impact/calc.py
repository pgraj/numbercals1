"""EV Savings Impact: compare a petrol car against an electric car over a year's
driving \u2014 petrol CO2 vs grid-charged CO2 \u2192 annual CO2 saving."""
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

# Petrol factor (see carbon-emission-impact for source)
PETROL_KG_PER_L = 2.31
PETROL_SOURCE_NAME = "US EPA \u2014 Greenhouse Gas Equivalencies (petrol)"
PETROL_SOURCE_URL = "https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator-calculations-and-references"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.2f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "Two cars, same distance",
     "body": "The calculator works out the CO\u2082 for driving the same yearly distance in "
             "a petrol car and in an electric car, then shows the difference. The petrol "
             "car burns fuel; the EV draws electricity from the grid."},
    {"heading": "Why the EV answer depends on country",
     "body": "An EV is only as clean as the electricity charging it. On a clean grid "
             "(France, Norway) an EV is dramatically lower-carbon than petrol. On a very "
             "coal-heavy grid the gap shrinks \u2014 and in extreme cases an efficient "
             "petrol car can even come close. That is why your country matters here."},
    {"heading": "What this leaves out",
     "body": "This compares only the energy used while driving (the 'tank-to-wheel' and "
             "charging emissions). It does not include the CO\u2082 of building either car "
             "or its battery, which is a one-off cost spread over the car's life."},
]

@register(
    slug="ev-savings-impact",
    name="EV Savings Impact",
    section="environment",
    topic="Carbon & Emissions",
    sub="Transport",
    order=2,
    summary="Compare a petrol car and an electric car over a year's driving and see the CO2 saved, using your country's grid factor.",
    formula="saving = petrol CO2 \u2212 EV charging CO2",
    tags=["ev", "electric vehicle", "petrol", "car", "carbon", "co2", "saving"],
    viz_template="viz/ev-savings-impact.html",
    related=["carbon-emission-impact", "household-carbon-reduction", "energy-usage-impact"],
)
def compute(country="IN", annual_km=15000.0,
            petrol_l_per_100km=8.0, ev_kwh_per_100km=18.0, **_ignored):
    def num(v):
        if v is None or v == "":
            return None
        return float(v)
    try:
        D = num(annual_km); pe = num(petrol_l_per_100km); ee = num(ev_kwh_per_100km)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}
    if D is None or pe is None or ee is None:
        return {"error": "Enter yearly distance, petrol economy (L/100km) and EV use (kWh/100km).",
                "steps": [], "disclaimer": _DISCLAIMER}
    if D < 0 or pe < 0 or ee < 0:
        return {"error": "Values cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}

    g, country_name = grid_factor(country)

    petrol_l = D * pe / 100.0
    petrol_co2 = petrol_l * PETROL_KG_PER_L
    ev_kwh = D * ee / 100.0
    ev_co2 = ev_kwh * g / 1000.0
    saving = petrol_co2 - ev_co2

    steps = [
        {"label": "Petrol CO2", "math": r"\(\dfrac{" + _f(D) + r" \times " + _f(pe) + r"}{100} \times " + _f(PETROL_KG_PER_L) + r"\)",
         "note": "Litres burned times the petrol factor = " + _f(petrol_co2) + " kg."},
        {"label": "EV CO2", "math": r"\(\dfrac{" + _f(D) + r" \times " + _f(ee) + r"}{100} \times " + _f(g) + r"\ \text{g/kWh}\)",
         "note": "kWh charged times " + country_name + " grid = " + _f(ev_co2) + " kg."},
        {"label": "Saving", "math": r"\(" + _f(petrol_co2) + r" - " + _f(ev_co2) + r" = " + _f(saving) + r"\ \text{kg}\)",
         "note": "Petrol CO2 minus EV CO2 over the year."},
    ]

    if saving > 0:
        headline = (_f(saving) + " kg CO\u2082 saved per year by the EV (in " + country_name + ")")
    elif saving < 0:
        headline = (_f(abs(saving)) + " kg CO\u2082 MORE per year for the EV on "
                    + country_name + "'s grid \u2014 a very carbon-heavy grid")
    else:
        headline = "The two cars emit the same over the year"

    law = ("An EV's driving emissions come from the grid: " + country_name + " is "
           + _f(g) + " g CO\u2082e/kWh. Petrol releases " + _f(PETROL_KG_PER_L)
           + " kg CO\u2082 per litre.")
    return {
        "result": headline, "country": country_name,
        "petrol_co2_kg": petrol_co2, "ev_co2_kg": ev_co2, "saving_kg": saving,
        "grid_factor": g,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": law, "law_source_name": GRID_SOURCE_NAME, "law_source_url": GRID_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
