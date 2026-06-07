"""Profit Impact — business-finance > Impact Metrics.
How profit changes when revenue and/or costs change by given percentages."""
from core.registry import register

@register(
    slug="profit-impact",
    name="Profit Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["profit", "impact", "revenue", "cost", "margin"],
    formula="new profit = revenue\u00d7(1+r%) \u2212 cost\u00d7(1+c%)",
    summary="See how profit moves when revenue and costs each change by a percentage \u2014 the leverage effect on the bottom line.",
    viz_template="viz/profit-impact.html",
)
def compute(revenue: float = 100000, cost: float = 70000,
            revenue_change_percent: float = 10, cost_change_percent: float = 5):
    try:
        R = float(revenue); C = float(cost)
        rp = float(revenue_change_percent); cp = float(cost_change_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if R < 0 or C < 0:
        return {"error": "Revenue and cost cannot be negative."}
    old_profit = R - C
    newR = R * (1 + rp / 100.0)
    newC = C * (1 + cp / 100.0)
    new_profit = newR - newC
    delta = new_profit - old_profit
    steps = [
        {"label": "Old profit", "math": r"\(" + ("%.2f" % R) + r" - " + ("%.2f" % C) + r" = " + ("%.2f" % old_profit) + r"\)", "note": "Revenue minus cost now."},
        {"label": "New revenue & cost", "math": r"\(" + ("%.2f" % newR) + r" - " + ("%.2f" % newC) + r"\)", "note": "After each percentage change."},
        {"label": "New profit", "math": r"\(" + ("%.2f" % new_profit) + r"\)", "note": ("Profit up " if delta >= 0 else "Profit down ") + "by " + ("%.2f" % abs(delta)) + "."},
    ]
    pct_change = (delta / old_profit * 100) if old_profit != 0 else None
    return {
        "result": ("Profit moves from " + ("%.2f" % old_profit) + " to " + ("%.2f" % new_profit)
                   + "  (" + ("+" if delta >= 0 else "") + ("%.2f" % delta) + ")"),
        "old_profit": round(old_profit, 2), "new_profit": round(new_profit, 2),
        "delta": round(delta, 2), "profit_change_percent": (round(pct_change, 2) if pct_change is not None else None),
        "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
