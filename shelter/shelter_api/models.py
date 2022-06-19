from django.db import models
from django.contrib.gis.db import models

class ShelterFacilities(models.Model):
    geom = models.PointField(blank=True, null=True)
    addr_city = models.CharField(db_column='addr:city', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    addr_street = models.CharField(db_column='addr:street', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone = models.CharField(db_column='contact:phone', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'shelter_facilities'

class ShelterSubCities(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    constituen = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shelter_sub_cities'