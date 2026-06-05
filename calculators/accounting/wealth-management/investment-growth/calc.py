"""Investment growth — accounting › Wealth Management.
Area chart layering principal, total contributions, and compounded earnings.
Steps included: the two-part formula is worth walking through."""
from core.registry import register


@register(
    slug="investment-growth",
    name="Investment Growth Calculator",
    section="accounting",
    sub="Wealth Management",
    tags=["investing", "contributions", "compound", "wealth"],
    formula="A = P(1+r)^t + PMT·[((1+r)^t − 1)/r]",
    summary="Future wealth from a starting principal plus regular yearly contributions, compounded.",
    viz_template="viz/investment-growth.html",
)
def compute(principal: float, annual_contribution: float, rate_pct: float, years: float):
    P = float(principal)
    PMT = float(annual_contribution)
    r = float(rate_pct) / 100
    t = float(years)
    if P < 0 or PMT < 0 or t < 0:
        return {"error": "Principal, contribution and years must be zero or positive.",
                "steps": []}

    def fv(n):
        grown_principal = P * (1 + r) ** n
        if r == 0:
            grown_contrib = PMT * n
        else:
            grown_contrib = PMT * (((1 + r) ** n - 1) / r)
        return grown_principal, grown_contrib

    gp, gc = fv(t)
    total = gp + gc

    # Year-by-year bands for the area chart.
    series = []
    last = int(t) if t == int(t) else int(t) + 1
    for yr in range(0, last + 1):
        yi = min(yr, t)
        p_band = P  # original principal stays flat as a reference band
        contrib_paid = PMT * yi  # cash the investor has put in so far
        gp_y, gc_y = fv(yi)
        total_y = gp_y + gc_y
        earnings = total_y - p_band - contrib_paid
        series.append({
            "year": yi,
            "principal": round(p_band, 2),
            "contributions": round(contrib_paid, 2),
            "earnings": round(max(earnings, 0), 2),
            "total": round(total_y, 2),
        })
        if yr > 200:
            break

    total_contrib = PMT * t
    total_earnings = total - P - total_contrib

    steps = [
        {"label": "List the known values",
         "math": r"\( P = %g,\quad PMT = %g,\quad r = %g\%% = %.4g,\quad t = %g \)"
                 % (P, PMT, float(rate_pct), r, t)},
        {"label": "Grow the starting principal",
         "math": r"\( P(1+r)^t = %g(1+%.4g)^{%g} = %.2f \)" % (P, r, t, gp)},
        {"label": "Grow the stream of yearly contributions",
         "math": r"\( PMT\cdot\dfrac{(1+r)^t - 1}{r} = %.2f \)" % gc,
         "note": "Each contribution compounds for the years remaining after it is paid in."},
        {"label": "Add the two parts for the future wealth",
         "math": r"\( A = %.2f + %.2f = %.2f \)" % (gp, gc, total)},
        {"label": "Of that, earnings = total − principal − contributions",
         "math": r"\( %.2f - %g - %.2f = %.2f \)" % (total, P, total_contrib, total_earnings)},
    ]
    return {
        "future_value": round(total, 2),
        "total_contributions": round(total_contrib, 2),
        "total_earnings": round(total_earnings, 2),
        "principal": round(P, 2),
        "series": series,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
