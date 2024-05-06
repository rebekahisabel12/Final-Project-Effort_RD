from typing import Any
from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny

from .models import AnalyticalMethod, Instrument
from .serializers import AnalyticalMethodSerializer, InstrumentSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class AnalyticalMethodViewSet(viewsets.ModelViewSet):
    queryset = AnalyticalMethod.objects.all()
    serializer_class = AnalyticalMethodSerializer


class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['analytical_methods'] = AnalyticalMethod.objects.all()
        context['instruments'] = Instrument.objects.all()
        return context


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class AnalyticalMethodRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = AnalyticalMethod.objects.all()
#     serializer_class = AnalyticalMethodSerializer
