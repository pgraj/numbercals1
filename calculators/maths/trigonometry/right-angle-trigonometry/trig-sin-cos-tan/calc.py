"""Find a side — Right-Angle Trigonometry cluster.

Given an acute angle and one known side of a right triangle, find another side
using opp = hyp·sinθ, adj = hyp·cosθ, opp = adj·tanθ (and rearrangements).
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)

# Which ratio links a (known, wanted) pair, and the multiply/divide direction.
# key: (known, wanted) -> (ratio_name, formula_text, fn)
def _solve(angle, known_type, known_val, want_type):
    th = math.radians(angle)
    s, c, t = math.sin(th), math.cos(th), math.tan(th)
    pairs = {
        ("hyp", "opp"): ("sin", r"\text{opp} = \text{hyp}\,\sin\theta", known_val * s),
        ("hyp", "adj"): ("cos", r"\text{adj} = \text{hyp}\,\cos\theta", known_val * c),
        ("opp", "hyp"): ("sin", r"\text{hyp} = \dfrac{\text{opp}}{\sin\theta}", known_val / s if s else None),
        ("adj", "hyp"): ("cos", r"\text{hyp} = \dfrac{\text{adj}}{\cos\theta}", known_val / c if c else None),
        ("adj", "opp"): ("tan", r"\text{opp} = \text{adj}\,\tan\theta", known_val * t),
        ("opp", "adj"): ("tan", r"\text{adj} = \dfrac{\text{opp}}{\tan\theta}", known_val / t if t else None),
    }
    return pairs.get((known_type, want_type))


@register(
    slug="trig-sin-cos-tan",
    name="Find a side",
    section="maths",
    sub="Right-Angle Trigonometry",
    topic="Trigonometry",
    order=0,
    summary=(
        "Find an unknown side of a right triangle from an acute angle and one "
        "known side, choosing sine, cosine, or tangent automatically, with a "
        "diagram whose sides update live as you drag the angle."
    ),
    formula="opp = hyp·sinθ · adj = hyp·cosθ · opp = adj·tanθ",
    tags=[
        "sine", "cosine", "tangent", "find missing side", "right triangle",
        "SOH CAH TOA", "trigonometry", "CBSE Class 10", "GCSE",
        "Common Core HSG-SRT", "Singapore Sec 3", "France 3e",
        "Germany Klasse 9", "ACARA Year 9", "NSW Stage 5", "UAE Grade 9",
    ],
    viz_template="viz/trig-sin-cos-tan.html",
)
def compute(angle_deg=None, known_type="hyp", known_val=None, want_type="opp"):
    try:
        if angle_deg is None or angle_deg == "" or known_val in (None, ""):
            return _err("Enter the angle and one known side.")
        angle = float(angle_deg)
        known_val = float(known_val)
        known_type = (known_type or "hyp").lower()
        want_type = (want_type or "opp").lower()

        if not (0 < angle < 90):
            return _err("Enter an acute angle strictly between 0° and 90°.")
        if known_val <= 0:
            return _err("The known side must be greater than zero.")
        if known_type == want_type:
            return _err("The known side and the side to find must be different.")
        if known_type not in ("opp", "adj", "hyp") or want_type not in ("opp", "adj", "hyp"):
            return _err("Sides must be opposite, adjacent, or hypotenuse.")

        sol = _solve(angle, known_type, known_val, want_type)
        if sol is None or sol[2] is None:
            return _err("That combination can't be solved; check the sides chosen.")
        ratio, formula_tex, value = sol

        nm = {"opp": "opposite", "adj": "adjacent", "hyp": "hypotenuse"}
        steps = [
            {"label": "Pick the ratio",
             "math": r"\(\%s\theta\)" % ("sin" if ratio == "sin" else ratio),
             "note": "Use %s because it links the %s (known) and the %s (wanted)."
                     % (ratio, nm[known_type], nm[want_type])},
            {"label": "Write the rearranged formula",
             "math": r"\(%s\)" % formula_tex,
             "note": "Rearranged so the unknown side is the subject."},
            {"label": "Substitute and evaluate",
             "math": r"\(\text{%s} = %s\)" % (nm[want_type], _fmt(value)),
             "note": "θ = %s°, %s = %s." % (_fmt(angle), nm[known_type], _fmt(known_val))},
        ]
        return {
            "result": _fmt(value),
            "angle": angle, "known_type": known_type, "known_val": known_val,
            "want_type": want_type, "value": round(value, 6), "ratio": ratio,
            "steps": steps,
            "explanation": [
                {"heading": "Choosing sin, cos, or tan",
                 "body": "Label the two sides involved relative to the angle, then "
                         "pick the ratio that uses exactly those two: sine for "
                         "opposite and hypotenuse, cosine for adjacent and "
                         "hypotenuse, tangent for opposite and adjacent."},
                {"heading": "Rearranging safely",
                 "body": "If the unknown is on top of the fraction you multiply; if "
                         "it is on the bottom you divide. Keeping the angle in degrees "
                         "mode on your calculator matters here."},
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
