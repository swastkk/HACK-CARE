import pip._vendor.requests as requests 
from .models import HospitalQuery
import json

latitude = HospitalQuery.longitude
longitude = HospitalQuery.latitude
radius = HospitalQuery.radius


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

# Print the list of nearby hospitals
print("Nearby hospitals:")
for hospital in hospitals:
    print("- {} ({})".format(hospital[0], hospital[1]))
