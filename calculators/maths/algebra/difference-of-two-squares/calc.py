"""Difference of Two Squares a²−b² — maths › Algebra › Difference of Two Squares. Factor and verify a²−b² = (a−b)(a+b) - the single most useful factorisation in algebra."""
from core.registry import register


@register(
    slug='difference-of-two-squares', name='Difference of Two Squares a²−b²', section="maths", topic="Algebra", sub='Difference of Two Squares',
    tags=['algebra', 'identity', 'factorisation', 'difference of squares', 'difference of two squares'],
    formula='a² - b² = (a-b)(a+b)',
    summary='Factor and verify a²−b² = (a−b)(a+b) - the single most useful factorisation in algebra.',
    viz_template="viz/difference-of-two-squares.html",
    scholar="brahmagupta",
)
def compute(a=8, b=3):
    uni_identity = 'a² - b² = (a-b)(a+b)'
    uni_lhs = 'a²-b²'
    try:
        a = float(a); b = float(b)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for a and b.", "steps": []}
    lhs = a*a - b*b
    rhs = (a - b) * (a + b)
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    terms = {"factor_tex": r"(a-b)(a+b) = (%s)(%s)" % (fmt(a-b), fmt(a+b)), "factor_plain": "(a-b)(a+b)", "chips": [(r"a^2", a*a), (r"b^2", b*b), (r"(a-b)", a-b), (r"(a+b)", a+b)]}
    steps = [
        {"label": "The identity",
         "math": r"\( a^2 - b^2 = (a-b)(a+b) \)"},
        {"label": "Substitute your values",
         "math": "\\( a=%s,\\ b=%s \\)" % (fmt(a), fmt(b))},
        {"label": "Left-hand side (the difference of squares)",
         "math": "\\( a^2-b^2 = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side (the factored product)",
         "math": "\\( " + terms["factor_tex"] + " = %s \\)" % fmt(rhs)},
        {"label": "Conclusion",
         "math": ("\\( \\text{both sides} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, which factors as %s = %s." % (fmt(lhs), terms["factor_plain"]%(fmt(a),fmt(b),fmt(a),fmt(b)) if "%s" in terms["factor_plain"] else terms["factor_plain"], fmt(rhs))
    return {"result": result, "identity": uni_identity,
            "lhs_label": uni_lhs, "lhs_val": fmt(lhs), "rhs_val": fmt(rhs),
            "verified": verified, "expand_title": "Difference of Two Squares a²−b²",
            "terms": [{"tex": t[0], "val": fmt(t[1]), "num": t[1]} for t in terms["chips"]],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
