# -*- coding: utf-8 -*-
from core.faqs import register_faqs

register_faqs("morphing-surface", [
    {"q": 'What is a surface in maths?', "a": "A shape where every point's height z is decided by two inputs x and y, written z = f(x, y) - like a landscape over a map grid."},
    {"q": 'Why does it move?', "a": 'A time term t is added to the formula, so the whole surface ripples - a simple way to picture waves and change.'},
    {"q": 'Who uses 3D surfaces?', "a": 'Architects and engineers model roofs and bridges; animators and game designers build worlds; scientists model terrain and weather.'},
    {"q": 'Is this the same as a graph?', "a": 'Yes - it is a graph with two inputs instead of one, so it needs a third dimension for the output.'},
    {"q": 'How does this lead to harder maths?', "a": 'It is the doorway to multivariable calculus, used everywhere from machine learning to fluid dynamics.'},
])
