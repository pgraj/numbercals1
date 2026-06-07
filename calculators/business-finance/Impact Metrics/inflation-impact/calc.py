"""Inflation Impact — business-finance > Impact Metrics.
Erosion of purchasing power and future nominal price over N years at a given inflation rate."""
from core.registry import register

@register(
    slug="inflation-impact",
    name="Inflation Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["inflation", "purchasing power", "real value", "impact", "money"],
    formula="future price = amount \u00d7 (1 + rate)^years ; real value = amount / (1 + rate)^years",
    summary="See how inflation raises future prices and erodes the real value of money held over time.",
    viz_template="viz/inflation-impact.html",
)
def compute(amount: float = 1000, inflation_rate_percent: float = 6, years: float = 10):
    try:
        A = float(amount); r = float(inflation_rate_percent); y = float(years)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if A < 0 or y < 0:
        return {"error": "Amount and years cannot be negative."}
    factor = (1 + r / 100.0) ** y
    future_price = A * factor
    real_value = A / factor if factor != 0 else None
    lost = A - real_value if real_value is not None else None
    steps = [
        {"label": "Growth factor", "math": r"\((1 + " + ("%.4g" % (r/100)) + r")^{" + ("%.4g" % y) + r"} = " + ("%.4f" % factor) + r"\)", "note": "Compounded over the years."},
        {"label": "Future price", "math": r"\(" + ("%.2f" % A) + r" \times " + ("%.4f" % factor) + r" = " + ("%.2f" % future_price) + r"\)", "note": "What costs " + ("%.0f" % A) + " today will cost then."},
        {"label": "Real value kept", "math": r"\(" + ("%.2f" % A) + r" / " + ("%.4f" % factor) + r" = " + ("%.2f" % real_value) + r"\)", "note": "Today's money is worth this much in future terms."},
    ]
    return {
        "result": ("In " + ("%.4g" % y) + " yr: a price of " + ("%.0f" % A) + " becomes " + ("%.2f" % future_price)
                   + "; today's " + ("%.0f" % A) + " is worth " + ("%.2f" % real_value)),
        "future_price": round(future_price, 2), "real_value": round(real_value, 2),
        "purchasing_power_lost": round(lost, 2), "factor": round(factor, 4), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
