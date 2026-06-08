"""Sum (a+b)³ + (a−b)³ — maths › Algebra › Cube Identities. Verify the elegant collapse (a+b)³ + (a−b)³ = 2a³ + 6ab², where odd-power terms cancel."""
from core.registry import register


@register(
    slug='sum-of-cubes-of-binomials', name='Sum (a+b)³ + (a−b)³', section="maths", topic="Algebra", sub='Cube Identities',
    tags=['algebra', 'identity', 'expansion', 'cube', 'sum of cubes of binomials'],
    formula='(a+b)³ + (a-b)³ = 2a³ + 6ab²',
    summary='Verify the elegant collapse (a+b)³ + (a−b)³ = 2a³ + 6ab², where odd-power terms cancel.',
    viz_template="viz/sum-of-cubes-of-binomials.html",
    scholar="pingala",
)
def compute(a=4, b=2):
    uni_identity = '(a+b)³ + (a-b)³ = 2a³ + 6ab²'
    uni_lhs = '(a+b)³ + (a-b)³'
    try:
        a = float(a); b = float(b)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for the variables.", "steps": []}
    lhs = (a + b) ** 3 + (a - b) ** 3
    terms = [{"tex": r"2a^3", "num": 2*a**3}, {"tex": r"6ab^2", "num": 6*a*b*b}]
    rhs = sum(t["num"] for t in terms)
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    steps = [
        {"label": "The identity",
         "math": r"\( (a+b)^3 + (a-b)^3 = 2a^3 + 6ab^2 \)"},
        {"label": "Substitute your values",
         "math": "\\( (a+b)^3 + (a-b)^3 \\) with " + ", ".join(["a=%s"%fmt(a),"b=%s"%fmt(b)] + (["None"] if False else []))},
        {"label": "Left-hand side",
         "math": "\\( (a+b)^3 + (a-b)^3 = %s \\)" % fmt(lhs)},
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
            "verified": verified, "expand_title": "Sum (a+b)³ + (a−b)³ expansion",
            "terms": [{"tex": t["tex"], "val": fmt(t["num"]), "num": t["num"]} for t in terms],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
