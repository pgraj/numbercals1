"""Price Change Impact — business-finance > Impact Metrics.
Uses price elasticity of demand to estimate how a price change moves units and revenue."""
from core.registry import register

@register(
    slug="price-change-impact",
    name="Price Change Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["price", "elasticity", "demand", "revenue", "impact"],
    formula="%\u0394 quantity = elasticity \u00d7 %\u0394 price ; revenue = price \u00d7 quantity",
    summary="Estimate how a price change affects units sold and total revenue, using price elasticity of demand.",
    viz_template="viz/price-change-impact.html",
)
def compute(current_price: float = 20, current_units: float = 1000,
            price_change_percent: float = 10, elasticity: float = -1.2):
    try:
        P = float(current_price); Q = float(current_units)
        dp = float(price_change_percent); e = float(elasticity)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if P < 0 or Q < 0:
        return {"error": "Price and units cannot be negative."}
    dq = e * dp  # percentage change in quantity
    newP = P * (1 + dp / 100.0)
    newQ = Q * (1 + dq / 100.0)
    if newQ < 0:
        newQ = 0.0
    old_rev = P * Q
    new_rev = newP * newQ
    delta = new_rev - old_rev
    steps = [
        {"label": "Demand response", "math": r"\(\%\Delta Q = " + ("%.4g" % e) + r" \times " + ("%.4g" % dp) + r"\% = " + ("%.4g" % dq) + r"\%\)", "note": "Elasticity links price and demand."},
        {"label": "New price & units", "math": r"\(" + ("%.2f" % newP) + r" \times " + ("%.0f" % newQ) + r"\)", "note": "After the price move."},
        {"label": "Revenue", "math": r"\(" + ("%.2f" % old_rev) + r" \to " + ("%.2f" % new_rev) + r"\)", "note": ("Revenue rises." if delta >= 0 else "Revenue falls \u2014 demand dropped more than price gained.")},
    ]
    return {
        "result": ("Revenue " + ("rises" if delta >= 0 else "falls") + " to " + ("%.2f" % new_rev)
                   + "  (" + ("+" if delta >= 0 else "") + ("%.2f" % delta) + ")"),
        "old_revenue": round(old_rev, 2), "new_revenue": round(new_rev, 2), "delta": round(delta, 2),
        "new_units": round(newQ, 1), "quantity_change_percent": round(dq, 2), "elasticity": e, "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
