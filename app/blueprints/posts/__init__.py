from flask_smorest import Blueprint
from .models import Post

PostsBlueprint = Blueprint('posts', __name__, url_prefix='/posts', description='Posts Operations')

from . import routes
