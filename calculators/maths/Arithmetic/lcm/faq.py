from core.faqs import register_faqs

register_faqs("lcm", [
    {"q": "What is the least common multiple?",
     "a": "The smallest number that both inputs divide into evenly. The LCM of 4 "
          "and 6 is 12, because 12 is the first number in both times-tables."},
    {"q": "How is the LCM calculated?",
     "a": "A reliable shortcut is LCM(a, b) = (a × b) / GCD(a, b). For 4 and 6: "
          "(4 × 6) / 2 = 12."},
    {"q": "Where is this used in real life?",
     "a": "Adding fractions — the LCM of the denominators is the smallest common "
          "denominator. Scheduling — if one bus comes every 4 minutes and another "
          "every 6, they arrive together every 12 minutes (LCM of 4 and 6). "
          "Packaging — matching items sold in packs of different sizes so none "
          "are left over."},
    {"q": "Why is the LCM useful for fractions specifically?",
     "a": "To add 1/4 and 1/6 you need a common denominator. The LCM of 4 and 6 "
          "is 12, so both become twelfths: 3/12 + 2/12 = 5/12 — using the "
          "smallest possible numbers."},
    {"q": "What does the number line show?",
     "a": "Each row marks the multiples of one number. The LCM is the first point "
          "where a mark from both rows lines up."},
])
