from core.faqs import register_faqs
register_faqs("carbon-emission-impact", [
    {"q": "What does this calculator do?",
     "a": "It estimates the carbon footprint \u2014 the kilograms of CO\u2082 \u2014 of an "
          "everyday activity: using electricity, burning petrol, or driving a car. You pick "
          "the activity, enter how much, and it does the maths."},
    {"q": "Why do I have to choose a country for electricity?",
     "a": "Because a unit of electricity is far dirtier in some countries than others. In "
          "France (mostly nuclear) a kWh carries about 41 g of CO\u2082; in India it is "
          "around 670 g because the grid leans on coal. The country picker loads the right "
          "number for where you are."},
    {"q": "Where do the numbers come from?",
     "a": "The per-country electricity factors come from Ember's Yearly Electricity Data "
          "(shared openly via Our World in Data). The petrol figure of about 2.31 kg "
          "CO\u2082 per litre is the standard GHG Protocol / US EPA value. Both are shown "
          "with links on the page \u2014 nothing here is made up."},
    {"q": "Can you show a quick example?",
     "a": "Using 100 kWh of electricity in India: 100 \u00d7 670 g = 67,000 g = about 67 kg "
          "of CO\u2082. The same 100 kWh in France would be only about 4 kg \u2014 same "
          "energy, very different carbon."},
    {"q": "Why is petrol the same everywhere but electricity is not?",
     "a": "Petrol's CO\u2082 comes from the fuel's own chemistry \u2014 burning a litre "
          "always makes about 2.31 kg of CO\u2082, wherever you are. Electricity's carbon "
          "depends on how it was generated, which differs hugely from country to country."},
    {"q": "What is 'CO\u2082e'?",
     "a": "It stands for carbon-dioxide-equivalent. Some activities release other "
          "greenhouse gases too, so they are all converted into the amount of CO\u2082 that "
          "would cause the same warming. It lets you compare everything on one scale."},
    {"q": "Is this exact?",
     "a": "No \u2014 it is a good estimate. Real emissions depend on your exact power mix, "
          "your specific car, driving style and more. Use it to understand and compare, not "
          "as an official figure."},
])
