"""Ideal Weight — health › Body Composition.
Devine formula (feet+inches). Shows a healthy span around the Devine point,
and where the user's current weight falls relative to it."""
from core.registry import register
from core.units import to_kg, height_to_inches, height_to_cm
from core.health_common import HEALTH_DISCLAIMER


def _bmi_status(weight_kg: float, height_cm: float):
    """Weight-status verdict via BMI, so it stays consistent with the BMI calculator."""
    if weight_kg <= 0 or height_cm <= 0:
        return None, None
    h = height_cm / 100.0
    bmi = weight_kg / (h * h)
    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"
    return round(bmi, 1), status


def _devine(sex: str, inches_over_5ft: float) -> float:
    over = max(0.0, inches_over_5ft)
    male = 50.0 + 2.3 * over
    female = 45.5 + 2.3 * over
    if sex == "male":
        return male
    if sex == "female":
        return female
    return (male + female) / 2.0


@register(
    slug="ideal-weight",
    name="Ideal Weight Calculator",
    section="health",
    sub="Body Composition",
    tags=["ideal weight", "devine", "healthy weight", "range"],
    formula=r"Devine: men 50 kg + 2.3 kg/inch over 5 ft · women 45.5 kg + 2.3 kg/inch",
    summary="A classic ideal-weight estimate (Devine formula) with a healthy range around it.",
    viz_template="viz/ideal-weight.html",
)
def compute(sex: str, height_ft: float, height_in: float = 0.0, current_weight_kg: float = 0.0,
            height_unit: str = "ft", weight_unit: str = "kg"):
    sex = str(sex).strip().lower()
    if sex not in ("male", "female", "other"):
        sex = "other"
    # Devine works in inches over 5 ft; accept any height unit and normalise.
    total_inches = height_to_inches(height_ft, height_unit, height_in)
    height_cm = height_to_cm(height_ft, height_unit, height_in)
    cur = to_kg(current_weight_kg, weight_unit)
    if total_inches <= 0:
        return {"error": "Height must be greater than zero.", "steps": []}

    over = total_inches - 60.0   # inches over 5 feet
    point = _devine(sex, over)

    # A healthy span: Devine point is a single figure, so show ±~10% as a band.
    low = round(point * 0.90, 1)
    high = round(point * 1.10, 1)

    # Weight-status verdict (BMI-based) for the entered current weight.
    bmi_val, status = _bmi_status(cur, height_cm) if cur > 0 else (None, None)

    relation = None
    if cur > 0:
        if cur < low:
            relation = "below"
        elif cur > high:
            relation = "above"
        else:
            relation = "within"

    steps = [
        {"label": "Height in inches over 5 ft",
         "math": r"\( %.1f\text{ in},\ \text{over 5 ft} = %.1f\text{ in} \)"
                 % (total_inches, max(0.0, over)),
         "note": "Devine counts only the inches above 5 feet (60 inches)."},
        {"label": "Apply the Devine formula",
         "math": r"\( \text{ideal} \approx %.1f\text{ kg} \)" % point},
        {"label": "Healthy span (±10%)",
         "math": r"\( %.1f \text{–} %.1f\text{ kg} \)" % (low, high),
         "note": "A single formula gives one number; the band reflects healthy individual variation."},
    ]
    if status:
        steps.append({
            "label": "Weight status of your current weight",
            "math": r"\( \text{BMI } %.1f \Rightarrow \text{%s} \)" % (bmi_val, status),
            "note": "The verdict uses BMI, so it agrees with the BMI calculator."})
    return {
        "ideal_kg": round(point, 1),
        "low_kg": low,
        "high_kg": high,
        "current_kg": round(cur, 1) if cur > 0 else None,
        "relation": relation,
        "status": status,
        "bmi": bmi_val,
        "disclaimer": HEALTH_DISCLAIMER,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
