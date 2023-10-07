from . import PostsBlueprint
from .views import posts, blog, post_create


# --------------- POSTS ---------------
PostsBlueprint.add_url_rule("/posts", "posts", posts, methods=["GET"])


# --------------- BLOG ---------------
PostsBlueprint.add_url_rule("/blog", "blog", blog, methods=["GET"])
PostsBlueprint.add_url_rule("/blog/create", "post-create", post_create, methods=["GET", "POST"])