from core.faqs import register_faqs

register_faqs("rw-ocean-depth", [
    {"q": 'How does sonar measure depth with an angle?',
     "a": 'A sonar beam sent at a known angle below the horizontal returns a slant distance. The depth straight down is that slant range times the sine of the beam angle, while the cosine gives how far ahead the seabed point lies.'},
    {"q": 'Why not just point the beam straight down?',
     "a": 'Straight-down (single-beam) sounders do exist, but angled and fan-shaped (multibeam) sonar map a wide swath of seabed in one pass, locate features ahead of the vessel, and find slopes and reefs a vertical beam would miss.'},
    {"q": 'How is the slant range itself found?',
     "a": 'Sonar measures the time for the ping to travel out and echo back, then multiplies half that time by the speed of sound in water (about 1500 m/s). That gives the slant distance the trigonometry then resolves into depth.'},
    {"q": 'What affects the accuracy?',
     "a": "The speed of sound varies with water temperature, salinity and pressure, so surveys calibrate for local conditions. The beam angle and the vessel's motion must also be tracked precisely for accurate depth and position."},
    {"q": 'Where is this used in real life?',
     "a": 'Marine biologists map seabed habitats and locate reefs and fish shoals, hydrographers chart safe shipping channels, and offshore engineers survey sites for cables and platforms — all using the angled-beam depth triangle.'},
])
