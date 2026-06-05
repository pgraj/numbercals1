from core.faqs import register_faqs

register_faqs("discount", [
    {"q": "How is a discount worked out?",
     "a": "Multiply the original price by the discount percentage (as a decimal) to get the "
          "saving, then subtract it. A $200 item at 25% off saves $50, leaving $150 before any tax."},
    {"q": "Why is tax added after the discount?",
     "a": "Tax is normally charged on what you actually pay, not the pre-discount sticker price. "
          "So the order is: take the discount off first, then apply the tax to the reduced amount."},
    {"q": "What is the total savings figure?",
     "a": "It is the discount amount — the difference between the original price and the "
          "discounted price, before tax. It tells you how much the sale knocked off, separate "
          "from any tax that is then added back on."},
    {"q": "How do I read the waterfall chart?",
     "a": "Read it left to right. The first bar is the original price. The next step drops down "
          "by the savings. The following step nudges back up by the tax. The final bar lands on "
          "what you actually pay — so you can see exactly how the price was built up."},
    {"q": "Where is this used in real life?",
     "a": "Shopping — a $1,200 laptop at 15% off with 10% tax comes to $1,122. Sales planning — "
          "a retailer checking the takings after a storewide markdown. Budgeting — working out "
          "the true checkout total once both the sale and the tax are applied, so there are no surprises."},
])
