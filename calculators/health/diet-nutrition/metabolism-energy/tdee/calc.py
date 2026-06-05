"""TDEE — health › Metabolism & Energy.
Total Daily Energy Expenditure = BMR x activity factor.
Stacked column: BMR base block + active-energy block on top."""
from core.registry import register
from core.units import to_kg, height_to_cm
from core.health_common import HEALTH_DISCLAIMER

ACTIVITY = {
    "sedentary":   (1.2,   "Little or no exercise"),
    "light":       (1.375, "Light exercise 1–3 days/week"),
    "moderate":    (1.55,  "Moderate exercise 3–5 days/week"),
    "active":      (1.725, "Hard exercise 6–7 days/week"),
    "extra":       (1.9,   "Very hard exercise or physical job"),
}


def _bmr(sex: str, w: float, h_cm: float, age: float) -> float:
    base = 10 * w + 6.25 * h_cm - 5 * age
    if sex == "male":
        return base + 5
    if sex == "female":
        return base - 161
    return ((base + 5) + (base - 161)) / 2.0


@register(
    slug="tdee",
    name="TDEE Calculator",
    section="health",
    sub="Metabolism & Energy",
    tags=["tdee", "total daily energy expenditure", "calories", "activity", "maintenance"],
    formula=r"TDEE = BMR × activity factor (1.2 sedentary … 1.9 extra active)",
    summary="Total Daily Energy Expenditure — your resting burn scaled up by how active you are.",
    viz_template="viz/tdee.html",
)
def compute(sex: str, age: float, weight_kg: float, height_cm: float, activity: str = "sedentary",
            weight_unit: str = "kg", height_unit: str = "cm", height_in2: float = 0.0):
    sex = str(sex).strip().lower()
    if sex not in ("male", "female", "other"):
        sex = "other"
    activity = str(activity).strip().lower()
    if activity not in ACTIVITY:
        activity = "sedentary"
    w = to_kg(weight_kg, weight_unit)
    h_cm = height_to_cm(height_cm, height_unit, height_in2)
    age = float(age)
    if w <= 0 or h_cm <= 0 or age <= 0:
        return {"error": "Age, weight and height must all be greater than zero.", "steps": []}

    bmr = _bmr(sex, w, h_cm, age)
    factor, desc = ACTIVITY[activity]
    tdee = bmr * factor
    active = tdee - bmr   # energy above resting

    steps = [
        {"label": "Start from resting burn (BMR)",
         "math": r"\( \text{BMR} \approx %d \text{ kcal/day} \)" % round(bmr),
         "note": "Calculated with Mifflin-St Jeor, the same as the BMR calculator."},
        {"label": "Pick the activity factor",
         "math": r"\( \text{%s} \Rightarrow \times %g \)" % (activity.title(), factor),
         "note": desc + "."},
        {"label": "Multiply",
         "math": r"\( \text{TDEE} = %d \times %g \approx %d \text{ kcal/day} \)"
                 % (round(bmr), factor, round(tdee))},
        {"label": "Energy above rest",
         "math": r"\( %d - %d \approx %d \text{ kcal/day} \)"
                 % (round(tdee), round(bmr), round(active))},
    ]
    return {
        "bmr": round(bmr),
        "tdee": round(tdee),
        "active": round(active),
        "factor": factor,
        "activity": activity,
        "disclaimer": HEALTH_DISCLAIMER,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
