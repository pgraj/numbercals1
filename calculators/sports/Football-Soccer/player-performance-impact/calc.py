"""Player Performance Impact Score — sports > Football / Soccer.
ILLUSTRATIVE composite index from goals, assists, key passes, tackles and minutes.
A transparent weighted score for comparison only \u2014 NOT an official rating."""
from core.registry import register

@register(
    slug="player-performance-impact",
    name="Player Performance Impact Score Calculator",
    section="sports",
    sub="Football / Soccer",
    tags=["football", "soccer", "player", "performance", "rating", "impact", "index"],
    formula="score = (4\u00d7goals + 3\u00d7assists + 1\u00d7key passes + 1\u00d7tackles) per 90 min \u2014 illustrative weights",
    summary="A transparent weighted impact score per 90 minutes from goals, assists, key passes and tackles. Illustrative composite \u2014 weights are our own, not an official metric.",
    viz_template="viz/player-performance-impact.html",
)
def compute(goals: float = 1, assists: float = 1, key_passes: float = 3,
            tackles: float = 4, minutes: float = 90):
    try:
        g = float(goals); a = float(assists); kp = float(key_passes)
        tk = float(tackles); mins = float(minutes)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if any(v < 0 for v in (g, a, kp, tk)):
        return {"error": "Stats cannot be negative."}
    if mins <= 0:
        return {"error": "Minutes must be greater than zero."}
    raw = 4 * g + 3 * a + 1 * kp + 1 * tk
    per90 = raw * 90.0 / mins
    steps = [
        {"label": "Weighted raw", "math": r"\(4(" + ("%g" % g) + r")+3(" + ("%g" % a) + r")+" + ("%g" % kp) + r"+" + ("%g" % tk) + r" = " + ("%.1f" % raw) + r"\)", "note": "Goals and assists weighted highest."},
        {"label": "Per 90 min", "math": r"\(" + ("%.1f" % raw) + r" \times 90 / " + ("%g" % mins) + r" = " + ("%.2f" % per90) + r"\)", "note": "Normalised so subs and starters compare fairly."},
    ]
    return {
        "result": "Impact score \u2248 " + ("%.2f" % per90) + " per 90 min",
        "impact_per90": round(per90, 2), "raw_score": round(raw, 1),
        "model": "illustrative weighted index", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
