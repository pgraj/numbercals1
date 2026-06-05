from core.faqs import register_faqs

register_faqs("convert-currency", [
    {"q": "Where do the exchange rates come from?",
     "a": "From the Frankfurter API (api.frankfurter.app), a free open service that publishes "
          "European Central Bank reference rates. NumberCals does not own or operate it. Rates "
          "are ECB business-day figures and can differ from real-time market and retail prices."},
    {"q": "Can you show a worked example?",
     "a": "If 1 USD = 1.52 AUD, then 100 USD × 1.52 = 152 AUD. The converter simply multiplies "
          "your amount by the live fetched rate."},
    {"q": "How do I read the trendline?",
     "a": "The chart plots the exchange rate over the last 30 days, so you can see whether the "
          "pair has been strengthening, weakening or holding steady before you convert."},
    {"q": "What happens if the rate service is offline?",
     "a": "The calculator never crashes — it shows an amber warning banner and a message that "
          "currency data is temporarily unavailable, and asks you to try again shortly."},
    {"q": "Should I rely on this for trading or large transfers?",
     "a": "No. These are reference rates for general information only, not financial advice. "
          "Banks and brokers add spreads and fees, so confirm the actual rate with your provider "
          "before committing to a transaction."},
])
