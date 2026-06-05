"""Ratio — maths › Arithmetic. Squares showing the two parts to scale."""
from math import gcd
from core.registry import register


@register(
    slug="ratio",
    name="Ratio calculator",
    section="maths",
    topic="Arithmetic",
    sub="Arithmetic",
    tags=["ratio", "simplify", "proportion"],
    formula="a:b ÷ gcd(a,b) = simplest ratio",
    summary="Simplify a ratio to its lowest terms.",
    viz_template="viz/ratio.html",
)
def compute(a: float = 12, b: float = 18):
    a = int(a); b = int(b)
    g = gcd(a, b) or 1
    sa, sb = a // g, b // g
    return {
        "simplified": f"{sa}:{sb}",
        "a_simple": sa,
        "b_simple": sb,
        "series": [
            {"label": "a", "value": sa},
            {"label": "b", "value": sb},
        ],
    }
from core.faqs import load_sibling_faq
load_sibling_faq(__file__)