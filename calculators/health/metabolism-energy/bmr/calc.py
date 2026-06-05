"""BMR — health › Metabolism & Energy.
Mifflin-St Jeor. Bar chart compares resting BMR against everyday energy references.
Gender: male/female are the defined formula variants; 'other' averages the two."""
from core.registry import register
from core.units import to_kg, height_to_cm
from core.health_common import HEALTH_DISCLAIMER


def _bmr(sex: str, w: float, h_cm: float, age: float) -> float:
    base = 10 * w + 6.25 * h_cm - 5 * age
    male = base + 5
    female = base - 161
    if sex == "male":
        return male
    if sex == "female":
        return female
    return (male + female) / 2.0   # 'other' -> midpoint of the two formula variants


@register(
    slug="bmr",
    name="BMR Calculator",
    section="health",
    sub="Metabolism & Energy",
    tags=["bmr", "basal metabolic rate", "calories", "metabolism", "mifflin"],
    formula=r"BMR = 10·w(kg) + 6.25·h(cm) − 5·age  (+5 male / −161 female)",
    summary="Basal Metabolic Rate — the calories your body burns at complete rest — via the Mifflin-St Jeor equation.",
    viz_template="viz/bmr.html",
    scholar="mifflin-st-jeor",
)
def compute(sex: str, age: float, weight_kg: float, height_cm: float,
            weight_unit: str = "kg", height_unit: str = "cm", height_in2: float = 0.0):
    sex = str(sex).strip().lower()
    if sex not in ("male", "female", "other"):
        sex = "other"
    w = to_kg(weight_kg, weight_unit)
    h_cm = height_to_cm(height_cm, height_unit, height_in2)
    age = float(age)
    if w <= 0 or h_cm <= 0 or age <= 0:
        return {"error": "Age, weight and height must all be greater than zero.", "steps": []}

    bmr = _bmr(sex, w, h_cm, age)
    bmr_r = round(bmr)

    sign = "+5" if sex == "male" else ("-161" if sex == "female" else "average of +5 and -161")
    steps = [
        {"label": "List the values",
         "math": r"\( w = %g\text{ kg},\ h = %g\text{ cm},\ \text{age} = %g \)" % (w, h_cm, age)},
        {"label": "Weight and height terms",
         "math": r"\( 10\times%g + 6.25\times%g = %.1f \)" % (w, h_cm, 10*w + 6.25*h_cm)},
        {"label": "Subtract the age term",
         "math": r"\( %.1f - 5\times%g = %.1f \)" % (10*w + 6.25*h_cm, age, 10*w + 6.25*h_cm - 5*age)},
        {"label": "Apply the sex constant (%s)" % sign,
         "math": r"\( \text{BMR} \approx %d \text{ kcal/day} \)" % bmr_r,
         "note": "Male adds 5, female subtracts 161; 'other' takes the midpoint of both."},
    ]
    # Comparison references (generic, illustrative kcal/day) for the bar chart.
    refs = [
        {"label": "Your BMR", "kcal": bmr_r, "self": True},
        {"label": "100 W light bulb", "kcal": 2064, "self": False},   # 100W over 24h ≈ 2064 kcal
        {"label": "Sleeping 8h", "kcal": round(bmr_r / 3), "self": False},
        {"label": "Small dog/day", "kcal": 400, "self": False},
    ]
    return {
        "bmr": bmr_r,
        "sex": sex,
        "series": refs,
        "disclaimer": HEALTH_DISCLAIMER,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
