from flask_smorest import Blueprint

AuthBlueprint = Blueprint('auth', __name__, url_prefix='/auth', description='Authentication')

from . import routes
