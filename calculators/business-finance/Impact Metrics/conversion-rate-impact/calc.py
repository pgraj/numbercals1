"""Conversion Rate Impact — business-finance > Impact Metrics.
How extra conversions and revenue follow from a change in conversion rate."""
from core.registry import register

@register(
    slug="conversion-rate-impact",
    name="Conversion Rate Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["conversion", "rate", "cro", "revenue", "impact"],
    formula="conversions = visitors \u00d7 rate ; revenue = conversions \u00d7 value",
    summary="See how lifting your conversion rate turns the same traffic into more customers and revenue.",
    viz_template="viz/conversion-rate-impact.html",
)
def compute(visitors: float = 10000, current_rate_percent: float = 2.0,
            new_rate_percent: float = 2.5, value_per_conversion: float = 50):
    try:
        V = float(visitors); r0 = float(current_rate_percent)
        r1 = float(new_rate_percent); val = float(value_per_conversion)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if V < 0 or val < 0:
        return {"error": "Visitors and value cannot be negative."}
    if r0 < 0 or r1 < 0:
        return {"error": "Conversion rates cannot be negative."}
    c0 = V * r0 / 100.0
    c1 = V * r1 / 100.0
    extra = c1 - c0
    rev0 = c0 * val
    rev1 = c1 * val
    delta_rev = rev1 - rev0
    steps = [
        {"label": "Conversions now", "math": r"\(" + ("%.0f" % V) + r" \times " + ("%.4g" % r0) + r"\% = " + ("%.1f" % c0) + r"\)", "note": "Customers at the current rate."},
        {"label": "Conversions after", "math": r"\(" + ("%.0f" % V) + r" \times " + ("%.4g" % r1) + r"\% = " + ("%.1f" % c1) + r"\)", "note": "Customers at the new rate."},
        {"label": "Extra revenue", "math": r"\(" + ("%.1f" % extra) + r" \times " + ("%.2f" % val) + r" = " + ("%.2f" % delta_rev) + r"\)", "note": "Same traffic, more value."},
    ]
    return {
        "result": (("+" if extra >= 0 else "") + ("%.1f" % extra) + " conversions, "
                   + ("+" if delta_rev >= 0 else "") + ("%.2f" % delta_rev) + " revenue"),
        "conversions_before": round(c0, 1), "conversions_after": round(c1, 1),
        "extra_conversions": round(extra, 1), "revenue_delta": round(delta_rev, 2), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
