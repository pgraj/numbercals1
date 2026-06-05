from core.faqs import register_faqs

register_faqs("density-weight", [
    {"q": "What does the Density & Shipping Weight Converter do?",
     "a": "It turns a volume of a known material into its real weight using the formula "
          "weight = volume × density, drawing density values from a built-in catalogue of "
          "common shipping materials."},
    {"q": "Can you show a worked example?",
     "a": "200 litres of water: 200 L = 0.2 m³, water density 1000 kg/m³, so weight = 0.2 × 1000 "
          "= 200 kg. The same 200 L of petrol (745 kg/m³) weighs only 149 kg."},
    {"q": "How do I read the graph?",
     "a": "The comparison bar plots your computed weight against the weight the same volume would "
          "have for a few reference materials, showing how dramatically density changes the load."},
    {"q": "Where is this used in real life?",
     "a": "Freight and logistics (chargeable weight), tank and container loading, and trades that "
          "buy by volume but ship or price by weight."},
    {"q": "How accurate is the catalogue?",
     "a": "Densities are nominal values at typical conditions; real materials vary with "
          "temperature, grade, moisture and purity. Use your supplier's specification for "
          "anything safety- or cost-critical."},
])
