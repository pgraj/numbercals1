"""Investment Return Impact — business-finance > Impact Metrics.
Compound growth of an investment and how the return rate changes the outcome."""
from core.registry import register

@register(
    slug="investment-return-impact",
    name="Investment Return Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["investment", "return", "compound", "growth", "impact"],
    formula="future value = principal \u00d7 (1 + rate)^years",
    summary="See how an annual return compounds a lump sum over time, and how changing the rate changes the result.",
    viz_template="viz/investment-return-impact.html",
)
def compute(principal: float = 10000, annual_return_percent: float = 8, years: float = 10):
    try:
        P = float(principal); r = float(annual_return_percent); y = float(years)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if P < 0 or y < 0:
        return {"error": "Principal and years cannot be negative."}
    fv = P * (1 + r / 100.0) ** y
    gain = fv - P
    steps = [
        {"label": "Compound", "math": r"\(" + ("%.2f" % P) + r" \times (1 + " + ("%.4g" % (r/100)) + r")^{" + ("%.4g" % y) + r"}\)", "note": "Each year's return builds on the last."},
        {"label": "Future value", "math": r"\(" + ("%.2f" % fv) + r"\)", "note": "Total after " + ("%.4g" % y) + " years."},
        {"label": "Gain", "math": r"\(" + ("%.2f" % gain) + r"\)", "note": "Profit above the original principal."},
    ]
    return {
        "result": ("Grows to " + ("%.2f" % fv) + "  (gain " + ("+" if gain >= 0 else "") + ("%.2f" % gain) + ")"),
        "future_value": round(fv, 2), "gain": round(gain, 2), "principal": round(P, 2), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
