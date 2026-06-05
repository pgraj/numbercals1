"""LCM — maths › Arithmetic. Number line marking common multiples."""
from math import gcd
from core.registry import register


@register(
    slug="lcm",
    name="LCM (Least Common Multiple) calculator",
    section="maths",
    sub="Arithmetic",
    tags=["lcm", "multiple", "least common multiple"],
    formula="lcm(a,b) = |a·b| / gcd(a,b)",
    summary="Least common multiple of two positive integers.",
    viz_template="viz/lcm.html",
    scholar="euclid",
)
def compute(a: float = 4, b: float = 6):
    a = int(a); b = int(b)
    if a == 0 or b == 0:
        return {"error": "both numbers must be non-zero", "series": []}
    lcm = abs(a * b) // gcd(a, b)
    series = [
        {"n": a, "multiples": [a * k for k in range(1, (lcm // a) + 1)]},
        {"n": b, "multiples": [b * k for k in range(1, (lcm // b) + 1)]},
    ]
    return {"lcm": lcm, "numbers": [a, b], "series": series}
from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
