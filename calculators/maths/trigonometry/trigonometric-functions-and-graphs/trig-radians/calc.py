"""Degrees & radians — Trigonometric Functions & Graphs cluster (Stage 2).

Convert between degrees and radians in either direction, giving the radian
answer as a multiple of pi where it is clean.
"""
import math
from fractions import Fraction

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-radians",
    name="Degrees & radians",
    section="maths",
    sub="Trigonometric Functions & Graphs",
    topic="Trigonometry",
    order=0,
    summary=(
        "Convert angles between degrees and radians in either direction, with the "
        "radian answer shown as a multiple of pi where it is exact, illustrated by "
        "a dual arc where both measures update together around the circle."
    ),
    formula="radians = degrees × π/180 · degrees = radians × 180/π",
    tags=[
        "radians", "degrees to radians", "radian measure", "pi radians",
        "arc length", "trigonometry", "CBSE Class 11", "A-Level",
        "Common Core HSF-TF", "Singapore A-Math", "France Premiere",
        "Germany Klasse 10", "ACARA Year 11", "UAE Grade 11",
    ],
    viz_template="viz/trig-radians.html",
)
def compute(value=None, direction="deg2rad"):
    try:
        if value is None or value == "":
            return _err("Enter a value to convert.")
        v = float(value)
        direction = (direction or "deg2rad").lower()

        if direction == "deg2rad":
            rad = math.radians(v)
            pretty = _as_pi_multiple(v)
            steps = [
                {"label": "Use the conversion factor",
                 "math": r"\(\text{radians} = \text{degrees} \times \dfrac{\pi}{180}\)",
                 "note": "A full turn is 360° = 2π radians, so 180° = π."},
                {"label": "Substitute",
                 "math": r"\(%s \times \dfrac{\pi}{180} = %s\)" % (_fmt(v), pretty),
                 "note": "Simplify the fraction of π where possible."},
                {"label": "Decimal value",
                 "math": r"\(\approx %s \text{ rad}\)" % _fmt(rad),
                 "note": "Useful when a calculator needs radian input."},
            ]
            return {
                "result": pretty, "result_decimal": round(rad, 6),
                "degrees": v, "radians": round(rad, 6), "direction": direction,
                "steps": steps, "explanation": _expl(), "disclaimer": DISCLAIMER,
            }
        elif direction == "rad2deg":
            deg = math.degrees(v)
            steps = [
                {"label": "Use the conversion factor",
                 "math": r"\(\text{degrees} = \text{radians} \times \dfrac{180}{\pi}\)",
                 "note": "The inverse of the degrees-to-radians factor."},
                {"label": "Substitute",
                 "math": r"\(%s \times \dfrac{180}{\pi} = %s^\circ\)" % (_fmt(v), _fmt(deg)),
                 "note": "Here the radian input is treated as a plain number."},
                {"label": "Result",
                 "math": r"\(%s^\circ\)" % _fmt(deg),
                 "note": "Multiples of π give round degree answers (π → 180°)."},
            ]
            return {
                "result": _fmt(deg) + "\u00b0", "result_decimal": round(deg, 6),
                "degrees": round(deg, 6), "radians": v, "direction": direction,
                "steps": steps, "explanation": _expl(), "disclaimer": DISCLAIMER,
            }
        else:
            return _err("Choose a direction: deg2rad or rad2deg.")
    except (TypeError, ValueError):
        return _err("Please enter a valid number.")


def _as_pi_multiple(deg):
    """Render deg×π/180 as a tidy multiple of π when the fraction is simple."""
    frac = Fraction(deg).limit_denominator(10**6) * Fraction(1, 180)
    n, d = frac.numerator, frac.denominator
    if n == 0:
        return "0"
    num = "" if n == 1 else ("-" if n == -1 else str(n))
    if d == 1:
        return (num + r"\pi") if num not in ("", "-") else (num + r"\pi")
    if num in ("", "-"):
        return r"%s\dfrac{\pi}{%d}" % (num, d)
    return r"\dfrac{%s\pi}{%d}" % (n, d)


def _expl():
    return [
        {"heading": "Why radians exist",
         "body": "A radian is the angle that wraps an arc equal in length to the "
                 "radius. Because it ties angle directly to arc length, radians make "
                 "the calculus and the wave formulas of trigonometry far cleaner than "
                 "degrees."},
        {"heading": "The key landmarks",
         "body": "Half a turn, 180°, is exactly π radians; a quarter turn, 90°, is "
                 "π/2; a full turn, 360°, is 2π. Memorising these makes most "
                 "conversions a quick mental step."},
    ]


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
