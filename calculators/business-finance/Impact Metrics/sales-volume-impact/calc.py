"""Sales Volume Impact — business-finance > Impact Metrics.
Effect on units sold of a percentage change in sales volume."""
from core.registry import register

@register(
    slug="sales-volume-impact",
    name="Sales Volume Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["sales", "volume", "units", "impact", "percentage change"],
    formula="new volume = current × (1 + change%/100)",
    summary="See how a percentage change in sales volume moves the unit count and the size of the swing.",
    viz_template="viz/sales-volume-impact.html",
)
def compute(current_units: float = 10000, change_percent: float = 8):
    try:
        base = float(current_units); pct = float(change_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if base < 0:
        return {"error": "Value cannot be negative."}
    new = base * (1 + pct / 100.0)
    delta = new - base
    steps = [
        {"label": "Apply change", "math": r"\(\text{new} = " + ("%.4g" % base) + r" \times (1 + " + ("%.4g" % pct) + r"/100)\)", "note": "Grow or shrink by the percentage."},
        {"label": "New value", "math": r"\(" + ("%.4g" % new) + r"\)", "note": "Volume after the change."},
        {"label": "Difference", "math": r"\(" + ("%.4g" % delta) + r"\)", "note": ("Increase." if delta >= 0 else "Decrease.")},
    ]
    return {
        "result": ("Volume " + ("rises" if delta >= 0 else "falls") + " to " + ("%.4g" % new) + "  (" + ("+" if delta >= 0 else "") + ("%.4g" % delta) + ")"),
        "new_value": round(new, 4), "delta": round(delta, 4), "change_percent": pct,
        "base": round(base, 4), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
