"""If x + 1/x = a, then x² + 1/x² = a² − 2 — maths › Algebra › Substitution Identities. Verify: if x + 1/x = a then x² + 1/x² = a² − 2, using your value of x."""
from core.registry import register


@register(
    slug='x-plus-reciprocal-squared', name='If x + 1/x = a, then x² + 1/x² = a² − 2', section="maths", topic="Algebra", sub='Substitution Identities',
    tags=['algebra', 'identity', 'x plus reciprocal squared'],
    formula='x + 1/x = a  =>  x² + 1/x² = a² - 2',
    summary='Verify: if x + 1/x = a then x² + 1/x² = a² − 2, using your value of x.',
    viz_template="viz/x-plus-reciprocal-squared.html",
    scholar="diophantus",
)
def compute(x=3):
    uni_identity = 'x + 1/x = a  ⇒  x² + 1/x² = a² - 2'
    uni_lhs = 'x² + 1/x²'
    try:
        x = float(x)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for all values.", "steps": []}
    lhs = x*x + 1.0/(x*x)
    rhs = (x + 1.0/x)**2 - 2
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    chips = [(r"(x+1/x)^2", (x+1.0/x)**2), (r"-2", -2), (r"a=x+1/x", x+1.0/x)]
    rhs_tex = r"a^2 - 2 \text{ where } a = x+1/x"
    steps = [
        {"label": "The identity", "math": r"\( x + \tfrac{1}{x} = a \;\Rightarrow\; x^2 + \tfrac{1}{x^2} = a^2 - 2 \)"},
        {"label": "Your values", "math": "\\( " + ", ".join(["x=%s"%fmt(x)]) + " \\)"},
        {"label": "Left-hand side", "math": "\\( x^2 + 1/x^2 = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side (expanded)", "math": "\\( " + rhs_tex + " = %s \\)" % fmt(rhs)},
        {"label": "Conclusion", "math": ("\\( \\text{both sides} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, and the expanded right-hand side also gives %s." % (fmt(lhs), fmt(rhs))
    return {"result": result, "identity": uni_identity, "lhs_label": uni_lhs,
            "lhs_val": fmt(lhs), "rhs_val": fmt(rhs), "verified": verified,
            "expand_title": 'If x + 1/x = a, then x² + 1/x² = a² − 2',
            "terms": [{"tex": t[0], "val": fmt(t[1]), "num": t[1]} for t in chips],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
