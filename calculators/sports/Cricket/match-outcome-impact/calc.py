"""Match Outcome Impact (Cricket) — sports > Cricket.
ILLUSTRATIVE chase model: required run rate vs current run rate gives a simple
pressure read and a rough chase-probability. Not an official forecast."""
from core.registry import register
import math

@register(
    slug="match-outcome-impact",
    name="Match Outcome Impact Calculator",
    section="sports",
    sub="Cricket",
    tags=["cricket", "match outcome", "chase", "run rate", "probability", "impact", "model"],
    formula="RRR = runs needed / overs left ; chase prob from RRR vs current RR \u2014 illustrative",
    summary="For a run chase, compares the required run rate with the current rate to gauge pressure and a rough chase probability. Illustrative model, not an official forecast.",
    viz_template="viz/match-outcome-impact.html",
)
def compute(runs_needed: float = 60, overs_left: float = 6, wickets_left: float = 5,
            current_run_rate: float = 8.5):
    try:
        need = float(runs_needed); ovl = float(overs_left); wk = float(wickets_left); crr = float(current_run_rate)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if need < 0 or crr < 0:
        return {"error": "Runs and run rate cannot be negative."}
    if ovl <= 0:
        return {"error": "Overs left must be greater than zero."}
    if not (0 <= wk <= 10):
        return {"error": "Wickets left must be between 0 and 10."}
    rrr = need / ovl
    gap = crr - rrr  # positive = chasing side ahead of the rate
    # crude logistic on (rate gap) and (wickets in hand)
    z = 0.45 * gap + 0.18 * (wk - 5)
    prob = 1.0 / (1.0 + math.exp(-z))
    steps = [
        {"label": "Required rate", "math": r"\(" + ("%g" % need) + r" / " + ("%g" % ovl) + r" = " + ("%.2f" % rrr) + r"\text{ rpo}\)", "note": "Runs per over still needed."},
        {"label": "Rate gap", "math": r"\(" + ("%.2f" % crr) + r" - " + ("%.2f" % rrr) + r" = " + ("%+.2f" % gap) + r"\)", "note": ("Ahead of the required rate." if gap >= 0 else "Behind \u2014 need to accelerate.")},
        {"label": "Chase probability", "math": r"\(\approx " + ("%.0f" % (prob*100)) + r"\%\)", "note": "Illustrative, also reflecting " + ("%g" % wk) + " wickets in hand."},
    ]
    return {
        "result": ("Need " + ("%.2f" % rrr) + " rpo; chase probability \u2248 " + ("%.0f" % (prob*100)) + "% (illustrative)"),
        "required_run_rate": round(rrr, 2), "rate_gap": round(gap, 2),
        "chase_probability": round(prob*100, 0), "model": "illustrative", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
