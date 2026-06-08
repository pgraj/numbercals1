"""General Difference of Squares A²−B² — maths › Algebra › Difference of Two Squares. The general form A²−B² = (A−B)(A+B), where A and B can be whole expressions, not just single letters."""
from core.registry import register


@register(
    slug='difference-of-squares-general', name='General Difference of Squares A²−B²', section="maths", topic="Algebra", sub='Difference of Two Squares',
    tags=['algebra', 'identity', 'factorisation', 'difference of squares', 'difference of squares general'],
    formula='A² - B² = (A-B)(A+B)',
    summary='The general form A²−B² = (A−B)(A+B), where A and B can be whole expressions, not just single letters.',
    viz_template="viz/difference-of-squares-general.html",
    scholar="brahmagupta",
)
def compute(a=12, b=5):
    uni_identity = 'A² - B² = (A-B)(A+B)'
    uni_lhs = 'A²-B²'
    try:
        a = float(a); b = float(b)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for a and b.", "steps": []}
    lhs = a*a - b*b
    rhs = (a - b) * (a + b)
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    terms = {"factor_tex": r"(A-B)(A+B) = (%s)(%s)" % (fmt(a-b), fmt(a+b)), "factor_plain": "(A-B)(A+B)", "chips": [(r"A^2", a*a), (r"B^2", b*b), (r"(A-B)", a-b), (r"(A+B)", a+b)]}
    steps = [
        {"label": "The identity",
         "math": r"\( A^2 - B^2 = (A-B)(A+B) \)"},
        {"label": "Substitute your values",
         "math": "\\( a=%s,\\ b=%s \\)" % (fmt(a), fmt(b))},
        {"label": "Left-hand side (the difference of squares)",
         "math": "\\( A^2-B^2 = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side (the factored product)",
         "math": "\\( " + terms["factor_tex"] + " = %s \\)" % fmt(rhs)},
        {"label": "Conclusion",
         "math": ("\\( \\text{both sides} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, which factors as %s = %s." % (fmt(lhs), terms["factor_plain"]%(fmt(a),fmt(b),fmt(a),fmt(b)) if "%s" in terms["factor_plain"] else terms["factor_plain"], fmt(rhs))
    return {"result": result, "identity": uni_identity,
            "lhs_label": uni_lhs, "lhs_val": fmt(lhs), "rhs_val": fmt(rhs),
            "verified": verified, "expand_title": "General Difference of Squares A²−B²",
            "terms": [{"tex": t[0], "val": fmt(t[1]), "num": t[1]} for t in terms["chips"]],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
