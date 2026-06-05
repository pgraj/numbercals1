from core.faqs import register_faqs

register_faqs("rw-plane-altitude", [
    {"q": "How can an angle on the ground give a plane's altitude?",
     "a": 'If you know the horizontal ground distance to the point beneath the aircraft and measure the angle of elevation, the altitude is that distance times the tangent of the angle — the plane sits at the top of a right triangle.'},
    {"q": 'What is the difference between altitude and slant range?',
     "a": 'Altitude is the vertical height of the aircraft. Slant range is the straight-line distance from the observer to the plane — the hypotenuse — which a radar actually measures. Cosine links the ground distance to the slant range.'},
    {"q": 'Do air-traffic controllers really use trigonometry?',
     "a": 'The underlying radar and tracking systems do it automatically, but the geometry is exactly this: angles and distances are continuously turned into positions, heights and ranges. The maths is the same as this worked example.'},
    {"q": 'Why use the angle of elevation rather than just radar height?',
     "a": 'Radar gives slant range and bearing; trigonometry converts those into the separate altitude and ground-distance figures controllers and pilots need. Each ratio (sine, cosine, tangent) extracts a different part of the same triangle.'},
    {"q": 'Where is this used in real life?',
     "a": 'Air-traffic control, military radar, missile and drone tracking, and even amateur rocketry all turn a measured angle and a known distance into height and range. Surveyors and ballooning teams use the identical triangle.'},
])
