from django.urls import path
from .views import symptoms, nearby_hospitals

urlpatterns = [
    path('symptoms/', symptoms, name='symptom'),
    path('find_hospital/', nearby_hospitals, name='find_hospital')
]
