"""Probability — maths > Probability. Single-event probability = favourable / total."""
from core.registry import register

@register(
    slug="probability",
    name="Probability Calculator",
    section="maths",
    sub="Probability",
    tags=["probability", "odds", "chance", "statistics"],
    formula="P = favourable outcomes / total outcomes",
    summary="The chance of an event \u2014 favourable outcomes divided by all equally likely outcomes.",
    viz_template="viz/probability.html",
)
def compute(favourable: float = 1, total: float = 6):
    try:
        f = float(favourable); t = float(total)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if t <= 0:
        return {"error": "Total outcomes must be greater than zero."}
    if f < 0:
        return {"error": "Favourable outcomes cannot be negative."}
    if f > t:
        return {"error": "Favourable outcomes cannot exceed total outcomes."}
    p = f / t
    steps = [
        {"label": "Formula", "math": r"\(P = \dfrac{\text{favourable}}{\text{total}}\)", "note": "Assumes every outcome is equally likely."},
        {"label": "Substitute", "math": r"\(P = \dfrac{" + ("%.4g" % f) + r"}{" + ("%.4g" % t) + r"}\)", "note": "Your numbers."},
        {"label": "Result", "math": r"\(P = " + ("%.4g" % p) + r"\ = " + ("%.2f" % (p * 100)) + r"\%\)", "note": "As a fraction and a percent."},
    ]
    return {
        "result": "P = " + ("%.6g" % p) + "  (" + ("%.2f" % (p * 100)) + "%)",
        "probability": round(p, 6), "percent": round(p * 100, 4),
        "against_percent": round((1 - p) * 100, 4), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
