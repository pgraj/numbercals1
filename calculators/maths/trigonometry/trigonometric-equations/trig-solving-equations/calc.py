"""Solve a basic trig equation over a stated domain.  Stage 3 (Year 11 Advanced)."""
from __future__ import annotations
import math
from core.registry import register

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are provided for general reference only — always verify results "
    "independently before relying on them for academic or professional decisions."
)
def _fmt(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")
def _disp(deg, unit):
    return (_fmt(math.radians(deg)) + " rad") if unit=="rad" else (_fmt(deg)+"\u00b0")
def _tex(deg, unit):
    return (_fmt(math.radians(deg)) + r"\,\text{rad}") if unit=="rad" else (_fmt(deg)+r"^\circ")

_EXPLANATION = [
    {"heading":"One equation, many solutions",
     "body":"Because sine, cosine and tangent repeat, an equation like sin x = 0.5 has "
            "infinitely many solutions. You list only those inside the stated domain, "
            "usually one full turn."},
    {"heading":"Finding every solution in range",
     "body":"Take the principal value from the inverse function, then use the symmetry "
            "of the function (supplementary angle for sine, negative for cosine, "
            "180°/π period for tangent) to generate the rest, keeping those in the "
            "domain."},
    {"heading":"When there is no solution",
     "body":"sin x and cos x only take values from −1 to 1, so if the right-hand side "
            "is outside that range there is no solution. tan x can equal any real "
            "number."},
]

@register(
    slug="trig-solving-equations",
    name="Solving Trig Equations",
    section="maths", sub="Trigonometric Equations", topic="Trigonometry",
    order=10,
    summary="Solve sin x = k, cos x = k or tan x = k over a chosen domain (degrees or "
            "radians), listing every solution in range with the working shown.",
    formula="sin x = k → x = sin⁻¹k and its symmetric partners, within the domain",
    tags=["solving trig equations", "trig equation", "solutions in range",
          "domain", "Year 11 Mathematics Advanced"],
    viz_template="viz/trig-solving-equations.html",
    related=["trig-general-solution", "trig-exact-values"],
)
def compute(func="sin", k=0.5, angle_unit="deg", **_ignored):
    unit = "rad" if str(angle_unit)=="rad" else "deg"
    func = func if func in ("sin","cos","tan") else "sin"
    try:
        kv = float(k)
    except (TypeError,ValueError):
        return {"error":"The value k must be a number.","steps":[],"disclaimer":_DISCLAIMER}
    hi = 360.0  # domain [0,360) deg  /  [0,2π) rad
    sols = []
    if func in ("sin","cos"):
        if abs(kv) > 1:
            return {"error":f"{func} x is never more than 1 or less than −1, so "
                            f"{func} x = {_fmt(kv)} has no solution.","steps":[],
                    "disclaimer":_DISCLAIMER}
        if func=="sin":
            base = math.degrees(math.asin(kv))
            raw = [base, 180-base]
        else:
            base = math.degrees(math.acos(kv))
            raw = [base, 360-base]
    else:  # tan
        base = math.degrees(math.atan(kv))
        raw = [base, base+180]
    for x in raw:
        xx = x % 360
        if not any(abs(xx-e)<1e-6 for e in sols):
            sols.append(round(xx,4))
    sols.sort()

    inv = {"sin":r"\sin^{-1}","cos":r"\cos^{-1}","tan":r"\tan^{-1}"}[func]
    dom = r"[0,2\pi)" if unit=="rad" else r"[0^\circ,360^\circ)"
    sol_tex = ",\\ ".join(_tex(x,unit) for x in sols) if sols else r"\text{none}"
    steps = [
        {"label":"Take the principal value",
         "math":rf"\(x = {inv}({_fmt(kv)})\)",
         "note":"The inverse function gives the first solution."},
        {"label":"Use the symmetry to find the rest",
         "math":(r"\(\sin:\ 180^\circ-x;\quad \cos:\ 360^\circ-x;\quad \tan:\ x+180^\circ\)"),
         "note":"Generate the partner solutions, then keep those within the domain."},
        {"label":f"Solutions in {('[0,2π)' if unit=='rad' else '[0°,360°)')}",
         "math":rf"\(x = {sol_tex}\)",
         "note":f"{len(sols)} solution(s) in range."},
    ]
    return {
        "result": (", ".join(_disp(x,unit) for x in sols) if sols else "no solution"),
        "func":func, "k":kv, "solutions_deg":sols, "angle_unit":unit,
        "steps":steps, "explanation":_EXPLANATION, "disclaimer":_DISCLAIMER,
    }


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
