from dotenv import dotenv_values


env = dotenv_values

DEBUG = bool(env['FLASK_DEBUG'])

SECRET_KEY = env['SECRET_KEY']
SQLALCHEMY_DATABASE_URI = env['DATABASE']
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
API_TITLE = 'TinyTales REST API'
API_VERSION = 'v1'
OPENAPI_VERSION = '3.1.0'
OPENAPI_URL_PREFIX = '/api'
OPENAPI_SWAGGER_UI_PATH = '/swagger-ui'
OPENAPI_SWAGGER_UI_URL = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
