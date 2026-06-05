from core.faqs import register_faqs

register_faqs("rw-tree-height", [
    {"q": "How do you measure a tree's height without climbing it?",
     "a": 'Stand a measured distance away, use a clinometer or phone app to read the angle of elevation to the top, then multiply the distance by the tangent of that angle and add your eye height. No ladder required.'},
    {"q": 'Why do you add the eye height at the end?',
     "a": 'The right triangle only reaches from the level of your measuring instrument up to the treetop, so it gives the height above eye level. Adding your eye (instrument) height converts that into the height above the ground.'},
    {"q": 'What if the ground is sloped?',
     "a": 'On a slope you measure the horizontal distance and account for any height difference between you and the tree base. A common approach is to take two angle readings, or measure to the base as well as the top, and combine them.'},
    {"q": 'How accurate is this method?',
     "a": 'It is accurate to within a few percent if the distance and angle are measured carefully. The biggest errors come from an imprecise angle reading or from not standing on level ground with the tree base.'},
    {"q": 'Where is this used in real life?',
     "a": 'Foresters estimate timber volume and tree health, arborists assess whether a tree could reach a building if it fell, surveyors record landmark heights, and the very same technique scales up to measuring towers, cliffs and mountains.'},
])
