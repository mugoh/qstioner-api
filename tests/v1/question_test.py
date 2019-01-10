from .base_test import BaseTestCase
import json


class TestQuestions(BaseTestCase):

    def test_create_new_question(self):
        self.new_question = json.dumps(dict(
            title="One Question",
            body="This looks lika a body"))

        response = self.client.post('api/v1/questions',
                                    data=self.new_question,
                                    content_type='application/json',
                                    headers=self.auth_header)
        self.assertEqual(response.status_code, 201,
                         msg="Fails to create a new question")

    def test_get_all_questions(self):

        response = self.client.get('api/v1/questions',
                                   content_type='application/json',
                                   headers=self.auth_header)
        self.assertEqual(response.status_code, 200,
                         msg="Fails to get all questions")

    def test_get_single_question(self):

        response = self.client.get('api/v1/questions/1',
                                   content_type='application/json',
                                   headers=self.auth_header)
        self.assertEqual(response.status_code, 200,
                         msg="Fails to fetch individual question")

    def test_create_existing_question(self):
        self.new_question = json.dumps(dict(
            title="One Question",
            body="This looks lika a body"))

        response = self.client.post('api/v1/questions',
                                    data=self.new_question,
                                    content_type='application/json',
                                    headers=self.auth_header)
        self.assertEqual(response.status_code, 201,
                         msg="Fails to avoid creation\
                         of question with same data twice")
