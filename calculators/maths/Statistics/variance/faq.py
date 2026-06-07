from core.faqs import register_faqs

register_faqs("variance", [
    {"q": "What does variance measure?",
     "a": "How spread out the data is. It is the average of the squared distances of each value from the mean, so a big variance means the values are scattered and a small one means they cluster tightly."},
    {"q": "Why square the differences?",
     "a": "Squaring makes every gap positive (so they do not cancel out) and punishes large gaps more than small ones. The downside is the units are squared, which is why standard deviation, the square root, is often quoted instead."},
    {"q": "What is the difference between population and sample variance?",
     "a": "Population variance divides by N and is used when you have every member of the group. Sample variance divides by N minus 1 to correct for the fact that a sample tends to underestimate the true spread."},
    {"q": "Why divide by N minus 1 for a sample?",
     "a": "Because the sample mean is itself estimated from the data, the squared gaps come out a touch too small. Dividing by N minus 1 nudges the estimate up to be unbiased. This is called Bessel's correction."},
    {"q": "When would I actually use variance?",
     "a": "It underpins risk in finance, quality control in manufacturing, and almost every statistical test. On its own it is a bit abstract, which is why its square root, the standard deviation, gets more airtime."},
])
