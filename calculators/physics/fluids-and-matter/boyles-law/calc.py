"""Boyle's Law: P1 V1 = P2 V2 at constant temperature. Pick what to solve for, and
optionally a container whose burst pressure flags when the gas would break it."""
from __future__ import annotations
from core.registry import register

_DISCLAIMER = ("These values are estimates and may contain computation, formula, "
    "or system errors. They are provided for general reference only \u2014 always verify "
    "results independently before relying on them for academic or professional "
    "decisions.")

_LAW_STATEMENT = ("At a constant temperature, the pressure of a fixed amount of gas is "
    "inversely proportional to its volume \u2014 squeeze it smaller and the pressure rises. "
    "So the product stays the same: P\u2081V\u2081 = P\u2082V\u2082.")
_LAW_SOURCE_NAME = "Wikipedia \u2014 Boyle's law"
_LAW_SOURCE_URL = "https://en.wikipedia.org/wiki/Boyle%27s_law"

# Approximate burst pressures (Pa), for illustration only \u2014 NOT engineering specs.
# Rough orders of magnitude: party balloon, plastic syringe, steel gas cylinder.
_CONTAINERS = {
    "none":     None,
    "balloon":  150000,      # ~150 kPa
    "syringe":  500000,      # ~500 kPa
    "steel":    20000000,    # ~20 MPa
}
_CONTAINER_LABEL = {
    "none": "No container limit",
    "balloon": "Party balloon (~150 kPa)",
    "syringe": "Plastic syringe (~500 kPa)",
    "steel": "Steel cylinder (~20 MPa)",
}

def _f(x):
    if x is None: return ""
    if abs(x - round(x)) < 1e-9: return str(int(round(x)))
    return ("%.4f" % x).rstrip("0").rstrip(".")

_EXPLANATION = [
    {"heading": "What Boyle's Law says",
     "body": "Push on a trapped gas and it squeezes into a smaller space, and its pressure "
             "goes up. Give it more room and the pressure drops. As long as the "
             "temperature stays the same, pressure and volume always trade off this way."},
    {"heading": "Why pressure times volume stays constant",
     "body": "If you halve the volume, the pressure exactly doubles; if you triple the "
             "volume, the pressure falls to a third. Multiply pressure by volume and you "
             "always get the same number, which is why P\u2081V\u2081 = P\u2082V\u2082."},
    {"heading": "Real containers have a limit",
     "body": "The gas law itself never stops, but a real container can. Push the pressure "
             "past what a balloon, syringe or cylinder can hold and it bursts. Pick a "
             "container to see the pressure at which it would fail \u2014 these are rough "
             "illustrative values, not engineering specifications."},
]

