from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework import routers
from rest_framework.test import APIRequestFactory, APITestCase


from .models import Analytical_Method
from .views import AnalyticalMethodViewSet


class AnalyticalMethodTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.analytical_method = Analytical_Method.objects.create(
            method_name="pH",
            method_description="testing pH of liquid",
            sample_matrix="liquid",
            cost_per_sample=50.00,
        )

        self.list_url = reverse("an_organ:analytical_method-list")
        self.detail_url = reverse(
            "an_organ:analytical_method-detail", kwargs={"pk": self.analytical_method.pk}
        )

    def test_create_analytical_method(self):
        data = {
            "method_name": "internal temp",
            "method_description": "Taking the temperature of liquid.",
            "sample_matrix": "liquid",
            "cost_per_sample": "20.00",
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(Analytical_Method.objects.count(), 2)
        created_method = Analytical_Method.objects.get(
            method_name="internal temp")
        self.assertEqual(created_method.method_name, "internal temp")

    # def test_analytical_method_detail(self):
    #     url = reverse('analytical-method-detail',
    #                   kwargs={'pk': self.analytical_method.pk})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['method_name'],
    #                      self.analytical_method_data['method_name'])

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
