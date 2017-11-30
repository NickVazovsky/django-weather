from django.test import TestCase

# Create your tests here.
class TestViews(TestCase):
    def test_view_get_currency(self):
        response = self.client.get('/currency/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '0')

    def test_view_get_weather(self):
        response = self.client.get('/weather/')
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '0')