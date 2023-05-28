from django.db import models

id = models.AutoField(primary_key=True)

class Vehicle(models.Model):
    city_name = models.CharField(max_length=255)
    county_code = models.CharField(max_length=255)
    month = models.IntegerField()
    vehicle_type = models.CharField(max_length=255)
    value = models.IntegerField()
