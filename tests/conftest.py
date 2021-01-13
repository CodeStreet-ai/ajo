import pytest
from fastapi.testclient import TestClient

from ajo.main import app


@pytest.fixture(scope="module")
def test_main():
    client = TestClient(app)
    yield client