@register(
    slug="boyles-law",
    name="Boyle's Law",
    section="physics",
    topic="Fluids & Matter",
    sub="Gas Laws",
    order=2,
    summary="Use Boyle's Law P1 V1 = P2 V2 at constant temperature; choose what to solve for, and check a container's burst limit.",
    formula="P\u2081V\u2081 = P\u2082V\u2082",
    tags=["boyle", "gas law", "pressure", "volume", "gas", "fluids", "matter", "burst"],
    viz_template="viz/boyles-law.html",
    related=["pressure", "density", "archimedes-principle"],
)
def compute(solve_for="p2", p1=100.0, v1=2.0, p2=200.0, v2=1.0,
            container="none", **_ignored):
    try:
        sf = str(solve_for or "p2").strip().lower()
    except Exception:
        sf = "p2"

    cont = str(container or "none").strip().lower()
    burst = _CONTAINERS.get(cont)

    def num(v):
        if v is None or v == "":
            return None
        return float(v)

    try:
        P1 = num(p1); V1 = num(v1); P2 = num(p2); V2 = num(v2)
    except (TypeError, ValueError):
        return {"error": "Please enter numbers only.", "steps": [], "disclaimer": _DISCLAIMER}

    steps = [
        {"label": "Boyle's Law", "math": r"\(P_1 V_1 = P_2 V_2\)",
         "note": "At constant temperature, pressure times volume stays constant."},
    ]
    result = ""

    if sf == "v2":
        if P1 is None or V1 is None or P2 is None:
            return {"error": "Enter P\u2081, V\u2081 and P\u2082 to find V\u2082.", "steps": [], "disclaimer": _DISCLAIMER}
        if P2 == 0:
            return {"error": "P\u2082 cannot be zero when solving for V\u2082.", "steps": [], "disclaimer": _DISCLAIMER}
        V2 = (P1 * V1) / P2
        steps += [
            {"label": "Rearrange", "math": r"\(V_2 = \dfrac{P_1 V_1}{P_2}\)", "note": "Solve for the final volume."},
            {"label": "Substitute", "math": r"\(V_2 = \dfrac{(" + _f(P1) + r")(" + _f(V1) + r")}{" + _f(P2) + r"}\)", "note": "Use the same units on both sides."},
            {"label": "Result", "math": r"\(V_2 = " + _f(V2) + r"\)", "note": "Final volume."},
        ]
        result = "V\u2082 = " + _f(V2)
    elif sf == "p2":
        if P1 is None or V1 is None or V2 is None:
            return {"error": "Enter P\u2081, V\u2081 and V\u2082 to find P\u2082.", "steps": [], "disclaimer": _DISCLAIMER}
        if V2 == 0:
            return {"error": "V\u2082 cannot be zero when solving for P\u2082.", "steps": [], "disclaimer": _DISCLAIMER}
        P2 = (P1 * V1) / V2
        steps += [
            {"label": "Rearrange", "math": r"\(P_2 = \dfrac{P_1 V_1}{V_2}\)", "note": "Solve for the final pressure."},
            {"label": "Substitute", "math": r"\(P_2 = \dfrac{(" + _f(P1) + r")(" + _f(V1) + r")}{" + _f(V2) + r"}\)", "note": "Use the same units on both sides."},
            {"label": "Result", "math": r"\(P_2 = " + _f(P2) + r"\)", "note": "Final pressure."},
        ]
        result = "P\u2082 = " + _f(P2)
    elif sf == "v1":
        if P1 is None or P2 is None or V2 is None:
            return {"error": "Enter P\u2081, P\u2082 and V\u2082 to find V\u2081.", "steps": [], "disclaimer": _DISCLAIMER}
        if P1 == 0:
            return {"error": "P\u2081 cannot be zero when solving for V\u2081.", "steps": [], "disclaimer": _DISCLAIMER}
        V1 = (P2 * V2) / P1
        steps += [
            {"label": "Rearrange", "math": r"\(V_1 = \dfrac{P_2 V_2}{P_1}\)", "note": "Solve for the initial volume."},
            {"label": "Substitute", "math": r"\(V_1 = \dfrac{(" + _f(P2) + r")(" + _f(V2) + r")}{" + _f(P1) + r"}\)", "note": "Use the same units on both sides."},
            {"label": "Result", "math": r"\(V_1 = " + _f(V1) + r"\)", "note": "Initial volume."},
        ]
        result = "V\u2081 = " + _f(V1)
    elif sf == "p1":
        if V1 is None or P2 is None or V2 is None:
            return {"error": "Enter V\u2081, P\u2082 and V\u2082 to find P\u2081.", "steps": [], "disclaimer": _DISCLAIMER}
        if V1 == 0:
            return {"error": "V\u2081 cannot be zero when solving for P\u2081.", "steps": [], "disclaimer": _DISCLAIMER}
        P1 = (P2 * V2) / V1
        steps += [
            {"label": "Rearrange", "math": r"\(P_1 = \dfrac{P_2 V_2}{V_1}\)", "note": "Solve for the initial pressure."},
            {"label": "Substitute", "math": r"\(P_1 = \dfrac{(" + _f(P2) + r")(" + _f(V2) + r")}{" + _f(V1) + r"}\)", "note": "Use the same units on both sides."},
            {"label": "Result", "math": r"\(P_1 = " + _f(P1) + r"\)", "note": "Initial pressure."},
        ]
        result = "P\u2081 = " + _f(P1)
    else:
        return {"error": "Choose what to solve for: P\u2081, V\u2081, P\u2082 or V\u2082.",
                "steps": [], "disclaimer": _DISCLAIMER}

    # Container burst check against the final pressure P2.
    # If the computed P2 exceeds what the container can hold, the material would break
    # or permanently deform: we CAP the reported pressure at the burst limit and flag
    # it, rather than letting P2 run away as a meaningless ever-rising number.
    burst_exceeded = None
    burst_note = ""
    p2_uncapped = P2          # the raw value the gas law gives
    p2_capped = False
    if burst is not None and P2 is not None:
        burst_exceeded = P2 > burst
        if burst_exceeded:
            p2_capped = True
            burst_note = ("The pressure needed (" + _f(P2) + " Pa) is beyond the ~" +
                          _f(burst) + " Pa this container can take. At this point the "
                          "material breaks or permanently deforms \u2014 it cannot be "
                          "squeezed further, so the pressure is capped at the burst "
                          "limit. (Illustrative value, not an engineering specification.)")
            # Pin the reported P2 at the burst limit, and adjust the headline result if
            # we were solving for P2 so the number shown is the capped one.
            P2 = burst
            if sf == "p2":
                result = ("P\u2082 reaches the container's limit of " + _f(burst) +
                          " Pa \u2014 beyond this the material would break or deform.")
        else:
            burst_note = ("The final pressure " + _f(P2) + " is within the ~" + _f(burst) +
                          " Pa this container can hold. (Illustrative value, not an "
                          "engineering specification.)")

    return {
        "result": result,
        "solve_for": sf,
        "p1": P1, "v1": V1, "p2": P2, "v2": V2,
        "p2_uncapped": p2_uncapped,
        "p2_capped": p2_capped,
        "container": cont,
        "container_label": _CONTAINER_LABEL.get(cont, "No container limit"),
        "burst_pressure": burst,
        "burst_exceeded": burst_exceeded,
        "burst_note": burst_note,
        "steps": steps,
        "explanation": _EXPLANATION,
        "law_statement": _LAW_STATEMENT,
        "law_source_name": _LAW_SOURCE_NAME,
        "law_source_url": _LAW_SOURCE_URL,
        "disclaimer": _DISCLAIMER,
    }

from core.faqs import load_sibling_faq  # noqa: E402
load_sibling_faq(__file__)
