"""Strike Rate Impact (Cricket) — sports > Cricket.
Batting strike rate, the exact standard definition: runs per 100 balls."""
from core.registry import register

@register(
    slug="batting-strike-rate-impact",
    name="Strike Rate Impact Calculator",
    section="sports",
    sub="Cricket",
    tags=["cricket", "strike rate", "batting", "runs", "balls", "impact"],
    formula="strike rate = runs / balls faced \u00d7 100",
    summary="Batting strike rate \u2014 runs scored per 100 balls faced, the standard measure of scoring speed.",
    viz_template="viz/batting-strike-rate-impact.html",
)
def compute(runs: float = 75, balls_faced: float = 50):
    try:
        r = float(runs); b = float(balls_faced)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if r < 0:
        return {"error": "Runs cannot be negative."}
    if b <= 0:
        return {"error": "Balls faced must be greater than zero."}
    sr = r / b * 100
    steps = [
        {"label": "Formula", "math": r"\(\text{SR} = \dfrac{\text{runs}}{\text{balls}} \times 100\)", "note": "Runs per 100 balls."},
        {"label": "Substitute", "math": r"\(" + ("%g" % r) + r" / " + ("%g" % b) + r" \times 100 = " + ("%.2f" % sr) + r"\)", "note": "Higher is faster scoring."},
    ]
    return {
        "result": "Strike rate = " + ("%.2f" % sr),
        "strike_rate": round(sr, 2), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
