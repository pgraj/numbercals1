"""Acoustics & Signal Converter — logarithmic ratio units.

Decibels, Bels and Nepers are logarithmic; SPL in pascals and loudness in sones
relate non-linearly. We anchor on the decibel (power ratio) and provide the
standard acoustic mappings.
"""
import math
from core.registry import register

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions."
)

# Reference for SPL: 20 µPa = 0 dB SPL
_P_REF = 20e-6

# labelled reference points for the log slider (dB SPL)
_REFS = [
    {"label": "Whisper", "db": 30},
    {"label": "Conversation", "db": 60},
    {"label": "City traffic", "db": 85},
    {"label": "Jet engine", "db": 140},
]


def _to_db(v, unit):
    """Normalise an input to decibels (power-ratio dB / dB SPL)."""
    if unit == "dB":
        return v
    if unit == "Bel":
        return v * 10.0
    if unit == "Neper":
        # 1 Np = 20/ln(10) dB ≈ 8.685889638 dB (field quantity)
        return v * (20.0 / math.log(10.0))
    if unit == "SPL (Pa)":
        if v <= 0:
            return None
        return 20.0 * math.log10(v / _P_REF)
    if unit == "Sone":
        if v <= 0:
            return None
        # loudness level (phon) ≈ 40 + 10·log2(sone); approximate phon→dB at 1 kHz
        return 40.0 + 10.0 * math.log2(v)
    return None


def _from_db(db, unit):
    if unit == "dB":
        return db
    if unit == "Bel":
        return db / 10.0
    if unit == "Neper":
        return db * (math.log(10.0) / 20.0)
    if unit == "SPL (Pa)":
        return _P_REF * (10.0 ** (db / 20.0))
    if unit == "Sone":
        return 2.0 ** ((db - 40.0) / 10.0)
    return None


_EXPLANATION = [
    {"heading": "Why sound uses a logarithmic scale",
     "body": "Human hearing spans an enormous range — the loudest sound we tolerate carries about a trillion times the power of the quietest we can detect. Writing that with ordinary numbers is hopeless, so we use the decibel (dB), a logarithmic scale. Every +10 dB is ten times the power; every +20 dB is ten times the pressure."},
    {"heading": "What 0 dB really means",
     "body": "0 dB is not silence — it is the reference threshold of human hearing, a sound pressure of 20 micropascals. Everything is measured relative to that: dB = 20 × log₁₀(pressure ÷ 20 µPa). So the scale measures how many times louder than the faintest audible sound something is."},
    {"heading": "A feel for the numbers",
     "body": "Whisper ≈ 30 dB, normal conversation ≈ 60 dB, city traffic ≈ 85 dB, a jet engine close up ≈ 140 dB. Because the scale is logarithmic, 85 dB traffic is not 'a bit louder' than 60 dB speech — it carries about 300× the sound power."},
    {"heading": "Reading the slider",
     "body": "The slider places your value on this logarithmic loudness scale between labelled landmarks, so you can see not just the converted number but how that level compares to sounds you know. Bels, nepers and sones are alternative ratio/loudness units handled through the same decibel hub."},
]


@register(
    slug="convert-acoustics",
    name="Acoustics & Signal Converter",
    section="conversions",
    sub="2 · Mechanics & Fluids",
    summary="Convert acoustic and signal levels between decibels, bels, nepers, sound pressure (Pa) and sones on a logarithmic scale.",
    formula="dB = 20·log10(p/p_ref); p_ref = 20 µPa. 1 Bel = 10 dB; 1 Np = 20/ln10 dB.",
    tags=["acoustics", "decibel", "bel", "neper", "spl", "sone", "logarithmic", "converter"],
    viz_template="viz/convert-acoustics.html",
)
def compute(value=None, from_unit=None, to_unit=None, **_ignored):
    if value is None or from_unit is None or to_unit is None:
        return {"error": "Provide a value, a source unit, and a target unit.", "steps": []}
    try:
        v = float(value)
    except (TypeError, ValueError):
        return {"error": "Value must be a number.", "steps": []}
    fu, tu = str(from_unit), str(to_unit)

    db = _to_db(v, fu)
    if db is None:
        return {"error": "Value must be positive for " + fu + ".", "steps": []}
    result = _from_db(db, tu)
    if result is None:
        return {"error": "Unknown target unit: " + tu, "steps": []}

    steps = [
        {"label": "Normalise to decibels",
         "math": f"{v:g} {fu} → {db:g} dB"},
        {"label": "Decibels to target",
         "math": f"{db:g} dB → {result:g} {tu}"},
    ]
    return {
        "result": result,
        "result_unit": tu,
        "db": db,
        "references": _REFS,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
