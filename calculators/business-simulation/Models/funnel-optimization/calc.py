"""Funnel Optimization — business-simulation > Models.
Multi-stage conversion funnel: chains stage rates to an overall rate, then shows the
uplift from improving one stage. Accepts comma-separated stage conversion percentages."""
from core.registry import register

def _parse(nums):
    if isinstance(nums, (list, tuple)):
        return [float(v) for v in nums]
    raw = str(nums).replace(";", ",").replace(" ", ",")
    return [float(p) for p in raw.split(",") if p != ""]

@register(
    slug="funnel-optimization",
    name="Funnel Optimization Calculator",
    section="business-simulation",
    sub="Models",
    tags=["funnel", "conversion", "optimization", "cro", "stages", "simulation"],
    formula="overall rate = product of stage rates ; conversions = visitors \u00d7 overall rate",
    summary="Chain each stage's conversion rate into an overall funnel rate, then see how lifting one stage flows through to total conversions and revenue.",
    viz_template="viz/funnel-optimization.html",
)
def compute(visitors: float = 10000, stage_rates_percent: str = "40, 50, 30",
            improve_stage: float = 2, improve_by_points: float = 10, value_per_conversion: float = 80):
    try:
        V = float(visitors); rates = _parse(stage_rates_percent)
        idx = int(float(improve_stage)); bump = float(improve_by_points); val = float(value_per_conversion)
    except (TypeError, ValueError):
        return {"error": "Enter visitors, comma-separated stage rates, and numbers."}
    if V < 0 or val < 0:
        return {"error": "Visitors and value cannot be negative."}
    if not rates:
        return {"error": "Enter at least one stage conversion rate."}
    if any(r < 0 or r > 100 for r in rates):
        return {"error": "Each stage rate must be between 0 and 100."}
    if not (1 <= idx <= len(rates)):
        return {"error": "Improve-stage must point to one of your stages (1.." + str(len(rates)) + ")."}

    def overall(rs):
        p = 1.0
        for r in rs:
            p *= r / 100.0
        return p
    base_overall = overall(rates)
    improved = list(rates)
    improved[idx - 1] = min(100.0, improved[idx - 1] + bump)
    new_overall = overall(improved)
    conv0 = V * base_overall
    conv1 = V * new_overall
    extra = conv1 - conv0
    rev_delta = extra * val
    steps = [
        {"label": "Overall rate now", "math": r"\(\prod = " + ("%.3f" % (base_overall*100)) + r"\%\)", "note": "Stages multiply \u2014 each leak compounds."},
        {"label": "Improve stage " + str(idx), "math": r"\(+" + ("%g" % bump) + r"\text{ pts} \to " + ("%.3f" % (new_overall*100)) + r"\%\)", "note": "Only that stage changes."},
        {"label": "Extra output", "math": r"\(+" + ("%.0f" % extra) + r"\text{ conv}, +" + ("%.0f" % rev_delta) + r"\text{ rev}\)", "note": "Same traffic, fixing one leak."},
    ]
    return {
        "result": ("Overall " + ("%.2f" % (base_overall*100)) + "% \u2192 " + ("%.2f" % (new_overall*100))
                   + "%; +" + ("%.0f" % extra) + " conversions, +" + ("%.0f" % rev_delta) + " revenue"),
        "overall_rate_before_percent": round(base_overall*100, 3),
        "overall_rate_after_percent": round(new_overall*100, 3),
        "extra_conversions": round(extra, 0), "revenue_delta": round(rev_delta, 0), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
