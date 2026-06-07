"""Buy vs Rent — real-estate > Advanced.
Compares the total cost of buying (interest + costs, net of capital growth) against
renting over a horizon. Simplified comparison \u2014 assumptions stated."""
from core.registry import register

@register(
    slug="buy-vs-rent",
    name="Buy vs Rent Calculator",
    section="real-estate",
    sub="Advanced",
    tags=["real estate", "buy vs rent", "renting", "buying", "comparison", "property"],
    formula="buy cost = interest + ownership costs \u2212 capital growth ; rent cost = weekly rent \u00d7 52 \u00d7 years",
    summary="Compare the rough net cost of buying versus renting over a chosen horizon, allowing for mortgage interest, ownership costs and capital growth. Simplified \u2014 see assumptions.",
    viz_template="viz/buy-vs-rent.html",
)
def compute(property_price: float = 600000, deposit: float = 120000,
            interest_rate_percent: float = 6.0, annual_ownership_costs: float = 8000,
            annual_growth_percent: float = 4.0, weekly_rent: float = 550, years: float = 7):
    try:
        price = float(property_price); dep = float(deposit); rate = float(interest_rate_percent)
        own = float(annual_ownership_costs); growth_pct = float(annual_growth_percent)
        rent_w = float(weekly_rent); yrs = float(years)
    except (TypeError, ValueError):
        return {"error": "Enter numbers only."}
    if price <= 0 or yrs <= 0:
        return {"error": "Price and years must be greater than zero."}
    if dep < 0 or rent_w < 0 or own < 0:
        return {"error": "Deposit, rent and costs cannot be negative."}
    loan = max(0.0, price - dep)
    # simple interest-only approximation on the loan over the horizon
    interest_total = loan * (rate / 100.0) * yrs
    ownership_total = own * yrs
    capital_growth = price * (((1 + growth_pct / 100.0) ** yrs) - 1)
    buy_net = interest_total + ownership_total - capital_growth
    rent_total = rent_w * 52 * yrs
    diff = buy_net - rent_total
    cheaper = "buying" if diff < 0 else "renting"
    steps = [
        {"label": "Cost of buying", "math": r"\(" + ("%.0f" % interest_total) + r" + " + ("%.0f" % ownership_total) + r" - " + ("%.0f" % capital_growth) + r" = " + ("%.0f" % buy_net) + r"\)", "note": "Interest + costs, minus capital growth over " + ("%g" % yrs) + " years."},
        {"label": "Cost of renting", "math": r"\(" + ("%g" % rent_w) + r" \times 52 \times " + ("%g" % yrs) + r" = " + ("%.0f" % rent_total) + r"\)", "note": "Rent paid over the same horizon."},
        {"label": "Difference", "math": r"\(" + ("%+.0f" % diff) + r"\)", "note": cheaper.capitalize() + " looks cheaper over this horizon (on these assumptions)."},
    ]
    return {
        "result": (cheaper.capitalize() + " is cheaper by \u2248 " + ("%.0f" % abs(diff)) + " over " + ("%g" % yrs) + " years"),
        "net_cost_of_buying": round(buy_net, 0), "cost_of_renting": round(rent_total, 0),
        "difference": round(diff, 0), "cheaper_option": cheaper, "steps": steps,
    }

from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
