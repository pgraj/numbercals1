"""Assist Impact — sports > Football / Soccer.
Goal involvement rate: (goals + assists) per 90, plus assists' share of involvements."""
from core.registry import register

@register(
    slug="assist-impact",
    name="Assist Impact Calculator",
    section="sports",
    sub="Football / Soccer",
    tags=["football", "soccer", "assist", "goal involvement", "creativity", "impact"],
    formula="involvements per 90 = (goals + assists) \u00d7 90 / minutes",
    summary="Measure a player's goal involvements (goals plus assists) per 90 minutes and how much of that is creating versus finishing.",
    viz_template="viz/assist-impact.html",
)
def compute(assists: float = 8, goals: float = 5, minutes: float = 2400):
    try:
        a = float(assists); g = float(goals); mins = float(minutes)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if a < 0 or g < 0:
        return {"error": "Goals and assists cannot be negative."}
    if mins <= 0:
        return {"error": "Minutes must be greater than zero."}
    involvements = a + g
    per90 = involvements * 90.0 / mins
    assist_share = (a / involvements * 100) if involvements > 0 else 0.0
    steps = [
        {"label": "Involvements", "math": r"\(" + ("%g" % g) + r" + " + ("%g" % a) + r" = " + ("%g" % involvements) + r"\)", "note": "Goals plus assists."},
        {"label": "Per 90", "math": r"\(" + ("%g" % involvements) + r" \times 90 / " + ("%g" % mins) + r" = " + ("%.2f" % per90) + r"\)", "note": "Rate over playing time."},
        {"label": "Assist share", "math": r"\(" + ("%.0f" % assist_share) + r"\%\)", "note": "How much of the output is creating chances vs scoring."},
    ]
    return {
        "result": (("%.2f" % per90) + " goal involvements per 90  (" + ("%.0f" % assist_share) + "% from assists)"),
        "involvements_per90": round(per90, 2), "total_involvements": involvements,
        "assist_share_percent": round(assist_share, 1), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
