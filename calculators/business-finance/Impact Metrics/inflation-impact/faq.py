from core.faqs import register_faqs

register_faqs("inflation-impact", [
    {"q": "What does inflation do to money?",
     "a": "It raises prices over time, which means the same amount of money buys less. This calculator shows both the higher future price and the shrunken real value of money you hold."},
    {"q": "What is purchasing power?",
     "a": "What your money can actually buy. If prices rise 6% a year, money sitting idle loses about 6% of its purchasing power each year even though the number on the note is unchanged."},
    {"q": "Why compound the rate?",
     "a": "Because inflation stacks year on year. 6% for ten years is not 60%; it is 1.06 to the power 10, which is about 79%, because each year's rise sits on top of the last."},
    {"q": "How do I protect against inflation?",
     "a": "Generally by holding assets that grow at least as fast as prices, rather than idle cash. The investment-return calculator lets you compare growth rates against the inflation rate."},
    {"q": "Is this the same as the real interest rate?",
     "a": "Related. The real return on savings is roughly the interest rate minus inflation. If your savings earn less than inflation, you are quietly losing ground."},
])
