"""General solution of a trig equation — the full solution family.  Stage 3."""
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

_EXPLANATION = [
    {"heading":"Beyond one turn",
     "body":"Instead of listing solutions in a fixed domain, the general solution "
            "captures every solution at once using an integer n. It is the compact way "
            "to state an infinite family."},
    {"heading":"The three patterns",
     "body":"For sin x = sin α: x = α + 360°n or x = 180° − α + 360°n. For cos x = "
            "cos α: x = ±α + 360°n. For tan x = tan α: x = α + 180°n. In radians replace "
            "360° with 2π and 180° with π."},
    {"heading":"Why n matters",
     "body":"Each integer value of n (…,−1,0,1,…) gives one concrete solution. Choosing "
            "the n that lands inside a required domain recovers the in-range solutions."},
]

@register(
    slug="trig-general-solution",
    name="General Solution",
    section="maths", sub="Trigonometric Equations", topic="Trigonometry",
    order=20,
    summary="Write the general solution family for sin x = sinα, cos x = cosα or "
            "tan x = tanα, in degrees or radians, with the first few concrete "
            "solutions listed.",
    formula="sin: x=α+360°n or 180°−α+360°n; cos: x=±α+360°n; tan: x=α+180°n",
    tags=["general solution", "trig equation family", "+360n", "+2πn",
          "Year 11 Mathematics Advanced", "Extension 1"],
    viz_template="viz/trig-general-solution.html",
    related=["trig-solving-equations", "trig-exact-values"],
)
def compute(func="sin", alpha=30, angle_unit="deg", **_ignored):
    unit = "rad" if str(angle_unit)=="rad" else "deg"
    func = func if func in ("sin","cos","tan") else "sin"
    try:
        a_in=float(alpha)
    except (TypeError,ValueError):
        return {"error":"α must be a number.","steps":[],"disclaimer":_DISCLAIMER}
    ad = math.degrees(a_in) if unit=="rad" else a_in
    turn = "2\\pi" if unit=="rad" else "360^\\circ"
    half = "\\pi" if unit=="rad" else "180^\\circ"
    def at(deg): return (_fmt(math.radians(deg))+r"\,\text{rad}") if unit=="rad" else (_fmt(deg)+r"^\circ")
    def ap(deg): return (_fmt(math.radians(deg))+" rad") if unit=="rad" else (_fmt(deg)+"\u00b0")

    if func=="sin":
        general = rf"x = {at(ad)} + {turn}\,n \quad\text{{or}}\quad x = {half} - {at(ad)} + {turn}\,n"
        fam = [ad+360*n for n in (-1,0,1)] + [180-ad+360*n for n in (-1,0,1)]
    elif func=="cos":
        general = rf"x = \pm {at(ad)} + {turn}\,n"
        fam = [ad+360*n for n in (-1,0,1)] + [-ad+360*n for n in (-1,0,1)]
    else:
        general = rf"x = {at(ad)} + {half}\,n"
        fam = [ad+180*n for n in (-1,0,1,2)]
    fam = sorted(set(round(x,4) for x in fam))
    sep = ",\\ "
    fam_tex = sep.join(at(x) for x in fam)
    steps=[
        {"label":"State the general solution",
         "math":rf"\({general}\)",
         "note":"n is any integer; this covers every solution."},
        {"label":"List a few concrete solutions",
         "math":r"\(x \in \{" + fam_tex + r"\}\)",
         "note":"Each comes from a particular integer n."},
    ]
    # Plain-text result for the viz-out box (no LaTeX there).
    PI = "\u03c0"; DEG = "\u00b0"; MINUS = "\u2212"; PLUSMINUS = "\u00b1"
    turn_txt = ("2" + PI) if unit == "rad" else ("360" + DEG)
    half_txt = PI if unit == "rad" else ("180" + DEG)
    supp_lead = (PI + " " + MINUS + " ") if unit == "rad" else ("180" + DEG + " " + MINUS + " ")
    a_txt = ap(ad)
    if func == "sin":
        result_plain = ("x = " + a_txt + " + " + turn_txt + "n   or   x = "
                        + supp_lead + a_txt + " + " + turn_txt + "n")
    elif func == "cos":
        result_plain = "x = " + PLUSMINUS + a_txt + " + " + turn_txt + "n"
    else:
        result_plain = "x = " + a_txt + " + " + half_txt + "n"
    return {
        "result": result_plain,
        "func":func, "alpha_deg":ad, "family_deg":fam, "angle_unit":unit,
        "steps":steps, "explanation":_EXPLANATION, "disclaimer":_DISCLAIMER,
    }


from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
