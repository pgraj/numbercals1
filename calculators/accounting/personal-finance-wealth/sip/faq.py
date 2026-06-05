from core.faqs import register_faqs

register_faqs("sip", [
    {"q": "What is a SIP?",
     "a": "A Systematic Investment Plan — investing a fixed amount every month rather than a "
          "lump sum. Each instalment buys into the fund and then compounds, so a steady habit "
          "of small contributions can build a large amount over time."},
    {"q": "What do the parts of the SIP formula mean?",
     "a": "P is your monthly investment, i is the monthly return rate (the annual rate divided "
          "by 12 and by 100), and n is the number of months. The bracketed term compounds the "
          "whole stream of payments; the final (1 + i) reflects that each instalment is invested "
          "at the start of its month."},
    {"q": "Why do my returns end up larger than what I put in?",
     "a": "Early instalments stay invested for years and earn returns on returns. Given enough "
          "time, that compounding growth can exceed the total of all the contributions you made — "
          "the longer the horizon, the more lopsided it becomes in favour of growth."},
    {"q": "How do I read the stacked columns?",
     "a": "Each column is one year. The lower part is the cash you have actually invested by then; "
          "the upper part is the growth compounding has added on top. Watch the upper band take up "
          "more and more of each column as the years pass."},
    {"q": "Where is this used in real life?",
     "a": "Regular fund investing — $500 a month at 10% for 20 years grows to roughly $380,000, "
          "of which only $120,000 is your own money. Retirement saving — automating a monthly "
          "transfer into super or an index fund. Goal saving — building a house deposit steadily "
          "rather than waiting to invest a lump sum. Returns are an estimate, not a guarantee."},
])
