from core.faqs import register_faqs

register_faqs('fibonacci-search', [
    {"q": 'Why would I search using only additions, like a broken calculator?',
     "a": 'Picture the number-guessing game, but your calculator cannot divide - so you decide where to guess using only additions, via Fibonacci steps. Fibonacci search does this: it chooses probe positions using Fibonacci numbers, needing only addition and subtraction, never the division that binary search uses for its midpoint. On old or simple hardware where division was far slower than addition, that made it genuinely faster, even though it makes a similar number of probes.'},
    {"q": 'Why would anyone avoid division in a search algorithm?',
     "a": 'On some hardware - early computers, small embedded chips, certain digital signal processors - division is dramatically slower than addition and subtraction, sometimes by an order of magnitude. Binary search needs to compute a midpoint, which is a division (or a shift). Fibonacci search replaces that with Fibonacci-number arithmetic using only adds and subtracts. On a platform where division is expensive, that can make Fibonacci search genuinely faster despite doing a similar number of probes.'},
    {"q": 'How do Fibonacci numbers decide where to probe?',
     "a": 'The algorithm keeps three consecutive Fibonacci numbers and uses them to place the probe so that the range is split in the golden ratio rather than exactly in half. On a mismatch it shifts to the previous Fibonacci numbers - again just additions and subtractions - which naturally shrinks the window to the correct sub-range. The exponential growth of the Fibonacci sequence is what keeps the number of probes logarithmic.'},
    {"q": 'Is Fibonacci search faster than binary search?',
     "a": 'In comparison count they are very close - both logarithmic. Fibonacci search is not about fewer comparisons; it is about cheaper arithmetic (no division) and a probing pattern that can be friendlier to certain memory systems, because it tends to examine elements at uneven but predictable gaps. On a modern CPU where division is fast, binary search is usually simpler and just as quick, so Fibonacci search is mostly of historical and educational interest now.'},
    {"q": 'What does Fibonacci search have to do with the golden ratio?',
     "a": "Consecutive Fibonacci numbers approximate the golden ratio (about 1.618) as they grow. Splitting a range by that ratio, rather than in half, is the same principle behind 'golden section search' used in optimization. So Fibonacci search is the discrete, integer-arithmetic cousin of golden section search - both exploit the golden ratio's self-similar splitting property to narrow a range efficiently."},
    {"q": 'Does Fibonacci search need the data sorted?',
     "a": 'Yes, exactly like binary search. The decision to move the window up or down on each probe relies on the sorted order: if the probed value is too small, the target must be further along, and vice versa. Without sorted data those decisions would be meaningless. The Fibonacci machinery only changes how the probe position is chosen, not the underlying requirement for sorted input.'},
])
