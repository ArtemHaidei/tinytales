from . import AuthBlueprint
from .views import sing_in, sign_up


AuthBlueprint.add_url_rule('/sign-in', 'sign-in', view_func=sing_in, methods=['GET', 'POST'])
AuthBlueprint.add_url_rule('/sign-up', 'sign-up', view_func=sign_up, methods=['GET', 'POST'])