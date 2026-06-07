"""Inverse trigonometric functions — arcsin, arccos, arctan with principal ranges.

Stage 3 (NSW Year 11 Mathematics Advanced).
"""
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

_RANGES = {
    "asin": ("arcsin", "[-90^\\circ, 90^\\circ]", "[-\\tfrac{\\pi}{2}, \\tfrac{\\pi}{2}]"),
    "acos": ("arccos", "[0^\\circ, 180^\\circ]", "[0, \\pi]"),
    "atan": ("arctan", "(-90^\\circ, 90^\\circ)", "(-\\tfrac{\\pi}{2}, \\tfrac{\\pi}{2})"),
}
_EXPLANATION = [
 {"heading":"What an inverse trig function does",
  "body":"It runs the trig function backwards: given a ratio, it returns the angle that "
         "produces it. arcsin(0.5) = 30° because sin 30° = 0.5."},
 {"heading":"Why the range is restricted",
  "body":"sin, cos and tan repeat, so without a rule the inverse would have infinitely "
         "many answers. Each inverse is given one principal range so it returns a single "
         "value: arcsin and arctan land in [−90°,90°], arccos in [0°,180°]."},
 {"heading":"Domain limits",
  "body":"arcsin and arccos only accept inputs from −1 to 1, because sine and cosine "
         "never exceed that. arctan accepts any real number."},
]

@register(
    slug="trig-inverse-functions",
    name="Inverse Trigonometric Functions",
    section="maths", sub="Advanced Applications", topic="Trigonometry",
    order=10,
    summary="Evaluate arcsin, arccos and arctan with their principal-value ranges, "
            "returning the angle in degrees or radians, with the full reasoning shown.",
    formula="arcsin x ∈ [−90°,90°]; arccos x ∈ [0°,180°]; arctan x ∈ (−90°,90°)",
    tags=["inverse trig", "arcsin", "arccos", "arctan", "principal value",
          "Year 11 Mathematics Advanced"],
    viz_template="viz/trig-inverse-functions.html",
    related=["trig-reciprocal", "trig-exact-values"],
)
def compute(fn="asin", value=0.5, angle_unit="deg", **_ignored):
    unit = "rad" if str(angle_unit)=="rad" else "deg"
    fn = fn if fn in _RANGES else "asin"
    try:
        x = float(value)
    except (TypeError, ValueError):
        return {"error":"The value must be a number.","steps":[],"disclaimer":_DISCLAIMER}
    if fn in ("asin","acos") and abs(x) > 1:
        name=_RANGES[fn][0]
        return {"error":f"{name} only accepts values between -1 and 1.","steps":[],
                "disclaimer":_DISCLAIMER}
    ang = {"asin":math.asin,"acos":math.acos,"atan":math.atan}[fn](x)
    deg = math.degrees(ang)
    name, rng_deg, rng_rad = _RANGES[fn]
    rng = rng_rad if unit=="rad" else rng_deg
    steps=[
        {"label":"Apply the inverse function",
         "math":rf"\(\theta = \{('arcsin' if fn=='asin' else 'arccos' if fn=='acos' else 'arctan')}({_fmt(x)})\)",
         "note":f"Find the angle whose {'sine' if fn=='asin' else 'cosine' if fn=='acos' else 'tangent'} is {_fmt(x)}."},
        {"label":"Take the principal value",
         "math":rf"\(\theta \in {rng}\)",
         "note":"The inverse returns the single value inside its principal range."},
        {"label":"Result",
         "math":rf"\(\theta \approx {_tex(deg,unit)}\)",
         "note":f"{name}({_fmt(x)}) = {_disp(deg,unit)}."},
    ]
    return {
        "result":_disp(deg,unit), "fn":fn, "value":x, "angle_deg":round(deg,4),
        "angle_unit":unit, "steps":steps, "explanation":_EXPLANATION, "disclaimer":_DISCLAIMER,
    }


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
