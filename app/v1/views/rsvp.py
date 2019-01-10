"""
    This module contains resource views for the
    rsvp Resource
"""

from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.v1.models.rsvp import RsvpModel
from ..models.meetups import MeetUpModel
from ..models.users import UserModel


class Rsvps(Resource):
    decorators = [jwt_required]

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
            return {
                "Status": 400,
                "Message": "That meetup does not exist"
            }, 400

        user = UserModel.get_by_name(get_jwt_identity()).id

        args.update({
            "user": user
        })

        # Create rsvp and confirm it's not a duplicate

        rsvp = RsvpModel(**args)
        if not RsvpModel.verify_unique(rsvp):
            return {
                "Status": 409,
                "Message": "You've done that same rsvp already"
            }, 409
        rsvp.save()

        return {
            "Status": 201,
            "Data": rsvp.dictify()
        }, 201
