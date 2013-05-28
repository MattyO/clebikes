"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from bikefinder.models import Neighborhood, Location
import libs.db as db
from libs.immutable.model import ImmutableModel

class ModelTests(TestCase):
    def test_get_neighborhoods_are_immutable(self):
        new_location = Location.objects.create(latitude=0.0, longitude=0.0)
        self.assertIsNotNone(new_location)
        Neighborhood(
                name="Cleveland",
                location =new_location ).save()

        self.assertIsInstance(db.get_neighborhoods()[0], ImmutableModel)

