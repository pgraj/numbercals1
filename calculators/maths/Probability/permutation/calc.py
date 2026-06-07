"""Permutation — maths > Probability. nPr = n! / (n - r)!  (order matters)."""
from core.registry import register
import math

@register(
    slug="permutation",
    name="Permutation Calculator",
    section="maths",
    sub="Probability",
    tags=["permutation", "npr", "arrangements", "order", "combinatorics"],
    formula="nPr = n! / (n \u2212 r)!",
    summary="How many ordered arrangements of r items can be drawn from n, where order matters.",
    viz_template="viz/permutation.html",
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
    npr = math.factorial(N) // math.factorial(N - R)
    steps = [
        {"label": "Formula", "math": r"\(^nP_r = \dfrac{n!}{(n-r)!}\)", "note": "Order matters here."},
        {"label": "Substitute", "math": r"\(\dfrac{" + str(N) + r"!}{(" + str(N) + r"-" + str(R) + r")!} = \dfrac{" + str(N) + r"!}{" + str(N - R) + r"!}\)", "note": "Cancel the common factorial."},
        {"label": "Result", "math": r"\(^{" + str(N) + r"}P_{" + str(R) + r"} = " + str(npr) + r"\)", "note": "Number of ordered arrangements."},
    ]
    return {
        "result": str(N) + "P" + str(R) + " = " + str(npr),
        "permutations": npr, "n": N, "r": R, "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
