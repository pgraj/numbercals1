from core.faqs import register_faqs
register_faqs("ev-savings-impact", [
    {"q": "What does this calculator do?",
     "a": "It compares a petrol car and an electric car over a year's driving and shows how "
          "much CO\u2082 the EV saves \u2014 or, on a very dirty grid, whether it saves much "
          "at all."},
    {"q": "Can you show an example?",
     "a": "Driving 15,000 km a year. A petrol car at 8 L/100km burns 1,200 L, making about "
          "2,772 kg of CO\u2082. An EV using 18 kWh/100km draws 2,700 kWh; in India that is "
          "about 1,809 kg. So the EV saves roughly 963 kg a year there."},
    {"q": "Why does the EV's saving depend on the country?",
     "a": "An EV is only as clean as the electricity charging it. In France the same EV "
          "would save about 2,660 kg a year because the grid is so clean; on a very "
          "coal-heavy grid the saving shrinks, because the electricity itself is "
          "carbon-heavy."},
    {"q": "Where do the numbers come from?",
     "a": "Electricity factors are from Ember / Our World in Data (per country). The petrol "
          "figure of 2.31 kg CO\u2082 per litre is the standard GHG Protocol / US EPA "
          "value. Both are shown and linked on the page."},
    {"q": "Does this include making the car and its battery?",
     "a": "No. It compares only the emissions from driving \u2014 burning petrol versus "
          "charging from the grid. Building a car (especially an EV battery) has its own "
          "one-off carbon cost, spread over the car's lifetime, which this does not count."},
    {"q": "Could a petrol car ever beat an EV on carbon?",
     "a": "Only on driving emissions, and only on an extremely coal-heavy grid with a very "
          "efficient petrol car against an inefficient EV. In most places, and especially "
          "as grids get cleaner over time, the EV comes out clearly ahead."},
])
