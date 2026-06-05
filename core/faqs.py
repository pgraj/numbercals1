"""Plug-and-play FAQ store. A faq.py drops its Q&A here on import.

Each calculator folder may contain a faq.py alongside calc.py:

    from core.faqs import register_faqs
    register_faqs("logarithm", [{"q": "...", "a": "..."}])

calc.py loads its sibling with ONE line at the bottom:

    from core.faqs import load_sibling_faq
    load_sibling_faq(__file__)

This works under the registry's file-based loader (which gives calc.py no
package context, so a plain `from . import faq` would silently fail).
No registry edits, no central list — drop the folder in and both load.

In your page route, pass the FAQs to the calc template, e.g.:

    from core import faqs
    ctx = _ctx(calc=calc, viz_template=..., faqs=faqs.faqs_for(calc.slug))
"""
import importlib.util
import pathlib

FAQS: dict[str, list[dict]] = {}   # slug -> [{"q":..., "a":...}, ...]


def register_faqs(slug: str, faqs: list[dict]) -> None:
    FAQS[slug] = faqs


def faqs_for(slug: str) -> list[dict]:
    return FAQS.get(slug, [])


def load_sibling_faq(calc_file: str) -> None:
    """Import faq.py sitting next to the given calc.py path, if present."""
    faq_path = pathlib.Path(calc_file).parent / "faq.py"
    if not faq_path.exists():
        return
    spec = importlib.util.spec_from_file_location(
        f"_ncfaq_{faq_path.parent.name}", faq_path)
    if spec and spec.loader:
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
