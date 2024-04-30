from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Analytical_Method
from .serializers import AnalyticalMethodSerializer


class AnalyticalMethodViewSet(viewsets.ModelViewSet):
    queryset = Analytical_Method.objects.all().order_by("-method_name")
    serializer_class = AnalyticalMethodSerializer


# class AnalyticalMethodRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = AnalyticalMethod.objects.all()
#     serializer_class = AnalyticalMethodSerializer
