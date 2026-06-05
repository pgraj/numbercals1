from core.faqs import register_faqs

register_faqs("convert-stress", [
    {"q": "What does the Stress & Modulus Converter do?",
     "a": "It converts mechanical stress and elastic modulus between Pa, MPa, GPa, PSI and ksi by first normalising your value to the SI base unit "
          "(pascal) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "250 MPa to PSI: 250 × 1e6 = 2.5e8 Pa, then ÷ 6894.757 ≈ 36,259 PSI."},
    {"q": "What is the difference between stress and modulus?",
     "a": "Both share these units. Stress is the load a material currently carries (force per unit area); the elastic modulus is its stiffness — how much stress is needed to stretch it by a given fraction. Steel yields near 250 MPa but has a modulus of about 200 GPa, roughly a thousand times larger."},
    {"q": "Where is this used in real life?",
     "a": "Structural and mechanical engineering, materials testing and design codes."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
