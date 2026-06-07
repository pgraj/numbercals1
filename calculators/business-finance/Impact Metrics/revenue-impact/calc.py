"""Revenue Impact — business-finance > Impact Metrics.
Shows the effect on revenue of a percentage change, with before/after and delta."""
from core.registry import register

@register(
    slug="revenue-impact",
    name="Revenue Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["revenue", "impact", "growth", "percentage change", "business"],
    formula="new revenue = current \u00d7 (1 + change%/100)",
    summary="See how a percentage change in revenue moves the absolute figure, and the size of the gain or loss.",
    viz_template="viz/revenue-impact.html",
)
def compute(current_revenue: float = 100000, change_percent: float = 12):
    try:
        cur = float(current_revenue); pct = float(change_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if cur < 0:
        return {"error": "Current revenue cannot be negative."}
    new = cur * (1 + pct / 100.0)
    delta = new - cur
    steps = [
        {"label": "Apply change", "math": r"\(\text{new} = " + ("%.2f" % cur) + r" \times (1 + " + ("%.4g" % pct) + r"/100)\)", "note": "Grow or shrink by the percentage."},
        {"label": "New revenue", "math": r"\(" + ("%.2f" % new) + r"\)", "note": "Revenue after the change."},
        {"label": "Difference", "math": r"\(" + ("%.2f" % delta) + r"\)", "note": ("Gain." if delta >= 0 else "Loss.")},
    ]
    return {
        "result": ("Revenue " + ("rises" if delta >= 0 else "falls") + " to " + ("%.2f" % new)
                   + "  (" + ("+" if delta >= 0 else "") + ("%.2f" % delta) + ")"),
        "new_revenue": round(new, 2), "delta": round(delta, 2), "change_percent": pct,
        "current_revenue": round(cur, 2), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
