import os

from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from app.blueprints import UsersBlueprint, PostsBlueprint, AuthBlueprint
from flask_migrate import Migrate
from dotenv import dotenv_values


env = dotenv_values()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

app = Flask(__name__)

app.config.from_envvar('YOURAPPLICATION_SETTINGS')

api = Api(app)

api.register_blueprint(UsersBlueprint)
api.register_blueprint(PostsBlueprint)
api.register_blueprint(AuthBlueprint)

db.init_app(app)
Migrate(app, db)
