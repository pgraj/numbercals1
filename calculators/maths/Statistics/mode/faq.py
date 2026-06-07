from core.faqs import register_faqs

register_faqs("mode", [
    {"q": "What is the mode?",
     "a": "The value that appears most often. Unlike the mean and median, the mode is about frequency, not position or size."},
    {"q": "Can there be more than one mode?",
     "a": "Yes. If two or more values tie for the most appearances, the set is multimodal and all of them are modes. This calculator lists every value that ties for the top count."},
    {"q": "What if nothing repeats?",
     "a": "Then there is no mode, because no value is more common than the others. The calculator tells you this rather than inventing one."},
    {"q": "When is the mode the most useful average?",
     "a": "For categories and whole-number counts, like the most common shoe size a shop sells or the most frequent star rating a product gets. You cannot take a 'mean' shoe style, but you can find the most popular one."},
    {"q": "Can data have a mode that is not in the middle?",
     "a": "Absolutely. The most common value can sit anywhere in the range, which is why the mode can differ sharply from the mean and median."},
])
