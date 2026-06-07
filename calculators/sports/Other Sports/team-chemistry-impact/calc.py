"""Team Chemistry Impact — sports > Other Sports.
ILLUSTRATIVE composite \u2014 NOT an official metric. Blends games played together,
win rate together and continuity into a transparent 0\u2013100 chemistry index."""
from core.registry import register

@register(
    slug="team-chemistry-impact",
    name="Team Chemistry Impact Calculator",
    section="sports",
    sub="Other Sports",
    tags=["team", "chemistry", "continuity", "cohesion", "impact", "index"],
    formula="index = blend of games together, win rate together and squad continuity \u2014 illustrative",
    summary="A transparent, illustrative 0\u2013100 team-chemistry index from games played together, win rate as a unit and squad continuity. This is NOT an official metric \u2014 it is a made-up composite for discussion only.",
    viz_template="viz/team-chemistry-impact.html",
)
def compute(games_together: float = 30, win_rate_together_percent: float = 60,
            squad_continuity_percent: float = 75):
    try:
        gt = float(games_together); wr = float(win_rate_together_percent); cont = float(squad_continuity_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if gt < 0:
        return {"error": "Games cannot be negative."}
    if not (0 <= wr <= 100 and 0 <= cont <= 100):
        return {"error": "Percentages must be between 0 and 100."}
    # games-together maxes out its contribution at ~50 games
    familiarity = min(1.0, gt / 50.0) * 100
    index = 0.35 * familiarity + 0.40 * wr + 0.25 * cont
    if index >= 70:
        label = "high cohesion"
    elif index >= 45:
        label = "moderate cohesion"
    else:
        label = "still gelling"
    steps = [
        {"label": "Familiarity", "math": r"\(\min(1, " + ("%g" % gt) + r"/50) \times 100 = " + ("%.0f" % familiarity) + r"\)", "note": "Games together, capped at 50."},
        {"label": "Weighted blend", "math": r"\(0.35(" + ("%.0f" % familiarity) + r") + 0.40(" + ("%g" % wr) + r") + 0.25(" + ("%g" % cont) + r")\)", "note": "Win rate weighted highest."},
        {"label": "Chemistry index", "math": r"\(\approx " + ("%.0f" % index) + r"/100\)", "note": "Illustrative only \u2014 not an official measure."},
    ]
    return {
        "result": ("Chemistry index \u2248 " + ("%.0f" % index) + "/100 \u2014 " + label + " (illustrative)"),
        "chemistry_index": round(index, 0), "model": "illustrative \u2014 not official", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
