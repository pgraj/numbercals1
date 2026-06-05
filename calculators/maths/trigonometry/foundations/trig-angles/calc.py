"""Angles & angle types — Foundations cluster of the Trigonometry topic.

Classify an angle as acute, right, obtuse, straight, reflex, or a full turn,
and report its complement and supplement where they exist.
"""
from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-angles",
    name="Angles & angle types",
    section="maths",
    sub="Foundations",
    topic="Trigonometry",
    order=0,
    summary=(
        "Classify any angle as acute, right, obtuse, straight, or reflex, and "
        "find its complement and supplement, with a live protractor dial that "
        "sweeps to the angle you enter and names its type instantly."
    ),
    formula="acute < 90° · right = 90° · obtuse 90–180° · straight = 180° · reflex 180–360°",
    tags=[
        "angles", "acute angle", "obtuse angle", "reflex angle", "angle types",
        "complementary angles", "supplementary angles", "trigonometry",
        "CBSE Class 7", "KS3", "Common Core Grade 4", "Singapore Sec 1",
        "France 6e", "Germany Klasse 6", "ACARA Year 5", "UAE Grade 5",
    ],
    viz_template="viz/trig-angles.html",
)
def compute(angle_deg=None):
    try:
        if angle_deg is None or angle_deg == "":
            return _err("Enter an angle in degrees.")
        a = float(angle_deg)
        if a < 0 or a > 360:
            return _err("Enter an angle between 0° and 360°.")

        if a == 0 or a == 360:
            kind = "full turn" if a == 360 else "zero angle"
        elif a < 90:
            kind = "acute"
        elif a == 90:
            kind = "right"
        elif a < 180:
            kind = "obtuse"
        elif a == 180:
            kind = "straight"
        else:
            kind = "reflex"

        complement = 90 - a if 0 < a < 90 else None
        supplement = 180 - a if 0 < a < 180 else None

        steps = [
            {"label": "Read the angle",
             "math": r"\(\theta = %s^\circ\)" % _fmt(a),
             "note": "Compare it against the key boundaries 90°, 180°, and 360°."},
            {"label": "Classify the type",
             "math": r"\(\text{type} = \text{%s}\)" % kind,
             "note": _kind_note(kind)},
        ]
        if complement is not None:
            steps.append({"label": "Complement (adds to 90°)",
                          "math": r"\(90^\circ - %s^\circ = %s^\circ\)" % (_fmt(a), _fmt(complement)),
                          "note": "Two angles are complementary when they sum to 90°."})
        if supplement is not None:
            steps.append({"label": "Supplement (adds to 180°)",
                          "math": r"\(180^\circ - %s^\circ = %s^\circ\)" % (_fmt(a), _fmt(supplement)),
                          "note": "Two angles are supplementary when they sum to 180°."})

        return {
            "result": _fmt(a) + "° is " + kind,
            "angle": a,
            "kind": kind,
            "complement": complement,
            "supplement": supplement,
            "steps": steps,
            "explanation": [
                {"heading": "The five everyday types",
                 "body": "Acute angles are smaller than 90°, a right angle is exactly "
                         "90°, obtuse angles fall between 90° and 180°, a straight "
                         "angle is exactly 180°, and reflex angles are larger than "
                         "180° but less than 360°."},
                {"heading": "Complement vs supplement",
                 "body": "A complement is what you add to reach 90°; a supplement is "
                         "what you add to reach 180°. Only acute angles have a "
                         "complement, and only angles below 180° have a supplement."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter a valid number of degrees.")


def _kind_note(kind):
    return {
        "acute": "An acute angle is less than 90°.",
        "right": "A right angle is exactly 90° — the square corner.",
        "obtuse": "An obtuse angle is between 90° and 180°.",
        "straight": "A straight angle is exactly 180° — a straight line.",
        "reflex": "A reflex angle is greater than 180° and less than 360°.",
        "zero angle": "A zero angle has no opening.",
        "full turn": "A full turn is one complete revolution, 360°.",
    }.get(kind, "")


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
