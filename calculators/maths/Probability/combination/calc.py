"""Combination — maths > Probability. nCr = n! / (r!(n - r)!)  (order does not matter)."""
from core.registry import register
import math

@register(
    slug="combination",
    name="Combination Calculator",
    section="maths",
    sub="Probability",
    tags=["combination", "ncr", "choose", "combinatorics", "binomial"],
    formula="nCr = n! / (r! (n \u2212 r)!)",
    summary="How many unordered selections of r items can be drawn from n, where order does not matter.",
    viz_template="viz/combination.html",
)
def compute(n: float = 5, r: float = 2):
    try:
        N = int(n); R = int(r)
    except (TypeError, ValueError):
        return {"error": "Enter whole numbers."}
    if N < 0 or R < 0:
        return {"error": "n and r cannot be negative."}
    if R > N:
        return {"error": "r cannot be larger than n."}
    ncr = math.comb(N, R)
    steps = [
        {"label": "Formula", "math": r"\(^nC_r = \dfrac{n!}{r!\,(n-r)!}\)", "note": "Order does NOT matter here."},
        {"label": "Substitute", "math": r"\(\dfrac{" + str(N) + r"!}{" + str(R) + r"!\,(" + str(N - R) + r")!}\)", "note": "Your numbers."},
        {"label": "Result", "math": r"\(^{" + str(N) + r"}C_{" + str(R) + r"} = " + str(ncr) + r"\)", "note": "Number of unordered selections."},
    ]
    return {
        "result": str(N) + "C" + str(R) + " = " + str(ncr),
        "combinations": ncr, "n": N, "r": R, "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
