from .models import ServiceArea, Provider
from rest_framework import serializers


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            }
        }


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = "__all__"
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            }
        }
    
