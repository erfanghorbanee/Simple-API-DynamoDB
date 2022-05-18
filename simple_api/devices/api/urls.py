from django.urls import include, path

from .views import DeviceCreateAPI, DeviceDetailAPI

urlpatterns = [
    path("devices/", DeviceCreateAPI.as_view()),
    path("devices/id<pk>/", DeviceDetailAPI.as_view()),
]
