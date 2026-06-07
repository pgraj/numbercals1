"""Pricing Strategy Impact Model — business-simulation > Models.
Profit-aware pricing: applies price elasticity to demand, then compares profit (not just
revenue) at the new price using a known unit cost. Helps find whether a price move pays."""
from core.registry import register

@register(
    slug="pricing-strategy-impact-model",
    name="Pricing Strategy Impact Model",
    section="business-simulation",
    sub="Models",
    tags=["pricing", "strategy", "elasticity", "profit", "margin", "simulation"],
    formula="%\u0394Q = elasticity \u00d7 %\u0394P ; profit = (price \u2212 unit cost) \u00d7 quantity",
    summary="Model a price change's effect on profit, not just revenue \u2014 elasticity drives the demand response and unit cost reveals whether the move actually grows profit.",
    viz_template="viz/pricing-strategy-impact-model.html",
)
def compute(current_price: float = 40, unit_cost: float = 25, current_units: float = 2000,
            price_change_percent: float = 10, elasticity: float = -1.3):
    try:
        P = float(current_price); cost = float(unit_cost); Q = float(current_units)
        dp = float(price_change_percent); e = float(elasticity)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if P < 0 or cost < 0 or Q < 0:
        return {"error": "Price, cost and units cannot be negative."}
    dq = e * dp
    newP = P * (1 + dp / 100.0)
    newQ = max(0.0, Q * (1 + dq / 100.0))
    profit0 = (P - cost) * Q
    profit1 = (newP - cost) * newQ
    delta = profit1 - profit0
    rev0 = P * Q
    rev1 = newP * newQ
    steps = [
        {"label": "Demand response", "math": r"\(\%\Delta Q = " + ("%.3g" % e) + r" \times " + ("%g" % dp) + r"\% = " + ("%.2f" % dq) + r"\%\)", "note": "Higher price usually means fewer units."},
        {"label": "New price & units", "math": r"\(" + ("%.2f" % newP) + r" \times " + ("%.0f" % newQ) + r"\)", "note": "After the change."},
        {"label": "Profit check", "math": r"\(" + ("%.0f" % profit0) + r" \to " + ("%.0f" % profit1) + r" (" + ("%+.0f" % delta) + r")\)", "note": ("Profit rises \u2014 the price move pays off." if delta >= 0 else "Profit falls \u2014 demand dropped too much.")},
    ]
    return {
        "result": ("Profit " + ("%.0f" % profit0) + " \u2192 " + ("%.0f" % profit1) + " (" + ("%+.0f" % delta)
                   + "); revenue " + ("%.0f" % rev0) + " \u2192 " + ("%.0f" % rev1)),
        "profit_before": round(profit0, 0), "profit_after": round(profit1, 0), "profit_delta": round(delta, 0),
        "revenue_before": round(rev0, 0), "revenue_after": round(rev1, 0),
        "new_units": round(newQ, 0), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
