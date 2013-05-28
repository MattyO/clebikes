from django.test import TestCase

from libs.db import immutable_list
from bikefinder.models import Neighborhood

@immutable_list
def test_decorator():
    return Neighborhood.objects.all()

class LibTests(TestCase):
    def test_immutable_decorator_on_empty_set(self):
        self.assertEqual(test_decorator(), [])

