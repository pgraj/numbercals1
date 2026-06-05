"""Loan EMI — accounting › Loans & Debt.
Donut: principal vs total interest. Steps show the EMI formula worked through."""
from core.registry import register


@register(
    slug="loan-emi",
    name="Loan EMI Calculator",
    section="accounting",
    sub="Loans & Debt",
    tags=["loan", "emi", "repayment", "interest"],
    formula="EMI = P·r·(1+r)^n / ((1+r)^n − 1)",
    summary="Equated Monthly Instalment, total interest and total repayment on a reducing-balance loan.",
    viz_template="viz/loan-emi.html",
)
def compute(amount: float, rate_pct: float, months: float):
    P = float(amount)
    annual = float(rate_pct)
    n = int(float(months))
    if P <= 0 or n <= 0 or annual < 0:
        return {"error": "Loan amount and tenure must be positive.", "steps": []}

    r = annual / 12 / 100  # monthly rate as a decimal
    if r == 0:
        emi = P / n
    else:
        factor = (1 + r) ** n
        emi = P * r * factor / (factor - 1)

    total_payment = emi * n
    total_interest = total_payment - P

    steps = [
        {"label": "List the known values",
         "math": r"\( P = %g,\quad \text{annual rate} = %g\%%,\quad n = %d \text{ months} \)"
                 % (P, annual, n)},
        {"label": "Convert the annual rate to a monthly decimal rate",
         "math": r"\( r = \dfrac{%g}{12 \times 100} = %.6g \)" % (annual, r)},
        {"label": "Raise (1 + r) to the number of months",
         "math": r"\( (1+r)^{n} = (1+%.6g)^{%d} = %.6g \)" % (r, n, (1+r)**n)},
        {"label": "Apply the EMI formula",
         "math": r"\( EMI = \dfrac{P\,r\,(1+r)^n}{(1+r)^n - 1} = %.2f \)" % emi},
        {"label": "Total payment over the whole tenure",
         "math": r"\( EMI \times n = %.2f \times %d = %.2f \)" % (emi, n, total_payment)},
        {"label": "Total interest = total payment − principal",
         "math": r"\( %.2f - %g = %.2f \)" % (total_payment, P, total_interest)},
    ]
    return {
        "emi": round(emi, 2),
        "total_payment": round(total_payment, 2),
        "total_interest": round(total_interest, 2),
        "principal": round(P, 2),
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
