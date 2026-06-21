import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from api.main import app
from api.storage import clear_storage
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    """Тестовый клиент FastAPI-приложения."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def clean_storage():
    """
    Очищает хранилище перед и после каждого теста.
    autouse=True — применяется автоматически ко всем тестам,
    параметр явно указывать не нужно.
    """
    clear_storage()
    yield
    clear_storage()
