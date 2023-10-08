import os

from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config.from_envvar('YOURAPPLICATION_SETTINGS')

    from .blueprints.main.error_handler import page_not_found
    app.register_error_handler(404, page_not_found)

    api = Api(app)

    from app.blueprints import (UsersBlueprint,
                                PostsBlueprint,
                                AuthBlueprint,
                                MainBlueprint)

    api.register_blueprint(MainBlueprint)
    api.register_blueprint(UsersBlueprint)
    api.register_blueprint(PostsBlueprint)
    api.register_blueprint(AuthBlueprint)

    login_manager.init_app(app)
    login_manager.login_view = 'auth.sign-in'

    db.init_app(app)
    Migrate(app, db)

    return app
