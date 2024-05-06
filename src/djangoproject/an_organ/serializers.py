from rest_framework import serializers
from .models import AnalyticalMethod, Instrument, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'


class AnalyticalMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticalMethod
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    instruments = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Instrument.objects.all()
    )
    analyticalmethod = AnalyticalMethodSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["username", "analyticalmethod"]
