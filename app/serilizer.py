from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    class Meta:
        address = serializers.CharField(max_length=300, allow_blank=False)