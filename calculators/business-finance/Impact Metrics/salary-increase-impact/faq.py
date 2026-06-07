from core.faqs import register_faqs

register_faqs("salary-increase-impact", [
    {"q": "What does this tell me?",
     "a": "Your new annual salary after a percentage pay rise, and the actual money the rise adds. A 5% rise on 60,000 is 3,000 more a year."},
    {"q": "Is this before or after tax?",
     "a": "Before tax. It shows the gross change to your salary; your take-home rise will be smaller once tax is applied, which the Tax Rate Change calculator can illustrate."},
    {"q": "How can I compare two job offers with it?",
     "a": "Run each offer's base and rise to see the resulting salary, then compare the figures directly rather than wrestling with percentages in your head."},
    {"q": "Does a percentage rise compound over years?",
     "a": "A single rise does not, but successive annual rises do build on each other. Run it year by year, using each new salary as the next base, to see the snowball."},
    {"q": "Why does the dollar figure matter more than the percentage?",
     "a": "Because 10% of a small salary can be less cash than 3% of a large one. The absolute gain is what actually lands in your account."},
])
