from core.faqs import register_faqs

register_faqs("trig-general-solution", [
    {"q": 'What is a general solution?',
     "a": 'It is a single expression, using an integer n, that captures every solution of a trig equation at once — rather than listing solutions inside a fixed domain.'},
    {"q": 'What are the three patterns?',
     "a": 'For sin x = sin α: x = α + 360°n or x = 180° − α + 360°n. For cos x = cos α: x = ±α + 360°n. For tan x = tan α: x = α + 180°n. In radians replace 360° with 2π and 180° with π.'},
    {"q": 'Can you show a worked example?',
     "a": 'For sin x = sin 30°, the general solution is x = 30° + 360°n or x = 150° + 360°n. Putting n = 0, 1 gives 30°, 150°, 390°, 510°… In radians α = π/6 and the period is 2π; switch the toggle to see it.'},
    {"q": 'How do I get the in-range solutions back?',
     "a": 'Substitute the integer values of n that land inside the required domain. Each n gives one concrete solution, so a domain of one turn usually picks out two of them.'},
    {"q": 'Where is this used?',
     "a": 'Anywhere a periodic condition recurs indefinitely — repeated alignment of rotating parts, recurring tide or daylight conditions, and resonance timing.'},
])
