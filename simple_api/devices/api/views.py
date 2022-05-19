from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from devices.models import Devices

from .serializers import DeviceSerializer


class DeviceCreateAPI(APIView):
    """
    A simple api which allows clients to create new instance of Device model.
    """

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data

            device = Devices(**data)
            device.save()

            return Response(status=status.HTTP_201_CREATED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class DeviceDetailAPI(APIView):
    """
    A simple api which allows clients to get an instance of Device model using its id.
    """

    def get(self, request, pk):
        device = Devices.get(id=f"/devices/{pk}")

        if device:
            serializer = DeviceSerializer(device)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
