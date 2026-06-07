from core.faqs import register_faqs
register_faqs("energy-usage-impact", [
    {"q": "What does this calculator do?",
     "a": "It turns your electricity use (in kilowatt-hours) into the CO\u2082 it causes, "
          "using your country's grid factor. Enter your price per kWh and it shows the cost "
          "too."},
    {"q": "What is a kilowatt-hour?",
     "a": "A kilowatt-hour (kWh) is the unit on your electricity bill. A 1000-watt heater "
          "running for one hour uses one kWh. A typical home might use several hundred kWh "
          "a month."},
    {"q": "Where does the carbon factor come from?",
     "a": "From Ember's Yearly Electricity Data, shared openly through Our World in Data. "
          "Each country has its own value because grids differ \u2014 the page shows the "
          "exact figure used and links to the source."},
    {"q": "Can you show an example?",
     "a": "100 kWh in India: 100 \u00d7 670 g = about 67 kg of CO\u2082. If your price were "
          "8 (in your local currency) per kWh, the cost would be 100 \u00d7 8 = 800."},
    {"q": "Why does the country change the answer so much?",
     "a": "A coal-heavy grid can be ten times more carbon-intensive than a hydro- or "
          "nuclear-heavy one. So the same 100 kWh might mean 67 kg of CO\u2082 in one "
          "country and under 5 kg in another."},
    {"q": "Does this include the cost of heating or my appliances' efficiency?",
     "a": "No \u2014 it works purely from the kWh you enter. How efficiently you use that "
          "energy is up to your appliances; this just tells you the carbon (and optional "
          "cost) of whatever amount you put in."},
])
