"""Difference (a+b)³ − (a−b)³ — maths › Algebra › Cube Identities. Verify (a+b)³ − (a−b)³ = 6a²b + 2b³, where even-power terms cancel and odd ones double."""
from core.registry import register


@register(
    slug='difference-of-cubes-of-binomials', name='Difference (a+b)³ − (a−b)³', section="maths", topic="Algebra", sub='Cube Identities',
    tags=['algebra', 'identity', 'expansion', 'cube', 'difference of cubes of binomials'],
    formula='(a+b)³ - (a-b)³ = 6a² b + 2b³',
    summary='Verify (a+b)³ − (a−b)³ = 6a²b + 2b³, where even-power terms cancel and odd ones double.',
    viz_template="viz/difference-of-cubes-of-binomials.html",
    scholar="pingala",
)
def compute(a=4, b=2):
    uni_identity = '(a+b)³ - (a-b)³ = 6a² b + 2b³'
    uni_lhs = '(a+b)³ - (a-b)³'
    try:
        a = float(a); b = float(b)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for the variables.", "steps": []}
    lhs = (a + b) ** 3 - (a - b) ** 3
    terms = [{"tex": r"6a^2b", "num": 6*a*a*b}, {"tex": r"2b^3", "num": 2*b**3}]
    rhs = sum(t["num"] for t in terms)
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    steps = [
        {"label": "The identity",
         "math": r"\( (a+b)^3 - (a-b)^3 = 6a^2 b + 2b^3 \)"},
        {"label": "Substitute your values",
         "math": "\\( (a+b)^3 - (a-b)^3 \\) with " + ", ".join(["a=%s"%fmt(a),"b=%s"%fmt(b)] + (["None"] if False else []))},
        {"label": "Left-hand side",
         "math": "\\( (a+b)^3 - (a-b)^3 = %s \\)" % fmt(lhs)},
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
            "verified": verified, "expand_title": "Difference (a+b)³ − (a−b)³ expansion",
            "terms": [{"tex": t["tex"], "val": fmt(t["num"]), "num": t["num"]} for t in terms],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
