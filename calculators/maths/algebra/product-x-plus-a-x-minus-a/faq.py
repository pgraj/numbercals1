from core.faqs import register_faqs

register_faqs('product-x-plus-a-x-minus-a', [
    {"q": "Isn't this just the difference of two squares again?",
     "a": 'Yes - it is the same identity seen from the product side: (x+a)(x−a) = x²−a². Listing it among the product identities highlights how you USE it: when you spot two brackets that are identical except for the sign between the terms, their product instantly collapses to a difference of squares with the middle term gone. That recognition is the practical skill, and it is one of the fastest mental-multiplication tricks there is.'},
    {"q": 'Why does the middle term vanish?',
     "a": "Expanding gives x² − ax + ax − a². The −ax and +ax cancel exactly, leaving x²−a². The cancellation happens precisely because the two brackets differ only in the sign of the second term, so their cross-products are equal and opposite. This 'conjugate pair' structure - same terms, opposite middle sign - is what makes the result so clean."},
    {"q": 'How is this used to rationalise denominators?',
     "a": 'When a denominator contains a surd like (√5 − 2), you multiply top and bottom by its conjugate (√5 + 2). The denominator becomes (√5)² − 2² = 5 − 4 = 1, a clean rational number with the root eliminated. This conjugate trick, powered entirely by (x+a)(x−a) = x²−a², is the standard method for removing square roots from denominators in algebra and calculus.'},
    {"q": 'Where else does the conjugate idea matter?',
     "a": "In complex numbers, multiplying a number by its conjugate (a+bi)(a−bi) gives a²+b², a real number - the basis for dividing complex numbers and for computing magnitudes. In limits and derivatives, multiplying by a conjugate clears troublesome roots so a 0/0 form can be evaluated. The same 'multiply by the conjugate to get a difference of squares' move recurs across maths."},
    {"q": 'Can it speed up arithmetic?',
     "a": 'Very much - it is the classic fast-multiplication trick for numbers symmetric about a round value. 96×104 = (100−4)(100+4) = 100²−4² = 10000−16 = 9984. 23×17 = (20+3)(20−3) = 400−9 = 391. Whenever two numbers are equally spaced around an easy middle, their product is one square minus a tiny square - instant mental arithmetic.'},
])
