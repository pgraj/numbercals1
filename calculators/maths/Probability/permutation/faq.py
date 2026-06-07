from core.faqs import register_faqs

register_faqs("permutation", [
    {"q": "What is a permutation?",
     "a": "An arrangement where order matters. Picking a gold, silver and bronze medallist from 8 runners is a permutation, because first and second are different outcomes."},
    {"q": "How is it different from a combination?",
     "a": "Order. Permutations count 'AB' and 'BA' as two different results; combinations treat them as the same selection. That is why nPr is always at least as big as nCr."},
    {"q": "What does the formula n! / (n-r)! actually do?",
     "a": "It counts the choices at each step: n options for the first pick, n-1 for the second, and so on for r picks. The factorial fraction is a tidy way to write that running product."},
    {"q": "What is a factorial?",
     "a": "n! means multiply every whole number from 1 up to n. So 5! = 5x4x3x2x1 = 120. It counts the ways to arrange n distinct items in a row."},
    {"q": "Where do permutations show up?",
     "a": "PIN codes and passwords, race finishing orders, seating arrangements, and any lock or code where the sequence is what counts."},
])
