from flask_smorest import Blueprint


PostsBlueprint = Blueprint('posts', __name__, url_prefix='/posts', description='Posts operations')
