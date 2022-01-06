from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    class Meta:
        address = serializers.CharField(max_length=300, allow_blank=False, allow_null=False, help_text="24634 N 36th Ave, Glendale, AZ 85310")