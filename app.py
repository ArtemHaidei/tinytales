from flask import Flask
from flask_smorest import Api
from auth.login import LoginBlueprint
from dotenv import dotenv_values


app = Flask(__name__)

env = dotenv_values('.env')


app.config['SECRET_KEY'] = env['SECRET_KEY']
app.config["SQLALCHEMY_DATABASE_URI"] = env['DATABASE']
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['API_TITLE'] = 'TinyTales REST API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.1.0'
app.config['OPENAPI_URL_PREFIX'] = '/api'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'


api = Api(app)

api.register_blueprint(LoginBlueprint)


if __name__ == "__main__":
    app.run(debug=bool(env['FLASK_DEBUG']))