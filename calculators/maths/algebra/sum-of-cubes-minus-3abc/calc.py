"""a³+b³+c³−3abc — maths › Algebra › Product of Three Terms. Factor and verify a³+b³+c³−3abc = (a+b+c)(a²+b²+c²−ab−bc−ca)."""
from core.registry import register


@register(
    slug='sum-of-cubes-minus-3abc', name='a³+b³+c³−3abc', section="maths", topic="Algebra", sub='Product of Three Terms',
    tags=['algebra', 'identity', 'factorisation', 'sum of cubes minus 3abc'],
    formula='a³+b³+c³-3abc = (a+b+c)(a²+b²+c²-ab-bc-ca)',
    summary='Factor and verify a³+b³+c³−3abc = (a+b+c)(a²+b²+c²−ab−bc−ca).',
    viz_template="viz/sum-of-cubes-minus-3abc.html",
    scholar="isaac-newton",
)
def compute(a=1, b=2, c=3):
    uni_identity = 'a³+b³+c³-3abc = (a+b+c)(a²+b²+c²-ab-bc-ca)'
    uni_lhs = 'a³+b³+c³-3abc'
    try:
        a = float(a); b = float(b); c = float(c)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for the variables.", "steps": []}
    lhs = a**3 + b**3 + c**3 - 3*a*b*c
    rhs = (a + b + c) * (a*a + b*b + c*c - a*b - b*c - c*a)
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    rhs_tex = r"(a+b+c)(a^2+b^2+c^2-ab-bc-ca) = (%s)(%s)" % (fmt(a+b+c), fmt(a*a+b*b+c*c-a*b-b*c-c*a))
    chips = [(r"a^3+b^3+c^3", a**3+b**3+c**3), (r"-3abc", -3*a*b*c), (r"(a+b+c)", a+b+c), (r"(a^2+b^2+c^2-ab-bc-ca)", a*a+b*b+c*c-a*b-b*c-c*a)]
    steps = [
        {"label": "The identity",
         "math": r"\( a^3+b^3+c^3-3abc = (a+b+c)(a^2+b^2+c^2-ab-bc-ca) \)"},
        {"label": "Substitute your values",
         "math": "\\( " + ", ".join(["a=%s"%fmt(a),"b=%s"%fmt(b)] + (["c=%s"%fmt(c)] if True else [])) + " \\)"},
        {"label": "Left-hand side",
         "math": "\\( a^3+b^3+c^3-3abc = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side (factored form)",
         "math": "\\( " + rhs_tex + " = %s \\)" % fmt(rhs)},
        {"label": "Conclusion",
         "math": ("\\( \\text{both sides} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, and the factored right-hand side also gives %s." % (fmt(lhs), fmt(rhs))
    return {"result": result, "identity": uni_identity, "lhs_label": uni_lhs,
            "lhs_val": fmt(lhs), "rhs_val": fmt(rhs), "verified": verified,
            "expand_title": 'a³+b³+c³−3abc',
            "terms": [{"tex": t[0], "val": fmt(t[1]), "num": t[1]} for t in chips],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
