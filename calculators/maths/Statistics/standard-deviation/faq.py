from core.faqs import register_faqs

register_faqs("standard-deviation", [
    {"q": "What is standard deviation?",
     "a": "The typical distance of a value from the mean, in the data's own units. It is just the square root of the variance, which undoes the squaring so the figure is interpretable again."},
    {"q": "Why is it more useful than variance?",
     "a": "Because it is in the same units as your data. If you measure heights in centimetres, the standard deviation is in centimetres too, whereas variance would be in centimetres squared, which means little to most people."},
    {"q": "Population or sample, which do I pick?",
     "a": "Use population when your numbers are the entire group. Use sample, which divides by N minus 1, when they are a subset you are using to estimate a bigger population."},
    {"q": "What does a small standard deviation tell me?",
     "a": "That the values huddle close to the mean, so the average is a reliable summary. A large one warns that individual values can sit far from the average."},
    {"q": "Where is this used?",
     "a": "Test-score reports, the spread of returns on an investment (its risk), measurement error in science, and the famous bell curve where about 68% of values fall within one standard deviation of the mean."},
])
