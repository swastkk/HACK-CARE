from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def symptoms(request):
    return render(request, 'symptoms.html')

def find_hospital(request):
    return render(request, 'find_hospital.html')
