import pytest

from app import create_app, db


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            db.create_all()

            yield client
            db.session.rollback()
            db.session.remove()
