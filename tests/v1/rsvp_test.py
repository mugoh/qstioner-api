from .base_test import BaseTestCase


class RSVPTest(BaseTestCase):

    def test_create_new_rsvp(self):

        response = self.post('api/v1/meetups/1/yes')

        self.assertEqual(response.status_code, 201,
                         msg="Fails to rsvp for a meetup")

    def test_create_rsvp_with_unknown_response(self):
        # Known responses are 'yes', 'no' and 'maybe'

        response = self.get('api/v1/meetups')
        self.assertEqual(response.status_code, 400,
                         msg="Fails to not\
                         create an rsvp with an invalid response")
