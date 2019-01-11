from .base_test import BaseTestCase


class RSVPTest(BaseTestCase):

    def test_create_new_rsvp(self):
        response = self.client.post('api/v1/meetups/1/yes',
                                    content_type='application/json',
                                    headers=self.auth_header)
        self.assertEqual(response.status_code, 201,
                         msg="Fails to rsvp for a meetup")
