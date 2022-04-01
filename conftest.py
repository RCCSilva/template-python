import pytest

from app import create_app, db


@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture
def client(app):
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client
            db.session.rollback()
            db.session.remove()
