"""Real-world worked example: measuring a tree's height (Heights & Distances).

A surveyor stands a known distance from a tree and measures the angle of
elevation to its top. The height follows from tan θ = opposite / adjacent, with
the surveyor's eye height added back. Pre-set to a realistic scenario; the
distance, angle and eye height are live so the reader can explore "what if".

This is a *scenario* wrapper around the same maths as the Angles of Elevation
calculator — it links back to the calculators it exercises via `links_to`.
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="rw-tree-height",
    name="Measuring a tree's height",
    section="real-world",
    sub="Heights & Distances",
    topic="Real-World Trigonometry",
    order=0,
    summary=(
        "A worked real-world example: a surveyor standing a known distance from a "
        "tree measures the angle of elevation to its top, then uses tan theta = "
        "height over distance (adding their own eye height) to find how tall the "
        "tree is — shown on an animated scene with sliders to explore."
    ),
    formula="height = distance × tan θ + eye height",
    tags=[
        "real life trigonometry", "angle of elevation", "tree height", "tangent",
        "surveying", "worked example", "heights and distances", "trigonometry",
        "CBSE Class 10", "GCSE", "ACARA Year 9", "Common Core HSG-SRT",
    ],
    viz_template="viz/rw-tree-height.html",
    scholar="hipparchus",
    related=['trig-elevation-depression', 'trig-sin-cos-tan'],
)
def compute(distance=None, angle_deg=None, eye_height=None):
    try:
        def num(x, default=None):
            if x is None or x == "":
                return default
            return float(x)

        d = num(distance, 25.0)
        a = num(angle_deg, 32.0)
        eye = num(eye_height, 1.6)

        if d <= 0:
            return _err("The distance to the tree must be greater than zero.")
        if not (0 < a < 90):
            return _err("The angle of elevation must be between 0° and 90°.")
        if eye < 0:
            return _err("Eye height cannot be negative.")

        above_eye = d * math.tan(math.radians(a))
        total = above_eye + eye

        steps = [
            {"label": "Picture the right triangle",
             "math": r"\(\tan\theta = \dfrac{\text{opposite}}{\text{adjacent}} = \dfrac{\text{height above eye}}{\text{distance}}\)",
             "note": "The horizontal distance is the adjacent side; the part of the tree above eye level is the opposite side."},
            {"label": "Substitute the measurements",
             "math": r"\(\tan %s^\circ = \dfrac{h}{%s}\)" % (_fmt(a), _fmt(d)),
             "note": "Angle of elevation %s°, measured %s m from the trunk." % (_fmt(a), _fmt(d))},
            {"label": "Solve for the height above eye level",
             "math": r"\(h = %s \times \tan %s^\circ = %s\ \text{m}\)" % (_fmt(d), _fmt(a), _fmt(above_eye)),
             "note": "This is how far the treetop rises above the surveyor's eye."},
            {"label": "Add the surveyor's eye height",
             "math": r"\(\text{tree height} = %s + %s = %s\ \text{m}\)" % (_fmt(above_eye), _fmt(eye), _fmt(total)),
             "note": "The instrument sits %s m above the ground, so add it back to reach the true total." % _fmt(eye)},
        ]
        return {
            "result": _fmt(total),
            "distance": d, "angle_deg": a, "eye_height": eye,
            "above_eye": round(above_eye, 4), "total_height": round(total, 4),
            "steps": steps,
            "explanation": [
                {"heading": "The scenario",
                 "body": "A surveyor stands %s m from the base of a tree and tilts a "
                         "clinometer up to the very top, reading an angle of %s°. Their "
                         "eye (the instrument) is %s m above the ground. The line of "
                         "sight, the horizontal, and the tree form a right triangle."
                         % (_fmt(d), _fmt(a), _fmt(eye))},
                {"heading": "Why tangent",
                 "body": "Tangent links exactly the two sides we have and want: the "
                         "horizontal distance (adjacent, known) and the height above "
                         "eye level (opposite, unknown). Multiplying the distance by "
                         "tan θ gives that height directly."},
                {"heading": "Don't forget eye height",
                 "body": "The triangle only reaches from eye level upward, so it finds "
                         "the height above the instrument — not the ground. Adding the "
                         "surveyor's eye height gives the tree's true total height. It is "
                         "a small step that students often miss."},
                {"heading": "Try it yourself",
                 "body": "Drag the angle slider: standing in the same spot, a taller "
                         "tree needs a steeper look-up. Move closer (smaller distance) "
                         "and the same tree gives a larger angle — that is how the maths "
                         "mirrors real life."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for the distance, angle and eye height.")


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
