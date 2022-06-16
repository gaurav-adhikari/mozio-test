from django.db import models


class Provider(models.Model):
    class Meta:
        db_table = "PROVIDER"

    id = models.BigAutoField(db_column="ID", primary_key=True)

    created_date = models.DateTimeField(
        db_column="CREATED_DATE", auto_now_add=True
    )

    modified_date = models.DateTimeField(
        db_column="MODIFIED_DATE", auto_now=True
    )
    
    name = models.CharField(
        db_column="NAME", max_length=200, null=True, blank=True
    )

    email = models.EmailField(
        db_column="EMAIL", null=True, blank=True, max_length=254
    )

    phone_number = models.BigIntegerField(
        db_column="PHONE_NUMBER", null=True, blank=True
    )

    language = models.CharField(
        db_column="LANGUAGE", max_length=50, null=True, blank=True
    )

    currency = models.CharField(
        db_column="CURRENCY", max_length=50, null=True, blank=True
    )


class ServiceArea(models.Model):
    class Meta:
        db_table = "SERVICE_AREA"

    id = models.BigAutoField(db_column="ID", primary_key=True)

    created_date = models.DateTimeField(
        db_column="CREATED_DATE", auto_now_add=True
    )

    modified_date = models.DateTimeField(
        db_column="MODIFIED_DATE", auto_now=True
    )

    name = models.CharField(
        db_column="NAME", max_length=200, null=True, blank=True
    )

    price = models.BigIntegerField(
        db_column="PRICE", null=True, blank=True
    )

    geojson_information = models.JSONField(
        db_column="GEOJSON_INFORMATION", null=True, blank=True
    )

    provider = models.ForeignKey(
        db_column="PROVIDER_ID",
        to=Provider,
        on_delete=models.CASCADE,
        related_name="s_provider",
    )
