from core.faqs import register_faqs

register_faqs("convert-pressure", [
    {"q": "What does the Pressure Converter do?",
     "a": "It converts convert pressure between pa, bar, psi, atm, mmhg/torr and inh₂o via the pascal by first normalising your value to the SI base unit "
          "(pascal) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "1 atm to PSI: 1 × 101325 = 101325 Pa, then ÷ 6894.757 ≈ 14.696 PSI."},
    {"q": 'Where does the number 101,325 come from?',
     "a": 'One standard atmosphere is defined as exactly 101,325 Pa — the average sea-level air pressure. You can check it physically: a 760 mm column of mercury gives ρgh = 13,595 × 9.80665 × 0.76 ≈ 101,325 Pa, which is why a barometer reads 760 mmHg at sea level.'},
    {"q": "Where is this used in real life?",
     "a": "Tyre inflation, weather, hydraulics, diving and process engineering."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
