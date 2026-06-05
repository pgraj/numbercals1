"""Mortgage — accounting › Loans & Debt.
Pie of the monthly payment: P&I + monthly tax + monthly insurance."""
from core.registry import register


@register(
    slug="mortgage",
    name="Mortgage Calculator",
    section="accounting",
    sub="Loans & Debt",
    tags=["mortgage", "home loan", "repayment", "PITI"],
    formula="M = P·r(1+r)^n / ((1+r)^n − 1) + T + I",
    summary="Total monthly mortgage payment broken into principal & interest, tax and insurance.",
    viz_template="viz/mortgage.html",
)
def compute(home_price: float, down_payment: float, years: float,
            rate_pct: float, annual_tax: float = 0, annual_insurance: float = 0):
    price = float(home_price)
    down = float(down_payment)
    yrs = float(years)
    annual = float(rate_pct)
    P = price - down

    if price <= 0 or yrs <= 0 or annual < 0 or down < 0 or down > price:
        return {"error": "Check inputs: down payment must be between 0 and the home price.",
                "steps": []}

    n = int(yrs * 12)
    r = annual / 12 / 100
    if r == 0:
        pi = P / n
    else:
        factor = (1 + r) ** n
        pi = P * r * factor / (factor - 1)

    t_month = float(annual_tax) / 12
    i_month = float(annual_insurance) / 12
    total = pi + t_month + i_month

    steps = [
        {"label": "Find the loan principal (price − deposit)",
         "math": r"\( P = %g - %g = %g \)" % (price, down, P)},
        {"label": "Monthly rate and number of payments",
         "math": r"\( r = \dfrac{%g}{1200} = %.6g,\quad n = %g \times 12 = %d \)"
                 % (annual, r, yrs, n)},
        {"label": "Principal & interest part of the payment",
         "math": r"\( P\!I = \dfrac{P\,r(1+r)^n}{(1+r)^n-1} = %.2f \)" % pi},
        {"label": "Monthly tax and insurance",
         "math": r"\( T = \dfrac{%g}{12} = %.2f,\quad I = \dfrac{%g}{12} = %.2f \)"
                 % (float(annual_tax), t_month, float(annual_insurance), i_month)},
        {"label": "Total monthly payment",
         "math": r"\( M = %.2f + %.2f + %.2f = %.2f \)" % (pi, t_month, i_month, total)},
    ]
    return {
        "monthly_payment": round(total, 2),
        "principal_interest": round(pi, 2),
        "monthly_tax": round(t_month, 2),
        "monthly_insurance": round(i_month, 2),
        "loan_principal": round(P, 2),
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
