"""Goal Impact on Win Probability — sports > Football / Soccer.
ILLUSTRATIVE MODEL: a logistic function of goal difference and time remaining.
This is a simplified teaching model, not an official or bookmaker probability."""
from core.registry import register
import math

@register(
    slug="goal-win-probability-impact",
    name="Goal Impact on Win Probability Calculator",
    section="sports",
    sub="Football / Soccer",
    tags=["football", "soccer", "goal", "win probability", "impact", "model"],
    formula="P(win) \u2248 logistic(k \u00d7 goal_diff \u00d7 time_weight) \u2014 illustrative model",
    summary="Estimate how scoring (or conceding) a goal shifts win probability, using a simplified logistic model of goal difference and time remaining. Illustrative, not official odds.",
    viz_template="viz/goal-win-probability-impact.html",
)
def compute(goal_diff_before: float = 0, minute: float = 60, scored: str = "for"):
    try:
        gd = float(goal_diff_before); m = float(minute)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if not (0 <= m <= 120):
        return {"error": "Minute must be between 0 and 120."}
    s = str(scored or "for").strip().lower()
    gd_after = gd + (1 if s == "for" else -1)

    def winprob(diff, minute):
        # time weight: a lead late in the game is worth more (less time to recover)
        tw = 0.6 + 1.4 * (minute / 90.0)
        return 1.0 / (1.0 + math.exp(-0.8 * diff * tw))

    wp0 = winprob(gd, m)
    wp1 = winprob(gd_after, m)
    swing = (wp1 - wp0) * 100
    steps = [
        {"label": "Before", "math": r"\(P_0 = " + ("%.1f" % (wp0*100)) + r"\%\)", "note": "Win chance at goal difference " + ("%g" % gd) + ", minute " + ("%g" % m) + "."},
        {"label": "After the goal", "math": r"\(P_1 = " + ("%.1f" % (wp1*100)) + r"\%\)", "note": "Goal difference becomes " + ("%g" % gd_after) + "."},
        {"label": "Swing", "math": r"\(" + ("+" if swing >= 0 else "") + ("%.1f" % swing) + r"\text{ pts}\)", "note": "Later goals swing probability more \u2014 less time to respond."},
    ]
    return {
        "result": ("Win probability " + ("%.1f" % (wp0*100)) + "% \u2192 " + ("%.1f" % (wp1*100))
                   + "%  (" + ("+" if swing >= 0 else "") + ("%.1f" % swing) + " pts)"),
        "win_prob_before": round(wp0*100, 1), "win_prob_after": round(wp1*100, 1),
        "swing": round(swing, 1), "model": "illustrative logistic", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
