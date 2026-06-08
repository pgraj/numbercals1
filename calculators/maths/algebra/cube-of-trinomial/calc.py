"""Cube of a Trinomial (a+b+c)³ — maths › Algebra › Cube Identities. Expand and verify (a+b+c)³ using the compact form a³+b³+c³+3(a+b)(b+c)(c+a)."""
from core.registry import register


@register(
    slug='cube-of-trinomial', name='Cube of a Trinomial (a+b+c)³', section="maths", topic="Algebra", sub='Cube Identities',
    tags=['algebra', 'identity', 'expansion', 'cube', 'cube of trinomial'],
    formula='(a+b+c)³ = a³+b³+c³+3(a+b)(b+c)(c+a)',
    summary='Expand and verify (a+b+c)³ using the compact form a³+b³+c³+3(a+b)(b+c)(c+a).',
    viz_template="viz/cube-of-trinomial.html",
    scholar="pingala",
)
def compute(a=1, b=2, c=3):
    uni_identity = '(a+b+c)³ = a³+b³+c³ + 3(a+b)(b+c)(c+a)'
    uni_lhs = '(a+b+c)³'
    try:
        a = float(a); b = float(b); c = float(c)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for the variables.", "steps": []}
    lhs = (a + b + c) ** 3
    terms = [{"tex": r"a^3", "num": a**3}, {"tex": r"b^3", "num": b**3}, {"tex": r"c^3", "num": c**3}, {"tex": r"3(a+b)(b+c)(c+a)", "num": 3*(a+b)*(b+c)*(c+a)}]
    rhs = sum(t["num"] for t in terms)
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    steps = [
        {"label": "The identity",
         "math": r"\( (a+b+c)^3 = a^3+b^3+c^3 + 3(a+b)(b+c)(c+a) \)"},
        {"label": "Substitute your values",
         "math": "\\( (a+b+c)^3 \\) with " + ", ".join(["a=%s"%fmt(a),"b=%s"%fmt(b)] + (["c=%s"%fmt(c)] if True else []))},
        {"label": "Left-hand side",
         "math": "\\( (a+b+c)^3 = %s \\)" % fmt(lhs)},
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
            "verified": verified, "expand_title": "Cube of a Trinomial (a+b+c)³ expansion",
            "terms": [{"tex": t["tex"], "val": fmt(t["num"]), "num": t["num"]} for t in terms],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
