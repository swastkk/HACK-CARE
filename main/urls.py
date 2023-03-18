from django.urls import path
from account.views import home
from .views import symptoms, nearby_hospitals

urlpatterns = [
    path('', home,  name='home'),
    path('symptoms', symptoms, name='symptom'),
    path('find_hospital', nearby_hospitals, name='find_hospital')
]
