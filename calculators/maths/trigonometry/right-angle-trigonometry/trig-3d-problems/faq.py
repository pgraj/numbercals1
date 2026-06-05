from core.faqs import register_faqs

register_faqs("trig-3d-problems", [
    {"q": "How do I solve a 3D trigonometry problem?",
     "a": "Break it into right-angled triangles you can see flat. For a cuboid, "
          "first find the base diagonal with Pythagoras, then use that diagonal "
          "and the height to find the space diagonal, then the angle to the base."},
    {"q": "What is the space diagonal of a cuboid?",
     "a": "It is the longest straight line inside the box, from one corner to the "
          "opposite corner. Its length is √(length² + width² + height²)."},
    {"q": "Can you give a worked example?",
     "a": "For a box 3 by 4 by 12, the base diagonal is √(3² + 4²) = 5, the space "
          "diagonal is √(5² + 12²) = 13, and the angle it makes with the base is "
          "tan⁻¹(12 ÷ 5) ≈ 67.4°."},
    {"q": "Why does the work split into two triangles?",
     "a": "A 3D line cannot be solved in one step, but it can be seen as the "
          "hypotenuse of an upright right triangle whose base is a diagonal lying "
          "flat — so two ordinary 2D steps solve it."},
    {"q": "Where is this used in real life?",
     "a": "Architects and structural engineers size diagonal braces and roof "
          "members, packaging designers check whether items fit in boxes, pilots "
          "and air-traffic controllers reason about 3D paths, and 3D modellers "
          "and game developers compute spatial distances."},
])
