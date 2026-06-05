from core.faqs import register_faqs

register_faqs("convert-data", [
    {"q": "What does the Data Storage Converter do?",
     "a": "It converts convert digital data and bandwidth across binary (kib/mib/gib) and decimal (kb/mb/gb) prefixes via the bit by first normalising your value to the SI base unit "
          "(bit) and then scaling to your chosen target unit. This hub-and-spoke "
          "approach guarantees every unit pair is internally consistent."},
    {"q": "Can you show a worked example?",
     "a": "1 GB to Mbit: 1 × 8e9 = 8e9 bit, then ÷ 1e6 = 8000 Mbit."},
    {"q": 'Why does my 1 TB drive show as about 931 GB?',
     "a": 'Drive makers use decimal units (1 TB = 1,000,000,000,000 bytes) while many operating systems display binary units (1 TiB = 1024⁴ bytes ≈ 1.1 trillion bytes). Same bytes, different prefix — so the binary figure looks smaller. Also remember network speeds are in bits, not bytes: divide Mbps by 8 for MB/s.'},
    {"q": "Where is this used in real life?",
     "a": "Storage sizing, network bandwidth planning and distinguishing KiB from KB."},
    {"q": "What are the limits or edge cases?",
     "a": "Conversions are exact ratios where the units are defined exactly (most SI and "
          "imperial units) and best-available constants otherwise. Extremely large or small "
          "magnitudes are shown in general (g) format; round-tripping through the base unit "
          "may introduce tiny floating-point differences in the final decimal places."},
])
