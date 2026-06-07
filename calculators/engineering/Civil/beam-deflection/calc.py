"""Simple beam deflection — engineering > Civil. Midspan deflection, simply-supported, central point load.
Educational use only, NOT for design."""
from core.registry import register

@register(
    slug="beam-deflection",
    name="Simple Beam Deflection Calculator (Point Load, Centre)",
    section="engineering",
    sub="Civil",
    tags=["beam", "deflection", "point load", "simply supported", "civil", "structural", "education"],
    formula="\u03b4 = P L\u00b3 / (48 E I)  (simply supported, central point load)",
    summary="Estimate midspan deflection of a simply-supported beam under a central point load, using the standard PL\u00b3/48EI formula. Educational use only \u2014 not for design.",
    viz_template="viz/beam-deflection.html",
)
def compute(load_N: float = 10000, span_m: float = 4,
            youngs_modulus_GPa: float = 200, moment_of_inertia_cm4: float = 8000):
    try:
        P = float(load_N); L = float(span_m)
        E_GPa = float(youngs_modulus_GPa); I_cm4 = float(moment_of_inertia_cm4)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if P < 0:
        return {"error": "Load cannot be negative."}
    if L <= 0:
        return {"error": "Span must be greater than zero."}
    if E_GPa <= 0 or I_cm4 <= 0:
        return {"error": "Modulus and moment of inertia must be greater than zero."}
    E = E_GPa * 1e9            # Pa
    I = I_cm4 * 1e-8           # m^4  (1 cm^4 = 1e-8 m^4)
    delta = P * L ** 3 / (48 * E * I)   # metres
    delta_mm = delta * 1000
    ratio = (L / delta) if delta > 0 else None
    steps = [
        {"label": "Convert units", "math": r"\(E = " + ("%g" % E_GPa) + r"\,\text{GPa},\ I = " + ("%g" % I_cm4) + r"\,\text{cm}^4\)", "note": "Worked in SI: E in Pa, I in m\u2074."},
        {"label": "Deflection formula", "math": r"\(\delta = \dfrac{P L^3}{48 E I}\)", "note": "Standard case: simply supported, load at centre."},
        {"label": "Result", "math": r"\(\delta \approx " + ("%.4g" % delta_mm) + r"\,\text{mm}\)", "note": ("Span/deflection ratio \u2248 L/" + ("%.0f" % ratio) + "." if ratio else "")},
    ]
    return {
        "result": ("Midspan deflection \u2248 " + ("%.4g" % delta_mm) + " mm"
                   + ((" (span/deflection \u2248 L/" + ("%.0f" % ratio) + ")") if ratio else "")),
        "deflection_mm": round(delta_mm, 4), "deflection_m": round(delta, 8),
        "span_over_deflection": (round(ratio, 1) if ratio else None),
        "disclaimer": "Educational estimate only \u2014 not for structural design. Real beams need code checks, factored loads and a qualified engineer.",
        "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
