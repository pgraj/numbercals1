from core.faqs import register_faqs

register_faqs('square-of-trinomial', [
    {"q": 'When would I ever square a sum of three things?',
     "a": 'Whenever three quantities combine and you need the square of the total - which is common in statistics and physics. The standout real use is variance of a sum of three variables: Var(X+Y+Z) expands into the three individual variances plus twice each pairwise covariance, exactly mirroring a²+b²+c²+2ab+2bc+2ca. Portfolio risk with three assets uses precisely this: the total risk is not just the sum of individual risks, but includes the cross-terms showing how each pair moves together.'},
    {"q": 'Why are there exactly three cross-terms?',
     "a": 'Because with three items there are three distinct pairs: a-b, b-c, and c-a. Each pair contributes a doubled product (the 2 comes from each pair appearing twice when you multiply the trinomial by itself, just like in (a+b)²). So you get three squares (one per term) and three cross-terms (one per pair). If you had four terms, you would get four squares and six cross-terms - the cross-terms grow as the number of pairs, which is why combining many things gets complicated fast.'},
    {"q": 'Where does this show up in physics?',
     "a": 'In computing the magnitude of a vector with three components. The squared length of a 3D vector is x²+y²+z², and if the vector is itself a sum of parts, expanding the square produces the cross-terms here. Energy calculations involving three contributions, and the law of cosines generalised to several terms, also rely on this expansion. Any time three measured quantities add and you need the square of the result, this identity does the work.'},
    {"q": 'Is it useful for mental arithmetic too?',
     "a": 'It can square numbers split into three convenient parts, though it is most valued for its structure. Its bigger everyday role is as a checking and factorising tool: if you see an expression like a²+b²+c²+2ab+2bc+2ca, you can instantly recognise it as a perfect square (a+b+c)² and collapse it - which simplifies otherwise messy algebra in engineering and exam problems.'},
    {"q": 'How is this used in data science or finance?',
     "a": "Directly in risk and error analysis with three sources. Combining three independent measurements, three forecast components, or three asset returns, the variance of the combination follows this exact pattern: sum of the parts' variances plus twice the pairwise covariances. Recognising the (a+b+c)² shape lets analysts see at a glance that ignoring the cross-terms (assuming things are independent when they are not) under- or over-states the combined risk."},
])
