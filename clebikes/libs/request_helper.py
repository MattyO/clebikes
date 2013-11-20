def get_location(request_obj):
    return FancyHash({
        "location": { 
            'latitude':request_obj['latitude'],
            'longitude':request_obj['longitude']
            }
        })

