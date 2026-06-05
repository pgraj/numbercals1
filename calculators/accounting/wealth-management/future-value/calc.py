"""Future value — accounting › Wealth Management.
Grouped bars: present value vs projected future value. Direct compounding; no steps."""
from core.registry import register


@register(
    slug="future-value",
    name="Future Value Calculator",
    section="accounting",
    sub="Wealth Management",
    tags=["future value", "time value of money", "compound"],
    formula="FV = PV·(1 + r)^n",
    summary="What a present sum will be worth after n periods of compound growth.",
    viz_template="viz/future-value.html",
)
def compute(present_value: float, rate_pct: float, periods: float):
    PV = float(present_value)
    r = float(rate_pct) / 100
    n = float(periods)
    if PV < 0 or n < 0:
        return {"error": "Present value and number of periods must be zero or positive."}
    FV = PV * (1 + r) ** n
    return {
        "future_value": round(FV, 2),
        "present_value": round(PV, 2),
        "growth": round(FV - PV, 2),
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
