"""Mortgage Stress Test — real-estate > Advanced.
Re-computes the repayment at a stressed (higher) interest rate and checks it against
an affordability limit (share of income). Standard lender-style buffer test."""
from core.registry import register

@register(
    slug="mortgage-stress-test",
    name="Mortgage Stress Test Calculator",
    section="real-estate",
    sub="Advanced",
    tags=["real estate", "mortgage", "stress test", "buffer", "affordability", "interest rate"],
    formula="stressed rate = current + buffer ; check stressed repayment vs income limit",
    summary="Lender-style stress test \u2014 recomputes the monthly repayment at a higher buffered rate and checks whether it still fits within a chosen share of your income.",
    viz_template="viz/mortgage-stress-test.html",
)
def compute(loan_amount: float = 480000, current_rate_percent: float = 6.0,
            buffer_percent: float = 3.0, term_years: float = 30,
            monthly_income: float = 9000, max_repayment_share_percent: float = 35):
    try:
        P = float(loan_amount); rate = float(current_rate_percent); buf = float(buffer_percent)
        term = float(term_years); income = float(monthly_income); share = float(max_repayment_share_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if P < 0 or term <= 0 or income <= 0:
        return {"error": "Loan, term and income must be valid positive numbers."}
    if buf < 0 or rate < 0:
        return {"error": "Rates cannot be negative."}
    if not (0 < share <= 100):
        return {"error": "Repayment share must be between 0 and 100."}

    def monthly_payment(principal, annual_rate_pct, years):
        r = annual_rate_pct / 100.0 / 12.0
        n = years * 12
        if r == 0:
            return principal / n
        return principal * r * (1 + r) ** n / ((1 + r) ** n - 1)

    stressed_rate = rate + buf
    pay_now = monthly_payment(P, rate, term)
    pay_stress = monthly_payment(P, stressed_rate, term)
    limit = income * share / 100.0
    passes = pay_stress <= limit
    steps = [
        {"label": "Stressed rate", "math": r"\(" + ("%g" % rate) + r"\% + " + ("%g" % buf) + r"\% = " + ("%.2f" % stressed_rate) + r"\%\)", "note": "Adds a safety buffer to today's rate."},
        {"label": "Stressed repayment", "math": r"\(" + ("%.0f" % pay_stress) + r"\text{/mo (vs }" + ("%.0f" % pay_now) + r"\text{ now)}\)", "note": "Repayment if rates climbed that far."},
        {"label": "Affordability", "math": r"\(" + ("%.0f" % pay_stress) + r" \;" + (r"\le" if passes else r">") + r"\; " + ("%.0f" % limit) + r"\)", "note": ("Within your " + ("%g" % share) + "% income limit \u2014 passes." if passes else "Exceeds your " + ("%g" % share) + "% income limit \u2014 fails.")},
    ]
    return {
        "result": (("PASS" if passes else "FAIL") + " \u2014 stressed repayment " + ("%.0f" % pay_stress)
                   + "/mo vs limit " + ("%.0f" % limit) + "/mo"),
        "payment_now": round(pay_now, 0), "payment_stressed": round(pay_stress, 0),
        "income_limit": round(limit, 0), "passes": passes, "stressed_rate_percent": round(stressed_rate, 2),
        "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
