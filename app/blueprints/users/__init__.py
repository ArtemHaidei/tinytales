from flask_smorest import Blueprint

UsersBlueprint = Blueprint('users', __name__, url_prefix='/users', description='Users API')

from .models import User
