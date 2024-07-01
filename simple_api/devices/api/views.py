import boto3
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings import (AWS_ACCESS_KEY_ID, AWS_REGION,
                             AWS_SECRET_ACCESS_KEY)

from .serializers import DeviceSerializer

# Get the service resource.
dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)
table = dynamodb.Table("Devices")


class DeviceCreateAPI(APIView):
    """
    A simple api which allows clients to create new instance of Device model.
    """

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            table.put_item(Item=data)

            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class DeviceDetailAPI(APIView):
    """
    A simple api which allows clients to get an instance of Device model using its id.
    """

    def get(self, request, pk):
        device = table.get_item(
            Key={
                "id": f"/devices/id{pk}",
            }
        )

        # Check if device exists.
        if "Item" in device:
            serializer = DeviceSerializer(device["Item"])
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
