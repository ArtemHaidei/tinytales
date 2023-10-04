from flask_smorest import Blueprint

Posts = Blueprint('posts', __name__, url_prefix='/posts', description='Posts operations')

from . import routes
