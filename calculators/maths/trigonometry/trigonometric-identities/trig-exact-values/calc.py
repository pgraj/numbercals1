"""Exact trigonometric values at the special angles.

Stage 3 (NSW Year 11 Mathematics Advanced) — reads sin, cos and tan as EXACT
surds at the standard special angles (0, 30, 45, 60, 90 ... 360), derived four
ways the student can switch between:
  * special-triangle  — the 30-60-90 / 45-45-90 triangle the value comes from;
  * unit-circle       — the (cos θ, sin θ) coordinate of the terminal point;
  * cast              — the CAST quadrant sign rule applied to the reference angle;
  * exact-value       — just the final surd + decimal.

Follows the Stage 3 contract: accepts `angle_unit`, full LaTeX steps that
re-derive in the chosen unit, plain-English explanation, verbatim disclaimer,
never raises.
"""
from __future__ import annotations

import math

from core.registry import register

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)

# --- Exact-value table -----------------------------------------------------
# Keyed by angle in WHOLE degrees. Each value is a display surd string already
# rationalised to NSW convention (1/√3 -> √3/3). tan is None where undefined.
_TABLE = {
    0:   ("0", "1", "0"),
    30:  ("1/2", "√3/2", "√3/3"),
    45:  ("√2/2", "√2/2", "1"),
    60:  ("√3/2", "1/2", "√3"),
    90:  ("1", "0", None),
    120: ("√3/2", "-1/2", "-√3"),
    135: ("√2/2", "-√2/2", "-1"),
    150: ("1/2", "-√3/2", "-√3/3"),
    180: ("0", "-1", "0"),
    210: ("-1/2", "-√3/2", "√3/3"),
    225: ("-√2/2", "-√2/2", "1"),
    240: ("-√3/2", "-1/2", "√3"),
    270: ("-1", "0", None),
    300: ("-√3/2", "1/2", "-√3"),
    315: ("-√2/2", "√2/2", "-1"),
    330: ("-1/2", "√3/2", "-√3/3"),
    360: ("0", "1", "0"),
}

# LaTeX form of each surd for the steps.
_LATEX = {
    "0": "0", "1": "1", "-1": "-1",
    "1/2": r"\tfrac{1}{2}", "-1/2": r"-\tfrac{1}{2}",
    "√3/2": r"\tfrac{\sqrt{3}}{2}", "-√3/2": r"-\tfrac{\sqrt{3}}{2}",
    "√2/2": r"\tfrac{\sqrt{2}}{2}", "-√2/2": r"-\tfrac{\sqrt{2}}{2}",
    "√3": r"\sqrt{3}", "-√3": r"-\sqrt{3}",
    "√3/3": r"\tfrac{\sqrt{3}}{3}", "-√3/3": r"-\tfrac{\sqrt{3}}{3}",
}

_CAST = {
    1: "All three (sin, cos, tan) are positive.",
    2: "Only sin is positive; cos and tan are negative.",
    3: "Only tan is positive; sin and cos are negative.",
    4: "Only cos is positive; sin and tan are negative.",
}

_METHODS = ("special-triangle", "unit-circle", "cast", "exact-value")

_EXPLANATION = [
    {"heading": "What the special angles are",
     "body": "A handful of angles — 0, 30°, 45°, 60°, 90° and their reflections "
             "around the circle — have sin, cos and tan values you can write "
             "exactly as surds, with no calculator. They come from two set-square "
             "triangles and the unit circle, so they turn up constantly in exact-form "
             "answers."},
    {"heading": "The two triangles",
     "body": "The 45-45-90 triangle has sides 1 : 1 : √2, giving sin 45° = cos 45° = "
             "√2/2. The 30-60-90 triangle has sides 1 : √3 : 2, giving sin 30° = 1/2, "
             "cos 30° = √3/2, and the 60° values swapped. Every special value is one "
             "of these read off the right side."},
    {"heading": "Reference angle + CAST",
     "body": "For angles past 90° you take the reference angle (its acute distance to "
             "the x-axis), read the value off the matching triangle, then apply the "
             "CAST rule for the sign: All in Q1, Sin in Q2, Tan in Q3, Cos in Q4 are "
             "positive. That single idea covers every special angle in all four "
             "quadrants."},
]


def _disp_angle(deg: float, unit: str) -> str:
    if unit == "rad":
        return f"{math.radians(deg):.4f}\\,\\text{{rad}}"
    return f"{deg:g}^\\circ"


def _disp_angle_plain(deg: float, unit: str) -> str:
    if unit == "rad":
        return f"{math.radians(deg):.4f} rad"
    return f"{deg:g}\u00b0"


