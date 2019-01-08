from flask_restful import Api
from flask import Blueprint

from views.user import UsersList

auth_blueprint = Blueprint('auth', __name__, url_prefix='/api/v1/auth/')

auth_api = Api(auth_blueprint)

auth_api.add_resource(UsersList, '/register')
