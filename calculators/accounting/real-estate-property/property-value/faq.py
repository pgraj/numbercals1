from core.faqs import register_faqs

register_faqs("property-value", [
    {"q": "What does this estimator actually project?",
     "a": "It takes the price you paid (or would pay) today and grows it by an annual "
          "appreciation rate to estimate the property's value after a number of years. "
          "It then strips inflation back out to show what that future price is worth in "
          "today's money — the real value — so a rising number isn't mistaken for a "
          "genuine gain when it's only keeping pace with rising prices generally."},
    {"q": "What is the difference between nominal value and real value?",
     "a": "Nominal value is the sticker price in future dollars: price compounded by the "
          "appreciation rate. Real value deflates that figure by inflation to express it "
          "in today's dollars. If a property appreciates 5% a year while inflation runs "
          "3%, the nominal value climbs steeply but the real value climbs only about 2% — "
          "and the gap between the two curves is the part that inflation quietly eats."},
    {"q": "What do the three modes do?",
     "a": "Simple projects one nominal curve and its real counterpart. Scenarios brackets "
          "the estimate with low, average and high appreciation bands (two percentage "
          "points either side), because no one knows the exact future rate. With Mortgage "
          "adds a deposit and loan, so instead of just the property's value it reports your "
          "equity — value minus the balance you still owe — and the real return on the cash "
          "you actually committed, which is the deposit."},
    {"q": "How do I read the chart?",
     "a": "The upper line is the nominal value rising over the years; the lower line is the "
          "real, inflation-adjusted value rising more gently. The shaded band between them "
          "is value lost to inflation. In Scenarios mode you instead see three nominal "
          "lines fanning out — low, average and high — showing how much the outcome depends "
          "on the rate you assume. In Mortgage mode the chart adds your growing equity."},
    {"q": "Where is this used in real life?",
     "a": "Deciding whether to buy or keep renting — a $600,000 home at 5% appreciation is "
          "worth about $977,000 in ten years on paper, but nearer $727,000 in today's "
          "money after 3% inflation. Sanity-checking an agent's growth promise by seeing "
          "the real figure, not just the headline. And in mortgage mode, judging a "
          "deposit as an investment: a $120,000 deposit that becomes far larger equity can "
          "still post a modest real return once inflation and the remaining loan are counted. "
          "These are rough estimates, not valuations or financial advice."},
])
