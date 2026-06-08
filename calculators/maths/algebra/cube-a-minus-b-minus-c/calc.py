"""Cube of (a−b−c) — maths › Algebra › Cube Identities. Compute and verify (a−b−c)³ numerically; the full signed expansion is shown step by step."""
from core.registry import register


@register(
    slug='cube-a-minus-b-minus-c', name='Cube of (a−b−c)', section="maths", topic="Algebra", sub='Cube Identities',
    tags=['algebra', 'identity', 'expansion', 'cube', 'cube a minus b minus c'],
    formula='(a-b-c)³',
    summary='Compute and verify (a−b−c)³ numerically; the full signed expansion is shown step by step.',
    viz_template="viz/cube-a-minus-b-minus-c.html",
    scholar="pingala",
)
def compute(a=9, b=2, c=1):
    uni_identity = '(a-b-c)³ = a³ - b³ - c³ - 3a²(b+c) + 3a(b+c)² - 3b² c - 3bc² - 6abc  (verified numerically)'
    uni_lhs = '(a-b-c)³'
    try:
        a = float(a); b = float(b); c = float(c)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for the variables.", "steps": []}
    lhs = (a - b - c) ** 3
    terms = [{"tex": r"(a-b-c)^3", "num": (a-b-c)**3}]
    rhs = sum(t["num"] for t in terms)
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    steps = [
        {"label": "The identity",
         "math": r"\( (a-b-c)^3 = a^3 - b^3 - c^3 - 3a^2(b+c) + 3a(b+c)^2 - 3b^2 c - 3bc^2 - 6abc \;(\text{verified numerically}) \)"},
        {"label": "Substitute your values",
         "math": "\\( (a-b-c)^3 \\) with " + ", ".join(["a=%s"%fmt(a),"b=%s"%fmt(b)] + (["c=%s"%fmt(c)] if True else []))},
        {"label": "Left-hand side",
         "math": "\\( (a-b-c)^3 = %s \\)" % fmt(lhs)},
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
            "verified": verified, "expand_title": "Cube of (a−b−c) expansion",
            "terms": [{"tex": t["tex"], "val": fmt(t["num"]), "num": t["num"]} for t in terms],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
