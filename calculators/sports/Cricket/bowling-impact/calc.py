"""Bowling Impact Rating (Cricket) — sports > Cricket.
ILLUSTRATIVE composite of wickets and economy versus a par economy. Transparent weights."""
from core.registry import register

@register(
    slug="bowling-impact",
    name="Bowling Impact Rating Calculator",
    section="sports",
    sub="Cricket",
    tags=["cricket", "bowling", "impact", "wickets", "economy", "index"],
    formula="rating = wickets\u00d725 + (par economy \u2212 economy)\u00d7overs \u2014 illustrative",
    summary="A transparent bowling impact rating combining wickets taken with runs saved against a par economy rate. Illustrative composite, not an official metric.",
    viz_template="viz/bowling-impact.html",
)
def compute(wickets: float = 3, runs_conceded: float = 28, overs: float = 4, par_economy: float = 8.0):
    try:
        w = float(wickets); r = float(runs_conceded); ov = float(overs); par = float(par_economy)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if w < 0 or r < 0:
        return {"error": "Wickets and runs cannot be negative."}
    if ov <= 0:
        return {"error": "Overs must be greater than zero."}
    if par <= 0:
        return {"error": "Par economy must be greater than zero."}
    econ = r / ov
    runs_saved = (par - econ) * ov
    rating = w * 25 + runs_saved
    steps = [
        {"label": "Economy", "math": r"\(" + ("%g" % r) + r" / " + ("%g" % ov) + r" = " + ("%.2f" % econ) + r"\)", "note": "Runs conceded per over."},
        {"label": "Runs saved", "math": r"\((" + ("%g" % par) + r" - " + ("%.2f" % econ) + r") \times " + ("%g" % ov) + r" = " + ("%+.1f" % runs_saved) + r"\)", "note": "Versus a par bowler over the same overs."},
        {"label": "Impact rating", "math": r"\(" + ("%g" % w) + r" \times 25 + " + ("%+.1f" % runs_saved) + r" = " + ("%.1f" % rating) + r"\)", "note": "Each wicket weighted at 25 'run-equivalents'."},
    ]
    return {
        "result": "Bowling impact \u2248 " + ("%.1f" % rating) + "  (" + ("%g" % w) + " wkts, econ " + ("%.2f" % econ) + ")",
        "impact_rating": round(rating, 1), "economy": round(econ, 2), "runs_saved": round(runs_saved, 1),
        "model": "illustrative", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
