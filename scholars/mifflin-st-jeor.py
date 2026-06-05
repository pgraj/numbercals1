"""Scholar: the authors of the Mifflin-St Jeor equation, used by the BMR calculator."""
from core.registry import register_scholar

register_scholar(
    slug="mifflin-st-jeor",
    name="Mifflin & St Jeor",
    era="1990",
    field_of="Nutrition science",
    blurb="In 1990, M. D. Mifflin and S. T. St Jeor and colleagues published a new equation for "
          "estimating resting energy expenditure from weight, height, age, and sex. Built on data "
          "from healthy adults, it proved more accurate for modern populations than the "
          "Harris-Benedict equation it largely replaced, and it remains the standard formula "
          "behind most BMR and calorie calculators today.",
    source_name="Wikipedia — Basal metabolic rate",
    source_url="https://en.wikipedia.org/wiki/Basal_metabolic_rate",
)
