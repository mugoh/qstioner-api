"""
    This module contains resource views for the
    rsvp Resource
"""

from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from app.v1.models.rsvp import RsvpModel
from ..models.meetups import MeetUpModel


class Rsvps(Resource):

    def post(self, id):
        """
            Creates an rsvp with refrence to a meetup and the
            existing user's
        """
        parser = reqparse.RequestParser(trim=True, bundle_errors=True)

        parser.add_argument('response', type=str, required=True)
        parser.add_argument('meetup', type=int, default=1)

        args = parser.parse_args(strict=True)

        # Confirm existence of meetup

        if not MeetUpModel.get_by_id(id):
            return
