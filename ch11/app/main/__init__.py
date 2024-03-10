from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from .config import config_env

db = SQLAlchemy()
ma = Marshmallow()


def create_app(env: str):
    app = Flask(__name__)
    app.config.from_object(config_env[env])

    try:
        db.init_app(app=app)
        ma.init_app(app=app)
    except:  # noqa: E722
        raise ("err_init_db")  # type: ignore

    return app
