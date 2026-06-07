"""Property ROI (Advanced) — real-estate > Advanced.
Cash-on-cash return and total ROI including annual cashflow and capital growth,
measured against the actual cash invested (deposit + costs)."""
from core.registry import register

@register(
    slug="property-roi-advanced",
    name="Property ROI Calculator (Advanced)",
    section="real-estate",
    sub="Advanced",
    tags=["real estate", "roi", "cash on cash", "return", "leverage", "investment"],
    formula="cash-on-cash = annual cashflow / cash invested ; total ROI adds capital growth",
    summary="Advanced property ROI on the cash you actually put in \u2014 cash-on-cash return from rental cashflow, plus total return once capital growth is included.",
    viz_template="viz/property-roi-advanced.html",
)
def compute(deposit: float = 120000, purchase_costs: float = 30000,
            annual_cashflow: float = 4000, annual_capital_growth: float = 24000):
    try:
        dep = float(deposit); pc = float(purchase_costs)
        cf = float(annual_cashflow); growth = float(annual_capital_growth)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if dep < 0 or pc < 0:
        return {"error": "Deposit and costs cannot be negative."}
    invested = dep + pc
    if invested <= 0:
        return {"error": "Total cash invested must be greater than zero."}
    coc = cf / invested * 100
    total_roi = (cf + growth) / invested * 100
    steps = [
        {"label": "Cash invested", "math": r"\(" + ("%.0f" % dep) + r" + " + ("%.0f" % pc) + r" = " + ("%.0f" % invested) + r"\)", "note": "Deposit plus buying costs."},
        {"label": "Cash-on-cash", "math": r"\(" + ("%.0f" % cf) + r" / " + ("%.0f" % invested) + r" = " + ("%.2f" % coc) + r"\%\)", "note": "Yearly rental cashflow on cash in."},
        {"label": "Total ROI", "math": r"\((" + ("%.0f" % cf) + r" + " + ("%.0f" % growth) + r") / " + ("%.0f" % invested) + r" = " + ("%.2f" % total_roi) + r"\%\)", "note": "Adds capital growth \u2014 leverage amplifies this."},
    ]
    return {
        "result": ("Cash-on-cash " + ("%.2f" % coc) + "%, total ROI " + ("%.2f" % total_roi) + "%"),
        "cash_on_cash_percent": round(coc, 2), "total_roi_percent": round(total_roi, 2),
        "cash_invested": round(invested, 0), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
