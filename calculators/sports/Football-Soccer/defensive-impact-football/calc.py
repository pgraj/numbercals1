"""Defensive Impact Rating (Football) — sports > Football / Soccer.
ILLUSTRATIVE composite of tackles, interceptions, clearances, blocks per 90 minutes."""
from core.registry import register

@register(
    slug="defensive-impact-football",
    name="Defensive Impact Rating Calculator (Football)",
    section="sports",
    sub="Football / Soccer",
    tags=["football", "soccer", "defensive", "tackles", "interceptions", "impact", "index"],
    formula="rating = (tackles + interceptions + clearances + 2\u00d7blocks) \u00d7 90 / minutes \u2014 illustrative",
    summary="A transparent per-90 defensive workload index from tackles, interceptions, clearances and blocks. Illustrative composite, not an official rating.",
    viz_template="viz/defensive-impact-football.html",
)
def compute(tackles: float = 3, interceptions: float = 2, clearances: float = 4,
            blocks: float = 1, minutes: float = 90):
    try:
        tk = float(tackles); inter = float(interceptions); cl = float(clearances)
        bl = float(blocks); mins = float(minutes)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if any(v < 0 for v in (tk, inter, cl, bl)):
        return {"error": "Stats cannot be negative."}
    if mins <= 0:
        return {"error": "Minutes must be greater than zero."}
    raw = tk + inter + cl + 2 * bl
    per90 = raw * 90.0 / mins
    steps = [
        {"label": "Weighted actions", "math": r"\(" + ("%g" % tk) + r"+" + ("%g" % inter) + r"+" + ("%g" % cl) + r"+2(" + ("%g" % bl) + r") = " + ("%.1f" % raw) + r"\)", "note": "Blocks weighted double (last-ditch)."},
        {"label": "Per 90", "math": r"\(" + ("%.1f" % raw) + r" \times 90 / " + ("%g" % mins) + r" = " + ("%.2f" % per90) + r"\)", "note": "Normalised to a full match."},
    ]
    return {
        "result": "Defensive impact \u2248 " + ("%.2f" % per90) + " per 90 min",
        "defensive_per90": round(per90, 2), "raw_actions": round(raw, 1),
        "model": "illustrative weighted index", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
