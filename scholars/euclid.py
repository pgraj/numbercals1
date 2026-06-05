"""Euclid of Alexandria — verified via Wolfram MathWorld / Wikipedia.
Linked to GCD and LCM (Elements Book VII, c. 300 BC)."""
from core.registry import register_scholar

register_scholar(
    slug="euclid", name="Euclid of Alexandria", era="c. 300 BC",
    field_of="Mathematics, geometry, number theory",
    blurb=("Greek mathematician whose Elements set out the algorithm for the "
           "greatest common divisor (Book VII) — the basis of GCD and, via "
           "lcm(a,b) = a·b / gcd(a,b), the least common multiple."),
    source_name="Wolfram MathWorld — Euclidean Algorithm",
    source_url="https://mathworld.wolfram.com/EuclideanAlgorithm.html",
)
