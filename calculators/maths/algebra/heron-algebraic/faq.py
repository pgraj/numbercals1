from core.faqs import register_faqs
register_faqs("heron-algebraic", [
    {"q": "How does algebra prove Heron's formula?",
     "a": "Drop a height onto the base, splitting the triangle into two right "
          "triangles that share that height. The Pythagorean theorem locates "
          "where the height lands and gives its length, then Area = 1/2 base x "
          "height. Simplifying with the difference-of-squares identity yields "
          "Heron's formula."},
    {"q": "What role does the Pythagorean theorem play?",
     "a": "It is the only tool used. Writing Pythagoras for each of the two right "
          "triangles and subtracting eliminates the height to find the foot of "
          "the altitude; applying it once more gives the height itself. No "
          "trigonometry is involved."},
    {"q": "Can you give a worked example?",
     "a": "For sides a=4, b=3, base c=5: d = (9-16+25)/(2 x 5) = 1.8, height = "
          "sqrt(9 - 1.8 squared) = 2.4, so Area = 1/2 x 5 x 2.4 = 6 -- matching "
          "Heron's formula."},
    {"q": "Why is this version filed under Algebra?",
     "a": "Because the proof is carried out entirely with algebraic manipulation "
          "and the Pythagorean theorem -- expanding, subtracting, and factoring -- "
          "rather than with angles or trigonometric ratios."},
    {"q": "Where is this used in real life?",
     "a": "The base-times-height idea and the algebra behind it underpin area "
          "calculations in construction, land surveying, and any setting where a "
          "triangle's area is found from measured lengths rather than angles."},
])
