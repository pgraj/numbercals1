"""Real-world worked example: a projectile's impact angle from its horizontal travel and vertical drop, via inverse tangent (Forensics / Criminology)."""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="rw-bullet-trajectory",
    name="Impact angle of a trajectory",
    section="maths",
    sub="Forensics",
    topic="Real-World Trigonometry",
    order=0,
    summary=(
        "A worked real-world example: from the horizontal travel and vertical drop "
        "between two marks, inverse tangent recovers the angle at which a "
        "projectile struck — the geometry behind trajectory and impact-angle "
        "reconstruction — shown on an animated scene you can adjust."
    ),
    formula="impact angle = tan⁻¹(vertical drop / horizontal travel)",
    tags=["real life trigonometry", "forensics", "criminology", "impact angle", "trajectory", "inverse tangent", "worked example", "trigonometry", "A-Level", "ACARA Year 10"],
    viz_template="viz/rw-bullet-trajectory.html",
    scholar="hipparchus",
    related=['trig-inverse', 'trig-elevation-depression'],
)
def compute(horizontal=None, vertical_drop=None):
    try:
        def num(x, d=None):
            return d if (x is None or x == "") else float(x)
        horiz = num(horizontal, 3.0)   # horizontal travel along the floor, metres
        drop = num(vertical_drop, 1.2) # vertical drop from entry to impact, metres
        if horiz <= 0 or drop <= 0:
            return _err("Horizontal travel and vertical drop must both be greater than zero.")
        angle = math.degrees(math.atan2(drop, horiz))
        path = math.hypot(horiz, drop)
        steps = [
            {"label": "Reconstruct the path triangle",
             "math": r"\(\tan\theta = \dfrac{\text{vertical drop}}{\text{horizontal travel}}\)",
             "note": "From the two marks (entry and impact), the drop is opposite the impact angle and the horizontal travel is adjacent."},
            {"label": "Impact angle by inverse tangent",
             "math": r"\(\theta = \tan^{-1}\!\left(\dfrac{%s}{%s}\right) = %s^\circ\)" % (_fmt(drop), _fmt(horiz), _fmt(angle)),
             "note": "The angle below the horizontal at which the projectile struck."},
            {"label": "Straight-line path length",
             "math": r"\(\text{path} = \sqrt{%s^2 + %s^2} = %s\ \text{m}\)" % (_fmt(horiz), _fmt(drop), _fmt(path)),
             "note": "The actual line travelled between the two reference points."},
        ]
        return {
            "result": _fmt(angle),
            "horizontal": horiz, "vertical_drop": drop,
            "impact_angle": round(angle, 3), "path_length": round(path, 4),
            "steps": steps,
            "explanation": [
                {"heading": "The scenario",
                 "body": "An investigator marks where a projectile entered a wall and where "
                         "it finally struck, %s m further along and %s m lower. The angle of "
                         "that descent helps reconstruct where it was fired from." % (_fmt(horiz), _fmt(drop))},
                {"heading": "Inverse tangent recovers the angle",
                 "body": "The vertical drop and horizontal travel are the opposite and "
                         "adjacent sides of a right triangle, so their ratio is the tangent "
                         "of the impact angle. Arctan turns that ratio into the angle itself."},
                {"heading": "Why it matters",
                 "body": "Forensic teams use exactly this geometry for trajectory and "
                         "blood-spatter analysis — angles of impact place a shooter or "
                         "reconstruct events from physical marks alone."},
                {"heading": "Try it yourself",
                 "body": "A larger drop over the same horizontal travel gives a steeper "
                         "impact angle; a long, flat travel gives a shallow, grazing angle."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for the horizontal travel and vertical drop.")


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
