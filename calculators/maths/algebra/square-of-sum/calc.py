"""Square of a Sum (a+b)² — maths › Algebra › Square Identities. Expand and verify (a+b)² = a² + 2ab + b², with each term shown numerically."""
from core.registry import register


@register(
    slug='square-of-sum', name='Square of a Sum (a+b)²', section="maths", topic="Algebra", sub='Square Identities',
    tags=['algebra', 'identity', 'expansion', 'square', 'square of sum'],
    formula='(a+b)² = a² + 2ab + b²',
    summary='Expand and verify (a+b)² = a² + 2ab + b², with each term shown numerically.',
    viz_template="viz/square-of-sum.html",
    scholar="al-khwarizmi",
)
def compute(a=3, b=4):
    uni_identity = '(a+b)² = a² + 2ab + b²'
    uni_lhs = '(a+b)²'
    try:
        a = float(a); b = float(b)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for the variables.", "steps": []}
    lhs = (a + b) ** 2
    terms = [{"tex": r"a^2", "num": a*a}, {"tex": r"2ab", "num": 2*a*b}, {"tex": r"b^2", "num": b*b}]
    rhs = sum(t["num"] for t in terms)
    verified = abs(lhs - rhs) < 1e-9
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    steps = [
        {"label": "The identity",
         "math": r"\( (a+b)^2 = a^2 + 2ab + b^2 \)"},
        {"label": "Substitute your values",
         "math": "\\( (a+b)^2 \\) with " + ", ".join(filter(None,["a=%s"%fmt(a),"b=%s"%fmt(b),"None"])) },
        {"label": "Left-hand side",
         "math": "\\( (a+b)^2 = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side, term by term",
         "math": "\\( " + " + ".join(t["tex"]+"=%s"%fmt(t["num"]) for t in terms) + " \\)"},
        {"label": "Sum of right-hand side",
         "math": "\\( = %s \\)" % fmt(rhs)},
        {"label": "Conclusion",
         "math": ("\\( \\text{LHS} = \\text{RHS} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, and expanding the right-hand side also gives %s." % (fmt(lhs), fmt(rhs))
    return {"result": result, "identity": uni_identity,
            "lhs_label": uni_lhs, "lhs_val": fmt(lhs), "rhs_val": fmt(rhs),
            "verified": verified, "expand_title": "Square of a Sum (a+b)² expansion",
            "terms": [{"tex": t["tex"], "val": fmt(t["num"]), "num": t["num"]} for t in terms],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
