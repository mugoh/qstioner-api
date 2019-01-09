from flask_restful import Api
from flask import Blueprint

from app.v1.views.user import UsersRegistration, UserLogin, UserLogout
from app.v1.views.meetups import Meetups

auth_blueprint = Blueprint("auth", __name__, url_prefix='/api/v1/auth/')
app_blueprint = Blueprint("app", __name__, url_prefix='/api/v1/')

auth_api = Api(auth_blueprint)
app_api = Api(app_blueprint)

auth_api.add_resource(UsersRegistration, 'register')
auth_api.add_resource(UserLogin, 'login')
auth_api.add_resource(UserLogout, 'logout')

app_api.add_resource(Meetups, 'meetups')
