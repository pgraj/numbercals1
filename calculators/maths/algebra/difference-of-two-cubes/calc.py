"""Difference of Two Cubes a³−b³ — maths › Algebra › Sum / Difference of Two Cubes. Factor and verify a³−b³ = (a−b)(a²+ab+b²), with each factor shown numerically."""
from core.registry import register


@register(
    slug='difference-of-two-cubes', name='Difference of Two Cubes a³−b³', section="maths", topic="Algebra", sub='Sum / Difference of Two Cubes',
    tags=['algebra', 'identity', 'factorisation', 'difference of two cubes'],
    formula='a³ - b³ = (a-b)(a² + ab + b²)',
    summary='Factor and verify a³−b³ = (a−b)(a²+ab+b²), with each factor shown numerically.',
    viz_template="viz/difference-of-two-cubes.html",
    scholar="isaac-newton",
)
def compute(a=4, b=2):
    uni_identity = 'a³ - b³ = (a-b)(a² + ab + b²)'
    uni_lhs = 'a³-b³'
    try:
        a = float(a); b = float(b)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for the variables.", "steps": []}
    lhs = a**3 - b**3
    rhs = (a - b) * (a*a + a*b + b*b)
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    rhs_tex = r"(a-b)(a^2+ab+b^2) = (%s)(%s)" % (fmt(a-b), fmt(a*a+a*b+b*b))
    chips = [(r"a^3", a**3), (r"b^3", b**3), (r"(a-b)", a-b), (r"(a^2+ab+b^2)", a*a+a*b+b*b)]
    steps = [
        {"label": "The identity",
         "math": r"\( a^3 - b^3 = (a-b)(a^2 + ab + b^2) \)"},
        {"label": "Substitute your values",
         "math": "\\( " + ", ".join(["a=%s"%fmt(a),"b=%s"%fmt(b)] + (["c=%s"%fmt(c)] if False else [])) + " \\)"},
        {"label": "Left-hand side",
         "math": "\\( a^3-b^3 = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side (factored form)",
         "math": "\\( " + rhs_tex + " = %s \\)" % fmt(rhs)},
        {"label": "Conclusion",
         "math": ("\\( \\text{both sides} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, and the factored right-hand side also gives %s." % (fmt(lhs), fmt(rhs))
    return {"result": result, "identity": uni_identity, "lhs_label": uni_lhs,
            "lhs_val": fmt(lhs), "rhs_val": fmt(rhs), "verified": verified,
            "expand_title": 'Difference of Two Cubes a³−b³',
            "terms": [{"tex": t[0], "val": fmt(t[1]), "num": t[1]} for t in chips],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
