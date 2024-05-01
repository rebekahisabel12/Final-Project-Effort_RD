from django.db import transaction
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import localtime

from an_organ.models import AnalyticalMethod
from chromatographyarch.domain.model import DomainAnalyticalMethod
from chromatographyarch.adapters import repository
from chromatographyarch.service_layer.uow import DjangoUnitofWork


class RepositoryTests(TestCase):
    def setUp(self):
        rightnow = localtime().date()

        self.repository = repository.DjangoRepository()
        self.domain_analyticalmethod_1 = DomainAnalyticalMethod(
            method_name="pH",
            method_description="testing pH of liquid",
            instrument="Spex",
            cost_per_sample=50.00,
        )

    def test_repository_add(self):
        self.repository.add(self.domain_analyticalmethod_1)
        self.assertEqual(AnalyticalMethod.objects.count(), 1)
