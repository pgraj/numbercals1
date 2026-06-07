from core.faqs import register_faqs

register_faqs("concrete-volume", [
    {"q": "Is this calculator for structural design?",
     "a": "No. It is for quantity estimation only, to help you order roughly the right amount of concrete. Mix design, reinforcement and structural sizing must come from a qualified engineer."},
    {"q": "How does it estimate the volume?",
     "a": "For a slab or footing it multiplies length by width by depth; for a column it uses pi r squared times height. Then it adds a wastage allowance for spillage and uneven ground."},
    {"q": "Why add a wastage allowance?",
     "a": "Because real pours never use the exact theoretical volume. Some is lost to spillage, over-excavation and uneven surfaces, so a few percent extra avoids running short."},
    {"q": "How is the bag count worked out?",
     "a": "It divides the total volume by the yield of one bag (how much mixed concrete a bag makes). Bag yields vary, so check the figure on your specific product and adjust."},
    {"q": "Should I trust the bag number exactly?",
     "a": "Treat it as a guide. Bag yields, mix ratios and how much water you add all change the real coverage, so round up and confirm with your supplier."},
])
