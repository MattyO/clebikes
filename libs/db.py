from bikefinder.models import POI, Neighborhood
from libs.immutable import ImmutableModel


def immutable_list(db_function):
    def create_immutable():
        #if db_function().exists():
        return lambda: [ ImmutableModel(db_entry) for db_entry in db_function() ]
        #else:
        #    return lambda: []

    return create_immutable()

@immutable_list
def get_confirmed_pois():
    return POI.objects.filter(is_confirmed__exact=True)

@immutable_list
def get_neighborhoods():
    return Neighborhood.objects.all()


