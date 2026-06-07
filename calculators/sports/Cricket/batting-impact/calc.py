"""Batting Impact Score (Cricket) — sports > Cricket.
ILLUSTRATIVE composite: blends runs, strike rate and not-out, contextualised by format.
Transparent weighting, not an official rating."""
from core.registry import register

@register(
    slug="batting-impact",
    name="Batting Impact Score Calculator",
    section="sports",
    sub="Cricket",
    tags=["cricket", "batting", "impact", "runs", "strike rate", "index"],
    formula="score = runs \u00d7 (strike rate / par SR) \u2014 illustrative blend of volume and tempo",
    summary="A transparent batting impact score that rewards both runs and scoring speed relative to a format's par strike rate. Illustrative composite, not an official metric.",
    viz_template="viz/batting-impact.html",
)
def compute(runs: float = 75, balls_faced: float = 50, format_par_sr: float = 130):
    try:
        r = float(runs); b = float(balls_faced); par = float(format_par_sr)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if r < 0:
        return {"error": "Runs cannot be negative."}
    if b <= 0:
        return {"error": "Balls faced must be greater than zero."}
    if par <= 0:
        return {"error": "Par strike rate must be greater than zero (e.g. 130 for T20)."}
    sr = r / b * 100
    score = r * (sr / par)
    steps = [
        {"label": "Strike rate", "math": r"\(" + ("%g" % r) + r" / " + ("%g" % b) + r" \times 100 = " + ("%.1f" % sr) + r"\)", "note": "Scoring speed."},
        {"label": "Tempo factor", "math": r"\(" + ("%.1f" % sr) + r" / " + ("%g" % par) + r" = " + ("%.2f" % (sr/par)) + r"\)", "note": "Above 1 = faster than format par."},
        {"label": "Impact score", "math": r"\(" + ("%g" % r) + r" \times " + ("%.2f" % (sr/par)) + r" = " + ("%.1f" % score) + r"\)", "note": "Rewards runs AND tempo."},
    ]
    return {
        "result": "Batting impact \u2248 " + ("%.1f" % score) + "  (SR " + ("%.1f" % sr) + ")",
        "impact_score": round(score, 1), "strike_rate": round(sr, 1),
        "model": "illustrative", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
