from django.shortcuts import render
import json
import pip._vendor.requests as requests
from .models import HospitalQuery
# Create your views here.


def home(request):
    return render(request, 'home.html')

def symptoms(request):
    return render(request, 'symptoms.html')

def nearby_hospitals(request):
    if request.method == 'POST':
        form = HospitalQuery(request.POST)
        if form.is_valid():
            longitude = form.cleaned_data['longitude']
            latitude = form.cleaned_data['latitude']
            radius = form.cleaned_data['radius']
            
           
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

            
            return render(request, 'nearby_hospitals.html', {'hospitals': hospitals})
    else:
        form = HospitalQuery()
    return render(request, 'find_hospital.html', {'form': form})
