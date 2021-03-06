from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import (
    ProviderView,
    ServiceAreaView,
    welcome_api,
    service_area_search
)

router = DefaultRouter()
router.register("provider", ProviderView, basename='provider')
router.register("service-area", ServiceAreaView,basename="service-area")


urlpatterns = [
    path('', welcome_api),
    path("", include(router.urls)),
    path("service-area-search",service_area_search)
]
