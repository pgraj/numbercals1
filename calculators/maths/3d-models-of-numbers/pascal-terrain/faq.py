# -*- coding: utf-8 -*-
from core.faqs import register_faqs

register_faqs("pascal-terrain", [
    {"q": "What is Pascal's triangle?", "a": 'A triangle of numbers where each entry is the sum of the two directly above it, starting from a single 1 at the top.'},
    {"q": 'What do the rows mean?', "a": 'Row n gives the coefficients of (a + b)^n, and also the chances of getting 0, 1, 2... heads when you flip n coins.'},
    {"q": 'Why is the height log10?', "a": 'The middle numbers grow huge quickly, so plotting their number of digits keeps the terrain readable.'},
    {"q": 'How does it connect to probability?', "a": "Each entry is 'n choose k', the number of ways to pick k items from n - the heart of probability and statistics."},
    {"q": 'Who really discovered Pascal\'s triangle?', "a": (
        "It was found independently across many cultures, long before Pascal. In "
        "India, Pingala (c. 3rd-2nd century BCE) studied the combinatorics in his "
        "work on poetic metre, and the explicit triangle - the Meru-prastara, or "
        "'staircase of Mount Meru' - was set out by the commentator Halayudha "
        "(10th century CE). In Persia, al-Karaji (c. 1000 CE) and Omar Khayyam "
        "(1048-1131) described it independently. In China, Jia Xian (11th century) "
        "devised it and Yang Hui (13th century) preserved it, so it is known there "
        "as 'Yang Hui's triangle'. Blaise Pascal (France, 1654) tied it to "
        "probability theory, which is why the West named it after him. You can read "
        "about each of them in the Scientists & Scholars directory.")},
])
