from core.faqs import register_faqs

register_faqs("triangle-area", [
    {"q": "What are the two ways to find a triangle's area?",
     "a": "If you know the base and the perpendicular height, use half base times height. If you only know the three side lengths, use Heron's formula. Pick the method that matches your measurements."},
    {"q": "What is Heron's formula?",
     "a": "A way to get the area from the three sides alone. Find the semi-perimeter s (half of a + b + c), then the area is the square root of s(s-a)(s-b)(s-c). No height needed."},
    {"q": "What is the triangle inequality?",
     "a": "A rule that any two sides must add up to more than the third, otherwise the sides cannot close into a triangle. The calculator checks this and warns you if they fail."},
    {"q": "Why must the height be perpendicular?",
     "a": "Because half base times height assumes the height drops at a right angle to the base. Using a slanted side instead would overstate the area."},
    {"q": "Is the 3-4-5 triangle special?",
     "a": "Yes, it is a right triangle (since 3 squared plus 4 squared equals 5 squared) and its area is a tidy 6. It is the classic example for both Pythagoras and Heron's formula."},
])
