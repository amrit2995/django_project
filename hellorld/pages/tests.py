from django.test import TestCase

class Tests(TestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def testabout(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)