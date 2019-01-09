from .base_test import BaseTestCase
import json


class MeetUpTests(BaseTestCase):

    def test_create_meetup(self):
        response = self.client.post('api/v1/meetups',
                                    data=json.dumps(dict(
                                        topic="Meats can Happen",
                                        location="Over Somewhere",
                                        happeningOn="2019-01-01T00:10:00",
                                        tags=['jump', 'eat', 'woke']
                                    )),
                                    content_type='application/json',
                                    headers=self.auth_header)

        self.assertTrue(response.status.code == 201)
