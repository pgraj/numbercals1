"""Exponential — maths › Algebra. Plots y = a·b^x and evaluates at a point."""
from core.registry import register


@register(
    slug="exponential", name="Exponential calculator", section="maths", sub="Algebra",
    tags=["exponential", "growth", "decay", "power"],
    formula="y = a · b^x",
    summary="Evaluate y = a·b^x at a chosen x, with the growth/decay curve plotted.",
    viz_template="viz/exponential.html",
)
def compute(a: float = 2, base: float = 3, x: float = 4):
    a = float(a); base = float(base); x = float(x)
    if base <= 0:
        return {"error": "base must be greater than 0", "series": [], "steps": []}
    result = a * (base ** x)
    span = max(5.0, abs(x) + 3)
    x0, x1 = x - span, x + span
    n = 60
    series = [{"x": round(x0 + (x1 - x0) * i / n, 6),
               "y": round(a * (base ** (x0 + (x1 - x0) * i / n)), 6)} for i in range(n + 1)]
    powers = [{"x": k, "y": round(a * (base ** k), 6)}
              for k in range(int(x0), int(x1) + 1) if abs(k) <= 8]
    steps = [
        {"label": "List the known values",
         "math": r"\( a = %g,\quad b = %g,\quad x = %g \)" % (a, base, x)},
        {"label": "Substitute into y = a·bˣ",
         "math": r"\( y = %g \cdot %g^{%g} \)" % (a, base, x)},
        {"label": "Compute the power",
         "math": r"\( %g^{%g} = %.6g \)" % (base, x, base ** x)},
        {"label": "Multiply by a",
         "math": r"\( y = %g \cdot %.6g = %.6g \)" % (a, base ** x, result)},
    ]
    return {"result": round(result, 6), "a": a, "base": base, "x": x,
            "series": series, "powers": powers, "steps": steps}


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
