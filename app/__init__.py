from flask import Flask
from flask_cors import CORS
from flasgger import Swagger

from app.api.v1 import auth_blueprint, app_blueprint
from instance.config import APP_CONFIG


def create_app(config_setting):
    app = Flask(__name__)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(app_blueprint)

    app.config.from_object(
        APP_CONFIG[config_setting.strip().lower()])

    CORS(app)

    template = {
        "swagger": "3.0",
        "info": {
            "title": "Questioner API",
            "description": "API for the Questioner \
            Application with data structures for persistence",
            "version": "1.0"
        }
    }

    Swagger(app, template=template)

    return app
