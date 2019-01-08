from flask import Flask
from flask_jwt_extended import JWTManager

from app.v1 import auth_blueprint
from instance.config import APP_CONFIG


def create_app(config_setting):
    app = Flask(__name__)
    app.register_blueprint(auth_blueprint)

    jwt = JWTManager(app)

    app.config.from_object(
        APP_CONFIG[config_setting.strip().lower()])

    return app
