"""Cube of a Sum (a+b)³ — maths › Algebra › Cube Identities. Expand and verify (a+b)³ = a³ + 3a²b + 3ab² + b³, each term shown numerically."""
from core.registry import register


@register(
    slug='cube-of-sum', name='Cube of a Sum (a+b)³', section="maths", topic="Algebra", sub='Cube Identities',
    tags=['algebra', 'identity', 'expansion', 'cube', 'cube of sum'],
    formula='(a+b)³ = a³ + 3a² b + 3ab² + b³',
    summary='Expand and verify (a+b)³ = a³ + 3a²b + 3ab² + b³, each term shown numerically.',
    viz_template="viz/cube-of-sum.html",
    scholar="pingala",
)
def compute(a=2, b=1):
    uni_identity = '(a+b)³ = a³ + 3a² b + 3ab² + b³'
    uni_lhs = '(a+b)³'
    try:
        a = float(a); b = float(b)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for the variables.", "steps": []}
    lhs = (a + b) ** 3
    terms = [{"tex": r"a^3", "num": a**3}, {"tex": r"3a^2b", "num": 3*a*a*b}, {"tex": r"3ab^2", "num": 3*a*b*b}, {"tex": r"b^3", "num": b**3}]
    rhs = sum(t["num"] for t in terms)
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    steps = [
        {"label": "The identity",
         "math": r"\( (a+b)^3 = a^3 + 3a^2 b + 3ab^2 + b^3 \)"},
        {"label": "Substitute your values",
         "math": "\\( (a+b)^3 \\) with " + ", ".join(["a=%s"%fmt(a),"b=%s"%fmt(b)] + (["None"] if False else []))},
        {"label": "Left-hand side",
         "math": "\\( (a+b)^3 = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side, term by term",
         "math": "\\( " + " + ".join(t["tex"]+"=%s"%fmt(t["num"]) for t in terms) + " \\)"},
        {"label": "Sum of right-hand side",
         "math": "\\( = %s \\)" % fmt(rhs)},
        {"label": "Conclusion",
         "math": ("\\( \\text{LHS} = \\text{RHS} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, and the expanded right-hand side also gives %s." % (fmt(lhs), fmt(rhs))
    return {"result": result, "identity": uni_identity,
            "lhs_label": uni_lhs, "lhs_val": fmt(lhs), "rhs_val": fmt(rhs),
            "verified": verified, "expand_title": "Cube of a Sum (a+b)³ expansion",
            "terms": [{"tex": t["tex"], "val": fmt(t["num"]), "num": t["num"]} for t in terms],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
