"""Water Intake — health › Diet & Nutrition.
Daily target from weight, exercise, and climate. Cylinder fill viz."""
from core.registry import register
from core.units import to_kg
from core.health_common import HEALTH_DISCLAIMER

# Seasonal options plus climate extras. Multiplier scales the baseline need.
CLIMATE = {
    "spring":    (1.00, "Spring"),
    "autumn":    (1.00, "Autumn"),
    "winter":    (0.95, "Winter"),
    "summer":    (1.15, "Summer"),
    "hot_humid": (1.20, "Hot / humid"),
    "dry_arid":  (1.18, "Dry / arid"),
}


@register(
    slug="water-intake",
    name="Water Intake Calculator",
    section="health",
    sub="Diet & Nutrition",
    tags=["water", "hydration", "fluid", "intake"],
    formula=r"Water (L) = weight(kg)·0.033 + (exercise min / 30)·0.35, ×climate",
    summary="A rough daily water-intake target from body weight, exercise, and climate.",
    viz_template="viz/water-intake.html",
)
def compute(weight_kg: float, exercise_min: float = 0.0, climate: str = "spring",
            weight_unit: str = "kg"):
    w = to_kg(weight_kg, weight_unit)
    ex = float(exercise_min)
    climate = str(climate).strip().lower()
    if climate not in CLIMATE:
        climate = "spring"
    if w <= 0 or ex < 0:
        return {"error": "Weight must be positive and exercise time cannot be negative.", "steps": []}

    base = w * 0.033
    exercise = (ex / 30.0) * 0.35
    mult, climate_label = CLIMATE[climate]
    litres = (base + exercise) * mult
    ounces = litres * 33.814

    steps = [
        {"label": "Base from body weight",
         "math": r"\( %g \times 0.033 = %.2f\text{ L} \)" % (w, base),
         "note": "About 33 mL of water per kilogram as a baseline."},
        {"label": "Add for exercise",
         "math": r"\( \dfrac{%g}{30}\times 0.35 = %.2f\text{ L} \)" % (ex, exercise),
         "note": "Roughly 350 mL extra for every 30 minutes of activity."},
        {"label": "Adjust for climate (%s)" % climate_label,
         "math": r"\( (%.2f + %.2f)\times %g = %.2f\text{ L} \)"
                 % (base, exercise, mult, litres)},
        {"label": "In ounces",
         "math": r"\( %.2f\text{ L} \approx %.0f\text{ fl oz} \)" % (litres, ounces)},
    ]
    return {
        "litres": round(litres, 2),
        "ounces": round(ounces),
        "glasses": round(litres / 0.25),   # 250 mL glasses
        "climate": climate,
        "disclaimer": HEALTH_DISCLAIMER,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
