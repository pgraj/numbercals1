"""Break-Even (Property, Advanced) — real-estate > Advanced.
Years for cumulative rental cashflow plus capital growth to recover the cash invested."""
from core.registry import register

@register(
    slug="break-even-property-advanced",
    name="Break-Even Calculator (Property, Advanced)",
    section="real-estate",
    sub="Advanced",
    tags=["real estate", "break even", "payback", "property", "cashflow", "investment"],
    formula="years to break even \u2248 cash invested / (annual cashflow + annual capital growth)",
    summary="How long until a property investment recovers the cash you put in, counting both annual rental cashflow and estimated capital growth.",
    viz_template="viz/break-even-property-advanced.html",
)
def compute(cash_invested: float = 150000, annual_cashflow: float = 4000,
            annual_capital_growth: float = 24000):
    try:
        invested = float(cash_invested); cf = float(annual_cashflow); growth = float(annual_capital_growth)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if invested < 0:
        return {"error": "Cash invested cannot be negative."}
    annual_return = cf + growth
    if annual_return <= 0:
        return {"error": "Annual cashflow plus growth must be positive to break even."}
    years = invested / annual_return
    steps = [
        {"label": "Annual return", "math": r"\(" + ("%.0f" % cf) + r" + " + ("%.0f" % growth) + r" = " + ("%.0f" % annual_return) + r"\)", "note": "Cashflow plus capital growth each year."},
        {"label": "Years to break even", "math": r"\(" + ("%.0f" % invested) + r" / " + ("%.0f" % annual_return) + r" = " + ("%.1f" % years) + r"\)", "note": "Straight-line estimate (growth assumed steady)."},
    ]
    return {
        "result": ("\u2248 " + ("%.1f" % years) + " years to recover the cash invested"),
        "years_to_break_even": round(years, 1), "annual_return": round(annual_return, 0), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
