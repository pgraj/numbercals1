"""Salary Increase Impact — business-finance > Impact Metrics.
Effect of a percentage pay rise on annual salary."""
from core.registry import register

@register(
    slug="salary-increase-impact",
    name="Salary Increase Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["salary", "pay rise", "increase", "income", "impact"],
    formula="new salary = current × (1 + rise%/100)",
    summary="See the new annual salary and the absolute gain from a percentage pay rise.",
    viz_template="viz/salary-increase-impact.html",
)
def compute(current_salary: float = 60000, change_percent: float = 5):
    try:
        base = float(current_salary); pct = float(change_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if base < 0:
        return {"error": "Value cannot be negative."}
    new = base * (1 + pct / 100.0)
    delta = new - base
    steps = [
        {"label": "Apply change", "math": r"\(\text{new} = " + ("%.4g" % base) + r" \times (1 + " + ("%.4g" % pct) + r"/100)\)", "note": "Grow or shrink by the percentage."},
        {"label": "New value", "math": r"\(" + ("%.4g" % new) + r"\)", "note": "Salary after the change."},
        {"label": "Difference", "math": r"\(" + ("%.4g" % delta) + r"\)", "note": ("Increase." if delta >= 0 else "Decrease.")},
    ]
    return {
        "result": ("Salary " + ("rises" if delta >= 0 else "falls") + " to " + ("%.4g" % new) + "  (" + ("+" if delta >= 0 else "") + ("%.4g" % delta) + ")"),
        "new_value": round(new, 4), "delta": round(delta, 4), "change_percent": pct,
        "base": round(base, 4), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
