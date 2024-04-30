from rest_framework import serializers
from .models import Analytical_Method, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class AnalyticalMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Analytical_Method
        fields = ("method_name", "method_description",
                  "sample_matrix", "cost_per_sample")
