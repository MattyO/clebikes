from bikefinder.models import POI, Neighborhood
from changeless.decorators import immutable_list

@immutable_list
def get_confirmed_pois():
    return POI.objects.filter(is_confirmed__exact=True)

@immutable_list
def get_neighborhoods():
    return Neighborhood.objects.all()


