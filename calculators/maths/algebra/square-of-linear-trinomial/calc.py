"""Square of a Linear Trinomial (ax+by+c)² — maths › Algebra › Square of Linear Trinomial. Expand and verify (ax+by+c)² with all squares and cross terms, shown numerically."""
from core.registry import register


@register(
    slug='square-of-linear-trinomial', name='Square of a Linear Trinomial (ax+by+c)²', section="maths", topic="Algebra", sub='Square of Linear Trinomial',
    tags=['algebra', 'identity', 'square of linear trinomial'],
    formula='(ax+by+c)² = a²x² + b²y² + c² + 2abxy + 2bcy + 2cax',
    summary='Expand and verify (ax+by+c)² with all squares and cross terms, shown numerically.',
    viz_template="viz/square-of-linear-trinomial.html",
    scholar="al-khwarizmi",
)
def compute(x=2, y=1, a=3, b=2, c=4):
    uni_identity = '(ax+by+c)² = a²x² + b²y² + c² + 2abxy + 2bcy + 2cax'
    uni_lhs = '(ax+by+c)²'
    try:
        x = float(x); y = float(y); a = float(a); b = float(b); c = float(c)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for all values.", "steps": []}
    lhs = (a*x + b*y + c)**2
    rhs = a*a*x*x + b*b*y*y + c*c + 2*a*b*x*y + 2*b*c*y + 2*c*a*x
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    chips = [(r"a^2x^2", a*a*x*x), (r"b^2y^2", b*b*y*y), (r"c^2", c*c), (r"2abxy", 2*a*b*x*y), (r"2bcy", 2*b*c*y), (r"2cax", 2*c*a*x)]
    rhs_tex = r"a^2x^2+b^2y^2+c^2+2abxy+2bcy+2cax"
    steps = [
        {"label": "The identity", "math": r"\( (ax+by+c)^2 = a^2x^2 + b^2y^2 + c^2 + 2abxy + 2bcy + 2cax \)"},
        {"label": "Your values", "math": "\\( " + ", ".join(["x=%s"%fmt(x), "y=%s"%fmt(y), "a=%s"%fmt(a), "b=%s"%fmt(b), "c=%s"%fmt(c)]) + " \\)"},
        {"label": "Left-hand side", "math": "\\( (ax+by+c)^2 = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side (expanded)", "math": "\\( " + rhs_tex + " = %s \\)" % fmt(rhs)},
        {"label": "Conclusion", "math": ("\\( \\text{both sides} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, and the expanded right-hand side also gives %s." % (fmt(lhs), fmt(rhs))
    return {"result": result, "identity": uni_identity, "lhs_label": uni_lhs,
            "lhs_val": fmt(lhs), "rhs_val": fmt(rhs), "verified": verified,
            "expand_title": 'Square of a Linear Trinomial (ax+by+c)²',
            "terms": [{"tex": t[0], "val": fmt(t[1]), "num": t[1]} for t in chips],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
