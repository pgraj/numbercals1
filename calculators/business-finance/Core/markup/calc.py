"""Markup — business-finance > Core. Selling price and margin from cost and markup%."""
from core.registry import register

@register(
    slug="markup",
    name="Markup Calculator",
    section="business-finance",
    sub="Core",
    tags=["markup", "cost", "price", "margin", "pricing"],
    formula="price = cost \u00d7 (1 + markup%/100) ; margin% = profit / price",
    summary="Find the selling price from a cost and a markup percentage, and see the resulting profit margin.",
    viz_template="viz/markup.html",
)
def compute(cost: float = 60, markup_percent: float = 50):
    try:
        C = float(cost); mu = float(markup_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if C < 0:
        return {"error": "Cost cannot be negative."}
    price = C * (1 + mu / 100.0)
    profit = price - C
    margin = (profit / price * 100) if price != 0 else 0.0
    steps = [
        {"label": "Apply markup", "math": r"\(" + ("%.2f" % C) + r" \times (1 + " + ("%.4g" % mu) + r"/100) = " + ("%.2f" % price) + r"\)", "note": "Markup is added on top of cost."},
        {"label": "Profit", "math": r"\(" + ("%.2f" % price) + r" - " + ("%.2f" % C) + r" = " + ("%.2f" % profit) + r"\)", "note": "Price minus cost."},
        {"label": "Margin", "math": r"\(" + ("%.2f" % profit) + r" / " + ("%.2f" % price) + r" = " + ("%.2f" % margin) + r"\%\)", "note": "Markup and margin differ \u2014 margin is profit over PRICE, not cost."},
    ]
    return {
        "result": "Sell at " + ("%.2f" % price) + "  (profit " + ("%.2f" % profit) + ", margin " + ("%.1f" % margin) + "%)",
        "price": round(price, 2), "profit": round(profit, 2), "margin_percent": round(margin, 2),
        "cost": round(C, 2), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
