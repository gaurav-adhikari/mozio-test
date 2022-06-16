# Generated by Django 4.0.5 on 2022-06-16 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='CREATED_DATE')),
                ('modified_date', models.DateTimeField(auto_now=True, db_column='MODIFIED_DATE')),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=200, null=True)),
                ('email', models.TextField(db_column='EMAIL', max_length=30)),
                ('phone_number', models.TextField(blank=True, db_column='PHONE_NUMBER', null=True)),
                ('language', models.CharField(blank=True, db_column='LANGUAGE', max_length=50, null=True)),
                ('currency', models.CharField(blank=True, db_column='CURRENCY', max_length=50, null=True)),
            ],
            options={
                'db_table': 'PROVIDER',
            },
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.BigAutoField(db_column='ID', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='CREATED_DATE')),
                ('modified_date', models.DateTimeField(auto_now=True, db_column='MODIFIED_DATE')),
                ('name', models.CharField(blank=True, db_column='NAME', max_length=200, null=True)),
                ('price', models.BigIntegerField(blank=True, db_column='PRICE', null=True)),
                ('geojson_information', models.JSONField(blank=True, db_column='GEOJSON_INFORMATION', null=True)),
            ],
            options={
                'db_table': 'SERVICE_AREA',
            },
        ),
    ]
