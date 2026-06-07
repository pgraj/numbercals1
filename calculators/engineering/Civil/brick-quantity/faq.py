from core.faqs import register_faqs

register_faqs("brick-quantity", [
    {"q": "How does it estimate brick numbers?",
     "a": "It divides the wall area by the area each brick covers including its mortar joint, then adds a wastage percentage. The result is rounded up to whole bricks."},
    {"q": "Why include the mortar joint?",
     "a": "Because each brick sits in a bed of mortar, so it effectively occupies a little more than its own face. Ignoring the joint would overestimate how many bricks you need."},
    {"q": "Is this for a single-skin or double wall?",
     "a": "The estimate is for a single skin (one brick thick). A double-skin or cavity wall roughly doubles the count, so multiply accordingly or check with your builder."},
    {"q": "Why add wastage?",
     "a": "Bricks get cut at corners and openings, and some arrive broken. A wastage allowance of around 5 percent keeps you from running out mid-job."},
    {"q": "Will the number be exact?",
     "a": "No, it is an estimate. Bond pattern, openings for doors and windows, and brick size all shift the real total, so order a little extra and confirm with your supplier."},
])
