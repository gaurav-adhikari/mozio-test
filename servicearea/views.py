
from rest_framework.decorators import api_view, renderer_classes
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
from rest_framework.renderers import JSONRenderer


@api_view(["GET"])
@renderer_classes([JSONRenderer])
def welcome_api(request):
    """
    This functional component is used to display welcome
    API
    """

    return MozioResponse(
        message="Welcome to Mozio Core API v2.1"
    ).build_response()


class ProviderView(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Provider.
    """

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    renderer_classes = [JSONRenderer]

    @method_decorator(cache_page(5))
    def list(self, request):
        """
        This GET function lists all the Provider and searlizes it
        to generates a detailed response.
        """
        result = Provider.objects.all()
        serializer = ProviderSerializer(
            result, context={"request": request}, many=True)
        return MozioResponse(
            data=serializer.data
        ).build_response()

    def retrieve(self, request, pk):
        """
        This GET function retrieves a Provider and searlizes it
        to generates a detailed response.

        Args:
            pk (int): Primary key of ServiceArea to look for.
        """
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
        """
        This POST function takes a json body and creates a new
        Provider object.
        """
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
        """
        This PUT function takes a json body to update
        a particular Provider object.

        Args:
            pk (int): Primary key of Provider to update.
        """

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
    """
    This viewset class provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Provider.
    """

    # Initialize class variables
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    renderer_classes = [JSONRenderer]

    # include static caching of 20 seconds
    @method_decorator(cache_page(20))
    def list(self, request):
        """
        This GET function lists all the service area and searlizes it
        to generates a detailed response.
        """
        result = ServiceArea.objects.all()
        serializer = ServiceAreaViewSerializer(
            result, context={"request": request}, many=True)
        return MozioResponse(
            data=serializer.data
        ).build_response()

    def retrieve(self, request, pk):
        """
        This GET function retrieves a service area and searlizes it
        to generates a detailed response.

        Args:
            pk (int): Primary key of ServiceArea to look for.
        """
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
        """
        This POST function takes a json body and creates a new
        ServiceArea object.
        """
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
        """
        This PUT function takes a json body to update
        a particular ServiceArea object.

        Args:
            pk (int): Primary key of ServiceArea to update.
        """

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


@api_view(("GET",))
@renderer_classes([JSONRenderer])
def service_area_search(request):
    """
    This functional component is used to query ServiceArea with given
    latitude and longitude from the request object
    """

    # validate if the args are passed onto the query params.
    if not request.GET.get("latitude") or not request.GET.get("longitude"):
        raise MozioError(
            http_status=BAD_REQUEST,
            message="Please provide a valid latitude & longitude",
        )

    try:
        # prepare data to a list to query the json field
        latlong = [float(request.query_params.get(
            "latitude")), float(request.GET.get("longitude"))]

        # Query Database
        qs = ServiceArea.objects.filter(
            geojson_information__coordinates=latlong)

        # Serialize the queryset
        serializer = ServiceAreaViewSerializer(
            qs, context={"request": request}, many=True)

        # Preapre a detailed response body
        return MozioResponse(
            data=serializer.data
        ).build_response()

    # Handle exception if any
    except Exception as e:
        raise MozioError(
            http_status=BAD_REQUEST,
            message=f"Invalid parameters",
        )
