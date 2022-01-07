from rest_framework import serializers
from .models import *


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = ["address"]