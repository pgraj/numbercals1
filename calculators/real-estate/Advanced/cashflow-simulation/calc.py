"""Cashflow Simulation — real-estate > Advanced.
Monthly and annual pre-tax cashflow on a rental: rent less mortgage, costs and vacancy."""
from core.registry import register

@register(
    slug="cashflow-simulation",
    name="Cashflow Simulation Calculator",
    section="real-estate",
    sub="Advanced",
    tags=["real estate", "cashflow", "rental", "mortgage", "vacancy", "investment"],
    formula="annual cashflow = rent\u00d7(1\u2212vacancy) \u2212 mortgage \u2212 costs",
    summary="Project a rental property's yearly and monthly cashflow after the mortgage, running costs and an allowance for vacancy.",
    viz_template="viz/cashflow-simulation.html",
)
def compute(weekly_rent: float = 550, annual_mortgage_payments: float = 22000,
            annual_costs: float = 8000, vacancy_rate_percent: float = 4):
    try:
        rent_w = float(weekly_rent); mort = float(annual_mortgage_payments)
        costs = float(annual_costs); vac = float(vacancy_rate_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if rent_w < 0 or mort < 0 or costs < 0:
        return {"error": "Values cannot be negative."}
    if not (0 <= vac <= 100):
        return {"error": "Vacancy rate must be between 0 and 100."}
    gross_rent = rent_w * 52
    effective_rent = gross_rent * (1 - vac / 100.0)
    annual_cf = effective_rent - mort - costs
    monthly_cf = annual_cf / 12.0
    steps = [
        {"label": "Effective rent", "math": r"\(" + ("%.0f" % gross_rent) + r" \times (1 - " + ("%g" % vac) + r"\%) = " + ("%.0f" % effective_rent) + r"\)", "note": "Rent after the vacancy allowance."},
        {"label": "Annual cashflow", "math": r"\(" + ("%.0f" % effective_rent) + r" - " + ("%.0f" % mort) + r" - " + ("%.0f" % costs) + r" = " + ("%+.0f" % annual_cf) + r"\)", "note": ("Positive \u2014 the property pays its way." if annual_cf >= 0 else "Negative \u2014 it costs you to hold (negatively geared).")},
        {"label": "Per month", "math": r"\(" + ("%+.0f" % monthly_cf) + r"\)", "note": "Annual cashflow spread over 12 months."},
    ]
    return {
        "result": ("Cashflow " + ("%+.0f" % annual_cf) + "/yr  (" + ("%+.0f" % monthly_cf) + "/month)"),
        "annual_cashflow": round(annual_cf, 0), "monthly_cashflow": round(monthly_cf, 0),
        "effective_rent": round(effective_rent, 0), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
