"""
    This module containes all Question resources.Question.
"""
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from app.v1.models.questions import QuestionModel


class Questions(Resource):
    """
        A resource that allows a suser to create a
        new questions and perform requests on existing
        multiple questions.
    """
    decorators = [jwt_required]

    def post(self):
        parser = reqparse.RequestParser(trim=True, bundle_errors=True)

        parser.add_argument('title', type=str, required=True)
        parser.add_argument('body', type=str, required=True)

        args = parser.parse_args(strict=True)
