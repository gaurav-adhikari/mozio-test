from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from .views import (
    welcome_api,
)

router = DefaultRouter()

urlpatterns = [
    path('', welcome_api),
    path("", include(router.urls)),
]
