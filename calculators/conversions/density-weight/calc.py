"""Density & Shipping Weight Converter — volume → actual weight via material density.

weight (kg) = volume (m³) × density (kg/m³). Volume is normalised to m³ from a
chosen unit; density comes from a static material catalogue.
"""
from core.registry import register

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

# material -> density kg/m³
_DENSITY = {
    "Water (fresh)": 1000.0,
    "Seawater": 1025.0,
    "Petrol/Gasoline": 745.0,
    "Diesel": 832.0,
    "Honey": 1420.0,
    "Steel": 7850.0,
    "Aluminium": 2700.0,
    "Oak (wood)": 750.0,
    "Pine (wood)": 500.0,
    "Concrete": 2400.0,
}

# volume unit -> m³
_VOL_TO_M3 = {
    "L": 1e-3, "mL": 1e-6, "m³": 1.0, "cm³": 1e-6,
    "US gal": 0.003785411784, "ft³": 0.028316846592,
}

# mass unit -> kg (for output display selection)
_KG_TO = {"kg": 1.0, "g": 1e-3, "lb": 0.45359237, "t (metric)": 1e3}


_EXPLANATION = [
    {"heading": "Turning volume into weight",
     "body": "You often know a volume (a tank, a drum) but need the weight for shipping or structures. Density bridges them: weight = volume × density. Density is mass per unit volume (kg/m³), and it varies enormously between materials, which is why identical containers can weigh wildly different amounts."},
    {"heading": "Why the same volume weighs different amounts",
     "body": "Water is 1000 kg/m³ by definition (1 litre = 1 kg). Petrol is lighter at ~745 kg/m³, so 200 L of petrol weighs only ~149 kg versus 200 kg of water. Steel (~7850) and concrete (~2400) are far denser. The graph shows your chosen material against these references so the weight difference is visual, not just numerical."},
    {"heading": "Worked example",
     "body": "200 L of diesel (density 832 kg/m³): first 200 L = 0.2 m³, then 0.2 × 832 = 166.4 kg. Shipping clerks call this the 'actual weight', as opposed to volumetric/dimensional weight."},
]


@register(
    slug="density-weight",
    name="Density & Shipping Weight Converter",
    section="conversions",
    sub="3 · Thermal, Materials & Everyday",
    summary="Convert a volume of a material into its actual shipping weight using a built-in density catalogue (water, fuels, metals, woods, concrete).",
    formula="weight = volume × density",
    tags=["density", "weight", "shipping", "freight", "material", "converter"],
    viz_template="viz/density-weight.html",
)
def compute(volume=None, volume_unit=None, material=None, weight_unit=None, **_ignored):
    if volume is None or volume_unit is None or material is None:
        return {"error": "Provide a volume, its unit, and a material.", "steps": []}
    try:
        vol = float(volume)
    except (TypeError, ValueError):
        return {"error": "Volume must be a number.", "steps": []}
    if vol < 0:
        return {"error": "Volume cannot be negative.", "steps": []}

    vu = str(volume_unit)
    if vu not in _VOL_TO_M3:
        return {"error": "Unknown volume unit: " + vu, "steps": []}
    mat = str(material)
    if mat not in _DENSITY:
        return {"error": "Unknown material: " + mat, "steps": []}
    wu = str(weight_unit) if weight_unit in _KG_TO else "kg"

    m3 = vol * _VOL_TO_M3[vu]
    rho = _DENSITY[mat]
    kg = m3 * rho
    result = kg / _KG_TO[wu]

    steps = [
        {"label": "Volume to m³", "math": f"{vol:g} {vu} × {_VOL_TO_M3[vu]:g} = {m3:g} m³"},
        {"label": f"Density of {mat}", "math": f"{rho:g} kg/m³"},
        {"label": "Weight", "math": f"{m3:g} m³ × {rho:g} = {kg:g} kg = {result:g} {wu}"},
    ]
    return {
        "result": result,
        "result_unit": wu,
        "kilograms": kg,
        "density": rho,
        "material": mat,
        "densities": _DENSITY,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
