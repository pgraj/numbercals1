from core.faqs import register_faqs

register_faqs("median", [
    {"q": "What is the median?",
     "a": "The middle value once you line the numbers up in order. Half the data sits below it and half above, so it marks the centre of the set."},
    {"q": "What if there is an even number of values?",
     "a": "There is no single middle, so you take the two middle values and average them. For 1, 2, 3, 4 the middles are 2 and 3, giving a median of 2.5."},
    {"q": "Why use the median instead of the mean?",
     "a": "Because it ignores how extreme the outliers are. House prices and incomes are usually reported as medians, since a few huge values would drag the mean to a figure that represents almost nobody."},
    {"q": "Do I have to sort the numbers first?",
     "a": "Yes, sorting is the whole point. The calculator sorts them for you, but the median is meaningless until the values are in order."},
    {"q": "Can the median equal the mean?",
     "a": "Yes, when the data is symmetric. The further apart they drift, the more skewed your data is, which is a useful clue in itself."},
])
