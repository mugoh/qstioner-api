import unittest
from app import create_app
import json


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

        # create admin user
        self.user_data = json.dumps(dict(
            username="Domesticable Cow",
            email="cow@mammals.milkable",
            password="pa55word",
            isAdmin=True))

        response = self.client.post('/api/v1/auth/register',
                                    data=self.user_data,
                                    content_type='application/json')
        self.new_user = json.loads(response.data.decode())

        login_response = self.client.post('/api/v1/auth/login',
                                          data=self.user_data,
                                          content_type='application/json')
        user = json.loads(login_response.data.decode()
                          ).get("Data")[0].get('token')
        self.auth_header = {"Authorization": "Bearer " + user}

        # create new meetup

        self.meetup_data = json.dumps(dict(
            topic="Meats can Happen",
            location="Over Here",
            happeningOn="2019-01-01T23:13:00",
            tags=['jump', 'eat', 'wake']
        ))

        meetup_response = self.client.post('api/v1/meetups',
                                           data=self.meetup_data,
                                           content_type='application/json',
                                           headers=self.auth_header)
