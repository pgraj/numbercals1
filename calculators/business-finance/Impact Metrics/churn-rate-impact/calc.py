"""Churn Rate Impact — business-finance > Impact Metrics.
How a change in monthly churn changes customers lost and revenue lost per year."""
from core.registry import register

@register(
    slug="churn-rate-impact",
    name="Churn Rate Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["churn", "attrition", "customers", "revenue", "impact", "saas"],
    formula="annual lost \u2248 customers \u00d7 (1 \u2212 (1 \u2212 monthly churn)\u00b9\u00b2)",
    summary="See how reducing monthly churn cuts the customers and revenue you lose over a year.",
    viz_template="viz/churn-rate-impact.html",
)
def compute(customers: float = 1000, current_churn_percent: float = 5,
            new_churn_percent: float = 3, monthly_value: float = 40):
    try:
        N = float(customers); c0 = float(current_churn_percent)
        c1 = float(new_churn_percent); val = float(monthly_value)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if N < 0 or val < 0:
        return {"error": "Customers and value cannot be negative."}
    if not (0 <= c0 <= 100 and 0 <= c1 <= 100):
        return {"error": "Churn rates must be between 0 and 100."}
    # annual retained fraction = (1 - monthly churn)^12
    lost0 = N * (1 - (1 - c0 / 100.0) ** 12)
    lost1 = N * (1 - (1 - c1 / 100.0) ** 12)
    saved = lost0 - lost1
    rev_saved = saved * val * 12
    steps = [
        {"label": "Annual loss now", "math": r"\(" + ("%.0f" % N) + r"\,(1-(1-" + ("%.4g" % (c0/100)) + r")^{12}) = " + ("%.1f" % lost0) + r"\)", "note": "Customers lost over a year at the current churn."},
        {"label": "Annual loss after", "math": r"\(" + ("%.1f" % lost1) + r"\)", "note": "At the lower churn."},
        {"label": "Saved", "math": r"\(" + ("%.1f" % saved) + r"\text{ customers}, \approx " + ("%.0f" % rev_saved) + r"\text{ revenue}\)", "note": "Fewer customers lost, times yearly value."},
    ]
    return {
        "result": (("%.1f" % saved) + " fewer customers lost/yr, \u2248" + ("%.0f" % rev_saved) + " revenue saved"),
        "annual_lost_before": round(lost0, 1), "annual_lost_after": round(lost1, 1),
        "customers_saved": round(saved, 1), "revenue_saved": round(rev_saved, 2), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
