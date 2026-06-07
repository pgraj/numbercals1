"""Electrical Power: P = V I (= I^2 R = V^2 / R). Solve power from a valid pair."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("Electrical power is the rate at which a device uses energy. It equals "
    "voltage times current, P = V I, and can also be written P = I\u00b2R or P = V\u00b2/R "
    "using Ohm's law.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Electric power"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Electric_power"

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "What electrical power means",
     "body": "Power tells you how fast a device turns electrical energy into light, heat or "
             "motion. A 100 W bulb uses energy ten times faster than a 10 W one. The basic "
             "rule is power = voltage \u00d7 current."},
    {"heading": "Three ways to write it",
     "body": "Using Ohm's law (V = IR) you can swap things in: P = V\u00d7I, or P = "
             "I\u00b2\u00d7R if you know current and resistance, or P = V\u00b2\u00f7R if you "
             "know voltage and resistance. They all give the same power."},
    {"heading": "Units",
     "body": "Power is in watts (W). One watt is one joule of energy per second. Voltage is "
             "in volts, current in amperes, resistance in ohms."},
]

@register(
    slug="electrical-power",
    name="Electrical Power",
    section="physics",
    topic="Electricity",
    sub="Circuits",
    order=1,
    summary="Find electrical power from voltage and current (P = VI), or from current and resistance, or voltage and resistance.",
    formula="P = V I = I\u00b2R = V\u00b2/R",
    tags=["power", "watt", "voltage", "current", "resistance", "electricity"],
    viz_template="viz/electrical-power.html",
    scholar="georg-ohm",
    related=["ohms-law", "mechanical-power"],
)
def compute(method="vi", voltage=12.0, current=2.0, resistance=6.0, **_ignored):
    try:
        mt = str(method or "vi").strip().lower()
    except Exception:
        mt = "vi"

    def num(v):
        if v is None or v == "":
            return None
        return float(v)

    try:
        V = num(voltage); I = num(current); R = num(resistance)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    P = None
    steps = []

    if mt == "vi":
        if V is None or I is None:
            return {"error": "Enter voltage and current to find power.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        P = V * I
        steps = [
            {"label": "Formula", "math": r"\(P = V I\)", "note": "Power = voltage times current."},
            {"label": "Substitute", "math": r"\(P = (" + _f(V) + r")(" + _f(I) + r")\)",
             "note": "Voltage in volts, current in amperes."},
            {"label": "Result", "math": r"\(P = " + _f(P) + r"\ \text{W}\)", "note": "Power in watts."},
        ]
    elif mt == "ir":
        if I is None or R is None:
            return {"error": "Enter current and resistance to find power.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        P = I * I * R
        steps = [
            {"label": "Formula", "math": r"\(P = I^2 R\)", "note": "Power from current and resistance."},
            {"label": "Substitute", "math": r"\(P = (" + _f(I) + r")^2 (" + _f(R) + r")\)",
             "note": "Current in amperes, resistance in ohms."},
            {"label": "Result", "math": r"\(P = " + _f(P) + r"\ \text{W}\)", "note": "Power in watts."},
        ]
    elif mt == "vr":
        if V is None or R is None:
            return {"error": "Enter voltage and resistance to find power.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        if R == 0:
            return {"error": "Resistance cannot be zero when using P = V\u00b2/R.",
                    "steps": [], "disclaimer": _DISCLAIMER}
        P = (V * V) / R
        steps = [
            {"label": "Formula", "math": r"\(P = \dfrac{V^2}{R}\)", "note": "Power from voltage and resistance."},
            {"label": "Substitute", "math": r"\(P = \dfrac{(" + _f(V) + r")^2}{" + _f(R) + r"}\)",
             "note": "Voltage in volts, resistance in ohms."},
            {"label": "Result", "math": r"\(P = " + _f(P) + r"\ \text{W}\)", "note": "Power in watts."},
        ]
    else:
        return {"error": "Choose a method: vi (V\u00d7I), ir (I\u00b2R) or vr (V\u00b2/R).",
                "steps": [], "disclaimer": _DISCLAIMER}

    return {
        "result": "Power = " + _f(P) + " W",
        "method": mt, "power": P,
        "voltage": V, "current": I, "resistance": R,
        "steps": steps, "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME, "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
