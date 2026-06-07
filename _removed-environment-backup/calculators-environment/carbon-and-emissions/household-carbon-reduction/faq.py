from core.faqs import register_faqs
register_faqs("household-carbon-reduction", [
    {"q": "What does this calculator do?",
     "a": "It compares how much electricity you used before a change with how much after, "
          "and shows the CO\u2082 you save \u2014 scaled up to a full year so you can see the "
          "real impact."},
    {"q": "Can you give an example?",
     "a": "Say you used 300 kWh a month and, after switching to LED bulbs and a more "
          "efficient fridge, you use 220. That is 80 kWh saved a month. In India that is "
          "about 54 kg of CO\u2082 a month, or roughly 643 kg a year."},
    {"q": "Why scale it to a year?",
     "a": "Because a change you make once keeps saving every day. A small monthly saving "
          "might not look like much, but over a year it adds up to a meaningful number \u2014 "
          "which is the honest way to judge it."},
    {"q": "What if my 'after' use is higher than 'before'?",
     "a": "Then the calculator tells you your emissions went UP, not down, and by how much. "
          "It is just as useful to spot that as to confirm a saving."},
    {"q": "Where does the carbon factor come from?",
     "a": "From Ember's Yearly Electricity Data via Our World in Data \u2014 the same "
          "per-country grid factors used across these tools, shown and linked on the page."},
    {"q": "Does the country I pick matter?",
     "a": "Yes. The same kWh saved avoids more CO\u2082 on a coal-heavy grid than a clean "
          "one. Saving 80 kWh a month avoids far more in India or South Africa than in "
          "France or Norway."},
])
