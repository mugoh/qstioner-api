from flask_restful import Resource, reqparse
import datetime

from app.v1.models.meetups import MeetUpModel


class Meetups(Resource):
    """
        This resource allows an admin user to create a meetup.
        It also makes it possible for any user to fetch all existing meetups
    """

    def post(self):
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

        MeetUpModel(**args).save()
