"""Break-even — accounting › Corporate / Business Accounting.
Classic break-even line graph: total revenue vs total cost, crossing at break-even.
Steps included: the rearrangement to units is a short teaching derivation."""
from core.registry import register


@register(
    slug="break-even",
    name="Break-even Calculator (Basic)",
    section="accounting",
    sub="Corporate / Business Accounting",
    tags=["break-even", "fixed cost", "contribution margin", "units"],
    formula="BEP (units) = Fixed Costs / (Price − Variable Cost)",
    summary="The number of units and the revenue at which total cost equals total revenue.",
    viz_template="viz/break-even.html",
)
def compute(fixed_costs: float, variable_cost: float, price: float):
    F = float(fixed_costs)
    v = float(variable_cost)
    p = float(price)
    if F < 0 or v < 0 or p <= 0:
        return {"error": "Price must be positive; costs cannot be negative.", "steps": []}
    contribution = p - v
    if contribution <= 0:
        return {"error": "Selling price must exceed the variable cost per unit, "
                         "otherwise the business never breaks even.", "steps": []}

    units = F / contribution
    revenue = units * p

    # Lines for the chart: plot from 0 to ~2x break-even units.
    span = max(int(units * 2) + 1, 2)
    series = []
    step = max(span // 40, 1)
    q = 0
    while q <= span:
        series.append({
            "units": q,
            "revenue": round(p * q, 2),
            "cost": round(F + v * q, 2),
        })
        q += step
    if series and series[-1]["units"] != span:
        series.append({"units": span, "revenue": round(p*span,2), "cost": round(F+v*span,2)})

    steps = [
        {"label": "Work out the contribution margin per unit",
         "math": r"\( p - v = %g - %g = %g \)" % (p, v, contribution),
         "note": "Each unit sold contributes this much towards the fixed costs."},
        {"label": "Set total revenue equal to total cost",
         "math": r"\( p\,Q = F + v\,Q \)"},
        {"label": "Group the Q terms",
         "math": r"\( (p - v)\,Q = F \)"},
        {"label": "Solve for Q (the break-even quantity)",
         "math": r"\( Q = \dfrac{F}{p - v} = \dfrac{%g}{%g} = %.4g \)" % (F, contribution, units)},
        {"label": "Break-even revenue = price × units",
         "math": r"\( %g \times %.4g = %.2f \)" % (p, units, revenue)},
    ]
    return {
        "units": round(units, 4),
        "revenue": round(revenue, 2),
        "contribution": round(contribution, 2),
        "fixed_costs": round(F, 2),
        "series": series,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
