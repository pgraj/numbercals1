"""
Shared pytest fixtures for NumberCals.

Both test_framework.py (write-once) and test_calculators.py (append-only)
use the `client` fixture from here, so they boot the app the same way.
You never need to re-send these files — keep them on disk.
"""
import importlib
import pathlib
import sys

import pytest
from fastapi.testclient import TestClient

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


@pytest.fixture()
def client():
    """Fresh import so load_all() re-scans the folder tree each test session."""
    import main
    importlib.reload(main)
    return TestClient(main.app)


@pytest.fixture()
def reg(client):
    """Convenience access to the live registry after boot."""
    from core import registry
    return registry
