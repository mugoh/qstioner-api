from flask_restful import Resource, reqparse
import datetime

from ..models.meetups import MeetUpModel
from ..utils.helpers import admin_required, auth_required


class Meetups(Resource):
    """
        This resource allows an admin user to create a meetup.
        It also makes it possible for any user to fetch all existing meetups
    """
    @auth_required
    @admin_required
    def post(self, this_user):
        parser = reqparse.RequestParser(trim=True, bundle_errors=True)
        parser.add_argument('topic', type=str)
        parser.add_argument(
            'happeningOn',
            type=lambda t: datetime.strptime(t, '%Y-%m-%dT%H:%M:%S'),
            default=datetime.datetime.utcnow().isoformat())
        parser.add_argument('tags', type=str, action='append')
        parser.add_argument('location', type=str)
        parser.add_argument('images', type=str, action='append')

        args = parser.parse_args(strict=True)

        # Ensure a meetup isn't created with same data twice

        new_meetup = MeetUpModel(**args)

        if MeetUpModel.verify_unique(new_meetup):
            return {
                "Status": 409,
                "Message": "Relax, Meetup already created"
            }, 409

        new_meetup.save()

        return {
            "Status": 201,
            "Data": [new_meetup.dictify()]
        }, 201


class MeetUp(Resource):
    """
        This resource fetches all existing meetup records
    """
    @auth_required
    def get(self, this_user):

        return {
            "Status": 200,
            "Data": [MeetUpModel.get_all_meetups()]
        }, 200


class MeetUpItem(Resource):
    """
        Searches for a meetup by its id
        and returns a matching record.
    """
    @auth_required
    def get(self, this_user, id):

        if not MeetUpModel.get_by_id(id):
            return {
                "Status": 404,
                "Error": "Meetup non-existent"
            }, 404
        return {
            "Status": 200,
            "Data": [MeetUpModel.get_by_id(id)]
        }, 200
