"""ROI — accounting › Investment Analytics.
Bar chart: invested vs current value, with the ROI % as the headline metric.
Direct percentage; no step-by-step (single-operation lookup)."""
from core.registry import register


@register(
    slug="roi",
    name="ROI Calculator",
    section="accounting",
    sub="Investment Analytics",
    tags=["roi", "return", "investment", "profit"],
    formula="ROI = (Current Value − Cost) / Cost × 100",
    summary="Return on investment as a percentage, plus the net profit, from cost and current value.",
    viz_template="viz/roi.html",
)
def compute(cost: float, current_value: float):
    C = float(cost)
    V = float(current_value)
    if C <= 0:
        return {"error": "Cost of investment must be greater than zero."}
    net = V - C
    roi = net / C * 100
    return {
        "roi_pct": round(roi, 2),
        "net_profit": round(net, 2),
        "cost": round(C, 2),
        "current_value": round(V, 2),
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
