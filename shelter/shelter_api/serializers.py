from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import  ShelterFacilities,ShelterSubCities

class ShelterSubCitiesSerializer(GeoFeatureModelSerializer):

	class Meta:
		model = ShelterSubCities
		fields = '__all__'
		geo_field = 'geom'

    
class ShelterFacilitiesSerializer(GeoFeatureModelSerializer):
    	
	distance = serializers.CharField()

	class Meta:
		model = ShelterFacilities
		fields = '__all__'
		geo_field = 'geom'
		read_only_fields = ['distance']