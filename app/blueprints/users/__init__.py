from flask_smorest import Blueprint
from utils import validate_password
from .models import User
from .schemas import UserSchema


UsersBlueprint = Blueprint('users', __name__, url_prefix='/users', description='Users operations')

