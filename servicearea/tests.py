
from rest_framework.test import APITestCase, APIClient
from servicearea.models import Provider
from servicearea.serializers import ProviderSerializer, ServiceAreaSerializer
from rest_framework import status

from servicearea.views import ProviderView


class ProviderTest(APITestCase):

    def test_provider(self):
        data = {
            "name": "Joseph50s Timalsina",
            "email": "joseph.timalsina@gmail.com",
            "phone_number": 9779845123587,
            "language": "Nepali",
            "currency": "NPR"
        }
        response = self.client.post('/provider-list/', data, format='json')
        print(response.__dict__)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
