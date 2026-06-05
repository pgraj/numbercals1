"""Heron's formula — Triangles cluster of the Geometry section.

Area = sqrt(s(s-a)(s-b)(s-c)) with s = (a+b+c)/2. Finds a triangle's area from
its three side lengths alone — no angle, no height. This is fundamentally a
geometry result, which is why it lives here rather than under Trigonometry. Two
companion calculators show how the same formula is *derived* with trigonometry
(law of cosines) and with algebra (the Pythagorean theorem).
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="geo-heron",
    name="Heron's formula",
    section="maths",
    sub="Triangles",
    topic="Geometry",
    order=1,
    summary=(
        "Find the area of any triangle from its three side lengths alone using "
        "Heron's formula, the square root of s times s minus a times s minus b "
        "times s minus c, where s is the semi-perimeter, with the triangle drawn "
        "to scale and the area shaded."
    ),
    formula="Area = √(s(s−a)(s−b)(s−c)),  s = (a+b+c)/2",
    tags=[
        "heron's formula", "hero of alexandria", "area from three sides",
        "semi-perimeter", "SSS area", "geometry", "triangle area",
        "CBSE Class 9", "GCSE", "Common Core", "Singapore E-Math",
        "France Premiere", "Germany Klasse 10", "ACARA Year 10", "UAE Grade 10",
    ],
    viz_template="viz/geo-heron.html",
    scholar="hero-of-alexandria",
)
def compute(a=None, b=None, c=None):
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

        s = (a_ + b_ + c_) / 2
        area = math.sqrt(s * (s - a_) * (s - b_) * (s - c_))
        steps = [
            {"label": "Find the semi-perimeter",
             "math": r"\(s = \dfrac{a+b+c}{2} = \dfrac{%s+%s+%s}{2} = %s\)"
                     % (_fmt(a_), _fmt(b_), _fmt(c_), _fmt(s)),
             "note": "Half the total perimeter of the triangle."},
            {"label": "Apply Heron's formula",
             "math": r"\(\text{Area} = \sqrt{s(s-a)(s-b)(s-c)}\)",
             "note": "Only the three side lengths are needed — no angle required."},
            {"label": "Substitute",
             "math": r"\(= \sqrt{%s(%s)(%s)(%s)}\)"
                     % (_fmt(s), _fmt(s - a_), _fmt(s - b_), _fmt(s - c_)),
             "note": "Each bracket is the semi-perimeter minus one side."},
            {"label": "Evaluate",
             "math": r"\(\text{Area} = %s\)" % _fmt(area),
             "note": "For a 3-4-5 triangle this gives the familiar area of 6."},
        ]
        return {
            "result": _fmt(area),
            "a": a_, "b": b_, "c": c_, "s": round(s, 6), "area": round(area, 6),
            "steps": steps,
            "explanation": [
                {"heading": "A geometry result, not trigonometry",
                 "body": "Heron's formula needs no angle and no height — only the "
                         "three side lengths. That is what makes it a result of pure "
                         "geometry. It is ideal when you have measured all three "
                         "sides of a plot or shape but cannot easily measure an angle."},
                {"heading": "Where it comes from",
                 "body": "The formula is credited to Hero of Alexandria (about 60 AD), "
                         "though it may have been known to Archimedes earlier. It can "
                         "be derived using trigonometry (the law of cosines) or "
                         "algebra (the Pythagorean theorem) — see the two companion "
                         "calculators for those proofs."},
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
