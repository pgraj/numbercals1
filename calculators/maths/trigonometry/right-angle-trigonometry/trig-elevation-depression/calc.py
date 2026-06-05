"""Angles of elevation & depression — Right-Angle Trigonometry cluster.

Solve the classic height/distance/angle triangle using tanθ = height / distance.
Given any two of {angle, height, distance}, find the third.
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-elevation-depression",
    name="Angles of elevation & depression",
    section="maths",
    sub="Right-Angle Trigonometry",
    topic="Trigonometry",
    order=0,
    summary=(
        "Solve angle-of-elevation and angle-of-depression problems linking a "
        "height, a horizontal distance, and the viewing angle with tan θ = "
        "height ÷ distance, shown on a scene with an observer, an object, and "
        "the angle arc."
    ),
    formula="tan θ = height / distance",
    tags=[
        "angle of elevation", "angle of depression", "tangent", "height",
        "distance", "right triangle", "trigonometry", "CBSE Class 10", "GCSE",
        "Common Core HSG-SRT", "Singapore Sec 3", "France 3e",
        "Germany Klasse 9", "ACARA Year 9", "NSW Stage 5", "UAE Grade 9",
    ],
    viz_template="viz/trig-elevation-depression.html",
)
def compute(angle_deg=None, height=None, distance=None, find="height"):
    try:
        def num(x):
            if x is None or x == "":
                return None
            return float(x)

        angle = num(angle_deg)
        height = num(height)
        distance = num(distance)
        find = (find or "height").lower()

        if find == "height":
            if angle is None or distance is None:
                return _err("To find the height, enter the angle and the distance.")
            if not (0 < angle < 90):
                return _err("Enter an angle strictly between 0° and 90°.")
            if distance <= 0:
                return _err("Distance must be greater than zero.")
            height = distance * math.tan(math.radians(angle))
            steps = [
                {"label": "Set up the ratio",
                 "math": r"\(\tan\theta = \dfrac{\text{height}}{\text{distance}}\)",
                 "note": "The angle sits at the observer; height is vertical, distance horizontal."},
                {"label": "Rearrange for height",
                 "math": r"\(\text{height} = \text{distance}\,\tan\theta = %s\,\tan %s^\circ\)"
                         % (_fmt(distance), _fmt(angle)),
                 "note": "Multiply the horizontal distance by tan of the angle."},
                {"label": "Result",
                 "math": r"\(\text{height} = %s\)" % _fmt(height),
                 "note": "Same formula works for depression, measured below the horizontal."},
            ]
            result = height
        elif find == "distance":
            if angle is None or height is None:
                return _err("To find the distance, enter the angle and the height.")
            if not (0 < angle < 90):
                return _err("Enter an angle strictly between 0° and 90°.")
            if height <= 0:
                return _err("Height must be greater than zero.")
            distance = height / math.tan(math.radians(angle))
            steps = [
                {"label": "Set up the ratio",
                 "math": r"\(\tan\theta = \dfrac{\text{height}}{\text{distance}}\)",
                 "note": "Rearrange to make the distance the subject."},
                {"label": "Rearrange for distance",
                 "math": r"\(\text{distance} = \dfrac{\text{height}}{\tan\theta} = \dfrac{%s}{\tan %s^\circ}\)"
                         % (_fmt(height), _fmt(angle)),
                 "note": "Divide the height by tan of the angle."},
                {"label": "Result",
                 "math": r"\(\text{distance} = %s\)" % _fmt(distance),
                 "note": "The horizontal distance from the observer to the base."},
            ]
            result = distance
        elif find == "angle":
            if height is None or distance is None:
                return _err("To find the angle, enter the height and the distance.")
            if height <= 0 or distance <= 0:
                return _err("Height and distance must be greater than zero.")
            angle = math.degrees(math.atan2(height, distance))
            steps = [
                {"label": "Set up the ratio",
                 "math": r"\(\tan\theta = \dfrac{\text{height}}{\text{distance}} = \dfrac{%s}{%s}\)"
                         % (_fmt(height), _fmt(distance)),
                 "note": "Form the ratio of vertical to horizontal."},
                {"label": "Take the inverse tangent",
                 "math": r"\(\theta = \tan^{-1}\!\left(\dfrac{%s}{%s}\right)\)"
                         % (_fmt(height), _fmt(distance)),
                 "note": "Use the inverse tangent to recover the angle."},
                {"label": "Result",
                 "math": r"\(\theta \approx %s^\circ\)" % _fmt(angle),
                 "note": "Elevation looks up; depression looks down by the same angle."},
            ]
            result = angle
        else:
            return _err("Choose what to find: height, distance, or angle.")

        return {
            "result": _fmt(result),
            "angle": round(angle, 4) if angle is not None else None,
            "height": round(height, 6) if height is not None else None,
            "distance": round(distance, 6) if distance is not None else None,
            "find": find,
            "steps": steps,
            "explanation": [
                {"heading": "Elevation vs depression",
                 "body": "An angle of elevation is measured upward from the "
                         "horizontal to an object above you; an angle of depression "
                         "is measured downward to an object below. The two are equal "
                         "between the same pair of points (alternate angles)."},
                {"heading": "Why tangent",
                 "body": "Tangent links the side opposite the angle (the height) with "
                         "the side adjacent to it (the distance), so it is the natural "
                         "ratio for these vertical-and-horizontal problems."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers.")


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
