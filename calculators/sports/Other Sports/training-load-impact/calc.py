"""Training Load Impact — sports > Other Sports.
Acute:chronic workload ratio (ACWR) \u2014 a real, widely-used sports-science concept.
ACWR = this week's load / 4-week rolling average. Flags injury-risk zones."""
from core.registry import register

@register(
    slug="training-load-impact",
    name="Training Load Impact Calculator",
    section="sports",
    sub="Other Sports",
    tags=["training", "load", "acwr", "workload", "injury risk", "impact"],
    formula="ACWR = acute (this week) load / chronic (4-week average) load",
    summary="The acute:chronic workload ratio (ACWR) flags whether a recent spike in training load pushes an athlete into a higher injury-risk zone. A widely used sports-science guide.",
    viz_template="viz/training-load-impact.html",
)
def compute(this_week_load: float = 600, four_week_average_load: float = 450):
    try:
        acute = float(this_week_load); chronic = float(four_week_average_load)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if acute < 0:
        return {"error": "Load cannot be negative."}
    if chronic <= 0:
        return {"error": "Four-week average load must be greater than zero."}
    acwr = acute / chronic
    if acwr < 0.8:
        zone = "undertraining (detraining risk)"
    elif acwr <= 1.3:
        zone = "sweet spot (lower injury risk)"
    elif acwr <= 1.5:
        zone = "caution \u2014 load rising fast"
    else:
        zone = "danger zone \u2014 elevated injury risk"
    steps = [
        {"label": "ACWR", "math": r"\(" + ("%g" % acute) + r" / " + ("%g" % chronic) + r" = " + ("%.2f" % acwr) + r"\)", "note": "This week against the rolling 4-week base."},
        {"label": "Zone", "math": r"\(" + ("%.2f" % acwr) + r"\)", "note": "Research often cites ~0.8\u20131.3 as the safer band."},
    ]
    return {
        "result": ("ACWR " + ("%.2f" % acwr) + " \u2014 " + zone),
        "acwr": round(acwr, 2), "zone": zone, "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
