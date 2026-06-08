"""(ax+b)(cx+d) — maths › Algebra › Other Useful Identities. Expand and verify the general product (ax+b)(cx+d) = acx² + (ad+bc)x + bd."""
from core.registry import register


@register(
    slug='product-ax-plus-b-cx-plus-d', name='(ax+b)(cx+d)', section="maths", topic="Algebra", sub='Other Useful Identities',
    tags=['algebra', 'identity', 'expansion', 'product', 'product ax plus b cx plus d'],
    formula='(ax+b)(cx+d) = acx² + (ad+bc)x + bd',
    summary='Expand and verify the general product (ax+b)(cx+d) = acx² + (ad+bc)x + bd.',
    viz_template="viz/product-ax-plus-b-cx-plus-d.html",
    scholar="francois-viete",
)
def compute(x=2, a=3, b=1, c=2, d=5):
    uni_identity = '(ax+b)(cx+d) = acx² + (ad+bc)x + bd'
    uni_lhs = '(ax+b)(cx+d)'
    try:
        x = float(x); a = float(a); b = float(b); c = float(c); d = float(d)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for all values.", "steps": []}
    lhs = (a*x + b) * (c*x + d)
    rhs = a*c*x*x + (a*d + b*c)*x + b*d
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    chips = [(r"acx^2", a*c*x*x), (r"(ad+bc)x", (a*d+b*c)*x), (r"bd", b*d)]
    rhs_tex = r"acx^2 + (ad+bc)x + bd"
    steps = [
        {"label": "The identity",
         "math": r"\( (ax+b)(cx+d) = acx^2 + (ad+bc)x + bd \)"},
        {"label": "Your values",
         "math": "\\( " + ", ".join(["x=%s"%fmt(x), "a=%s"%fmt(a), "b=%s"%fmt(b), "c=%s"%fmt(c), "d=%s"%fmt(d)]) + " \\)"},
        {"label": "Left-hand side (the product)",
         "math": "\\( (ax+b)(cx+d) = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side (expanded)",
         "math": "\\( " + rhs_tex + " = %s \\)" % fmt(rhs)},
        {"label": "Conclusion",
         "math": ("\\( \\text{both sides} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, and the expanded right-hand side also gives %s." % (fmt(lhs), fmt(rhs))
    return {"result": result, "identity": uni_identity, "lhs_label": uni_lhs,
            "lhs_val": fmt(lhs), "rhs_val": fmt(rhs), "verified": verified,
            "expand_title": '(ax+b)(cx+d)',
            "terms": [{"tex": t[0], "val": fmt(t[1]), "num": t[1]} for t in chips],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
