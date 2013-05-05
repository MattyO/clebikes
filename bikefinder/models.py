from django.db import models
from django.forms import ModelForm

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

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

