"""Period & amplitude — Trigonometric Functions & Graphs cluster (Stage 2).

From y = A·sin(Bx), report amplitude |A| and period 360/|B| (and 2π/|B| in
radians). Accepts `angle_unit` ("deg"|"rad"): the period is led in the chosen
unit and the graph x-axis is relabelled to match (π-fractions in radians). The
amplitude is a pure number, unaffected by the angle unit.
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-period-amplitude",
    name="Period & amplitude",
    section="maths",
    sub="Trigonometric Functions & Graphs",
    topic="Trigonometry",
    order=0,
    summary=(
        "Find the amplitude and period of a wave y = A sin(Bx): the amplitude is "
        "the absolute value of A and the period is 360 degrees (or 2π radians) "
        "divided by the absolute value of B, shown with a wave that stretches or "
        "compresses as you change A and B, with the x-axis in degrees or radians."
    ),
    formula="amplitude = |A| · period = 360°/|B| = 2π/|B|",
    tags=[
        "period", "amplitude", "frequency", "wavelength", "sine wave",
        "trigonometry", "CBSE Class 11", "A-Level", "Common Core HSF-TF",
        "Singapore A-Math", "France Premiere", "Germany Klasse 10",
        "ACARA Year 11", "UAE Grade 11",
    ],
    viz_template="viz/trig-period-amplitude.html",
)
def compute(A=1, B=1, angle_unit="deg"):
    try:
        unit = "rad" if str(angle_unit) == "rad" else "deg"

        def num(v, dflt):
            if v is None or v == "":
                return dflt
            return float(v)

        A = num(A, 1.0)
        B = num(B, 1.0)
        if B == 0:
            return _err("B cannot be zero (the period would be infinite).")

        amplitude = abs(A)
        period_deg = 360.0 / abs(B)
        period_rad = 2 * math.pi / abs(B)

        if unit == "rad":
            period_step = {
                "label": "Period from B (radians)",
                "math": r"\(T = \dfrac{2\pi}{|B|} = \dfrac{2\pi}{%s} = %s\,\text{rad}\)"
                        % (_fmt(abs(B)), _fmt(period_rad)),
                "note": "Larger B means more cycles in the same span — a shorter period."}
            alt_step = {
                "label": "Period in degrees",
                "math": r"\(T = \dfrac{360^\circ}{|B|} = %s^\circ\)" % _fmt(period_deg),
                "note": "The same period expressed in degrees."}
            result = "amplitude %s, period %s rad" % (_fmt(amplitude), _fmt(period_rad))
        else:
            period_step = {
                "label": "Period from B (degrees)",
                "math": r"\(T = \dfrac{360^\circ}{|B|} = \dfrac{360^\circ}{%s} = %s^\circ\)"
                        % (_fmt(abs(B)), _fmt(period_deg)),
                "note": "Larger B means more cycles in the same span — a shorter period."}
            alt_step = {
                "label": "Period in radians",
                "math": r"\(T = \dfrac{2\pi}{|B|} = %s\,\text{rad}\)" % _fmt(period_rad),
                "note": "The same period expressed in radians."}
            result = "amplitude %s, period %s\u00b0" % (_fmt(amplitude), _fmt(period_deg))

        steps = [
            {"label": "Amplitude from A",
             "math": r"\(\text{amplitude} = |A| = %s\)" % _fmt(amplitude),
             "note": "The wave rises this far above and below the centre line."},
            period_step,
            alt_step,
        ]
        return {
            "result": result,
            "A": A, "B": B, "angle_unit": unit,
            "amplitude": round(amplitude, 6),
            "period_deg": round(period_deg, 6),
            "period_rad": round(period_rad, 6),
            "steps": steps,
            "explanation": [
                {"heading": "Amplitude is height, period is width",
                 "body": "Amplitude measures how tall the wave is — the distance from "
                         "the midline to a peak. Period measures how wide one full "
                         "cycle is before the pattern repeats. They are independent: "
                         "changing one does not affect the other."},
                {"heading": "Degrees or radians",
                 "body": "The period is the same physical width either way: 360°/|B| "
                         "and 2π/|B| describe the identical cycle. Radians are the "
                         "natural choice for the wave's x-axis in higher mathematics, "
                         "where the axis is marked in multiples of π."},
                {"heading": "B and frequency",
                 "body": "The number B counts how many full waves fit in one turn. "
                         "Doubling B halves the period and doubles the frequency, "
                         "squeezing twice as many cycles into the same space."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for A and B.")


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
