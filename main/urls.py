from django.urls import path
from .views import home, guide, disease_detection, nearby_hospitals

urlpatterns = [
    path('', home, name='home'),
    path('symptoms/', disease_detection, name='symptom'),
    path('find_hospital/', nearby_hospitals, name='find_hospital'),
    path('guide', guide, name='guide')
]
