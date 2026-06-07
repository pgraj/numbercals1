"""Household Carbon Reduction: compare a 'before' and 'after' electricity use
(kWh per period) and show the CO2 saved, scaled to a year."""
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

_PERIODS = {"day": 365.0, "week": 52.0, "month": 12.0, "year": 1.0}

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.2f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "Before and after",
     "body": "Enter how much electricity you used before a change (say, before switching to "
             "LED bulbs or a heat pump) and how much after. The drop in kWh, turned into "
             "CO\u2082 with your country's grid factor, is your saving."},
    {"heading": "Scaled to a year",
     "body": "A small daily or weekly saving adds up. The calculator multiplies your "
             "per-period saving by how many periods fit in a year, so you can see the full "
             "annual impact of a change you make once."},
    {"heading": "Country still matters",
     "body": "The same kWh saved avoids more CO\u2082 on a coal-heavy grid than on a clean "
             "one. The saving is calculated with the grid factor for the country you pick."},
]

@register(
    slug="household-carbon-reduction",
    name="Household Carbon Reduction",
    section="environment",
    topic="Carbon & Emissions",
    sub="Footprint",
    order=1,
    summary="Compare before/after electricity use and see the CO2 saved per year, using your country's grid factor.",
    formula="saved = (before \u2212 after) \u00d7 grid factor \u00d7 periods/year",
    tags=["carbon", "reduction", "saving", "household", "electricity", "co2"],
    viz_template="viz/household-carbon-reduction.html",
    related=["energy-usage-impact", "carbon-emission-impact", "ev-savings-impact"],
)
def compute(country="IN", before_kwh=300.0, after_kwh=220.0, period="month", **_ignored):
    def num(v):
        if v is None or v == "":
            return None
        return float(v)
    try:
        b = num(before_kwh); a = num(after_kwh)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}
    if b is None or a is None:
        return {"error": "Enter both the before and after electricity use (kWh).", "steps": [], "disclaimer": _DISCLAIMER}
    if b < 0 or a < 0:
        return {"error": "Electricity use cannot be negative.", "steps": [], "disclaimer": _DISCLAIMER}

    p = str(period or "month").strip().lower()
    per_year = _PERIODS.get(p, 12.0)
    g, country_name = grid_factor(country)

    diff = b - a
    saved_period = diff * g / 1000.0
    saved_year = saved_period * per_year

    if diff > 0:
        headline = (_f(saved_year) + " kg CO\u2082e saved per year ("
                    + _f(saved_period) + " kg per " + p + ")")
    elif diff < 0:
        headline = (_f(abs(saved_year)) + " kg CO\u2082e MORE per year \u2014 the 'after' "
                    "use is higher than 'before'")
    else:
        headline = "No change \u2014 before and after use are equal"

    steps = [
        {"label": "Change per " + p, "math": r"\(" + _f(b) + r" - " + _f(a) + r" = " + _f(diff) + r"\ \text{kWh}\)",
         "note": "Electricity saved each " + p + "."},
        {"label": "To CO2", "math": r"\(" + _f(diff) + r" \times " + _f(g) + r"\ \text{g/kWh}\)",
         "note": "Using the grid factor for " + country_name + "."},
        {"label": "Per year", "math": r"\(" + _f(saved_period) + r" \times " + _f(per_year) + r"\)",
         "note": "Scaled by the number of " + p + "s in a year."},
    ]

    law = ("A saved kilowatt-hour avoids the CO\u2082 it would have caused. The grid factor "
           "for " + country_name + " is " + _f(g) + " g CO\u2082e per kWh (lifecycle).")
    return {
        "result": headline, "country": country_name,
        "saved_year_kg": saved_year, "saved_period_kg": saved_period,
        "diff_kwh": diff, "grid_factor": g, "period": p,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": law, "law_source_name": GRID_SOURCE_NAME, "law_source_url": GRID_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
