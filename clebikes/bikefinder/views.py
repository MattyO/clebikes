# Create your views here.
import json 
import types

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django import forms

import libs.db as db
import libs.request_helper as request_helper
#import libs.form_helper as form_helper

from bikefinder.models import Location, POI, POIType, POIForm, Neighborhood
from bikefinder.models import sort_by_position, find_by_name, is_location, get_location
from changeless.types import FancyHash
from changeless.methods import to_json, to_dict

#from libs.classes import POI, Location, to_json

def standard_context():
    return { "neighborhoods" : db.get_neighborhoods() }

def jsonify(an_object):
    return HttpResponse(json.dumps(an_object), content_type="application/json")

def resolve_http_method(request, methods):
    '''Thinking this method is pasted a list of methods or the dictonary returned from the 
    python core function locals.  However any dictonary with function objects will do 
    which gives it a nice amount of scoping and configurablity
    '''
    if isinstance(methods, types.ListType):
        methods = { a_function.__name__ : a_function for a_function in methods }
    return methods[request.method.lower()]()


def index(request):
    c = standard_context()
    cleveland = find_by_name(standard_context['neighborhoods'], "Cleveland")

    render(request, "bikefinder/index.html")

def map(request):
    c = standard_context()

    cleveland = find_by_name(c['neighborhoods'], "Cleveland")

    points = db.get_confirmed_pois()
    points = sort_by_position(points, get_location(cleveland))

    c.update({"points": points })

    return render(request, "bikefinder/map.html", c)

def points_of_intrests(request):

    points = db.get_confirmed_pois()
    location = request_helper.get_location(request.GET)
    if location is not  None:
        points = sort_by_position(points, location)

    print to_json(points)
    points = {"points" : to_dict(points)}
    return jsonify(points)

def neighborhood(request, neighborhood_name):
    c = standard_context()
    neighborhood = find_by_name(db.get_neighborhoods(), neighborhood_name)
    points = db.get_confirmed_pois()

    c.update({"points":points , "neighborhood":neighborhood })

    return render(request, "bikefinder/neighborhood.html", c)

def search(request):
    return HttpResponse(json.dumps({}), content_type="application/json")


def submit(request):
    c = standard_context()
    c.update(csrf(request))
    a_form = POIForm()
    a_form.fields['name'].widget = forms.TextInput(attrs={"class":"span6"})
    a_form.fields['description'].widget = forms.Textarea(attrs={"class":"span6", "rows":"5", "cols":"80"})
    c.update({ "submit_form" : a_form })

    def post():
        a_form = POIForm(request.POST)
        if a_form.is_valid(): 
            new_poi = a_form.save(commit=False)
            new_poi.location = Location.objects.create(
                    latitude = request.POST['hdn-latitude'],
                    longitude = request.POST['hdn-longitude'])
            new_poi.save()
            return redirect("bikefinder.views.submit")

        print dir(a_form.fields['time'])
        c.update({ "submit_form" : a_form })
        return render(request, "bikefinder/submit.html", c)


    def get():
        return render(request, "bikefinder/submit.html", c)

    return resolve_http_method(request, [get, post])

