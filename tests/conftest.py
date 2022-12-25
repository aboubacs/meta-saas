import pytest

from src.infrastructure.app import init


@pytest.fixture
def test_app():
    app, _ = init()
    return app
