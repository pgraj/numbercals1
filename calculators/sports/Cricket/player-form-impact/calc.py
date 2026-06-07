"""Player Form Impact (Cricket) — sports > Cricket.
ILLUSTRATIVE: recent scores vs career average gives a form index. Subjective by nature;
clearly labelled. Accepts a list of recent scores."""
from core.registry import register

def _parse(nums):
    if isinstance(nums, (list, tuple)):
        return [float(v) for v in nums]
    raw = str(nums).replace(";", ",").replace(" ", ",")
    return [float(p) for p in raw.split(",") if p != ""]

@register(
    slug="player-form-impact",
    name="Player Form Impact Calculator",
    section="sports",
    sub="Cricket",
    tags=["cricket", "form", "recent", "average", "impact", "index"],
    formula="form index = recent average / career average \u2014 illustrative",
    summary="Compares a player's recent scores with their career average to give a simple form index (above 1 = in form). Illustrative and subjective \u2014 see the FAQ.",
    viz_template="viz/player-form-impact.html",
)
def compute(recent_scores: str = "62, 8, 45, 90, 12", career_average: float = 38):
    try:
        xs = _parse(recent_scores); car = float(career_average)
    except (TypeError, ValueError):
        return {"error": "Enter recent scores separated by commas and a numeric career average."}
    if not xs:
        return {"error": "Enter at least one recent score."}
    if any(x < 0 for x in xs):
        return {"error": "Scores cannot be negative."}
    if car <= 0:
        return {"error": "Career average must be greater than zero."}
    recent_avg = sum(xs) / len(xs)
    form = recent_avg / car
    if form >= 1.15:
        label = "in strong form"
    elif form >= 0.9:
        label = "around their usual level"
    else:
        label = "below their usual level"
    steps = [
        {"label": "Recent average", "math": r"\(\sum / " + str(len(xs)) + r" = " + ("%.1f" % recent_avg) + r"\)", "note": "Mean of the recent scores."},
        {"label": "Form index", "math": r"\(" + ("%.1f" % recent_avg) + r" / " + ("%g" % car) + r" = " + ("%.2f" % form) + r"\)", "note": "Above 1 means hotter than career norm."},
    ]
    return {
        "result": ("Form index " + ("%.2f" % form) + " \u2014 " + label),
        "form_index": round(form, 2), "recent_average": round(recent_avg, 1),
        "model": "illustrative", "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
