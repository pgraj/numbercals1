"""The unit circle — Trigonometric Functions & Graphs cluster (Stage 2).

For any angle, give the point (cos θ, sin θ) on the unit circle, the quadrant,
the reference angle, and exact surd values at the special angles. This is the
pivot concept: it links right-angle ratios (Stage 1) to the wave graphs and to
Stage 3's identities.

Accepts `angle_unit` ("deg"|"rad"): θ is READ in the chosen unit and DISPLAYED in
it (the step angle, the reference angle, and the result echo), while the geometry
and exact-value lookup work internally in degrees. The unit circle is where
radians is most naturally taught, so the toggle matters here.
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)

# Exact-value lookup at the common special angles (degrees -> LaTeX surd strings).
_EXACT = {
    0:   ("1", "0", "0"),
    30:  (r"\tfrac{\sqrt{3}}{2}", r"\tfrac{1}{2}", r"\tfrac{\sqrt{3}}{3}"),
    45:  (r"\tfrac{\sqrt{2}}{2}", r"\tfrac{\sqrt{2}}{2}", "1"),
    60:  (r"\tfrac{1}{2}", r"\tfrac{\sqrt{3}}{2}", r"\sqrt{3}"),
    90:  ("0", "1", r"\text{undefined}"),
    120: (r"-\tfrac{1}{2}", r"\tfrac{\sqrt{3}}{2}", r"-\sqrt{3}"),
    135: (r"-\tfrac{\sqrt{2}}{2}", r"\tfrac{\sqrt{2}}{2}", "-1"),
    150: (r"-\tfrac{\sqrt{3}}{2}", r"\tfrac{1}{2}", r"-\tfrac{\sqrt{3}}{3}"),
    180: ("-1", "0", "0"),
    210: (r"-\tfrac{\sqrt{3}}{2}", r"-\tfrac{1}{2}", r"\tfrac{\sqrt{3}}{3}"),
    225: (r"-\tfrac{\sqrt{2}}{2}", r"-\tfrac{\sqrt{2}}{2}", "1"),
    240: (r"-\tfrac{1}{2}", r"-\tfrac{\sqrt{3}}{2}", r"\sqrt{3}"),
    270: ("0", "-1", r"\text{undefined}"),
    300: (r"\tfrac{1}{2}", r"-\tfrac{\sqrt{3}}{2}", r"-\sqrt{3}"),
    315: (r"\tfrac{\sqrt{2}}{2}", r"-\tfrac{\sqrt{2}}{2}", "-1"),
    330: (r"\tfrac{\sqrt{3}}{2}", r"-\tfrac{1}{2}", r"-\tfrac{\sqrt{3}}{3}"),
    360: ("1", "0", "0"),
}


@register(
    slug="trig-unit-circle",
    name="The unit circle",
    section="maths",
    sub="Trigonometric Functions & Graphs",
    topic="Trigonometry",
    order=0,
    summary=(
        "Explore the unit circle: for any angle it gives the point (cos theta, "
        "sin theta), the quadrant and reference angle, and exact surd values at "
        "the special angles, in degrees or radians, with an animated point whose "
        "sine and cosine projections are drawn live alongside the right-triangle "
        "interpretation."
    ),
    formula="P = (cos θ, sin θ) on the circle of radius 1",
    tags=[
        "unit circle", "cos theta sin theta", "radians", "reference angle",
        "quadrants", "special angles", "trigonometry", "CBSE Class 11",
        "A-Level", "Common Core HSF-TF", "Singapore A-Math", "France Premiere",
        "Germany Klasse 10", "ACARA Year 11", "UAE Grade 11",
    ],
    viz_template="viz/trig-unit-circle.html",
)
def compute(angle_deg=None, angle_unit="deg"):
    try:
        unit = "rad" if str(angle_unit) == "rad" else "deg"
        if angle_deg is None or angle_deg == "":
            lim = "in degrees" if unit == "deg" else "in radians"
            return _err("Enter an angle %s." % lim)
        a_in = float(angle_deg)
        # interpret the entered angle in the chosen unit; work in degrees inside
        a = a_in if unit == "deg" else math.degrees(a_in)
        th = math.radians(a)
        cos_v = math.cos(th)
        sin_v = math.sin(th)
        tan_v = None if abs(cos_v) < 1e-12 else math.tan(th)

        a_norm = a % 360
        if a_norm in (0, 90, 180, 270, 360):
            quadrant = "on an axis"
        elif 0 < a_norm < 90:
            quadrant = "Quadrant I (+, +)"
        elif 90 < a_norm < 180:
            quadrant = "Quadrant II (\u2212, +)"
        elif 180 < a_norm < 270:
            quadrant = "Quadrant III (\u2212, \u2212)"
        else:
            quadrant = "Quadrant IV (+, \u2212)"

        # reference angle (acute angle to the x-axis)
        r = a_norm % 180
        ref = r if r <= 90 else 180 - r
        ref = min(ref, 180 - ref) if ref > 90 else ref

        steps = [
            {"label": "Place the angle on the circle",
             "math": r"\(\theta = %s\)" % _ang(a, unit),
             "note": "Measured anticlockwise from the positive x-axis on a circle of radius 1."},
            {"label": "Read the coordinates",
             "math": r"\(P = (\cos\theta,\ \sin\theta) = (%s,\ %s)\)" % (_fmt(cos_v), _fmt(sin_v)),
             "note": "The x-coordinate is the cosine; the y-coordinate is the sine."},
            {"label": "Quadrant & signs",
             "math": r"\(\text{%s}\)" % quadrant,
             "note": "The signs of cos and sin follow the quadrant (ASTC)."},
        ]
        key = int(round(a_norm))
        if key in _EXACT and abs(a_norm - key) < 1e-9:
            ec, es, et = _EXACT[key]
            steps.append({
                "label": "Exact values (special angle)",
                "math": r"\(\cos = %s,\ \sin = %s,\ \tan = %s\)" % (ec, es, et),
                "note": "These exact surd values are worth memorising."})

        return {
            "result": "(%s, %s)" % (_fmt(cos_v), _fmt(sin_v)),
            "angle": a,
            "angle_norm": a_norm,
            "angle_unit": unit,
            "angle_display": _disp(a, unit),
            "cos": round(cos_v, 6),
            "sin": round(sin_v, 6),
            "tan": (round(tan_v, 6) if tan_v is not None else None),
            "quadrant": quadrant,
            "reference": round(ref, 4),
            "reference_display": _disp(ref, unit),
            "steps": steps,
            "explanation": [
                {"heading": "Why the circle has radius 1",
                 "body": "On a circle of radius 1, the right triangle formed by an "
                         "angle has a hypotenuse of 1, so the opposite side equals "
                         "sin θ and the adjacent side equals cos θ directly. The "
                         "point on the circle is therefore exactly (cos θ, sin θ)."},
                {"heading": "Degrees and radians",
                 "body": "The unit circle is where radians come into their own: a "
                         "full turn is 2π radians, a right angle is π/2, and the arc "
                         "length equals the angle in radians. Switch the toggle to "
                         "see the same point described either way."},
                {"heading": "Beyond the first quadrant",
                 "body": "Unlike right-angle trig, the unit circle defines sine and "
                         "cosine for every angle, including those past 90° and "
                         "negative ones. The signs change by quadrant, which is what "
                         "makes the wave graphs rise and fall."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        lim = "degrees" if unit == "deg" else "radians"
        return _err("Please enter a valid number of %s." % lim)


def _ang(deg, unit):
    """LaTeX angle in the chosen unit (for step math)."""
    if unit == "rad":
        return _fmt(math.radians(deg)) + r"\,\text{rad}"
    return _fmt(deg) + r"^\circ"


def _disp(deg, unit):
    """Plain-text angle in the chosen unit."""
    if unit == "rad":
        return _fmt(math.radians(deg)) + " rad"
    return _fmt(deg) + "\u00b0"


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
