from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import overpy
# from .models import HospitalQuery
# Create your views here.


def home(request):
    return render(request, 'home.html')


def symptoms(request):
    return render(request, 'symptoms.html')


def nearby_hospitals(request):
    radius = "3000"
    lat = "25.3176"
    longt = "82.9739"
    api = overpy.Overpass()
    result = api.query("""[out:json][timeout:25];
nwr(around:%s,%s,%s)["amenity"="hospital"];
out center;""" % (radius, lat, longt))
    print(result.ways)
    return HttpResponse(result.ways)
