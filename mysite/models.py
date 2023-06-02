from django.db import models

id = models.AutoField(primary_key=True)

class Tdx_api(models.Model):
    api_id = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)

class City_name(models.Model):
    city_English_name = models.CharField(max_length=255)
    city_Chinese_name = models.CharField(max_length=255)

class Vehicle(models.Model):
    year=models.IntegerField()
    city_name = models.CharField(max_length=255)
    county_code = models.CharField(max_length=255)
    month = models.IntegerField()
    vehicle_type = models.CharField(max_length=255)
    value = models.IntegerField()
