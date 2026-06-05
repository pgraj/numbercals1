"""Compass bearings — Right-Angle Trigonometry cluster.

Convert an east/north displacement into a three-figure compass bearing measured
clockwise from north (000°–360°), with the straight-line distance.
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-bearing-navigation",
    name="Compass bearings",
    section="maths",
    sub="Right-Angle Trigonometry",
    topic="Trigonometry",
    order=0,
    summary=(
        "Turn an east and north displacement into a three-figure compass bearing "
        "measured clockwise from north, plus the straight-line distance, shown on "
        "a compass rose with the bearing line and angle drawn from the start point."
    ),
    formula="bearing = (90° − atan2(N, E)) mod 360°",
    tags=[
        "bearings", "three-figure bearing", "compass", "navigation",
        "tangent", "trigonometry", "CBSE Class 10", "GCSE",
        "Common Core HSG-SRT", "Singapore Sec 3", "ACARA Year 9",
        "NSW Stage 5", "UAE Grade 9",
    ],
    viz_template="viz/trig-bearing-navigation.html",
)
def compute(east=None, north=None):
    try:
        def num(x):
            if x is None or x == "":
                return None
            return float(x)

        e, n = num(east), num(north)
        if e is None or n is None:
            return _err("Enter the east and north displacement components.")
        if e == 0 and n == 0:
            return _err("The start and end points are the same — no bearing.")

        # Bearing is clockwise from north. atan2(E, N) gives exactly that.
        bearing = math.degrees(math.atan2(e, n)) % 360
        distance = math.hypot(e, n)

        steps = [
            {"label": "Identify the components",
             "math": r"\(E = %s,\; N = %s\)" % (_fmt(e), _fmt(n)),
             "note": "East is the horizontal step, north is the vertical step (negatives go west/south)."},
            {"label": "Bearing clockwise from north",
             "math": r"\(\text{bearing} = \operatorname{atan2}(E, N) = \operatorname{atan2}(%s, %s)\)"
                     % (_fmt(e), _fmt(n)),
             "note": "Measured clockwise starting from due north (000°)."},
            {"label": "Write as three figures",
             "math": r"\(\text{bearing} = %s^\circ\)" % _fmt3(bearing),
             "note": "Bearings always use three digits, e.g. 045°, not 45°."},
            {"label": "Straight-line distance",
             "math": r"\(d = \sqrt{E^2 + N^2} = %s\)" % _fmt(distance),
             "note": "Pythagoras gives the direct distance between the two points."},
        ]
        return {
            "result": _fmt3(bearing) + "°",
            "bearing": round(bearing, 4), "distance": round(distance, 6),
            "east": e, "north": n,
            "steps": steps,
            "explanation": [
                {"heading": "What a three-figure bearing is",
                 "body": "A bearing describes direction as an angle measured clockwise "
                         "from north, written with three digits from 000° to 360°. "
                         "Due east is 090°, due south 180°, due west 270°."},
                {"heading": "From grid steps to a bearing",
                 "body": "Break the journey into how far east and how far north you "
                         "move, then the bearing comes from those two components and "
                         "the distance from Pythagoras — the heart of navigation."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for the displacement.")


def _err(msg):
    return {"error": msg, "steps": [], "disclaimer": DISCLAIMER}


def _fmt(x):
    if x is None:
        return ""
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")


def _fmt3(x):
    """Three-figure bearing formatting, e.g. 45 -> 045."""
    r = round(x, 1)
    whole = int(r)
    if abs(r - whole) < 1e-9:
        return "%03d" % whole
    return "%05.1f" % r  # e.g. 045.5


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
