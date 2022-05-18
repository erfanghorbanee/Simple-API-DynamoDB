import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from devices.api.serializers import (DeviceCreateSerializer,
                                     DeviceDetailSerializer)
from devices.models import Device, DeviceModel

client = APIClient()


class TestDeviceDetailAPI(APITestCase):
    """Test module for TestDeviceDetailAPI view"""

    def setUp(self):
        self.deviceModel1 = DeviceModel.objects.create(id=1, name="device model1")

        self.device1 = Device.objects.create(
            id=1,
            deviceModel=self.deviceModel1,
            name="device1",
            note="note1",
            serial="124nfjs31aa",
        )

    def test_get_valid_one_device(self):
        response = client.get(reverse("device-detail", kwargs={"pk": self.device1.pk}))
        device = Device.objects.get(pk=self.device1.pk)
        serializer = DeviceDetailSerializer(device)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_one_device(self):
        response = client.get(reverse("device-detail", kwargs={"pk": 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestDeviceCreateAPI(APITestCase):
    """Test module for inserting a new Device"""

    def setUp(self):
        self.valid_payload = {
            "id": "/devices/id1",
            "deviceModel": "/devicemodels/id1",
            "name": "Sensor",
            "note": "Testing a sensor.",
            "serial": "A020000102",
        }

        self.invalid_payload = {
            "id": "",
            "deviceModel": "/devicemodels/id1",
            "name": "Sensor",
            "note": "Testing a sensor.",
        }

        self.url = reverse("create-device")

        self.deviceModel1 = DeviceModel.objects.create(id=1, name="device model1")

    def test_create_valid_device(self):
        response = client.post(self.url, self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_device(self):
        response = client.post(self.url, self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
