from django.urls import include, path

from .views import DeviceCreateAPI

urlpatterns = [
    path(
        "devices/",
        DeviceCreateAPI.as_view(),
        name="create_device",
    )
]
