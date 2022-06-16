
from rest_framework.decorators import api_view
from rest_framework import viewsets
from mozioapi.configurations.exceptions.mozio_core_exception import MozioError
from mozioapi.configurations.utilities.global_constants import (
    SUCCESSFULLY_CREATED,
    SUCCESSFULLY_UPDATED
)
from mozioapi.configurations.utilities.http_codes import (
    BAD_REQUEST,
    CREATED,
    UPDATED
)
from .models import Provider, ServiceArea
from mozioapi.configurations.utilities.api_response import MozioResponse
from .serializers import (
    ProviderSerializer,
    ServiceAreaSerializer,
    ServiceAreaViewSerializer
)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


@api_view(["GET"])
def welcome_api(request):
    return MozioResponse(
        message="Welcome to Mozio Core API v2.1"
    ).build_response()


class ProviderView(viewsets.ModelViewSet):

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    @method_decorator(cache_page(5))
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


class ServiceAreaView(viewsets.ModelViewSet):

    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    @method_decorator(cache_page(20))
    def list(self, request):
        result = ServiceArea.objects.all()
        serializer = ServiceAreaViewSerializer(
            result, context={"request": request}, many=True)
        return MozioResponse(
            data=serializer.data
        ).build_response()

    def retrieve(self, request, pk):
        try:
            result = ServiceArea.objects.get(id=pk)
        except ServiceArea.DoesNotExist:
            raise MozioError(
                http_status=BAD_REQUEST,
                message="No Matching Record found"
            )

        serializer = ServiceAreaViewSerializer(
            result, context={"request": request})
        return MozioResponse(
            data=serializer.data
        ).build_response()

    def create(self, request):
        serializer = ServiceAreaSerializer(
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
            instance = ServiceArea.objects.get(id=pk)
        except ServiceArea.DoesNotExist:
            raise MozioError(
                http_status=BAD_REQUEST,
                message="No Matching Record found"
            )
        serializer = ServiceAreaSerializer(
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
