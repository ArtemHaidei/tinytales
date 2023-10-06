from flask_smorest import Blueprint

PostsBlueprint = Blueprint('posts', __name__, url_prefix='/posts', description='Posts routes')

from .models import Post
from . import routes
