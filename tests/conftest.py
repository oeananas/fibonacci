import pytest
from config import configure_app
from app import app


@pytest.fixture
def application():
    """ Create and configure a new app instance for each test. """

    configure_app(app)
    yield app


@pytest.fixture
def client(application):
    """ A test client for the app. """

    return app.test_client()
