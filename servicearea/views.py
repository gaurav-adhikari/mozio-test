
from rest_framework.decorators import api_view

from mozioapi.configurations.utilities.api_response import MozioResponse


@api_view(["GET"])
def welcome_api(request):
    return MozioResponse(message="Welcome to Mozio Core API v2.1").build_response()
