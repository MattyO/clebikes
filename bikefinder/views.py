# Create your views here.
import json 

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django import forms

from libs.immutable import ImmutableModel

from bikefinder.models import Location, POI, POIType, POIForm, Neighborhood
from bikefinder.models import sort_by_position, find_by_name

#from libs.classes import POI, Location, to_json

def standard_context():
    return { "neighborhoods" : Neighborhood.objects.all() }

def jsonify(object):
    json_obj =json.dumps(object, 
                default=lambda instance: instance.__dict__) 

    return HttpResponse(json_obj, content_type="application/json")

def index(request):
    #c = standard_context()
    #cleveland = find_by_name(standard_context("Cleveland"))

    render(request, "bikefinder/index.html")

def map(request):
    c = standard_context()
    cleveland = ImmutableModel(
            find_by_name(c["neighborhoods"], "Cleveland"))

    c.update({"points": sort_by_position(load_poi(), cleveland.location)})

    return render(request, "bikefinder/map.html", c)

def points_of_intrests(request):
    points = {"points" : load_poi()}

    return jsonify(points)

def neighborhood(request, neighborhood_name):
    c = standard_context()
    c.update({"points":load_poi(), "neighborhood_name":neighborhood_name })

    return render(request, "bikefinder/neighborhood.html", c)

def search(request):
    pass

def submit(request):
    c = standard_context()
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

