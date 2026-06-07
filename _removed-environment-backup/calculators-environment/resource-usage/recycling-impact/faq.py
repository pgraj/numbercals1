from core.faqs import register_faqs
register_faqs("recycling-impact", [
    {"q": "What does this calculator do?",
     "a": "It estimates the CO\u2082 you avoid by recycling material instead of throwing it "
          "in the bin to be landfilled. Enter the kilograms recycled and it gives the "
          "emissions saved."},
    {"q": "How does recycling save CO\u2082?",
     "a": "Two ways. Making things from recycled material usually takes much less energy "
          "than making them from raw materials, and keeping waste out of landfill avoids "
          "the methane it would release as it rots. Together those are the 'avoided' "
          "emissions."},
    {"q": "Can you show an example?",
     "a": "Recycling 10 kg of mixed household recyclables avoids about 31 kg of CO\u2082e, "
          "using the US EPA's average figure of roughly 3.12 kg saved per kilogram "
          "recycled."},
    {"q": "Where does the factor come from?",
     "a": "From the US EPA's WARM model: recycling instead of landfilling mixed waste "
          "avoids about 2.83 tonnes of CO\u2082e per short ton, which works out to about "
          "3.12 kg per kilogram. The page links to the EPA source."},
    {"q": "Do all materials save the same amount?",
     "a": "No \u2014 this is an average across typical recyclables. Aluminium saves a LOT "
          "per kilogram (making new aluminium is very energy-hungry), paper saves a good "
          "amount, and glass saves less. For one specific material, the EPA's WARM tool "
          "gives a material-by-material figure."},
    {"q": "Is recycling always better than landfill?",
     "a": "For the common household materials here, recycling comes out ahead on carbon. "
          "The exact benefit depends on local systems and how clean the material is \u2014 "
          "contaminated recycling can end up landfilled anyway, so rinsing helps."},
])
