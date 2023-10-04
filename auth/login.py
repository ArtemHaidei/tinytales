from flask_smorest import Blueprint


LoginBlueprint = Blueprint('login', __name__, url_prefix='/login', description='Login operations')
