from flask_smorest import Blueprint

Auth = Blueprint('auth', __name__, url_prefix='/auth', description='Authentication and authorizations operations')

from . import routes
