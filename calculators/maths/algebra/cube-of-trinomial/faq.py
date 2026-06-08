from core.faqs import register_faqs

register_faqs('cube-of-trinomial', [
    {"q": 'When would anyone cube a sum of three terms?',
     "a": 'It is mostly an algebraic and exam tool rather than an everyday calculation, but the underlying situation - the cubic growth of a total made of three parts - does arise in volume scaling and combinatorial counting. The neat compact form shown here, a³+b³+c³+3(a+b)(b+c)(c+a), is far easier to use and verify than the full ten-term expansion, and recognising it lets you collapse a long expression into something manageable.'},
    {"q": 'Why is the compact form 3(a+b)(b+c)(c+a) so much tidier?',
     "a": 'The full expansion of (a+b+c)³ has ten terms: three cubes plus six terms like 3a²b and a 6abc term. That is unwieldy. Mathematicians discovered that all the non-cube terms factor neatly as 3(a+b)(b+c)(c+a). So instead of tracking ten terms you track one product. This kind of clever refactoring - hiding complexity inside a compact product - is exactly the skill that makes hard algebra tractable, and it is a frequent exam shortcut.'},
    {"q": 'Does this relate to anything in higher maths?',
     "a": "Yes - symmetric polynomials. Expressions that stay the same when you swap the variables (like a+b+c, ab+bc+ca, abc) recur throughout algebra, and (a+b+c)³ is built from them. They appear in the relationships between a polynomial's roots and its coefficients (Vieta's formulas), which matter in solving equations. So this identity is a stepping stone to understanding how roots and coefficients connect."},
    {"q": 'Is there a practical computation use?',
     "a": 'Its practical value is simplification and verification. If a derivation produces a sprawling sum of cubes and cross-terms in three variables, recognising the (a+b+c)³ structure lets you compress it, reducing the chance of arithmetic slips in engineering or physics work. The calculator lets you confirm numerically that the compact form really equals the cube for your values, building trust in the shortcut.'},
    {"q": 'How is the cube of three terms different from the square?',
     "a": 'The square (a+b+c)² has six terms (three squares, three cross-terms). The cube is much richer: three cubes, six squared-times-other terms, and a 6abc term - ten in all - which is why the compact factored form is so welcome. The jump in complexity from square to cube illustrates a general theme: each extra power multiplies the number of terms, so factored and compact forms become increasingly valuable as powers grow.'},
])
