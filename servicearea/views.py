
from rest_framework.decorators import api_view
from rest_framework import viewsets

from mozioapi.configurations.exceptions.mozio_core_exception import MozioError
from mozioapi.configurations.utilities.global_constants import SUCCESSFULLY_CREATED, SUCCESSFULLY_UPDATED
from mozioapi.configurations.utilities.http_codes import BAD_REQUEST, CREATED, UPDATED
from .models import Provider, ServiceArea
from mozioapi.configurations.utilities.api_response import MozioResponse
from .serializers import ProviderSerializer, ServiceAreaSerializer


@api_view(["GET"])
def welcome_api(request):
    return MozioResponse(message="Welcome to Mozio Core API v2.1").build_response()


class ProviderView(viewsets.ModelViewSet):

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


    def list(self, request):
        result = Provider.objects.all()
        serializer = ProviderSerializer(
            result, context={"request": request}, many=True)
        return MozioResponse(
            data=serializer.data
        ).build_response()


    def retrieve(self, request, pk):
        try:
            result = Provider.objects.get(id=pk)
        except Provider.DoesNotExist:
            raise MozioError(
                http_status=BAD_REQUEST,
                message="No Matching Record found"
            )

        serializer = ProviderSerializer(result, context={"request": request})
        return MozioResponse(
            data=serializer.data
        ).build_response()


    def create(self, request):
        serializer = ProviderSerializer(
            data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return MozioResponse(
            data=serializer.data,
            http_status=CREATED,
            message=SUCCESSFULLY_CREATED,
        ).build_response()

    def update(self, request, pk):
        try:
            instance = Provider.objects.get(id=pk)
        except Provider.DoesNotExist:
            raise MozioError(
                http_status=BAD_REQUEST,
                message="No Matching Record found"
            )
        serializer = ProviderSerializer(
            instance=instance,
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return MozioResponse(
            data=serializer.data,
            http_status=UPDATED,
            message=SUCCESSFULLY_UPDATED,
        ).build_response()
