from core.faqs import register_faqs
register_faqs("water-usage-impact", [
    {"q": "What does this calculator do?",
     "a": "It estimates the hidden carbon footprint of tap water \u2014 the CO\u2082 from the "
          "electricity used to pump, treat and distribute it, and to treat the wastewater "
          "afterwards."},
    {"q": "Wait, water has a carbon footprint?",
     "a": "A small one, yes. Clean water does not arrive by magic \u2014 pumps, treatment "
          "plants and pipes all run on electricity. That electricity has a carbon cost, so "
          "each litre carries a tiny share of it."},
    {"q": "Can you show an example?",
     "a": "1000 litres (one cubic metre) needs about 0.6 kWh to supply and treat. In India "
          "that 0.6 kWh makes about 0.4 kg of CO\u2082. So a thousand litres is well under "
          "half a kilogram of carbon \u2014 small per litre, but it adds up at city scale."},
    {"q": "Does this include heating the water?",
     "a": "No \u2014 and that is the big one to remember. Heating water at home (showers, "
          "washing) usually uses far MORE energy than supplying it. This calculator covers "
          "only the supply and treatment, not your water heater."},
    {"q": "Where do the numbers come from?",
     "a": "The energy-per-litre figure (about 0.6 kWh per 1000 L) is a typical value from "
          "World Bank ESMAP and water-sector studies; supply is around 0.37 kWh/m\u00b3 and "
          "treatment adds roughly 0.5\u20132.0 kWh/m\u00b3. The grid factor is from Ember / "
          "Our World in Data. All are linked on the page."},
    {"q": "How accurate is it?",
     "a": "It is a rough guide. Real energy per litre varies a lot by region, water source "
          "(pumping from deep groundwater uses more) and treatment level. Treat it as an "
          "order-of-magnitude estimate."},
])
