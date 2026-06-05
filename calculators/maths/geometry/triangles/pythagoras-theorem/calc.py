"""Pythagoras' theorem calculator — Triangles cluster of the Geometry section.

Solve any one side of a right-angled triangle given the other two:
  - solve_for="c"      -> hypotenuse  c = sqrt(a^2 + b^2)
  - solve_for="a"/"b"  -> a leg       leg = sqrt(c^2 - other^2)

The theorem is fundamentally a result of Euclidean geometry (a relation among
the three sides of a right triangle, with no angle involved), so it lives in the
Geometry section. Its animation shows the two small squares (a^2, b^2) visibly
summing to the big square (c^2).
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="geo-pythagoras",
    name="Pythagoras' theorem",
    section="maths",
    sub="Triangles",
    topic="Geometry",
    order=0,
    summary=(
        "Find the missing side of a right-angled triangle using Pythagoras' "
        "theorem, a squared plus b squared equals c squared, with full working "
        "and a visual proof that the two smaller squares add up to the largest."
    ),
    formula="a² + b² = c²",
    tags=[
        "pythagoras", "pythagorean theorem", "right triangle", "hypotenuse",
        "geometry", "CBSE Class 8", "GCSE", "KS3", "Common Core Grade 8",
        "Singapore Sec 2", "France 4e", "Germany Klasse 9", "ACARA Year 9",
        "NSW Stage 5", "UAE Grade 8",
    ],
    viz_template="viz/geo-pythagoras.html",
    scholar="pythagoras",
)
def compute(a=None, b=None, c=None, solve_for="c"):
    try:
        solve_for = (solve_for or "c").strip().lower()

        def num(x):
            if x is None or x == "":
                return None
            return float(x)

        a = num(a)
        b = num(b)
        c = num(c)

        if solve_for == "c":
            if a is None or b is None:
                return _err("Enter both legs a and b to find the hypotenuse c.")
            if a <= 0 or b <= 0:
                return _err("Side lengths must be greater than zero.")
            c_val = math.hypot(a, b)
            steps = [
                {"label": "Write Pythagoras' theorem",
                 "math": r"\(a^2 + b^2 = c^2\)",
                 "note": "The square on the hypotenuse equals the sum of the squares on the two legs."},
                {"label": "Substitute the two legs",
                 "math": r"\(%s^2 + %s^2 = c^2\)" % (_fmt(a), _fmt(b)),
                 "note": "a = %s, b = %s." % (_fmt(a), _fmt(b))},
                {"label": "Square each leg and add",
                 "math": r"\(%s + %s = c^2\)" % (_fmt(a * a), _fmt(b * b)),
                 "note": "%s + %s = %s." % (_fmt(a * a), _fmt(b * b), _fmt(a * a + b * b))},
                {"label": "Take the square root",
                 "math": r"\(c = \sqrt{%s} = %s\)" % (_fmt(a * a + b * b), _fmt(c_val)),
                 "note": "The hypotenuse is the longest side, opposite the right angle."},
            ]
            return _ok(a=a, b=b, c=c_val, solved="c", result=c_val, steps=steps)

        elif solve_for in ("a", "b"):
            # Need the hypotenuse c and the other leg.
            other = b if solve_for == "a" else a
            if c is None or other is None:
                return _err("To find a leg, enter the hypotenuse c and the other leg.")
            if c <= 0 or other <= 0:
                return _err("Side lengths must be greater than zero.")
            if c <= other:
                return _err("The hypotenuse c must be longer than the other leg.")
            leg = math.sqrt(c * c - other * other)
            steps = [
                {"label": "Rearrange for a leg",
                 "math": r"\(\text{leg} = \sqrt{c^2 - \text{other}^2}\)",
                 "note": "Subtract the known leg's square from the hypotenuse's square, then take the root."},
                {"label": "Substitute the known sides",
                 "math": r"\(\text{leg} = \sqrt{%s^2 - %s^2}\)" % (_fmt(c), _fmt(other)),
                 "note": "c = %s, other leg = %s." % (_fmt(c), _fmt(other))},
                {"label": "Square and subtract",
                 "math": r"\(\text{leg} = \sqrt{%s - %s} = \sqrt{%s}\)"
                         % (_fmt(c * c), _fmt(other * other), _fmt(c * c - other * other)),
                 "note": "%s − %s = %s." % (_fmt(c * c), _fmt(other * other), _fmt(c * c - other * other))},
                {"label": "Take the square root",
                 "math": r"\(\text{leg} = %s\)" % _fmt(leg),
                 "note": "This is the length of the missing leg."},
            ]
            if solve_for == "a":
                return _ok(a=leg, b=other, c=c, solved="a", result=leg, steps=steps)
            else:
                return _ok(a=other, b=leg, c=c, solved="b", result=leg, steps=steps)

        else:
            return _err("Choose which side to solve for: a, b, or c.")

    except (TypeError, ValueError):
        return _err("Please enter valid numbers for the side lengths.")


def _ok(a, b, c, solved, result, steps):
    return {
        "result": round(result, 6),
        "result_label": {"a": "Leg a", "b": "Leg b", "c": "Hypotenuse c"}[solved],
        "a": round(a, 6),
        "b": round(b, 6),
        "c": round(c, 6),
        "solved": solved,
        "steps": steps,
        "explanation": [
            {"heading": "Why it works",
             "body": "In a right-angled triangle, the area of the square drawn on "
                     "the hypotenuse exactly equals the combined area of the squares "
                     "drawn on the two shorter sides. The animation shows the two "
                     "small squares filling and matching the large one."},
            {"heading": "Naming the sides",
             "body": "The hypotenuse (c) is always the longest side and sits opposite "
                     "the right angle. The other two sides (a and b) are the legs, "
                     "which meet at the right angle."},
        ],
        "disclaimer": DISCLAIMER,
    }


def _err(msg):
    return {"error": msg, "steps": [], "disclaimer": DISCLAIMER}


def _fmt(x):
    """Compact number formatting: integers without a trailing .0, else up to 4 dp."""
    if x is None:
        return ""
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
