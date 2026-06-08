"""Cube of a Linear Binomial (ax+b)³ — maths › Algebra › Cube of Linear Binomial. Expand and verify (ax+b)³ = a³x³ + 3a²bx² + 3ab²x + b³."""
from core.registry import register


@register(
    slug='cube-of-linear-binomial', name='Cube of a Linear Binomial (ax+b)³', section="maths", topic="Algebra", sub='Cube of Linear Binomial',
    tags=['algebra', 'identity', 'cube of linear binomial'],
    formula='(ax+b)³ = a³x³ + 3a²bx² + 3ab²x + b³',
    summary='Expand and verify (ax+b)³ = a³x³ + 3a²bx² + 3ab²x + b³.',
    viz_template="viz/cube-of-linear-binomial.html",
    scholar="pingala",
)
def compute(x=2, a=3, b=1):
    uni_identity = '(ax+b)³ = a³x³ + 3a²bx² + 3ab²x + b³'
    uni_lhs = '(ax+b)³'
    try:
        x = float(x); a = float(a); b = float(b)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for all values.", "steps": []}
    lhs = (a*x + b)**3
    rhs = a**3*x**3 + 3*a*a*b*x*x + 3*a*b*b*x + b**3
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    chips = [(r"a^3x^3", a**3*x**3), (r"3a^2bx^2", 3*a*a*b*x*x), (r"3ab^2x", 3*a*b*b*x), (r"b^3", b**3)]
    rhs_tex = r"a^3x^3 + 3a^2bx^2 + 3ab^2x + b^3"
    steps = [
        {"label": "The identity", "math": r"\( (ax+b)^3 = a^3x^3 + 3a^2bx^2 + 3ab^2x + b^3 \)"},
        {"label": "Your values", "math": "\\( " + ", ".join(["x=%s"%fmt(x), "a=%s"%fmt(a), "b=%s"%fmt(b)]) + " \\)"},
        {"label": "Left-hand side", "math": "\\( (ax+b)^3 = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side (expanded)", "math": "\\( " + rhs_tex + " = %s \\)" % fmt(rhs)},
        {"label": "Conclusion", "math": ("\\( \\text{both sides} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, and the expanded right-hand side also gives %s." % (fmt(lhs), fmt(rhs))
    return {"result": result, "identity": uni_identity, "lhs_label": uni_lhs,
            "lhs_val": fmt(lhs), "rhs_val": fmt(rhs), "verified": verified,
            "expand_title": 'Cube of a Linear Binomial (ax+b)³',
            "terms": [{"tex": t[0], "val": fmt(t[1]), "num": t[1]} for t in chips],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
