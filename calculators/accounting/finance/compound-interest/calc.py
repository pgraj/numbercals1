"""Compound interest — accounting › Finance. Custom interactive growth chart."""
from core.registry import register


@register(
    slug="compound-interest",
    name="Compound interest",
    section="accounting",
    sub="Finance",
    tags=["interest", "savings", "growth"],
    formula="A = P(1 + r/n)^(nt)",
    summary="Future value of a principal under compound interest.",
    viz_template="viz/compound_interest.html",
)
def compute(principal: float, rate_pct: float, years: float, n: float = 12):
    P = float(principal); r = float(rate_pct) / 100
    t = float(years); n = float(n)
    A = P * (1 + r / n) ** (n * t)
    # Year-by-year series for the interactive chart.
    series = []
    yr = 0
    while yr <= int(t) if t == int(t) else yr <= t:
        bal = P * (1 + r / n) ** (n * yr)
        series.append({"year": yr, "balance": round(bal, 2)})
        yr += 1
        if yr > 200:  # safety bound
            break
    # ensure the final fractional year is included
    if series and series[-1]["year"] != t:
        series.append({"year": t, "balance": round(A, 2)})

    steps = [
        {"label": "List the known values",
         "math": r"\( P = %g,\quad r = %g\%%,\quad n = %g,\quad t = %g \)"
                 % (P, float(rate_pct), n, t),
         "note": "r is the annual rate; n is how many times a year interest is added."},
        {"label": "Write the rate as a decimal and per period",
         "math": r"\( \dfrac{r}{n} = \dfrac{%g}{%g} = %.6g \)" % (r, n, r / n)},
        {"label": "Apply the compound interest formula",
         "math": r"\( A = P\left(1 + \dfrac{r}{n}\right)^{nt} = %g\left(1 + %.6g\right)^{%g} \)"
                 % (P, r / n, n * t)},
        {"label": "Final amount",
         "math": r"\( A = %.2f \)" % A},
        {"label": "Interest earned = A − P",
         "math": r"\( %.2f - %g = %.2f \)" % (A, P, A - P)},
    ]
    return {
        "future_value": round(A, 2),
        "interest_earned": round(A - P, 2),
        "series": series,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
