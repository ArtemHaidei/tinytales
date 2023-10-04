from flask_smorest import Blueprint

Users = Blueprint('users', __name__, url_prefix='/users', description='Users operations')

from . import routes
