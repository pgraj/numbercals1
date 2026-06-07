"""Marketing Spend Impact — business-finance > Impact Metrics.
ROAS-based: how a change in marketing spend flows to revenue at a given return on ad spend."""
from core.registry import register

@register(
    slug="marketing-spend-impact",
    name="Marketing Spend Impact Calculator",
    section="business-finance",
    sub="Impact Metrics",
    tags=["marketing", "spend", "roas", "revenue", "impact", "advertising"],
    formula="revenue = spend \u00d7 ROAS ; \u0394revenue = \u0394spend \u00d7 ROAS",
    summary="See how changing marketing spend moves revenue at a given return on ad spend (ROAS), and the net gain after the extra spend.",
    viz_template="viz/marketing-spend-impact.html",
)
def compute(current_spend: float = 10000, new_spend: float = 15000, roas: float = 4.0):
    try:
        s0 = float(current_spend); s1 = float(new_spend); R = float(roas)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if s0 < 0 or s1 < 0:
        return {"error": "Spend cannot be negative."}
    if R < 0:
        return {"error": "ROAS cannot be negative."}
    rev0 = s0 * R
    rev1 = s1 * R
    d_spend = s1 - s0
    d_rev = rev1 - rev0
    net = d_rev - d_spend
    steps = [
        {"label": "Revenue now", "math": r"\(" + ("%.2f" % s0) + r" \times " + ("%.4g" % R) + r" = " + ("%.2f" % rev0) + r"\)", "note": "Spend times ROAS."},
        {"label": "Revenue after", "math": r"\(" + ("%.2f" % s1) + r" \times " + ("%.4g" % R) + r" = " + ("%.2f" % rev1) + r"\)", "note": "At the new spend."},
        {"label": "Net gain", "math": r"\(" + ("%.2f" % d_rev) + r" - " + ("%.2f" % d_spend) + r" = " + ("%.2f" % net) + r"\)", "note": "Extra revenue minus the extra spend."},
    ]
    return {
        "result": ("Revenue " + ("+" if d_rev >= 0 else "") + ("%.2f" % d_rev)
                   + " for " + ("+" if d_spend >= 0 else "") + ("%.2f" % d_spend) + " spend  \u2192  net "
                   + ("+" if net >= 0 else "") + ("%.2f" % net)),
        "revenue_before": round(rev0, 2), "revenue_after": round(rev1, 2),
        "revenue_delta": round(d_rev, 2), "spend_delta": round(d_spend, 2), "net_gain": round(net, 2),
        "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
