"""Points Impact — sports > Basketball.
True shooting % (a real, standard metric): TS% = PTS / (2 \u00d7 (FGA + 0.44\u00d7FTA))."""
from core.registry import register

@register(
    slug="points-impact",
    name="Points Impact Calculator",
    section="sports",
    sub="Basketball",
    tags=["basketball", "points", "true shooting", "scoring", "efficiency", "impact"],
    formula="TS% = PTS / (2 \u00d7 (FGA + 0.44 \u00d7 FTA)) \u00d7 100",
    summary="Measure scoring efficiency with true shooting percentage, which credits threes and free throws \u2014 the standard way to judge how well points are earned.",
    viz_template="viz/points-impact.html",
)
def compute(points: float = 28, field_goals_attempted: float = 18, free_throws_attempted: float = 6):
    try:
        pts = float(points); fga = float(field_goals_attempted); fta = float(free_throws_attempted)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if pts < 0 or fga < 0 or fta < 0:
        return {"error": "Values cannot be negative."}
    denom = 2 * (fga + 0.44 * fta)
    if denom <= 0:
        return {"error": "Enter at least one shot attempt."}
    ts = pts / denom * 100
    steps = [
        {"label": "Shooting possessions", "math": r"\(2(" + ("%g" % fga) + r" + 0.44 \times " + ("%g" % fta) + r") = " + ("%.2f" % denom) + r"\)", "note": "0.44 estimates free-throw trips."},
        {"label": "True shooting", "math": r"\(" + ("%g" % pts) + r" / " + ("%.2f" % denom) + r" = " + ("%.1f" % ts) + r"\%\)", "note": "Above ~55% is good; ~60%+ is elite."},
    ]
    return {
        "result": "True shooting = " + ("%.1f" % ts) + "%",
        "true_shooting_percent": round(ts, 1), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
