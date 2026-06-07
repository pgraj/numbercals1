"""Real-world worked example: a roof's pitch angle and rafter length from its rise and run (Construction)."""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="rw-roof-pitch",
    name="Roof pitch and rafter length",
    section="real-world",
    sub="Construction",
    topic="Real-World Trigonometry",
    order=0,
    summary=(
        "A worked real-world example: from a roof's vertical rise and horizontal "
        "run, inverse tangent gives the pitch angle and the Pythagorean theorem "
        "gives the rafter length — the two numbers a carpenter needs — shown on "
        "an animated roof cross-section you can reshape."
    ),
    formula="pitch = tan⁻¹(rise / run),  rafter = √(rise² + run²)",
    tags=["real life trigonometry", "construction", "roof pitch", "rafter", "inverse tangent", "carpentry", "worked example", "trigonometry", "GCSE", "ACARA Year 10"],
    viz_template="viz/rw-roof-pitch.html",
    scholar="hipparchus",
    related=['trig-sin-cos-tan', 'trig-inverse'],
)
def compute(run_width=None, rise=None):
    try:
        def num(x, d=None):
            return d if (x is None or x == "") else float(x)
        run = num(run_width, 4.0)     # half-span (horizontal run), metres
        rise = num(rise, 2.5)         # vertical rise, metres
        if run <= 0 or rise <= 0:
            return _err("Run and rise must both be greater than zero.")
        pitch = math.degrees(math.atan2(rise, run))
        rafter = math.hypot(run, rise)
        steps = [
            {"label": "Pitch angle from rise and run",
             "math": r"\(\theta = \tan^{-1}\!\left(\dfrac{\text{rise}}{\text{run}}\right) = \tan^{-1}\!\left(\dfrac{%s}{%s}\right) = %s^\circ\)" % (_fmt(rise), _fmt(run), _fmt(pitch)),
             "note": "The roof pitch is the angle whose tangent is rise over run."},
            {"label": "Rafter length by Pythagoras",
             "math": r"\(\text{rafter} = \sqrt{%s^2 + %s^2} = %s\ \text{m}\)" % (_fmt(run), _fmt(rise), _fmt(rafter)),
             "note": "The sloping rafter is the hypotenuse of the rise–run right triangle."},
        ]
        return {
            "result": _fmt(pitch),
            "run_width": run, "rise": rise,
            "pitch_deg": round(pitch, 3), "rafter": round(rafter, 4),
            "steps": steps,
            "explanation": [
                {"heading": "The scenario",
                 "body": "A roof rises %s m over a horizontal run of %s m from the wall "
                         "to the ridge. The carpenter needs the pitch angle (to cut the "
                         "rafter ends) and the rafter length (to order timber)." % (_fmt(rise), _fmt(run))},
                {"heading": "Inverse tangent finds the angle",
                 "body": "Rise and run are the opposite and adjacent sides, so their "
                         "ratio is the tangent of the pitch. Taking the inverse tangent "
                         "(arctan) turns that ratio back into the angle in degrees."},
                {"heading": "Pythagoras finds the rafter",
                 "body": "The rafter is the slope itself — the hypotenuse — so its length "
                         "is the square root of rise squared plus run squared. Builders "
                         "add an overhang allowance on top of this."},
                {"heading": "Try it yourself",
                 "body": "Increase the rise for a steeper, more dramatic roof; flatten it "
                         "and watch the pitch angle and rafter shrink toward the run."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for the rise and run.")


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
