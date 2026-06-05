"""Amortization — accounting › Loans & Debt.
Stacked area over the term: interest portion falling, principal portion rising.
Steps included: deriving the monthly payment then the first row split."""
from core.registry import register


@register(
    slug="amortization",
    name="Amortization Calculator",
    section="accounting",
    sub="Loans & Debt",
    tags=["amortization", "loan", "schedule", "principal", "interest"],
    formula="EMI = P·r(1+r)^n/((1+r)^n−1);  interestₘ = balance·r",
    summary="Amortisation schedule showing how each payment splits between interest and principal.",
    viz_template="viz/amortization.html",
)
def compute(amount: float, rate_pct: float, years: float):
    P = float(amount)
    annual = float(rate_pct)
    yrs = float(years)
    if P <= 0 or yrs <= 0 or annual < 0:
        return {"error": "Loan amount and term must be positive.", "steps": []}

    r = annual / 12 / 100
    n = int(round(yrs * 12))
    if r == 0:
        emi = P / n
    else:
        factor = (1 + r) ** n
        emi = P * r * factor / (factor - 1)

    # Build the monthly schedule, then aggregate per year for the chart.
    balance = P
    yearly = {}
    total_interest = 0.0
    first_interest = balance * r
    first_principal = emi - first_interest
    for m in range(1, n + 1):
        interest = balance * r
        principal = emi - interest
        balance = max(balance - principal, 0)
        total_interest += interest
        yr = (m - 1) // 12 + 1
        agg = yearly.setdefault(yr, {"interest": 0.0, "principal": 0.0})
        agg["interest"] += interest
        agg["principal"] += principal

    series = []
    for yr in sorted(yearly):
        series.append({
            "year": yr,
            "interest": round(yearly[yr]["interest"], 2),
            "principal": round(yearly[yr]["principal"], 2),
        })

    total_payment = emi * n

    steps = [
        {"label": "Monthly rate and number of payments",
         "math": r"\( r = \dfrac{%g}{1200} = %.6g,\quad n = %g \times 12 = %d \)"
                 % (annual, r, yrs, n)},
        {"label": "Work out the fixed monthly payment (EMI)",
         "math": r"\( EMI = \dfrac{P\,r(1+r)^n}{(1+r)^n-1} = %.2f \)" % emi},
        {"label": "Month 1 — interest is charged on the full balance",
         "math": r"\( \text{interest}_1 = P\,r = %g \times %.6g = %.2f \)"
                 % (P, r, first_interest)},
        {"label": "Month 1 — the rest of the payment reduces the principal",
         "math": r"\( \text{principal}_1 = EMI - \text{interest}_1 = %.2f - %.2f = %.2f \)"
                 % (emi, first_interest, first_principal),
         "note": "As the balance falls, later months charge less interest and repay more principal."},
        {"label": "Total interest over the life of the loan",
         "math": r"\( \text{total interest} = %.2f \)" % total_interest},
    ]
    return {
        "emi": round(emi, 2),
        "total_interest": round(total_interest, 2),
        "total_payment": round(total_payment, 2),
        "series": series,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
