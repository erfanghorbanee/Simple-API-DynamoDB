from django.contrib import admin
from .models import Device, DeviceModel


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    pass


@admin.register(DeviceModel)
class DeviceModelAdmin(admin.ModelAdmin):
    pass
