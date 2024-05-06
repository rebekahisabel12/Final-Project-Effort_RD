from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework import routers
from rest_framework.test import APIRequestFactory, APITestCase


from .models import AnalyticalMethod
from .models import Instrument
from .views import AnalyticalMethodViewSet, InstrumentViewSet


class InstrumentTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.instrument = Instrument.objects.create(
            manufacturer='Firenza',
            sample_type='Solid',
        )
        self.list_url = reverse("an_organ:instrument-list")
        self.detail_url = reverse(
            "an_organ:instrument-detail", kwargs={"pk": self.instrument.id})

    def test_create_instrument(self):
        data = {
            "manufacturer": "New Manufacturer",
            "sample_type": "Liquid"
        }
        response = self.client.post(self.list_url, data, format="json")
        print("Status Code:", response.status_code)
        print("Response Data:", response.json())
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(Instrument.objects.count(), 2)
        self.assertEqual(Instrument.objects.get(
            manufacturer="New Manufacturer").sample_type, "Liquid")

    def test_list_instruments(self):
        response = self.client.get(self.list_url)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(
            response.data["results"][0]["manufacturer"], self.instrument.manufacturer)

    def test_retrieve_instrument(self):
        response = self.client.get(self.detail_url)
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(
            response.data["manufacturer"], self.instrument.manufacturer)

    def test_update_instrument(self):
        data = {
            "manufacturer": "Updated Manufacturer",
            "sample_type": "gas"
        }
        response = self.client.put(
            reverse("an_organ:instrument-detail",
                    kwargs={"pk": self.instrument.id}),
            data,
            format="json",
        )
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(
            response.data["manufacturer"], "Updated Manufacturer")
    # def test_delete_instrument(self):
    #     response = self.client.delete(self.detail_url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(Instrument.objects.count(), 0)

# class AnalyticalMethodAPITestCase(APITestCase):
#     def setUp(self):
#         self.instrument = Instrument.objects.create(
#             manufacturer='Firenza',
#             sample_type='Solid'
#         )
#         self.method = AnalyticalMethod.objects.create(
#             method_name='Test Method',
#             method_description='Description of analytical method',
#             instrument=self.instrument,
#             cost_per_sample=100.00
#         )

#     def test_create_analytical_method(self):
#         self.assertEqual(self.method.method_name, 'Test Method')
#         self.assertEqual(self.method.method_description,
#                          'Description of analytical method')
#         self.assertEqual(self.method.instrument, self.instrument)
#         self.assertEqual(self.method.cost_per_sample, 100.00)

#     # def test_analytical_method_detail(self):
#     #     url = reverse('analytical-method-detail',
#     #                   kwargs={'pk': self.analytical_method.pk})
#     #     response = self.client.get(url)
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     #     self.assertEqual(response.data['method_name'],
#     #                      self.analytical_method_data['method_name'])

    # def test_analytical_method_create(self):
    #     url = reverse('analytical-method-list')
    #     new_analytical_method_data = {
    #         "method_name": "New Method",
    #         "method_description": "Description of New Method",
    #         "sample_matrix": "New Matrix",
    #         "cost_per_sample": 100.00,
    #     }
    #     response = self.client.post(
    #         url, new_analytical_method_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     # Assuming two AnalyticalMethod objects are created now
    #     self.assertEqual(Analytical_Method.objects.count(), 2)
