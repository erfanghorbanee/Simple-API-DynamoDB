from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from devices.models import Device


class DeviceSerializer(ModelSerializer):
    id = serializers.CharField(max_length=50, allow_null=False)
    deviceModel = serializers.CharField(max_length=50, allow_null=False)

    class Meta:
        model = Device
        fields = ("id", "deviceModel", "name", "note", "serial")
