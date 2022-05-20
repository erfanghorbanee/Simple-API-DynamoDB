import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APISimpleTestCase

client = APIClient()


class TestDeviceDetailAPI(APISimpleTestCase):
    """Test module for TestDeviceDetailAPI view"""

    def test_get_valid_one_device(self):
        response = client.get("http://127.0.0.1:8000/api/v1/devices/id1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_one_device(self):
        response = client.get("http://127.0.0.1:8000/api/v1/devices/id22/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestDeviceCreateAPI(APISimpleTestCase):
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

        self.url = reverse("create_device")

    def test_create_valid_device(self):
        response = client.post(self.url, self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_device(self):
        response = client.post(self.url, self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
