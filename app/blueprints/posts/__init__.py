from flask_smorest import Blueprint
from .models import Post
from .schemas import PostSchema

PostsBlueprint = Blueprint('posts', __name__, url_prefix='/posts', description='Posts operations')

from . import routes
