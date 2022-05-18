from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from devices.models import Device, DeviceModel


class DeviceCreateSerializer(ModelSerializer):
    id = serializers.CharField(max_length=50, allow_null=False)
    deviceModel = serializers.CharField(max_length=50, allow_null=False)

    class Meta:
        model = Device
        fields = ("id", "deviceModel", "name", "note", "serial")

    def validate_id(self, value):
        id = value.replace("/devices/id", "")

        if not id.isdigit():
            raise serializers.ValidationError(
                "id field must be eithrt in this format: /devices/id1 or just a number"
            )
        else:
            id = int(id)

        if Device.objects.only("id").filter(id=id).exists():
            raise serializers.ValidationError("Device with this id already exists!")

        return id

    def validate_deviceModel(self, value):
        deviceModel = value.replace("/devicemodels/id", "")

        if not deviceModel.isdigit():
            raise serializers.ValidationError(
                "deviceModel field must be either in this format /devicemodels/id1 or just a number"
            )
        else:
            deviceModel = int(deviceModel)
            qs = DeviceModel.objects.only("id").filter(id=deviceModel)

        if not qs.exists():
            raise serializers.ValidationError(
                "deviceModel with this id doest not exist!"
            )

        return qs.first()


class DeviceDetailSerializer(ModelSerializer):
    id = serializers.SerializerMethodField()
    deviceModel = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Device
        fields = ("id", "deviceModel", "name", "note", "serial")

    def get_id(self, obj):
        return f"/devicemodels/id{obj.id}"

    def get_deviceModel(self, obj):
        return f"/devicemodels/id{obj.deviceModel.id}"
