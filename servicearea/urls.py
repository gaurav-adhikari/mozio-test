from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import (
    ProviderView,
    welcome_api,
)

router = DefaultRouter()
router.register("provider", ProviderView)


urlpatterns = [
    path('', welcome_api),
    path("", include(router.urls)),
]
