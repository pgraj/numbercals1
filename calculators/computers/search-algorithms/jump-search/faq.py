from core.faqs import register_faqs

register_faqs('jump-search', [
    {"q": 'How is jump search like flipping through a textbook?',
     "a": 'Imagine finding a page by flipping 20 pages at a time. You leap forward in fixed jumps until you overshoot your page, then flip back and read that small range one page at a time. Jump search does exactly this on sorted data: it strides forward in blocks of about sqrt(n), and once it passes the target, it linearly scans just the last block. The block size sqrt(n) balances the jumping against the final scan.'},
    {"q": 'Why is the block size the square root of n?',
     "a": 'It is the size that minimises the total work. With block size k, jump search makes about n/k jumps and then up to k steps inside the final block, so total work is roughly n/k + k. Calculus (or trial and error) shows this sum is smallest when k equals the square root of n - the two costs are balanced. That is why jump search is O(sqrt n): a million items take about a thousand jumps plus a thousand steps.'},
    {"q": 'When is jump search better than binary search?',
     "a": "Almost never on speed - binary search's O(log n) beats O(sqrt n). Jump search wins when jumping backward is expensive. Binary search bounces left and right across the data; jump search mostly moves forward in steady strides, then scans forward. On magnetic tape, some disk layouts, or linked structures where forward access is cheap but random backward seeks are slow, that access pattern can make jump search the practical winner."},
    {"q": 'Does jump search need sorted data like binary search?',
     "a": "Yes. The whole method relies on the guarantee that if a block's last element is still smaller than the target, the target cannot be anywhere earlier - that only holds for sorted data. On unsorted data the jumps would skip over the target with no way to know, so you would fall back to linear search."},
    {"q": 'What happens if the target is larger than everything in the list?',
     "a": "The jump phase keeps advancing blocks until 'prev' runs past the end of the array, at which point the algorithm reports the target as absent without ever scanning - it never found a block whose end reached the target. This early exit is part of why jump search avoids scanning the whole list even for absent targets near the top end."},
    {"q": 'Can the block size be tuned away from sqrt(n)?',
     "a": 'Yes, and sometimes it should be. If comparisons inside a block are far cheaper or more expensive than a jump, the optimal block size shifts. Larger blocks mean fewer jumps but longer scans; smaller blocks mean more jumps but shorter scans. sqrt(n) is the theoretical sweet spot when jumps and comparisons cost the same, but real systems sometimes pick a block size matched to a disk page or cache line.'},
])
