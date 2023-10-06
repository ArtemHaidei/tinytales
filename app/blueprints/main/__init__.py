from flask_smorest import Blueprint

MainBlueprint = Blueprint(
    'main',
    __name__,
    url_prefix='/',
    description='Main routes'
)

from . import routes
