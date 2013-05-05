# Create your views here.
import json 

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django import forms

from bikefinder.models import Location, POI, POIType, POIForm
from libs.immutable import ImmutableModel
#from libs.classes import POI, Location, to_json

def jsonify(object):
    json_obj =json.dumps(object, 
                default=lambda instance: instance.__dict__) 

    return HttpResponse(json_obj, content_type="application/json")

def index(request):
    render(request, "bikefinder/index.html")

def map(request):
    context = {"points":load_poi()}
    return render(request, "bikefinder/map.html", context)

def points_of_intrests(request):
    points = {"points" : load_poi()}

    return jsonify(points)

def submit(request):
    c = {}
    c.update(csrf(request))

    if(request.POST):
        a_form = POIForm(request.POST)
        if(a_form.is_valid()):
            new_poi = a_form.save(commit=False)
            new_poi.location = Location.objects.create(
                    latitude = request.POST['hdn-latitude'], 
                    longitude = request.POST['hdn-longitude'])
            new_poi.save()

        else:
            print a_form.errors
        #print request.POST
        #print request.POST['poi_type'][0]
        #POI.objects.create(
        #        name = request.POST['name'], 
        #        location = Location.objects.create(
        #            latitude = request.POST['hdn-latitude'], 
        #            longitude = request.POST['hdn-longitude']), 
        #        description = request.POST['description'], 
        #        type= POIType.objects.get(pk=request.POST['poi_type'][0]),
        #        address = request.POST['address'],
        #        )
        return redirect("bikefinder.views.submit")

    a_form = POIForm()
    a_form.fields['name'].widget = forms.TextInput(attrs={"class":"span6"})
    a_form.fields['description'].widget = forms.Textarea(attrs={"class":"span6", "rows":"5", "cols":"80"})

    c.update({ "submit_form" : a_form })
    return render(request, "bikefinder/submit.html", c)

def get_confirmed_pois():
    return POI.objects.filter(is_confirmed__exact=True)

def load_poi():
    return [ ImmutableModel(poi_object) for poi_object in get_confirmed_pois() ]

