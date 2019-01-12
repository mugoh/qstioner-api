from flask import Flask

from app.api.v1 import auth_blueprint, app_blueprint
from instance.config import APP_CONFIG


def create_app(config_setting):
    app = Flask(__name__)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(app_blueprint)

    app.config.from_object(
        APP_CONFIG[config_setting.strip().lower()])

    return app
