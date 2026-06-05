"""Dividend — accounting › Wealth Management.
Bars of annual dividend income; if DRIP on, a compounding curve of reinvested value.
Direct income; no step-by-step."""
from core.registry import register


@register(
    slug="dividend",
    name="Dividend Calculator",
    section="accounting",
    sub="Wealth Management",
    tags=["dividend", "yield", "drip", "income", "shares"],
    formula="Annual dividend = Shares × Price × (Yield% / 100)",
    summary="Annual dividend income, and the reinvested value over time when DRIP is enabled.",
    viz_template="viz/dividend.html",
)
def compute(stock_price: float, shares: float, yield_pct: float,
            years: float = 10, reinvest: bool = False):
    price = float(stock_price)
    sh = float(shares)
    y = float(yield_pct) / 100
    yrs = int(float(years))
    if isinstance(reinvest, str):
        drip = reinvest.strip().lower() in ("true", "yes", "1", "on", "y")
    else:
        drip = bool(reinvest)
    if price < 0 or sh < 0 or y < 0 or yrs < 0:
        return {"error": "Inputs must be zero or positive."}

    invested = price * sh
    annual_dividend = invested * y

    # Series: without DRIP the income is flat each year; with DRIP the holding
    # value compounds at the yield (a simplified model assuming price steady).
    series = []
    value = invested
    cumulative = 0.0
    for yr in range(1, yrs + 1):
        if drip:
            div = value * y
            value += div          # reinvested back into the holding
        else:
            div = annual_dividend
        cumulative += div
        series.append({
            "year": yr,
            "dividend": round(div, 2),
            "value": round(value, 2),
            "cumulative": round(cumulative, 2),
        })

    future_value = round(value, 2) if drip else round(invested, 2)
    return {
        "annual_dividend": round(annual_dividend, 2),
        "invested": round(invested, 2),
        "future_value": future_value,
        "reinvest": drip,
        "series": series,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
