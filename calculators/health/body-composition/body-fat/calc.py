"""Body Fat — health › Body Composition.
US Navy circumference method (inches). Donut: fat mass vs lean mass.
NOTE: height is required by the Navy formula; it was added to the inputs."""
import math
from core.registry import register
from core.units import to_kg, to_inches, height_to_inches
from core.health_common import HEALTH_DISCLAIMER


@register(
    slug="body-fat",
    name="Body Fat Calculator",
    section="health",
    sub="Body Composition",
    tags=["body fat", "navy method", "lean mass", "fat mass", "composition"],
    formula=r"US Navy: men 86.010·log₁₀(waist−neck) − 70.041·log₁₀(height) + 36.76",
    summary="Body-fat percentage via the US Navy tape method, split into fat mass and lean mass.",
    viz_template="viz/body-fat.html",
)
def compute(sex: str, weight_kg: float, height_in: float, waist_in: float,
            neck_in: float, hip_in: float = 0.0,
            weight_unit: str = "kg", length_unit: str = "in",
            height_unit: str = "in", height_in2: float = 0.0):
    sex = str(sex).strip().lower()
    if sex not in ("male", "female", "other"):
        sex = "other"
    # Mass -> kg for the fat/lean split; circumferences -> inches for the Navy formula.
    w = to_kg(weight_kg, weight_unit)
    h = height_to_inches(height_in, height_unit, height_in2)
    waist = to_inches(waist_in, length_unit)
    neck = to_inches(neck_in, length_unit)
    hip = to_inches(hip_in, length_unit) if hip_in else 0.0

    if w <= 0 or h <= 0 or waist <= 0 or neck <= 0:
        return {"error": "Weight, height, waist and neck must all be greater than zero.", "steps": []}

    def male_pct():
        if waist - neck <= 0:
            return None
        return 86.010 * math.log10(waist - neck) - 70.041 * math.log10(h) + 36.76

    def female_pct():
        if waist + hip - neck <= 0:
            return None
        return 163.205 * math.log10(waist + hip - neck) - 97.684 * math.log10(h) - 78.387

    if sex == "male":
        pct = male_pct()
    elif sex == "female":
        if hip <= 0:
            return {"error": "Hip circumference is required for the female formula.", "steps": []}
        pct = female_pct()
    else:  # other -> average whichever variants are computable
        vals = [v for v in (male_pct(), female_pct() if hip > 0 else None) if v is not None]
        pct = sum(vals) / len(vals) if vals else None

    if pct is None:
        return {"error": "Those measurements don't form a valid body — check waist, neck and hip.",
                "steps": []}

    pct = max(2.0, min(60.0, pct))   # clamp to a physically sensible range
    fat_mass = w * pct / 100.0
    lean_mass = w - fat_mass

    steps = [
        {"label": "Measurements (inches)",
         "math": r"\( \text{waist}=%g,\ \text{neck}=%g,\ \text{height}=%g%s \)"
                 % (waist, neck, h, (r",\ \text{hip}=%g" % hip) if (sex != "male" and hip > 0) else "")},
        {"label": "Apply the US Navy formula",
         "math": r"\( \text{body fat} \approx %.1f\%% \)" % pct,
         "note": "A log-based estimate from tape measurements; results are approximate."},
        {"label": "Fat mass",
         "math": r"\( %g \times %.1f\%% = %.1f\text{ kg} \)" % (w, pct, fat_mass)},
        {"label": "Lean mass",
         "math": r"\( %g - %.1f = %.1f\text{ kg} \)" % (w, fat_mass, lean_mass)},
    ]
    return {
        "body_fat_pct": round(pct, 1),
        "fat_mass_kg": round(fat_mass, 1),
        "lean_mass_kg": round(lean_mass, 1),
        "weight_kg": round(w, 1),
        "disclaimer": HEALTH_DISCLAIMER,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
