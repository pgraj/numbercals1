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
def compute(value=None, direction="deg2rad", mode="convert",
            radius=None, angle=None, angle_unit="rad"):
    try:
        mode = (mode or "convert").lower()
        if mode in ("arc", "sector"):
            return _arc_sector(mode, radius, angle, angle_unit)
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


def _ang_tex(deg, unit):
    """Angle as LaTeX in the chosen unit (radians = decimal)."""
    if unit == "rad":
        return ("%.4f" % math.radians(deg)).rstrip("0").rstrip(".") + r"\,\text{rad}"
    return _fmt(deg) + r"^\circ"


def _ang_plain(deg, unit):
    if unit == "rad":
        return ("%.4f" % math.radians(deg)).rstrip("0").rstrip(".") + " rad"
    return _fmt(deg) + "\u00b0"


def _arc_sector(mode, radius, angle, angle_unit):
    """Arc length s = rθ  or  sector area A = ½r²θ.  θ used in RADIANS internally."""
    if radius in (None, "") or angle in (None, ""):
        return _err("Enter both the radius and the angle.")
    try:
        r = float(radius)
        a_in = float(angle)
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for the radius and angle.")
    unit = "rad" if str(angle_unit) == "rad" else "deg"
    if r <= 0:
        return _err("The radius must be greater than zero.")
    # angle in degrees (for display) and radians (for the formula)
    deg = a_in if unit == "deg" else math.degrees(a_in)
    if deg <= 0:
        return _err("The angle must be greater than zero.")
    theta = math.radians(deg)          # radians used in the formula
    over = deg > 360.0                 # exceeds a full turn

    note_full = (" Note: this angle exceeds a full turn (360\u00b0 = 2\u03c0 rad), "
                 "so the arc wraps past the start point.") if over else ""

    if mode == "arc":
        s = r * theta
        steps = [
            {"label": ("Convert the angle to radians" if unit == "deg" else "Angle is already in radians"),
             "math": (r"\(\theta = %s^\circ \times \dfrac{\pi}{180} = %s\,\text{rad}\)" % (_fmt(deg), _fmt(theta))
                      if unit == "deg" else
                      r"\(\theta = %s\,\text{rad}\)" % _fmt(theta)),
             "note": "Arc length needs the angle in radians." + (" Degrees are converted with \u00d7\u03c0/180." if unit == "deg" else "")},
            {"label": "Apply s = r\u03b8",
             "math": r"\(s = r\theta = %s \times %s\)" % (_fmt(r), _fmt(theta)),
             "note": "Multiply the radius by the angle in radians." + note_full},
            {"label": "Arc length",
             "math": r"\(s \approx %s\)" % _fmt(s),
             "note": "In the same length units as the radius."},
        ]
        return {
            "result": _fmt(s), "result_decimal": round(s, 6),
            "mode": "arc", "radius": r, "angle_deg": deg, "angle_unit": unit,
            "radians": round(theta, 6), "arc_length": round(s, 6),
            "steps": steps,
            "explanation": [
                {"heading": "Arc length from the radian definition",
                 "body": "A radian is the angle whose arc equals the radius, so an "
                         "angle of \u03b8 radians sweeps an arc of \u03b8 radii: s = r\u03b8. "
                         "This only works when \u03b8 is measured in radians."},
                {"heading": "Why convert degrees first",
                 "body": "If the angle is given in degrees, change it to radians with "
                         "\u00d7\u03c0/180 before using s = r\u03b8; using degrees directly "
                         "would give the wrong length."},
            ],
            "disclaimer": DISCLAIMER,
        }
    else:  # sector
        area = 0.5 * r * r * theta
        steps = [
            {"label": ("Convert the angle to radians" if unit == "deg" else "Angle is already in radians"),
             "math": (r"\(\theta = %s^\circ \times \dfrac{\pi}{180} = %s\,\text{rad}\)" % (_fmt(deg), _fmt(theta))
                      if unit == "deg" else
                      r"\(\theta = %s\,\text{rad}\)" % _fmt(theta)),
             "note": "Sector area needs the angle in radians." + (" Degrees are converted with \u00d7\u03c0/180." if unit == "deg" else "")},
            {"label": "Apply A = \u00bdr\u00b2\u03b8",
             "math": r"\(A = \tfrac{1}{2}r^2\theta = \tfrac{1}{2}\times %s^2 \times %s\)" % (_fmt(r), _fmt(theta)),
             "note": "Half the radius squared, times the angle in radians." + note_full},
            {"label": "Sector area",
             "math": r"\(A \approx %s\)" % _fmt(area),
             "note": "In squared length units of the radius."},
        ]
        return {
            "result": _fmt(area), "result_decimal": round(area, 6),
            "mode": "sector", "radius": r, "angle_deg": deg, "angle_unit": unit,
            "radians": round(theta, 6), "sector_area": round(area, 6),
            "steps": steps,
            "explanation": [
                {"heading": "Sector area as a fraction of the circle",
                 "body": "A sector of angle \u03b8 radians is the fraction \u03b8/2\u03c0 of the "
                         "whole circle \u03c0r\u00b2, which simplifies to A = \u00bdr\u00b2\u03b8. As "
                         "with arc length, \u03b8 must be in radians."},
                {"heading": "Link to arc length",
                 "body": "Since s = r\u03b8, the sector area is also A = \u00bdrs \u2014 half the "
                         "radius times the arc length, the curved analogue of \u00bd\u00d7base\u00d7height."},
            ],
            "disclaimer": DISCLAIMER,
        }


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
