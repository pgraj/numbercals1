from core.faqs import register_faqs

register_faqs("ratio", [
    {"q": "How do I simplify a ratio?",
     "a": "Divide both sides by their greatest common divisor. 12:18 both divide "
          "by 6, giving 2:3 — the simplest form."},
    {"q": "What does a ratio actually mean?",
     "a": "It compares two quantities by how many parts each has. 2:3 means for "
          "every 2 of the first thing there are 3 of the second."},
    {"q": "Is 2:3 the same as 12:18?",
     "a": "Yes — they are equivalent ratios. Simplifying does not change the "
          "relationship, only the size of the numbers used to describe it."},
    {"q": "Where is this used in real life?",
     "a": "Cooking — mixing rice and water 1:2 means 1 cup rice to 2 cups water. "
          "Maps and models — a 1:100 scale means 1 cm on paper is 100 cm in "
          "reality. Mixing — petrol-to-oil at 50:1 for a two-stroke engine. "
          "Sharing — splitting $50 in the ratio 2:3 gives $20 and $30."},
    {"q": "What do the squares show?",
     "a": "Each coloured square is one part. Counting the two colours shows the "
          "simplified ratio visually, so 2:3 appears as 2 squares beside 3."},
])
