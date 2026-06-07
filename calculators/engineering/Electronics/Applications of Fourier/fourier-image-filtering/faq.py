from core.faqs import register_faqs

register_faqs("fourier-image-filtering", [
    {"q": "How is filtering an image related to Fourier?", "a": "An image is just intensity values, and its Fourier transform sorts those into smooth, slowly-varying parts (low frequencies) and sharp edges and texture (high frequencies). Keep the low ones and you blur; keep the high ones and you find edges. This page shows the idea on a single row of pixels."},
    {"q": "What is a low-pass filter good for?", "a": "Smoothing and blurring — removing noise, softening skin in portraits, or creating depth-of-field effects. It keeps the broad shapes and discards fine detail. Slide the cutoff down here and watch the row lose its sharp steps and ripples."},
    {"q": "What does a high-pass filter do?", "a": "It keeps the rapid changes and throws away the smooth background, which is exactly how edge detection works. Sharpening filters, the outline-finding step in computer vision, and medical-image enhancement all lean on high-pass filtering. Watch the edges pop out in the high-pass plot."},
    {"q": "Is this how Instagram filters and photo apps work?", "a": "Many effects are built from these blocks: blur, sharpen, and 'clarity' or 'structure' sliders are low- and high-pass operations under the hood. Real photo apps work in 2D and use fast algorithms, but the frequency-domain intuition is identical to this 1D slice."},
    {"q": "Why only a 1D pixel row instead of a full image?", "a": "A real image needs a 2D Fourier transform, which is harder to draw and grasp at a glance. Taking a single horizontal line keeps the maths visible — you can watch every value change — while teaching the exact same lesson that scales up to full pictures."},
])
