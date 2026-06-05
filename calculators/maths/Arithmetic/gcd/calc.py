"""GCD — maths › Arithmetic. Squares-in-rectangle view of the common divisor."""
from math import gcd
from core.registry import register


@register(
    slug="gcd",
    name="GCD (Greatest Common Divisor) calculator",
    section="maths",
    topic="Arithmetic",
    sub="Arithmetic",
    tags=["gcd", "hcf", "greatest common divisor", "factor"],
    formula="gcd via Euclid's algorithm",
    summary="Greatest common divisor (HCF) of two integers.",
    viz_template="viz/gcd.html",
    scholar="euclid",
)
def compute(a: float = 48, b: float = 36):
    a = abs(int(a)); b = abs(int(b))
    if a == 0 and b == 0:
        return {"error": "both numbers cannot be zero", "series": []}
    g = gcd(a, b)
    return {
        "gcd": g,
        "numbers": [a, b],
        "series": [{"label": "tile", "value": g}],
    }
from core.faqs import load_sibling_faq
load_sibling_faq(__file__)