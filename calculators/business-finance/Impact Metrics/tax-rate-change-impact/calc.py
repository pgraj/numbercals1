"""Tax Rate Change Impact — business-finance > Impact Metrics.
How a change in tax rate changes tax owed and take-home on a given income/profit."""
from core.registry import register

@register(
    slug="tax-rate-change-impact",
    name="Tax Rate Change Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["tax", "rate", "take-home", "net income", "impact"],
    formula="tax = income \u00d7 rate ; net = income \u2212 tax (flat-rate estimate)",
    summary="See how a change in a flat tax rate changes the tax owed and what you keep, on a given income or profit.",
    viz_template="viz/tax-rate-change-impact.html",
)
def compute(income: float = 80000, current_rate_percent: float = 30, new_rate_percent: float = 33):
    try:
        I = float(income); r0 = float(current_rate_percent); r1 = float(new_rate_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if I < 0:
        return {"error": "Income cannot be negative."}
    if not (0 <= r0 <= 100 and 0 <= r1 <= 100):
        return {"error": "Tax rates must be between 0 and 100."}
    tax0 = I * r0 / 100.0
    tax1 = I * r1 / 100.0
    net0 = I - tax0
    net1 = I - tax1
    d_tax = tax1 - tax0
    steps = [
        {"label": "Tax now", "math": r"\(" + ("%.0f" % I) + r" \times " + ("%.4g" % r0) + r"\% = " + ("%.2f" % tax0) + r"\)", "note": "At the current flat rate."},
        {"label": "Tax after", "math": r"\(" + ("%.0f" % I) + r" \times " + ("%.4g" % r1) + r"\% = " + ("%.2f" % tax1) + r"\)", "note": "At the new rate."},
        {"label": "Take-home change", "math": r"\(" + ("%.2f" % net0) + r" \to " + ("%.2f" % net1) + r"\)", "note": ("You keep less." if d_tax >= 0 else "You keep more.")},
    ]
    return {
        "result": ("Tax " + ("+" if d_tax >= 0 else "") + ("%.2f" % d_tax) + ", take-home "
                   + ("%.2f" % net0) + " \u2192 " + ("%.2f" % net1)),
        "tax_before": round(tax0, 2), "tax_after": round(tax1, 2),
        "net_before": round(net0, 2), "net_after": round(net1, 2), "tax_delta": round(d_tax, 2),
        "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
