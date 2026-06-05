from core.faqs import register_faqs

register_faqs("packaging-units", [
    {"q": "What does the Retail Packaging Converter do?",
     "a": "It translates a quantity at any level of the supply chain — pallets, cases, packs or "
          "individual units — into every other level, using the units-per-level you supply for "
          "your specific product."},
    {"q": "Can you show a worked example?",
     "a": "With 24 units/pack, 12 packs/case and 40 cases/pallet, one pallet holds 24 × 12 × 40 "
          "= 11,520 units. So 2 pallets = 23,040 units = 960 cases."},
    {"q": "Where is this used in real life?",
     "a": "Warehouse picking, purchase-order sizing, retail replenishment and freight planning, "
          "where staff routinely move between ordering in cases and stocking in single units."},
    {"q": "What are the limits?",
     "a": "Every level multiplier must be positive. Roll-ups can produce fractional pallets or "
          "cases (e.g. 1.5 pallets) — this reflects partial loads and is expected, not an error."},
    {"q": 'Does the step-by-step working change when I change the ratios?',
     "a": 'Yes. The working multiplies your quantity by the units contained in your chosen level, where units per pallet = cases/pallet × packs/case × units/pack. Change any ratio and both the total and every roll-up figure update accordingly.'},
])
