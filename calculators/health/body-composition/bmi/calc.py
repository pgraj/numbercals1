"""BMI — health › Body Composition.
Colour-coded horizontal gauge with a needle at the user's score.
Bands: <18.5 underweight, 18.5-25 normal, 25-30 overweight, >=30 obese (WHO)."""
from core.registry import register
from core.units import to_kg, height_to_cm
from core.health_common import HEALTH_DISCLAIMER


def _status(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"


@register(
    slug="bmi",
    name="BMI Calculator",
    section="health",
    sub="Body Composition",
    tags=["bmi", "body mass index", "weight status", "health"],
    formula=r"BMI = weight (kg) / [height (m)]²",
    summary="Body Mass Index from weight and height, with the WHO weight-status band it falls in.",
    viz_template="viz/bmi.html",
)
def compute(weight_kg: float, height_cm: float,
            weight_unit: str = "kg", height_unit: str = "cm", height_in2: float = 0.0):
    # Normalise to canonical units (kg, cm); raw values may arrive in any unit.
    w = to_kg(weight_kg, weight_unit)
    h_cm = height_to_cm(height_cm, height_unit, height_in2)
    if w <= 0 or h_cm <= 0:
        return {"error": "Weight and height must be greater than zero.", "steps": []}

    h = h_cm / 100.0
    bmi = w / (h * h)
    status = _status(bmi)

    steps = [
        {"label": "Convert height to metres",
         "math": r"\( h = %g\text{ cm} \div 100 = %.3f\text{ m} \)" % (h_cm, h),
         "note": "BMI uses height in metres, so divide centimetres by 100."},
        {"label": "Square the height",
         "math": r"\( h^2 = %.3f^2 = %.4f\text{ m}^2 \)" % (h, h * h)},
        {"label": "Divide weight by height squared",
         "math": r"\( \text{BMI} = \dfrac{%g}{%.4f} = %.1f \)" % (w, h * h, bmi)},
        {"label": "Read the band",
         "math": r"\( %.1f \Rightarrow \text{%s} \)" % (bmi, status),
         "note": "Bands: under 18.5 underweight · 18.5–25 normal · 25–30 overweight · 30+ obese."},
    ]
    # Bands drive the coloured gauge; needle sits at `bmi` clamped to the scale.
    bands = [
        {"label": "Underweight", "from": 10.0, "to": 18.5, "tone": "low"},
        {"label": "Normal", "from": 18.5, "to": 25.0, "tone": "ok"},
        {"label": "Overweight", "from": 25.0, "to": 30.0, "tone": "warn"},
        {"label": "Obese", "from": 30.0, "to": 40.0, "tone": "high"},
    ]
    return {
        "bmi": round(bmi, 1),
        "status": status,
        "scale_min": 10.0,
        "scale_max": 40.0,
        "bands": bands,
        "disclaimer": HEALTH_DISCLAIMER,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
