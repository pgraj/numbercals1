from core.faqs import register_faqs

register_faqs('square-of-linear-trinomial', [
    {"q": 'Where would I square a linear expression like ax+by+c?',
     "a": 'All the time in optimisation, statistics, and physics, because squared linear expressions are how we measure error and energy. A line or plane ax+by+c describes a relationship; squaring its value gives the squared deviation from a target, which is exactly what least-squares fitting minimises - the method behind trend lines, regression, and most of machine learning. The expansion shows every contribution to that squared error, including the cross-terms that couple the variables.'},
    {"q": 'Why are there six terms - three squares and three cross-terms?',
     "a": "Because squaring a three-term expression pairs every term with every other. The three terms ax, by, c each get squared (giving a²x², b²y², c²), and each of the three pairs produces a doubled cross-product (2abxy, 2bcy, 2cax). It is the same structure as (a+b+c)² but with the coefficients and variables carried along. Six terms is simply 'three squares plus three pairs'."},
    {"q": 'How does this relate to least-squares and regression?',
     "a": 'Fitting a line or plane to data means choosing coefficients to minimise the sum of squared residuals, where each residual is a linear expression like (ax+by+c) − observed. Expanding those squares produces exactly these square and cross terms, and the cross-terms are what make the variables interact in the solution. The normal equations of regression come directly from expanding and differentiating such squared linear forms.'},
    {"q": 'Does it appear in physics or engineering?',
     "a": 'Yes - the squared magnitude of a quantity built from several linear components expands this way. Energy often depends on the square of a linear combination of variables (displacements, currents, fields), so computing total energy involves exactly these squared and cross terms. The cross-terms represent interaction or coupling between components, which is physically meaningful - they show how the parts reinforce or oppose each other.'},
    {"q": 'Is recognising this pattern useful for simplification?',
     "a": 'Very. A sprawling expression with three squared terms and three matching cross-terms can be collapsed into a single squared bracket (ax+by+c)², which is far easier to handle. Spotting this in an engineering derivation or exam question turns six terms into one, reducing the chance of error and often revealing structure (like a perfect square) that suggests the next step.'},
])
