from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import (
    ProviderView,
    ServiceAreaView,
    welcome_api,
)

router = DefaultRouter()
router.register("provider", ProviderView)
router.register("service-area", ServiceAreaView)


urlpatterns = [
    path('', welcome_api),
    path("", include(router.urls)),
]
