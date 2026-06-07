"""CAC Impact Simulator — business-simulation > Models.
LTV:CAC ratio and payback period \u2014 the core unit-economics health check \u2014
simulated as CAC changes."""
from core.registry import register

@register(
    slug="cac-impact-simulator",
    name="CAC Impact Simulator",
    section="business-simulation",
    sub="Models",
    tags=["cac", "ltv", "unit economics", "payback", "ratio", "simulation", "saas"],
    formula="LTV:CAC ratio = LTV / CAC ; payback months = CAC / (ARPU \u00d7 margin)",
    summary="Simulate unit-economics health \u2014 the LTV:CAC ratio (3:1 is a common target) and the months to pay back acquisition cost \u2014 as CAC changes.",
    viz_template="viz/cac-impact-simulator.html",
)
def compute(ltv: float = 1200, current_cac: float = 400, new_cac: float = 300,
            arpu: float = 50, gross_margin_percent: float = 80):
    try:
        ltv_v = float(ltv); c0 = float(current_cac); c1 = float(new_cac)
        arpu_v = float(arpu); margin = float(gross_margin_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if ltv_v < 0 or arpu_v < 0:
        return {"error": "LTV and ARPU cannot be negative."}
    if c0 <= 0 or c1 <= 0:
        return {"error": "CAC must be greater than zero."}
    if not (0 <= margin <= 100):
        return {"error": "Gross margin must be between 0 and 100."}
    m = margin / 100.0
    ratio0 = ltv_v / c0
    ratio1 = ltv_v / c1
    monthly_contrib = arpu_v * m
    payback0 = c0 / monthly_contrib if monthly_contrib > 0 else None
    payback1 = c1 / monthly_contrib if monthly_contrib > 0 else None

    def verdict(r):
        if r >= 3: return "healthy (\u22653:1)"
        if r >= 1: return "thin \u2014 below the 3:1 guide"
        return "unprofitable (<1:1)"
    steps = [
        {"label": "Ratio now", "math": r"\(" + ("%.0f" % ltv_v) + r" / " + ("%.0f" % c0) + r" = " + ("%.2f" % ratio0) + r":1\)", "note": verdict(ratio0) + "."},
        {"label": "Ratio after", "math": r"\(" + ("%.0f" % ltv_v) + r" / " + ("%.0f" % c1) + r" = " + ("%.2f" % ratio1) + r":1\)", "note": verdict(ratio1) + "."},
        {"label": "Payback", "math": r"\(" + ("%.0f" % c1) + r" / (" + ("%g" % arpu_v) + r" \times " + ("%.2g" % m) + r") \approx " + (("%.1f" % payback1) if payback1 else "n/a") + r"\text{ mo}\)", "note": "Months of margin to recover the new CAC."},
    ]
    return {
        "result": ("LTV:CAC " + ("%.2f" % ratio0) + ":1 \u2192 " + ("%.2f" % ratio1) + ":1; payback \u2248 "
                   + (("%.1f" % payback1) if payback1 else "n/a") + " months"),
        "ratio_before": round(ratio0, 2), "ratio_after": round(ratio1, 2),
        "payback_before_months": (round(payback0, 1) if payback0 else None),
        "payback_after_months": (round(payback1, 1) if payback1 else None), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
