"""Player Efficiency Impact — sports > Basketball.
The NBA 'efficiency' (EFF) formula \u2014 a real, standard box-score metric:
EFF = (PTS+REB+AST+STL+BLK) \u2212 (missed FG + missed FT + TO). Per-game or total."""
from core.registry import register

@register(
    slug="player-efficiency-impact",
    name="Player Efficiency Impact Calculator",
    section="sports",
    sub="Basketball",
    tags=["basketball", "efficiency", "eff", "per", "box score", "impact"],
    formula="EFF = (PTS + REB + AST + STL + BLK) \u2212 (missed FG + missed FT + turnovers)",
    summary="The standard NBA efficiency (EFF) rating from a box-score line \u2014 positive contributions minus misses and turnovers.",
    viz_template="viz/player-efficiency-impact.html",
)
def compute(points: float = 24, rebounds: float = 8, assists: float = 6, steals: float = 2,
            blocks: float = 1, fg_missed: float = 7, ft_missed: float = 2, turnovers: float = 3):
    try:
        vals = [float(x) for x in (points, rebounds, assists, steals, blocks, fg_missed, ft_missed, turnovers)]
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if any(v < 0 for v in vals):
        return {"error": "Stats cannot be negative."}
    pts, reb, ast, stl, blk, fgm, ftm, to = vals
    positive = pts + reb + ast + stl + blk
    negative = fgm + ftm + to
    eff = positive - negative
    steps = [
        {"label": "Positives", "math": r"\(" + ("%g+%g+%g+%g+%g" % (pts, reb, ast, stl, blk)) + r" = " + ("%.0f" % positive) + r"\)", "note": "Points, rebounds, assists, steals, blocks."},
        {"label": "Negatives", "math": r"\(" + ("%g+%g+%g" % (fgm, ftm, to)) + r" = " + ("%.0f" % negative) + r"\)", "note": "Missed shots and turnovers."},
        {"label": "EFF", "math": r"\(" + ("%.0f" % positive) + r" - " + ("%.0f" % negative) + r" = " + ("%.0f" % eff) + r"\)", "note": "The standard NBA efficiency rating."},
    ]
    return {
        "result": "Efficiency (EFF) = " + ("%.0f" % eff),
        "efficiency": round(eff, 1), "positive": positive, "negative": negative, "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
