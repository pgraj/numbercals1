"""Clinical Lab Value Converter — mmol/L ↔ mg/dL via molar mass.

Conventional units (mg/dL) and SI units (mmol/L) relate through the analyte's
molar mass:  mmol/L = (mg/dL × 10) ÷ molar_mass.
"""
from core.registry import register

# Full health disclaimer (unchanged §G text).
_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or system "
    "errors. They are general information only, not medical advice. Always consult "
    "a qualified professional — a doctor or accredited practitioner — before acting on them."
)

# analyte -> molar mass in g/mol (g/mol == mg/mmol)
_MOLAR_MASS = {
    "Glucose": 180.16,
    "Cholesterol": 386.65,
    "LDL": 386.65,
    "HDL": 386.65,
    "Creatinine": 113.12,
    "Urea/BUN": 60.06,
}

# HbA1c uses a separate linear relationship (IFCC), not a molar mass.
# mmol/mol (IFCC) = (DCCT% − 2.15) × 10.929
def _hba1c(value, unit):
    if unit == "%":  # DCCT/NGSP percent -> IFCC mmol/mol
        ifcc = (value - 2.15) * 10.929
        return ifcc, "mmol/mol"
    if unit == "mmol/mol":  # IFCC -> DCCT percent
        pct = value / 10.929 + 2.15
        return pct, "%"
    return None, None


_EXPLANATION = [
    {"heading": "Why lab results come in two unit systems",
     "body": "Conventional units (mg/dL — milligrams per decilitre) measure the MASS of a substance in blood. SI units (mmol/L — millimoles per litre) measure the NUMBER of molecules. Different countries and journals prefer different systems, so the same blood test can be quoted two ways."},
    {"heading": "The bridge is molar mass",
     "body": "To go between mass and molecules you need the substance's molar mass (grams per mole). The relationship is: mmol/L = (mg/dL × 10) ÷ molar mass. The ×10 fixes the dL-to-L and mg-to-g scaling. So the conversion factor is different for every analyte — glucose, cholesterol and creatinine each have their own molar mass."},
    {"heading": "Worked example (glucose)",
     "body": "Glucose has molar mass 180.16 g/mol. A reading of 100 mg/dL converts as (100 × 10) ÷ 180.16 ≈ 5.55 mmol/L — the familiar normal fasting value. A reading of 126 mg/dL (the diabetes threshold) is about 7.0 mmol/L."},
    {"heading": "HbA1c is the exception",
     "body": "HbA1c (long-term blood sugar) is reported as a percentage (older DCCT/NGSP) or mmol/mol (newer IFCC), related by a straight-line formula, not a molar mass: mmol/mol = (% − 2.15) × 10.929. So 7% ≈ 53 mmol/mol."},
]


@register(
    slug="clinical-units",
    name="Clinical Lab Value Converter",
    section="conversions",
    sub="2 · Advanced Converters",
    summary="Convert clinical lab values between conventional (mg/dL) and SI (mmol/L) units using each analyte's molar mass, plus HbA1c percent ↔ mmol/mol.",
    formula="mmol/L = (mg/dL × 10) ÷ molar mass;  mg/dL = (mmol/L × molar mass) ÷ 10",
    tags=["clinical", "lab", "mmol", "mg/dl", "glucose", "cholesterol", "hba1c", "converter"],
    viz_template="viz/clinical-units.html",
    scholar=None,
)
def compute(value=None, analyte=None, from_unit=None, **_ignored):
    if value is None or analyte is None or from_unit is None:
        return {"error": "Provide a value, an analyte, and the source unit.", "steps": []}
    try:
        v = float(value)
    except (TypeError, ValueError):
        return {"error": "Value must be a number.", "steps": []}
    if v < 0:
        return {"error": "Lab values cannot be negative.", "steps": []}
    a = str(analyte)
    fu = str(from_unit)

    if a == "HbA1c":
        result, to_unit = _hba1c(v, fu)
        if result is None:
            return {"error": "HbA1c units are % or mmol/mol.", "steps": []}
        steps = [
            {"label": "IFCC relationship",
             "math": f"{v:g} {fu} → {result:g} {to_unit}",
             "note": "HbA1c uses the IFCC linear formula, not a molar mass."},
        ]
        return {"result": result, "result_unit": to_unit, "analyte": a,
                "steps": steps, "disclaimer": _DISCLAIMER}

    mm = _MOLAR_MASS.get(a)
    if mm is None:
        return {"error": "Unknown analyte: " + a, "steps": []}

    if fu == "mg/dL":
        result = (v * 10.0) / mm
        to_unit = "mmol/L"
        math1 = f"({v:g} × 10) ÷ {mm:g} = {result:g} mmol/L"
    elif fu == "mmol/L":
        result = (v * mm) / 10.0
        to_unit = "mg/dL"
        math1 = f"({v:g} × {mm:g}) ÷ 10 = {result:g} mg/dL"
    else:
        return {"error": "Source unit must be mg/dL or mmol/L for " + a + ".", "steps": []}

    steps = [
        {"label": f"Molar mass of {a}", "math": f"{mm:g} g/mol"},
        {"label": "Convert", "math": math1},
    ]
    return {
        "result": result,
        "result_unit": to_unit,
        "analyte": a,
        "molar_mass": mm,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