def _surd_float(s):
    if s is None:
        return None
    table = {
        "0": 0.0, "1": 1.0, "-1": -1.0,
        "1/2": 0.5, "-1/2": -0.5,
        "√3/2": math.sqrt(3) / 2, "-√3/2": -math.sqrt(3) / 2,
        "√2/2": math.sqrt(2) / 2, "-√2/2": -math.sqrt(2) / 2,
        "√3": math.sqrt(3), "-√3": -math.sqrt(3),
        "√3/3": math.sqrt(3) / 3, "-√3/3": -math.sqrt(3) / 3,
    }
    return table[s]


def _meta(deg: int) -> dict:
    """Reference angle, quadrant, axis-flag for a special angle in [0,360]."""
    d = deg % 360
    if d in (0, 90, 180, 270):
        return {"axis": True, "quadrant": None, "ref": (0 if d in (0, 180) else 90)}
    q = 1 + (d // 90)
    if q == 1:
        ref = d
    elif q == 2:
        ref = 180 - d
    elif q == 3:
        ref = d - 180
    else:
        ref = 360 - d
    return {"axis": False, "quadrant": int(q), "ref": int(ref)}


@register(
    slug="trig-exact-values",
    name="Exact Trigonometric Values",
    section="maths",
    sub="Trigonometric Identities",
    topic="Trigonometry",
    order=55,
    summary="Read sin, cos and tan as exact surds at every special angle — 0, 30°, "
            "45°, 60°, 90° and their reflections in all four quadrants — derived from "
            "the special triangles, the unit circle and the CAST rule, in degrees or "
            "radians.",
    formula="sin 30°=1/2, cos 30°=√3/2, sin 45°=cos 45°=√2/2, sin 60°=√3/2",
    tags=["exact values", "special angles", "special triangles", "unit circle exact",
          "CAST rule", "surd trig values"],
    viz_template="viz/trig-exact-values.html",
    scholar="pythagoras",
    related=["trig-pythagorean-identities", "trig-unit-circle"],
)
def compute(angle=30, method="special-triangle", angle_unit="deg", **_ignored):
    """Exact sin/cos/tan at a special `angle`, derived by `method`.

    angle      : a special angle, expressed in `angle_unit`.
    method     : "special-triangle" | "unit-circle" | "cast" | "exact-value".
    angle_unit : "deg" (default) or "rad".
    """
    unit = "rad" if str(angle_unit) == "rad" else "deg"
    if method not in _METHODS:
        method = "special-triangle"
    try:
        a = float(angle)
    except (TypeError, ValueError):
        return {"error": "Angle must be a number.", "steps": [], "disclaimer": _DISCLAIMER}

    # Normalise to whole degrees in [0,360].
    deg = a if unit == "deg" else math.degrees(a)
    deg_key = int(round(deg)) % 360
    if deg_key == 0 and round(deg) % 360 != 0:
        deg_key = 0
    # 360 collapses to 0 in the key; keep a display value matching the input.
    if deg_key not in _TABLE:
        # Not a standard special angle — guide rather than guess.
        return {
            "error": "That is not one of the standard special angles. Pick from the "
                     "list (0, 30°, 45°, 60°, 90° and their reflections).",
            "steps": [], "disclaimer": _DISCLAIMER,
        }

    ss, cs, ts = _TABLE[deg_key]
    sin_f, cos_f = _surd_float(ss), _surd_float(cs)
    tan_f = _surd_float(ts)
    m = _meta(deg_key)
    disp = _disp_angle(deg_key, unit)
    disp_plain = _disp_angle_plain(deg_key, unit)

    # --- Build steps per method --------------------------------------------
    steps = []
    if method == "exact-value":
        tan_tex = _LATEX[ts] if ts is not None else r"\text{undefined}"
        steps = [
            {"label": f"Exact values at θ = {disp_plain}",
             "math": rf"\(\sin\theta={_LATEX[ss]},\quad \cos\theta={_LATEX[cs]},"
                     rf"\quad \tan\theta={tan_tex}\)"},
        ]
    elif method == "unit-circle":
        tan_note = ("tan θ = sin θ / cos θ is undefined here because cos θ = 0."
                    if ts is None else
                    "tan θ is the ratio sin θ / cos θ of those two coordinates.")
        steps = [
            {"label": "Terminal point on the unit circle",
             "math": rf"\(\theta={disp}\ \Rightarrow\ (\cos\theta,\ \sin\theta)"
                     rf"=({_LATEX[cs]},\ {_LATEX[ss]})\)",
             "note": "On a circle of radius 1 the point's coordinates ARE cos θ and sin θ."},
            {"label": "Read sin and cos straight off",
             "math": rf"\(\sin\theta={_LATEX[ss]},\quad \cos\theta={_LATEX[cs]}\)"},
            {"label": "tan from the ratio",
             "math": (r"\(\tan\theta=\dfrac{\sin\theta}{\cos\theta}=\text{undefined}\)"
                      if ts is None else
                      rf"\(\tan\theta=\dfrac{{\sin\theta}}{{\cos\theta}}={_LATEX[ts]}\)"),
             "note": tan_note},
        ]
    elif method == "cast":
        if m["axis"]:
            steps = [
                {"label": "Axis angle — no quadrant",
                 "math": rf"\(\theta={disp}\)",
                 "note": "This angle lies on an axis, so the CAST quadrant rule doesn't "
                         "apply; read the value directly off the unit circle."},
                {"label": "Values on the axis",
                 "math": rf"\(\sin\theta={_LATEX[ss]},\quad \cos\theta={_LATEX[cs]},"
                         rf"\quad \tan\theta="
                         + (r"\text{undefined}" if ts is None else _LATEX[ts]) + r"\)"},
            ]
        else:
            ref_disp = _disp_angle(m["ref"], unit)
            rs, rc, rt = _TABLE[m["ref"]]
            steps = [
                {"label": "Find the reference angle",
                 "math": rf"\(\theta={disp}\ \text{{ is in quadrant }}{m['quadrant']},"
                         rf"\ \text{{reference angle }}={ref_disp}\)",
                 "note": "The reference angle is the acute distance from θ to the x-axis."},
                {"label": "Read the magnitude off the reference angle",
                 "math": rf"\(\sin={_LATEX[rs]},\ \cos={_LATEX[rc]},"
                         rf"\ \tan=" + (r"\text{undef}" if rt is None else _LATEX[rt]) + r"\)",
                 "note": "Same magnitude as the matching first-quadrant special angle."},
                {"label": f"Apply CAST in quadrant {m['quadrant']}",
                 "math": rf"\(\sin\theta={_LATEX[ss]},\quad \cos\theta={_LATEX[cs]},"
                         rf"\quad \tan\theta="
                         + (r"\text{undefined}" if ts is None else _LATEX[ts]) + r"\)",
                 "note": _CAST[m["quadrant"]]},
            ]
    else:  # special-triangle
        if m["axis"]:
            steps = [
                {"label": "Axis angle — no triangle",
                 "math": rf"\(\theta={disp}\)",
                 "note": "Axis angles (0, 90°, 180°, 270°) don't form a triangle; their "
                         "values are read straight off the unit circle instead."},
                {"label": "Values from the unit circle",
                 "math": rf"\(\sin\theta={_LATEX[ss]},\quad \cos\theta={_LATEX[cs]},"
                         rf"\quad \tan\theta="
                         + (r"\text{undefined}" if ts is None else _LATEX[ts]) + r"\)"},
            ]
        else:
            tri = "45-45-90" if m["ref"] == 45 else "30-60-90"
            sides = (r"1:1:\sqrt{2}" if m["ref"] == 45 else r"1:\sqrt{3}:2")
            ref_disp = _disp_angle(m["ref"], unit)
            steps = [
                {"label": f"Use the {tri} triangle",
                 "math": rf"\(\text{{sides }}{sides}\)",
                 "note": f"The reference angle is {m['ref']}°, which sits in this set-square "
                         "triangle."},
                {"label": "Ratios at the reference angle",
                 "math": rf"\(\text{{at }}{ref_disp}:\ \sin={_LATEX[_TABLE[m['ref']][0]]},"
                         rf"\ \cos={_LATEX[_TABLE[m['ref']][1]]}\)",
                 "note": "Opposite/hypotenuse and adjacent/hypotenuse from the triangle."},
                {"label": f"Place it in quadrant {m['quadrant']} (CAST)",
                 "math": rf"\(\sin\theta={_LATEX[ss]},\quad \cos\theta={_LATEX[cs]},"
                         rf"\quad \tan\theta="
                         + (r"\text{undefined}" if ts is None else _LATEX[ts]) + r"\)",
                 "note": _CAST[m["quadrant"]]},
            ]

    return {
        "result": ss if ts is not None else ss,   # headline shows sin by convention
        "sin_surd": ss, "cos_surd": cs, "tan_surd": (ts if ts is not None else "undefined"),
        "sin": round(sin_f, 6), "cos": round(cos_f, 6),
        "tan": (None if tan_f is None else round(tan_f, 6)),
        "angle_deg": deg_key,
        "angle_display": disp,
        "angle_unit": unit,
        "method": method,
        "quadrant": m["quadrant"],
        "ref_angle": m["ref"],
        "axis": m["axis"],
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
