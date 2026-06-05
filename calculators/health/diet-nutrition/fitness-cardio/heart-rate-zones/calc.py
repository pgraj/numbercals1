"""Heart Rate Zones — health › Fitness & Cardio.
Max HR = 220 - age. With a resting HR, uses Karvonen (heart-rate reserve).
Five training zones rendered as a segmented horizontal bar."""
from core.registry import register
from core.health_common import HEALTH_DISCLAIMER

# (label, lower %, upper %, tone) — standard 5-zone model.
ZONES = [
    ("Warm up",   0.50, 0.60, "z1"),
    ("Fat burn",  0.60, 0.70, "z2"),
    ("Aerobic",   0.70, 0.80, "z3"),
    ("Anaerobic", 0.80, 0.90, "z4"),
    ("Red line",  0.90, 1.00, "z5"),
]


@register(
    slug="heart-rate-zones",
    name="Heart Rate Zone Calculator",
    section="health",
    sub="Fitness & Cardio",
    tags=["heart rate", "zones", "karvonen", "cardio", "training"],
    formula=r"Max HR = 220 − age · Karvonen: target = HRR·%I + resting",
    summary="Maximum heart rate and the five training zones, using the Karvonen method when a resting rate is given.",
    viz_template="viz/heart-rate-zones.html",
    scholar="karvonen",
)
def compute(age: float, resting_hr: float = 0.0):
    age = float(age)
    rhr = float(resting_hr)
    if age <= 0 or age > 120:
        return {"error": "Enter an age between 1 and 120.", "steps": []}
    if rhr < 0 or rhr > 200:
        return {"error": "Resting heart rate looks out of range.", "steps": []}

    max_hr = 220 - age
    use_karvonen = rhr > 0
    hrr = max_hr - rhr if use_karvonen else None

    def target(pct):
        if use_karvonen:
            return round(hrr * pct + rhr)
        return round(max_hr * pct)

    zones = []
    for label, lo, hi, tone in ZONES:
        zones.append({
            "label": label, "tone": tone,
            "low_pct": round(lo * 100), "high_pct": round(hi * 100),
            "low_bpm": target(lo), "high_bpm": target(hi),
        })

    steps = [
        {"label": "Estimate maximum heart rate",
         "math": r"\( \text{Max HR} = 220 - %g = %d \text{ bpm} \)" % (age, round(max_hr))},
    ]
    if use_karvonen:
        steps.append({
            "label": "Heart-rate reserve (Karvonen)",
            "math": r"\( \text{HRR} = %d - %g = %d \text{ bpm} \)" % (round(max_hr), rhr, round(hrr)),
            "note": "Karvonen scales each zone within your reserve, then adds your resting rate."})
        steps.append({
            "label": "A zone target, e.g. aerobic lower edge (70%)",
            "math": r"\( %d \times 0.70 + %g = %d \text{ bpm} \)"
                    % (round(hrr), rhr, target(0.70))})
    else:
        steps.append({
            "label": "Zone target, e.g. aerobic lower edge (70%)",
            "math": r"\( %d \times 0.70 = %d \text{ bpm} \)" % (round(max_hr), target(0.70)),
            "note": "Add a resting heart rate to switch to the more personalised Karvonen method."})

    return {
        "max_hr": round(max_hr),
        "resting_hr": round(rhr) if use_karvonen else None,
        "method": "Karvonen" if use_karvonen else "Percentage of max",
        "zones": zones,
        "disclaimer": HEALTH_DISCLAIMER,
        "steps": steps,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
