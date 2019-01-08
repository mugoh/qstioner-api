"""
    This file conntains views for all the user endpoints
"""

from flask_restful import Resource, reqparse, inputs


class UsersList(Resource):

    def post(self):
        parser = reqparse.RequestParser(trim=True, bundle_errors=True)
        parser.add_argument('firstname', type=str)
        parser.add_argument('lastname', type=str)
        parser.add_argument('othername', type=str)
        parser.add_argument('email', type=inputs.regex(
            r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$"), required=True)
        parser.add_argument('phonenumber', type=int)
        parser.add_argument('username', type=str)
        parser.add_argument('isAdmin', type=bool, default=False)
        parser.add_argument('password', required=True)

        args = parser.parse_args(strict=True)
