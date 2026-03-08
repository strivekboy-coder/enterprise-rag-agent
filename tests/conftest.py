import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parents[1]  # project root
sys.path.insert(0, str(ROOT))

from src.api.main import app  # noqa: E402


@pytest.fixture()
def client():
    return TestClient(app)
