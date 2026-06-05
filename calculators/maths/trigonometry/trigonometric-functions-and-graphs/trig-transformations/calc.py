"""y = A·sin(Bx + C) + D — Trigonometric Functions & Graphs cluster (Stage 2).

Evaluate the transformed sine and report amplitude |A|, period 360/|B|, phase
shift -C/B, and vertical shift D.
"""
import math

from core.registry import register

DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)


@register(
    slug="trig-transformations",
    name="Transformations: y = A·sin(Bx + C) + D",
    section="maths",
    sub="Trigonometric Functions & Graphs",
    topic="Trigonometry",
    order=0,
    summary=(
        "Explore how the four parameters in y = A sin(Bx + C) + D stretch, "
        "compress, and shift the sine curve — amplitude, period, phase shift, and "
        "vertical shift — with live sliders and a graph that redraws as you change "
        "each one."
    ),
    formula="y = A·sin(Bx + C) + D",
    tags=[
        "transformations", "amplitude", "period", "phase shift", "vertical shift",
        "sine transformation", "trigonometry", "CBSE Class 11", "A-Level",
        "Common Core HSF-TF", "Singapore A-Math", "France Premiere",
        "Germany Klasse 10", "ACARA Year 11", "UAE Grade 11",
    ],
    viz_template="viz/trig-transformations.html",
)
def compute(A=1, B=1, C=0, D=0, x_deg=None):
    try:
        def num(v, dflt):
            if v is None or v == "":
                return dflt
            return float(v)

        A = num(A, 1.0)
        B = num(B, 1.0)
        C = num(C, 0.0)
        D = num(D, 0.0)
        if B == 0:
            return _err("B cannot be zero (the period would be infinite).")

        amplitude = abs(A)
        period = 360.0 / abs(B)
        phase = -C / B  # horizontal shift in degrees
        midline = D

        x = num(x_deg, None)
        y = None
        if x is not None:
            y = A * math.sin(math.radians(B * x + C)) + D

        steps = [
            {"label": "Amplitude",
             "math": r"\(|A| = %s\)" % _fmt(amplitude),
             "note": "The curve reaches A above and below the midline."},
            {"label": "Period",
             "math": r"\(\dfrac{360^\circ}{|B|} = %s^\circ\)" % _fmt(period),
             "note": "B horizontally stretches (|B|<1) or compresses (|B|>1) the wave."},
            {"label": "Phase shift",
             "math": r"\(-\dfrac{C}{B} = %s^\circ\)" % _fmt(phase),
             "note": "A positive C shifts the curve to the left."},
            {"label": "Vertical shift (midline)",
             "math": r"\(y = %s\)" % _fmt(midline),
             "note": "D raises or lowers the whole curve."},
        ]
        if x is not None:
            steps.append({
                "label": "Evaluate at the chosen x",
                "math": r"\(y = %s\sin(%s\cdot %s + %s) + %s = %s\)"
                        % (_fmt(A), _fmt(B), _fmt(x), _fmt(C), _fmt(D), _fmt(y)),
                "note": "Substituting the x value into the full expression."})

        return {
            "result": (_fmt(y) if y is not None else "amp %s, period %s\u00b0" % (_fmt(amplitude), _fmt(period))),
            "A": A, "B": B, "C": C, "D": D, "x": x,
            "y": (round(y, 6) if y is not None else None),
            "amplitude": round(amplitude, 6),
            "period_deg": round(period, 6),
            "phase_deg": round(phase, 6),
            "midline": D,
            "steps": steps,
            "explanation": [
                {"heading": "What each letter does",
                 "body": "A sets the amplitude (height), B sets how many cycles fit "
                         "in 360° and hence the period, C shifts the curve "
                         "horizontally (phase), and D shifts it vertically. Together "
                         "they can model almost any simple oscillation."},
                {"heading": "Reading a real wave",
                 "body": "Given a graph, you can read A from its peak height above the "
                         "midline, the period from the distance between repeats, the "
                         "midline from D, and the phase from how far the start is "
                         "shifted — the reverse of building the equation."},
            ],
            "disclaimer": DISCLAIMER,
        }
    except (TypeError, ValueError):
        return _err("Please enter valid numbers for A, B, C, D.")


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
