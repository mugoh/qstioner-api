from flask_restful import Api
from flask import Blueprint

from app.v1.views.user import UsersRegistration, UserLogin, UserLogout
from app.v1.views.meetups import Meetups, MeetUp, MeetUpItem
from app.v1.views.questions import Question, Questions

auth_blueprint = Blueprint("auth", __name__, url_prefix='/api/v1/auth/')
app_blueprint = Blueprint("app", __name__, url_prefix='/api/v1/')

auth_api = Api(auth_blueprint)
app_api = Api(app_blueprint)

auth_api.add_resource(UsersRegistration, 'register')
auth_api.add_resource(UserLogin, 'login')
auth_api.add_resource(UserLogout, 'logout')

app_api.add_resource(Meetups, 'meetups')
app_api.add_resource(MeetUp, 'meetups/upcoming')
app_api.add_resource(MeetUpItem, 'meetups/<int:id>')
app_api.add_resource(Question, 'questions')
app_api.add_resource(Questions, 'questions/<int:id>')
