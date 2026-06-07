"""GDP Growth Impact — business-finance > Impact Metrics.
Effect of a percentage growth rate on GDP."""
from core.registry import register

@register(
    slug="gdp-growth-impact",
    name="GDP Growth Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["gdp", "growth", "economy", "impact", "macroeconomics"],
    formula="new GDP = current × (1 + growth%/100)",
    summary="See projected GDP after a one-period growth rate and the absolute change.",
    viz_template="viz/gdp-growth-impact.html",
)
def compute(current_gdp: float = 2000, change_percent: float = 6):
    try:
        base = float(current_gdp); pct = float(change_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if base < 0:
        return {"error": "Value cannot be negative."}
    new = base * (1 + pct / 100.0)
    delta = new - base
    steps = [
        {"label": "Apply change", "math": r"\(\text{new} = " + ("%.4g" % base) + r" \times (1 + " + ("%.4g" % pct) + r"/100)\)", "note": "Grow or shrink by the percentage."},
        {"label": "New value", "math": r"\(" + ("%.4g" % new) + r"\)", "note": "GDP after the change."},
        {"label": "Difference", "math": r"\(" + ("%.4g" % delta) + r"\)", "note": ("Increase." if delta >= 0 else "Decrease.")},
    ]
    return {
        "result": ("GDP " + ("rises" if delta >= 0 else "falls") + " to " + ("%.4g" % new) + "  (" + ("+" if delta >= 0 else "") + ("%.4g" % delta) + ")"),
        "new_value": round(new, 4), "delta": round(delta, 4), "change_percent": pct,
        "base": round(base, 4), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
