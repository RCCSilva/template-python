from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.infrastructure.register_bluprints import register_blueprints
from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    register_blueprints(app)

    return app
