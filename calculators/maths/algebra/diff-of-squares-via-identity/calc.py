"""(a+b)² − (a−b)² = 4ab — maths › Algebra › Other Useful Identities. Verify (a+b)² − (a−b)² = 4ab - subtracting the squares isolates four times the product."""
from core.registry import register


@register(
    slug='diff-of-squares-via-identity', name='(a+b)² − (a−b)² = 4ab', section="maths", topic="Algebra", sub='Other Useful Identities',
    tags=['algebra', 'identity', 'expansion', 'product', 'diff of squares via identity'],
    formula='(a+b)² - (a-b)² = 4ab',
    summary='Verify (a+b)² − (a−b)² = 4ab - subtracting the squares isolates four times the product.',
    viz_template="viz/diff-of-squares-via-identity.html",
    scholar="brahmagupta",
)
def compute(a=5, b=3):
    uni_identity = '(a+b)² - (a-b)² = 4ab'
    uni_lhs = '(a+b)²-(a-b)²'
    try:
        a = float(a); b = float(b)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for all values.", "steps": []}
    lhs = (a + b)**2 - (a - b)**2
    rhs = 4*a*b
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    chips = [(r"(a+b)^2", (a+b)**2), (r"-(a-b)^2", -((a-b)**2)), (r"4ab", 4*a*b)]
    rhs_tex = r"4ab"
    steps = [
        {"label": "The identity",
         "math": r"\( (a+b)^2 - (a-b)^2 = 4ab \)"},
        {"label": "Your values",
         "math": "\\( " + ", ".join(["a=%s"%fmt(a), "b=%s"%fmt(b)]) + " \\)"},
        {"label": "Left-hand side (the product)",
         "math": "\\( (a+b)^2-(a-b)^2 = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side (expanded)",
         "math": "\\( " + rhs_tex + " = %s \\)" % fmt(rhs)},
        {"label": "Conclusion",
         "math": ("\\( \\text{both sides} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, and the expanded right-hand side also gives %s." % (fmt(lhs), fmt(rhs))
    return {"result": result, "identity": uni_identity, "lhs_label": uni_lhs,
            "lhs_val": fmt(lhs), "rhs_val": fmt(rhs), "verified": verified,
            "expand_title": '(a+b)² − (a−b)² = 4ab',
            "terms": [{"tex": t[0], "val": fmt(t[1]), "num": t[1]} for t in chips],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
