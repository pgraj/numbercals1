"""LTV Growth Simulator — business-simulation > Models.
Lifetime value from churn: LTV = ARPU \u00d7 gross margin / monthly churn (the standard
1/churn lifespan model), simulated before vs after an improvement."""
from core.registry import register

@register(
    slug="ltv-growth-simulator",
    name="LTV Growth Simulator",
    section="business-simulation",
    sub="Models",
    tags=["ltv", "lifetime value", "churn", "arpu", "simulation", "saas"],
    formula="LTV = ARPU \u00d7 gross margin% / monthly churn ; lifespan \u2248 1 / churn",
    summary="Simulate customer lifetime value using the churn-based model (expected lifespan = 1 / churn), and see how cutting churn or lifting margin grows LTV.",
    viz_template="viz/ltv-growth-simulator.html",
)
def compute(arpu: float = 50, gross_margin_percent: float = 80,
            monthly_churn_percent: float = 4, new_monthly_churn_percent: float = 3):
    try:
        arpu_v = float(arpu); margin = float(gross_margin_percent)
        c0 = float(monthly_churn_percent); c1 = float(new_monthly_churn_percent)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if arpu_v < 0:
        return {"error": "ARPU cannot be negative."}
    if not (0 <= margin <= 100):
        return {"error": "Gross margin must be between 0 and 100."}
    if not (0 < c0 <= 100 and 0 < c1 <= 100):
        return {"error": "Churn rates must be between 0 (exclusive) and 100."}
    m = margin / 100.0
    life0 = 1 / (c0 / 100.0)
    life1 = 1 / (c1 / 100.0)
    ltv0 = arpu_v * m * life0
    ltv1 = arpu_v * m * life1
    delta = ltv1 - ltv0
    pct = (delta / ltv0 * 100) if ltv0 > 0 else None
    steps = [
        {"label": "Lifespan now", "math": r"\(1 / " + ("%.3g" % (c0/100)) + r" = " + ("%.1f" % life0) + r"\text{ months}\)", "note": "Average customer life at the current churn."},
        {"label": "LTV now", "math": r"\(" + ("%g" % arpu_v) + r" \times " + ("%.2g" % m) + r" \times " + ("%.1f" % life0) + r" = " + ("%.0f" % ltv0) + r"\)", "note": "ARPU \u00d7 margin \u00d7 lifespan."},
        {"label": "LTV after churn cut", "math": r"\(" + ("%.0f" % ltv1) + r"\ (" + ("%+.0f" % delta) + r")\)", "note": ("Lower churn lengthens life and lifts LTV." if delta >= 0 else "Higher churn shortens life and cuts LTV.")},
    ]
    return {
        "result": ("LTV " + ("%.0f" % ltv0) + " \u2192 " + ("%.0f" % ltv1)
                   + "  (" + ("+" if delta >= 0 else "") + ("%.0f" % delta)
                   + (", " + ("%.0f" % pct) + "%" if pct is not None else "") + ")"),
        "ltv_before": round(ltv0, 0), "ltv_after": round(ltv1, 0), "delta": round(delta, 0),
        "lifespan_before_months": round(life0, 1), "lifespan_after_months": round(life1, 1),
        "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
