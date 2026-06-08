from core.faqs import register_faqs

register_faqs('exponential-search', [
    {"q": 'How is this like finding an old post by scrolling a feed?',
     "a": 'When you hunt for an old post, you do not scroll one screen at a time - you jump 1 screen, then 2, then 4, then 8, until you have clearly gone past it, then search back within that last window. Exponential search works identically: it doubles an index (1, 2, 4, 8...) until it overshoots the target, fixing a bounded range, then binary-searches inside it. Doubling reaches far-off items in just a few logarithmic leaps.'},
    {"q": 'What problem does exponential search solve that binary search cannot?',
     "a": 'Binary search needs both ends of the data up front - it starts by looking at the middle, which requires knowing the length. Exponential search does not. It discovers an upper bound by doubling an index until it overshoots the target, then binary-searches the bounded range. This makes it usable on unbounded or streamed sorted data - for example, a sorted sequence you are reading lazily and whose total size you do not yet know.'},
    {"q": 'Why double the bound instead of stepping linearly?',
     "a": 'Doubling reaches position p in only about log(p) steps, whereas stepping one at a time would take p steps. So if the target sits at index 1000, doubling finds a bounding range in about 10 jumps rather than 1000. The doubling phase is therefore logarithmic, matching the binary-search phase that follows, keeping the whole algorithm O(log n).'},
    {"q": 'Is exponential search faster than binary search on a normal array?',
     "a": 'On a fully known array, binary search is at least as fast and usually simpler. Exponential search shines in two situations: when the size is unknown or unbounded, and when the target is likely to be near the beginning. In the second case the doubling phase finds a tiny range almost immediately, so it can beat binary search which always starts from the global middle.'},
    {"q": "Why is exponential search sometimes called 'galloping' search?",
     "a": "Because the doubling phase 'gallops' ahead in ever-larger leaps, like a horse accelerating, until it overshoots. The name appears in real implementations - notably the merge step of Timsort (Python's and Java's sort), which uses galloping mode to skip quickly through long runs of one input. So the doubling idea is not just academic; it speeds up one of the most widely used sorting algorithms."},
    {"q": 'What if the array has unknown length and we read past the end?',
     "a": 'A careful implementation checks the bound against the data as it doubles and stops if it reaches the end, clamping the upper index to the last valid position. In a streamed setting you would detect end-of-data during doubling. The key is that the doubling never needs to know the exact size in advance - it only needs to detect when it has gone far enough or run out of data.'},
])
