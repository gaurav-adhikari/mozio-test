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

    email = models.TextField(
        db_column="EMAIL", null=False, blank=False, max_length=30
    )

    phone_number = models.TextField(
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
