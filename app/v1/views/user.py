"""
	This file conntains views for all the user endpoints
"""

from flask_restful import Resource


class UsersList(Resource):

    def post(self):
