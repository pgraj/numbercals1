from core.faqs import register_faqs

register_faqs("trig-inverse-functions", [
    {"q": 'What are inverse trig functions?',
     "a": 'arcsin, arccos and arctan run the trig functions backwards: given a ratio they return the angle that produces it. For example arcsin(0.5) = 30° because sin 30° = 0.5.'},
    {"q": 'Why do they have restricted ranges?',
     "a": 'Because sin, cos and tan repeat, an inverse would otherwise have infinitely many answers. Each is given one principal range: arcsin and arctan return [−90°, 90°], arccos returns [0°, 180°].'},
    {"q": 'Can you show a worked example?',
     "a": 'arccos(0.5): the angle in [0°,180°] whose cosine is 0.5 is 60°. In radians that is π/3 ≈ 1.0472 rad; switch the toggle and the answer is shown in radians.'},
    {"q": 'What inputs are allowed?',
     "a": 'arcsin and arccos only accept values from −1 to 1, since sine and cosine never exceed that range. arctan accepts any real number.'},
    {"q": 'Where are they used?',
     "a": 'Finding an angle from a ratio in navigation, working out a launch or view angle, and defining the principal branches used throughout calculus.'},
])
