"""Real-world worked example: an aircraft's altitude and slant range from a ground-measured angle of elevation (Navigation / Aviation)."""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="rw-plane-altitude",
    name="Tracking an aircraft's altitude",
    section="real-world",
    sub="Navigation & Aviation",
    topic="Real-World Trigonometry",
    order=0,
    summary=(
        "A worked real-world example: a ground controller measures the angle of "
        "elevation to an aircraft a known horizontal distance away, then uses "
        "tangent to find its altitude and cosine to find the slant (radar) range "
        "— shown on an animated sky scene you can adjust."
    ),
    formula="altitude = ground distance × tan θ",
    tags=["real life trigonometry", "aviation", "angle of elevation", "altitude", "radar", "navigation", "tangent", "worked example", "trigonometry", "ACARA Year 10", "GCSE"],
    viz_template="viz/rw-plane-altitude.html",
    scholar="hipparchus",
    related=['trig-elevation-depression', 'trig-bearing-navigation'],
)
def compute(distance=None, angle_deg=None):
    try:
        def num(x, d=None):
            return d if (x is None or x == "") else float(x)
        ground = num(distance, 12000.0)   # horizontal ground distance, metres
        ang = num(angle_deg, 7.0)         # angle of elevation from the controller
        if ground <= 0:
            return _err("The ground distance must be greater than zero.")
        if not (0 < ang < 90):
            return _err("The angle of elevation must be between 0° and 90°.")
        altitude = ground * math.tan(math.radians(ang))
        slant = ground / math.cos(math.radians(ang))
        steps = [
            {"label": "Set up the right triangle",
             "math": r"\(\tan\theta = \dfrac{\text{altitude}}{\text{ground distance}}\)",
             "note": "The aircraft's altitude is opposite the elevation angle; the ground distance is adjacent."},
            {"label": "Solve for altitude",
             "math": r"\(\text{altitude} = %s \times \tan %s^\circ = %s\ \text{m}\)" % (_fmt(ground), _fmt(ang), _fmt(altitude)),
             "note": "Altitude above the ground station."},
            {"label": "Slant range (line-of-sight distance)",
             "math": r"\(\text{slant} = \dfrac{%s}{\cos %s^\circ} = %s\ \text{m}\)" % (_fmt(ground), _fmt(ang), _fmt(slant)),
             "note": "Cosine gives the straight-line radar distance to the plane."},
        ]
        return {
            "result": _fmt(altitude),
            "distance": ground, "angle_deg": ang,
            "altitude": round(altitude, 3), "slant": round(slant, 3),
            "steps": steps,
            "explanation": [
                {"heading": "The scenario",
                 "body": "A ground controller %s m (horizontally) from a point below an "
                         "aircraft measures its angle of elevation as %s°. From just that "
                         "angle and distance, trigonometry recovers the plane's altitude "
                         "and its straight-line distance." % (_fmt(ground), _fmt(ang))},
                {"heading": "Two ratios, two answers",
                 "body": "Tangent (opposite over adjacent) gives the altitude; cosine "
                         "(adjacent over hypotenuse) gives the slant range — the actual "
                         "line-of-sight distance a radar would report."},
                {"heading": "Why it matters",
                 "body": "Air-traffic control, radar and missile tracking all turn a "
                         "measured angle and a known ground distance into height and "
                         "range. The same triangle scales from a model rocket to a jet."},
                {"heading": "Try it yourself",
                 "body": "Lower the angle and watch the plane sit lower and further out; "
                         "raise it and the aircraft climbs steeply overhead."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for the distance and angle.")


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
