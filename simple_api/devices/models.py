from django.db import models


# Create your models here.
class Device(models.Model):
    deviceModel = models.ForeignKey(
        "DeviceModel", on_delete=models.CASCADE, related_name="devices"
    )
    name = models.CharField(max_length=200, unique=True)
    note = models.TextField(max_length=5000, default="Coming soon...")
    serial = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class DeviceModel(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
