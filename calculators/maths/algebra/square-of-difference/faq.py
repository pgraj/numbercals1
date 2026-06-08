from core.faqs import register_faqs

register_faqs('square-of-difference', [
    {"q": 'Where is (a−b)² used in everyday life?',
     "a": 'It is the mental shortcut for squaring numbers just below a round one. 19² = (20−1)² = 400 − 40 + 1 = 361. 98² = (100−2)² = 10000 − 400 + 4 = 9604. The minus sign on the middle term is the only change from (a+b)². Builders and machinists use it when a square is trimmed down by a margin on two sides; the area lost is 2ab − b², which is why shaving a little off each side removes more than you might expect.'},
    {"q": 'Why is the middle term negative here but positive in (a+b)²?',
     "a": 'Because you are subtracting. Expanding (a−b)(a−b) gives a² − ab − ba + b² = a² − 2ab + b². The two cross-products are now negative, so they subtract. Geometrically, starting from an a×a square and cutting back to side (a−b), you remove two a×b strips (the −2ab) but you have double-counted the little corner b×b square, so you add it back - which is exactly the +b². Getting the sign of the middle term wrong is a classic exam slip.'},
    {"q": 'How is this used in statistics?',
     "a": "It is the heart of how 'spread' is measured. Variance and standard deviation are built from squared differences from the mean, (x − mean)². Every data point's deviation is squared using exactly this identity, which is why squaring is central to statistics: it makes all deviations positive and penalises large gaps more. The same (a−b)² shape underlies least-squares fitting, the method behind trend lines and most of machine learning's error measures."},
    {"q": 'Does (a−b)² appear in physics or engineering?',
     "a": 'Frequently. Kinetic-energy changes, error margins, and tolerance calculations all involve squared differences. When an engineer computes how far a measurement deviates from a target and squares it (to weight large errors more and ignore sign), that is (a−b)². Control systems and signal processing minimise squared error - the difference between desired and actual - using this exact expansion.'},
    {"q": 'How does it help with quick mental arithmetic?',
     "a": 'Any number near a round value squares fast: pick the nearest ten or hundred as a, the gap as b, and apply a² − 2ab + b². For 47²: nearest is 50, so (50−3)² = 2500 − 300 + 9 = 2209. The round square is easy, the cross term is a quick doubling, and the correction b² is small. Together with (a+b)², this lets you square almost any two-digit number mentally in seconds.'},
])
