from core.faqs import register_faqs

register_faqs('cube-of-linear-binomial', [
    {"q": 'When do I need to cube a linear expression like ax+b?',
     "a": 'Whenever a cubic model is built from a scaled-and-shifted variable - common in physics, engineering, and calculus. Many cubic curves are most naturally written as (ax+b)³ (a stretched, shifted basic cube), and expanding reveals the standard polynomial form for differentiation, integration, or graphing. It also generalises the (a+b)³ volume idea to cases where one dimension is scaled by a factor a, which arises in similar-shape scaling problems.'},
    {"q": 'What do the coefficients 1, 3, 3, 1 carry here?',
     "a": "They are the binomial coefficients from Pascal's triangle, the same as in (a+b)³, but now each term also carries powers of the coefficient a and the variable x. So a³x³ (all three factors are ax), 3a²bx² (two ax and one b), 3ab²x (one ax and two b), and b³ (all b). The 1-3-3-1 pattern counts the combinations; the a's, b's, and x's track which factor each combination used."},
    {"q": 'How is this used in calculus?',
     "a": 'Cubic functions like (2x+1)³ appear constantly, and to differentiate or integrate them you often expand to the polynomial form a³x³+3a²bx²+3ab²x+b³, or use the chain rule which produces the same structure. Expanding also helps with Taylor and binomial series, where powers of linear expressions are the building blocks. Knowing the expanded form lets you check chain-rule answers and integrate term by term.'},
    {"q": 'Does it have a geometric or scaling meaning?',
     "a": "Yes - it describes the volume of a cube whose side is a scaled, shifted length ax+b. If a length is stretched by factor a and then increased by b, the resulting cube's volume expands with these terms, where the a³x³ part is the pure scaling and the other terms account for the added b. This connects to how volumes change under scaling, relevant in design, manufacturing, and physics."},
    {"q": 'How is it different from the plain (a+b)³?',
     "a": 'Structurally identical - same 1-3-3-1 coefficients - but the leading term ax carries a coefficient a that gets cubed and squared through the expansion, so you see a³x³, 3a²bx², and so on instead of just a³, 3a²b. It is the realistic version for when your variable is multiplied by something other than 1, which is the usual case in applied problems where coefficients come from physical or economic constants.'},
])
