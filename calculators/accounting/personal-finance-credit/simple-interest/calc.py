"""Simple interest — accounting › Personal Finance / Credit.
Stacked bar: fixed principal at the base, linearly growing interest on top."""
from core.registry import register


@register(
    slug="simple-interest",
    name="Simple Interest Calculator",
    section="accounting",
    sub="Personal Finance / Credit",
    tags=["interest", "principal", "loan", "savings"],
    formula="I = P·r·t,  A = P + I",
    summary="Interest and maturity value when interest is charged only on the original principal.",
    viz_template="viz/simple-interest.html",
)
def compute(principal: float, rate_pct: float, years: float):
    P = float(principal)
    r = float(rate_pct) / 100
    t = float(years)
    if P < 0 or t < 0:
        return {"error": "Principal and time must be zero or positive.", "steps": []}

    I = P * r * t
    A = P + I

    # Year-by-year stack: principal stays flat, interest grows in a straight line.
    series = []
    last = int(t) if t == int(t) else int(t) + 1
    for yr in range(0, last + 1):
        yi = min(yr, t)
        series.append({
            "year": yi,
            "principal": round(P, 2),
            "interest": round(P * r * yi, 2),
        })
        if yr > 200:
            break

    steps = [
        {"label": "List the known values",
         "math": r"\( P = %g,\quad r = %g\%% = %.4g,\quad t = %g \)"
                 % (P, float(rate_pct), r, t),
         "note": "r is the annual rate written as a decimal; t is the time in years."},
        {"label": "Apply the simple interest formula",
         "math": r"\( I = P\,r\,t = %g \times %.4g \times %g \)" % (P, r, t)},
        {"label": "Interest earned (or owed)",
         "math": r"\( I = %.2f \)" % I},
        {"label": "Add the interest back to the principal",
         "math": r"\( A = P + I = %g + %.2f = %.2f \)" % (P, I, A)},
    ]
    return {
        "interest": round(I, 2),
        "amount": round(A, 2),
        "series": series,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
