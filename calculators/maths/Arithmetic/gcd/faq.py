from core.faqs import register_faqs

register_faqs("gcd", [
    {"q": "What is the greatest common divisor?",
     "a": "The largest number that divides both inputs with no remainder. The GCD "
          "of 48 and 36 is 12."},
    {"q": "What is Euclid's algorithm?",
     "a": "A fast method: replace the larger number with its remainder when "
          "divided by the smaller, and repeat until one becomes zero. The last "
          "non-zero value is the GCD. It dates back to Euclid's Elements (c. 300 BC)."},
    {"q": "Is GCD the same as HCF?",
     "a": "Yes. Highest Common Factor (HCF) and Greatest Common Divisor (GCD) are "
          "two names for the same thing."},
    {"q": "Where is this used in real life?",
     "a": "Simplifying fractions — 48/36 divides top and bottom by their GCD 12 "
          "to give 4/3. Even sharing — splitting 48 pens and 36 pencils into the "
          "most identical kits possible makes 12 kits. Tiling — the largest "
          "square tile that fits a 48 × 36 cm area exactly is 12 × 12 cm."},
    {"q": "What do the tiles show?",
     "a": "Each number is drawn as a row of g-sized tiles, where g is the GCD. "
          "Because both rows use the same tile size, you can see the GCD is the "
          "biggest square that measures both lengths exactly."},
])
