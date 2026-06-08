"""Square of (a−b+c) — maths › Algebra › Square Identities. Expand and verify (a−b+c)² with its specific cross-term signs, shown numerically."""
from core.registry import register


@register(
    slug='square-a-minus-b-plus-c', name='Square of (a−b+c)', section="maths", topic="Algebra", sub='Square Identities',
    tags=['algebra', 'identity', 'expansion', 'square', 'square a minus b plus c'],
    formula='(a-b+c)² = a²+b²+c²-2ab-2bc+2ca',
    summary='Expand and verify (a−b+c)² with its specific cross-term signs, shown numerically.',
    viz_template="viz/square-a-minus-b-plus-c.html",
    scholar="al-khwarizmi",
)
def compute(a=6, b=2, c=5):
    uni_identity = '(a-b+c)² = a² + b² + c² - 2ab - 2bc + 2ca'
    uni_lhs = '(a-b+c)²'
    try:
        a = float(a); b = float(b); c = float(c)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for the variables.", "steps": []}
    lhs = (a - b + c) ** 2
    terms = [{"tex": r"a^2", "num": a*a}, {"tex": r"b^2", "num": b*b}, {"tex": r"c^2", "num": c*c}, {"tex": r"-2ab", "num": -2*a*b}, {"tex": r"-2bc", "num": -2*b*c}, {"tex": r"2ca", "num": 2*c*a}]
    rhs = sum(t["num"] for t in terms)
    verified = abs(lhs - rhs) < 1e-9
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    steps = [
        {"label": "The identity",
         "math": r"\( (a-b+c)^2 = a^2 + b^2 + c^2 - 2ab - 2bc + 2ca \)"},
        {"label": "Substitute your values",
         "math": "\\( (a-b+c)^2 \\) with " + ", ".join(filter(None,["a=%s"%fmt(a),"b=%s"%fmt(b),"c=%s"%fmt(c)])) },
        {"label": "Left-hand side",
         "math": "\\( (a-b+c)^2 = %s \\)" % fmt(lhs)},
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
            "verified": verified, "expand_title": "Square of (a−b+c) expansion",
            "terms": [{"tex": t["tex"], "val": fmt(t["num"]), "num": t["num"]} for t in terms],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
