"""Lineup Impact — sports > Basketball.
Net rating (a real metric): points scored minus allowed per 100 possessions, while a
lineup is on court. Plus/minus per 100."""
from core.registry import register

@register(
    slug="lineup-impact",
    name="Lineup Impact Calculator",
    section="sports",
    sub="Basketball",
    tags=["basketball", "lineup", "net rating", "plus minus", "possessions", "impact"],
    formula="net rating = (points for \u2212 points against) / possessions \u00d7 100",
    summary="Measure a lineup's net rating \u2014 points outscored per 100 possessions while they are on the floor, the standard way to judge a five-man unit.",
    viz_template="viz/lineup-impact.html",
)
def compute(points_for: float = 58, points_against: float = 49, possessions: float = 52):
    try:
        pf = float(points_for); pa = float(points_against); poss = float(possessions)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if pf < 0 or pa < 0:
        return {"error": "Points cannot be negative."}
    if poss <= 0:
        return {"error": "Possessions must be greater than zero."}
    net = (pf - pa) / poss * 100
    off = pf / poss * 100
    deff = pa / poss * 100
    steps = [
        {"label": "Offensive rating", "math": r"\(" + ("%g" % pf) + r" / " + ("%g" % poss) + r" \times 100 = " + ("%.1f" % off) + r"\)", "note": "Points scored per 100 possessions."},
        {"label": "Defensive rating", "math": r"\(" + ("%g" % pa) + r" / " + ("%g" % poss) + r" \times 100 = " + ("%.1f" % deff) + r"\)", "note": "Points allowed per 100."},
        {"label": "Net rating", "math": r"\(" + ("%.1f" % off) + r" - " + ("%.1f" % deff) + r" = " + ("%+.1f" % net) + r"\)", "note": ("Outscoring opponents." if net >= 0 else "Being outscored.")},
    ]
    return {
        "result": ("Net rating " + ("%+.1f" % net) + " per 100 possessions"),
        "net_rating": round(net, 1), "offensive_rating": round(off, 1),
        "defensive_rating": round(deff, 1), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
