from django.shortcuts import render
from django.http import HttpResponse
import pip._vendor.requests as requests
import json
import pickle
from .models import Disease
from .forms import DiseaseDetectionForm
# from .models import HospitalQuery
# Create your views here.


def home(request):
    return render(request, 'home.html')


def symptoms(request):
    return render(request, 'symptoms.html')

def predict_disease(symptoms):
    with open('static/model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model.predict([symptoms])[0]

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
    return render(request, 'nearby_hospitals.html', {'location': location})

# Def view for the disease detection
def disease_detection(request):
    if request.method == 'POST':
        form = DiseaseDetectionForm(request.POST)
        if form.is_valid():
            symptoms = form.cleaned_data['symptoms']
            # Perform disease detection logic using the symptoms
            disease = predict_disease(symptoms)
            context = {'disease': disease}
            return render(request, 'result.html', context)
    else:
        form = DiseaseDetectionForm()

    return render(request, 'symptoms.html', {'form': form})



