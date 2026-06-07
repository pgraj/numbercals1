"""Possession Impact — sports > Football / Soccer.
Relates possession % to a simple expected-control read; ILLUSTRATIVE \u2014 possession
does not guarantee results, which the result text and FAQ make explicit."""
from core.registry import register

@register(
    slug="possession-impact",
    name="Possession Impact Calculator",
    section="sports",
    sub="Football / Soccer",
    tags=["football", "soccer", "possession", "control", "tempo", "impact"],
    formula="possession % = team seconds / total seconds ; passes per possession-minute",
    summary="Turn possession time and passes into possession share and passing tempo. Note: more possession does not guarantee more goals \u2014 see the FAQ.",
    viz_template="viz/possession-impact.html",
)
def compute(team_minutes: float = 33, opponent_minutes: float = 27, team_passes: float = 520):
    try:
        tm = float(team_minutes); om = float(opponent_minutes); tp = float(team_passes)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if tm < 0 or om < 0 or tp < 0:
        return {"error": "Values cannot be negative."}
    total = tm + om
    if total <= 0:
        return {"error": "Total possession time must be greater than zero."}
    share = tm / total * 100
    tempo = tp / tm if tm > 0 else 0.0
    steps = [
        {"label": "Possession share", "math": r"\(" + ("%g" % tm) + r" / " + ("%g" % total) + r" = " + ("%.1f" % share) + r"\%\)", "note": "Your share of ball time."},
        {"label": "Passing tempo", "math": r"\(" + ("%g" % tp) + r" / " + ("%g" % tm) + r" = " + ("%.1f" % tempo) + r"\text{ passes/min}\)", "note": "How quickly you move the ball while in control."},
    ]
    return {
        "result": (("%.1f" % share) + "% possession, " + ("%.1f" % tempo) + " passes/min in control"),
        "possession_percent": round(share, 1), "passes_per_minute": round(tempo, 1),
        "note": "Possession is control, not a guarantee of goals.", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
