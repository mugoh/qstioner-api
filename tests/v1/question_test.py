from .base_test import BaseTestCase
import json


class TestQuestions(BaseTestCase):

    def test_create_new_question(self):
        self.new_question = json.dumps(dict(
            title="One Question",
            body="This looks lika a body"))

        response = self.client.post('api/v1/questions/',
                                    data=self.new_question,
                                    content_type='application/json',
                                    headers=self.auth_header)
        self.assertEqual(response.status_code, 203)
