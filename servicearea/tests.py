from django.test import TestCase, Client
from django.urls import reverse

from servicearea.models import Provider
from servicearea.serializers import ProviderSerializer


class GetAllProviderTest(TestCase):
    """ Test module for GET all puppies API """

    # def setUp(self):
    #     Puppy.objects.create(
    #         name='Casper', age=3, breed='Bull Dog', color='Black')
    #     Puppy.objects.create(
    #         name='Muffin', age=1, breed='Gradane', color='Brown')
    #     Puppy.objects.create(
    #         name='Rambo', age=2, breed='Labrador', color='Black')
    #     Puppy.objects.create(
    #         name='Ricky', age=6, breed='Labrador', color='Brown')

    def test_get_all_providers(self):
        response = Client.get(reverse('provider'))
        qs = Provider.objects.all()
        serializer = ProviderSerializer(qs, many=True)
        self.assertEqual(response.data, serializer.data)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
