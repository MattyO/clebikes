from django.db import models
from django.forms import ModelForm
from geopy import distance 
from geopy.point import Point

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    def __str__(self):
        return "id: {2}. lat: {0}, lng: {1}".format(self.latitude, self.longitude, self.id)

class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location)
    def __str__(self):
        return self.name

class POIType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class POI(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    location = models.ForeignKey(Location)
    type = models.ForeignKey(POIType)
    is_confirmed = models.BooleanField(default=False)

class POIForm(ModelForm):
        class Meta:
            model = POI
            exclude=('location',)


def sort_by_position(list_with_location, points_closest_to):
    def adistance(location_one, location_two):
        point_one = Point(location_one.latitude,location_one.longitude)
        point_two = Point(location_two.latitude,location_two.longitude)
        return int(distance.distance(point_one, point_two).kilometers)

    return sorted(list_with_location,
            lambda x,y:
                adistance(x.location, points_closest_to) -
                adistance(y.location, points_closest_to) )

def find_by_name(list_with_names, name_to_find):
    item_found = None
    for item in list_with_names:
        if item.name == name_to_find:
            item_found = item
            break

    return item_found


