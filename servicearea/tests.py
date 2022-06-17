import json
from re import A

from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
from servicearea.models import Provider
from servicearea.serializers import ProviderSerializer, ServiceAreaSerializer
from rest_framework import status

class ProviderTest(APITestCase):

    def test_provider(self):
        data={
            "name": "Joseph Timalsina",
            "email": "joseph.timalsina@gmail.com",
            "phone_number": 9779845123587,
            "language": "Nepali",
            "currency": "NPR"
        }

        response= self.client.post('/provider/',data)
        self.assertEqual(response.status_code==status.HTTP_201_CREATED)