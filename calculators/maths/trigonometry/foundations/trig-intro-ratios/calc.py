"""Intro to sin, cos, tan — Foundations cluster of the Trigonometry topic.

Given the three sides of a right triangle (opposite, adjacent, hypotenuse with
respect to an acute angle), report the three primary ratios and show which two
sides each ratio uses (SOH-CAH-TOA). Stays on the triangle — the unit circle and
wave graphs are introduced later, in the Functions & Graphs cluster.
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-intro-ratios",
    name="Intro to sin, cos, tan",
    section="maths",
    sub="Foundations",
    topic="Trigonometry",
    order=0,
    summary=(
        "Learn the three trigonometric ratios sine, cosine, and tangent from the "
        "sides of a right triangle using SOH-CAH-TOA, with a diagram that labels "
        "the opposite, adjacent, and hypotenuse and highlights which two sides "
        "each ratio uses."
    ),
    formula="sin = O/H · cos = A/H · tan = O/A  (SOH-CAH-TOA)",
    tags=[
        "sine", "cosine", "tangent", "SOH CAH TOA", "trigonometric ratios",
        "right triangle", "trigonometry", "CBSE Class 9", "GCSE",
        "Common Core HSG-SRT", "Singapore Sec 3", "France 3e",
        "Germany Klasse 9", "ACARA Year 9", "NSW Stage 5", "UAE Grade 9",
    ],
    viz_template="viz/trig-intro-ratios.html",
)
def compute(opp=None, adj=None, hyp=None):
    try:
        def num(x):
            if x is None or x == "":
                return None
            return float(x)

        opp, adj, hyp = num(opp), num(adj), num(hyp)

        # Need at least two of the three; derive the missing one via Pythagoras.
        known = [v for v in (opp, adj, hyp) if v is not None]
        if len(known) < 2:
            return _err("Enter at least two of: opposite, adjacent, hypotenuse.")
        for v in known:
            if v <= 0:
                return _err("Side lengths must be greater than zero.")

        if hyp is None:
            hyp = math.hypot(opp, adj)
        elif opp is None:
            if hyp <= adj:
                return _err("The hypotenuse must be the longest side.")
            opp = math.sqrt(hyp * hyp - adj * adj)
        elif adj is None:
            if hyp <= opp:
                return _err("The hypotenuse must be the longest side.")
            adj = math.sqrt(hyp * hyp - opp * opp)

        if hyp <= opp or hyp <= adj:
            return _err("The hypotenuse must be the longest side of a right triangle.")

        sin = opp / hyp
        cos = adj / hyp
        tan = opp / adj
        angle = math.degrees(math.atan2(opp, adj))

        steps = [
            {"label": "Label the sides",
             "math": r"\(O=%s,\; A=%s,\; H=%s\)" % (_fmt(opp), _fmt(adj), _fmt(hyp)),
             "note": "Opposite is across from the angle, adjacent is beside it, "
                     "hypotenuse is opposite the right angle."},
            {"label": "SOH — sine",
             "math": r"\(\sin\theta = \dfrac{O}{H} = \dfrac{%s}{%s} = %s\)"
                     % (_fmt(opp), _fmt(hyp), _fmt(sin)),
             "note": "Sine uses the Opposite over the Hypotenuse."},
            {"label": "CAH — cosine",
             "math": r"\(\cos\theta = \dfrac{A}{H} = \dfrac{%s}{%s} = %s\)"
                     % (_fmt(adj), _fmt(hyp), _fmt(cos)),
             "note": "Cosine uses the Adjacent over the Hypotenuse."},
            {"label": "TOA — tangent",
             "math": r"\(\tan\theta = \dfrac{O}{A} = \dfrac{%s}{%s} = %s\)"
                     % (_fmt(opp), _fmt(adj), _fmt(tan)),
             "note": "Tangent uses the Opposite over the Adjacent."},
            {"label": "The angle itself",
             "math": r"\(\theta \approx %s^\circ\)" % _fmt(angle),
             "note": "Found from the inverse tangent of opposite over adjacent."},
        ]
        return {
            "result": "sin %s, cos %s, tan %s" % (_fmt(sin), _fmt(cos), _fmt(tan)),
            "opp": opp, "adj": adj, "hyp": hyp,
            "sin": round(sin, 6), "cos": round(cos, 6), "tan": round(tan, 6),
            "angle": round(angle, 4),
            "steps": steps,
            "explanation": [
                {"heading": "SOH-CAH-TOA",
                 "body": "This memory aid packs all three ratios: Sine = Opposite / "
                         "Hypotenuse, Cosine = Adjacent / Hypotenuse, Tangent = "
                         "Opposite / Adjacent. Identify the angle first, then label "
                         "the three sides relative to it."},
                {"heading": "Ratios, not lengths",
                 "body": "Because similar right triangles share the same angles, "
                         "these ratios depend only on the angle, not the triangle's "
                         "size — which is exactly why they are so useful."},
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
