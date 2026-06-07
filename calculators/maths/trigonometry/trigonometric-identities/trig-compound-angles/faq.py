from core.faqs import register_faqs

register_faqs("trig-compound-angles", [
    {"q": 'What are the compound-angle formulae?',
     "a": 'They expand the sine, cosine or tangent of a sum or difference of two angles: sin(A±B)=sinA cosB ± cosA sinB, cos(A±B)=cosA cosB ∓ sinA sinB, and tan(A±B)=(tanA±tanB)/(1∓tanA tanB).'},
    {"q": 'Can you show a worked example?',
     "a": 'sin 75° = sin(45°+30°) = sin45 cos30 + cos45 sin30 ≈ 0.9659. In radians the same angle is 75° = 5π/12 ≈ 1.3090 rad; switch the toggle and the working re-derives.'},
    {"q": 'Why does cosine flip the sign?',
     "a": 'Because cos(A+B) loses a sin·sin term with a minus, while cos(A−B) gains it with a plus. So cos(A+B) uses − between the terms and cos(A−B) uses +, the opposite of sine.'},
    {"q": 'When is tan(A±B) undefined?',
     "a": 'When the denominator 1∓tanA tanB is zero, or when any of A, B or A±B is an odd multiple of 90° (π/2 rad), where the tangent itself does not exist.'},
    {"q": 'Where are they used?',
     "a": 'They underpin every later identity and are used to combine waves of the same frequency, in AC circuit analysis, and in rotation formulae for graphics.'},
])
