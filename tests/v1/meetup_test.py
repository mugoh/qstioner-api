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
        self.assertEqual(response.status_code, 200)

    def test_create_new_meetup(self):
        user_data = json.dumps(dict(
            username="Domesticable Admin",
            email="admin@mammals.milkable",
            password="pa55word",
            isAdmin=True))

        # Register admin user

        self.client.post('api/v1/auth/register',
                         data=user_data,
                         content_type='application/json')

        # Login Admin

        user_res = self.client.post('api/v1/auth/login',
                                    data=json.dumps(dict(
                                        username="Domesticable Admin",
                                        email="admin@mammals.milkable",
                                        password="pa55word"
                                    )),
                                    content_type='application/json')
        # Get Authorization token

        userH = user_res.get_json().get('Data')[0].get('token')
        self.admin_auth = {"Authorization": "Bearer " + userH}

        # Having happeningOn paramenter here gets cocky.
        res = self.client.post('api/v1/meetups',
                               content_type='application/json',
                               data=json.dumps(dict(
                                   topic="Meats can Happen",
                                   location="Over Here",
                                   tags=['jump', 'eat', 'wake']
                               )),
                               headers=self.admin_auth)
        print(res.get_json())
        self.assertEqual(res.status_code, 201)
