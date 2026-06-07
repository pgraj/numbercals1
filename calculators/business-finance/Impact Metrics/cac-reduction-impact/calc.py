"""CAC Reduction Impact — business-finance > Impact Metrics.
How lowering customer acquisition cost frees up budget or buys more customers."""
from core.registry import register

@register(
    slug="cac-reduction-impact",
    name="CAC Reduction Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["cac", "acquisition cost", "marketing", "impact", "saas", "efficiency"],
    formula="customers = budget / CAC ; savings = customers \u00d7 (old CAC \u2212 new CAC)",
    summary="See how cutting customer acquisition cost either saves budget for the same customers or wins more for the same spend.",
    viz_template="viz/cac-reduction-impact.html",
)
def compute(budget: float = 100000, current_cac: float = 200, new_cac: float = 150):
    try:
        B = float(budget); c0 = float(current_cac); c1 = float(new_cac)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if B < 0:
        return {"error": "Budget cannot be negative."}
    if c0 <= 0 or c1 <= 0:
        return {"error": "CAC must be greater than zero."}
    cust0 = B / c0
    cust1 = B / c1
    extra_customers = cust1 - cust0
    savings_same_customers = cust0 * (c0 - c1)
    steps = [
        {"label": "Customers now", "math": r"\(" + ("%.0f" % B) + r" / " + ("%.2f" % c0) + r" = " + ("%.1f" % cust0) + r"\)", "note": "What the budget buys at the current CAC."},
        {"label": "Customers after", "math": r"\(" + ("%.0f" % B) + r" / " + ("%.2f" % c1) + r" = " + ("%.1f" % cust1) + r"\)", "note": "Same budget, lower CAC."},
        {"label": "Two ways to win", "math": r"\(+" + ("%.1f" % extra_customers) + r"\text{ customers, or save }" + ("%.0f" % savings_same_customers) + r"\)", "note": "More customers for the same spend, OR keep customers flat and bank the saving."},
    ]
    return {
        "result": ("+" + ("%.1f" % extra_customers) + " customers for the same budget (or save "
                   + ("%.0f" % savings_same_customers) + " at the same customer count)"),
        "customers_before": round(cust0, 1), "customers_after": round(cust1, 1),
        "extra_customers": round(extra_customers, 1), "savings": round(savings_same_customers, 2), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
