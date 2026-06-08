from core.faqs import register_faqs

register_faqs('square-of-sum', [
    {"q": 'Where would I actually use (a+b)² in real life?',
     "a": 'It is the everyday mental-maths shortcut for squaring numbers near a round figure. To square 23 quickly, write it as (20+3)²: 20² + 2·20·3 + 3² = 400 + 120 + 9 = 529 - no long multiplication needed. Engineers and builders use it when a square area grows: enlarge a square plot of side a by an extra strip b on two sides and the new area is exactly a² + 2ab + b², which is why a small increase in side length adds disproportionately more area (the 2ab cross-term). It also appears whenever you expand squared expressions in physics formulas, statistics (variance of a sum), and finance (compounding two combined rates).'},
    {"q": 'Why is there a 2ab term - where does the 2 come from?',
     "a": 'Geometrically, draw a square of side (a+b). It splits into four pieces: a small a×a square, a small b×b square, and TWO identical a×b rectangles - one along the top, one down the side. Those two rectangles are the 2ab. People who forget the middle term and write (a+b)² = a² + b² are forgetting those two rectangles, which is one of the most common algebra mistakes. The animation here shows exactly those terms building up.'},
    {"q": 'How does this help with squaring numbers in my head?',
     "a": 'Split the number into an easy part plus a small part. 31² = (30+1)² = 900 + 60 + 1 = 961. 52² = (50+2)² = 2500 + 200 + 4 = 2704. The trick works because the round part squares easily, the cross term 2ab is a quick doubling, and the small square b² is tiny. With practice this is far faster than long multiplication and is a favourite of mental-maths and competitive-exam techniques.'},
    {"q": 'Does (a+b)² connect to anything in statistics or data?',
     "a": 'Yes. When you add two quantities and look at how their combined value varies, the variance of a sum expands just like (a+b)²: Var(X+Y) = Var(X) + Var(Y) + 2·Cov(X,Y). The 2ab cross-term becomes twice the covariance - how the two move together. So the same algebraic shape that squares 23 also explains why combining two correlated investments or measurements does not simply add their individual variabilities.'},
    {"q": 'Is this identity used in computing or graphics?',
     "a": 'It shows up in distance and lighting calculations. Squared distances (used everywhere in graphics and physics to avoid slow square roots) expand using these identities. When a coordinate changes by a small amount, (a+b)² tells you how the squared distance shifts, and the cross-term 2ab is the dominant change for small b - the basis of many fast approximations in game engines and simulations.'},
])
