from django.test import TestCase

# Create your tests here.

class CreditTest(TestCase):
    def test_credit(self):
        response = self.client.get('/credit/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])