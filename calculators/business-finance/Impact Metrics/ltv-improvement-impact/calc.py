"""LTV Improvement Impact — business-finance > Impact Metrics.
Customer lifetime value from ARPU, margin and lifespan; effect of improving each."""
from core.registry import register

@register(
    slug="ltv-improvement-impact",
    name="LTV Improvement Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["ltv", "lifetime value", "arpu", "retention", "impact", "saas"],
    formula="LTV = ARPU \u00d7 gross margin% \u00d7 lifespan ; compare before/after",
    summary="Estimate customer lifetime value and see how lifting ARPU, margin or lifespan changes it.",
    viz_template="viz/ltv-improvement-impact.html",
)
def compute(arpu: float = 50, gross_margin_percent: float = 70, lifespan_months: float = 24,
            new_arpu: float = 55, new_margin_percent: float = 72, new_lifespan_months: float = 30):
    try:
        a0 = float(arpu); m0 = float(gross_margin_percent); l0 = float(lifespan_months)
        a1 = float(new_arpu); m1 = float(new_margin_percent); l1 = float(new_lifespan_months)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if a0 < 0 or a1 < 0 or l0 < 0 or l1 < 0:
        return {"error": "ARPU and lifespan cannot be negative."}
    if not (0 <= m0 <= 100 and 0 <= m1 <= 100):
        return {"error": "Margin must be between 0 and 100."}
    ltv0 = a0 * (m0 / 100.0) * l0
    ltv1 = a1 * (m1 / 100.0) * l1
    delta = ltv1 - ltv0
    pct = (delta / ltv0 * 100) if ltv0 != 0 else None
    steps = [
        {"label": "LTV now", "math": r"\(" + ("%.2f" % a0) + r" \times " + ("%.4g" % (m0/100)) + r" \times " + ("%.0f" % l0) + r" = " + ("%.2f" % ltv0) + r"\)", "note": "ARPU \u00d7 margin \u00d7 months."},
        {"label": "LTV after", "math": r"\(" + ("%.2f" % a1) + r" \times " + ("%.4g" % (m1/100)) + r" \times " + ("%.0f" % l1) + r" = " + ("%.2f" % ltv1) + r"\)", "note": "With the improvements."},
        {"label": "Change", "math": r"\(" + ("+" if delta >= 0 else "") + ("%.2f" % delta) + r"\)", "note": ("Up " if delta >= 0 else "Down ") + (("%.1f" % pct) + "%." if pct is not None else "")},
    ]
    return {
        "result": ("LTV " + ("rises" if delta >= 0 else "falls") + " from " + ("%.2f" % ltv0)
                   + " to " + ("%.2f" % ltv1) + "  (" + ("+" if delta >= 0 else "") + ("%.2f" % delta) + ")"),
        "ltv_before": round(ltv0, 2), "ltv_after": round(ltv1, 2), "delta": round(delta, 2),
        "ltv_change_percent": (round(pct, 2) if pct is not None else None), "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
