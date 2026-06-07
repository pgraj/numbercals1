"""Economy Rate Impact (Cricket) — sports > Cricket.
Bowling economy rate, the exact standard definition: runs conceded per over."""
from core.registry import register

@register(
    slug="economy-rate-impact",
    name="Economy Rate Impact Calculator",
    section="sports",
    sub="Cricket",
    tags=["cricket", "economy rate", "bowling", "runs", "overs", "impact"],
    formula="economy = runs conceded / overs bowled",
    summary="Bowling economy rate \u2014 runs conceded per over, the standard measure of how restrictive a bowler is. Balls are converted to overs (6 balls = 1 over).",
    viz_template="viz/economy-rate-impact.html",
)
def compute(runs_conceded: float = 42, overs: float = 8, balls_extra: float = 0):
    try:
        r = float(runs_conceded); ov = float(overs); be = float(balls_extra)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if r < 0 or ov < 0 or be < 0:
        return {"error": "Values cannot be negative."}
    total_overs = ov + be / 6.0
    if total_overs <= 0:
        return {"error": "Enter the overs bowled."}
    econ = r / total_overs
    steps = [
        {"label": "Total overs", "math": r"\(" + ("%g" % ov) + r" + " + ("%g" % be) + r"/6 = " + ("%.3f" % total_overs) + r"\)", "note": "Six balls make one over."},
        {"label": "Economy", "math": r"\(" + ("%g" % r) + r" / " + ("%.3f" % total_overs) + r" = " + ("%.2f" % econ) + r"\)", "note": "Lower is more economical."},
    ]
    return {
        "result": "Economy rate = " + ("%.2f" % econ) + " runs/over",
        "economy_rate": round(econ, 2), "total_overs": round(total_overs, 3), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
