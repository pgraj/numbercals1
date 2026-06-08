"""If x + 1/x = a, then x³ + 1/x³ = a³ − 3a — maths › Algebra › Substitution Identities. Verify: if x + 1/x = a then x³ + 1/x³ = a³ − 3a, using your value of x."""
from core.registry import register


@register(
    slug='x-plus-reciprocal-cubed', name='If x + 1/x = a, then x³ + 1/x³ = a³ − 3a', section="maths", topic="Algebra", sub='Substitution Identities',
    tags=['algebra', 'identity', 'x plus reciprocal cubed'],
    formula='x + 1/x = a  =>  x³ + 1/x³ = a³ - 3a',
    summary='Verify: if x + 1/x = a then x³ + 1/x³ = a³ − 3a, using your value of x.',
    viz_template="viz/x-plus-reciprocal-cubed.html",
    scholar="diophantus",
)
def compute(x=2):
    uni_identity = 'x + 1/x = a  ⇒  x³ + 1/x³ = a³ - 3a'
    uni_lhs = 'x³ + 1/x³'
    try:
        x = float(x)
    except (TypeError, ValueError):
        return {"error": "Enter numbers for all values.", "steps": []}
    lhs = x**3 + 1.0/(x**3)
    rhs = (x + 1.0/x)**3 - 3*(x + 1.0/x)
    verified = abs(lhs - rhs) < 1e-6
    def fmt(v):
        return str(int(v)) if abs(v - round(v)) < 1e-9 else str(round(v, 4))
    chips = [(r"(x+1/x)^3", (x+1.0/x)**3), (r"-3(x+1/x)", -3*(x+1.0/x)), (r"a=x+1/x", x+1.0/x)]
    rhs_tex = r"a^3 - 3a \text{ where } a = x+1/x"
    steps = [
        {"label": "The identity", "math": r"\( x + \tfrac{1}{x} = a \;\Rightarrow\; x^3 + \tfrac{1}{x^3} = a^3 - 3a \)"},
        {"label": "Your values", "math": "\\( " + ", ".join(["x=%s"%fmt(x)]) + " \\)"},
        {"label": "Left-hand side", "math": "\\( x^3 + 1/x^3 = %s \\)" % fmt(lhs)},
        {"label": "Right-hand side (expanded)", "math": "\\( " + rhs_tex + " = %s \\)" % fmt(rhs)},
        {"label": "Conclusion", "math": ("\\( \\text{both sides} = %s \\;\\checkmark \\)" % fmt(lhs)) if verified else "\\( \\text{mismatch} \\)"},
    ]
    result = uni_lhs + " = %s, and the expanded right-hand side also gives %s." % (fmt(lhs), fmt(rhs))
    return {"result": result, "identity": uni_identity, "lhs_label": uni_lhs,
            "lhs_val": fmt(lhs), "rhs_val": fmt(rhs), "verified": verified,
            "expand_title": 'If x + 1/x = a, then x³ + 1/x³ = a³ − 3a',
            "terms": [{"tex": t[0], "val": fmt(t[1]), "num": t[1]} for t in chips],
            "steps": steps}


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
