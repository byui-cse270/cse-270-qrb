from django.test import TestCase, RequestFactory
from django.urls import reverse
from data.views import index

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_my_view(self):
        # Create a GET request to the view
        url = reverse('all')  
        request = self.factory.get(url)

        # Call the view function with the request
        response = index.as_view()(request)

        # Perform assertions on the response
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'businesses')