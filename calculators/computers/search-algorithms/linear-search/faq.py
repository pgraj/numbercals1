from core.faqs import register_faqs

register_faqs('linear-search', [
    {"q": "Is linear search really how I'd find a friend's name in movie credits?",
     "a": 'Exactly that. Movie credits scroll in no order you can exploit, so you have no choice but to read every name from top to bottom until you spot the one you want. That is linear search: no shortcuts, just check each item in turn. It is why the method works on any list, sorted or not - and also why it feels slow for long credits, because in the worst case you read all the way to the end.'},
    {"q": 'Why use linear search when binary search is so much faster?',
     "a": 'Because linear search has zero prerequisites. Binary search only works on sorted data, and sorting costs time and effort up front. If your list is unsorted, tiny, or you only need to search it once, linear search is simpler and often just as fast in practice - you would spend more time sorting than you would ever save. It also works on data structures where you cannot jump to the middle, like a singly linked list or a data stream you read once.'},
    {"q": 'What is the average number of comparisons linear search makes?',
     "a": 'If the target is present and equally likely to be at any position, linear search checks about n/2 items on average - half the list. If the target is absent it always checks all n. This is why its time complexity is written O(n): the work grows in direct proportion to the number of items, with no shortcut.'},
    {"q": 'Does the order of items affect linear search?',
     "a": "It does not affect correctness - linear search finds the target wherever it is - but it affects speed for a given search. If frequently-searched items sit near the front, average searches finish sooner. Some systems exploit this with a 'move to front' trick: each time an item is found, move it to the start, so popular items drift forward and are found faster over time."},
    {"q": "How is linear search related to filtering or 'find' in programming?",
     "a": "Almost every language's built-in find, indexOf, includes, or filter on an unsorted collection is a linear search underneath. When you call array.find(x => x.id === 42) in JavaScript or use the 'in' operator on a Python list, the runtime walks the elements one by one. Knowing this helps you reason about why such operations slow down on very large lists."},
    {"q": 'Can linear search be made faster without sorting?',
     "a": "Only modestly. Tricks like the sentinel version remove one comparison per step, and checking two elements per loop iteration ('loop unrolling') can help slightly. But these are constant-factor improvements - the fundamental O(n) growth stays the same. To beat O(n) you must change the data structure: sort it (binary search), index it (hash table), or organise it as a tree."},
])
