from core.faqs import register_faqs

register_faqs("clothing-sizes", [
    {"q": "What does the Clothing Size Converter do?",
     "a": "It maps a size you know — say UK 10 — onto its equivalents in the US, EU and Asian "
          "systems, across tops and shoes for men, women and children, using standard "
          "alignment matrices."},
    {"q": "Can you show an example?",
     "a": "A women's top entered as UK 12 returns US 8, EU 40 and Asian L on the same row — the "
          "garment's equivalent size in each region's system."},
    {"q": "How do I read the comparison table?",
     "a": "The converter shows the full matrix with your matched row highlighted, so you can see "
          "your size in every region at once and the rows immediately above and below for "
          "borderline fits."},
    {"q": "Where is this used in real life?",
     "a": "Online shopping from overseas retailers, travel, and gifting, where the same body "
          "measurement carries a different size label in each market."},
    {"q": "Why might the size still not fit?",
     "a": "These are general alignment guides only. Cut, fabric stretch and brand-specific "
          "'vanity sizing' all shift the real fit, so always check the manufacturer's own size "
          "chart and, where possible, the garment measurements."},
])
