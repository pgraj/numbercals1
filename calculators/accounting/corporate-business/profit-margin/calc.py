"""Profit margin — accounting › Corporate / Business Accounting.
Gauge: gross profit margin %, coloured low->high. Direct ratios; no steps."""
from core.registry import register


@register(
    slug="profit-margin",
    name="Profit Margin Calculator",
    section="accounting",
    sub="Corporate / Business Accounting",
    tags=["profit", "margin", "gross", "net", "cogs"],
    formula="Gross Margin = (Revenue − COGS) / Revenue × 100",
    summary="Gross and net profit margins from revenue, cost of goods sold and operating expenses.",
    viz_template="viz/profit-margin.html",
)
def compute(revenue: float, cogs: float, operating_expenses: float = 0):
    R = float(revenue)
    C = float(cogs)
    O = float(operating_expenses)
    if R <= 0:
        return {"error": "Revenue must be greater than zero."}
    if C < 0 or O < 0:
        return {"error": "Costs cannot be negative."}

    gross_profit = R - C
    net_profit = R - C - O
    gross_margin = gross_profit / R * 100
    net_margin = net_profit / R * 100
    return {
        "gross_profit": round(gross_profit, 2),
        "net_profit": round(net_profit, 2),
        "gross_margin_pct": round(gross_margin, 2),
        "net_margin_pct": round(net_margin, 2),
        "revenue": round(R, 2),
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
