from flask import Flask
from flask_jwt_extended import JWTManager

from app.v1 import auth_blueprint, app_blueprint
from app.v1.views.user import blacklisted_tokens
from instance.config import APP_CONFIG


def create_app(config_setting):
    app = Flask(__name__)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(app_blueprint)

    jwt = JWTManager(app)

    app.config.from_object(
        APP_CONFIG[config_setting.strip().lower()])

    @jwt.token_in_blacklist_loader
    def check_blacklisted_token(token):
        jti = token['jti']
        return jti in blacklisted_tokens

    return app
