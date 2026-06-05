"""CAGR — accounting › Investment Analytics.
Line chart: the smooth compounding curve at the CAGR rate across the years.
Steps included: working through the n-th root is worth showing."""
from core.registry import register


@register(
    slug="cagr",
    name="CAGR Calculator",
    section="accounting",
    sub="Investment Analytics",
    tags=["cagr", "growth", "annualised", "return"],
    formula="CAGR = (End / Begin)^(1/n) − 1",
    summary="Compound annual growth rate — the single yearly rate that links a start and end value.",
    viz_template="viz/cagr.html",
)
def compute(begin_value: float, end_value: float, years: float):
    B = float(begin_value)
    E = float(end_value)
    n = float(years)
    if B <= 0 or E <= 0 or n <= 0:
        return {"error": "Beginning value, end value and years must all be positive.",
                "steps": []}

    ratio = E / B
    cagr = ratio ** (1 / n) - 1

    # Smooth compounding curve year by year at the constant CAGR rate.
    series = []
    last = int(n) if n == int(n) else int(n) + 1
    for yr in range(0, last + 1):
        yi = min(yr, n)
        series.append({"year": yi, "value": round(B * (1 + cagr) ** yi, 2)})
        if yr > 200:
            break

    steps = [
        {"label": "List the known values",
         "math": r"\( \text{Begin} = %g,\quad \text{End} = %g,\quad n = %g \)" % (B, E, n)},
        {"label": "Divide end by beginning to get the total growth factor",
         "math": r"\( \dfrac{End}{Begin} = \dfrac{%g}{%g} = %.6g \)" % (E, B, ratio)},
        {"label": "Take the n-th root to spread the growth over each year",
         "math": r"\( %.6g^{\,1/%g} = %.6g \)" % (ratio, n, ratio ** (1/n))},
        {"label": "Subtract 1 to turn the factor into a rate",
         "math": r"\( %.6g - 1 = %.6g \)" % (ratio ** (1/n), cagr)},
        {"label": "Express as a percentage",
         "math": r"\( CAGR = %.2f\%% \)" % (cagr * 100)},
    ]
    return {
        "cagr_pct": round(cagr * 100, 2),
        "begin_value": round(B, 2),
        "end_value": round(E, 2),
        "series": series,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
