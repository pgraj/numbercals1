from core.faqs import register_faqs

register_faqs("geo-pythagoras", [
    {
        "q": "What is Pythagoras' theorem?",
        "a": "Pythagoras' theorem states that in a right-angled triangle, the "
             "square of the hypotenuse (the longest side, opposite the right "
             "angle) equals the sum of the squares of the other two sides. "
             "Written as a² + b² = c², it lets you find any one side when you "
             "know the other two.",
    },
    {
        "q": "How do I find the hypotenuse from the two legs?",
        "a": "Square each leg, add the results, then take the square root. For "
             "example, with legs of 3 and 4: 3² + 4² = 9 + 16 = 25, and the "
             "square root of 25 is 5, so the hypotenuse is 5.",
    },
    {
        "q": "Can I use it to find a shorter side instead of the hypotenuse?",
        "a": "Yes. Rearrange the formula to leg = √(c² − other²). Subtract the "
             "known leg's square from the hypotenuse's square, then take the "
             "square root. With a hypotenuse of 13 and one leg of 5: "
             "√(169 − 25) = √144 = 12.",
    },
    {
        "q": "Does the theorem work for every triangle?",
        "a": "No. Pythagoras' theorem only applies to right-angled triangles — "
             "those with one 90° angle. For triangles without a right angle you "
             "need the sine rule or cosine rule instead, which are covered in "
             "later trigonometry calculators.",
    },
    {
        "q": "Where is this used in real life?",
        "a": "Builders and carpenters use it to check that corners are square; "
             "surveyors and navigators use it to measure straight-line distances; "
             "architects size diagonal braces and roof rafters; and game "
             "developers and computer-graphics engineers use it constantly to "
             "compute distances between points on screen.",
    },
])
