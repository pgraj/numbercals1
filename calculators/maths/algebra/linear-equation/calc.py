"""Linear equation solver — maths › Algebra. Plots the line and its root."""
from core.registry import register


@register(
    slug="linear-equation", name="Linear equation solver", section="maths", sub="Algebra",
    tags=["linear", "equation", "root", "slope", "intercept"],
    formula="ax + b = 0  →  x = −b / a",
    summary="Solve ax + b = 0 for x, and see where the line crosses zero.",
    viz_template="viz/linear_equation.html",
)
def compute(a: float = 2, b: float = -6):
    a = float(a); b = float(b)
    if a == 0:
        if b == 0:
            return {"error": "0 = 0: infinitely many solutions", "series": [], "steps": []}
        return {"error": "no solution (a = 0, b ≠ 0)", "series": [], "steps": []}
    root = -b / a
    span = max(10.0, abs(root) * 2 + 5)
    x0, x1 = root - span, root + span
    steps = [
        {"label": "Start from the equation",
         "math": r"\( %g x + (%g) = 0 \)" % (a, b)},
        {"label": "Move the constant to the right",
         "math": r"\( %g x = %g \)" % (a, -b)},
        {"label": "Divide both sides by a",
         "math": r"\( x = \dfrac{%g}{%g} = %.6g \)" % (-b, a, root)},
    ]
    return {"root": round(root, 6), "slope": a, "intercept": b,
            "series": [{"x": round(x0, 6), "y": round(a * x0 + b, 6)},
                       {"x": round(x1, 6), "y": round(a * x1 + b, 6)}],
            "steps": steps}


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
