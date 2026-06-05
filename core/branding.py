"""
Site-wide branding & version constants.

Single place for the version badge (top-right of every page) and the
one-line disclaimer that runs at the bottom of every page.
"""

SITE_NAME = "NumberCals"
SITE_URL = "https://numbercals.com"
TAGLINE = "From Aryabhata to Algorithms — Calculators for the Curious"

# Shown top-right on every page, per the design spec.
SKIN_VERSION = "v0.6.0"        # frontend / UI skin
BACKEND_VERSION = "v0.3.0"     # FastAPI backend

# One-line disclaimer, bottom of every page.
DISCLAIMER = (
    "Learning tool only — verify results independently before relying on them "
    "for academic, financial, or professional decisions."
)

CONTACT_EMAIL = "hello@numbercals.com"

# Ad monetisation. Leave ADSENSE_CLIENT empty until approved; the ad slot
# renders nothing while empty, so the skin is never broken by a raw ad box.
# When ready, set e.g. ADSENSE_CLIENT = "ca-pub-XXXXXXXXXXXXXXXX".
ADSENSE_CLIENT = ""
AD_SLOT = ""


def context() -> dict:
    """Common template context injected into every page."""
    import datetime
    return {
        "site_name": SITE_NAME,
        "site_url": SITE_URL,
        "tagline": TAGLINE,
        "skin_version": SKIN_VERSION,
        "backend_version": BACKEND_VERSION,
        "disclaimer": DISCLAIMER,
        "contact_email": CONTACT_EMAIL,
        "adsense_client": ADSENSE_CLIENT,
        "ad_slot": AD_SLOT,
        "current_year": datetime.datetime.now().year,
    }
