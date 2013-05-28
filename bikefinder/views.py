# Create your views here.
import json 

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django import forms

from libs.immutable import ImmutableModel
import libs.immutable as immutable 
import libs.db as db

from bikefinder.models import Location, POI, POIType, POIForm, Neighborhood
from bikefinder.models import sort_by_position, find_by_name, is_location

#from libs.classes import POI, Location, to_json

def standard_context():
    print db.get_neighborhoods()
    return { "neighborhoods" : db.get_neighborhoods() }

def jsonify(object):
    json_obj =json.dumps(object, 
                default=lambda instance: instance.__dict__)

    return HttpResponse(json_obj, content_type="application/json")

def index(request):
    c = standard_context()
    cleveland = find_by_name(standard_context['neighborhoods'], "Cleveland")

    render(request, "bikefinder/index.html")

def map(request):
    c = standard_context()
    cleveland = find_by_name(c["neighborhoods"], "Cleveland")
    points = sort_by_position(db.get_confirmed_pois(), cleveland.location)

    c.update({"points": points })

    return render(request, "bikefinder/map.html", c)

def points_of_intrests(request):

    points = db.get_confirmed_pois()

    query_args = immutable.create(request.GET)
    if is_location(query_args):
        points = sort_by_position(points, query_args)

    points = {"points" : points}
    return jsonify(points)

def neighborhood(request, neighborhood_name):
    c = standard_context()
    neighborhoods = find_by_name(db.get_neighborhoods())
    points = db.get_confirmed_pois()

    c.update({"points":points , "neighborhood_name":neighborhood_name })

    return render(request, "bikefinder/neighborhood.html", c)

def search(request):
    points
    return HttpResponse(json.dumps({}), content_type="application/json")


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

