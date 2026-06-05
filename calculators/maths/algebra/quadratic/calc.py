"""Quadratic solver — maths › Algebra. Roots, parabola, and worked steps."""
from math import sqrt
from core.registry import register


@register(
    slug="quadratic",
    name="Quadratic equation solver",
    section="maths",
    topic="Algebra",
    sub="Algebra",
    tags=["roots", "discriminant", "parabola"],
    formula="x = (−b ± √(b²−4ac)) / 2a",
    summary="Real and complex roots of ax² + bx + c = 0.",
    viz_template="viz/quadratic.html",
)
def compute(a: float = 1, b: float = -3, c: float = 2):
    a = float(a); b = float(b); c = float(c)
    if a == 0:
        return {"error": "a must be non-zero (otherwise it is not quadratic)",
                "discriminant": None, "steps": []}
    d = b * b - 4 * a * c

    # ---- worked steps (LaTeX inside \( \) so MathJax renders them) ----
    steps = [
        {"label": "Write the equation in standard form",
         "math": r"\( %g x^2 + (%g)x + (%g) = 0 \)" % (a, b, c),
         "note": "Identify a, b and c."},
        {"label": "Compute the discriminant  D = b² − 4ac",
         "math": r"\( D = (%g)^2 - 4(%g)(%g) = %g \)" % (b, a, c, d)},
    ]

    if d > 0:
        r1 = (-b + sqrt(d)) / (2 * a)
        r2 = (-b - sqrt(d)) / (2 * a)
        steps.append({"label": "D > 0 → two distinct real roots",
                      "math": r"\( x = \dfrac{-(%g) \pm \sqrt{%g}}{2(%g)} \)" % (b, d, a)})
        steps.append({"label": "Evaluate both roots",
                      "math": r"\( x_1 = %g,\quad x_2 = %g \)" % (r1, r2)})
        nature = "two distinct real roots"
        out = {"discriminant": d, "root1": r1, "root2": r2, "nature": nature}
    elif d == 0:
        r = -b / (2 * a)
        steps.append({"label": "D = 0 → one repeated real root",
                      "math": r"\( x = \dfrac{-(%g)}{2(%g)} = %g \)" % (b, a, r)})
        nature = "one repeated real root"
        out = {"discriminant": d, "root1": r, "root2": r, "nature": nature}
    else:
        real = -b / (2 * a)
        imag = sqrt(-d) / (2 * a)
        real = real + 0.0  # normalise -0.0 to 0.0
        if real == 0:
            real = 0.0
        steps.append({"label": "D < 0 → no real roots; roots are complex",
                      "math": r"\( x = \dfrac{-(%g) \pm \sqrt{%g}\,i}{2(%g)} \)" % (b, -d, a)})
        steps.append({"label": "Express as a complex conjugate pair",
                      "math": r"\( x = %.4g \pm %.4g\,i \)" % (real, imag)})
        nature = "no real roots (complex)"
        out = {"discriminant": d,
               "root1": f"{real:.4g} + {imag:.4g}i",
               "root2": f"{real:.4g} - {imag:.4g}i",
               "nature": nature}

    # ---- parabola series for the chart ----
    vx = -b / (2 * a)              # vertex x
    span = max(5.0, abs(vx) + 4)
    x0, x1 = vx - span, vx + span
    n = 60
    series = [{"x": round(x0 + (x1 - x0) * i / n, 4),
               "y": round(a * (x0 + (x1 - x0) * i / n) ** 2
                          + b * (x0 + (x1 - x0) * i / n) + c, 4)}
              for i in range(n + 1)]
    out["series"] = series
    out["vertex"] = {"x": round(vx, 4), "y": round(a * vx * vx + b * vx + c, 4)}
    out["steps"] = steps
    return out


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
