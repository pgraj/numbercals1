from core.faqs import register_faqs

register_faqs("average", [
    {"q": "What is the mean?",
     "a": "The mean is the everyday average: add all the numbers together and divide by how many there are. It is the single value that best stands in for the whole set when you want one summary figure."},
    {"q": "When is the mean a bad choice?",
     "a": "When the data has extreme outliers. One billionaire walking into a room sends the mean income soaring even though almost everyone is on a normal wage. In skewed data the median often describes the typical value better."},
    {"q": "Does the order of the numbers matter?",
     "a": "No. Adding them up gives the same total whatever order you type them in, so the mean is unaffected by ordering. Sorting only matters for the median."},
    {"q": "Can the mean be a value that is not in the list?",
     "a": "Yes, and usually it is. The mean of 2 and 4 is 3, which never appears in the data. It is a calculated balance point, not necessarily a real data value."},
    {"q": "Where would I use this?",
     "a": "Everywhere from working out your average test score, to a shop tracking average daily sales, to a scientist reporting the average result of repeated measurements."},
])
