"""Temperature Converter — affine (offset) conversions via Kelvin.

Temperature scales are NOT simple multiplications: °C and °F have intercept
offsets, so we convert any input TO Kelvin first, then Kelvin to the target.
"""
from core.registry import register

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

# colour-banded zones on the dial (in °C), for the radial gauge viz
_ZONES = [
    {"label": "Freezing", "from_c": -50, "to_c": 0},
    {"label": "Comfortable", "from_c": 0, "to_c": 30},
    {"label": "Hot", "from_c": 30, "to_c": 45},
    {"label": "Danger", "from_c": 45, "to_c": 100},
]


def _to_kelvin(v, unit):
    if unit == "K":
        return v
    if unit == "°C":
        return v + 273.15
    if unit == "°F":
        return (v - 32.0) * 5.0 / 9.0 + 273.15
    if unit == "°R":  # Rankine
        return v * 5.0 / 9.0
    return None


def _from_kelvin(k, unit):
    if unit == "K":
        return k
    if unit == "°C":
        return k - 273.15
    if unit == "°F":
        return (k - 273.15) * 9.0 / 5.0 + 32.0
    if unit == "°R":
        return k * 9.0 / 5.0
    return None


_EXPLANATION = [
    {"heading": "Why temperature is special",
     "body": "Most conversions are a single multiplication (1 km = 1000 m). Temperature is not, because the Celsius and Fahrenheit scales put their zero in different places. Converting needs both a multiply AND an offset — an 'affine' transform — so we route every value through Kelvin, the absolute scale whose zero is the coldest possible temperature (−273.15 °C)."},
    {"heading": "The conversions, step by step",
     "body": "To Kelvin: from °C add 273.15; from °F do (°F − 32) × 5/9 + 273.15; from Rankine multiply by 5/9. Then Kelvin back out to your target reverses those. The 5/9 (and its inverse 9/5) appears because a Fahrenheit degree is smaller than a Celsius degree — there are 180 °F between water's freezing and boiling but only 100 °C."},
    {"heading": "Worked example and the dial",
     "body": "100 °C → 100 + 273.15 = 373.15 K → (373.15 − 273.15) × 9/5 + 32 = 212 °F (water boils). The dial gauge maps your temperature onto colour-banded comfort zones — freezing, comfortable, hot, danger — so the number lands in a human context. Nothing can read below 0 K, so the tool blocks impossible inputs."},
]


@register(
    slug="convert-temperature",
    name="Temperature Converter",
    section="conversions",
    sub="1 · Basic Converters",
    summary="Convert temperature between Celsius, Fahrenheit, Kelvin and Rankine using affine transforms via Kelvin.",
    formula="K = f(value); target = g(K). Affine: °C+273.15; (°F−32)×5/9+273.15; °R×5/9",
    tags=["temperature", "celsius", "fahrenheit", "kelvin", "rankine", "converter", "conversion"],
    viz_template="viz/convert-temperature.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    if value is None or from_unit is None or to_unit is None:
        return {"error": "Provide a value, a source unit, and a target unit.", "steps": []}
    try:
        v = float(value)
    except (TypeError, ValueError):
        return {"error": "Value must be a number.", "steps": []}
    fu, tu = str(from_unit), str(to_unit)

    k = _to_kelvin(v, fu)
    if k is None:
        return {"error": "Unknown source unit: " + fu, "steps": []}
    if k < 0:
        return {"error": "Result is below absolute zero (0 K). Check your input.", "steps": []}
    result = _from_kelvin(k, tu)
    if result is None:
        return {"error": "Unknown target unit: " + tu, "steps": []}

    celsius = k - 273.15
    steps = [
        {"label": "Convert source to Kelvin",
         "math": f"{v:g} {fu} → {k:g} K"},
        {"label": "Convert Kelvin to target",
         "math": f"{k:g} K → {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "kelvin": k,
        "celsius": celsius,
        "zones": _ZONES,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
