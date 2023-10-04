import os

from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('config.config.py')

    api = Api(app)

    from app.blueprints.auth import Auth
    api.register_blueprint(Auth)

    from app.blueprints.posts import Posts
    api.register_blueprint(Posts)

    from app.blueprints.users import Users
    api.register_blueprint(Users)

    db.init_app(app)

    return app
