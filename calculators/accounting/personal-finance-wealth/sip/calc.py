"""SIP — accounting › Personal Finance / Wealth Management.
Stacked columns year-by-year: contributions vs growth from compounding.
Steps included: the monthly-rate SIP formula is worth walking through."""
from core.registry import register


@register(
    slug="sip",
    name="SIP Calculator",
    section="accounting",
    sub="Personal Finance / Wealth Management",
    tags=["sip", "investing", "monthly", "compound", "mutual fund"],
    formula="M = P·[((1+i)^n − 1)/i]·(1+i)",
    summary="Future value of a monthly Systematic Investment Plan, split into amount invested and returns.",
    viz_template="viz/sip.html",
)
def compute(monthly_investment: float, rate_pct: float, years: float):
    P = float(monthly_investment)
    annual = float(rate_pct)
    yrs = float(years)
    if P < 0 or annual < 0 or yrs <= 0:
        return {"error": "Monthly investment and years must be positive.", "steps": []}

    i = annual / 12 / 100  # monthly rate as a decimal
    n = int(round(yrs * 12))

    def fv(months):
        if months <= 0:
            return 0.0
        if i == 0:
            return P * months
        return P * (((1 + i) ** months - 1) / i) * (1 + i)

    M = fv(n)
    invested = P * n
    returns = M - invested

    # Year-by-year stack of invested vs returns.
    series = []
    last = int(yrs) if yrs == int(yrs) else int(yrs) + 1
    for yr in range(1, last + 1):
        yi = min(yr, yrs)
        months = int(round(yi * 12))
        v = fv(months)
        inv = P * months
        series.append({
            "year": yi,
            "invested": round(inv, 2),
            "returns": round(max(v - inv, 0), 2),
            "total": round(v, 2),
        })
        if yr > 200:
            break

    steps = [
        {"label": "List the known values",
         "math": r"\( P = %g,\quad \text{annual rate} = %g\%%,\quad t = %g \text{ yr} \)"
                 % (P, annual, yrs)},
        {"label": "Convert to a monthly rate and a month count",
         "math": r"\( i = \dfrac{%g}{1200} = %.6g,\quad n = %g \times 12 = %d \)"
                 % (annual, i, yrs, n)},
        {"label": "Grow the annuity factor over n months",
         "math": r"\( \dfrac{(1+i)^n - 1}{i} = %.4f \)"
                 % (((1+i)**n - 1)/i if i else n)},
        {"label": "Apply the SIP future-value formula (payments at month start)",
         "math": r"\( M = P\cdot\dfrac{(1+i)^n - 1}{i}\cdot(1+i) = %.2f \)" % M},
        {"label": "Split into your money and the returns",
         "math": r"\( \text{invested} = P\,n = %.2f,\quad \text{returns} = M - \text{invested} = %.2f \)"
                 % (invested, returns)},
    ]
    return {
        "future_value": round(M, 2),
        "invested": round(invested, 2),
        "returns": round(returns, 2),
        "series": series,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
