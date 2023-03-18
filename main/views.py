from django.shortcuts import render
from django.http import HttpResponse
import pip._vendor.requests as requests
import json

# from .models import HospitalQuery
# Create your views here.


def home(request):
    return render(request, 'home.html')


def symptoms(request):
    return render(request, 'symptoms.html')


def nearby_hospitals(request):
    latitude = 25.320575
    longitude = 82.993012
    radius = 5000

    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
        [out:json];
        node(around:{}, {}, {})[amenity=hospital];
        out;
        """.format(radius, latitude, longitude)

    response = requests.get(overpass_url, params={'data': overpass_query})
    data = response.json()

    hospitals = []
    for element in data['elements']:
        if element['type'] == 'node' and 'name' in element['tags']:
            hospital_name = element['tags']['name']
            hospital_location = (element['lat'], element['lon'])
            hospitals.append((hospital_name, hospital_location))
    location = [{"Name": a[0], "Geolang": a[1]} for a in hospitals]
    print(location)

    # for hospital in hospitals:
    #     location["Name"].append(hospital[0])
    #     location["Geolang"].append(hospital[1])
    return render(request, 'nearby_hospitals.html', {'location': location})
