from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from django_filters import filters
from .models import ShelterSubCities,ShelterFacilities

class ShelterFacilitiesFilter(GeoFilterSet):
    subcounty = filters.CharFilter(method= 'get_facilities_by_subcounty')


    class Meta:
        model = ShelterFacilities
        exclude = ['geom']

    def get_facilities_by_subcounty(self, queryset, name, value ):
        query_ = ShelterSubCities.objects.filter(pk=value)
        if query_:
            obj = query_.first()
            return queryset.filter(geom__within = obj.geom)
        return queryset