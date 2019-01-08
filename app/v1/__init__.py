from flask_restful import Api
from flask import Blueprint

from app.v1.views.user import UsersRegistration, UserLogin

auth_blueprint = Blueprint("auth", __name__, url_prefix='/api/v1/auth/')

auth_api = Api(auth_blueprint)

auth_api.add_resource(UsersRegistration, 'register')
auth_api.add_resource(UserLogin, 'login')
