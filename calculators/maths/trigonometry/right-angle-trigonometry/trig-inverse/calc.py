"""Find an angle — Right-Angle Trigonometry cluster.

Given two sides of a right triangle, find an acute angle using the inverse
trigonometric functions: θ = sin⁻¹(opp/hyp), cos⁻¹(adj/hyp), or tan⁻¹(opp/adj).
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


def _ang_tex(deg, unit):
    """Solved angle as LaTeX for step math, in the chosen unit (radians = decimal)."""
    if unit == "rad":
        return ("%.4f" % math.radians(deg)).rstrip("0").rstrip(".") + r"\,\text{rad}"
    return _fmt(deg) + r"^\circ"


def _ang_disp(deg, unit):
    """Solved angle as plain display text, in the chosen unit."""
    if unit == "rad":
        return ("%.4f" % math.radians(deg)).rstrip("0").rstrip(".") + " rad"
    return _fmt(deg) + "\u00b0"


@register(
    slug="trig-inverse",
    name="Find an angle",
    section="maths",
    sub="Right-Angle Trigonometry",
    topic="Trigonometry",
    order=0,
    summary=(
        "Find an unknown acute angle in a right triangle from two known sides "
        "using the inverse sine, cosine, or tangent, with a diagram that draws "
        "and labels the angle arc once it is solved."
    ),
    formula="θ = sin⁻¹(O/H) · cos⁻¹(A/H) · tan⁻¹(O/A)",
    tags=[
        "inverse sine", "inverse cosine", "inverse tangent", "find angle",
        "arcsin", "arccos", "arctan", "right triangle", "trigonometry",
        "CBSE Class 10", "GCSE", "Common Core HSG-SRT", "Singapore Sec 3",
        "France 3e", "Germany Klasse 9", "ACARA Year 9", "NSW Stage 5",
        "UAE Grade 9",
    ],
    viz_template="viz/trig-inverse.html",
)
def compute(side1=None, side1_type="opp", side2=None, side2_type="hyp", angle_unit="deg"):
    try:
        unit = "rad" if str(angle_unit) == "rad" else "deg"
        if side1 in (None, "") or side2 in (None, ""):
            return _err("Enter two side lengths and say which sides they are.")
        s1, s2 = float(side1), float(side2)
        t1 = (side1_type or "opp").lower()
        t2 = (side2_type or "hyp").lower()
        if s1 <= 0 or s2 <= 0:
            return _err("Side lengths must be greater than zero.")
        if t1 == t2:
            return _err("The two sides must be of different types.")
        pair = frozenset((t1, t2))

        # Map by side pair to the inverse function.
        if pair == frozenset(("opp", "hyp")):
            opp = s1 if t1 == "opp" else s2
            hyp = s2 if t2 == "hyp" else s1
            if opp >= hyp:
                return _err("The opposite side must be shorter than the hypotenuse.")
            ratio = opp / hyp
            angle = math.degrees(math.asin(ratio))
            fn, tex = "sin⁻¹", r"\theta = \sin^{-1}\!\left(\dfrac{O}{H}\right) = \sin^{-1}\!\left(\dfrac{%s}{%s}\right)" % (_fmt(opp), _fmt(hyp))
        elif pair == frozenset(("adj", "hyp")):
            adj = s1 if t1 == "adj" else s2
            hyp = s2 if t2 == "hyp" else s1
            if adj >= hyp:
                return _err("The adjacent side must be shorter than the hypotenuse.")
            ratio = adj / hyp
            angle = math.degrees(math.acos(ratio))
            fn, tex = "cos⁻¹", r"\theta = \cos^{-1}\!\left(\dfrac{A}{H}\right) = \cos^{-1}\!\left(\dfrac{%s}{%s}\right)" % (_fmt(adj), _fmt(hyp))
        elif pair == frozenset(("opp", "adj")):
            opp = s1 if t1 == "opp" else s2
            adj = s2 if t2 == "adj" else s1
            ratio = opp / adj
            angle = math.degrees(math.atan(ratio))
            fn, tex = "tan⁻¹", r"\theta = \tan^{-1}\!\left(\dfrac{O}{A}\right) = \tan^{-1}\!\left(\dfrac{%s}{%s}\right)" % (_fmt(opp), _fmt(adj))
        else:
            return _err("Choose two of: opposite, adjacent, hypotenuse.")

        steps = [
            {"label": "Choose the inverse ratio",
             "math": r"\(%s\)" % fn.replace("⁻¹", "^{-1}"),
             "note": "Use the inverse function matching the two sides you know."},
            {"label": "Substitute the ratio",
             "math": r"\(%s\)" % tex,
             "note": "Form the ratio, then apply the inverse function."},
            {"label": "Evaluate the angle",
             "math": r"\(\theta \approx %s\)" % _ang_tex(angle, unit),
             "note": "On a calculator this is the shift/2nd key above sin, cos, or tan; "
                     "make sure it is set to the same mode (degrees or radians) you want the answer in."},
        ]
        return {
            "result": _ang_disp(angle, unit),
            "angle": round(angle, 4), "angle_unit": unit, "ratio": round(ratio, 6), "fn": fn,
            "steps": steps,
            "explanation": [
                {"heading": "Inverse functions undo the ratio",
                 "body": "The ordinary sine turns an angle into a ratio; the inverse "
                         "sine turns a ratio back into the angle. The same idea gives "
                         "cos⁻¹ and tan⁻¹ for the other side pairs."},
                {"heading": "Pick by the sides you have",
                 "body": "Opposite and hypotenuse → inverse sine; adjacent and "
                         "hypotenuse → inverse cosine; opposite and adjacent → inverse "
                         "tangent. The answer is always the acute angle here."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for the sides.")


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
