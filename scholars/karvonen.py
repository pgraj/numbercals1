"""Scholar: Martti Karvonen, behind the heart-rate-reserve method used by the HR-zone calculator."""
from core.registry import register_scholar

register_scholar(
    slug="karvonen",
    name="Martti Karvonen",
    era="1918–2009",
    field_of="Exercise physiology",
    blurb="Martti J. Karvonen was a Finnish physiologist whose work on exercise intensity gave rise "
          "to the heart-rate-reserve method. Rather than working from maximum heart rate alone, it "
          "uses the gap between maximum and resting heart rate, so training zones reflect individual "
          "fitness. The approach is now a staple of cardio training and the heart-rate features on "
          "modern fitness watches.",
    source_name="Wikipedia — Heart rate",
    source_url="https://en.wikipedia.org/wiki/Heart_rate",
)
