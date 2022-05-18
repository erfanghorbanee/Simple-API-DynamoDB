from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from devices.models import Device, DeviceModel

from .serializers import DeviceCreateSerializer, DeviceDetailSerializer


class DeviceCreateAPI(CreateAPIView):
    """
    A simple api which allows clients to create new instance of Device model.
    """

    # permission_classes = (IsAuthenticated,)

    queryset = Device.objects.all()
    serializer_class = DeviceCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)


class DeviceDetailAPI(RetrieveAPIView):
    """
    A simple api which allows clients to get an instance of Device model using its id.
    """

    # permission_classes = (IsAuthenticated,)

    queryset = Device.objects.all()
    serializer_class = DeviceDetailSerializer
