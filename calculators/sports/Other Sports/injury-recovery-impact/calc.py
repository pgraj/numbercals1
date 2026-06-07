"""Injury Recovery Impact — sports > Other Sports.
ILLUSTRATIVE return-to-play guide: typical recovery window scaled by severity and age.
A rough planning estimate ONLY \u2014 never medical advice (stated in result + FAQ)."""
from core.registry import register

@register(
    slug="injury-recovery-impact",
    name="Injury Recovery Impact Calculator",
    section="sports",
    sub="Other Sports",
    tags=["injury", "recovery", "return to play", "rehab", "impact", "estimate"],
    formula="estimated weeks \u2248 base weeks \u00d7 severity factor \u00d7 age factor \u2014 illustrative",
    summary="A rough, illustrative return-to-play timeline that scales a typical recovery window by severity and age. NOT medical advice \u2014 always follow a clinician.",
    viz_template="viz/injury-recovery-impact.html",
)
def compute(base_recovery_weeks: float = 6, severity_1to5: float = 3, age: float = 26):
    try:
        base = float(base_recovery_weeks); sev = float(severity_1to5); a = float(age)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if base < 0:
        return {"error": "Base recovery weeks cannot be negative."}
    if not (1 <= sev <= 5):
        return {"error": "Severity must be between 1 and 5."}
    if not (12 <= a <= 70):
        return {"error": "Age should be between 12 and 70."}
    severity_factor = 0.6 + (sev - 1) * 0.35   # 1 -> 0.6, 5 -> 2.0
    age_factor = 1.0 + max(0.0, (a - 30)) * 0.012  # older heals a little slower
    weeks = base * severity_factor * age_factor
    steps = [
        {"label": "Severity factor", "math": r"\(\times " + ("%.2f" % severity_factor) + r"\)", "note": "Higher severity stretches the timeline."},
        {"label": "Age factor", "math": r"\(\times " + ("%.2f" % age_factor) + r"\)", "note": ("Recovery slows slightly with age." if a > 30 else "Younger athletes often recover at the base rate.")},
        {"label": "Estimated window", "math": r"\(" + ("%g" % base) + r" \times " + ("%.2f" % severity_factor) + r" \times " + ("%.2f" % age_factor) + r" \approx " + ("%.1f" % weeks) + r"\text{ wks}\)", "note": "Rough planning estimate \u2014 not medical advice."},
    ]
    return {
        "result": ("\u2248 " + ("%.1f" % weeks) + " weeks (illustrative \u2014 follow your clinician)"),
        "estimated_weeks": round(weeks, 1), "severity_factor": round(severity_factor, 2),
        "age_factor": round(age_factor, 2), "model": "illustrative \u2014 not medical advice", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
