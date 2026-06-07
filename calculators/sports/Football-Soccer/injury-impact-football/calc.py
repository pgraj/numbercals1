"""Injury Impact — sports > Football / Soccer.
Matches missed and the team's points-per-game drop while a key player is out.
Straightforward arithmetic (games x ppg gap), labelled as an estimate."""
from core.registry import register

@register(
    slug="injury-impact-football",
    name="Injury Impact Calculator",
    section="sports",
    sub="Football / Soccer",
    tags=["football", "soccer", "injury", "points", "availability", "impact"],
    formula="points lost \u2248 matches missed \u00d7 (ppg with player \u2212 ppg without)",
    summary="Estimate the league points a team forgoes while a key player is injured, from matches missed and the points-per-game difference with and without them.",
    viz_template="viz/injury-impact-football.html",
)
def compute(weeks_out: float = 6, matches_per_week: float = 1.0,
            ppg_with: float = 2.1, ppg_without: float = 1.4):
    try:
        w = float(weeks_out); mpw = float(matches_per_week)
        pw = float(ppg_with); pwo = float(ppg_without)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if w < 0 or mpw < 0:
        return {"error": "Weeks and matches cannot be negative."}
    if not (0 <= pw <= 3 and 0 <= pwo <= 3):
        return {"error": "Points per game must be between 0 and 3."}
    matches = w * mpw
    gap = pw - pwo
    points_lost = matches * gap
    steps = [
        {"label": "Matches missed", "math": r"\(" + ("%g" % w) + r" \times " + ("%g" % mpw) + r" = " + ("%.1f" % matches) + r"\)", "note": "Weeks out times matches per week."},
        {"label": "Points-per-game gap", "math": r"\(" + ("%.2f" % pw) + r" - " + ("%.2f" % pwo) + r" = " + ("%.2f" % gap) + r"\)", "note": "How much worse the team does without them."},
        {"label": "Points forgone", "math": r"\(" + ("%.1f" % matches) + r" \times " + ("%.2f" % gap) + r" = " + ("%.1f" % points_lost) + r"\)", "note": "Estimated league points lost."},
    ]
    return {
        "result": ("\u2248" + ("%.1f" % points_lost) + " league points forgone over " + ("%.0f" % matches) + " matches"),
        "matches_missed": round(matches, 1), "ppg_gap": round(gap, 2),
        "points_lost": round(points_lost, 1), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
