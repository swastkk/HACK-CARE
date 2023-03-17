from django.urls import path
from account.views import home
from .views import symptoms, find_hospital

urlpatterns = [
    path('', home,  name='home'),
    path('symptoms', symptoms, name='symptom'),
    path('find_hospital', find_hospital, name='find_hospital')
]
