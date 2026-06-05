"""Heron's formula via algebra (the Pythagorean theorem) — Algebra topic.

A companion to the Geometry Heron calculator. Drops an altitude to split the
triangle into two right triangles, uses the Pythagorean theorem to locate the
foot of the altitude and find the height, then area = ½·base·height. This is the
algebraic proof (similar to Raifaizen's) given on Wikipedia, and it confirms the
result matches Heron's square-root formula.
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="heron-algebraic",
    name="Heron's formula via the Pythagorean theorem",
    section="maths",
    sub="Algebra",
    topic="Algebra",
    order=0,
    summary=(
        "See how Heron's area formula is derived with algebra and the Pythagorean "
        "theorem: drop a height onto the base, use Pythagoras to find where it "
        "lands and how tall it is, then one half base times height — shown to "
        "equal Heron's square-root formula exactly."
    ),
    formula="d = (a²−b²+c²)/(2c),  h = √(a²−d²),  Area = ½·c·h = √(s(s−a)(s−b)(s−c))",
    tags=[
        "heron's formula", "pythagorean theorem", "algebraic proof", "triangle area",
        "difference of squares", "algebra", "derivation", "CBSE Class 9", "GCSE",
        "Common Core", "Singapore E-Math", "France Seconde", "Germany Klasse 9",
        "ACARA Year 10", "UAE Grade 9",
    ],
    viz_template="viz/heron-algebraic.html",
    scholar="hero-of-alexandria",
)
def compute(a=None, b=None, c=None):
    """Sides labelled so c is the base; the altitude h is dropped onto c.
    a is the side meeting the base at the right end, b at the left end."""
    try:
        def num(x):
            if x is None or x == "":
                return None
            return float(x)

        a_, b_, c_ = num(a), num(b), num(c)
        if a_ is None or b_ is None or c_ is None:
            return _err("Enter all three side lengths.")
        if a_ <= 0 or b_ <= 0 or c_ <= 0:
            return _err("Side lengths must be greater than zero.")
        if a_ + b_ <= c_ or a_ + c_ <= b_ or b_ + c_ <= a_:
            return _err("Those side lengths cannot form a triangle (triangle inequality).")

        # Foot of altitude from the apex onto base c, measured from the left vertex.
        # Using a^2 - d'^2 = h^2 = b^2 - d^2 with d + d' = c  ->  d = (b^2 - a^2 + c^2)/(2c)
        d = (b_ * b_ - a_ * a_ + c_ * c_) / (2 * c_)
        h_sq = b_ * b_ - d * d
        h = math.sqrt(h_sq) if h_sq > 0 else 0.0
        area_alg = 0.5 * c_ * h

        s = (a_ + b_ + c_) / 2
        area_heron = math.sqrt(s * (s - a_) * (s - b_) * (s - c_))

        steps = [
            {"label": "Drop a height onto the base",
             "math": r"\(\text{base} = c = %s\)" % _fmt(c_),
             "note": "The altitude h from the opposite vertex splits the triangle into two right triangles."},
            {"label": "Locate the foot with Pythagoras",
             "math": r"\(d = \dfrac{b^2 - a^2 + c^2}{2c} = %s\)" % _fmt(d),
             "note": "Both right triangles share the height, which lets us solve for the foot position d."},
            {"label": "Find the height",
             "math": r"\(h = \sqrt{b^2 - d^2} = \sqrt{%s - %s} = %s\)"
                     % (_fmt(b_ * b_), _fmt(d * d), _fmt(h)),
             "note": "Pythagoras in the left right-triangle gives the height."},
            {"label": "Area, and compare with Heron",
             "math": r"\(\tfrac{1}{2}ch = %s \quad=\quad \sqrt{s(s-a)(s-b)(s-c)} = %s\)"
                     % (_fmt(area_alg), _fmt(area_heron)),
             "note": "Expanding ½·c·√(b²−d²) with the difference-of-squares identity yields Heron's formula exactly."},
        ]
        return {
            "result": _fmt(area_alg),
            "a": a_, "b": b_, "c": c_,
            "foot_d": round(d, 6), "height": round(h, 6),
            "area_alg": round(area_alg, 6), "area_heron": round(area_heron, 6),
            "match": abs(area_alg - area_heron) < 1e-6,
            "steps": steps,
            "explanation": [
                {"heading": "Pythagoras does the work",
                 "body": "Dropping the altitude creates two right triangles that "
                         "share the same height. Writing Pythagoras for each and "
                         "subtracting eliminates the height long enough to find where "
                         "the altitude lands; then Pythagoras again gives the height "
                         "itself. No trigonometry is used anywhere."},
                {"heading": "From height-area to Heron",
                 "body": "Substituting the height into ½·base·height and repeatedly "
                         "applying the difference-of-squares identity reorganises the "
                         "expression into the symmetric product s(s−a)(s−b)(s−c) under "
                         "a square root — Heron's formula, obtained purely "
                         "algebraically."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for the sides.")


def _err(msg):
    return {"error": msg, "steps": [], "disclaimer": DISCLAIMER}


def _fmt(x):
    if x is None:
        return ""
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
