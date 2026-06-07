"""Defensive Impact Rating (Basketball) — sports > Basketball.
Stocks per game and a simple defensive workload per-36 index. ILLUSTRATIVE composite."""
from core.registry import register

@register(
    slug="defensive-impact-basketball",
    name="Defensive Impact Rating Calculator (Basketball)",
    section="sports",
    sub="Basketball",
    tags=["basketball", "defensive", "steals", "blocks", "rebounds", "impact", "index"],
    formula="rating = (steals + blocks + 0.5\u00d7def rebounds) \u00d7 36 / minutes \u2014 illustrative",
    summary="A transparent per-36-minute defensive index from steals, blocks and defensive rebounds. Illustrative composite, not an official defensive rating.",
    viz_template="viz/defensive-impact-basketball.html",
)
def compute(steals: float = 2, blocks: float = 1.5, defensive_rebounds: float = 6, minutes: float = 32):
    try:
        stl = float(steals); blk = float(blocks); dreb = float(defensive_rebounds); mins = float(minutes)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if any(v < 0 for v in (stl, blk, dreb)):
        return {"error": "Stats cannot be negative."}
    if mins <= 0:
        return {"error": "Minutes must be greater than zero."}
    stocks = stl + blk
    raw = stl + blk + 0.5 * dreb
    per36 = raw * 36.0 / mins
    steps = [
        {"label": "Stocks", "math": r"\(" + ("%g" % stl) + r" + " + ("%g" % blk) + r" = " + ("%.1f" % stocks) + r"\)", "note": "Steals + blocks, the classic defensive pair."},
        {"label": "Weighted raw", "math": r"\(" + ("%g + %g + 0.5(%g)" % (stl, blk, dreb)) + r" = " + ("%.1f" % raw) + r"\)", "note": "Defensive rebounds count half."},
        {"label": "Per 36 min", "math": r"\(" + ("%.1f" % raw) + r" \times 36 / " + ("%g" % mins) + r" = " + ("%.2f" % per36) + r"\)", "note": "Normalised to a starter's minutes."},
    ]
    return {
        "result": "Defensive impact \u2248 " + ("%.2f" % per36) + " per 36 min  (" + ("%.1f" % stocks) + " stocks)",
        "defensive_per36": round(per36, 2), "stocks": round(stocks, 1),
        "model": "illustrative weighted index", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
