from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from devices.models import Device, DeviceModel

from .serializers import DeviceSerializer


class DeviceCreateAPI(APIView):
    """
    A simple api which allows clients to create new instance of Device model
    or update the one that already exists.
    """

    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            name = data.get("name")
            note = data.get("note")
            serial = data.get("serial")
            id = data.get("id").replace("/devices/id", "")
            deviceModel_id = data.get("deviceModel").replace("/devicemodels/id", "")

            if not id.isdigit():
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={"error": "id field must be in this format: /devices/id1"},
                )

            elif not deviceModel_id.isdigit():
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={
                        "error": "deviceModel field must be in this format: /devicemodels/id1"
                    },
                )

            elif (
                not DeviceModel.objects.only("id")
                .filter(id=int(deviceModel_id))
                .exists()
            ):
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={"error": "Device model with this id does not exist."},
                )

            else:
                new_device = Device(
                    id=int(id),
                    deviceModel_id=int(deviceModel_id),
                    name=name,
                    note=note,
                    serial=serial,
                )
                new_device.save()

                return Response(
                    status=status.HTTP_201_CREATED,
                )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
