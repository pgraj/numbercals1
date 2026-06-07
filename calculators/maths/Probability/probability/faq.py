from core.faqs import register_faqs

register_faqs("probability", [
    {"q": "What is probability?",
     "a": "A number from 0 to 1 (or 0% to 100%) saying how likely something is. Zero means impossible, one means certain, and a half means an even chance like a coin flip."},
    {"q": "How do I work it out?",
     "a": "For equally likely outcomes, divide the number of outcomes you want by the total number of possible outcomes. Rolling a 5 on a die is one favourable outcome out of six, so 1/6."},
    {"q": "What does 'equally likely' mean and why does it matter?",
     "a": "It means each outcome has the same chance, like faces on a fair die. The simple favourable-over-total formula only works when that holds; a loaded die would need different maths."},
    {"q": "What is the probability of the event NOT happening?",
     "a": "One minus the probability that it does. If there is a 0.25 chance of rain, there is a 0.75 chance of no rain. This calculator shows both."},
    {"q": "Can probability be more than 1?",
     "a": "No. If your favourable count ever exceeds the total, something has gone wrong with the setup, which is why the calculator flags it."},
])
