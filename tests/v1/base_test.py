import unittest
from app import create_app
import json


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

        # create new user
        self.user_data = json.dumps(dict(
            username="Domesticable Cow",
            email="cow@mammals.milkable",
            password="pa55word"))

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
