from .base_test import BaseTestCase
import json


class MeetUpTests(BaseTestCase):

    def test_create_meetup_as_non_admin(self):
        response = self.client.post('api/v1/meetups',
                                    data=json.dumps(dict(
                                        topic="Meats can Happen",
                                        location="Over Somewhere",
                                        happeningOn="2019-01-01T00:10:00",
                                        tags=['jump', 'eat', 'woke']
                                    )),
                                    content_type='application/json',
                                    headers=self.auth_header)
        self.assertEqual(response.status_code, 403,
                         msg="Fails to create new meetup")

    def test_get_all_meetups(self):
        response = self.client.get('api/v1/meetups/upcoming',
                                   content_type='application/json',
                                   headers=self.auth_header)
        self.assertEqual(response.status_code, 201)

    def test_create_new_meetup(self):
