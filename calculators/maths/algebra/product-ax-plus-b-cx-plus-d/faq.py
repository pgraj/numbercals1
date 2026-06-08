from core.faqs import register_faqs

register_faqs('product-ax-plus-b-cx-plus-d', [
    {"q": 'Why does the general (ax+b)(cx+d) matter beyond (x+a)(x+b)?',
     "a": "Because real quadratics often have a leading coefficient other than 1 - like 6x²+11x+3 - and those need this fuller form to factor. Here the x² coefficient is the product ac, the constant is bd, and the middle term combines both cross-products as ad+bc. This is the basis of factoring 'hard' quadratics (the ones where you cannot just find two numbers that add and multiply), using methods like the AC-method or grouping."},
    {"q": 'How does this connect to the AC-method of factoring?',
     "a": 'The AC-method factors ax²+bx+c by finding two numbers that multiply to a·c and add to b - which is exactly searching for the ad and bc pieces of this identity. Once found, you split the middle term and factor by grouping, recovering the (ax+b)(cx+d) form. So this identity is the theoretical justification for that widely-taught technique for factoring quadratics with a leading coefficient.'},
    {"q": 'Where do quadratics with a leading coefficient appear?',
     "a": 'Constantly in physics and engineering, where coefficients come from physical constants, not tidy integers - projectile equations with a ½g factor, electrical and mechanical resonance, optimisation where rates differ. Economics too: revenue or cost curves rarely have a leading coefficient of exactly 1. The general product identity is what lets you expand and factor these realistic models.'},
    {"q": 'Why is the middle term ad+bc and not just one product?',
     "a": "Multiplying (ax+b)(cx+d) produces four terms: ac·x² (the x²), ad·x and bc·x (two separate x-terms), and bd (the constant). The two x-terms combine, so the middle coefficient is their sum, ad+bc. This 'cross-multiply and add' pattern is the heart of the FOIL method (First, Outer, Inner, Last) and explains why factoring with a leading coefficient is trickier - the middle term mixes two products."},
    {"q": 'Is this the same as the FOIL method?',
     "a": 'Yes - FOIL (First, Outer, Inner, Last) is just a way to remember the four products when expanding two binomials: First gives acx², Outer and Inner give the adx and bcx that combine into the middle term, and Last gives bd. This identity is the general result FOIL produces. Understanding it means you can expand any product of two linear terms reliably, and reverse the process to factor.'},
])
