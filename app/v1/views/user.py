"""
    This file conntains views for all the user endpoints
"""

from flask_restful import Resource, reqparse, inputs
import random

from app.v1.models.users import UserModel
from app.v1.utils import verify_pass


class UsersRegistration(Resource):
    """
        This resource allows a user to create a new account.
    """

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
        parser.add_argument('password', required=True, type=verify_pass)

        args = parser.parse_args(strict=True)

        if UserModel.get_by_email(args['email']):
            return {
                "Status": 409,
                "Message": "Account exists. Maybe log in?"
            }, 409

        if UserModel.get_by_name(args['name']):
            return {
                "Status": 409,
                f"Message": "Oopsy! username exists.Try {random.randint(0, 40)}"
            }

        user = UserModel(**args).save()

        return {
            "Status": 201,
            "Data": user.dictify()
        }

        def get(self):
            return {
                "Status": 200,
                "Data": UserModel.get_all_users()
            }
