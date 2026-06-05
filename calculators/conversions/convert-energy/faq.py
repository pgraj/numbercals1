from core.faqs import register_faqs

register_faqs("convert-energy", [
    {"q": "What does the Energy Converter do?",
     "a": "It converts convert energy between joules, calories, watt-hours, btu and electronvolts via the joule by first normalising your value to the SI base unit "
          "(joule) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "1 kWh to MJ: 1 × 3.6e6 = 3.6e6 J, then ÷ 1e6 = 3.6 MJ."},
    {"q": 'Why does the same energy have so many units?',
     "a": 'Energy is one physical quantity, but fields invented their own units: joules in physics, calories in chemistry and food, watt-hours and kWh in electricity, BTU in heating. They all convert through the joule. Note the food "Calorie" is actually a kilocalorie (4184 J).'},
    {"q": "Where is this used in real life?",
     "a": "Nutrition (kcal), utility bills (kWh), HVAC (BTU) and physics (eV)."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
