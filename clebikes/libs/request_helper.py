from changeless.types import FancyHash
def get_location(request_obj):
    location = None
    if 'latitude' in request_obj.keys():
        location =  FancyHash({
            "location": { 
                'latitude':request_obj['latitude'],
                'longitude':request_obj['longitude']
                }
        })

    return location
