import json 
def distance_between(point_a, point_b):
    return 1

def sort_by_closest(a_list, location):
    return sorted(a_list, cmp=distance_between)

class Location():
    def __init__(self, latitude=0, longitude=0):
        self.latitude = latitude
        self.longitude = longitude

class POI():
    def __init__(self, id=-1, name="", type="", location=Location()):
        self.id= id
        self.name = name
        self.description = ""
        self.type = type
        self.location = location

def to_json(object):
    return json.dumps(object, 
            default=lambda instance: instance.__dict__)

