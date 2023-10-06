from .views import home, about
from . import MainBlueprint


MainBlueprint.add_url_rule("/", "home", home, methods=["GET"])
MainBlueprint.add_url_rule("/about", "about", about, methods=["GET"])
