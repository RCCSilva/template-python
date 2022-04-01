import pytest

from app import create_app, db


@pytest.fixture
def client():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    with app.test_client() as client:
        with app.app_context():
            db.create_all()

            yield client
            db.session.rollback()
            db.session.remove()
