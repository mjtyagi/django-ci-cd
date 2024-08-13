from django.test import TestCase, Client
from django.urls import reverse

class IndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        # Use reverse to get the URL of the view
        url = reverse('index')
        
        # Send a GET request to the URL
        response = self.client.get(url)
        
        # Check the status code
        self.assertEqual(response.status_code, 200)
        
        # Check the response content
        self.assertContains(response, "Testing")