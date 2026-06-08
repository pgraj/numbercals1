"""(x+a)(x−a) — maths › Algebra › Other Useful Identities. Expand and verify (x+a)(x−a) = x² − a² - the difference of squares as a product."""
from core.registry import register


@register(
    slug='product-x-plus-a-x-minus-a', name='(x+a)(x−a)', section="maths", topic="Algebra", sub='Other Useful Identities',
    tags=['algebra', 'identity', 'expansion', 'product', 'product x plus a x minus a'],
    formula='(x+a)(x-a) = x² - a²',
    summary='Expand and verify (x+a)(x−a) = x² − a² - the difference of squares as a product.',
    viz_template="viz/product-x-plus-a-x-minus-a.html",
    scholar="brahmagupta",
)
def compute(x=9, a=4):
    uni_identity = '(x+a)(x-a) = x² - a²'
    uni_lhs = '(x+a)(x-a)'
    try:
        x = float(x); a = float(a)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for all values.", "steps": []}
    lhs = (x + a) * (x - a)
    rhs = x*x - a*a
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    chips = [(r"x^2", x*x), (r"-a^2", -(a*a))]
    rhs_tex = r"x^2 - a^2"
    steps = [
        {"label": "The identity",
         "math": r"\( (x+a)(x-a) = x^2 - a^2 \)"},
        {"label": "Your values",
         "math": "\\( " + ", ".join(["x=%s"%fmt(x), "a=%s"%fmt(a)]) + " \\)"},
        {"label": "Left-hand side (the product)",
         "math": "\\( (x+a)(x-a) = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side (expanded)",
         "math": "\\( " + rhs_tex + " = %s \\)" % fmt(rhs)},
        {"label": "Conclusion",
         "math": ("\\( \\text{both sides} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, and the expanded right-hand side also gives %s." % (fmt(lhs), fmt(rhs))
    return {"result": result, "identity": uni_identity, "lhs_label": uni_lhs,
            "lhs_val": fmt(lhs), "rhs_val": fmt(rhs), "verified": verified,
            "expand_title": '(x+a)(x−a)',
            "terms": [{"tex": t[0], "val": fmt(t[1]), "num": t[1]} for t in chips],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
