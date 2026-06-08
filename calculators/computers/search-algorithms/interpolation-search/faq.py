from core.faqs import register_faqs

register_faqs('interpolation-search', [
    {"q": "Is this like flipping straight to the back for 'Zara' in a register?",
     "a": "That is the perfect picture. Looking up 'Zara' in a class register, you do not open to the middle - you flip near the back, because you know Z is late in the alphabet. Interpolation search does the same with numbers: it estimates where the target should be from its value, not blindly probing the middle. On evenly spread data this lands very close, which is why it can beat binary search; on clumpy data the guess is poor and it slows down."},
    {"q": "How does interpolation search 'guess' where the target is?",
     "a": 'It treats the values as if they rise in a straight line across the indices. If the low end holds 10 and the high end holds 100, and you want 30, then 30 is about a quarter of the way up the value range, so it probes about a quarter of the way along the indices. The formula pos = lo + (target - arr[lo]) * (hi - lo) / (arr[hi] - arr[lo]) is exactly that proportional estimate. Binary search ignores values and always guesses the middle; interpolation search uses the values to guess smarter.'},
    {"q": 'Why is it O(log log n) sometimes but O(n) other times?',
     "a": 'On uniformly distributed data the estimate is so good that each probe shrinks the range dramatically, giving the remarkable O(log log n) - for a million items, around four probes. But if the data is clustered or skewed, the linear estimate is badly wrong and the range shrinks by only one element at a time, collapsing to O(n) like a linear search. So the same algorithm is brilliant or terrible depending entirely on the distribution of values.'},
    {"q": 'When should I prefer interpolation search over binary search?',
     "a": "When you know your sorted data is roughly uniformly distributed - evenly spaced IDs, timestamps, phone numbers - and lookups are frequent enough that the extra speed matters. If the distribution is unknown or known to be skewed, binary search's guaranteed O(log n) is the safer choice because it never degrades to O(n). Many libraries default to binary search precisely because it has no bad cases."},
    {"q": 'What stops the formula from probing outside the array?',
     "a": 'Two guards. The loop only continues while the target lies between the values at the current ends (arr[lo] <= target <= arr[hi]), so a target outside the range exits immediately. And the computed position is clamped to the current [lo, hi] window so arithmetic quirks cannot send the probe out of bounds. Together these prevent the index errors that a naive implementation of the formula can suffer.'},
    {"q": 'Is interpolation search related to how humans use a dictionary?',
     "a": "Very much so - it is arguably the most 'human' search. Nobody opens a dictionary in the exact middle to find 'Wilson'; they open near the back because W is late in the alphabet. That is interpolation: using the value (the letter W) to estimate the position. Binary search, by contrast, would stubbornly open the middle every time. Interpolation search formalises the intuitive shortcut people already use."},
])
