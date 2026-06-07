"""Interest Rate Change Impact — business-finance > Impact Metrics.
How a change in interest rate moves the periodic interest cost on a balance (e.g. a loan)."""
from core.registry import register

@register(
    slug="interest-rate-change-impact",
    name="Interest Rate Change Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["interest rate", "loan", "repayment", "impact", "borrowing"],
    formula="annual interest = balance \u00d7 rate ; compare old vs new rate",
    summary="See how a change in interest rate (e.g. a central-bank move) changes the yearly interest on a loan or balance.",
    viz_template="viz/interest-rate-change-impact.html",
)
def compute(balance: float = 300000, current_rate_percent: float = 5.0, new_rate_percent: float = 6.5):
    try:
        B = float(balance); r0 = float(current_rate_percent); r1 = float(new_rate_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if B < 0:
        return {"error": "Balance cannot be negative."}
    i0 = B * r0 / 100.0
    i1 = B * r1 / 100.0
    delta = i1 - i0
    monthly_delta = delta / 12.0
    steps = [
        {"label": "Interest now", "math": r"\(" + ("%.0f" % B) + r" \times " + ("%.4g" % r0) + r"\% = " + ("%.2f" % i0) + r"\)", "note": "Yearly interest at the current rate."},
        {"label": "Interest after", "math": r"\(" + ("%.0f" % B) + r" \times " + ("%.4g" % r1) + r"\% = " + ("%.2f" % i1) + r"\)", "note": "At the new rate."},
        {"label": "Change", "math": r"\(" + ("+" if delta >= 0 else "") + ("%.2f" % delta) + r"\text{/yr } (" + ("%.2f" % monthly_delta) + r"\text{/mo})\)", "note": ("Costs more." if delta >= 0 else "Costs less.")},
    ]
    return {
        "result": ("Yearly interest " + ("rises" if delta >= 0 else "falls") + " by " + ("%.2f" % abs(delta))
                   + "  (" + ("%.2f" % abs(monthly_delta)) + "/month)"),
        "interest_before": round(i0, 2), "interest_after": round(i1, 2),
        "annual_delta": round(delta, 2), "monthly_delta": round(monthly_delta, 2), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
