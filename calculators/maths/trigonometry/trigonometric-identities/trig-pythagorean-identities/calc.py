"""Pythagorean Identities — sin²θ+cos²θ=1 and the tan/sec, cot/cosec forms.

Reference calculator for the Stage 3 Trigonometric Identities cluster. It
demonstrates the conventions every Stage 3 calc follows:
  * accepts `angle_unit` ("deg"|"rad") so results AND step-by-step working
    re-derive in the unit the student picked via the shared deg/rad toggle;
  * emits the COMPLETE derivation as steps (not an abbreviated summary), with
    LaTeX in `math` so _steps.html renders proper mathematics;
  * returns an `explanation` (plain-English cards) + verbatim disclaimer;
  * never raises; always JSON-serialisable.
"""
from __future__ import annotations

import math

from core.registry import register

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)

_EXPLANATION = [
    {"heading": "Where the identity comes from",
     "body": "On the unit circle a point at angle θ has coordinates (cos θ, sin θ). "
             "Because the radius is 1, Pythagoras' theorem on the right triangle "
             "formed by that point gives cos²θ + sin²θ = 1 for every angle — it is "
             "an identity, true everywhere, not an equation to solve."},
    {"heading": "The two derived forms",
     "body": "Dividing sin²θ + cos²θ = 1 through by cos²θ gives tan²θ + 1 = sec²θ. "
             "Dividing instead by sin²θ gives 1 + cot²θ = cosec²θ. All three are the "
             "same identity wearing different clothes, and each is the handy one in a "
             "different problem."},
    {"heading": "Why it matters",
     "body": "These identities let you swap between sin, cos, tan, sec, cosec and cot "
             "without knowing the angle — the backbone of simplifying expressions, "
             "integrating trig functions, and deriving the compound- and double-angle "
             "formulae that follow in this topic."},
]

_FORMS = {
    "sin-cos": "sin²θ + cos²θ = 1",
    "tan-sec": "1 + tan²θ = sec²θ",
    "cot-cosec": "1 + cot²θ = cosec²θ",
}


def _ang(value_deg: float, unit: str) -> str:
    """Render an angle (given in degrees) for display in the chosen unit."""
    if unit == "rad":
        r = math.radians(value_deg)
        return f"{r:.4f}\\,\\text{{rad}}"
    return f"{value_deg:g}^\\circ"


@register(
    slug="trig-pythagorean-identities",
    name="Pythagorean Identities",
    section="maths",
    sub="Trigonometric Identities",
    topic="Trigonometry",
    order=50,
    summary="Verify and explore the three Pythagorean identities — sin²θ+cos²θ=1, "
            "1+tan²θ=sec²θ and 1+cot²θ=cosec²θ — for any angle, in degrees or radians, "
            "with the full unit-circle derivation worked step by step.",
    formula="sin²θ + cos²θ = 1",
    tags=["pythagorean identity", "sin squared cos squared", "sec tan identity",
          "cot cosec identity", "trig identity"],
    viz_template="viz/trig-pythagorean-identities.html",
    scholar="pythagoras",
)
def compute(angle=30, form="sin-cos", angle_unit="deg", **_ignored):
    """Verify a Pythagorean identity at `angle`, with full working.

    angle      : the angle, expressed in `angle_unit`.
    form       : which identity — "sin-cos" | "tan-sec" | "cot-cosec".
    angle_unit : "deg" (default) or "rad" — controls how the angle is READ and
                 how every step is displayed.
    """
    unit = "rad" if str(angle_unit) == "rad" else "deg"
    if form not in _FORMS:
        return {"error": f"Unknown form: {form}", "steps": [], "disclaimer": _DISCLAIMER}
    try:
        a = float(angle)
    except (TypeError, ValueError):
        return {"error": "Angle must be a number.", "steps": [], "disclaimer": _DISCLAIMER}

    # Normalise to degrees internally for the trig calls.
    deg = a if unit == "deg" else math.degrees(a)
    rad = math.radians(deg)

    s, c = math.sin(rad), math.cos(rad)
    disp = _ang(deg, unit)
    steps = []

    if form == "sin-cos":
        lhs = s * s + c * c
        steps = [
            {"label": "Start from the unit circle",
             "math": rf"\(\text{{Point at }}\theta={disp}\text{{ is }}(\cos\theta,\ \sin\theta)\)",
             "note": "Radius 1, so the coordinates are exactly cos θ and sin θ."},
            {"label": "Evaluate sin θ and cos θ",
             "math": rf"\(\sin\theta={s:.4f},\quad \cos\theta={c:.4f}\)"},
            {"label": "Square each",
             "math": rf"\(\sin^2\theta={s*s:.4f},\quad \cos^2\theta={c*c:.4f}\)"},
            {"label": "Add — Pythagoras on the unit circle",
             "math": rf"\(\sin^2\theta+\cos^2\theta={s*s:.4f}+{c*c:.4f}={lhs:.4f}\)",
             "note": "Equals 1 (any tiny difference is floating-point rounding)."},
        ]
        result = lhs
        result_label = "sin²θ + cos²θ"
    elif form == "tan-sec":
        if abs(c) < 1e-12:
            return {"error": "cos θ = 0 here, so tan and sec are undefined at this angle.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        t, sec = s / c, 1 / c
        lhs = 1 + t * t
        steps = [
            {"label": "Divide the base identity by cos²θ",
             "math": r"\(\dfrac{\sin^2\theta}{\cos^2\theta}+\dfrac{\cos^2\theta}{\cos^2\theta}=\dfrac{1}{\cos^2\theta}\)",
             "note": "Each term divided by cos²θ."},
            {"label": "Rewrite as tan and sec",
             "math": r"\(\tan^2\theta+1=\sec^2\theta\)"},
            {"label": "Evaluate at θ = " + disp,
             "math": rf"\(\tan\theta={t:.4f},\quad \sec\theta={sec:.4f}\)"},
            {"label": "Check both sides",
             "math": rf"\(1+\tan^2\theta={lhs:.4f},\quad \sec^2\theta={sec*sec:.4f}\)",
             "note": "The two sides match."},
        ]
        result = lhs
        result_label = "1 + tan²θ"
    else:  # cot-cosec
        if abs(s) < 1e-12:
            return {"error": "sin θ = 0 here, so cot and cosec are undefined at this angle.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        cot, cosec = c / s, 1 / s
        lhs = 1 + cot * cot
        steps = [
            {"label": "Divide the base identity by sin²θ",
             "math": r"\(\dfrac{\sin^2\theta}{\sin^2\theta}+\dfrac{\cos^2\theta}{\sin^2\theta}=\dfrac{1}{\sin^2\theta}\)",
             "note": "Each term divided by sin²θ."},
            {"label": "Rewrite as cot and cosec",
             "math": r"\(1+\cot^2\theta=\operatorname{cosec}^2\theta\)"},
            {"label": "Evaluate at θ = " + disp,
             "math": rf"\(\cot\theta={cot:.4f},\quad \operatorname{{cosec}}\theta={cosec:.4f}\)"},
            {"label": "Check both sides",
             "math": rf"\(1+\cot^2\theta={lhs:.4f},\quad \operatorname{{cosec}}^2\theta={cosec*cosec:.4f}\)",
             "note": "The two sides match."},
        ]
        result = lhs
        result_label = "1 + cot²θ"

    return {
        "result": round(result, 6),
        "result_label": result_label,
        "identity": _FORMS[form],
        "angle_deg": deg,
        "angle_display": disp,
        "angle_unit": unit,            # <-- presence signals "this calc uses angles"
        "sin": round(s, 6),
        "cos": round(c, 6),
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
