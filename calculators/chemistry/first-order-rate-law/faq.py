from core.faqs import register_faqs

register_faqs('first-order-rate-law', [
    {"q": 'What is a first-order reaction?',
     "a": 'One whose speed depends on the amount of a single reactant: double that reactant and the rate doubles. It decays exponentially - losing the same fraction in each equal time slice. Radioactivity is the classic case.'},
    {"q": 'What is special about its half-life?',
     "a": 'It is constant - the time to lose half is the same whether you start with a lot or a little. That is why the example uses [A]₀ = 1, [A] = 0.5 (exactly half left) with t = 693 s, giving k ≈ 0.001 s⁻¹.'},
    {"q": 'Why the 2.303 and the log?',
     "a": 'Exponential decay leads to a natural-log relationship. The 2.303 converts a base-10 log (easy on a calculator) into the natural log the maths actually needs, since ln(x) = 2.303 × log₁₀(x).'},
    {"q": 'How is it used in medicine?',
     "a": 'Drugs usually clear first-order, giving a half-life that sets how often you must take them. This rate-constant calculation is how dosing schedules are designed.'},
    {"q": 'How does carbon dating use it?',
     "a": 'Carbon-14 decays first-order with a 5,730-year half-life. Measuring how much is left and applying this maths gives the age of a once-living sample.'},
])
