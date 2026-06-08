from core.faqs import register_faqs

register_faqs('cube-a-minus-b-minus-c', [
    {"q": 'Where does the (a−b−c)³ form appear?',
     "a": 'Wherever a baseline quantity has two amounts removed and the result feeds a cubic (volume-like) measure. It is more of a sign-handling exercise than a daily formula, but it teaches a genuinely useful skill: correctly cubing a bracket with multiple negative terms. The safest practical approach, which this calculator demonstrates, is often to compute (a−b−c) first and then cube that single number, rather than expanding all ten signed terms by hand.'},
    {"q": 'Why is cubing a multi-term bracket so error-prone?',
     "a": 'Because every term picks up sign contributions from three factors, and with two negative variables the signs interact in non-obvious ways. A term like 3a²(b+c) is straightforward, but terms mixing b and c, and the 6abc term, can flip sign depending on how many negatives they contain. This is precisely why verifying numerically - plug in numbers, compute the bracket, cube it, and check against your expansion - is such valuable practice.'},
    {"q": 'What is the most reliable way to evaluate this?',
     "a": 'Collapse first, then cube. Work out the value inside the bracket (a − b − c) as a single number, then cube that. For a=9, b=2, c=1 the bracket is 6, and 6³ = 216 - no sign juggling required. The expanded form matters when you need the symbolic breakdown (for factorising or calculus), but for a numeric answer, simplifying the bracket first avoids almost all the sign mistakes.'},
    {"q": 'Does this kind of expression occur in real calculations?',
     "a": 'In tolerance and volume analysis, yes: a nominal dimension reduced by two separate allowances, then cubed for a volume estimate. More broadly, cubic expressions of signed sums appear in physics (volumes, certain energy terms) and in numerical methods. The key takeaway is procedural - know how to handle the signs, and verify - rather than the specific formula being something you reach for often.'},
    {"q": 'Why show the full expansion if collapsing first is easier?',
     "a": 'Because seeing the expansion teaches where every term and sign comes from, which you need when the variables are symbolic (you cannot just compute a number) - for instance when factorising or differentiating. The step-by-step view builds the understanding; the collapse-first trick is the practical shortcut once you trust the algebra. Both skills matter, and the calculator lets you confirm they agree.'},
])
