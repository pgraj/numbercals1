"""Customer Retention Impact — business-finance > Impact Metrics.
How improving the retention rate grows the retained customer base and its revenue."""
from core.registry import register

@register(
    slug="customer-retention-impact",
    name="Customer Retention Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["retention", "customers", "revenue", "impact", "loyalty"],
    formula="retained = customers \u00d7 retention% ; revenue = retained \u00d7 value",
    summary="See how a higher retention rate keeps more customers and how much extra annual revenue that protects.",
    viz_template="viz/customer-retention-impact.html",
)
def compute(customers: float = 1000, current_retention_percent: float = 80,
            new_retention_percent: float = 88, annual_value: float = 500):
    try:
        N = float(customers); r0 = float(current_retention_percent)
        r1 = float(new_retention_percent); val = float(annual_value)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if N < 0 or val < 0:
        return {"error": "Customers and value cannot be negative."}
    if not (0 <= r0 <= 100 and 0 <= r1 <= 100):
        return {"error": "Retention rates must be between 0 and 100."}
    kept0 = N * r0 / 100.0
    kept1 = N * r1 / 100.0
    extra = kept1 - kept0
    d_rev = extra * val
    steps = [
        {"label": "Kept now", "math": r"\(" + ("%.0f" % N) + r" \times " + ("%.4g" % r0) + r"\% = " + ("%.1f" % kept0) + r"\)", "note": "Customers retained at the current rate."},
        {"label": "Kept after", "math": r"\(" + ("%.0f" % N) + r" \times " + ("%.4g" % r1) + r"\% = " + ("%.1f" % kept1) + r"\)", "note": "At the improved rate."},
        {"label": "Revenue protected", "math": r"\(" + ("%.1f" % extra) + r" \times " + ("%.2f" % val) + r" = " + ("%.2f" % d_rev) + r"\)", "note": "Extra customers kept, times their yearly value."},
    ]
    return {
        "result": (("+" if extra >= 0 else "") + ("%.1f" % extra) + " customers kept, "
                   + ("+" if d_rev >= 0 else "") + ("%.2f" % d_rev) + " revenue protected"),
        "kept_before": round(kept0, 1), "kept_after": round(kept1, 1),
        "extra_kept": round(extra, 1), "revenue_delta": round(d_rev, 2), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
