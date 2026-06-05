"""Currency Converter — live rates via the Frankfurter API (ECB data).

The backend computes the conversion when a rate is supplied by the viz, and the
viz fetches live + 30-day historical rates from api.frankfurter.app directly.
If the API is unreachable, compute() still returns a graceful error object and
the viz shows an amber warning banner.
"""
from core.registry import register

_DISCLAIMER = (
    "These values are estimates and may contain computation, formula, or "
    "system errors. They are provided for general reference only — always "
    "verify results independently before relying on them for engineering, "
    "commercial, or professional decisions. "
    "Currency rates are sourced from the Frankfurter API "
    "(api.frankfurter.app), a free service backed by European Central Bank "
    "data. NumberCals does not own or operate this API. Rates reflect ECB "
    "business-day data and may not match real-time market prices."
)


_EXPLANATION = [
    {"heading": "There is no formula — only today's rate",
     "body": "Unlike metres or kilograms, currencies have no fixed conversion factor. The 'rate' floats every second on global markets. This tool multiplies your amount by the latest published rate: target = amount × rate."},
    {"heading": "Where the rate comes from",
     "body": "Rates are fetched live from the Frankfurter service, which republishes European Central Bank reference rates. These are daily reference figures, not the exact price your bank gives you — banks add a margin (spread) and fees on top."},
    {"heading": "Why your bank quotes a different number",
     "body": "A mid-market rate (what this shows) sits halfway between the buy and sell price. A retailer or bank widens that gap to make money, so the rate you actually pay when buying foreign currency is usually a few percent worse."},
]


@register(
    slug="convert-currency",
    name="Currency Converter",
    section="conversions",
    sub="1 · Basic Converters",
    summary="Convert between world currencies using free European Central Bank rates via the Frankfurter API, with a 30-day historical trendline.",
    formula="target = amount × rate(from→to)",
    tags=["currency", "forex", "exchange", "money", "frankfurter", "ecb", "converter"],
    viz_template="viz/convert-currency.html",
)
def compute(amount=None, rate=None, from_cur=None, to_cur=None, **_ignored):
    """Pure arithmetic step; the viz supplies the live `rate` it fetched.

    Kept server-side compute network-free so the page never blocks on an
    outbound call; if the viz couldn't fetch a rate it sends rate=None and we
    return the documented offline error object.
    """
    if amount is None or rate is None:
        return {"error": "Currency data unavailable — live rate could not be fetched. "
                         "Please try again shortly.", "steps": []}
    try:
        amt = float(amount)
        rt = float(rate)
    except (TypeError, ValueError):
        return {"error": "Amount and rate must be numbers.", "steps": []}
    if rt <= 0:
        return {"error": "Rate must be positive.", "steps": []}

    result = amt * rt
    fc = (from_cur or "FROM").upper()
    tc = (to_cur or "TO").upper()
    steps = [
        {"label": "Apply exchange rate",
         "math": f"{amt:g} {fc} × {rt:g} = {result:g} {tc}"},
    ]
    return {
        "result": result,
        "result_unit": tc,
        "rate": rt,
        "steps": steps,
        "explanation": _EXPLANATION,
        "disclaimer": _DISCLAIMER,
    }


from core.faqs import load_sibling_faq
load_sibling_faq(__file__)
