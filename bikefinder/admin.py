from django.contrib import admin
from bikefinder.models import POIType, POI, Neighborhood

admin.site.register(POIType)
admin.site.register(POI)
admin.site.register(Neighborhood)

