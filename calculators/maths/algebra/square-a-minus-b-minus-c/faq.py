from core.faqs import register_faqs

register_faqs('square-a-minus-b-minus-c', [
    {"q": 'Where is the (a−b−c)² form used in practice?',
     "a": 'Wherever a starting quantity has two amounts subtracted and the result is then squared - common in error and tolerance analysis. If a target value a has two deductions b and c, the squared deviation (a−b−c)² expands with these specific signs. The interesting feature is that the b-c cross-term is POSITIVE while the a-b and a-c terms are negative, because b and c are both subtracted from a, so they share the same sign relative to a but the opposite relative to each other.'},
    {"q": 'Why is the bc term positive when the others are negative?',
     "a": "Sign-tracking is the whole lesson here. Each cross-term's sign is the product of the two variables' signs in the bracket. In (a − b − c), a is positive, b is negative, c is negative. So a·b is (+)(−) = negative → −2ab; a·c is negative → −2ca; but b·c is (−)(−) = positive → +2bc. Two negatives multiply to a positive. This is exactly the kind of sign bookkeeping that trips students up, and the term-by-term animation makes each sign explicit."},
    {"q": 'Does this come up in real measurement problems?',
     "a": 'Yes - subtracting two corrections from a baseline and squaring the residual is routine in metrology and quality control. For example, a machined length starts at a, then two separate wear allowances b and c are removed; the squared error from nominal expands this way. Getting the cross-term signs right matters because they determine whether the combined effect of the two corrections reinforces or partly cancels.'},
    {"q": 'How is this different from (a+b+c)²?',
     "a": 'Only the signs of the cross-terms change; the three squared terms (a², b², c²) are always positive because squaring removes sign. In (a+b+c)² all three cross-terms are positive. In (a−b−c)², the terms pairing a with a subtracted variable are negative, while the term pairing the two subtracted variables is positive. Comparing the two side by side is the clearest way to learn that squaring kills signs on the square terms but preserves the sign logic on the cross-terms.'},
    {"q": 'Is there a mental-maths use?',
     "a": 'It helps square numbers expressed as a base minus two parts, but its main value is as a factorisation and simplification aid. Spotting that a messy expression matches the (a−b−c)² pattern lets you rewrite six terms as a single squared bracket, which is a powerful simplification in engineering derivations and exam algebra where compactness reduces error.'},
])
