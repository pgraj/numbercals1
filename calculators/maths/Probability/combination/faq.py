from core.faqs import register_faqs

register_faqs("combination", [
    {"q": "What is a combination?",
     "a": "A selection where order does not matter. Choosing 2 pizza toppings from 5 is a combination, because cheese-then-mushroom is the same pizza as mushroom-then-cheese."},
    {"q": "Why divide by r! compared with permutations?",
     "a": "Because every group of r items can be arranged in r! different orders, and combinations should count all those as one. Dividing the permutation count by r! removes the duplicate orderings."},
    {"q": "When do I use combinations versus permutations?",
     "a": "Ask yourself whether reordering the same items makes a different outcome. Lottery numbers, committee members and hands of cards are combinations; rankings, codes and finishing orders are permutations."},
    {"q": "What is nCr also called?",
     "a": "The binomial coefficient, often read as 'n choose r'. It is the same number that appears in Pascal's triangle and the binomial expansion."},
    {"q": "A quick real example?",
     "a": "Picking 6 lottery numbers from 45 is a combination because the draw order does not matter. The huge number of combinations is exactly why the jackpot is so hard to win."},
])
