"""Ohm's Law: V = I R. Solve for voltage, current or resistance."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("Ohm's Law: the voltage across a resistor equals the current through it "
    "times its resistance, V = I R. Push harder (more voltage) and more current flows; add "
    "more resistance and less current flows.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Ohm's law"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Ohm%27s_law"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "What Ohm's Law says",
     "body": "Think of electricity like water in a pipe. Voltage is the push, current is "
             "how much flows, and resistance is how narrow the pipe is. Ohm's Law links "
             "them: voltage = current \u00d7 resistance."},
    {"heading": "How they trade off",
     "body": "For a fixed resistance, more voltage means more current. For a fixed voltage, "
             "more resistance means less current. That is why a thin wire (high resistance) "
             "lets less current through than a thick one."},
    {"heading": "Units",
     "body": "Voltage is in volts (V), current in amperes (A) and resistance in ohms "
             "(\u03a9). One volt across one ohm drives one ampere of current."},
]

@register(
    slug="ohms-law",
    name="Ohm's Law",
    section="physics",
    topic="Electricity",
    sub="Circuits",
    order=0,
    summary="Find voltage, current or resistance using Ohm's Law V = I R.",
    formula="V = I R",
    tags=["ohm", "voltage", "current", "resistance", "electricity", "circuit"],
    viz_template="viz/ohms-law.html",
    scholar="georg-ohm",
    related=["electrical-power"],
)
def compute(solve_for="voltage", voltage=None, current=2.0, resistance=5.0, **_ignored):
    try:
        sf = str(solve_for or "voltage").strip().lower()
    except Exception:
        sf = "voltage"

    def num(v):
        if v is None or v == "":
            return None
        return float(v)

    try:
        V = num(voltage); I = num(current); R = num(resistance)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    out_V, out_I, out_R = V, I, R
    steps = []
    result = ""

    if sf == "voltage":
        if I is None or R is None:
            return {"error": "Enter current and resistance to find voltage.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_V = I * R
        steps = [
            {"label": "Formula", "math": r"\(V = I R\)", "note": "Voltage = current times resistance."},
            {"label": "Substitute", "math": r"\(V = (" + _f(I) + r")(" + _f(R) + r")\)",
             "note": "Current in amperes, resistance in ohms."},
            {"label": "Result", "math": r"\(V = " + _f(out_V) + r"\ \text{V}\)", "note": "Voltage in volts."},
        ]
        result = "Voltage = " + _f(out_V) + " V"
    elif sf == "current":
        if V is None or R is None:
            return {"error": "Enter voltage and resistance to find current.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if R == 0:
            return {"error": "Resistance cannot be zero when solving for current.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_I = V / R
        steps = [
            {"label": "Rearrange", "math": r"\(I = \dfrac{V}{R}\)", "note": "Solve V = IR for current."},
            {"label": "Substitute", "math": r"\(I = \dfrac{" + _f(V) + r"}{" + _f(R) + r"}\)",
             "note": "Voltage in volts, resistance in ohms."},
            {"label": "Result", "math": r"\(I = " + _f(out_I) + r"\ \text{A}\)", "note": "Current in amperes."},
        ]
        result = "Current = " + _f(out_I) + " A"
    elif sf == "resistance":
        if V is None or I is None:
            return {"error": "Enter voltage and current to find resistance.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if I == 0:
            return {"error": "Current cannot be zero when solving for resistance.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        out_R = V / I
        steps = [
            {"label": "Rearrange", "math": r"\(R = \dfrac{V}{I}\)", "note": "Solve V = IR for resistance."},
            {"label": "Substitute", "math": r"\(R = \dfrac{" + _f(V) + r"}{" + _f(I) + r"}\)",
             "note": "Voltage in volts, current in amperes."},
            {"label": "Result", "math": r"\(R = " + _f(out_R) + r"\ \Omega\)", "note": "Resistance in ohms."},
        ]
        result = "Resistance = " + _f(out_R) + " \u03a9"
    else:
        return {"error": "Choose what to solve for: voltage, current or resistance.",
                "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": result, "solve_for": sf,
        "voltage": out_V, "current": out_I, "resistance": out_R,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME, "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
