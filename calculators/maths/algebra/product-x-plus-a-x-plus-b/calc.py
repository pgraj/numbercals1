"""(x+a)(x+b) — maths › Algebra › Other Useful Identities. Expand and verify (x+a)(x+b) = x² + (a+b)x + ab."""
from core.registry import register


@register(
    slug='product-x-plus-a-x-plus-b', name='(x+a)(x+b)', section="maths", topic="Algebra", sub='Other Useful Identities',
    tags=['algebra', 'identity', 'expansion', 'product', 'product x plus a x plus b'],
    formula='(x+a)(x+b) = x² + (a+b)x + ab',
    summary='Expand and verify (x+a)(x+b) = x² + (a+b)x + ab.',
    viz_template="viz/product-x-plus-a-x-plus-b.html",
    scholar="francois-viete",
)
def compute(x=5, a=2, b=3):
    uni_identity = '(x+a)(x+b) = x² + (a+b)x + ab'
    uni_lhs = '(x+a)(x+b)'
    try:
        x = float(x); a = float(a); b = float(b)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for all values.", "steps": []}
    lhs = (x + a) * (x + b)
    rhs = x*x + (a + b)*x + a*b
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    chips = [(r"x^2", x*x), (r"(a+b)x", (a+b)*x), (r"ab", a*b)]
    rhs_tex = r"x^2 + (a+b)x + ab"
    steps = [
        {"label": "The identity",
         "math": r"\( (x+a)(x+b) = x^2 + (a+b)x + ab \)"},
        {"label": "Your values",
         "math": "\\( " + ", ".join(["x=%s"%fmt(x), "a=%s"%fmt(a), "b=%s"%fmt(b)]) + " \\)"},
        {"label": "Left-hand side (the product)",
         "math": "\\( (x+a)(x+b) = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side (expanded)",
         "math": "\\( " + rhs_tex + " = %s \\)" % fmt(rhs)},
        {"label": "Conclusion",
         "math": ("\\( \\text{both sides} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, and the expanded right-hand side also gives %s." % (fmt(lhs), fmt(rhs))
    return {"result": result, "identity": uni_identity, "lhs_label": uni_lhs,
            "lhs_val": fmt(lhs), "rhs_val": fmt(rhs), "verified": verified,
            "expand_title": '(x+a)(x+b)',
            "terms": [{"tex": t[0], "val": fmt(t[1]), "num": t[1]} for t in chips],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
