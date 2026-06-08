from core.faqs import register_faqs

register_faqs('sentinel-linear-search', [
    {"q": 'How is this like putting a STOP sign at the end of a buffet?',
     "a": "Picture strolling a buffet line looking for dessert, having placed a 'STOP' sign at the very end. You check each dish as you go, but you never have to keep asking 'is this the last dish?' - the sign guarantees you will halt. The sentinel is that sign: a copy of your target placed past the real data, so the loop is certain to stop and can drop the end-of-list check from every single step."},
    {"q": 'What exactly does the sentinel save?',
     "a": "A plain linear search loop checks two things every iteration: 'have I found the target?' and 'have I run off the end of the array?'. The sentinel - a copy of the target placed just past the real data - guarantees the search always finds a match, so the second check becomes unnecessary. That removes one comparison per element. Over a long array that halves the comparison count in the loop body, a real if modest speedup."},
    {"q": 'If it is still O(n), why does the sentinel matter at all?',
     "a": 'Big-O hides constant factors, but constants matter in tight, frequently-run loops. The sentinel does not change the growth rate - double the data still doubles the work - but it can make each pass noticeably faster on real hardware. It is a classic example of a micro-optimization: useless asymptotically, valuable in a hot loop that runs billions of times.'},
    {"q": 'How do you tell a real match from the sentinel matching?',
     "a": "After the loop stops, you check the position. If the stopping index is within the original array bounds, it is a genuine match. If the loop ran all the way to the sentinel's position (just past the real data), then nothing in the actual list matched - the target is absent. So exactly one extra comparison at the very end replaces one comparison on every single step."},
    {"q": 'Does the sentinel technique work on linked lists or only arrays?',
     "a": 'It works best on arrays, where appending one cell is cheap and indices are simple. It can be adapted to a linked list by adding a sentinel node at the tail, which is also a common trick for simplifying insertion and deletion logic. But the speed benefit is clearest in arrays, where the removed bounds check was a real per-iteration cost.'},
    {"q": 'Is the sentinel approach used in real software?',
     "a": 'Yes, in performance-critical and low-level code. Sentinel nodes are widely used inside data-structure implementations (linked lists, trees) to remove special-case checks for empty or boundary conditions, which both speeds up and simplifies the code. The searching variant shown here is more of a teaching classic, but the underlying idea - add a guard element so the loop never needs a boundary test - appears throughout systems programming.'},
])
