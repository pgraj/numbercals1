"""Interest rate — accounting › Loans & Credit Analytics.
Sensitivity map: maturity value over time at the implied rate +/- bands.
Steps included: recovering the rate via the n-th root."""
from core.registry import register


@register(
    slug="interest-rate",
    name="Interest Rate Calculator",
    section="accounting",
    sub="Loans & Credit Analytics",
    tags=["interest rate", "implied rate", "effective rate", "maturity"],
    formula="r = (A / P)^(1/n) − 1",
    summary="The implied annual interest rate that turns a principal into a known maturity amount.",
    viz_template="viz/interest-rate.html",
)
def compute(principal: float, maturity_amount: float, years: float):
    P = float(principal)
    A = float(maturity_amount)
    n = float(years)
    if P <= 0 or A <= 0 or n <= 0:
        return {"error": "Principal, maturity amount and years must all be positive.",
                "steps": []}

    ratio = A / P
    r = ratio ** (1 / n) - 1            # nominal annual rate (annual compounding)
    effective = (1 + r) ** 1 - 1        # equals r here; shown for completeness

    # Sensitivity: project P at r-2%, r, r+2% across the years.
    bands = []
    for delta, label in [(-0.02, "−2%"), (0.0, "implied"), (0.02, "+2%")]:
        rr = r + delta
        pts = []
        last = int(n) if n == int(n) else int(n) + 1
        for yr in range(0, last + 1):
            yi = min(yr, n)
            pts.append({"year": yi, "value": round(P * (1 + rr) ** yi, 2)})
            if yr > 200:
                break
        bands.append({"label": label, "delta_pct": round(delta * 100, 2),
                      "rate_pct": round(rr * 100, 2), "points": pts})

    steps = [
        {"label": "List the known values",
         "math": r"\( P = %g,\quad A = %g,\quad n = %g \)" % (P, A, n)},
        {"label": "Divide the maturity amount by the principal",
         "math": r"\( \dfrac{A}{P} = \dfrac{%g}{%g} = %.6g \)" % (A, P, ratio)},
        {"label": "Take the n-th root to undo the compounding",
         "math": r"\( \left(\dfrac{A}{P}\right)^{1/n} = %.6g^{\,1/%g} = %.6g \)"
                 % (ratio, n, ratio ** (1/n))},
        {"label": "Subtract 1 to recover the rate",
         "math": r"\( r = %.6g - 1 = %.6g \)" % (ratio ** (1/n), r)},
        {"label": "Express as a percentage",
         "math": r"\( r = %.2f\%% \text{ per year} \)" % (r * 100)},
    ]
    return {
        "rate_pct": round(r * 100, 2),
        "effective_pct": round(effective * 100, 2),
        "principal": round(P, 2),
        "maturity_amount": round(A, 2),
        "bands": bands,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
